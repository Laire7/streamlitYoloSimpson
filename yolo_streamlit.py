import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Upload the CSV file
uploaded_file = st.file_uploader("Upload YOLO Training Log", type=["csv"])

if uploaded_file is not None:
    # Read the CSV file
    df = pd.read_csv(uploaded_file)

    # Display the column names to check if 'loss' exists
    st.write("Columns in the uploaded file:", df.columns.tolist())

    # Check if 'loss' column exists
    if 'metrics/mAP50-95(B)' in df.columns:
        epochs = df['epoch']
        loss = df['metrics/mAP50-95(B)']

        # Create a plot for loss values
        fig, ax = plt.subplots()
        ax.plot(epochs, loss, label='Training Loss', marker='o')

        # Add labels and title
        ax.set_xlabel('Epochs')
        ax.set_ylabel('mAP50-95')
        ax.set_title('YOLO Training Loss Over Epochs')
        ax.legend()

        # Display the plot
        st.pyplot(fig)
    else:
        st.error("The 'metrics/mAP50-95(B)' column does not exist in the uploaded file.")
