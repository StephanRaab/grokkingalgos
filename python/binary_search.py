import datetime

def intro():
    print("Welcome. Please pick a number between 1 and ....")
    highCount = int(input())
    print(f'Wow, {highCount}. Which number should we find between 1 and {highCount}?')
    guessNumber = int(input())

    if guessNumber <= highCount:
        return [guessNumber, highCount]
    else:
        print(f'{guessNumber} is over {highCount}, try again.')
        return intro()

def binary_search(list, item):
    low = 0    
    high = len(list) -1 # due to zero indexing
    guessCount = 0

    while low <= high:
        mid = (low + high) // 2 # using the // converts it to an int
        guess = list[mid]
        guessCount += 1

        if guess == item:
            return [mid, guessCount]
        if guess > item:
            high = mid -1
        if guess < item:
            low = mid +1
    return None

def generateList(maxCount):
    newList = []
    for i in range(maxCount):
        newList.append(i)
    return newList

def main():
    response = intro()

    startTime = datetime.datetime.now()
    numericList = generateList(response[1])
    answer = binary_search(numericList, response[0])
    endTime = datetime.datetime.now()
    delta = endTime - startTime

    print(f'Binary search: {answer[0]} in {answer[1]} guesses --> {int(delta.total_seconds() * 1000)} ms')

main()