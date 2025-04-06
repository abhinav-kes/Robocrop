from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai

app = Flask(__name__)  # Create a Flask app
CORS(app)  # Allow frontend requests

# Configure Google Gemini API
genai.configure(api_key="AIzaSyB4bPOV7p7-aeWbCepI5mORwHEo23k6M8I")  # Replace with your actual API key
model = genai.GenerativeModel("gemini-1.5-pro-latest")  # Use an available model

# Route for homepage
@app.route("/", methods=["GET"])
def home():
    return "Welcome to the Farming Chatbot API!"

# Route to handle chatbot responses
@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()  # Get JSON data from frontend
    user_message = data.get("message", "")

    # If no message is provided, return an error
    if not user_message:
        return jsonify({"error": "Message is required"}), 400

    # Generate response using Gemini API
    response = model.generate_content(user_message)
    
    return jsonify({"response": response.text})  # Send back the chatbot response

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
