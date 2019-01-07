#Author: Soumen Nath


'''
This is the load function responsible for loading the data (text) from a specified file.
@params         fName, the variable that contains the filename specifed by the user.
@return         The return value is the entire body of text contained in the file.
'''
def load(fName):
    try:
        fo = open(fName, 'r')
        #open the specified file in read mode
        fo = open(fName, 'r')
        #read the contents of the file and store it in fText
        fText = fo.read()
        #close the file and return the variable that contains the file data
        fo.close()
    except FileNotFoundError:
        print('Error! an invalid filename was entered!')
        fText = ''
    return fText
'''
This is the save function responsible for saving the data (text) to a specified file.
@params         fName, the variable that contains the filename specifed by the user.
                fText, the variable that  contains the data (current text) that is to be saved in a file.
@return         none
'''
def save(fName, fText):
    #open the specified file in write mode
    fo = open(fName, 'w')
    #use the print function to write the data into the specifed file
    print(fText, file=fo)
    #close the file
    fo.close()
'''
This is the cryptogram_alphabet function responsible for getting a valid user defined alphabet.
@params         none
@return         a valid user defined alphabet or the default alphabet if a valid alphabet was not entered by the user.
'''
def cryptogram_alphabet():
    #get the user defined alphabet
    uAlpha = input("Please enter the alphabet you wish to use for enchiphering/deciphering: ").upper()
    #store the default alphabet in a variable
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    #check to see if the user entered 26 characters
    if len(uAlpha) != len(alpha):
        print("Error! an invalid alphabet was entered!")
        return alpha
    else:
        #compare each value in the user defined alphabet with the other values that come after the current value to check for duplicates
        dup = False
        for i in range(len(uAlpha)):
            for j in range((i+1), len(uAlpha)):
                if uAlpha[j] == uAlpha[i]:
                    dup = True
        #check to see if all 26 letters in the standard alphabet are in the user defined alphabet (to check if there are any special characters)
        counter = 0
        for letter in alpha:
            if letter in uAlpha:
                counter+=1
        #if the user defined alphabet passes all the checks then it is returned, otherwise the default alphabet is returned
        if dup == False and counter == len(alpha):
            return uAlpha
        else:
            print("Error! an invalid alphabet was entered!")
            return alpha
'''
This is the encipher function responsible for enciphering (encrypting) text.
@params         cText, this variable cintains the current text that the user wishes to encrypt
                cAlphabet, this variable contains the current alphabet
@return         The return value is the enciphered text
'''
def encipher(cText, cAlphabet):
    #store the default alphabet in a variable
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    #the encrypted text, initially empty
    eText = ''
    #traverse through all the characters in the current text
    for letter in cText.upper():
        counter = 0
        for i in range(26):
            #if the character is a letter in the default alphabet then add the corresponding letter from the current alphabet to the encrypted text
            if letter == alpha[i]:
                eText += cAlphabet[i]
            else:
                counter+=1
        #if the character is not a letter then just add it to the encrypted text without changing it
        if counter==26:
            eText+=letter
    return eText
'''
This is the decipher function responsible for denciphering (decrypting) text.
@params         cText, this variable cintains the current text that the user wishes to encrypt
                cAlphabet, this variable contains the current alphabet
@return         The return value is the enciphered text
'''
def decipher(cText, cAlphabet):
    #store the default alphabet in a variable
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    #the decrypted text, initially empty
    dText = ''
    #traverse through all the characters in the current text
    for letter in cText.upper():
        counter = 0
        for i in range(26):
            #if the character is a letter in the current default alphabet then add the corresponding letter from the default alphabet to the decrypted text
            if letter == cAlphabet[i]:
                dText += alpha[i]
            else:
                counter+=1
        #if the character is not a letter then just add it to the decrypted text without changing it
        if counter==26:
            dText+=letter
    return dText
'''
This is the main function responsible for user interface.
@params         none
@return         none
'''
def main():
    print("\t\t\t----------------------------------------\n\t\t\tWelcome to Soumen's Cryptography Machine\n\t\t\t----------------------------------------\n\n")
    #the default values of the initial text, current text and current alphabet respectively
    iText = ''
    cText = ''
    cAlphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    #loop for the menu
    while True:
        print("\n\n\nInitial Text:", iText+'\n'+'Curent Text:', cText+"\nThe current alphabet is:", cAlphabet)
        print("Please Choose an option:\n1-Load a File\n2-Save a File\n3-Define an alphabet\n4-Encipher Text\n5-Decipher Text\n6-Quit")
        #loop to make sure that the user eneters a valid selection
        while True:
            try:
                selection = int(input('Please enter your selection: '))
            except ValueError:
                print('Error! A valid selection was not entered'); continue
            if selection<1 or selection>6:
                print('Error! A valid selection was not entered'); continue
            else:
                break
        if selection == 1:
            #ask the user for the name of the file that they wish to load and run the load
            fName = input("Please enter the name of the file you wish to load: ")
            fText = load(fName)
            #set the values of the following variables to the text that was in the specified file
            iText = fText
            cText = fText
        elif selection == 2:
            #check to see if the current text is empty, if so then deny the user from saving to a file
            if cText == '':
                print("Error, there is no text available that can be saved to a file!")
            else:
                #if there is text to be saved then ask the user for the name of the file they would lkie to save the text in
                fName = input('Please enter the name of the file where you wish to save the current text: ')
                save(fName, cText)
        elif selection == 3:
            #run the cryptogram_alphabet function to deermine the currrent alphabet
            cAlphabet = cryptogram_alphabet()
        elif selection == 4:
            #check to see if the current text is empty, if so then deny the user from encrypting text. Otherwise run the encipher function and display the encrypted text.
            if iText == '':
                print("Error, you must load a file first!")
            else:
                if cText == '':
                    cText = encipher(iText, cAlphabet)
                else:
                    cText = encipher(cText, cAlphabet)
                print('The enciphered text is:', cText)
        elif selection == 5:
            #check to see if the current text is empty, if so then deny the user from decrypting text. Otherwise run the decipher function and display the decrypted text.
            if iText == '':
                print("Error, you must load a file first!")
            else:
                if cText == '':
                    cText = decipher(iText, cAlphabet)
                else:
                    cText = decipher(cText, cAlphabet)
                print('The deciphered text is:', cText)
        else:
            #if the user chooses to quit, break the loop
            print('\n\nThank you for using this program!')
            break
main()
