import streamlit as st
from PIL import Image

from prediction import predict_disease
from disease_info import DISEASE_INFO

# Page Configuration
st.set_page_config(
    page_title="PlantCare AI",
    page_icon="🌿",
    layout="centered"
)

# Title
st.title("🌿 PlantCare AI")

# Subtitle
st.subheader("Plant Disease Detection Using Deep Learning")

# Description
st.write("""
Upload an image of a plant leaf, and the AI model will predict
the disease affecting the plant.
""")

st.info("""
📌 **Supported Plants**

This application can detect diseases for the following plants:

• Apple
• Blueberry
• Cherry
• Corn
• Grape
• Orange
• Peach
• Pepper Bell
• Potato
• Raspberry
• Soybean
• Squash
• Strawberry
• Tomato

⚠️ Please upload a clear leaf image belonging to one of the above plants.
The model may produce incorrect results for unsupported plants or non-leaf images.
""")

st.divider()

# Image Upload
uploaded_file = st.file_uploader(
    "📤 Upload a Leaf Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")

    st.image(
        image,
        caption="Uploaded Leaf Image",
        use_container_width=True
    )

    st.success("Image uploaded successfully!")

if st.button("🔍 Predict Disease"):

    plant, disease, confidence, class_name = predict_disease(image)

    st.success("Prediction Completed!")

    with st.container():
        st.subheader("🌿 Prediction Results")

        col1, col2 = st.columns(2)

    with col1:
       st.markdown("##### 🌿 Plant")
       st.write(plant)

    with col2:
       st.markdown("##### 📊 Confidence")
       st.write(f"{confidence * 100:.2f}%")

    st.markdown("##### 🦠 Disease")
    st.write(disease)
        
    # get information about disease   
    info = DISEASE_INFO.get(class_name)

    if info:

        st.divider()

        st.subheader("📝 Disease Description")
        st.write(info["description"])

        st.subheader("⚠️ Symptoms")
        for symptom in info["symptoms"]:
            st.write(f"• {symptom}")

        st.subheader("🌱 Prevention Tips")
        for tip in info["prevention"]:
            st.write(f"• {tip}")