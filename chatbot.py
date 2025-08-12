print("Hello! I am a simple chatbot. Type 'exit' to end our conversation.")
while True:
    user_input = input("You: ").lower()
    
    if user_input == 'exit':
        print("Bot: Goodbye! Have a great day.")
        break
    
   
    elif "your" in user_input and "name" in user_input:
        print("Bot: I am a simple Python bot, I don't have a name!")
        
    elif "how" in user_input and "old" in user_input:
        print("Bot: As a program, I am ageless.")
        
    elif "time" in user_input:
        import datetime
        now = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"Bot: The current time is {now}.")
        
    elif "date" in user_input:
        import datetime
        today = datetime.date.today().strftime("%Y-%m-%d")
        print(f"Bot: Today's date is {today}.")
        
    elif "hello" in user_input or "hi" in user_input:
        print("Bot: Hi there! How can I help you today?")
    
    else:
        print("Bot: I'm sorry, I don't understand that.")