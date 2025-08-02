# # modules/ui_custom.py
# import streamlit as st

# def apply_custom_css():
#     st.markdown("""
#     <style>
#     .main {background-color: #f8f9fa;}
#     .stTextArea textarea {font-size: 16px !important;}
#     .stButton>button {background-color: #4CAF50; color: white;}
#     .stDownloadButton>button {background-color: #2196F3; color: white;}
#     .sidebar .sidebar-content {background-color: #e9f5ff;}
#     </style>
#     """, unsafe_allow_html=True)

# import streamlit as st

# def apply_custom_css():
#     st.markdown("""
#     <style>
#     /* Main background gradient animation */
#     .main {
#         background: linear-gradient(-45deg, #ff9a9e, #fad0c4, #a1c4fd, #c2e9fb);
#         background-size: 400% 400%;
#         animation: gradientBG 15s ease infinite;
#     }

#     @keyframes gradientBG {
#         0% {background-position: 0% 50%;}
#         50% {background-position: 100% 50%;}
#         100% {background-position: 0% 50%;}
#     }

#     /* Glass effect for cards (text areas, results) */
#     .glass-card {
#         background: rgba(255, 255, 255, 0.15);
#         border-radius: 16px;
#         padding: 15px;
#         box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
#         backdrop-filter: blur(8px);
#         -webkit-backdrop-filter: blur(8px);
#         border: 1px solid rgba(255, 255, 255, 0.18);
#         margin-bottom: 20px;
#     }

#     /* Text areas styling */
#     .stTextArea textarea {
#         font-size: 16px !important;
#         color: #333 !important;
#         border-radius: 10px;
#         border: 2px solid #fff;
#         background: rgba(255,255,255,0.7);
#         box-shadow: inset 0 2px 4px rgba(0,0,0,0.1);
#     }

#     /* Buttons with hover and pop animation */
#     .stButton>button, .stDownloadButton>button {
#         background: linear-gradient(to right, #ff9966, #ff5e62);
#         color: white;
#         border: none;
#         border-radius: 30px;
#         padding: 0.6em 1.2em;
#         font-size: 16px;
#         transition: all 0.3s ease-in-out;
#         box-shadow: 0px 4px 10px rgba(0,0,0,0.2);
#     }
#     .stButton>button:hover, .stDownloadButton>button:hover {
#         transform: scale(1.07);
#         box-shadow: 0px 6px 14px rgba(0,0,0,0.3);
#         background: linear-gradient(to right, #ff5e62, #ff9966);
#     }

#     /* Sidebar customization */
#     section[data-testid="stSidebar"] {
#         background: rgba(255, 255, 255, 0.2);
#         backdrop-filter: blur(8px);
#         border-right: 2px solid rgba(255,255,255,0.3);
#     }

#     /* Table metrics styling */
#     .stTable {
#         border-radius: 12px;
#         overflow: hidden;
#         box-shadow: 0px 4px 15px rgba(0,0,0,0.1);
#     }
#     /* Diff Highlight Styling */
# span[style*="green"] {
#     background-color: #d4fcd4;
#     padding: 2px 4px;
#     border-radius: 4px;
# }
# span[style*="red"] {
#     background-color: #fcd4d4;
#     padding: 2px 4px;
#     border-radius: 4px;
# }

#     </style>
#     """, unsafe_allow_html=True)



# import streamlit as st

# def apply_custom_css():
#     st.markdown("""
#     <style>
#     /* App container full size with light blue gradient background */
#     .stApp {
#         background: linear-gradient(135deg, #e6f0ff 0%, #b5e6fa 100%);
#         min-height: 100vh;
#         min-width: 100vw;
#         padding: 0 !important;
#         margin: 0 !important;
#         overflow-x: hidden;
#     }

#     /* Base font styling and scaling */
#     body, .main, .stApp, .description-box, .section-title, 
#     .stButton>button, .stDownloadButton>button {
#         font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
#         font-size: 1.22rem;
#         color: #222222;
#     }


#     /* Main title: big gradient pink-red text with subtle shadow */
#     .main-title h1 {
#         font-size: 4rem;
#         text-align: center;
#         background: linear-gradient(90deg, #ff6a00 15%, #ee0979 85%);
#         -webkit-background-clip: text;
#         -webkit-text-fill-color: transparent;
#         margin-bottom: 0.1em;
#         letter-spacing: 2px;
#         text-shadow: 2px 2px 8px rgba(238, 9, 121, 0.4);
#     }
#     .main-title p {
#         font-size: 1.2rem;
#         text-align: center;
#         color: #ee0979;
#         margin-bottom: 2em;
#         font-weight: 600;
#     }

#     /* Section titles in warm pink/orange to match button pallet */
#     .section-title {
#         font-size: 1.5rem;
#         margin-top: 1em;
#         margin-bottom: 0.5em;
#         color: #ff6a00;
#         text-shadow: 1px 1px 4px rgba(255, 106, 0, 0.35);
#         font-weight: 600;
#     }

#     /* Text area: pastel gradient pink/orange */
#     .stTextArea textarea {
#         background: linear-gradient(135deg, #ffe29f 10%, #ffa99f 80%);
#         border: none;
#         border-radius: 18px;
#         font-size: 1.1rem !important;
#         color: #392785;
#         padding: 1.2em;
#         box-shadow: 0 2px 12px rgba(60, 21, 75, 0.12);
#         font-weight: 550;
#         resize: vertical;
#     }

#     /* Buttons - retain pink to blue gradient with smooth hover */
#     .stButton>button, .stDownloadButton>button {
#         background: linear-gradient(90deg, #ff6a00, #ee0979);
#         color: white;
#         border: none;
#         border-radius: 25px;
#         font-size: 1.1rem;
#         font-weight: bold;
#         padding: 0.7em 1.4em;
#         box-shadow: 0 5px 20px rgba(238, 9, 121, 0.18);
#         transition: transform 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
#         margin-top: 0.6em;
#         width: 100%;
#         cursor: pointer;
#     }
#     .stButton>button:hover, .stDownloadButton>button:hover {
#         transform: translateY(-2px) scale(1.02);
#         box-shadow: 0 8px 28px rgba(252,106,0,0.28);
#         background: linear-gradient(90deg, #3f5efb, #fc466b);
#     }

#     /* Description and output boxes: pastel pink to blue gradient */
#     .description-box {
#         background: linear-gradient(120deg, #c3bef0 30%, #8ec5fc 100%);
#         color: #2e1a63;
#         border-radius: 14px;
#         padding: 1.1em;
#         margin-top: 1em;
#         font-size: 1.1rem;
#         box-shadow: 0 2px 12px rgba(64, 56, 192, 0.15);
#         white-space: pre-wrap;
#     }

#     /* Diff Box styling reflecting the pastel output colors */
#     .diff-box {
#         background: rgba(140, 197, 252, 0.15);
#         border-radius: 10px;
#         padding: 1em;
#         max-height: 250px;
#         overflow-y: auto;
#         border: 1px solid rgba(130, 130, 255, 0.3);
#         font-size: 1.05rem;
#         color: #2e1a63;
#         white-space: pre-wrap;
#         box-shadow: 0 2px 15px rgba(60,70,255,0.2);
#     }
#     .diff-box ins {
#         background: #28a745;
#         text-decoration: none;
#         color: #fff;
#         padding: 0 4px;
#         border-radius: 3px;
#     }
#     .diff-box del {
#         background: #dc3545;
#         text-decoration: none;
#         color: #fff;
#         padding: 0 4px;
#         border-radius: 3px;
#     }

#     /* Sidebar content background with slight transparency */
#     .sidebar .sidebar-content {
#         background: rgba(255, 255, 255, 0.15);
#         padding: 1em;
#         border-radius: 12px;
#         box-shadow: 0 6px 20px rgba(238, 9, 121, 0.15);
#     }

#     /* Remove top padding for the main title container */
#     .main-title {
#         margin-top: 0 !important;
#         padding-top: 0 !important;
#     }

#     /* Smooth horizontal sliding effect containers */
#     /* This only styles containers for transition; actual slide animation needs page logic */

#     .page-container {
#         overflow: hidden;
#         position: relative;
#     }

#     .page {
#         position: absolute;
#         width: 100%;
#         top: 0;
#         left: 0;
#         transition: transform 0.6s ease-in-out;
#         will-change: transform;
#     }

#     .page-enter {
#         transform: translateX(100%);
#     }
#     .page-enter-active {
#         transform: translateX(0%);
#     }
#     .page-exit {
#         transform: translateX(0%);
#     }
#     .page-exit-active {
#         transform: translateX(-100%);
#     }

#     </style>
#     """, unsafe_allow_html=True)



import streamlit as st

def apply_custom_css():
    st.markdown("""
    <style>
    /* Light blue shaded background for the full app */
    .stApp {
        background: linear-gradient(135deg, #e6f0ff 0%, #b5e6fa 100%);
        min-height: 100vh;
        min-width: 100vw;
        padding: 0 !important;
        margin: 0 !important;
        overflow-x: hidden;
    }

    /* Base font styling and scaling */
    body, .main, .stApp, .description-box, .section-title, 
    .stButton>button, .stDownloadButton>button {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        font-size: 1.22rem;
        color: #222222;
    }

    /* Main title with pink/orange gradient and subtle shadow */
    .main-title h1 {
        font-size: 4rem;
        text-align: center;
        background: linear-gradient(90deg, #ff6a00 15%, #ee0979 85%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.1em;
        letter-spacing: 2px;
        text-shadow: 2px 2px 8px rgba(238, 9, 121, 0.4);
    }
    .main-title p {
        font-size: 1.2rem;
        text-align: center;
        color: #ee0979;
        margin-bottom: 2em;
        font-weight: 600;
    }

    /* Section titles warm pink/orange */
    .section-title {
        font-size: 1.5rem;
        margin-top: 1em;
        margin-bottom: 0.5em;
        color: #ff6a00;
        text-shadow: 1px 1px 4px rgba(255, 106, 0, 0.35);
        font-weight: 600;
    }

    /* Text area (input) pastel pink/orange */
    .stTextArea textarea {
        background: linear-gradient(135deg, #ffe29f 10%, #ffa99f 80%);
        border: none;
        border-radius: 18px;
        font-size: 1.1rem !important;
        color: #392785;
        padding: 1.2em;
        box-shadow: 0 2px 12px rgba(60, 21, 75, 0.12);
        font-weight: 550;
        resize: vertical;
    }

    /* Buttons: pink to blue gradient with smooth hover */
    .stButton>button, .stDownloadButton>button {
        background: linear-gradient(90deg, #ff6a00, #ee0979);
        color: white;
        border: none;
        border-radius: 25px;
        font-size: 1.1rem;
        font-weight: bold;
        padding: 0.7em 1.4em;
        box-shadow: 0 5px 20px rgba(238, 9, 121, 0.18);
        transition: transform 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
        margin-top: 0.6em;
        width: 100%;
        cursor: pointer;
    }
    .stButton>button:hover, .stDownloadButton>button:hover {
        transform: translateY(-2px) scale(1.02);
        box-shadow: 0 8px 28px rgba(252,106,0,0.28);
        background: linear-gradient(90deg, #3f5efb, #fc466b);
    }

    /* Output and description boxes pastel pink to blue gradient */
    .description-box {
        background: linear-gradient(120deg, #c3bef0 30%, #8ec5fc 100%);
        color: #2e1a63;
        border-radius: 14px;
        padding: 1.1em;
        margin-top: 1em;
        font-size: 1.1rem;
        box-shadow: 0 2px 12px rgba(64, 56, 192, 0.15);
        white-space: pre-wrap;
    }

    /* Diff Box styling */
    .diff-box {
        background: rgba(140, 197, 252, 0.15);
        border-radius: 10px;
        padding: 1em;
        max-height: 250px;
        overflow-y: auto;
        border: 1px solid rgba(130, 130, 255, 0.3);
        font-size: 1.05rem;
        color: #2e1a63;
        white-space: pre-wrap;
        box-shadow: 0 2px 15px rgba(60,70,255,0.2);
    }
    .diff-box ins {
        background: #28a745;
        text-decoration: none;
        color: #fff;
        padding: 0 4px;
        border-radius: 3px;
    }
    .diff-box del {
        background: #dc3545;
        text-decoration: none;
        color: #fff;
        padding: 0 4px;
        border-radius: 3px;
    }

    /* Sidebar content background with slight transparency */
    .sidebar .sidebar-content {
        background: rgba(255, 255, 255, 0.15);
        padding: 1em;
        border-radius: 12px;
        box-shadow: 0 6px 20px rgba(238, 9, 121, 0.15);
    }

    /* Remove top gap for main title container */
    .main-title {
        margin-top: 0 !important;
        padding-top: 0 !important;
    }

    </style>
    """, unsafe_allow_html=True)
