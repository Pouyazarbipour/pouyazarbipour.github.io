---
layout: archive
title: "Programming & Software"
permalink: /Programming/
author_profile: true
redirect_from:
  - /resume
---
{% include base_path %}

You can see all my programming projects on my **[GitHub page](https://github.com/Pouyazarbipour)** (21 public repositories).

## Developed Software Tools for Coastal Engineering Applications
**Dec. 2021 – Present**

I have developed **more than 10 Python-based tools** (plus several MATLAB GUI applications) for coastal, ocean, and water engineering. These tools integrate machine learning, deep learning, uncertainty quantification (UQ), causal inference, physics-informed neural networks (PINN), and quantum machine learning with real-world hydrodynamic and structural problems.

### Advanced Python & ML Tools (Key Highlights)

**The XGBoost Berm Breakwater Recession Prediction Tool**  
[Repository](https://github.com/Pouyazarbipour/The-XG-Boost-Berm-Breakwater-Recession-Prediction-tools)  
A web-based application using **XGBoost** (with Optuna hyperparameter tuning) for highly accurate prediction of berm breakwater recession (Rec/Dₙ₅₀). Achieves R² = 0.99 (training) / 0.97 (testing). Includes **bootstrap-based uncertainty quantification** (95% confidence interval and upper-bound conservative estimate).  
**Input parameters** (dimensionless): H₀√T₀p, H₀, f₉, h/Dₙ₅₀, h_b/H_s.  
**Features**: Full GUI, downloadable executable, User & Technical Manual. Directly supports the paper “Accurate Prediction of Berm Breakwater Recession Using XGBoost-Optuna” (Under Review).

**The Quantum SVM Wave Overtopping Prediction Tool**  
[Repository](https://github.com/Pouyazarbipour/The-Quantum-SVM-Wave-Overtopping-Prediction-tool)  
Desktop application (Windows .exe + macOS .dmg) using **quantum machine learning** (variational quantum classifier adapted for regression) on the CLASH database. Predicts average wave overtopping discharge (q) with R² = 0.97.  
**13 input parameters** including wave height, period, structure geometry, roughness, and freeboard.  
**Features**: Quantum Monte Carlo sampling for **aleatoric + epistemic uncertainty quantification** (95% CI and upper-bound prediction). Standalone, no internet required. References the 2026 Ocean Engineering paper on quantum ML for wave overtopping.

**The Physics-Informed UQ SWAN Surrogate Wave Prediction Tool**  
[Repository](https://github.com/Pouyazarbipour/The-Physics-Informed-UQ-SWAN-Surrogate-Wave-Prediction-Tool)  
Standalone scientific software for ultra-fast spatial prediction of SWAN wave parameters (Hs, Tp, Dir) over 2D grids. Hybrid **PINN + CNN** architecture with physics constraints (dispersion, refraction, shoaling).  
**Features**: Monte Carlo Dropout for full **aleatoric and epistemic uncertainty** maps. Orders-of-magnitude faster than full SWAN simulations. Includes GUI and pretrained model for Salalah coastal domain. Supports the 2026 paper “Hybrid PINN-UQ Surrogate for Spatial Reconstruction of SWAN Wave Parameters”.

**The Physics-Informed UQ Overtopping Prediction Tool**  
[Repository](https://github.com/Pouyazarbipour/The-Physics-Informed-UQ-Overtopping-Prediction-Tool)  
Advanced Python tool implementing causal-aware physics-informed neural surrogate with aleatoric and epistemic uncertainty for wave overtopping prediction (directly supports the 2026 manuscript “Causal-Aware Physics-Informed Neural Surrogate...”).

**Other Python Tools**  
- Coastal Vertical Structures Designer  
- GEE_Bath_Oman (Google Earth Engine bathymetry processor for Oman coast)  
- ML-based tool for prediction of effective fixed-base level (soil-structure interaction)  
- Depth Data Extractor from NetCDF files (geospatial processing)

### MATLAB GUI Tools for Coastal & Marine Engineering

**Newmark Method in Marine Structures GUI**  
[Repository](https://github.com/Pouyazarbipour/Newmark-method-in-Marine-structures)  
Simulates displacement and velocity of marine structures under wave forces using the Newmark-β method. Real-time plotting and error handling.

**Earthquake Acceleration Response Spectrum GUI**  
[Repository](https://github.com/Pouyazarbipour/Earthquake-Acceleration-Response-Spectrum-Generation)  
Generates acceleration response spectrum according to **API RP 2WSD 2014**. Supports soil types A/B/C and exports to .txt.

**Sediment Transport Calculator GUI**  
[Repository](https://github.com/Pouyazarbipour/Sediment-Transport-Calculator)  
Computes sediment transport rates using common coastal engineering formulas (CERC, Kamphuis, etc.).

**Groin Simulation GUI**  
[Repository](https://github.com/Pouyazarbipour/Groin-Simulation-GUI)  
One-line contour model simulating shoreline evolution, sand deposition/erosion, and bypassing around a groin.

**Beach Simulation GUI Model**  
[Repository](https://github.com/Pouyazarbipour/Beach-Simulation-GUI)  
Analyzes native vs. nourished beach profiles, calculates volume, closure depth, and maximum extent.

**Inlet Tide Calculator GUI**  
[Repository](https://github.com/Pouyazarbipour/Inlet-Tide-Calculator-App)  
Keulegan’s method + Runge-Kutta 4th order for tidal dynamics in lagoons/bays. Plots ocean vs. bay tide with phase lag and repletion coefficient.

**Wave Calculator GUI**  
[Repository](https://github.com/Pouyazarbipour/WaveCalculator)  
Comprehensive linear wave theory calculator (L, k, C, Cg, Ks, Kr, ub, etc.) with full input validation and reset function.

**Extract Underwater Depth Data from NetCDF Files**  
[Repository](https://github.com/Pouyazarbipour/Depth-Data-from-NetCDF-Files)  
Batch processing of bathymetry NetCDF files to extract and save underwater points (lat/lon/depth).

**Linear Wave Kinematics Simulation GUI**  
[Repository](https://github.com/Pouyazarbipour/Linear-wave-Simulation)  
Real-time animated simulation of linear wave motion with stop button and input validation.

**EdgeTheory – Wave Simulation GUI**  
[Repository](https://github.com/Pouyazarbipour/EdgeTheory)  
Simulates wave propagation over sloping bathymetry using EdgeWave theory (up to 3 modes).

All tools are open-source (MIT license) and include user manuals where applicable. Source code, executables, and documentation are available on GitHub and my personal website.
