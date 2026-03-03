import requests
import json

def ask_local_llm(question, context):
    url = "http://localhost:11434/api/generate"
    prompt = f"""
    You are a helpful assistant.

    Use ONLY the following context to answer the question.

    Context:
    {context}

    Question:
    {question}

    Answer in 3–4 lines.
    """

    data = {
        "model": "phi3:mini",
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(url, json=data)
    data = response.json()
    print("LLM RESPONSE JSON:", data)  # debugging
    
    # Try different possible keys
    
    if "response" in data:
        return data["response"]
    elif "answer" in data:
        return data["answer"]
    elif "message" in data:
        return data["message"]

# If no known key found, return whole JSON
    return str(data)

