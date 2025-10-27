import google.generativeai as genai

genai.configure(api_key="AIzaSyA-3AAqyK8WusyByQH0vNcSle3XY-pZip8")

model = genai.GenerativeModel("gemini-2.5-flash")

response = model.generate_content("Explain in five lines about python")

print(response.text)
