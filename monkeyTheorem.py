from random import choice

def generate(inputLen):
 
    characters = list(chr(i) for i in range(ord('a'),ord('z')+1))
    characters.append(' ')

    randPhrase = []
    for i in range(inputLen):
    	randPhrase.append(choice(characters))

    return randPhrase

def score(originalPhrase,generatedPhrase):
    count = 0
    for i in range(len(originalPhrase)):
        if originalPhrase[i] == generatedPhrase[i]:
            del originalPhrase[i]
            del generatedPhrase[i]
            count += 1
        if i == len(originalPhrase) - count:
            break
        continue
    return originalPhrase

def main():

    inputPhrase = list(input("Enter a phrase: "))
    newPhrase = generate(len(inputPhrase))
    while 1:
        
        newPhrase = generate(len(inputPhrase))
        if inputPhrase != newPhrase:
            inputPhrase = score(inputPhrase, newPhrase)
        else: 
            break  
main()
