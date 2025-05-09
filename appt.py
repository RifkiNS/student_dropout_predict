import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder
from joblib import load
import streamlit as st

bundle = load('rfmodel.joblib')
model = bundle['model']
scaler = bundle['scaler']

columns_to_scale = [
    "Curricular_units_1st_sem_approved",
    "Curricular_units_1st_sem_grade",
    "Curricular_units_2nd_sem_approved",
    "Curricular_units_2nd_sem _grade",
    "Curricular_units_2nd_sem_evaluations",
    "Curricular_units_1st_sem_evaluations"
    "Age_at_enrollment"
]

feature = ["Course", "Admission_grade", "Previous_qualification_grade", "Tuition_fees_up_to_date"]



def prepro_df(df):
    process_df = df.copy()


    category_cols =["Course", "Tuition_fees_up_to_date"]
    label_encoder = LabelEncoder()
    for col in category_cols:
        if col in process_df.columns:
            process_df[col] = label_encoder.fit_transform(process_df[col])

    scaler = StandardScaler()
    process_df[process_df.columns] = scaler.fit_transform(process_df)

    return process_df

def preprocessing(input_df):
    input_df = prepro_df(input_df)
    return input_df


st.set_page_config(
    page_title="Prediksi Mahasiswa Dropout", page_icon="🏫", layout="wide"
)

st.title("🎓 Student Dropout Prediction")


def main():

    st.subheader("Input Student Information:")

    input_data = {}  # Dictionary to store user input data
    col1, col2 = st.columns(2)  # Split the interface into two columns

    with col1:
        input_data["Curricular_units_2nd_sem_approved"] = st.number_input(
            "Approve Second Semester Course Unit: ", step=1
        )
        input_data["Curricular_units_1st_sem_approved"] = st.number_input(
            "Approve First Semester Course Unit: ", step=1
        )
        input_data["Curricular_units_2nd_sem_grade"] = st.number_input(
            "Second semester grade: ", step=1
        )
        input_data["Curricular_units_1st_sem_grade"] = st.number_input(
            "First semester grade: ", step=1
        )
        input_data["Tuition_fees_up_to_date"] = st.radio(
            "Select Tuition fees up to date:", ["Yes", "No"]
        )
        input_data["Curricular_units_2nd_sem_evaluations"] = st.number_input(
            "Evaluations Second Semester Course Unit: ", step=1
        )
        

        
        

    with col2:
        input_data["Admission_grade"] = st.number_input("Admission grade", min_value=0, max_value=200, step=1)
        input_data["Age_at_enrollment"] = st.number_input("Age", step=1)
        input_data["Previous_qualification_grade"] = st.number_input("Previous qualification grade", min_value=0, max_value=200, step=1)
        input_data['Course'] = st.selectbox(
            "Course",
            [
                "33 - Biofuel Production Technologies ",
                "171 - Animation and Multimedia Design ",
                "8014 - Social Service (evening attendance) ",
                "9003 - Agronomy 9070 - Communication Design ",
                "9085 - Veterinary Nursing ",
                "9119 - Informatics Engineering ",
                "9130 - Equinculture ",
                "9147 - Management",
                "9238 - Social Service ",
                "9254 - Tourism ",
                "9500 - Nursing ",
                "9556 - Oral Hygiene ",
                "9670 - Advertising and Marketing Management ",
                "9773 - Journalism and Communication ",
                "9853 - Basic Education 9991 - Management (evening attendance)"
            ]
        )
        input_data["Curricular_units_1st_sem_evaluations"] = st.number_input(
            "Evaluation Second Semester Course Unit: ", step=1
        )

    input_df = pd.DataFrame([input_data])  # Convert collected data into a DataFrame

    if st.button("Predict"):  # When the 'Predict' button is clicked
        final_df = preprocessing(input_df)  # Preprocess the collected data
        prediction = model.predict(final_df)[0]  # Use the model to predict the outcome

        # Display the prediction result
        if prediction == 0:
            st.write("Graduate")
        elif prediction == 1:
            st.write("Dropout")


if __name__ == "__main__":
    main()

