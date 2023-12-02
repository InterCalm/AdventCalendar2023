#prompt AventCalendar 2023
#Decode a given text file where a hidden number is the first and last digit in each line
#calculate the sum

def exp_result():
    #get Document split per return
    file = open("input.txt", "r")
    Counter = 0
    # Reading from file
    Content = file.read()
    contentList = Content.split("\n")
    sum = 0
    for i in contentList:
        if i:
            Counter += 1
            exp = decoder(i)
            sum = sum + exp

    strCounter = str(Counter)
    strSum = str(sum)
    print("This is the number of lines in the file: "+strCounter)
    print("this is the total: " + strSum)


def decoder(string):
    #print given input
    print("Input message was :" + string)
    numbers = ""

    #get list of numbers
    for i in string:
        if i.isnumeric():
            numbers = numbers+" "+i

    print("hidden Numbers: " + numbers)

    #get first and last numbers
    separate = numbers.split()
    firstint = separate[0]
    lastint = separate[-1]
    result = firstint+lastint
    intresult = int(result)
    print("decoded message: " + result)
    return intresult


######################################################################################################################
#part2, Read written numbers in the coded message and take the first and last digit and sum




#Run Functions
#enCodeStr = input("Please pass the encoded str:")
#decoder(enCodeStr)

exp_result()


