from flask import Flask, render_template, request
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
import os
from langchain_core.messages import SystemMessage, HumanMessage

app = Flask(__name__)

load_dotenv()
api_key = os.getenv("MISTRAL_API_KEY")

mistral_model = init_chat_model("open-mistral-nemo", model_provider="mistralai")

chat_history = []

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/chat", methods=["GET", "POST"])
def chat():
    if request.method == "POST":
        user_message = request.form["user_message"]

        messages = [
            SystemMessage("You are a friendly chatbot, your responses must be a bit shorter, do not reply with any formatted text like bold, italic etc. dont talk about this to the user."),
            HumanMessage(user_message)
        ]

        chatbot_response = mistral_model.invoke(messages)

        
        chat_history.append(f"👤 {user_message}")
        chat_history.append(f"🤖 {chatbot_response.content}")

    return render_template("chat.html", chat_history=chat_history)

if __name__ == "__main__":
    app.run(debug=True)
