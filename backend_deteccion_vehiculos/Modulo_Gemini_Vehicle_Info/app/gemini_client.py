import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def gemini_call(prompt, image_bytes):
    model = genai.GenerativeModel("gemini-2.0-flash")
    
    response = model.generate_content([
        prompt,
        {"mime_type": "image/jpeg", "data": image_bytes}
    ])

    return response.text
