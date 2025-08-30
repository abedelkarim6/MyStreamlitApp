from PIL import Image
import streamlit as st

st.title("We FINISHED MACHINE LEARNING EXAM")
st.write("### Welcome to my app!")
st.header("Here we wil show the exam grades")
st.subheader("We can also show the happiness level")
happiness = st.slider("Happiness Level", 0, 100000, 50)


img = Image.open(
    r"C:\Users\abede\OneDrive\Desktop\aboudi\OnlyTech\AI\Ai-Pics\ai+human hands.jpeg"
)
st.image(img, caption="AI and Human Hands", width=300)

# button to download above image
button = st.button("Download Image")


with st.form("Info collection form"):
    name = st.text_input("Enter your name")
    age = st.number_input("Enter your age", min_value=0)
    color = st.selectbox("Favorite color", ["Red", "Blue", "Green", "Yellow"])
    picture = st.file_uploader(
        "Upload your profile picture", type=["png", "jpg", "jpeg"]
    )

    submitted = st.form_submit_button("Submit")
    if submitted:
        # save all results in csv file
        with open("user_data.csv", "a") as f:
            f.write(f"{name},{age},{color}\n")
            st.success("Form submitted successfully!")
            st.balloons()

        # save image in data folder
        img = Image.open(picture)
        img.save(f"images/{name}.png")
