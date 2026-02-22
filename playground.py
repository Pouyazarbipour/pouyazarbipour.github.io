import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, uniform, expon, binom, poisson, gamma, beta, t as student_t


def _pos(v, eps=1e-12):
    return float(v) if float(v) > eps else eps


DISTS = {
    "Normal": {
        "kind": "continuous",
        "params": [("mu", -5.0, 5.0, 0.1, 0.0), ("sigma", 0.1, 5.0, 0.1, 1.0)],
        "pdf": lambda x, p: norm.pdf(x, loc=p["mu"], scale=_pos(p["sigma"])),
        "latex": {
            "pdf": r"$f(x)=\frac{1}{\sigma\sqrt{2\pi}}\exp\!\left(-\frac{1}{2}\left(\frac{x-\mu}{\sigma}\right)^{2}\right)$",
            "ex":  r"$E[X]=\mu$",
            "var": r"$\mathrm{Var}[X]=\sigma^{2}$",
        },
        "default_xlim": (-6, 6),
    },
    "Uniform": {
        "kind": "continuous",
        "params": [("a", -5.0, 5.0, 0.1, 0.0), ("b", -5.0, 10.0, 0.1, 1.0)],
        "pdf": lambda x, p: uniform.pdf(x, loc=p["a"], scale=max(p["b"]-p["a"], 1e-9)),
        "latex": {
                "pdf": r"$f(x)=\frac{1}{b-a}\ \ (a<=x<=b)$",
            "ex":  r"$E[X]=\frac{a+b}{2}$",
            "var": r"$\mathrm{Var}[X]=\frac{(b-a)^{2}}{12}$",
        },
        "default_xlim": (-6, 11),
    },
    "Exponential (rate \u03bb)": {
        "kind": "continuous",
        "params": [("rate", 0.05, 5.0, 0.05, 1.0)],
        "pdf": lambda x, p: expon.pdf(x, scale=1.0/_pos(p["rate"])),
        "latex": {
            "pdf": r"$f(x)=\lambda e^{-\lambda x},\ x\geq 0$",
            "ex":  r"$E[X]=\frac{1}{\lambda}$",
            "var": r"$\mathrm{Var}[X]=\frac{1}{\lambda^{2}}$",
        },
        "default_xlim": (0, 10),
    },
    "Gamma": {
        "kind": "continuous",
        "params": [("k", 0.1, 10.0, 0.1, 2.0), ("theta", 0.05, 5.0, 0.05, 1.0)],
        "pdf": lambda x, p: gamma.pdf(x, a=_pos(p["k"]), scale=_pos(p["theta"])),
        "latex": {
            "pdf": r"$f(x)=\frac{x^{k-1}e^{-x/\theta}}{\Gamma(k)\,\theta^{k}},\ x\geq 0$",
            "ex":  r"$E[X]=k\theta$",
            "var": r"$\mathrm{Var}[X]=k\theta^{2}$",
        },
        "default_xlim": (0, 20),
    },
    "Beta": {
        "kind": "continuous",
        "params": [("alpha", 0.1, 10.0, 0.1, 2.0), ("beta", 0.1, 10.0, 0.1, 5.0)],
        "pdf": lambda x, p: beta.pdf(x, a=_pos(p["alpha"]), b=_pos(p["beta"])),
        "latex": {
                "pdf": r"$f(x)=\frac{x^{\alpha-1}(1-x)^{\beta-1}}{B(\alpha,\beta)},\ 0<=x<=1$",
            "ex":  r"$E[X]=\frac{\alpha}{\alpha+\beta}$",
            "var": r"$\mathrm{Var}[X]=\frac{\alpha\beta}{(\alpha+\beta)^{2}(\alpha+\beta+1)}$",
        },
        "default_xlim": (0, 1),
    },
    "Student-t": {
        "kind": "continuous",
        "params": [("nu", 0.5, 40.0, 0.5, 5.0), ("loc", -5.0, 5.0, 0.1, 0.0), ("scale", 0.1, 5.0, 0.1, 1.0)],
        "pdf": lambda x, p: student_t.pdf((x-p["loc"])/_pos(p["scale"]), df=_pos(p["nu"]))/_pos(p["scale"]),
        "latex": {
            "pdf": r"$f(x)=\frac{\Gamma\left(\frac{\nu+1}{2}\right)}{\sqrt{\nu\pi}\,\Gamma\left(\frac{\nu}{2}\right)}\left(1+\frac{x^{2}}{\nu}\right)^{-\frac{\nu+1}{2}}$",
            "ex":  r"$E[X]=0\ \ (\nu>1)$",
            "var": r"$\mathrm{Var}[X]=\frac{\nu}{\nu-2}\ \ (\nu>2)$",
        },
        "default_xlim": (-10, 10),
    },
    "Poisson": {
        "kind": "discrete",
        "params": [("mu", 0.1, 40.0, 0.1, 5.0)],
        "pmf": lambda k, p: poisson.pmf(k, mu=_pos(p["mu"])),
        "latex": {
            "pdf": r"$P(X=k)=\frac{\mu^{k}e^{-\mu}}{k!}$",
            "ex":  r"$E[X]=\mu$",
            "var": r"$\mathrm{Var}[X]=\mu$",
        },
        "default_xlim": (0, 40),
    },
    "Binomial": {
        "kind": "discrete",
        "params": [("n", 1, 200, 1, 20), ("p", 0.0, 1.0, 0.01, 0.3)],
        "pmf": lambda k, p: binom.pmf(k, n=int(round(p["n"])), p=float(p["p"])),
        "latex": {
            "pdf": r"$P(X=k)=\binom{n}{k}p^{k}(1-p)^{\,n-k}$",
            "ex":  r"$E[X]=np$",
            "var": r"$\mathrm{Var}[X]=np(1-p)$",
        },
        "default_xlim": (0, 200),
    },
}

st.set_page_config(layout="wide", page_title="Distribution Playground")
st.title("Interactive Distribution Playground")

# Initialize session state for curves
if 'curves' not in st.session_state:
    st.session_state.curves = []

# Sidebar for controls
with st.sidebar:
    st.header("Add a New Curve")
    dist_name = st.selectbox("Choose a distribution:", list(DISTS.keys()))

    selected_dist = DISTS[dist_name]
    params = {}
    for pname, lo, hi, step, default in selected_dist["params"]:
        params[pname] = st.slider(pname, lo, hi, default, step)

    if st.button("Add Curve"):
        st.session_state.curves.append({
            "name": dist_name,
            "params": params
        })

    if st.button("Clear all curves"):
        st.session_state.curves = []

# Main content area
col1, col2 = st.columns([2, 1])

with col1:
    st.header("PDF / PMF Plot")
    fig, ax = plt.subplots()
    ax.set_title("PDF / PMF")
    ax.grid(True, alpha=0.3)
    ax.set_autoscale_on(True)

    default_xlim = (-6, 6)
    if st.session_state.curves:
        # Determine combined x-range for all curves
        all_xlims = [DISTS[curve["name"]]["default_xlim"]
                     for curve in st.session_state.curves]
        min_x = min([x[0] for x in all_xlims])
        max_x = max([x[1] for x in all_xlims])
        default_xlim = (min_x, max_x)

    ax.set_xlim(default_xlim)

    if st.session_state.curves:
        for curve in st.session_state.curves:
            name = curve["name"]
            params = curve["params"]
            current_dist = DISTS[name]

            x_min, x_max = ax.get_xlim()
            x_vals = np.linspace(x_min, x_max, 1000)

            if current_dist["kind"] == "continuous":
                y_vals = current_dist["pdf"](x_vals, params)
                ax.plot(x_vals, y_vals, label=f"{name} {params}")
            else:
                k_vals = np.arange(
                    max(0, int(np.floor(x_min))), int(np.ceil(x_max)) + 1)
                y_vals = current_dist["pmf"](k_vals, params)
                ax.stem(k_vals, y_vals, label=f"{name} {params}")

    ax.legend(loc="best")
    st.pyplot(fig)

with col2:
    st.header("Formulas")
    if selected_dist:
        latex_text = f"""
        **Distribution:** {dist_name}
        
        **PDF/PMF:**
        {selected_dist['latex']['pdf']}
        
        **Expected Value ($E[X]$):**
        {selected_dist['latex']['ex']}
        
        **Variance ($Var[X]$):**
        {selected_dist['latex']['var']}
        """
        st.markdown(latex_text, unsafe_allow_html=True)

    st.header("Currently Plotted Curves")
    if st.session_state.curves:
        for i, curve in enumerate(st.session_state.curves):
            st.markdown(f"**Curve {i+1}:** {curve['name']}")
            st.json(curve["params"])
    else:
        st.info("No curves have been added yet.")
