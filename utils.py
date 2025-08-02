# modules/utils.py
def split_chapters(text, length=1000):
    words = text.split()
    return [' '.join(words[i:i+length]) for i in range(0, len(words), length)]

from difflib import ndiff
import re

def generate_diff_html(original, adapted):
    """
    Returns HTML highlighting differences:
    - Green (added in adapted)
    - Red strikethrough (removed from original)
    """
    diff = list(ndiff(original.split(), adapted.split()))
    html = []

    for word in diff:
        if word.startswith("- "):  # Removed
            html.append(f"<span style='color:red;text-decoration:line-through;'>{word[2:]}</span> ")
        elif word.startswith("+ "):  # Added
            html.append(f"<span style='color:green;font-weight:bold;'>{word[2:]}</span> ")
        elif word.startswith("? "):  # Ignore helper lines
            continue
        else:
            html.append(f"{word[2:]} ")

    # Clean multiple spaces
    return re.sub(r'\s+', ' ', ''.join(html))
