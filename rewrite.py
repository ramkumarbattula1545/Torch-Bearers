# modules/rewrite.py
# modules/rewrite.py
# import requests

# HF_API_KEY = "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"
# MODEL = "meta-llama/Meta-Llama-3-8B-Instruct"

# API_URL = f"https://api-inference.huggingface.co/models/{MODEL}"
# HEADERS = {"Authorization": f"Bearer {HF_API_KEY}"}

# def rewrite_text(text, tone):
#     """Rewrite text using Hugging Face Inference API dynamically"""
#     prompt = f"Rewrite the following text in a {tone} tone, keeping the meaning same:\n{text}"
#     payload = {"inputs": prompt, "parameters": {"max_new_tokens": 300}}

#     response = requests.post(API_URL, headers=HEADERS, json=payload)
#     try:
#         return response.json()[0]['generated_text']
#     except Exception:
#         return text

# modules/rewrite.py
# import requests

# HF_API_KEY = "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"
# MODEL = "meta-llama/Meta-Llama-3-8B-Instruct"

# API_URL = f"https://api-inference.huggingface.co/models/{MODEL}"
# HEADERS = {"Authorization": f"Bearer {HF_API_KEY}"}

# def rewrite_text(text, tone):
#     """
#     Rewrite text using Hugging Face Inference API dynamically.
#     Ensures the rewritten text has noticeable adaptation.
#     """
#     prompt = (
#         f"Rewrite the following text in a **{tone}** tone. "
#         f"Make it sound natural and human, vary sentence structure, and use synonyms. "
#         f"Do not repeat the text verbatim; make it noticeably different but keep meaning intact.\n\n"
#         f"Original text:\n{text}\n\nRewritten version:"
#     )
#     payload = {
#         "inputs": prompt,
#         "parameters": {
#             "max_new_tokens": 400,
#             "temperature": 0.8,
#             "top_p": 0.9,
#             "do_sample": True
#         }
#     }

#     response = requests.post(API_URL, headers=HEADERS, json=payload)
#     try:
#         # Some models return list, some return dict with 'generated_text'
#         result = response.json()
#         if isinstance(result, list) and "generated_text" in result[0]:
#             return result[0]["generated_text"]
#         elif "generated_text" in result:
#             return result["generated_text"]
#         else:
#             return text  # fallback
#     except Exception:
#         return text

# import requests

# HF_API_KEY = "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"
# MODEL = "meta-llama/Meta-Llama-3-8B-Instruct"

# API_URL = f"https://api-inference.huggingface.co/models/{MODEL}"
# HEADERS = {"Authorization": f"Bearer {HF_API_KEY}"}

# def rewrite_text(text, tone):
#     """
#     Rewrite text using Hugging Face API with *strong adaptation*:
#     - Use synonyms, alter sentence order
#     - Add details/emphasis based on tone
#     - Avoid copying original phrasing
#     """
#     prompt = (
#         f"You are an expert creative writer. Rewrite the following text into a {tone} tone:\n\n"
#         f"- Use synonyms and different sentence structures.\n"
#         f"- Enrich with descriptive words fitting the tone.\n"
#         f"- Reorder ideas where possible.\n"
#         f"- Avoid repeating exact phrases from the original text.\n\n"
#         f"Original:\n{text}\n\nRewritten:"
#     )

#     payload = {
#         "inputs": prompt,
#         "parameters": {
#             "max_new_tokens": 400,
#             "temperature": 0.9,   # More creativity
#             "top_p": 0.95,
#             "do_sample": True
#         }
#     }

#     response = requests.post(API_URL, headers=HEADERS, json=payload)
#     try:
#         result = response.json()
#         if isinstance(result, list) and "generated_text" in result[0]:
#             return result[0]["generated_text"]
#         elif "generated_text" in result:
#             return result["generated_text"]
#         else:
#             return text
#     except Exception:
#         return text


# import requests

# HF_API_KEY = "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"
# MODEL = "meta-llama/Meta-Llama-3-8B-Instruct"

# API_URL = f"https://api-inference.huggingface.co/models/{MODEL}"
# HEADERS = {"Authorization": f"Bearer {HF_API_KEY}"}

# def rewrite_text(text, tone):
#     """
#     Rewrite text using Hugging Face Inference API dynamically
#     with strong differentiation while maintaining meaning.
#     """
#     prompt = f"""
#     Rewrite the following text entirely in a **{tone}** tone.
#     - Use more expressive vocabulary, metaphors, and emotional intensity.
#     - Adjust sentence structure and pacing to match the tone.
#     - Keep meaning intact but make it feel stylistically different.
#     - Add human-like storytelling elements if possible.

#     Original text:
#     {text}
#     """

#     payload = {"inputs": prompt, "parameters": {"max_new_tokens": 400}}

#     response = requests.post(API_URL, headers=HEADERS, json=payload)
#     try:
#         # Extract generated text carefully
#         generated = response.json()[0].get("generated_text", "")
#         # Remove prompt echo if model repeats it
#         if "Original text:" in generated:
#             generated = generated.split("Original text:")[-1].strip()
#         return generated if generated else text
#     except Exception:
#         return text


# import requests

# HF_API_KEY = "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"
# MODEL = "meta-llama/Meta-Llama-3-8B-Instruct"

# API_URL = f"https://api-inference.huggingface.co/models/{MODEL}"
# HEADERS = {"Authorization": f"Bearer {HF_API_KEY}"}

# def rewrite_text(text):
#     """
#     Rewrite text adaptively into 3 tones: Suspenseful, Neutral, Professional.
#     Returns a dict with all three rewrites.
#     """
#     tones = {
#         "suspenseful": """
# Rewrite the following text in a suspenseful tone.
# - Use vivid descriptions, build tension and anticipation.
# - Use rhetorical questions and pacing to hook the reader.
# - Keep original meaning intact, add storytelling elements.
# """,
#         "neutral": """
# Rewrite the following text in a neutral tone.
# - Use clear, straightforward language.
# - Avoid strong emotions or stylistic flair.
# - Preserve the original meaning exactly.
# """,
#         "professional": """
# Rewrite the following text in a professional tone.
# - Use formal language and precise vocabulary.
# - Maintain clarity and objectivity.
# - Ensure the text sounds credible and authoritative.
# """
#     }

#     rewritten_texts = {}

#     for tone_name, tone_prompt in tones.items():
#         prompt = f"""
# {tone_prompt}

# Original text:
# {text}
# """
#         payload = {
#             "inputs": prompt,
#             "parameters": {"max_new_tokens": 400}
#         }

#         try:
#             response = requests.post(API_URL, headers=HEADERS, json=payload, timeout=30)
#             response.raise_for_status()
#             result = response.json()

#             generated = ""
#             if isinstance(result, list) and len(result) > 0:
#                 generated = result[0].get("generated_text", "")
#             elif isinstance(result, dict):
#                 generated = result.get("generated_text", "")

#             if "Original text:" in generated:
#                 generated = generated.split("Original text:")[-1].strip()

#             rewritten_texts[tone_name] = generated if generated else text

#         except Exception:
#             rewritten_texts[tone_name] = text

#     return rewritten_texts


import requests

HF_API_KEY = "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"
MODEL = "meta-llama/Meta-Llama-3-8B-Instruct"

API_URL = f"https://api-inference.huggingface.co/models/{MODEL}"
HEADERS = {"Authorization": f"Bearer {HF_API_KEY}"}


def rewrite_text(text):
    """
    Generate rewrites in 3 distinct tones: Suspenseful, Neutral, Professional.
    Returns a dict with tone keys mapping to rewritten texts.
    """
    tones = {
        "suspenseful": """
Rewrite the following text in a suspenseful tone.
- Use vivid descriptions, build tension and anticipation.
- Use rhetorical questions and pacing to hook the reader.
- Keep original meaning intact, add storytelling elements.
""",
        "neutral": """
Rewrite the following text in a neutral tone.
- Use clear, straightforward language.
- Avoid strong emotions or stylistic flair.
- Preserve the original meaning exactly.
""",
        "professional": """
Rewrite the following text in a professional tone.
- Use formal language and precise vocabulary.
- Maintain clarity and objectivity.
- Ensure the text sounds credible and authoritative.
"""
    }

    rewritten_texts = {}

    for tone_name, tone_prompt in tones.items():
        prompt = f"""
{tone_prompt}

Original text:
{text}
"""
        payload = {
            "inputs": prompt,
            "parameters": {"max_new_tokens": 400}
        }

        try:
            response = requests.post(API_URL, headers=HEADERS, json=payload, timeout=30)
            response.raise_for_status()
            result = response.json()

            generated = ""
            if isinstance(result, list) and len(result) > 0:
                generated = result[0].get("generated_text", "")
            elif isinstance(result, dict):
                generated = result.get("generated_text", "")

            if "Original text:" in generated:
                generated = generated.split("Original text:")[-1].strip()

            rewritten_texts[tone_name] = generated if generated else text

        except Exception:
            rewritten_texts[tone_name] = text

    return rewritten_texts
