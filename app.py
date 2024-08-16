import streamlit as st
from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
from googletrans import Translator
from gtts import gTTS
import io

def main():
    st.title("Image to Speech App")

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)

# Extract text from image
text = extract_text(image)

# Translate text (if needed)
translated_text = translate_text(text)

# Convert text to speech
audio = text_to_speech(translated_text)

# Display text and audio player
st.write(translated_text)
st.audio(audio)

def extract_text(image):
# Use pytesseract to extract text
    return pytesseract.image_to_string(image, lang='tel') # 'tel' for Telugu

def translate_text(text):
    # Translate text to English
    translator = Translator()
    return translator.translate(text, dest='en').text

def text_to_speech(text):
# Convert text to speech
    tts = gTTS(text=text, lang='en')
    fp = io.BytesIO()
    tts.write_to_fp(fp)
    return fp.getvalue()

if __name__ == "__main__":
    main()