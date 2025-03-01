import streamlit as st
import base64

# Function to set the background image and fonts
def set_bg_image(image_path):
    with open(image_path, "rb") as img_file:
        encoded_string = base64.b64encode(img_file.read()).decode()
    
    background_image = f"""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');

            html, body, [class*="stApp"] {{
                font-family: 'Poppins', sans-serif;
                background-image: url("data:image/png;base64,{encoded_string}");
                background-size: cover;
                background-repeat: no-repeat;
                background-attachment: fixed;
            }}

            .main {{
                background-color: rgba(255, 255, 255, 0.85);
                padding: 30px;
                border-radius: 15px;
                box-shadow: 0px 6px 15px rgba(0, 0, 0, 0.2);
                margin-top: 30px;
            }}

            /* Styled Title */
            .title-container {{
                text-align: center;
                padding: 20px;
                background: linear-gradient(135deg, #4A90E2, #357ABD);
                color: white;
                border-radius: 12px;
                box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2);
                font-size: 36px;
                font-weight: 700;
                letter-spacing: 1px;
                text-shadow: 2px 2px 8px rgba(0, 0, 0, 0.3);
                margin-bottom: 20px;
            }}

            label {{
                font-size: 18px;
                font-weight: 500;
                color: #333;
            }}

            .stButton>button {{
                background: linear-gradient(135deg, #4A90E2, #357ABD);
                color: white;
                border: none;
                padding: 12px 18px;
                border-radius: 8px;
                font-size: 18px;
                font-weight: 600;
                transition: 0.3s;
            }}

            .stButton>button:hover {{
                background: linear-gradient(135deg, #357ABD, #4A90E2);
                transform: scale(1.05);
            }}

            .stTextInput input {{
                padding: 12px;
                font-size: 16px;
                border-radius: 8px;
            }}

            .stSelectbox div[data-baseweb="select"] {{
                border-radius: 8px;
            }}
        </style>
    """
    
    st.markdown(background_image, unsafe_allow_html=True)

# ✅ Call the function with the image file path
set_bg_image("image.png")

# Main Container
st.markdown('<div class="main">', unsafe_allow_html=True)

# Styled Title
st.markdown(
    """
    <div class="title-container">🔄 Unit Converter</div>
    """,
    unsafe_allow_html=True
)

# Select Conversion Type
conversion_type = st.selectbox("Choose conversion type:", ["Length", "Weight", "Temperature"])

# Conversion Functions
def convert_length(value, from_unit, to_unit):
    length_units = {
        "Meters": 1,
        "Kilometers": 0.001,
        "Centimeters": 100,
        "Millimeters": 1000,
        "Miles": 0.000621371,
        "Yards": 1.09361,
        "Feet": 3.28084,
        "Inches": 39.3701
    }
    return value * (length_units[to_unit] / length_units[from_unit])

def convert_weight(value, from_unit, to_unit):
    weight_units = {
        "Kilograms": 1,
        "Grams": 1000,
        "Pounds": 2.20462,
        "Ounces": 35.274
    }
    return value * (weight_units[to_unit] / weight_units[from_unit])

def convert_temperature(value, from_unit, to_unit):
    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        return (value * 9/5) + 32
    elif from_unit == "Celsius" and to_unit == "Kelvin":
        return value + 273.15
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        return (value - 32) * 5/9
    elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
        return ((value - 32) * 5/9) + 273.15
    elif from_unit == "Kelvin" and to_unit == "Celsius":
        return value - 273.15
    elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
        return ((value - 273.15) * 9/5) + 32
    else:
        return value

# User Input
value = st.number_input("Enter value:", min_value=0.0, step=0.01)

if conversion_type == "Length":
    from_unit = st.selectbox("From:", ["Meters", "Kilometers", "Centimeters", "Millimeters", "Miles", "Yards", "Feet", "Inches"])
    to_unit = st.selectbox("To:", ["Meters", "Kilometers", "Centimeters", "Millimeters", "Miles", "Yards", "Feet", "Inches"])
    if st.button("Convert", key="convert_length"):
        result = convert_length(value, from_unit, to_unit)
        st.success(f"🎉 Congratulations! {value} {from_unit} = {result:.4f} {to_unit}")
        st.balloons()

elif conversion_type == "Weight":
    from_unit = st.selectbox("From:", ["Kilograms", "Grams", "Pounds", "Ounces"])
    to_unit = st.selectbox("To:", ["Kilograms", "Grams", "Pounds", "Ounces"])
    if st.button("Convert", key="convert_weight"):
        result = convert_weight(value, from_unit, to_unit)
        st.success(f"🎉 Congratulations! {value} {from_unit} = {result:.4f} {to_unit}")
        st.balloons()

elif conversion_type == "Temperature":
    from_unit = st.selectbox("From:", ["Celsius", "Fahrenheit", "Kelvin"])
    to_unit = st.selectbox("To:", ["Celsius", "Fahrenheit", "Kelvin"])
    if st.button("Convert", key="convert_temp"):
        result = convert_temperature(value, from_unit, to_unit)
        st.success(f"🎉 Congratulations! {value} {from_unit} = {result:.2f} {to_unit}")
        st.balloons()

st.markdown('</div>', unsafe_allow_html=True)
