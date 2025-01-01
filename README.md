# YouTube Transcript App

This Python application converts YouTube transcripts into detailed notes using the `youtube_transcript_api` and Google's Generative AI model. application uses Streamlit to create a user-friendly interface.

## Getting Started

1. Clone the repository:
git clone https://github.com/CodeX-Addy/yt_transcript.git


2. Create a `.env` file in the root directory of the project and add your Google API key:
GOOGLE_API_KEY=your_google_api_key


3. Install the required packages:
pip install -r requirements.txt


4. Run the application:
streamlit run app.py

5. Enter a YouTube video link and click "Get Detailed Notes" to generate the summary and key points.

## How it Works

1. The `extract_transcript` function extracts the transcript text from a given YouTube video URL using the `youtube_transcript_api`.
2. The `generate_content` function takes the prompt and transcript text as input and generates a summary and key points using Google's Generative AI model.
3. The Streamlit app displays the user interface and handles user input, displaying the generated detailed notes.

## Dependencies

- `streamlit`
- `youtube_transcript_api`
- `google-cloud-generativeai`
- `python-dotenv`

## License

This project is licensed under the MIT License.


