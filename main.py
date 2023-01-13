
'''
 * CÓDIGO MORSE
 * Dificultad: MEDIA
 *
 * Enunciado: Crea un programa que sea capaz de transformar texto natural a código morse y viceversa.

'''
from string import ascii_letters, punctuation


morse_code_dict = {

    'A': '.-', 'B': '-...',
    'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-',
    'L': '.-..', 'M': '--', 'N': '-.',
    'O': '---', 'P': '.--.', 'Q': '--.-',
    'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--',
    'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.',
    '0': '-----', ', ': '--..--', '.': '.-.-.-',
    '?': '..--..', '/': '-..-.', '-': '-....-',
    '(': '-.--.', ')': '-.--.-'
}


def text_to_morse(text):
    white_space = ' '
    letters = [let for let in ascii_letters]
    letters.append(white_space)

    result = ''

    for let in text:
        if let not in letters:
            return 'Los datos proporcionados no son validos para convertir texto a código morse, vuelve a intentarlo.'

    for let in text.upper():
        if let in letters:
            if let == white_space:
                result += white_space

            else:
                result += morse_code_dict[let] + white_space

    return f"text to morse: {result}"


def morse_to_text(morse):
    morse_code_dict_inverse = {v: k for k, v in morse_code_dict.items()}
    char_morse = [let for let in punctuation]
    char_morse.extend([' '])

    text_words = []

    words = morse.split('  ')
    print(words)

    for let in morse:
        if let not in char_morse:
            return 'El códifo morse ingresado no es valido, vuelve a intentarlo'

    for word in words:
        text_word = ''

        for let in word.split():
            if let in morse_code_dict_inverse:
                text_word += morse_code_dict_inverse[let]

        text_words.append(text_word)

    result = ' '.join(text_words)

    return f"morse to text: {result.lower()}"


if __name__ == '__main__':

    print(text_to_morse('kevin asael'))

    print(morse_to_text(
        '-.- . ...- .. -.  .- ... .- . .-.. '))

