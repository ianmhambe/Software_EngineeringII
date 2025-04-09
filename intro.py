from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Simple chatbot responses
def chatbot_response(user_input):
    responses = {
        "hello": "Hi there! How can I help you today?",
        "how are you": "I'm just a bot, but I'm doing great! How about you?",
        "what is your name": "I'm a chatbot created to assist you.",
        "bye": "Goodbye! Have a great day!"
    }
    
    return responses.get(user_input.lower(), "I'm sorry, I don't understand that.")

@app.route('/')
def home():
    return render_template('chat.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.form['message']
    bot_reply = chatbot_response(user_message)
    return jsonify({"reply": bot_reply})

if __name__ == '__main__':
    app.run(debug=True)