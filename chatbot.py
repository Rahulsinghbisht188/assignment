import nltk
from nltk.tokenize import word_tokenize

intents = {
    "hours": ["hours", "timing", "open", "close", "working"],
    "price": ["price", "cost", "charges", "rate"],
    "services": ["service", "offer", "do you have", "facilities"],
    "contact": ["contact", "phone", "email", "call"],
    "booking": ["book", "order", "schedule", "appointment"],
    "greeting": ["hi", "hello", "hey"],
    "goodbye": ["bye", "thank", "thanks", "see you"]
}

def match_intent(user_input):
    tokens = word_tokenize(user_input.lower())
    for intent, keywords in intents.items():
        if any(word in tokens for word in keywords):
            return intent
    return "unknown"

def rule_based_response(user_input):
    user_input = user_input.lower()
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I assist you today?"
    elif "hours" in user_input or "timing" in user_input:
        return "We are open from 9 AM to 9 PM, Monday to Saturday."
    elif "price" in user_input or "cost" in user_input:
        return "Our laundry service starts at ₹50 per item. Bulk discounts are available!"
    elif "services" in user_input:
        return "We offer washing, dry cleaning, ironing, and express delivery."
    elif "contact" in user_input:
        return "You can reach us at +91-9876543210 or email us at support@laundrywallah.com"
    elif "book" in user_input or "order" in user_input:
        return "You can book a service directly on our website or by calling us."
    elif "bye" in user_input or "thank" in user_input:
        return "You're welcome! Have a great day 😊"
    else:
        return None

def chatbot_response(user_input):
    intent = match_intent(user_input)
    responses = {
        "hours": "We are open 9 AM to 9 PM, Monday–Saturday.",
        "price": "Our laundry service starts at ₹50 per item.",
        "services": "We provide washing, dry cleaning, ironing, and express delivery.",
        "contact": "You can reach us at +91-9876543210 or email support@laundrywallah.com",
        "booking": "You can book via our website or call us directly.",
        "greeting": "Hi there! How can I help you?",
        "goodbye": "Goodbye! Have a wonderful day 🌸",
        "unknown": None
    }
    response = responses.get(intent)
    if response is None:
        response = rule_based_response(user_input)
    if response is None:
        response = "I'm sorry, I didn't quite get that. Can you rephrase?"
    return response

print("Laundry Service Chatbot 🤖 (type 'exit' to quit)")
while True:
    user = input("You: ")
    if user.lower() == "exit":
        print("Chatbot: Goodbye! 👋")
        break
    print("Chatbot:", chatbot_response(user))