import streamlit as st

# Define the GCS components
def gcs_score(eye_opening, verbal_response, motor_response):
    return eye_opening + verbal_response + motor_response

# Define pupil reactivity score (-2 for both unreactive, -1 for one unreactive, 0 for both reactive)
def pupil_score(both_reactive, one_reactive):
    if both_reactive:
        return 0
    elif one_reactive:
        return -1
    else:
        return -2

# Define GCS-Pupils Score calculation (GCS minus pupil score)
def gcs_pupils_score(gcs, pupil_score):
    return gcs - pupil_score

# Streamlit app
st.title("GCS-Pupils Score Calculator")
st.write("""
### Description:
This calculator provides the GCS-Pupils Score, a clinical tool used to assess patients with traumatic brain injuries by integrating the Glasgow Coma Scale (GCS) with pupil reactivity. 
The lower the score, the more severe the neurological injury.
""")

# Input for GCS score
st.header("Glasgow Coma Scale (GCS) Components")
eye_opening = st.selectbox("Eye Opening", [1, 2, 3, 4], format_func=lambda x: f"{x} (Eye Opening)")
verbal_response = st.selectbox("Verbal Response", [1, 2, 3, 4, 5], format_func=lambda x: f"{x} (Verbal Response)")
motor_response = st.selectbox("Motor Response", [1, 2, 3, 4, 5, 6], format_func=lambda x: f"{x} (Motor Response)")

gcs = gcs_score(eye_opening, verbal_response, motor_response)
st.write(f"**GCS Score:** {gcs}")

# Input for pupil reactivity
st.header("Pupil Reactivity")
both_reactive = st.checkbox("Both pupils reactive")
one_reactive = st.checkbox("One pupil reactive")

pupil_react = pupil_score(both_reactive, one_reactive)
st.write(f"**Pupil Reactivity Score:** {pupil_react}")

# Calculate GCS-Pupils Score
gcs_pupil_score_result = gcs_pupils_score(gcs, pupil_react)
st.write(f"**GCS-Pupils Score:** {gcs_pupil_score_result}")
