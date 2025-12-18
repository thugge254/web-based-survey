import streamlit as st
import json
from db import insert_response

st.set_page_config(page_title="Python Survey")

st.title("🐍 Python Survey")

with st.form("survey_form"):
    # Basic info
    name = st.text_input("What is your name?")
    age = st.number_input("How old are you?", min_value=0, step=1)

    # Gender
    gender = st.selectbox(
        "Gender",
        ["Select", "Male", "Female", "Non-binary", "Prefer not to say"]
    )

    # Employment Status
    employment_status = st.selectbox(
        "Employment Status",
        [
            "Select",
            "Student",
            "Employed (Full-time)",
            "Employed (Part-time)",
            "Self-employed",
            "Unemployed",
            "Retired"
        ]
    )

    # Industry
    industry = st.selectbox(
        "Industry",
        [
            "Select",
            "IT / Software",
            "Finance",
            "Healthcare",
            "Education",
            "Business",
            "Other"
        ]
    )

    # Education Level
    education = st.selectbox(
        "Education Level",
        [
            "Select",
            "Primary",
            "Secondary",
            "Diploma",
            "Bachelor’s degree",
            "Master’s degree",
            "Doctorate",
            "Other"
        ]
    )

    # Python preference
    enjoys_python = st.selectbox(
        "Do you enjoy Python programming?",
        ["Yes", "No"]
    )

    submitted = st.form_submit_button("Submit")

# Validation & response handling
if submitted:
    if (
        gender == "Select"
        or employment_status == "Select"
        or industry == "Select"
        or education == "Select"
    ):
        st.error("Please complete all required fields.")
    else:
        responses = {
            "name": name,
            "age": int(age),
            "gender": gender,
            "employment_status": employment_status,
            "industry": industry,
            "education": education,
            "enjoys_python": enjoys_python == "Yes"
        }

        st.success(f"Thank you, {name}!")
        st.json(responses)

        # Optional: save responses to a file
        # with open("survey_results.json", "a") as f:
        #     json.dump(responses, f)
        #     f.write("\n")
            # ✅ Call insert_response to save into PostgreSQL
        try:
            insert_response(responses)
            st.success(f"Thank you, {name}! Your response has been saved.")
        except Exception as e:
            st.error(f"Failed to save response: {e}")

        st.json(responses)

