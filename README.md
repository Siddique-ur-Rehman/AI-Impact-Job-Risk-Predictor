# 🤖 AI Impact Job Risk Predictor

An end-to-end Machine Learning project that predicts the impact of Artificial Intelligence on jobs by classifying job roles into three risk categories:

- 🟢 Low AI Risk
- 🟡 Medium AI Risk
- 🔴 High AI Risk

The project uses a **LightGBM Multiclass Classification Model** trained on job-related features such as automation percentage, AI adoption, creativity requirements, human interaction, industry, and experience level.

The trained model is deployed as an interactive **Streamlit Web Application** where users can enter job details and receive an AI impact risk prediction.

---

## 🌐 Live Application

🚀 Streamlit Deployment:

https://YOUR_STREAMLIT_APP_LINK

---

# 📌 Project Objective

Artificial Intelligence is rapidly changing the workplace by automating repetitive tasks and increasing the demand for AI-related skills.

The goal of this project is to build a machine learning system that can predict how vulnerable a job role is to AI-driven automation.

This system helps users understand:

- The possibility of AI replacing certain job tasks
- The influence of automation on different industries
- The importance of creativity and human interaction
- The role of AI adoption and training in future job security

---

# 🧠 Machine Learning Problem

## Problem Type

Multiclass Classification

## Target Variable

`Layoff_Risk`

The model predicts one of the following classes:

| Class | Meaning |
|---|---|
| High | Job has high AI automation risk |
| Medium | Job has moderate AI impact risk |
| Low | Job has lower AI automation risk |

---

# 📊 Dataset Information

Dataset Size:

- Total Records: 20,000
- Total Features: 16

The dataset contains information about:

- Employee demographics
- Education level
- Job characteristics
- Industry information
- AI usage patterns
- Automation potential
- Human skill requirements

---

# 📋 Dataset Features

## Numerical Features

- Age
- Years_of_Experience
- Routine_Task_Percentage
- Creativity_Requirement
- Human_Interaction_Level
- Number_of_AI_Tools_Used
- AI_Usage_Hours_Per_Week
- Tasks_Automated_Percentage
- AI_Training_Hours


## Categorical Features

- Education_Level
- Industry
- Job_Role
- Company_Size
- Job_Level
- AI_Adoption_Level


## Target

- Layoff_Risk

---

# 🔄 Machine Learning Pipeline

The complete workflow followed:

```
Dataset Loading
        |
        ↓
Data Exploration
        |
        ↓
Data Cleaning & Validation
        |
        ↓
Feature and Target Separation
        |
        ↓
Categorical Feature Encoding
        |
        ↓
Train-Test Split
        |
        ↓
LightGBM Model Training
        |
        ↓
Model Evaluation
        |
        ↓
Model Serialization using Pickle
        |
        ↓
Streamlit Deployment
```

---

# 🧹 Data Preprocessing

The following preprocessing steps were performed:

- Checked dataset shape
- Checked data types
- Verified missing values
- Separated input features and target variable
- Encoded target labels using Label Encoder
- Applied One-Hot Encoding to categorical variables
- Created a complete Scikit-Learn Pipeline
- Split dataset into training and testing sets using stratified sampling

---

# 🤖 Model Used

## LightGBM Classifier

The final model used for prediction is:

**LightGBM (Light Gradient Boosting Machine)**


### Why LightGBM?

LightGBM was selected because:

- It performs well on structured/tabular data
- It handles complex feature relationships
- It provides high prediction accuracy
- It trains faster compared to many traditional boosting algorithms
- It works effectively for multiclass classification problems

---

# 📈 Model Performance

## LightGBM Evaluation Results

| Metric | Score |
|---|---|
| Accuracy | 94.67% |
| Macro Precision | 95% |
| Macro Recall | 95% |
| Macro F1 Score | 95% |


## Classification Report

| Risk Level | Precision | Recall | F1 Score |
|---|---|---|---|
| High | 0.97 | 0.96 | 0.96 |
| Low | 0.96 | 0.95 | 0.96 |
| Medium | 0.91 | 0.93 | 0.92 |

---

# 🖥️ Streamlit Application Features

The deployed application provides:

✅ Professional dashboard interface  
✅ User-friendly input form  
✅ AI job risk prediction  
✅ Prediction confidence score  
✅ Explanation of each risk category  
✅ Recommendations based on predicted risk level  


---

# 🟢 Prediction Class Explanation

## High AI Risk

Meaning:

- Job contains highly repetitive tasks
- Large percentage of tasks can be automated
- AI adoption may strongly affect the role

Recommendations:

- Learn AI tools related to the field
- Improve creative problem-solving skills
- Develop human-centered abilities


---

## Medium AI Risk

Meaning:

- Some job tasks can be automated
- Human involvement remains important

Recommendations:

- Improve AI knowledge
- Combine domain expertise with AI skills
- Continue professional development


---

## Low AI Risk

Meaning:

- Job requires strong human abilities
- Automation replacement possibility is lower

Recommendations:

- Continue improving expertise
- Maintain adaptability with new technologies

---

# 🛠️ Technologies Used

## Programming Language

Python


## Machine Learning Libraries

- LightGBM
- Scikit-Learn


## Data Processing

- Pandas
- NumPy


## Visualization

- Matplotlib
- Seaborn


## Deployment

- Streamlit


## Model Saving

- Pickle


---

# 📁 Project Structure

```
AI_Job_Risk_Prediction/

│
├── app.py
│
├── ai_job_risk_lgbm_model.pkl
│
├── label_encoder.pkl
│
├── requirements.txt
│
├── README.md
│
└── AI_Job_Risk_Model_Training.ipynb

```

---

# ⚙️ Installation and Running Locally

## Clone Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_LINK
```

## Open Project Folder

```bash
cd AI_Job_Risk_Prediction
```

## Install Required Libraries

```bash
pip install -r requirements.txt
```

## Run Streamlit Application

```bash
streamlit run app.py
```

The application will open automatically in your browser.

---

# 📦 Requirements

```
scikit-learn==1.6.1
lightgbm==4.6.0
pandas==2.2.2
numpy==2.0.2
streamlit
```

---

# 👨‍💻 Author

**Siddique ur Rehman**

Data Science 

Areas of Interest:

- Machine Learning
- Artificial Intelligence
- Deep Learning
- NLP
- Data Analytics


---

# 📄 License

This project is developed for educational and research purposes.
