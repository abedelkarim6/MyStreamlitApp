import streamlit as st
from PIL import Image

# Title and description
st.title("🌟 Personal Profile Dashboard")
st.write("Fill in your details below to see your profile!")

# Form for user input
with st.form("profile_form"):
    name = st.text_input("Enter your name")
    age = st.number_input("Enter your age", min_value=0)
    color = st.selectbox("Favorite color", ["Red", "Blue", "Green", "Yellow"])
    picture = st.file_uploader(
        "Upload your profile picture", type=["png", "jpg", "jpeg"]
    )

    submitted = st.form_submit_button("Submit")

# Display results in container with columns
if submitted:
    with st.container():
        st.subheader("Your Profile Info")
        col1, col2 = st.columns([1, 2])

        # Display picture
        if picture is not None:
            img = Image.open(picture)
            col1.image(img, caption="Profile Picture", width=150)

        # Display info
        col2.write(f"**Name:** {name}")
        col2.write(f"**Age:** {age}")
        col2.write(f"**Favorite Color:** {color}")


happiness = st.slider("Happiness Level", 0, 100, 50)
