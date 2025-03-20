**# Voice-Text-based-chatbot**
This repository contains a simple voice-based chatbot application built with Streamlit and Gemini AI. It takes voice input, transcribes it to text, and generates a response using the Gemini AI API.

**📌 Features**
Speech-to-Text Conversion using speech_recognition.
Text Generation using google.generativeai.
Easy-to-use interface with Streamlit.
Real-time audio recording.
Display of both transcribed input and AI-generated response.
**
📝 Requirements**
Install the dependencies with: pip install streamlit speechrecognition google-generativeai

**🚀 Usage**
Clone the repository.
Install the dependencies.
Set your Gemini AI API key in the code: genai.configure(api_key="YOUR_API_KEY")

Run the Streamlit app : streamlit run app.py

**📂 Code Explanation**
record_audio()
Captures audio from the microphone and returns the audio object.

speech_to_text()
Converts recorded audio to text using Google Speech Recognition.

analyze_response()
Generates a response from Gemini AI based on the transcribed text.

Streamlit Interface
The Record Your Question button triggers the audio recording process.
Displays transcribed text and AI-generated responses.
💡 Example Output
User: (Speaks a question)
App: Shows transcribed text and Gemini AI's response.
🔒 Note
Ensure your API key is kept safe and not exposed publicly.

