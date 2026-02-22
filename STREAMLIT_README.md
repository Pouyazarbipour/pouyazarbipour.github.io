# Interactive Distribution Playground

A Streamlit web application for exploring probability distributions interactively. This tool allows you to visualize and compare different probability density functions (PDFs) and probability mass functions (PMFs) in real-time.

## Features

- **Interactive Parameter Adjustment**: Use sliders to adjust distribution parameters and see changes instantly
- **Multiple Distribution Support**: Compare up to 10 different distributions on the same plot
- **Mathematical Formulas**: View the mathematical expressions for PDF/PMF, expected value, and variance
- **Both Continuous and Discrete Distributions**: Support for both continuous (Normal, Uniform, Exponential, etc.) and discrete (Poisson, Binomial) distributions
- **Real-time Visualization**: Add and remove curves dynamically

## Supported Distributions

### Continuous Distributions
- **Normal**: Gaussian distribution with mean (μ) and standard deviation (σ)
- **Uniform**: Continuous uniform distribution between parameters a and b
- **Exponential**: Exponential distribution with rate parameter λ
- **Gamma**: Gamma distribution with shape (k) and scale (θ) parameters
- **Beta**: Beta distribution with shape parameters α and β
- **Student-t**: Student's t-distribution with degrees of freedom (ν), location, and scale

### Discrete Distributions
- **Poisson**: Poisson distribution with mean parameter μ
- **Binomial**: Binomial distribution with number of trials (n) and success probability (p)

## Installation

1. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Streamlit app:**
   ```bash
   streamlit run distribution_playground.py
   ```

3. **Open your browser** and navigate to the URL shown in the terminal (usually `http://localhost:8501`)

## Usage

1. **Select a Distribution**: Choose from the dropdown menu in the sidebar
2. **Adjust Parameters**: Use the sliders to modify distribution parameters
3. **Add to Plot**: Click "Add Curve" to add the distribution to the main plot
4. **Compare Distributions**: Add multiple curves to compare different distributions
5. **View Formulas**: Check the mathematical expressions in the right panel
6. **Clear Plot**: Use "Clear All" to remove all curves and start over

## Examples

### Comparing Normal Distributions
- Add a Normal distribution with μ=0, σ=1
- Add another Normal distribution with μ=2, σ=1.5
- Observe how the mean shifts the distribution and how variance affects the spread

### Exploring the Beta Distribution
- Try α=1, β=1 (uniform on [0,1])
- Try α=2, β=5 (skewed left)
- Try α=5, β=2 (skewed right)
- Notice how the shape changes dramatically with different parameters

### Discrete vs Continuous
- Add a Poisson distribution with μ=5
- Add a Normal distribution with μ=5, σ=2.2
- See how the Normal approximates the Poisson for large μ

## Technical Details

- Built with Streamlit for the web interface
- Uses NumPy and SciPy for statistical computations
- Matplotlib for plotting and visualization
- Session state management for maintaining multiple curves
- Responsive design with sidebar controls and main plotting area

## Requirements

- Python 3.7+
- Streamlit >= 1.28.0
- NumPy >= 1.24.0
- Matplotlib >= 3.7.0
- SciPy >= 1.11.0

## Deployment

This app can be deployed to various platforms:

- **Streamlit Cloud**: Upload to GitHub and deploy directly
- **Heroku**: Use the Procfile and requirements.txt
- **Docker**: Create a Dockerfile for containerized deployment
- **Local Server**: Run on your own server with proper port configuration

## Contributing

Feel free to add more distributions, improve the UI, or add new features like:
- Cumulative distribution function (CDF) plots
- Quantile-quantile (Q-Q) plots
- Statistical tests and comparisons
- Export functionality for plots
- More interactive features

## License

This project is open source and available under the MIT License.
