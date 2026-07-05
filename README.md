# 🎥 AI Video Dubbing & Subtitle Generator (English to Kannada)

An AI-powered Python application that automatically extracts speech from a video, converts it into text, translates it into Kannada, generates Kannada audio, and creates a new video with Kannada subtitles.

## 🚀 Features

- 🎬 Extracts audio from an input video
- 🎤 Converts speech to text using Google Speech Recognition
- 🌐 Translates English text to Kannada
- 📝 Adds Kannada subtitles to the original video
- 🔊 Generates Kannada speech using Google Text-to-Speech (gTTS)
- 📁 Automatically creates an output folder for generated files

---

## 🛠️ Tech Stack

- Python
- OpenCV
- SpeechRecognition
- Google Translate (googletrans)
- gTTS (Google Text-to-Speech)
- PyDub
- FFmpeg
- OS Module

---

## 📂 Project Structure

```
project/
│── dubbing_ffmpeg.py
│── input.mp4
│── output_files/
│     ├── output_video_kannada.mp4
│     ├── translated_audio.mp3
│     └── translated_audio.wav
│── README.md
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/your-username/AI-Video-Dubbing.git
cd AI-Video-Dubbing
```

### Install dependencies

```bash
pip install opencv-python
pip install SpeechRecognition
pip install googletrans==4.0.0rc1
pip install pydub
pip install gTTS
```

### Install FFmpeg

Download and install FFmpeg from:

https://ffmpeg.org/download.html

Add FFmpeg to your system PATH.

---

## ▶️ Usage

1. Place your input video in the project folder.

2. Rename it as:

```
input.mp4
```

3. Run the program:

```bash
python dubbing_ffmpeg.py
```

4. The generated files will be available inside the **output_files** folder.

---

## 📸 Workflow

```
Input Video
      │
      ▼
Extract Audio
      │
      ▼
Speech-to-Text
      │
      ▼
Translate to Kannada
      │
      ├────────► Generate Kannada Audio
      │
      ▼
Add Kannada Subtitles
      │
      ▼
Output Video
```

---

## 📦 Output

The project generates:

- ✅ Video with Kannada subtitles
- ✅ Kannada audio (.mp3)
- ✅ Kannada audio (.wav)

---

## 📌 Applications

- Educational video localization
- Government awareness videos
- Digital literacy campaigns
- Regional language content creation
- Accessibility and multilingual communication

---

## 🔮 Future Improvements

- Support multiple regional languages
- Real-time video dubbing
- AI voice cloning
- Lip-sync animation
- Subtitle (.srt) file generation
- Offline speech recognition support
- Better translation accuracy using transformer-based models

---

## 👨‍💻 Author

**Mouna M**

GitHub: https://github.com/Mouna-1122
