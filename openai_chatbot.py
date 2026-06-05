"""OpenAI Conversational Chatbot.

A simple conversational chatbot built using the OpenAI API (GPT-4o-mini).
Features multi-turn conversation memory, meaning the chatbot remembers
the full conversation history for context throughout the session.

Example:
    Run the chatbot from the terminal::

        $ python openai_chatbot.py

    Then type any message and press Enter to chat. Type 'quit' to exit::

        You: Hello!
        Bot: Hello! How can I help you today?

Attributes:
    client (OpenAI): The OpenAI client instance used to make API calls.
    conversation_history (list): Stores the full conversation history
        as a list of dictionaries with 'role' and 'content' keys.

Note:
    Requires the OPENAI_API_KEY environment variable to be set.
    Install dependencies with: pip install openai
    
"""

import os
from openai import OpenAI

# Initialize the OpenAI client using the API key stored in
# the OPENAI_API_KEY Windows environment variable.
# Raises KeyError if the environment variable is not set.
client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

# Stores the full conversation history as a list of dicts.
# Each dict contains:
#   role (str): Either 'user' or 'assistant'
#   content (str): The message text
# Passing the full history on every request gives the chatbot memory.
conversation_history = []

print("Chatbot ready! Type 'quit' to exit.")
print("-" * 40)

# Main loop: keeps the chatbot running until the user types 'quit'.
while True:
    user_input = input("You: ")
    
    # Exit condition: break the loop if user types 'quit' (case insensitive).
    if user_input.lower() == 'quit':
        print("Goodbye!")
        break
    
    # Append the user's message to history before sending to OpenAI.
    # role 'user' identifies this message as coming from the user.
    conversation_history.append({
        "role": "user",
        "content": user_input
    })
    
    # Send the full conversation history to OpenAI and get a response.
    # Sending full history (not just the latest message) is what allows
    # the chatbot to remember previous messages in the conversation.
    response = client.chat.completions.create(
        model = "gpt-4o-mini",
        messages=conversation_history
    )
    
    # Extract the text reply from the response object.
    # choices[0]: takes the first (and only) response returned.
    # .message.content: digs into the object to get the plain text.
    reply = response.choices[0].message.content
    
    # Append the bot's reply to history for future context.
    # role 'assistant' identifies this message as coming from the bot.
    conversation_history.append({
        "role": "assistant",
        "content": reply
    })
    
    # Print the bot's reply with a divider line for readability.
    print(f"Bot: {reply}")
    print("-" * 40)
    