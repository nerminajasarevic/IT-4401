CIPHER = {
    'a': '0', 'b': '1', 'c': '2', 'd': '3', 'e': '4', 'f': '5', 'g': '6', 'h': '7', 'i': '8', 'j': '9',
    'k': '!', 'l': '@', 'm': '#', 'n': '$', 'o': '%', 'p': '^', 'q': '&', 'r': '*', 's': '(', 't': ')',
    'u': '-', 'v': '+', 'w': '<', 'x': '>', 'y': '?', 'z': '=', ' ': ' '
}

def encode_decode(message, operation):
    result = ''
    
    for char in message:

        #encode
        if operation == 'encode' and char in CIPHER:
            result += CIPHER[char]

        #decode
        elif operation == 'decode':
            for key, value in CIPHER.items():
                if char == value:
                    result += key
                    break
                
        #uppercase
        else:
            result += char
            
    return result

def main():
    
    print("Welcome to the Secret Message Encoder/Decoder\n")
    
    while True:
        try:
            
            option = int(input("1. Encode a message \n2. Decode a message \n3. Exit\n \nWhat would you like to do? "))

            #send message to encode
            if option == 1:
                
                message = input("Enter a message to encode: ")
                encoded = encode_decode(message, 'encode')
                
                print("Encoded message:", encoded)

            #send message to decode
            elif option == 2:
                
                message = input("Enter a message to decode: ")
                decoded = encode_decode(message, 'decode')
                
                print('Decoded message:', decoded)

            #exit 
            elif option == 3:
                break

            #invalid input
            else:
                print(f"Error: {option} is not a valid choice.(1 for Encode, 2 for Decode, or 3 to Exit).")

        
        except Exception as err:
            print("Error:", err)


main()
