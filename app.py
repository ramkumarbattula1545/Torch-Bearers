# import streamlit as st
# import json
# import time

# from modules.sentiment import analyze_sentiment_and_tone
# from modules.rewrite import rewrite_text
# from modules.tts import generate_audio
# from modules.utils import split_chapters
# from modules.ui_custom import apply_custom_css

# apply_custom_css()

# st.title("🎧 EchoVerse - Dynamic GenAI Audiobook Creator")
# st.markdown("Everything handled dynamically via Hugging Face GenAI")

# # Sidebar
# with st.sidebar:
#     st.header("Settings")
#     chapter_split = st.checkbox("Split into chapters", value=False)
#     chapter_length = st.slider("Words per chapter", 500, 2000, 1000, 100) if chapter_split else 1000

# # Input
# col1, col2 = st.columns([1, 1])
# with col1:
#     st.subheader("Input Text")
#     input_method = st.radio("Input method:", ("Paste text", "Upload file"))

#     text = ""
#     if input_method == "Paste text":
#         text = st.text_area("Enter your text here:", height=300)
#     else:
#         uploaded_file = st.file_uploader("Upload a text file", type=["txt"])
#         if uploaded_file:
#             text = uploaded_file.read().decode("utf-8")

#     if text and st.button("Generate Audiobook"):
#         with st.spinner("Processing with GenAI..."):
#             start_time = time.time()

#             # 1. Analyze sentiment + suggest tone
#             sentiment_response = analyze_sentiment_and_tone(text)
#             try:
#                 sentiment_data = json.loads(sentiment_response)
#             except:
#                 sentiment_data = {"sentiment": "neutral", "suggested tone": "neutral"}
#             tone = sentiment_data.get("suggested tone", "neutral")

#             # 2. Rewrite dynamically
#             rewritten_text = rewrite_text(text, tone)

#             # 3. Split chapters if enabled
#             chapters = split_chapters(rewritten_text, chapter_length) if chapter_split else [rewritten_text]

#             # 4. Generate audio dynamically
#             audio_files = [generate_audio(chap) for chap in chapters]

#             # Save session state
#             st.session_state.audio_files = audio_files
#             st.session_state.original_text = text
#             st.session_state.rewritten_text = rewritten_text
#             st.session_state.sentiment = sentiment_data
#             st.session_state.processing_time = time.time() - start_time
#             st.success("Audiobook generated successfully!")

# with col2:
#     if 'audio_files' in st.session_state:
#         st.subheader("Results")
#         st.audio(st.session_state.audio_files[0], format='audio/wav')

#         for i, audio in enumerate(st.session_state.audio_files):
#             st.download_button(
#                 f"Download Chapter {i+1}",
#                 data=audio,
#                 file_name=f"chapter_{i+1}.wav",
#                 mime="audio/wav"
#             )

#         # Text comparison
#         st.subheader("Text Comparison")
#         col_o, col_r = st.columns(2)
#         with col_o:
#             st.markdown("**Original Text**")
#             st.text_area("", st.session_state.original_text, height=200)
#         with col_r:
#             st.markdown("**Adapted Text**")
#             st.text_area("", st.session_state.rewritten_text, height=200)

#         # Metrics
#         st.subheader("Performance Metrics")
#         metrics = [
#             ["Original Length", len(st.session_state.original_text.split())],
#             ["Adapted Length", len(st.session_state.rewritten_text.split())],
#             ["Processing Time", f"{st.session_state.processing_time:.2f} sec"],
#             ["Chapters Generated", len(st.session_state.audio_files)]
#         ]
#         st.table(metrics)

#         # Sentiment visualization (bar chart without pandas/plotly)
#         st.subheader("Text Sentiment Analysis")
#         sentiment_scores = {
#             "positive": 1 if sentiment_data.get("sentiment") == "positive" else 0,
#             "negative": 1 if sentiment_data.get("sentiment") == "negative" else 0,
#             "neutral": 1 if sentiment_data.get("sentiment") == "neutral" else 0,
#         }
#         st.bar_chart([list(sentiment_scores.values())], height=200)




# import streamlit as st
# import json
# import time

# from modules.sentiment import analyze_sentiment_and_tone
# from modules.rewrite import rewrite_text
# from modules.tts import generate_audio
# from modules.utils import split_chapters, generate_diff_html
# from modules.ui_custom import apply_custom_css

# # Apply global mesmerizing CSS
# apply_custom_css()

# # ---- Title Section ----
# st.markdown("""
# <div class="main-title">
#     <h1>🎧 EchoVerse</h1>
#     <p>Dynamic GenAI Audiobook Creator</p>
# </div>
# """, unsafe_allow_html=True)

# # Sidebar
# with st.sidebar:
#     st.markdown("<h2 style='text-align:center;'>⚙️ Settings</h2>", unsafe_allow_html=True)
#     chapter_split = st.checkbox("Split into chapters", value=False)
#     chapter_length = st.slider("Words per chapter", 500, 2000, 1000, 100) if chapter_split else 1000

# # Input and Results
# col1, col2 = st.columns([1, 1])

# with col1:
#     st.markdown("<h3 class='section-title'>📜 Input Text</h3>", unsafe_allow_html=True)
#     input_method = st.radio("Input method:", ("Paste text", "Upload file"), horizontal=True)

#     text = ""
#     if input_method == "Paste text":
#         text = st.text_area("Enter your text here:", height=300, placeholder="Paste or type your story/content...")
#     else:
#         uploaded_file = st.file_uploader("Upload a text file", type=["txt"])
#         if uploaded_file:
#             text = uploaded_file.read().decode("utf-8")

#     if text and st.button("🚀 Generate Audiobook", use_container_width=True):
#         with st.spinner("Generating Audiobook with AI magic... ✨"):
#             start_time = time.time()

#             # 1. Analyze sentiment and tone
#             sentiment_response = analyze_sentiment_and_tone(text)
#             try:
#                 sentiment_data = json.loads(sentiment_response)
#             except:
#                 sentiment_data = {"sentiment": "neutral", "suggested tone": "neutral"}
#             tone = sentiment_data.get("suggested tone", "neutral")

#             # 2. Rewrite dynamically
#             rewritten_text = rewrite_text(text, tone)

#             # 3. Split chapters if enabled
#             chapters = split_chapters(rewritten_text, chapter_length) if chapter_split else [rewritten_text]

#             # 4. Generate audio
#             audio_files = [generate_audio(chap) for chap in chapters]

#             # Save session state
#             st.session_state.audio_files = audio_files
#             st.session_state.original_text = text
#             st.session_state.rewritten_text = rewritten_text
#             st.session_state.sentiment = sentiment_data
#             st.session_state.processing_time = time.time() - start_time
#             st.success("Audiobook generated successfully! 🎉")

# with col2:
#     if 'audio_files' in st.session_state:
#         # Audio player
#         st.markdown("<h3 class='section-title'>🎵 Listen</h3>", unsafe_allow_html=True)
#         st.audio(st.session_state.audio_files[0], format='audio/wav')

#         # Download buttons
#         for i, audio in enumerate(st.session_state.audio_files):
#             st.download_button(
#                 f"⬇️ Download Chapter {i+1}",
#                 data=audio,
#                 file_name=f"chapter_{i+1}.wav",
#                 mime="audio/wav",
#                 use_container_width=True
#             )

#         # Text comparison with scrollable, highlighted diff
#         st.markdown("<h3 class='section-title'>📝 Text Comparison</h3>", unsafe_allow_html=True)
#         diff_html = generate_diff_html(st.session_state.original_text, st.session_state.rewritten_text)
#         st.markdown(f"<div class='diff-box'>{diff_html}</div>", unsafe_allow_html=True)

#         # Metrics in cards
#         st.markdown("<h3 class='section-title'>📊 Performance Metrics</h3>", unsafe_allow_html=True)
#         metric_cols = st.columns(4)
#         metrics = [
#             ("Original Length", len(st.session_state.original_text.split())),
#             ("Adapted Length", len(st.session_state.rewritten_text.split())),
#             ("Processing Time", f"{st.session_state.processing_time:.2f}s"),
#             ("Chapters", len(st.session_state.audio_files))
#         ]
#         for col, (label, value) in zip(metric_cols, metrics):
#             col.markdown(f"""
#             <div class="metric-card">
#                 <h4>{label}</h4>
#                 <p>{value}</p>
#             </div>
#             """, unsafe_allow_html=True)

#         # Sentiment visualization
#         st.markdown("<h3 class='section-title'>💡 Sentiment Analysis</h3>", unsafe_allow_html=True)
#         sentiment_scores = {
#             "positive": 1 if st.session_state.sentiment.get("sentiment") == "positive" else 0,
#             "negative": 1 if st.session_state.sentiment.get("sentiment") == "negative" else 0,
#             "neutral": 1 if st.session_state.sentiment.get("sentiment") == "neutral" else 0,
#         }
#         st.bar_chart([list(sentiment_scores.values())], height=200)


# import streamlit as st
# import json
# import time

# from modules.sentiment import analyze_sentiment_and_tone
# from modules.rewrite import rewrite_text
# from modules.tts import generate_audio
# from modules.utils import split_chapters, generate_diff_html
# from modules.ui_custom import apply_custom_css
# import streamlit as st

def rerun_app():
    try:
        st.experimental_rerun()
    except AttributeError:
        # Older versions fallback: do nothing or print a warning
        pass

# # Set page config to wide for full-screen layout
# st.set_page_config(layout="wide", page_title="EchoVerse Audiobook Creator", page_icon="🎧")

# # Apply custom CSS styles
# apply_custom_css()

# # --- Session State for page navigation ---
# if "page" not in st.session_state:
#     st.session_state.page = "input"

# if "audio_files" not in st.session_state:
#     st.session_state.audio_files = []

# if "original_text" not in st.session_state:
#     st.session_state.original_text = ""

# if "rewritten_text" not in st.session_state:
#     st.session_state.rewritten_text = ""

# # --- Title ---
# st.markdown("""
# <div class="main-title">
#     <h1>🎧 EchoVerse</h1>
#     <p>Dynamic GenAI Audiobook Creator</p>
# </div>
# """, unsafe_allow_html=True)

# # Sidebar (always visible for settings)
# with st.sidebar:
#     st.markdown("<h2 style='text-align:center;'>⚙️ Settings</h2>", unsafe_allow_html=True)
#     chapter_split = st.checkbox("Split into chapters", value=False)
#     chapter_length = st.slider("Words per chapter", 500, 2000, 1000, 100) if chapter_split else 1000
#     st.markdown("---")
#     if st.session_state.page == "output":
#         if st.button("⬅️ Back to Input", use_container_width=True):
#             st.session_state.page = "input"
#             rerun_app()


# # --- Input Page ---
# if st.session_state.page == "input":
#     # Inputs and generate button side by side with wide columns
#     col1, col2 = st.columns([3, 2], gap="large")

#     with col1:
#         st.markdown("<h3 class='section-title'>📜 Input Text</h3>", unsafe_allow_html=True)
#         input_method = st.radio("Input method:", ("Paste text", "Upload file"), horizontal=True)

#         text = ""
#         if input_method == "Paste text":
#             text = st.text_area(
#                 "Enter your text here:",
#                 height=350,
#                 placeholder="Paste or type your story/content here...",
#                 key="input_text_area",
#                 help="Type or paste your story, article, or any text you want to convert to an audiobook."
#             )
#         else:
#             uploaded_file = st.file_uploader("Upload a text file", type=["txt"])
#             if uploaded_file:
#                 text = uploaded_file.read().decode("utf-8")
#                 # Prefill text area with uploaded content for editing or confirmation
#                 st.text_area(
#                     "Preview uploaded content:",
#                     value=text,
#                     height=300,
#                     disabled=True
#                 )

#         # Generate button
#         if st.button("🚀 Generate Audiobook", use_container_width=True) and (text.strip() != ""):
#             with st.spinner("Generating Audiobook with AI magic... ✨"):
#                 start_time = time.time()

#                 # Analyze sentiment and tone (for adaptive rewriting)
#                 sentiment_response = analyze_sentiment_and_tone(text)
#                 try:
#                     sentiment_data = json.loads(sentiment_response)
#                 except Exception:
#                     sentiment_data = {"sentiment": "neutral", "suggested tone": "neutral"}
#                 tone = sentiment_data.get("suggested tone", "neutral")

#                 # Rewrite text dynamically with tone
#                 rewritten_text = rewrite_text(text, tone)

#                 # Split chapters if enabled
#                 chapters = split_chapters(rewritten_text, chapter_length) if chapter_split else [rewritten_text]

#                 # Generate audio files for each chapter
#                 audio_files = [generate_audio(chap) for chap in chapters]

#                 # Store into session state
#                 st.session_state.audio_files = audio_files
#                 st.session_state.original_text = text
#                 st.session_state.rewritten_text = rewritten_text

#                 # Switch to output page
#                 st.session_state.page = "output"

#                 rerun_app()

#     with col2:
#         # Optionally add some info or inspirational quote or instructions here
#         st.markdown(
#             """
#             <div class="description-box" style="font-style: italic; text-align:center;">
#                 <b>Tip:</b><br>
#                 Use the input box to paste any text. You can split long text into chapters using the sidebar option.<br>
#                 Click "Generate Audiobook" to transform your text into dynamic, adaptive audiobooks.<br>
#                 The output will appear on the next screen.
#             </div>
#             """,
#             unsafe_allow_html=True
#         )

# # --- Output Page ---
# elif st.session_state.page == "output":
#     col1, col2 = st.columns([3,2], gap="large")
#     with col1:
#         st.markdown("<h3 class='section-title'>🎵 Listen</h3>", unsafe_allow_html=True)
#         # Play first audio file by default
#         st.audio(st.session_state.audio_files[0], format='audio/wav')

#         # Show download buttons for chapters
#         for idx, audio in enumerate(st.session_state.audio_files):
#             st.download_button(
#                 label=f"⬇️ Download Chapter {idx + 1}",
#                 data=audio,
#                 file_name=f"chapter_{idx + 1}.wav",
#                 mime="audio/wav",
#                 use_container_width=True
#             )

#         # Text comparison with highlighted differences
#         st.markdown("<h3 class='section-title'>📝 Text Comparison</h3>", unsafe_allow_html=True)
#         diff_html = generate_diff_html(st.session_state.original_text, st.session_state.rewritten_text)
#         st.markdown(f"<div class='diff-box'>{diff_html}</div>", unsafe_allow_html=True)

#         # Show the AI adapted rewritten text clearly
#         st.markdown(
#             "<div class='description-box'><b>AI Adapted Text:</b><br>" +
#             st.session_state.rewritten_text.replace("\n", "<br>") +
#             "</div>",
#             unsafe_allow_html=True
#         )

#     with col2:
#         # Could add helpful tips or instructions on this side if desired
#         st.markdown(
#             """
#             <div class="description-box" style="font-style: italic; text-align:center;">
#             <b>Pro Tip:</b><br>
#             Use the audio players and download buttons to listen to or save your chapters.<br>
#             Click the Back button in the sidebar to return and generate another audiobook.<br>
#             </div>
#             """,
#             unsafe_allow_html=True
#         )

# import streamlit as st
# import json
# import time

# from modules.sentiment import analyze_sentiment_and_tone  # Optional: you can skip if unused
# from modules.rewrite import rewrite_text
# from modules.tts import generate_audio
# from modules.utils import split_chapters, generate_diff_html
# from modules.ui_custom import apply_custom_css

# # Set wide layout and page config
# st.set_page_config(layout="wide", page_title="EchoVerse Audiobook Creator", page_icon="🎧")

# # Apply custom CSS styles (keep your ui_custom.py)
# apply_custom_css()

# # Initialize session state variables
# if "page" not in st.session_state:
#     st.session_state.page = "input"

# if "audio_files" not in st.session_state:
#     st.session_state.audio_files = {"suspenseful": [], "neutral": [], "professional": []}

# if "original_text" not in st.session_state:
#     st.session_state.original_text = ""

# if "rewritten_texts" not in st.session_state:
#     st.session_state.rewritten_texts = {}

# # Title section
# st.markdown("""
# <div class="main-title">
#     <h1>🎧 EchoVerse</h1>
#     <p>Dynamic GenAI Audiobook Creator</p>
# </div>
# """, unsafe_allow_html=True)

# # Sidebar for settings and back button
# with st.sidebar:
#     st.markdown("<h2 style='text-align:center;'>⚙️ Settings</h2>", unsafe_allow_html=True)
#     chapter_split = st.checkbox("Split into chapters", value=False)
#     chapter_length = st.slider("Words per chapter", 500, 2000, 1000, 100) if chapter_split else 1000
#     st.markdown("---")
#     if st.session_state.page == "output":
#         if st.button("⬅️ Back to Input", use_container_width=True):
#             st.session_state.page = "input"
#             rerun_app()

# # Input Page
# if st.session_state.page == "input":
#     col1, col2 = st.columns([3, 2], gap="large")
#     with col1:
#         st.markdown("<h3 class='section-title'>📜 Input Text</h3>", unsafe_allow_html=True)
#         input_method = st.radio("Input method:", ("Paste text", "Upload file"), horizontal=True)

#         text = ""
#         if input_method == "Paste text":
#             text = st.text_area(
#                 "Enter your text here:",
#                 height=350,
#                 placeholder="Paste or type your story/content here...",
#                 key="input_text_area",
#                 help="Type or paste your story, article, or any text you want to convert to an audiobook."
#             )
#         else:
#             uploaded_file = st.file_uploader("Upload a text file", type=["txt"])
#             if uploaded_file:
#                 text = uploaded_file.read().decode("utf-8")
#                 st.text_area(
#                     "Preview uploaded content:",
#                     value=text,
#                     height=300,
#                     disabled=True
#                 )

#         if st.button("🚀 Generate Audiobook", use_container_width=True) and (text.strip() != ""):
#             with st.spinner("Generating Audiobook with AI magic... ✨"):
#                 # Optional: sentiment for tone detection - can be skipped or used for other logic
#                 sentiment_response = analyze_sentiment_and_tone(text)
#                 try:
#                     sentiment_data = json.loads(sentiment_response)
#                 except Exception:
#                     sentiment_data = {"sentiment": "neutral", "suggested tone": "neutral"}

#                 # Generate 3 adaptive rewrites at once
#                 rewritten_texts = rewrite_text(text)

#                 # Generate audio for each tone, possibly split into chapters
#                 audio_files = {}
#                 for tone_name, rewritten_text in rewritten_texts.items():
#                     chapters = split_chapters(rewritten_text, chapter_length) if chapter_split else [rewritten_text]
#                     # generate_audio must accept voice param to differentiate voices
#                     audio_files[tone_name] = [generate_audio(chap) for chap in chapters]


#                 # Save all in session state
#                 st.session_state.audio_files = audio_files
#                 st.session_state.original_text = text
#                 st.session_state.rewritten_texts = rewritten_texts

#                 st.session_state.page = "output"
#                 rerun_app()

#     with col2:
#         st.markdown(
#             """
#             <div class="description-box" style="font-style: italic; text-align:center;">
#                 <b>Tip:</b><br>
#                 Paste or upload your text here.<br>
#                 Choose to split long texts into chapters.<br>
#                 Click "Generate Audiobook" to see Suspenseful, Neutral, and Professional rewrites.<br>
#                 Audio generated separately for each tone with distinct voices.
#             </div>
#             """,
#             unsafe_allow_html=True
#         )

# # Output Page
# elif st.session_state.page == "output":
#     col1, col2 = st.columns([3, 2], gap="large")

#     with col1:
#         st.markdown("<h3 class='section-title'>🎵 Listen & Download</h3>", unsafe_allow_html=True)
#         for tone_name in ["suspenseful", "neutral", "professional"]:
#             st.markdown(f"### {tone_name.capitalize()} Voice Audio")
#             audio_chapters = st.session_state.audio_files.get(tone_name, [])
#             if audio_chapters:
#                 # Audio player for first chapter, please implement advanced player if you want multiple playback
#                 st.audio(audio_chapters[0], format="audio/wav")
#                 # Download buttons for all chapters per tone
#                 for idx, audio in enumerate(audio_chapters):
#                     st.download_button(
#                         label=f"⬇️ Download {tone_name.capitalize()} Chapter {idx + 1}",
#                         data=audio,
#                         file_name=f"{tone_name}_chapter_{idx + 1}.wav",
#                         mime="audio/wav",
#                         use_container_width=True,
#                     )
#             else:
#                 st.info(f"No audio generated for {tone_name} voice.")

#         st.markdown("<h3 class='section-title'>📝 Text Comparison (Original vs Suspenseful)</h3>", unsafe_allow_html=True)
#         diff_html = generate_diff_html(st.session_state.original_text, st.session_state.rewritten_texts.get("suspenseful", ""))
#         st.markdown(f"<div class='diff-box'>{diff_html}</div>", unsafe_allow_html=True)

#         st.markdown("<h3 class='section-title'>🎭 AI Adaptive Rewrites</h3>", unsafe_allow_html=True)
#         for tone_name in ["suspenseful", "neutral", "professional"]:
#             st.markdown(f"<h4>{tone_name.capitalize()} Version</h4>", unsafe_allow_html=True)
#             text_version = st.session_state.rewritten_texts.get(tone_name, "")
#             st.markdown(f"<div class='description-box'>{text_version.replace(chr(10), '<br>')}</div>", unsafe_allow_html=True)

#     with col2:
#         st.markdown(
#             """
#             <div class="description-box" style="font-style: italic; text-align:center;">
#                 <b>Pro Tip:</b><br>
#                 Listen or download each tone’s audiobook separately.<br>
#                 Review all rewritten text versions side by side.<br>
#                 Use the Back button in the sidebar to generate again.
#             </div>
#             """,
#             unsafe_allow_html=True
#         )

# import streamlit as st
# import json
# import time

# from modules.sentiment import analyze_sentiment_and_tone  # optional for tone detection
# from modules.rewrite import rewrite_text
# from modules.tts import generate_audio
# from modules.utils import split_chapters, generate_diff_html
# from modules.ui_custom import apply_custom_css

# st.set_page_config(layout="wide", page_title="EchoVerse Audiobook Creator", page_icon="🎧")

# apply_custom_css()

# if "page" not in st.session_state:
#     st.session_state.page = "input"

# if "audio_files" not in st.session_state:
#     st.session_state.audio_files = {"suspenseful": [], "neutral": [], "professional": []}

# if "original_text" not in st.session_state:
#     st.session_state.original_text = ""

# if "rewritten_texts" not in st.session_state:
#     st.session_state.rewritten_texts = {}

# st.markdown("""
# <div class="main-title">
#     <h1>🎧 EchoVerse</h1>
#     <p>Dynamic GenAI Audiobook Creator</p>
# </div>
# """, unsafe_allow_html=True)

# with st.sidebar:
#     st.markdown("<h2 style='text-align:center;'>⚙️ Settings</h2>", unsafe_allow_html=True)
#     chapter_split = st.checkbox("Split into chapters", value=False)
#     chapter_length = st.slider("Words per chapter", 500, 2000, 1000, 100) if chapter_split else 1000

#     st.markdown("---")
#     if st.session_state.page == "output":
#         if st.button("⬅️ Back to Input", use_container_width=True):
#             st.session_state.page = "input"
#             rerun_app()

# if st.session_state.page == "input":
#     col1, col2 = st.columns([3, 2], gap="large")
#     with col1:
#         st.markdown("<h3 class='section-title'>📜 Input Text</h3>", unsafe_allow_html=True)
#         input_method = st.radio("Input method:", ("Paste text", "Upload file"), horizontal=True)

#         text = ""
#         if input_method == "Paste text":
#             text = st.text_area(
#                 "Enter your text here:",
#                 height=350,
#                 placeholder="Paste or type your story/content here...",
#                 key="input_text_area",
#                 help="Type or paste your story, article, or any text you want to convert to an audiobook."
#             )
#         else:
#             uploaded_file = st.file_uploader("Upload a text file", type=["txt"])
#             if uploaded_file:
#                 text = uploaded_file.read().decode("utf-8")
#                 st.text_area(
#                     "Preview uploaded content:",
#                     value=text,
#                     height=300,
#                     disabled=True
#                 )

#         if st.button("🚀 Generate Audiobook", use_container_width=True) and (text.strip() != ""):
#             with st.spinner("Generating Audiobook with AI magic... ✨"):
#                 # Optional sentiment/tone analysis
#                 sentiment_response = analyze_sentiment_and_tone(text)
#                 try:
#                     sentiment_data = json.loads(sentiment_response)
#                 except Exception:
#                     sentiment_data = {"sentiment": "neutral", "suggested tone": "neutral"}

#                 # Get all 3 adaptive rewrites
#                 rewritten_texts = rewrite_text(text)

#                 # Generate audio files for each tone
#                 audio_files = {}
#                 for tone_name, rewritten_text in rewritten_texts.items():
#                     chapters = split_chapters(rewritten_text, chapter_length) if chapter_split else [rewritten_text]
#                     # Pass tone_name as voice param to generate_audio (extend if needed)
#                     audio_files[tone_name] = [generate_audio(chap, voice=tone_name) for chap in chapters]

#                 st.session_state.audio_files = audio_files
#                 st.session_state.original_text = text
#                 st.session_state.rewritten_texts = rewritten_texts

#                 st.session_state.page = "output"
#                 rerun_app()

#     with col2:
#         st.markdown(
#             """
#             <div class="description-box" style="font-style: italic; text-align:center;">
#                 <b>Tip:</b><br>
#                 Paste or upload your text here.<br>
#                 Choose to split long texts into chapters.<br>
#                 Click "Generate Audiobook" to get Suspenseful, Neutral, and Professional rewrites.<br>
#                 Generate audio with distinct voices per tone.
#             </div>
#             """,
#             unsafe_allow_html=True
#         )

# elif st.session_state.page == "output":
#     col1, col2 = st.columns([3, 2], gap="large")
#     with col1:
#         st.markdown("<h3 class='section-title'>🎵 Listen & Download</h3>", unsafe_allow_html=True)
#         for tone_name in ["suspenseful", "neutral", "professional"]:
#             st.markdown(f"### {tone_name.capitalize()} Voice Audio")
#             audio_chapters = st.session_state.audio_files.get(tone_name, [])
#             if audio_chapters:
#                 st.audio(audio_chapters[0], format="audio/wav")
#                 for idx, audio in enumerate(audio_chapters):
#                     st.download_button(
#                         label=f"⬇️ Download {tone_name.capitalize()} Chapter {idx + 1}",
#                         data=audio,
#                         file_name=f"{tone_name}_chapter_{idx + 1}.wav",
#                         mime="audio/wav",
#                         use_container_width=True,
#                     )
#             else:
#                 st.info(f"No audio generated for {tone_name} voice.")

#         st.markdown("<h3 class='section-title'>📝 Text Comparison (Original vs Suspenseful)</h3>", unsafe_allow_html=True)
#         diff_html = generate_diff_html(st.session_state.original_text, st.session_state.rewritten_texts.get("suspenseful", ""))
#         st.markdown(f"<div class='diff-box'>{diff_html}</div>", unsafe_allow_html=True)

#         st.markdown("<h3 class='section-title'>🎭 AI Adaptive Rewrites</h3>", unsafe_allow_html=True)
#         for tone_name in ["suspenseful", "neutral", "professional"]:
#             st.markdown(f"<h4>{tone_name.capitalize()} Version</h4>", unsafe_allow_html=True)
#             text_version = st.session_state.rewritten_texts.get(tone_name, "")
#             st.markdown(f"<div class='description-box'>{text_version.replace(chr(10), '<br>')}</div>", unsafe_allow_html=True)

#     with col2:
#         st.markdown(
#             """
#             <div class="description-box" style="font-style: italic; text-align:center;">
#                 <b>Pro Tip:</b><br>
#                 Listen or download each tone’s audiobook.<br>
#                 Review rewritten text versions side by side.<br>
#                 Use the sidebar Back button to generate again.
#             </div>
#             """,
#             unsafe_allow_html=True
#         )
import streamlit as st
import json
import time

from modules.sentiment import analyze_sentiment_and_tone
from modules.rewrite import rewrite_text
from modules.tts import generate_audio
from modules.utils import split_chapters, generate_diff_html
from modules.ui_custom import apply_custom_css
from modules.translate import translate_text  # NEW MODULE

st.set_page_config(layout="wide", page_title="EchoVerse Audiobook Creator", page_icon="🎧")

apply_custom_css()

# Session State Initialization
if "page" not in st.session_state:
    st.session_state.page = "input"

if "audio_files" not in st.session_state:
    st.session_state.audio_files = {"suspenseful": [], "neutral": [], "professional": []}

if "original_text" not in st.session_state:
    st.session_state.original_text = ""

if "rewritten_texts" not in st.session_state:
    st.session_state.rewritten_texts = {}

if "selected_language" not in st.session_state:
    st.session_state.selected_language = "English"

# Title
st.markdown("""
<div class="main-title">
    <h1>🎧 EchoVerse</h1>
    <p>Dynamic GenAI Audiobook Creator with Multi-Language Support</p>
</div>
""", unsafe_allow_html=True)

# Sidebar Settings
with st.sidebar:
    st.markdown("<h2 style='text-align:center;'>⚙️ Settings</h2>", unsafe_allow_html=True)
    chapter_split = st.checkbox("Split into chapters", value=False)
    chapter_length = st.slider("Words per chapter", 500, 2000, 1000, 100) if chapter_split else 1000

    # Language Selection
    st.markdown("### 🌐 Select Language")
    language = st.selectbox(
        "Choose Audiobook Language",
        ["English",  "Spanish", "French"],
        index=0
    )
    st.session_state.selected_language = language

    st.markdown("---")
    if st.session_state.page == "output":
        if st.button("⬅️ Back to Input", use_container_width=True):
            st.session_state.page = "input"
            st.rerun()

# Input Page
if st.session_state.page == "input":
    col1, col2 = st.columns([3, 2], gap="large")
    with col1:
        st.markdown("<h3 class='section-title'>📜 Input Text</h3>", unsafe_allow_html=True)
        input_method = st.radio("Input method:", ("Paste text", "Upload file"), horizontal=True)

        text = ""
        if input_method == "Paste text":
            text = st.text_area(
                "Enter your text here:",
                height=350,
                placeholder="Paste or type your story/content here...",
                key="input_text_area",
                help="Type or paste your story, article, or any text you want to convert to an audiobook."
            )
        else:
            uploaded_file = st.file_uploader("Upload a text file", type=["txt"])
            if uploaded_file:
                text = uploaded_file.read().decode("utf-8")
                st.text_area("Preview uploaded content:", value=text, height=300, disabled=True)

        if st.button("🚀 Generate Audiobook", use_container_width=True) and (text.strip() != ""):
            with st.spinner("Generating Audiobook with AI magic... ✨"):
                # Step 1: Translate if not English
                # Step 1: Translate if not English
                translated_text = text
                if language in ["Spanish", "French"]:
                    translated_text = translate_text(text, target_lang=language)


                # Step 2: Sentiment & Tone (optional)
                sentiment_response = analyze_sentiment_and_tone(translated_text)
                try:
                    sentiment_data = json.loads(sentiment_response)
                except Exception:
                    sentiment_data = {"sentiment": "neutral", "suggested tone": "neutral"}

                # Step 3: Adaptive Rewrites
                rewritten_texts = rewrite_text(translated_text)

                # Step 4: Generate Audio for each tone
                audio_files = {}
                for tone_name, rewritten_text in rewritten_texts.items():
                    chapters = split_chapters(rewritten_text, chapter_length) if chapter_split else [rewritten_text]
                    audio_files[tone_name] = [generate_audio(chap, voice=tone_name) for chap in chapters]
                st.session_state.audio_files = audio_files
                st.session_state.original_text = translated_text
                st.session_state.rewritten_texts = rewritten_texts
                st.session_state.page = "output"
                st.rerun()

    with col2:
        st.markdown(
            """
            <div class="description-box" style="font-style: italic; text-align:center;">
                <b>Tip:</b><br>
                Select your preferred language.<br>
                Paste or upload text, split into chapters if needed.<br>
                Click Generate to create multi-tone audiobook.
            </div>
            """,
            unsafe_allow_html=True
        )

# Output Page
elif st.session_state.page == "output":
    col1, col2 = st.columns([3, 2], gap="large")
    with col1:
        st.markdown("<h3 class='section-title'>🎵 Listen & Download</h3>", unsafe_allow_html=True)
        for tone_name in ["suspenseful", "neutral", "professional"]:
            st.markdown(f"### {tone_name.capitalize()} Voice Audio")
            audio_chapters = st.session_state.audio_files.get(tone_name, [])
            if audio_chapters:
                st.audio(audio_chapters[0], format="audio/wav")
                for idx, audio in enumerate(audio_chapters):
                    st.download_button(
                        label=f"⬇️ Download {tone_name.capitalize()} Chapter {idx + 1}",
                        data=audio,
                        file_name=f"{tone_name}_chapter_{idx + 1}.wav",
                        mime="audio/wav",
                        use_container_width=True,
                    )
            else:
                st.info(f"No audio generated for {tone_name} voice.")

        st.markdown("<h3 class='section-title'>📝 Text Comparison (Original vs Suspenseful)</h3>", unsafe_allow_html=True)
        diff_html = generate_diff_html(st.session_state.original_text, st.session_state.rewritten_texts.get("suspenseful", ""))
        st.markdown(f"<div class='diff-box'>{diff_html}</div>", unsafe_allow_html=True)

        st.markdown("<h3 class='section-title'>🎭 AI Adaptive Rewrites</h3>", unsafe_allow_html=True)
        for tone_name in ["suspenseful", "neutral", "professional"]:
            st.markdown(f"<h4>{tone_name.capitalize()} Version</h4>", unsafe_allow_html=True)
            text_version = st.session_state.rewritten_texts.get(tone_name, "")
            st.markdown(f"<div class='description-box'>{text_version.replace(chr(10), '<br>')}</div>", unsafe_allow_html=True)

    with col2:
        st.markdown(
            """
            <div class="description-box" style="font-style: italic; text-align:center;">
                <b>Pro Tip:</b><br>
                Listen or download each tone’s audiobook.<br>
                Compare original and adaptive rewrites.<br>
                Use sidebar to go back and regenerate.
            </div>
            """,
            unsafe_allow_html=True
        )
