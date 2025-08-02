# # modules/tts.py
# from transformers import pipeline
# import io
# import wave
# import numpy as np

# HF_TTS_MODEL = "facebook/mms-tts-eng"  # Lightweight TTS model

# def generate_audio(text):
#     """Generate audio using Hugging Face TTS and return WAV bytes (no soundfile needed)"""
#     tts = pipeline("text-to-speech", model=HF_TTS_MODEL)
#     audio_data = tts(text)
#     audio_array = audio_data["audio"]
#     sample_rate = audio_data["sampling_rate"]

#     # Convert float32 [-1,1] to int16
#     int_audio = (np.array(audio_array) * 32767).astype(np.int16)

#     # Write to memory buffer as WAV
#     buffer = io.BytesIO()
#     with wave.open(buffer, 'wb') as wf:
#         wf.setnchannels(1)  # mono
#         wf.setsampwidth(2)  # 16-bit
#         wf.setframerate(sample_rate)
#         wf.writeframes(int_audio.tobytes())

    # buffer.seek(0)
    # return buffer.read()


# modules/tts.py
# from transformers import pipeline
# import io
# import wave
# import numpy as np
# import re

# HF_TTS_MODEL = "facebook/mms-tts-eng"  # Lightweight TTS model

# def add_pauses(text):
#     """Add natural pauses based on punctuation for human-like pacing"""
#     # Add extra spaces after commas and periods to create pause effect
#     text = re.sub(r',', ', ...', text)
#     text = re.sub(r'\.', '. ...', text)
#     return text

# def generate_audio(text):
#     """Generate audio using Hugging Face TTS and return WAV bytes (no soundfile needed)"""
#     # Add pauses for natural effect
#     text_with_pauses = add_pauses(text)

#     tts = pipeline("text-to-speech", model=HF_TTS_MODEL)
#     audio_data = tts(text_with_pauses)
#     audio_array = audio_data["audio"]
#     sample_rate = audio_data["sampling_rate"]

#     # Convert float32 [-1,1] to int16
#     int_audio = (np.array(audio_array) * 32767).astype(np.int16)

#     # Write to memory buffer as WAV
#     buffer = io.BytesIO()
#     with wave.open(buffer, 'wb') as wf:
#         wf.setnchannels(1)  # mono
#         wf.setsampwidth(2)  # 16-bit
#         wf.setframerate(sample_rate)
#         wf.writeframes(int_audio.tobytes())

#     buffer.seek(0)
#     return buffer.read()


# from transformers import pipeline
# import io
# import wave
# import numpy as np
# import re

# HF_TTS_MODEL = "facebook/mms-tts-eng"  # Lightweight TTS model

# def split_text_for_pauses(text):
#     """
#     Split text into segments at punctuation and preserve punctuation.
#     """
#     segments = re.split(r'([,.!?])', text)
#     combined = []
#     for i in range(0, len(segments)-1, 2):
#         combined.append(segments[i].strip() + segments[i+1].strip())
#     if len(segments) % 2 != 0:
#         combined.append(segments[-1].strip())
#     return [seg for seg in combined if seg]

# def generate_audio(text):
#     """
#     Generate audio with explicit pauses at punctuation for natural pacing.
#     """
#     tts = pipeline("text-to-speech", model=HF_TTS_MODEL)
#     segments = split_text_for_pauses(text)

#     combined_audio = []
#     sample_rate = 16000  # fallback

#     for seg in segments:
#         audio_data = tts(seg)
#         audio_array = np.array(audio_data["audio"])

#         # Flatten 2D -> 1D if necessary
#         if audio_array.ndim > 1:
#             audio_array = audio_array.flatten()

#         sample_rate = audio_data["sampling_rate"]

#         # Convert float32 [-1,1] to int16
#         int_audio = (audio_array * 32767).astype(np.int16)
#         combined_audio.append(int_audio)

#         # Add silence after punctuation (~0.5s)
#         silence = np.zeros(int(sample_rate * 0.5), dtype=np.int16)
#         combined_audio.append(silence)

#     # Concatenate safely
#     final_audio = np.concatenate(combined_audio)

#     # Write WAV to buffer
#     buffer = io.BytesIO()
#     with wave.open(buffer, 'wb') as wf:
#         wf.setnchannels(1)
#         wf.setsampwidth(2)
#         wf.setframerate(sample_rate)
#         wf.writeframes(final_audio.tobytes())

#     buffer.seek(0)
#     return buffer.read()

# from transformers import pipeline
# import io
# import wave
# import numpy as np
# import re

# HF_TTS_MODEL = "facebook/mms-tts-eng"  # Lightweight TTS model

# # Initialize TTS pipeline once at module load for performance
# tts_pipeline = pipeline("text-to-audio", model=HF_TTS_MODEL)


# def split_text_for_pauses(text):
#     """
#     Split text into segments at punctuation marks (.,!?) preserving punctuation,
#     to insert pauses naturally in speech.
#     """
#     segments = re.split(r'([,.!?])', text)
#     combined = []
#     for i in range(0, len(segments) - 1, 2):
#         part = segments[i].strip()
#         punct = segments[i + 1].strip()
#         combined.append(part + punct)
#     if len(segments) % 2 != 0:
#         last_segment = segments[-1].strip()
#         if last_segment:
#             combined.append(last_segment)
#     return combined


# def generate_audio(text):
#     """
#     Generate WAV audio bytes from input text with 0.5s pauses after punctuations.
#     Returns raw WAV bytes.
#     """
#     segments = split_text_for_pauses(text)

#     combined_audio = []
#     sample_rate = 16000  # default fallback

#     for seg in segments:
#         # Generate audio for each segment
#         audio_data = tts_pipeline(seg)

#         # audio_data['audio'] might be list of floats or numpy array, convert safely
#         audio_array = np.array(audio_data["audio"])

#         # Flatten to 1D if multi-dimensional (ensure mono channel)
#         if audio_array.ndim > 1:
#             audio_array = audio_array.flatten()

#         sample_rate = audio_data.get("sampling_rate", sample_rate)

#         # Convert float [-1, 1] to int16 PCM
#         int_audio = (audio_array * 32767).astype(np.int16)
#         combined_audio.append(int_audio)

#         # Add 0.5s silence after each segment (except maybe last)
#         silence = np.zeros(int(sample_rate * 0.5), dtype=np.int16)
#         combined_audio.append(silence)

#     # Concatenate all audio segments + silences
#     final_audio = np.concatenate(combined_audio)

#     # Write WAV to in-memory buffer (BytesIO)
#     buffer = io.BytesIO()
#     with wave.open(buffer, 'wb') as wf:
#         wf.setnchannels(1)           # mono
#         wf.setsampwidth(2)           # bytes per sample (16-bit PCM)
#         wf.setframerate(sample_rate) # sample rate
#         wf.writeframes(final_audio.tobytes())

#     # Move pointer to start
#     buffer.seek(0)

#     # Return bytes
#     return buffer.read()


# from transformers import pipeline
# import io
# import wave
# import numpy as np
# import re

# HF_TTS_MODEL = "facebook/mms-tts-eng"

# # Initialize pipeline once globally for efficiency
# tts_pipeline = pipeline("text-to-audio", model=HF_TTS_MODEL)


# def split_text_for_pauses(text):
#     """
#     Split text at punctuation to introduce natural pauses.
#     """
#     segments = re.split(r'([,.!?])', text)
#     combined = []
#     for i in range(0, len(segments) - 1, 2):
#         combined.append(segments[i].strip() + segments[i + 1].strip())
#     if len(segments) % 2 != 0 and segments[-1].strip():
#         combined.append(segments[-1].strip())
#     return combined


# def generate_audio(text, voice=None):
#     """
#     Generate audio bytes from text with optional voice parameter (not used in this basic example).
#     The 'voice' parameter is placeholder to extend multi-voice support.
#     """
#     assert isinstance(text, str), f"Input must be a string, got {type(text)}"

#     segments = split_text_for_pauses(text)

#     sample_rate = 16000  # default sample rate
#     combined_audio = []

#     for seg in segments:
#         if not isinstance(seg, str):
#             seg = str(seg)

#         audio_data = tts_pipeline(seg)
#         audio_array = np.array(audio_data["audio"])

#         if audio_array.ndim > 1:
#             audio_array = audio_array.flatten()

#         sample_rate = audio_data.get("sampling_rate", sample_rate)

#         int_audio = (audio_array * 32767).astype(np.int16)
#         combined_audio.append(int_audio)

#         # Add 0.5s silence as pause
#         silence = np.zeros(int(sample_rate * 0.5), dtype=np.int16)
#         combined_audio.append(silence)

#     final_audio = np.concatenate(combined_audio)

#     buffer = io.BytesIO()
#     with wave.open(buffer, 'wb') as wf:
#         wf.setnchannels(1)
#         wf.setsampwidth(2)  # 16-bit audio
#         wf.setframerate(sample_rate)
#         wf.writeframes(final_audio.tobytes())

#     buffer.seek(0)
#     return buffer.read()


from transformers import pipeline
import io
import wave
import numpy as np
import re

# Mapping for supported languages
LANGUAGE_CODES = {
    "English": "eng",
    "Spanish": "spa",
    "French": "fra"
}

def split_text_for_pauses(text):
    """
    Split text at punctuation marks to add natural pauses in speech.
    """
    segments = re.split(r'([,.!?])', text)
    combined = []
    for i in range(0, len(segments) - 1, 2):
        combined.append(segments[i].strip() + segments[i + 1].strip())
    if len(segments) % 2 != 0 and segments[-1].strip():
        combined.append(segments[-1].strip())
    return combined

def generate_audio(text, voice=None, language="English"):
    """
    Generate TTS audio for given text and language.
    Supports punctuation pauses and multiple languages.
    """
    assert isinstance(text, str), f"Input must be a string, got {type(text)}"

    # Select correct model based on language
    lang_code = LANGUAGE_CODES.get(language, "eng")
    model_name = f"facebook/mms-tts-{lang_code}"

    # Initialize TTS pipeline for the chosen language
    tts_pipeline = pipeline("text-to-audio", model=model_name)

    # Split text for pauses
    segments = split_text_for_pauses(text)

    sample_rate = 16000  # default sample rate
    combined_audio = []

    for seg in segments:
        if not isinstance(seg, str):
            seg = str(seg)

        audio_data = tts_pipeline(seg)
        audio_array = np.array(audio_data["audio"])

        # Flatten if stereo (2D array)
        if audio_array.ndim > 1:
            audio_array = audio_array.flatten()

        sample_rate = audio_data.get("sampling_rate", sample_rate)

        # Convert to 16-bit PCM
        int_audio = (audio_array * 32767).astype(np.int16)
        combined_audio.append(int_audio)

        # Add 0.5 second silence between segments
        silence = np.zeros(int(sample_rate * 0.5), dtype=np.int16)
        combined_audio.append(silence)

    # Concatenate all audio parts
    final_audio = np.concatenate(combined_audio)

    # Write WAV to memory
    buffer = io.BytesIO()
    with wave.open(buffer, 'wb') as wf:
        wf.setnchannels(1)      # mono
        wf.setsampwidth(2)      # 16-bit
        wf.setframerate(sample_rate)
        wf.writeframes(final_audio.tobytes())

    buffer.seek(0)
    return buffer.read()
