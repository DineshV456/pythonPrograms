import google.generativeai as genai

genai.configure(api_key="")

model = genai.GenerativeModel("gemini-2.5-flash")

response = model.generate_content("Explain in five lines about python")

print(response.text)
