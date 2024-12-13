# Lab 12

# ******************** Morse Code Dictionary ********************
morseCode = {
    'A': '.-',    'B': '-...',  'C': '-.-.',  'D': '-..',   'E': '.',
    'F': '..-.',  'G': '--.',   'H': '....',  'I': '..',    'J': '.---',
    'K': '-.-',   'L': '.-..',  'M': '--',    'N': '-.',    'O': '---',
    'P': '.--.',  'Q': '--.-',  'R': '.-.',   'S': '...',   'T': '-',
    'U': '..-',   'V': '...-',  'W': '.--',   'X': '-..-',  'Y': '-.--',
    'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    'SPACE' : ' ', 'END-WORD' : '.......'
}

sentenceInMorse = []

# sentence = input("Enter a sentence: ")
sentence = "feSD_DEE ERC-454 45@Valid EnDOf S.e>ntence words AnD N¿umbers"
#sentence = "Th1?5 Ph-rase co@NTains numb3r5 **/_.? and w0rd5 [%, ;:><"

# Converts sentence to upper since Morse Code letters are in upper case.
words = sentence.strip().upper().split()

for word in words:
    word = ''.join(filter(str.isalnum, word)) # Filters only letters and numbers
    if len(word) > 0: # if the word contains only invalid characters, it will be ignored
        for char in word:
            letter = morseCode[char]
            sentenceInMorse.append(letter)
            sentenceInMorse.append(morseCode['SPACE']) # Space between characters
        sentenceInMorse.append(morseCode['END-WORD']) # Space between words
        sentenceInMorse.append(morseCode['SPACE']) # Space to start a new word

del sentenceInMorse[-3:] # Removes the last three spaces carried by the loop
finalMorseSentece = ''.join(map(str, sentenceInMorse)) # Converted to string
print(f'Your sentence in Morse: {finalMorseSentece}')

