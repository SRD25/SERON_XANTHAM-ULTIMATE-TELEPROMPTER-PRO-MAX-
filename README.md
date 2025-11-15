🎨🚀 ULTIMATE AI TELEPROMPTER 4000 - COLOR EDITION
🌟 Project Overview
This is the Ultimate AI Teleprompter 4000 - Color Edition, a powerful, feature-rich teleprompter application built using Python and the Tkinter GUI library.

Designed to enhance presentation and speech delivery, this teleprompter goes beyond simple scrolling text by integrating modern "AI" and utility features like document support, real-time translation, and text-to-speech functionality.

🧑‍💻 Authors
This project was developed collaboratively by:

Ritesh Bagde

Sanket Nandagawali

We are fellow classmates passionate about leveraging Python for practical desktop applications.

⚙️ Key Features and Working
The application is encapsulated within the UltimateAITeleprompter class and offers a suite of advanced features to enhance the teleprompting experience:

1. Advanced Script Handling
Word Document Support: Directly import and process scripts from .docx files using the python-docx library.

Color Themes: The "Color Edition" includes a set of 10 vibrant color themes to customize the appearance for different environments or user preferences.

Intuitive Controls: Uses the Tkinter framework to provide a responsive and user-friendly Graphical User Interface (GUI) for text input, control adjustments, and feature toggles.

2. AI & Utility Integrations
Real-time Translation: Integrated with deep-translator, users can translate their script on the fly.

Quick Tip: The application is designed to respond to F8 for translation.

Text-to-Speech (TTS): Utilizes the gTTS library to convert the teleprompter script into spoken audio.

Voice Features (Planned/Implemented): Includes support for speech_recognition, indicating capabilities for potential voice control or analysis features (e.g., auto-scroll control).

3. Performance & Architecture
Multi-threading: Employs the threading module to ensure that demanding operations (like translations, TTS, or audio playback via pygame) do not freeze the main GUI thread.

Robust Dependency Check: The application performs checks on startup for all required external libraries (like python-docx, deep-translator, gtts, SpeechRecognition) and notifies the user if any are missing.

🚀 Getting Started
Prerequisites
To run this teleprompter, you need Python 3.x installed. The following libraries are required for full functionality. You can install them using pip:



pip install tk
pip install python-docx
pip install deep-translator
pip install gtts
pip install SpeechRecognition
pip install pygame
Running the Application
Save the code as wrokingtelepromter2.py.

Open your terminal or command prompt.

Run the file using the Python interpreter:



python wrokingtelepromter2.py
Upon startup, the console will display the initialization status and confirm which features (Translation, TTS, Word document support) are available based on your installed packages.
