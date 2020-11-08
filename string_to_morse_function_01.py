
def etmf2(str):
    code = {' ': '_',
            "'": '.----.', '(': '-.--.-', ')': '-.--.-', ',': '--..--', '-': '-....-', '.': '.-.-.-', '/': '-..-.',
            '0': '-----', '1': '.----',
            '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
            '9': '----.', ':': '---...', ';': '-.-.-.',
            '?': '..--..', 'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.',
            'H': '....', 'I': '..', 'J': '.---',
            'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...',
            'T': '-', 'U': '..-',
            'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '_': '..--.-'
            }

    def convert_to_morse_code(sentence):
        sentence = sentence.upper()
        encodedSentence = ""
        for character in sentence:
            encodedSentence += code[character] + " "
        return encodedSentence

    message = str
    code = convert_to_morse_code(message)
    print(code)
    etmf2.code = code
