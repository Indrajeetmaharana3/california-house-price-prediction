
# 🏠 House Price Prediction Using Machine Learning



## 📌 Project Overview

This project predicts median house values in California using Machine Learning regression algorithms. It includes exploratory data analysis (EDA), feature engineering, model comparison, evaluation, and an interactive Streamlit web application.

The goal is to build a reusable machine learning pipeline that predicts house values from housing and location-related features.

## 🎯 Objectives

* Explore and analyze the California Housing dataset.
* Perform data preprocessing and exploratory data analysis.
* Create new features using feature engineering.
* Train and compare multiple regression models.
* Evaluate model performance using MAE, RMSE, and R².
* Save the best-performing model.
* Build an interactive application using Streamlit.

## 📊 Dataset

**Dataset:** California Housing dataset from Scikit-learn.

* Total records: 20,640
* Original input features: 8
* Target variable: `<span>MedHouseVal</span>`
* Training data: 80%
* Testing data: 20%

The target represents median house value in units of $100,000.

## 🛠️ Technologies Used

* Python
* Pandas and NumPy
* Matplotlib and Seaborn
* Scikit-learn
* Joblib
* Streamlit
* Jupyter Notebook

## 🤖 Machine Learning Models

The following regression algorithms were trained and compared:

1. Linear Regression
2. Random Forest Regressor
3. Gradient Boosting Regressor

### Model Evaluation

| Model             | MAE    | RMSE   | R² Score |
| ----------------- | ------ | ------ | --------- |
| Linear Regression | 0.5261 | 0.7292 | 0.5942    |
| Random Forest     | 0.3278 | 0.5054 | 0.8051    |
| Gradient Boosting | 0.3675 | 0.5378 | 0.7793    |

**Best-performing model:** Random Forest Regressor

Random Forest achieved the lowest MAE and RMSE and the highest R² score among the three tested models.

*Note: These are the evaluation results from the current train/test split. The target values are measured in units of $100,000.*

## ⚙️ Feature Engineering

A new feature, `<span>BedroomsPerRoom</span>`, was created using:

`<span>BedroomsPerRoom = AveBedrms / AveRooms</span>`

Feature engineering is included in the reusable pipeline so the same transformation is applied during training and prediction.


## 📁 Project Structure

```text
House_Price_Prediction/
├── app/
│   └── app.py
├── data/
├── models/
│   └── best_house_price_model.pkl
├── notebooks/
│   ├── 01_data_understanding.ipynb
│   ├── 02_data_preprocessing.ipynb
│   └── 03_model_training.ipynb
├── src/
│   └── feature_engineering.py
├── requirements.txt
└── README.md
```



🚀 Installation and Setup

1. Clone the repository

```shell
git clone https://github.com/Indrajeetmaharana3/california-house-price-prediction.git
cd california-house-price-prediction
```

2. Create a virtual environment

python -m venv .venv

3. Activate the environment

Windows PowerShell:

.\.venv\Scripts\Activate.ps1

4. Install dependencies

python -m pip install -r requirements.txt

5. Run the Streamlit application

streamlit run app/app.py

The application will open in your browser. Enter the housing details and click Predict House Price to see the estimated value.

💾 Trained Model

The selected model is saved at:

models/best_house_price_model.pkl

The model includes feature engineering and the trained Random Forest estimator.

Important: Ensure the saved model file is included in your repository if you want the app to run immediately after cloning. Otherwise, provide instructions for generating it by running the training notebook.

📈 Evaluation Metrics

MAE (Mean Absolute Error): Average absolute difference between actual and predicted values.

RMSE (Root Mean Squared Error): Penalizes larger prediction errors more heavily.

R² Score: Measures how much variation in the target is explained by the model.

Lower MAE and RMSE are better; a higher R² score is generally better.

🔮 Future Improvements

Add cross-validation and hyperparameter tuning.

Improve feature selection and feature engineering.

Add interactive visualizations to the Streamlit app.

Deploy the application online.

Add automated tests for the preprocessing pipeline and predictions.

👨‍💻 Author

**Indrajeet Maharana**

* GitHub: [@Indrajeetmaharana3](https://github.com/Indrajeetmaharana3)
* Project: [California House Price Prediction](https://github.com/Indrajeetmaharana3/california-house-price-prediction)

Aspiring Machine Learning Engineer | Python | NumPy | Pandas | Scikit-learn | Machine Learning

📄 License

Choose and add an appropriate open-source license before distributing the project.
