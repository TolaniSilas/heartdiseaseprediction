# Import the necessary modules and libraries.
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import xgboost as xgb


# Read the dataset file.
data = pd.read_csv('new_heart_data.csv')
# Drop the mentioned not needed columns.
data = data.drop(["Unnamed: 0", "target"], axis=1)

# Seperate the feature and the target variable.
features= data.drop(["presence"], axis=1)
target = data.presence

# Get both the categorical and numerical columns name.
categorical_columns = ["sex", "chest_pain", "fasting_blood_sugar", "restecg", "exercise_induced_angina", "st_slope", "colored_by_fluoroscopy", "thallium_stress_test"]
numerical_columns = [col for col in features.columns if col not in categorical_columns]

# Get both the categorical and numerical columns in feature_cat and feature_num respectively.
feature_categorical = features[categorical_columns]
feature_numerical = features[numerical_columns]

# Instantiate the StandardScaler class.
scaler = StandardScaler()

# Scale the numerical columns.
feature_numerical = scaler.fit_transform(feature_numerical)

# Convert the scaled array to DataFrame with column names.
feature_numerical = pd.DataFrame(feature_numerical, columns=numerical_columns)

# Combine both the categorical and numerical columns.
features = pd.concat([feature_numerical, feature_categorical], axis=1)

# Split the data into training and temporary sets, which will be further splitted into validation and testing sets.
X_train, X_temp, y_train, y_temp = train_test_split(features, target, test_size=0.3, random_state=2024, stratify=target, shuffle=True)

# Split the temporary data into validation and testing sets.
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=2024, stratify=y_temp, shuffle=True)

# Predefine the best hyper parameters.
best_params = {'subsample': 0.7, 'reg_lambda': 0.6, 'reg_alpha': 0.7, 'n_estimators': 200, 'min_child_weight': 1, 'max_depth': 4, 'learning_rate': 0.2, 'gamma': 0.01, 'colsample_bytree': 0.7}

# Instantiate the XGBClassifier object.
xgb_model = xgb.XGBClassifier(**best_params, objective="binary:logistic", seed=20202024, booster="gbtree")

# Fit the data into the model.
xgb_model.fit(X_train, y_train)



# A function that predict if a patient has heart disease or not.
def predict_disease_presence(num_input, cat_input):
    """A function that predict the presence or absence of heart disease in a patient."""
    
    # Get both the categorical and numerical columns in user's input.
    input_categorical = cat_input
    input_numerical = num_input
    
    # Get both the categorical and numerical columns name.
    categorical_columns = ["sex", "chest_pain", "fasting_blood_sugar", "restecg", "exercise_induced_angina", "st_slope", "colored_by_fluoroscopy", "thallium_stress_test"]
    numerical_columns = [col for col in features.columns if col not in categorical_columns]

    # Scale the numerical columns.
    input_numerical = scaler.fit_transform(input_numerical)
    
    # Convert the scaled array to DataFrame with column names.
    input_numerical = pd.DataFrame(input_numerical, columns=numerical_columns)

    # Convert the scaled array to DataFrame with column names.
    input_categorical = pd.DataFrame(input_categorical, columns=categorical_columns)

    # Combine both the categorical and numerical columns.
    input = pd.concat([input_numerical, input_categorical], axis=1)

    
    # Predict the probability of presence and absence of heart disease.
    pred_probs = xgb_model.predict_proba(input)
    
    return pred_probs[0]
    
    
    
    