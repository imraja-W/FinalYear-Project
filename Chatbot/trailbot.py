import nltk
from nltk.chat.util import Chat, reflections
import spacy
from textblob import TextBlob

# Load Spacy model
nlp = spacy.load("en_core_web_sm")

# Load information from file into memory
def load_information_from_file(file_path):
    information = {}
    with open(file_path, 'r') as file:
        for line in file:
            question, answer = line.strip().split('|')
            information[question.strip()] = answer.strip()
    return information

# Main function to interact with the chatbot
def chat_with_bot(information):
    print("Welcome to the Local Information Chatbot. How can I assist you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("Goodbye!")
            break
        
        # Greet the user
        if user_input.lower() in ['hello', 'hi', 'hey']:
            print("Bot: Hello! How can I assist you today?")
            continue
        
        # Check for spelling mistakes and suggest corrections
        suggestions = find_suggestions(user_input, information)
        if suggestions:
            print("Bot: Did you mean one of these questions?")
            for suggestion in suggestions:
                print("    " + suggestion)
            print("Bot: Would you like to see the answers to any of these questions? (yes/no):")
            answers_response = input().strip().lower()
            if answers_response == 'yes':
                display_answers(suggestions, information)
            continue
        
        # Analyze user input using Spacy for contextual understanding
        user_input_doc = nlp(user_input)
        for question in information:
            question_doc = nlp(question)
            similarity = user_input_doc.similarity(question_doc)
            if similarity >= 0.7:  # Adjust similarity threshold as needed
                print("Bot:", information[question])
                break
        else:
            print("Bot: I'm sorry, I don't understand that question.")

# Function to find spelling suggestions using TextBlob
def find_suggestions(user_input, information):
    suggestions = []
    blob = TextBlob(user_input)
    corrected_user_input = str(blob.correct())
    for question in information:
        if corrected_user_input.lower() in question.lower():
            suggestions.append(question)
    return suggestions

# Function to display answers for selected questions
def display_answers(questions, information):
    for question in questions:
        if question in information:
            print("Answer:", information[question])

# Main function to start the chat
if __name__ == "__main__":
    nltk.download('punkt')  # Download NLTK tokenizer data
    nltk.download('averaged_perceptron_tagger')  # Download NLTK POS tagger data
    # Load information from local files
    local_information_file_path = 'local_information.txt'  # Adjust the file path as needed
    greet_file_path = 'greet.txt'  # Adjust the file path as needed
    local_information = load_information_from_file(local_information_file_path)
    greet_information = load_information_from_file(greet_file_path)
    # Merge information from both files
    merged_information = {**local_information, **greet_information}
    # Start the chat with merged information
    chat_with_bot(merged_information)
