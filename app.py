import os
from flask import Flask, render_template, request, jsonify
from groq import Groq

app = Flask(__name__)

# 1. SECURE YOUR API KEY: 
# Get it from environment variables. Fallback to the string ONLY for local testing (not recommended!).
API_KEY = os.environ.get("GROQ_API_KEY", "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")
client = Groq(api_key=API_KEY)

# 2. CHOOSE YOUR MODEL (Double-check string spelling)
MODEL = "llama-3.3-70b-versatile"

@app.route('/')
def home():
    """Renders the main chatbot interface page."""
    # Note: Make sure 'index.html' is inside a folder named 'templates' in your project root!
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    """Handles sending the payload to Groq and returning the text."""
    try:
        # Check if the request is actually JSON
        if not request.is_json:
            return jsonify({'error': 'Request must be JSON'}), 400

        data = request.json
        messages = data.get('messages', [])
        
        if not messages:
            return jsonify({'error': 'No messages provided'}), 400

        # Inject system prompt at the beginning if not present
        if messages[0].get('role') != 'system':
            messages.insert(0, {
                "role": "system",
                "content": "You are a highly capable AI assistant. Give concise, well-structured answers."
            })

        # Fetch the completion from Groq
        completion = client.chat.completions.create(
            messages=messages,
            model=MODEL,
            stream=False 
        )
        
        reply = completion.choices[0].message.content
        return jsonify({'reply': reply})

    except Exception as e:
        # This will print the EXACT error traceback in your console/terminal
        import traceback
        traceback.print_exc() 
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)