def Select(optionList,boolean):

    #print options to the user
    print("Selection Panel")
    for i in range(len(optionList)):
        print(i+1,optionList[i])

    #continue getting input until valid response, ignore value errors
    while True:
        try:
            response = int(input("Choose a number from above: "))
            if response > 0 and response <= len(optionList):
                if boolean == True:
                    return optionList[response-1]
                return response-1
        except ValueError:
            pass
