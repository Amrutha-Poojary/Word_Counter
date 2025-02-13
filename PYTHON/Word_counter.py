# Function to get user input
def get_user_input():
    return input("Welcome to the WORD_COUNTER!!\nPlease enter a sentence or paragraph:\n ")

# Function to count words in the input text
def count_words(text):
    words = text.split()  # Split the text into words
    return len(words)     # Return the number of words

# Function to display the word count
def display_word_count(word_count):
    print(f"Word count: {word_count}")

# Function to validate user input
def validate_input(text):
    return text.strip() != ""  # Check if the input is not empty after removing leading/trailing spaces

# Main function to run the program
def main():
    while True:
        # Get user input
        user_input = get_user_input()
        
        # Validate input
        if validate_input(user_input):
            # Count words
            word_count = count_words(user_input)
            
            # Display the word count
            display_word_count(word_count)
            break  # Exit the loop after successful processing
        else:
            print("Error: Input cannot be empty. Please try again.")

# Run the program
if __name__ == "__main__":
    main()