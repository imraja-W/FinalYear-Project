import nltk
from nltk.chat.util import Chat, reflections

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
    print("Welcome to the Local Information Chatbot. Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("Goodbye!")
            break
        # Convert user input to lowercase for case-insensitive matching
        user_input_lower = user_input.lower().strip()
        # Check if the user input matches a stored question (case-insensitive)
        if user_input_lower.strip() in map(str.lower, information):
            print("Bot:", information[user_input_lower.strip()])
        else:
            # If no match found, check for spelling mistakes
            print("Would you like suggestions for spelling mistakes? (yes/no):")
            spell_check_response = input().strip().lower()
            if spell_check_response == 'yes':
                suggestions = find_suggestions(user_input_lower, information)
                if suggestions:
                    print("Oh, did you mean one of these questions?")
                    for suggestion in suggestions:
                        print("    " + suggestion)
                    print("Would you like to see the answers to any of these questions? (yes/no):")
                    answers_response = input().strip().lower()
                    if answers_response == 'yes':
                        display_answers(suggestions, information)
                else:
                    print("No suggestions found. Could you be more specific?")
            else:
                print("Could you be more specific?")

# Function to find spelling suggestions
def find_suggestions(user_input, information):
    suggestions = []
    for question in information:
        if user_input in question.lower():
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
