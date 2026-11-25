# California Housing Prices Analysis and Prediction

## Project Overview
This project focuses on analyzing and predicting housing prices in California using a dataset containing features related to geographical, demographic, and economic factors. We carried out comprehensive data analysis, feature engineering, and data preparation to build a foundation for implementing machine learning models that can predict housing prices (`medianHouseValue`). This repository serves as a step-by-step guide for EDA, data preprocessing, and machine learning modeling.

---

## Table of Contents
- [Project Overview](#project-overview)
- [Dataset](#dataset)
- [Project Workflow](#project-workflow)
  - [1. Data Inspection](#1-data-inspection)
  - [2. Handling Missing Values](#2-handling-missing-values)
  - [3. Outlier Detection and Handling](#3-outlier-detection-and-handling)
  - [4. Feature Analysis and Correlation](#4-feature-analysis-and-correlation)
  - [5. Feature Engineering](#5-feature-engineering)
  - [6. Data Splitting](#6-data-splitting)
  - [7. Scaling and Normalization (Future Considerations)](#7-scaling-and-normalization-future-considerations)
  - [8. Implementing Machine Learning Models](#8-implementing-machine-learning-models)
- [Next Steps](#next-steps)

---

## Dataset
The dataset consists of the following features:
- **longitude**: Distance westward within California.
- **latitude**: Distance northward within California.
- **housingMedianAge**: Median age of houses in a block.
- **totalRooms**: Total number of rooms in a block.
- **totalBedrooms**: Total number of bedrooms in a block.
- **population**: Total population in a block.
- **households**: Total number of households in a block.
- **medianIncome**: Median income of households in a block (in tens of thousands of USD).
- **medianHouseValue**: Median house value for households in a block (in USD).
- **oceanProximity**: Location relative to the ocean (categorical).

---

## Project Workflow

### 1. Data Inspection
We started by inspecting the dataset using functions such as `head()`, `info()`, and `describe()` to gain an initial understanding of the data structure, data types, and presence of missing values.

### 2. Handling Missing Values
The `totalBedrooms` column contained 207 missing values. We explored different strategies to handle these missing values, including filling with median values, dropping rows, or using interpolation, based on the dataset’s context and impact analysis.

### 3. Outlier Detection and Handling
Using boxplots and statistical measures such as the Interquartile Range (IQR), we identified potential outliers in numerical columns. We made a deliberate decision to retain these outliers based on their significance in housing market analysis.

### 4. Feature Analysis and Correlation
We conducted correlation analysis using a heatmap to identify relationships among numerical features. We examined strong correlations with the target variable (`medianHouseValue`) and any multicollinearity among predictors. Key predictors such as `medianIncome` were highlighted for further consideration.

### 5. Feature Engineering
- Created potential new features such as `rooms_per_household` and `bedrooms_per_room` to capture meaningful relationships and enhance model performance.
- Categorical data handling focused on encoding the `oceanProximity` feature using techniques like one-hot encoding.

### 6. Data Splitting
The dataset was split into training and testing sets using `train_test_split` to ensure robust model evaluation and validation.

### 7. Scaling and Normalization (Future Considerations)
For algorithms sensitive to the scale of features (e.g., Linear Regression, KNN), we discussed normalization or standardization approaches. However, tree-based models do not necessarily require this step.

### 8. Implementing Machine Learning Models
- **Model Selection**: Plan to experiment with models such as Linear Regression, Decision Trees, Random Forest, Gradient Boosting Machines, etc.
- **Model Evaluation**: Evaluate model performance using metrics like Mean Absolute Error (MAE) and Root Mean Squared Error (RMSE).
- **Hyperparameter Tuning**: Use GridSearchCV or RandomizedSearchCV for model optimization.

---

## Next Steps
- Implement machine learning models to predict `medianHouseValue`.
- Perform hyperparameter tuning and cross-validation to ensure model robustness.
- Explore model interpretability techniques such as feature importance analysis and SHAP values.
- Further enhance features based on domain insights and observed patterns.

---

## Run it
```bash
git clone https://github.com/FaizanSSDQ/Data-Engineering-and-Visualization-Projects.git
cd Data-Engineering-and-Visualization-Projects/data-analysis/california-housing-prices
pip install -r requirements.txt
jupyter notebook California_Housing_Prices_DataAnalysis.ipynb
```

---
## 👤 About the Author

**Faizan Saleem Siddiqui**, Embedded Firmware Engineer | Research Scholar

Electronics engineer with 2+ years of experience in embedded systems and firmware development.
I build production firmware for **BLE wearables and biosignal devices** on Nordic nRF52 (Zephyr / nRF
Connect SDK), including **secure OTA updates (MCUboot, signed images)**, **low-power battery
management** and **true-wireless Bluetooth audio**. My background also covers STM32 and ESP32 with
FreeRTOS, real-time data acquisition, digital signal processing, industrial IoT, and Python tooling
for data, automation and machine learning.

- 🎓 MS Electronics, Quaid-i-Azam University, Islamabad (BS Electronics: 1st position, merit scholar)
- 🧑‍🏫 Former Visiting Faculty, Embedded Systems, and Research Assistant, Autonomous Vehicles (COMSIP Lab)
- 🌍 Open to embedded / firmware engineering opportunities worldwide

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Faizan%20Saleem%20Siddiqui-0A66C2?logo=linkedin&logoColor=white)](https://www.linkedin.com/in/faizan-saleem-siddiqui-4411bb247/)
[![GitHub](https://img.shields.io/badge/GitHub-FaizanSSDQ-181717?logo=github&logoColor=white)](https://github.com/FaizanSSDQ)
[![Email](https://img.shields.io/badge/Email-faizansaleemsdq%40gmail.com-D14836?logo=gmail&logoColor=white)](mailto:faizansaleemsdq@gmail.com)

Licensed under the [MIT License](../../LICENSE).
