"""
If we consider spaces in the input string "race car," it is not a palindrome 
because it reads differently backward and forward when spaces are included.
"""

def is_palindrome(string):
    # Check if the string is equal to its reverse
    return string == string[::-1]

if __name__ == "__main__":
    while True:
        input_string = input("Enter a string to check if it is a palindrome (type 'q' to quit): ").lower()
        
        if input_string == 'q':
            print("exiting the prgram...")
            break
        #check if the input is a palindrome
        if is_palindrome(input_string):
            print(input_string, "is a palindrome")
        else:
            print(input_string, "is not a palindrome")
    