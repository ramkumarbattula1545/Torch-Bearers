# modules/sentiment.py
import requests
import json

HF_API_KEY = "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"  # Replace with your HF token
MODEL = "meta-llama/Meta-Llama-3-8B-Instruct"  # LLM model for sentiment

API_URL = f"https://api-inference.huggingface.co/models/{MODEL}"
HEADERS = {"Authorization": f"Bearer {HF_API_KEY}"}

def analyze_sentiment_and_tone(text):
    """Use HF Inference API to analyze sentiment and suggest tone dynamically"""
    prompt = f"""
    Analyze the sentiment and suggest the best tone for the following text.
    Return your answer strictly as JSON:
    {{
        "sentiment": "<positive|negative|neutral>",
        "suggested_tone": "<tone>"
    }}
    Text: {text}
    """

    payload = {"inputs": prompt, "parameters": {"max_new_tokens": 100}}

    response = requests.post(API_URL, headers=HEADERS, json=payload)
    
    try:
        result_text = response.json()[0]['generated_text']
        return result_text  # This will be parsed in app.py
    except Exception as e:
        return json.dumps({"sentiment": "neutral", "suggested_tone": "neutral"})
