#prompt AdventCalendar 2023
#Decode a given text file where a hidden number is the first and last digit in each line
#calculate the sum

def exp_result():
    #get Document split per return
    file = open("AdventCalendar2023/input.txt", "r")
    Counter = 0
    # Reading from file
    Content = file.read()
    contentList = Content.split("\n")
    sum = 0
    altsum = 0
    for i in contentList:
        if i:
            Counter += 1
            exp = decoder(i)
            sum = sum + exp

            value = read_decoder(i)
            newexp = decoder(value)
            altsum = altsum + newexp


    #print result1
    strCounter = str(Counter)
    strSum = str(sum)
    print("This is the number of lines in the file: "+strCounter)
    print("this is the first total: " + strSum)

    # print result2
    strAltSum = str(altsum)
    print("this is the second total: " + strAltSum)


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


#part2, Read written numbers in the coded message and take the first and last digit and sum
def read_decoder(string):
    converter = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    #Take string read string for numbers and convert the text into a number and run in decode function
    print("Read string Input message was :" + string)
    for i in string:
        string = string.replace("one", "1")
        string = string.replace("two", "2")
        string = string.replace("three", "3")
        string = string.replace("four", "4")
        string = string.replace("five", "5")
        string = string.replace("six", "6")
        string = string.replace("seven", "7")
        string = string.replace("eight", "8")
        string = string.replace("nine", "9")
    print(string)

    return string



#Run Functions
#enCodeStr = input("Please pass the encoded str:")
#decoder(enCodeStr)
#read_decoder(enCodeStr)
#decoder(read_decoder(enCodeStr))

exp_result()

