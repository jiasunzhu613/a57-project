# Ontario Air Pollution Trends

This project investigates long-term spatial and temporal trends of key air pollutants—**NO<sub>x</sub> (in ppb)**, **O<sub>3</sub> (in ppb)**, and **PM<sub>2.5</sub> (in µg/m³)**—in various Ontario cities from **2003 to 2022**. The analysis aims to understand how pollutant levels have changed over time, identify regions and years with peak concentrations, and model relationships among pollutants using statistical and machine learning techniques.

---

## Dataset Description

Each pollutant dataset contains the following fields:

- `Year`: Calendar year of measurement  
- `Station Number`: Unique monitoring station ID  
- `City` / `Location`: City and specific monitoring site  
- `Type`: Type of monitoring station or measurement protocol  
- `Valid Hour`: Number of valid hourly measurements  
- Percentiles: 10th, 30th, 50th, 70th, 90th, 99th  
- `Mean`: Annual average concentration  
- `1-Hour Maximum`, `24-Hour Maximum`: Peak concentrations over specific periods  

---

## Research Questions

1. How have annual mean concentrations changed from 2003 to 2022?
2. Which cities/regions consistently show high pollutant levels?
3. What correlations exist between NO<sub>x</sub>, O<sub>3</sub>, and PM<sub>2.5</sub>?
4. What are the projected trends in pollution based on current data?

---

## Code Summary (R)

### Data Processing
- Load and clean NO<sub>x</sub>, O<sub>3</sub>, and PM<sub>2.5</sub> datasets.
- Convert cities to Ontario regions via mapping.
- Remove non-numeric values and filter for years ≥ 2003.

### Tables
- **Top 10 Polluted Cities** for each pollutant.
- **Top 10 Region-Year Pairs** with highest pollution levels.
- **Top 10 Years** with peak mean pollutant concentrations.

### Visualizations
- **Line Charts**: Pollutant concentrations over time by region.
- **Scatter Plot**: Yearly overall mean pollutant levels.
- **Heatmaps**: Spatial pollutant distribution across Ontario cities.

### Statistical Analysis
- **Hypothesis Testing**: Paired t-test comparing pollutant levels in 2003 vs. 2022.
- **Bootstrapping**: Estimate 2022 mean pollutant levels with 95% confidence intervals.
- **Regression**: Log-linear model predicting NO<sub>x</sub> using year, PM<sub>2.5</sub>, and O<sub>3</sub>.
- **Cross-Validation**: 5-fold CV to validate PM<sub>2.5</sub> model (MSE ≈ 0.545).

---

## Key Findings

- **NO<sub>x</sub> and PM<sub>2.5</sub>** show significant declines since 2003.
- **O<sub>3</sub>** levels remain relatively stable due to complex atmospheric behavior.
- Urban and industrial regions (e.g., Toronto, Hamilton, Sarnia) report consistently high NO<sub>x</sub> and PM<sub>2.5</sub> levels.
- Regression and hypothesis testing confirm significant relationships among pollutants and temporal trends.

---

## Libraries Used

- `tidyverse`
- `readxl`
- `ggplot2`
- `lubridate`
- `sf`
- `viridis`
- `patchwork`, `cowplot`
- `kableExtra`, `stringr`, `gridExtra`, `purrr`

---

## Acknowledgements

- Data sourced from the **Ontario Ministry of the Environment, Conservation and Parks**.
- Project by: **Mohamad Damaj**, **Mohammad Anwar**, **Jonathan Zhu**

---

