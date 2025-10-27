import google.generativeai as genai

# Configure Gemini API key
genai.configure(api_key="AIzaSyA-3AAqyK8WusyByQH0vNcSle3XY-pZip8")

# Load the model
model = genai.GenerativeModel("gemini-2.5-flash")

print("Gemini Chatbot (type 'exit' to quit)\n")

# Chat loop
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit", "bye"]:
        print("Bot: Goodbye! 👋")
        break

    response = model.generate_content(user_input)
    print("Bot:", response.text)
