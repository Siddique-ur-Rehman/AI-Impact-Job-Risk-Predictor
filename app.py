import streamlit as st
import pickle
import pandas as pd


# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="AI Job Risk Predictor",
    page_icon="🤖",
    layout="wide"
)


# -----------------------------
# Load Model
# -----------------------------
@st.cache_resource
def load_model():

    with open("ai_job_risk_lgbm_model.pkl", "rb") as file:
        model = pickle.load(file)

    with open("label_encoder.pkl", "rb") as file:
        encoder = pickle.load(file)

    return model, encoder


model, label_encoder = load_model()


# -----------------------------
# Header
# -----------------------------
st.title("🤖 AI Impact Job Risk Predictor")

st.markdown(
"""
Predict the potential **AI-driven job risk level** based on:
- Job characteristics
- AI adoption
- Automation level
- Human skill requirements
"""
)


st.divider()


# -----------------------------
# Input Layout
# -----------------------------

col1, col2, col3 = st.columns(3)


with col1:

    st.subheader("👤 Employee Profile")

    Age = st.number_input(
        "Age",
        18,
        70,
        30
    )

    Education_Level = st.selectbox(
        "Education Level",
        [
            "High School",
            "Bachelor's",
            "Master's",
            "PhD"
        ]
    )


    Years_of_Experience = st.number_input(
        "Experience (Years)",
        0,
        50,
        5
    )


    Industry = st.selectbox(
        "Industry",
        [
            "Finance",
            "Manufacturing",
            "Retail",
            "Healthcare",
            "Technology"
        ]
    )


    Job_Role = st.text_input(
        "Job Role",
        "Accountant"
    )



with col2:

    st.subheader("🏢 Job Information")


    Company_Size = st.selectbox(
        "Company Size",
        [
            "Small",
            "Medium",
            "Large"
        ]
    )


    Job_Level = st.selectbox(
        "Job Level",
        [
            "Entry",
            "Mid",
            "Senior"
        ]
    )


    AI_Adoption_Level = st.selectbox(
        "AI Adoption Level",
        [
            "Low",
            "Medium",
            "High"
        ]
    )


    Number_of_AI_Tools_Used = st.number_input(
        "AI Tools Used",
        0,
        20,
        2
    )


    AI_Usage_Hours_Per_Week = st.number_input(
        "AI Usage Hours / Week",
        0,
        100,
        5
    )



with col3:

    st.subheader("⚙️ Task Analysis")


    Routine_Task_Percentage = st.slider(
        "Routine Tasks (%)",
        0,
        100,
        50
    )


    Creativity_Requirement = st.slider(
        "Creativity Requirement (%)",
        0,
        100,
        50
    )


    Human_Interaction_Level = st.slider(
        "Human Interaction (%)",
        0,
        100,
        50
    )


    Tasks_Automated_Percentage = st.slider(
        "Tasks Automated (%)",
        0,
        100,
        40
    )


    AI_Training_Hours = st.number_input(
        "AI Training Hours",
        0,
        200,
        10
    )



st.divider()


# -----------------------------
# Prediction
# -----------------------------

if st.button(
    "🚀 Predict Job Risk",
    use_container_width=True
):

    input_data = pd.DataFrame({

        "Age":[Age],
        "Education_Level":[Education_Level],
        "Years_of_Experience":[Years_of_Experience],
        "Industry":[Industry],
        "Job_Role":[Job_Role],
        "Company_Size":[Company_Size],
        "Job_Level":[Job_Level],
        "Routine_Task_Percentage":[Routine_Task_Percentage],
        "Creativity_Requirement":[Creativity_Requirement],
        "Human_Interaction_Level":[Human_Interaction_Level],
        "AI_Adoption_Level":[AI_Adoption_Level],
        "Number_of_AI_Tools_Used":[Number_of_AI_Tools_Used],
        "AI_Usage_Hours_Per_Week":[AI_Usage_Hours_Per_Week],
        "Tasks_Automated_Percentage":[Tasks_Automated_Percentage],
        "AI_Training_Hours":[AI_Training_Hours]

    })


    prediction = model.predict(input_data)

    prediction_label = label_encoder.inverse_transform(
        prediction
    )[0]


    probabilities = model.predict_proba(input_data)[0]

    confidence = max(probabilities)*100



    st.divider()

    st.subheader("📊 Prediction Result")


    if prediction_label == "High":

        st.error(
        f"""
        ## 🔴 High AI Job Risk
        
        Confidence: {confidence:.2f}%

        ### Meaning:
        - Job has high automation potential
        - Many tasks can be replaced by AI
        - Requires skill improvement
        
        ### Recommendations:
        ✅ Learn AI tools  
        ✅ Improve creative skills  
        ✅ Develop human-centered abilities  
        """
        )


    elif prediction_label == "Medium":

        st.warning(
        f"""
        ## 🟡 Medium AI Job Risk
        
        Confidence: {confidence:.2f}%

        ### Meaning:
        - Some tasks may be automated
        - Human involvement is still important
        
        ### Recommendations:
        ✅ Upskill with AI technologies  
        ✅ Combine domain knowledge with AI  
        """
        )


    else:

        st.success(
        f"""
        ## 🟢 Low AI Job Risk
        
        Confidence: {confidence:.2f}%

        ### Meaning:
        - Job requires strong human skills
        - Lower automation possibility
        
        ### Recommendations:
        ✅ Continue learning  
        ✅ Strengthen expertise  
        """
        )