# FinalYear-Project
Local Information Chatbot

Overview

This is a simple Local Information Chatbot built using Python and NLTK. The chatbot retrieves answers from a predefined dataset stored in text files and provides users with responses based on their queries. It also suggests possible matches in case of spelling errors.

Features

Loads predefined questions and answers from text files.

Provides case-insensitive matching for user queries.

Offers spelling mistake suggestions if an exact match isn't found.

Supports multiple data sources by merging different information files.

Runs in a simple command-line interface.

Requirements

Before running the chatbot, ensure you have the following installed:

Python 3.x

NLTK Library

You can install the dependencies using:

pip install nltk

How to Use

Clone this repository or download the script.

Prepare your text files (local_information.txt and greet.txt) with the following format:

question | answer

Run the chatbot script:

python chatbot.py

Interact with the chatbot by typing a question.

Type quit to exit.

File Structure

📂 Local-Information-Chatbot
├── chatbot.py  # Main chatbot script
├── local_information.txt  # File containing questions and answers
├── greet.txt  # File containing greetings
└── README.md  # Documentation

Example Interaction

Welcome to the Local Information Chatbot. Type 'quit' to exit.
You: What are the store hours?
Bot: The store is open from 9 AM to 9 PM.
You: What is your name?
Bot: I'm a local information chatbot!
You: Quit
Goodbye!

Future Improvements

Implement a GUI interface.

Improve spelling correction using NLP techniques.

Integrate with a database for dynamic content.

Contributing

Feel free to fork the project and submit pull requests for improvements! 🚀

License

This project is open-source under the MIT License.

