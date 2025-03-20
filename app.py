import streamlit as st
import speech_recognition as sr
import google.generativeai as genai
st.title("WELCOME TO VOICE BASED CHATBOT")
genai.configure(api_key="AIzaSyD5sS998Fbgr1fBCRSNwrBTPZ_lBI0McqE") 
recognizer = sr.Recognizer()
def record_audio():
    try:
        with sr.Microphone() as source:
            st.write("🎙 Speak now...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source, phrase_time_limit=100)
            st.write("✅ Recorded successfully!")
        return audio
    except Exception as e:
        st.error(f"Error recording audio: {e}")
        return None

# Convert speech to text
def speech_to_text(audio):
    if not audio:
        return None
    try:
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return "Could not understand the audio."
    except sr.RequestError:
        return "API error occurred."

# Analyze response with Gemini AI
def analyze_response(text):
    if not text or text in ["Could not understand the audio.", "API error occurred."]:
        return "❌ No valid response to analyze."
   
    try:
        model = genai.GenerativeModel("gemini-1.5-pro")  # Use correct model name
        response = model.generate_content(text)
        return response.text if hasattr(response, "text") else "⚠️ AI response error."
    except Exception as e:
        return f"⚠️ AI API error: {e}"
if st.button("Record Your Question"):
    audio = record_audio()
    text = speech_to_text(audio)

    st.subheader("📝 Your Response:")
    st.write(text)

    if text and text not in ["Could not understand the audio.", "API error occurred."]:
        feedback = analyze_response(text)
        st.subheader("💡 Your Answer:")
        st.write(feedback)

    # Show "Next Question" button after feedback
    if "show_next_button" not in st.session_state:
        st.session_state.show_next_button = True

