import streamlit as st
from model import get_model

clf, iris = get_model()

st.title("🌸 Iris Flower Classifier")

sepal_length = st.slider('Sepal length', 4.0, 8.0, 5.0)
sepal_width = st.slider('Sepal width', 2.0, 4.5, 3.0)
petal_length = st.slider('Petal length', 1.0, 7.0, 4.0)
petal_width = st.slider('Petal width', 0.1, 2.5, 1.0)

input_data = [[sepal_length, sepal_width, petal_length, petal_width]]
prediction = clf.predict(input_data)[0]
predicted_class = iris.target_names[prediction]

st.success(f"Predicted Flower: {predicted_class}")
