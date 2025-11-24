---
layout: archive
title: "Programming & Software"
permalink: /Programming/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

You can see my completed programming on my [GitHub page](https://github.com/Pouyazarbipour).

## [Newmark Method in Marine Structures GUI](https://github.com/Pouyazarbipour/Newmark-method-in-Marine-structures)

This MATLAB GUI application simulates and visualizes the displacement and velocity of a system (like a Marine structure) subjected to wave forces using the Newmark method. The GUI allows users to input various parameters, run the simulation, and view the results in graphical form.
- Input fields for key parameters such as wave length, wave height, water depth, drag coefficient, and more.
- Real-time simulation of displacement and velocity based on the Newmark method.
- Dynamic plotting of displacement and velocity against time.
- Basic error handling for incorrect input types.

## [Earthquake Acceleration Response Spectrum GUI](https://github.com/Pouyazarbipour/Earthquake-acceleration-response-spectrum-GUI)

This MATLAB GUI application generates an **Acceleration Response Spectrum** based on the **API RP 2WSD 2014** standard. The tool allows users to input soil type and coefficient values to compute and visualize the response spectrum.
- **Input parameters:**
    - Coefficient (G)
    - Soil Type (A, B, C)
- Plots the **Spectral Acceleration vs. Period** graph.
- Exports spectrum data to a `.txt` file.
- Simple and user-friendly interface.

## [Sediment Transport Calculator GUI](https://github.com/Pouyazarbipour/Sediment-Transport-Calculator)

The **Sediment Transport Calculator** is a MATLAB-based graphical user interface (GUI) application designed to compute sediment transport rates using common coastal engineering equations. This tool is useful for researchers, engineers, and students working in coastal engineering and sediment transport studies.

## [Groin Simulation GUI](https://github.com/Pouyazarbipour/Groin-Simulation-GUI)

This MATLAB app simulates the deposition of sand on the updrift side and the erosion of sand on the downdrift side of a groin. The simulation uses a one-line contour model to calculate and visualize shoreline evolution over time.
- **Deposition & Erosion Modeling:** Simulates the deposition of sand on the updrift side and erosion on the downdrift side of a groin.
- **Dynamic Visualization:** Displays the shoreline evolution and real-time sediment transport (Q) as the simulation progresses.
- **Groin Influence:** Calculates the critical distance (`xm`) and when the groin starts bypassing sand (i.e., when the groin reaches its capacity).

## [Beach Simulation GUI Model](https://github.com/Pouyazarbipour/Beach-Simulation-Project)

This MATLAB project provides a simulation tool to analyze and visualize beach profiles under native and filled conditions. The model calculates key beach metrics, including depth, volume, and maximum profile extent, based on user-defined input parameters. It is particularly useful for coastal engineering applications such as beach nourishment design and sediment transport studies.
- Simulates native and filled beach profiles.
- Computes beach volume and maximum horizontal extent.
- Provides customizable input parameters for grain size, berm height, and closure depth.
- Visualizes native and filled beach profiles with clear, labeled plots.
- Outputs key metrics to the MATLAB console.

## [Inlet Tide Calculator GUI](https://github.com/Pouyazarbipour/Inlet-Tide-Calculator-App)

The **Inlet Tide Calculator** is a MATLAB-based graphical user interface (GUI) designed to simulate the tidal dynamics of a lagoon or bay connected to the ocean through an inlet. The app calculates the bay's tide response, considering factors such as inlet geometry, energy losses, and tidal propagation time. It uses **Keulegan's method** and the **Runge-Kutta 4th order integration** to solve for the tidal dynamics and visualize the results.
- **Tidal Wave Calculation**: Computes the tidal response in a bay, considering inlet geometry and energy losses.
- **Graphical User Interface**: Interactive GUI to input parameters and view results.
- **Visualization**: Plots both ocean and bay tides with corresponding phase lag.
- **Results Display**: Displays the repletion coefficient (K), phase lag (in degrees), and response ratio of the bay tide to the ocean tide.

## [Wave Calculator GUI](https://github.com/Pouyazarbipour/WaveCalculator)

The **Wave Calculator GUI** is a MATLAB-based GUI tool designed to compute various wave parameters such as wave length, wave speed, wave height, and others based on user-provided inputs. The tool provides an interactive interface for entering wave properties and displays calculated results dynamically. This application is useful for students, researchers, and engineers working in fields such as oceanography, coastal engineering, and marine structures. 

- **Interactive GUI**:  
  A user-friendly interface with input fields, dropdown menus, and buttons for calculations.  

- **Customizable Inputs**:  
  Enter wave height, period or frequency, wave angle, and local water depth.  

- **Calculated Parameters**:  
  - Wave length (`L`)  
  - Wave number (`k`)  
  - Wave speed (`C`)  
  - Group velocity (`Cg`)  
  - Shoaling coefficient (`Ks`)  
  - Refraction coefficient (`Kr`)  
  - Resultant wave height (`H`)  
  - Bottom orbital velocity (`u_b`)
  - more Parameters

- **Error Handling**:  
  Input validation ensures that only valid numeric values are accepted. Errors are displayed via pop-up dialogs.  

- **Reset Functionality**:  
  Resets all inputs and outputs to their default values.  

## [Extract Underwater Depth Data from NetCDF Files](https://github.com/Pouyazarbipour/Depth-Data-from-NetCDF-Files)

This script processes **NetCDF (.nc)** files to extract longitude, latitude, and elevation data and saves the information about underwater points (where elevation is below sea level) into a plain text file.
- Reads geospatial data (latitude, longitude, elevation) from a NetCDF file.
- Identifies underwater points (negative elevation).
- Outputs results to a formatted text file (`depth.txt`).

## [Linear Wave Kinematics Simulation GUI](https://github.com/Pouyazarbipour/Linear-wave-Simulation)

Linear Wave Kinematics Simulation is a MATLAB-based graphical user interface (GUI) for simulating linear waves. The simulation allows users to input wave parameters (height, period, and depth), calculate the corresponding wavelength, and visualize the wave's motion over time. The GUI also includes a "Stop" button to halt the simulation. This tool is designed for researchers, students, and engineers interested in coastal and marine applications.
- **Wave Simulation**: Simulates linear waves based on user input for wave height, period, and local depth.
- **Real-time Visualization**: Displays a plot of the wave motion that updates in real time.
- **Input Validation**: Ensures that the input values are positive and within reasonable limits (e.g., wave height is adjusted if it exceeds 80% of the depth).
- **Interactive Controls**: Users can adjust parameters and start/stop the simulation via the GUI.

## [EdgeTheory - Wave Simulation GUI](https://github.com/Pouyazarbipour/EdgeTheory)

EdgeTheory is a MATLAB-based graphical user interface (GUI) for simulating wave propagation over sloping bathymetry. This tool is designed for researchers, students, and engineers interested in coastal and marine applications.
- Simulate wave profiles for up to three modes with decay factors based on seabed slope.
- Interactive GUI with user-defined input parameters:
  - **Wave Period (T)**: Time period of the waves (in seconds).
  - **Mean Slope**: Average slope of the seabed.
  - **Max Offshore Distance**: The farthest distance for the simulation.
- Real-time animated visualization of wave propagation.
- Simple and intuitive interface for easy use.

