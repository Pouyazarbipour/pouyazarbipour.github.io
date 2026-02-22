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
    "Exponential (rate λ)": {
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

st.set_page_config(
    layout="wide", 
    page_title="Distribution Playground",
    page_icon="📊",
    initial_sidebar_state="expanded"
)

st.title("📊 Interactive Distribution Playground")
st.markdown("""
Explore probability distributions interactively! Add multiple curves, adjust parameters in real-time, 
and see how different distributions behave. Perfect for understanding statistical concepts and 
visualizing probability density functions (PDFs) and probability mass functions (PMFs).
""")

# Compact spacing for controls
st.markdown(
    """
    <style>
    /* Tighten global spacing a bit */
    .stSlider > div { margin-bottom: 0.25rem; }
    .stMarkdown p { margin-bottom: 0.35rem; }
    .stTabs [data-baseweb="tab-list"] { margin-bottom: 0.35rem; }
    hr { margin: 0.35rem 0; }
    /* Compact controls and captions */
    .compact-row .stSlider { padding-bottom: 0.15rem; }
    .compact-row .stCaption, .compact-row .st-emotion-cache-16idsys p { margin: 0.15rem 0; }
    .compact-row .stButton>button { padding: 0.25rem 0.6rem; margin-top: 0.25rem; }
    /* Curve block header and button */
    .curve-block .curve-title { margin: 0 0 0.05rem 0; }
    .curve-block .stButton>button { white-space: nowrap; padding: 0.15rem 0.8rem; min-width: 170px; height: 30px; line-height: 1; font-size: 0.9rem; }
    .curve-block { margin-bottom: 0.25rem; }
    /* Reduce column/gap around sliders inside each curve block */
    .curve-block [data-testid="stHorizontalBlock"] { gap: 0.5rem; margin-top: 0.1rem; margin-bottom: 0.1rem; }
    .curve-block .stSlider > div { margin-top: 0.05rem; margin-bottom: 0.05rem; }
    .curve-block label { margin-bottom: 0.1rem; }
    /* Reduce extra space after the curve title markdown */
    .curve-block [data-testid="stMarkdownContainer"] p { margin-bottom: 0.1rem; }
    /* Tighten vertical blocks that may add spacing */
    .curve-block [data-testid="stVerticalBlock"] { gap: 0.15rem; margin-top: 0.05rem; margin-bottom: 0.05rem; }
    /* Right panel scroll area - boxed container applied to the second column of main content */
    section.main div[data-testid="stHorizontalBlock"] > div:nth-child(2) > div:first-child {
      position: sticky;
      top: 0.25rem;
      max-height: calc(100vh - 0.75rem);
      overflow-y: auto;
      padding: 0.75rem;
      border: 1px solid #e6e6e6;
      border-radius: 8px;
      background-color: #fafafa;
      box-shadow: 0 1px 2px rgba(0,0,0,0.04);
    }
    /* Subtle custom scrollbar */
    section.main div[data-testid="stHorizontalBlock"] > div:nth-child(2) > div:first-child::-webkit-scrollbar { width: 8px; }
    section.main div[data-testid="stHorizontalBlock"] > div:nth-child(2) > div:first-child::-webkit-scrollbar-thumb { background: #d1d1d1; border-radius: 6px; }
    </style>
    """,
    unsafe_allow_html=True,
)

# Initialize session state for curves and axis settings
if 'curves' not in st.session_state:
    st.session_state.curves = []
if 'axis_settings' not in st.session_state:
    st.session_state.axis_settings = {
        'lock_axes': False,
        'x_min': -6.0,
        'x_max': 6.0,
        'y_min': 0.0,
        'y_max': 1.0
    }

# Sidebar for controls
with st.sidebar:
    st.header("🎛️ Add a New Curve")
    dist_name = st.selectbox("Choose a distribution:", list(DISTS.keys()))

    col1, col2 = st.columns(2)
    with col1:
        if st.button("➕ Add Curve", type="primary"):
            # Use default parameters for the selected distribution
            selected_dist = DISTS[dist_name]
            default_params = {}
            for pname, lo, hi, step, default in selected_dist["params"]:
                default_params[pname] = default
            
            st.session_state.curves.append({
                "name": dist_name,
                "params": default_params
            })
            st.rerun()
    
    with col2:
        if st.button("🗑️ Clear All"):
            st.session_state.curves = []
            st.rerun()
    
    st.markdown("---")
    st.markdown("**💡 Tip:** Add curves with default parameters, then use the sliders in the 'Currently Plotted Curves' section to modify them!")

# Main content area. Make right panel scrollable by applying an id and using sticky positioning.
col1, col2 = st.columns([2, 1])

with col1:
    st.header("📈 PDF / PMF Plot")
    
    # Axis control options
    col_axis1, col_axis2, col_axis3, col_axis4 = st.columns(4)
    with col_axis1:
        lock_axes = st.checkbox("🔒 Lock Axes", 
                               value=st.session_state.axis_settings['lock_axes'], 
                               help="Lock axis ranges to prevent auto-scaling")
        if lock_axes != st.session_state.axis_settings['lock_axes']:
            st.session_state.axis_settings['lock_axes'] = lock_axes
    
    with col_axis2:
        if lock_axes:
            x_min = st.number_input("X Min", 
                                   value=st.session_state.axis_settings['x_min'], 
                                   step=0.5, key="x_min")
            x_max = st.number_input("X Max", 
                                   value=st.session_state.axis_settings['x_max'], 
                                   step=0.5, key="x_max")
            if x_min != st.session_state.axis_settings['x_min']:
                st.session_state.axis_settings['x_min'] = x_min
            if x_max != st.session_state.axis_settings['x_max']:
                st.session_state.axis_settings['x_max'] = x_max
        else:
            st.info("Auto-scaling enabled")
    
    with col_axis3:
        if lock_axes:
            y_min = st.number_input("Y Min", 
                                   value=st.session_state.axis_settings['y_min'], 
                                   step=0.1, key="y_min")
            y_max = st.number_input("Y Max", 
                                   value=st.session_state.axis_settings['y_max'], 
                                   step=0.1, key="y_max")
            if y_min != st.session_state.axis_settings['y_min']:
                st.session_state.axis_settings['y_min'] = y_min
            if y_max != st.session_state.axis_settings['y_max']:
                st.session_state.axis_settings['y_max'] = y_max
        else:
            st.info("Auto-scaling enabled")
    
    with col_axis4:
        if st.button("🔄 Reset View", help="Reset plot to default view"):
            st.session_state.axis_settings = {
                'lock_axes': False,
                'x_min': -6.0,
                'x_max': 6.0,
                'y_min': 0.0,
                'y_max': 1.0
            }
            st.rerun()
    
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_title("Probability Density/Mass Function", fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3)
    
    # Set axis limits based on user choice
    if lock_axes:
        ax.set_xlim(st.session_state.axis_settings['x_min'], st.session_state.axis_settings['x_max'])
        ax.set_ylim(st.session_state.axis_settings['y_min'], st.session_state.axis_settings['y_max'])
        ax.set_autoscale_on(False)
    else:
        ax.set_autoscale_on(True)
        # Auto-determine x-range if not locked
        default_xlim = (-6, 6)
        if st.session_state.curves:
            all_xlims = [DISTS[curve["name"]]["default_xlim"]
                         for curve in st.session_state.curves]
            min_x = min([x[0] for x in all_xlims])
            max_x = max([x[1] for x in all_xlims])
            default_xlim = (min_x, max_x)
        ax.set_xlim(default_xlim)

    if st.session_state.curves:
        colors = plt.cm.tab10(np.linspace(0, 1, len(st.session_state.curves)))
        for i, curve in enumerate(st.session_state.curves):
            name = curve["name"]
            params = curve["params"]
            current_dist = DISTS[name]

            # Build safe parameters by merging with defaults to avoid KeyError
            safe_params = {}
            for pname, lo, hi, step, default in current_dist.get("params", []):
                safe_params[pname] = params.get(pname, default)

            x_min, x_max = ax.get_xlim()
            x_vals = np.linspace(x_min, x_max, 1000)

            if current_dist["kind"] == "continuous":
                y_vals = current_dist["pdf"](x_vals, safe_params)
                ax.plot(x_vals, y_vals, label=f"{name} {safe_params}", color=colors[i], linewidth=2)
            else:
                k_vals = np.arange(
                    max(0, int(np.floor(x_min))), int(np.ceil(x_max)) + 1)
                y_vals = current_dist["pmf"](k_vals, safe_params)
                ax.stem(k_vals, y_vals, label=f"{name} {safe_params}", basefmt=" ", linefmt=colors[i], markerfmt=f'o{colors[i]}')

        # If axes are locked, make absolutely sure y-limits do not autoscale
        if st.session_state.axis_settings['lock_axes']:
            ax.autoscale(enable=False, axis='y')
            ax.set_ylim(
                st.session_state.axis_settings['y_min'],
                st.session_state.axis_settings['y_max']
            )

    if st.session_state.curves:
        ax.legend(loc="best", fontsize=10)
    ax.set_xlabel("x", fontsize=12)
    ax.set_ylabel("f(x) or P(X=x)", fontsize=12)
    
    # Enable interactive features
    plt.tight_layout()
    
    # Add interactive controls info
    st.markdown("""
    **🖱️ Interactive Controls:**
    - **Zoom:** Mouse wheel or right-click + drag
    - **Pan:** Left-click + drag to move around
    - **Reset:** Double-click to reset view or use "Reset View" button
    - **Lock Axes:** Use checkbox above to prevent auto-scaling
    - **Manual Axis Control:** Set custom X and Y ranges when axes are locked
    """)
    
    st.pyplot(fig)

with col2:
    # Wrap right panel in a container with an id for sticky/scroll styles
    st.markdown("<div id='right-panel'>", unsafe_allow_html=True)
    st.header("📚 Plotted Curves Info")

    if st.session_state.curves:
        # Group by distribution
        grouped = {}
        for idx, curve in enumerate(st.session_state.curves):
            grouped.setdefault(curve['name'], []).append((idx, curve))

        tab_labels = [f"{name} ({len(items)})" for name, items in grouped.items()]
        tabs = st.tabs(tab_labels)

        for (name, items), tab in zip(grouped.items(), tabs):
            with tab:
                latex = DISTS[name]['latex']
                st.markdown("**Mathematical Properties (generic):**")
                pdf_expr = latex['pdf'].strip('$')
                ex_expr = latex['ex'].strip('$')
                var_expr = latex['var'].strip('$')
                st.markdown("PDF/PMF:")
                st.markdown(f"$$\\normalsize {pdf_expr} $$")
                # Render Expected Value and Variance in one row
                c1, c2 = st.columns(2)
                with c1:
                    st.markdown("Expected Value:")
                    st.markdown(f"$$\\normalsize {ex_expr} $$")
                with c2:
                    st.markdown("Variance:")
                    st.markdown(f"$$\\normalsize {var_expr} $$")

                st.markdown("---")
                st.markdown("**Curves of this type:**")

                for i, (idx, curve) in enumerate(items, start=1):
                    st.markdown("<div class='curve-block'>", unsafe_allow_html=True)
                    header_col, btn_col = st.columns([7, 3])
                    with header_col:
                        st.markdown(f"<div class='curve-title'><strong>Curve {idx+1}</strong></div>", unsafe_allow_html=True)
                    with btn_col:
                        if st.button("🗑️ Delete", key=f"delete_{name}_{idx}"):
                            st.session_state.curves.pop(idx)
                            st.rerun()
                    st.markdown("<div class='compact-row'>", unsafe_allow_html=True)
                    dist_info = DISTS[name]
                    new_params = {}
                    params_list = dist_info['params']
                    # Render up to 2 sliders per row for compact layout
                    for start in range(0, len(params_list), 2):
                        row_params = params_list[start:start+2]
                        cols = st.columns(len(row_params))
                        for (pdef, col) in zip(row_params, cols):
                            pname, lo, hi, step, default = pdef
                            label = pname
                            if pname == 'mu':
                                label = 'μ'
                            elif pname == 'sigma':
                                label = 'σ'
                            elif pname == 'alpha':
                                label = 'α'
                            elif pname == 'beta':
                                label = 'β'
                            elif pname == 'nu':
                                label = 'ν'
                            with col:
                                current_value = curve['params'].get(pname, default)
                                new_value = st.slider(
                                    f"{label}", lo, hi, current_value, step,
                                    key=f"tab_{name}_curve_{idx}_{pname}"
                                )
                                new_params[pname] = new_value

                    if new_params != curve['params']:
                        st.session_state.curves[idx]['params'] = new_params
                        st.rerun()

                    # Brief numeric properties
                    if name == 'Normal':
                        mu, sigma = new_params['mu'], new_params['sigma']
                        st.caption(f"E[X]={mu:.2f}, Var[X]={sigma**2:.2f}")
                    elif name == 'Uniform':
                        a, b = new_params['a'], new_params['b']
                        st.caption(f"E[X]={((a+b)/2):.2f}, Var[X]={((b-a)**2/12):.2f}")
                    elif name == 'Exponential (rate λ)':
                        rate = new_params['rate']
                        st.caption(f"E[X]={1/rate:.2f}, Var[X]={1/(rate**2):.2f}")
                    elif name == 'Gamma':
                        k, theta = new_params['k'], new_params['theta']
                        st.caption(f"E[X]={k*theta:.2f}, Var[X]={k*theta**2:.2f}")
                    elif name == 'Beta':
                        a, b = new_params['alpha'], new_params['beta']
                        st.caption(f"E[X]={a/(a+b):.2f}, Var[X]={a*b/((a+b)**2*(a+b+1)):.2f}")
                    elif name == 'Student-t':
                        nu, loc, scale = new_params['nu'], new_params['loc'], new_params['scale']
                        mean_txt = f"{loc:.2f}" if nu > 1 else "undefined"
                        var_txt = f"{(nu/(nu-2) * scale**2):.2f}" if nu > 2 else "undefined"
                        st.caption(f"E[X]={mean_txt}, Var[X]={var_txt}")
                    elif name == 'Poisson':
                        mu = new_params['mu']
                        st.caption(f"E[X]={mu:.2f}, Var[X]={mu:.2f}")
                    elif name == 'Binomial':
                        n, p = int(new_params['n']), new_params['p']
                        st.caption(f"E[X]={n*p:.2f}, Var[X]={n*p*(1-p):.2f}")

                    st.markdown("</div></div>", unsafe_allow_html=True)
    else:
        st.info("No curves have been added yet. Use the sidebar to add your first distribution!")
    st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
**How to use:**
1. Select a distribution from the dropdown in the sidebar
2. Click "Add Curve" to add it with default parameters
3. Use the sliders in each curve's section to modify parameters in real-time
4. Add multiple distributions to compare them
5. Delete individual curves or clear all to start over

**Tips:**
- Each curve has its own sliders for real-time parameter adjustment
- Try comparing Normal distributions with different means and variances
- Explore how the Beta distribution changes shape with different α and β parameters
- Compare discrete distributions like Poisson and Binomial
- Notice how the Student-t distribution approaches Normal as degrees of freedom increase
- Use the delete button to remove specific curves you don't want
""")
