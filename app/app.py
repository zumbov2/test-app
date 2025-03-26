import streamlit as st

# Title of the app
st.title("Simple Streamlit Demo App")

# Slider input
slider_value = st.slider("Select a value", 0, 100, 50)

# Display the slider value or a default message
if slider_value is not None:
    st.write(f"Selected value: {slider_value}")
else:
    st.write("No value selected yet.")

# Button
if st.button("Click Me"):
    st.write("Button clicked!")
