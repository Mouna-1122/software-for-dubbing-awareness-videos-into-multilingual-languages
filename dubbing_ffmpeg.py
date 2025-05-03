
import os
import cv2
import speech_recognition as sr
from googletrans import Translator
from pydub import AudioSegment
from gtts import gTTS

def create_output_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def extract_audio(video_file, output_directory):
    audio_file = os.path.join(output_directory, "extracted_audio.mp3")
    video = AudioSegment.from_file(video_file)
    video.export(audio_file, format="mp3")  # Save as MP3
    return audio_file

def convert_mp3_to_wav(mp3_file, output_directory):
    wav_file = os.path.join(output_directory, "extracted_audio.wav")
    audio = AudioSegment.from_mp3(mp3_file)
    audio.export(wav_file, format="wav")  # Convert to WAV
    return wav_file

def transcribe_audio(audio_file):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.record(source)
        text = recognizer.recognize_google(audio_data)
    return text

def translate_text(text, target_language='kn'):
    translator = Translator()
    translated = translator.translate(text, dest=target_language)
    return translated.text

def create_subtitle_video(video_file, subtitle, output_file):
    # Open the original video
    cap = cv2.VideoCapture(video_file)
    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Define the codec and create a VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_file, fourcc, fps, (width, height))

    # Read frames and add subtitles
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        # Add subtitle text
        cv2.putText(frame, subtitle, (50, height - 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
        
        # Write the frame to the output video
        out.write(frame)

    cap.release()
    out.release()

def text_to_speech(text, output_file):
    tts = gTTS(text=text, lang='kn')  # Create TTS object for Kannada
    tts.save(output_file)  # Save as MP3
    # Optionally convert to WAV if needed
    audio = AudioSegment.from_mp3(output_file)
    wav_file = output_file.replace('.mp3', '.wav')
    audio.export(wav_file, format="wav")  # Convert to WAV
    return wav_file

def main(video_file):
    output_directory = "output_files"
    create_output_directory(output_directory)

    audio_file = extract_audio(video_file, output_directory)
    wav_file = convert_mp3_to_wav(audio_file, output_directory)
    transcribed_text = transcribe_audio(wav_file)
    
    # Translate to Kannada
    translated_text = translate_text(transcribed_text)

    output_video_file = os.path.join(output_directory, "output_video_kannada.mp4")
    create_subtitle_video(video_file, translated_text, output_video_file)

    # Convert translated text to Kannada audio
    kannada_audio_file = os.path.join(output_directory, "translated_audio.mp3")
    kannada_wav_file = text_to_speech(translated_text, kannada_audio_file)

    # Clean up temporary audio files
    os.remove(audio_file)
    os.remove(wav_file)

    print("DONE")
    print(f"Translated audio saved as: {kannada_audio_file} and {kannada_wav_file}")

if __name__ == "__main__":
    video_file = "input.mp4"  # Replace with your video file
    main(video_file)