# 🏠 House Price Prediction Project

This project uses a machine learning pipeline to predict house prices based on various features such as area, number of bedrooms, bathrooms, and more.

## 📂 Dataset

The dataset was obtained from [Kaggle](https://www.kaggle.com), containing housing details with features like:

* Area
* Bedrooms
* Bathrooms
* Stories
* Parking
* Main road access
* Guestroom availability
* Basement presence
* Hot water heating
* Air conditioning
* Furnishing status
* Preferred area

## ⚙️ Tools & Libraries

* Python
* Pandas
* NumPy
* scikit-learn
* Matplotlib
* Seaborn
* Jupyter Notebook

## 🧪 Model Workflow

1. **Data Cleaning**

   * Handled missing values
   * Categorical encoding using `OneHotEncoder`
2. **Feature Engineering**

   * Separated numerical and categorical features
   * Scaled numerical features
3. **Model Training**

   * Used `RandomForestRegressor` with pipeline and `ColumnTransformer`
   * Used `LinearRegression` with pipeline and `ColumnTransformer`

## 📊 Evaluation Metrics

For RandomForestRegressor model

* Mean Absolute Error (MAE): `1028242.7705`
* R² Score: `0.6108` on test data
* Training Score: `0.95` (indicates possible overfitting)

For LinearRegression model

Baseline mean Absolute Error: `1440702.92`

Mean Absolute Error (MAE): `1028242.7705`

R² Score: `0.6108` on test data

Training Score: `0.69`

Test Score: `0.65`

## 🔍 Results & Insights

* The model performs reasonably well with an R² score above 0.6.
* Tuning didn’t significantly outperform the baseline model, suggesting feature limitations.
* Top predictors likely include area and number of rooms.

## 🚀 How to Run

```bash
# Clone the repo
git clone https://github.com/SamJcloud/house-price-prediction.git
cd house-price-prediction

# Create virtual environment (optional)
python -m venv env
source env/bin/activate  # or env\Scripts\activate on Windows

# Launch Jupyter
jupyter notebook
```
