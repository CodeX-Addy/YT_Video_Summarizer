from youtube_transcript_api import yta
import os
import streamlit as st
from dotenv import load_dotenv

load_dotenv(verbose=True)  # Take environment variables from .env file if present.
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

prompt = """
You are an youtube video summarizer. And you will take a transcript text
and with that you will extracting the summary of that video along with relevant
key points. And try to summarize within 250-300 words. The transcript text is given here:  
"""

## Extracting text from youtube video url
def extract_transcript(yt_video_url):
    try:
        video_id = yt_video_url.split("=")[1]
        transcript_text = yta.get_transcript(video_id)
        transcript = ""
        for i in transcript_text:
            transcript += " " + i["text"]

        return transcript

    
    except Exception as e:
        raise e

##generating content
def generate_content(prompt, transcript):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt+transcript)
    return response.text

### Main Streamlit App
st.title("YouTube Transcript App..")


youtube_link = st.text_input("Enter YouTube Video Link:")

if youtube_link:
    video_id = youtube_link.split("=")[1]
    st.image(
        f"http://img.youtube.com/vi/{video_id}/0.jpg", use_column_width=True)

if st.button("Get Detailed Notes"):
    transcript_text = extract_transcript(youtube_link)

    if transcript_text:
        summary = generate_content(prompt,transcript_text)
        st.markdown("## Generate Notes:")
        st.write(summary)


