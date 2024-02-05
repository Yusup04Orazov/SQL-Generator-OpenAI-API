import openai

# Set your OpenAI API key
api_key = ''

# Configure the OpenAI API client
openai.api_key = api_key

# def generate_sql():
try:
    while True:
        # Take user input
        user_input = input("User:             ")

        # Check if the user wants to quit
        keywords = ['exit', 'quit', 'stop']
        if any(keyword in user_input.lower() for keyword in keywords):
            print("Goodbye!")
            break

        # Check if any of the keywords exist anywhere in the user input
        keywords = ['sql', 'database', 'format', 'table']
        if any(keyword in user_input.lower() for keyword in keywords):
            # Send user input to OpenAI API
            chat_completion = openai.ChatCompletion.create(
                messages=[{"role": "user", "content": user_input}],
                model="gpt-3.5-turbo"
            )

            # Print the response from OpenAI API
            print("AI:", chat_completion.choices[0].message['content'])
        else:
            print("Please ask a question related to building and formatting SQL databases.")

except Exception as error:
    print("Error:", error)
