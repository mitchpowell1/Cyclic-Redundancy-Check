__author__ = 'Mitchell Powell'
__course__ = 'CSC 344'

def Subtract(gen,remain): #Subtract method performs bitwise XOR between generator and remainder
    rem= []
    for x in range(0,len(gen)):
        rem.append(int(gen[x]^remain[x]))
    return rem

def Carrythrough(gen,mes,encode = True):
    '''This method performs the main operations of the CRC, it is used by both the Encode and Verify functions'''
    print(mes)
    quotient = []
    message = []
    generator = []
    for char in mes:
        message.append(int(char,2))     #Converts message into a list of bits
    for char in gen:
        generator.append(int(char,2))   #Converts generator into a list of bits
    if encode == True:                  #Appends 0's to message if used for encode function
        for x in range(len(gen)-1):
            message.append(0)
    remainder = message[0:len(generator)]
    index = 0
    while index+len(generator) < len(message):   # performs while there are still bits to process in the transmission
        if remainder[0] == 1:                     #if the first index in the remainder = 1, add a 1 to the quotient
            quotient.append(1)                      #and then subtract the generator from the remainder
            remainder = Subtract(generator,remainder)
        else:
            quotient.append(0)
        remainder.pop(0)                                    #remove the first 0 in the remainder
        remainder.append(message[index+len(generator)])     # (should always be first character)
        index+=1
    if remainder[0] ==1:
        remainder = Subtract(generator,remainder)
    remainder.pop(0)
    for item in remainder:
        mes+=str(item)
    return(mes)

def Encode():
    '''Encode method takes a message as a string of 1's and 0's and
    a generator polynomial and creates a transmission in the form of the original method
    with a checksum'''

    mes = str(input("Enter message for transmission (in string of 1's and 0's): "))
    gen = str(input("Enter Generator Polynomial Coefficients as (in string of 1's and 0's): "))

    print('Transmission: '+Carrythrough(gen,mes))
    print('Generator: ' +gen)

def Verify():
    '''Verify method takes a transmission as a string of 1's and 0's and a generator polynomial
    and checks it against a generator (input as a string of 1's and 0's) for errors '''
    mes = str(input("Enter transmission for error detection (in string of 1's and 0's: "))
    gen = str(input("Enter Generator Polynomial (string of 1's and 0's): "))

    detection = Carrythrough(gen,mes,False) #calls the Carrythrough function with a False for the encode flag
    if int(detection[len(mes):]) != 0:      #so that 0's aren't added to the end of the transmission
        print("There is an error")
    else:
        print("No errors detected")

def main():
    '''Main function gives users the option to either choose the encode or verify function and brings the prompt
    back up if the input doesn't match one of the options'''
    choice = str(input("Encode or Verify? (Enter E for encode, V for verify): "))
    if choice.lower() == 'e':
        Encode()
    elif choice.lower() == 'v':
        Verify()
    else:
        main()
main()
