import google.generativeai as genai

key = "Enter your key"


genai.configure(api_key = key)
model = genai.GenerativeModel("gemini-2.5-flash")

while True:
    user = input("You:")
    if user.lower() == "exit":
        print("Bye Bye")
        break
    response = model.generate_content(user)
    print("Bot: ",response.text)