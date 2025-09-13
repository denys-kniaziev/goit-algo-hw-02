from collections import deque
import re

def is_palindrome(text):
    """
    Check if a string is a palindrome using deque
    
    Args:
        text (str): Input string to check
        
    Returns:
        bool: True if palindrome, False otherwise
    """
    # Normalize text: remove spaces, punctuation, convert to lowercase
    normalized = re.sub(r'[^a-zA-Z0-9]', '', text.lower())
    
    # Add all characters to deque
    char_deque = deque(normalized)
    
    # Compare characters from both ends
    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False
    
    return True

def test_palindromes():
    """Test the palindrome function with various examples"""
    test_cases = [
        "racecar",
        "A man a plan a canal Panama",
        "race a car",
        "hello",
        "Madam",
        "No 'x' in Nixon",
        "Mr. Owl ate my metal worm",
        "",
        "a",
        "Able was I, ere I saw Elba"
    ]
    
    print("Palindrome Checker Results:")
    print("-" * 40)
    
    for text in test_cases:
        result = is_palindrome(text)
        status = "✓ Palindrome" if result else "✗ Not a palindrome"
        print(f"'{text}' -> {status}")

def main():
    """Main program for interactive palindrome checking"""
    print("Palindrome Checker")
    print("Enter strings to check if they are palindromes")
    print("Type 'test' to run test cases, 'quit' to exit")
    
    while True:
        user_input = input("\nEnter text: ").strip()
        
        if user_input.lower() == 'quit':
            print("Goodbye!")
            break
        elif user_input.lower() == 'test':
            test_palindromes()
        elif user_input:
            result = is_palindrome(user_input)
            status = "is" if result else "is NOT"
            print(f"'{user_input}' {status} a palindrome")
        else:
            print("Please enter some text")

if __name__ == "__main__":
    main()