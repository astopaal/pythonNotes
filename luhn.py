import random as rd

def generateCheckDigit(numbers):
    
    
    if len(numbers)%2 == 1:
        for i in range(0,len(numbers),2):
            numbers[i] *= 2
    else:
        for i in range(1,len(numbers),2):
            numbers[i] *= 2

    check_digit = (sum(numbers)*9) % 10

    return check_digit


def generateMasterCard():
    
    #first number must be 5
    #second number must be between 1 and 5
    #card number must consist of 16 digits
    card_number = [rd.randint(0,9) for i in range(13)]

    card_number.insert(0, rd.randint(1,5))
    card_number.insert(0,5)
    card_number.append(generateCheckDigit(card_number.copy()))

    return card_number

def generateVisa():
    
    #first number must be 4
    #card number must consist of 16 digits
    card_number = [rd.randint(0,9) for i in range(14)]
    card_number.insert(0,4)
    card_number.append(generateCheckDigit(card_number.copy()))

    return card_number

print(generateVisa())
print(generateMasterCard())