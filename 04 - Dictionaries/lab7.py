# Task 2:
# Write and test a function called isSorted that takes a list as a parameter and returns True if the list is sorted
# in ascending order and False otherwise. You can assume (as a precondition) that the elements of the list can be compared
# with the relational operators <, >, etc. For example, is_sorted([1,2,2]) should return True and is_sorted(['b','a'])
# should return False. #
# Two words are anagrams if you can rearrange the letters from one to spell the other. Write and test a function called
# isAnagram that takes two strings and returns True if they are anagrams.
#
# Write and test a function called removeDuplicates that takes a list and returns a new list with only the unique elements
# from the original. Hint: they don’t have to be in the same order.
#
# Write and test a function sumOfSquares(xs) that computes the sum of the squares of the numbers in the list xs.
# For example, sum_of_squares([2, 3, 4]) should return 4+9+16 which is 29.
#
# Write a program lab7.py that presents the user a menu to test the 4 functions from Task 2.
# Your program then gathers the necessary inputs to test the function and displays the result to the user.
# The user then has the opportunity to test another function until he/she decides to exit

def isSorted(myList): #prints TRUE if the sequence is sorted
    c = myList[:]
    c.sort()
    if myList == c:
        return ("True")
    else:
        return ('False')

def anagram(str1, str2): #prints TRUE if the two words are anagrams
    st1 = list(str1)
    st1.sort()
    st2 = list(str2)
    st2.sort()
    if st1 == st2:
        return('True')
    else:
        return("False")

def removeDuplicates(orig): #prints only unique elements
    dupItems = [ ]
    uniqElem = [ ]
    for x in orig:
        if x not in dupItems:
            uniqElem.append(x)
            dupItems.append(x)
    return (uniqElem)

def sumOfSquares(list1): #prints the sum of squared numbers typed
    adding = []
    i = 0
    while i < len(list1):
        sqr = (list1[i]) * (list1[i])
        adding.append(sqr)
        i = i + 1
    result = sum(adding)
    return result

user = 0
while user < 5:
    user = int(input("What function would you like to test today? Type: \n1 for 'Sorting' function; \n2 for 'Anagram' function; "
        "\n3 for 'Duplicates' function;\n4 for 'Square' function;\nor '5' to quit: > "))

    if user == 1:
        print("Lets check if a sequence of numbers or letters is sorted?")
        number1 = (input("Type the sequence of numbers or letters. (Ex: 1,2,3 or 'a', 'b', 'c') in any order you want.\nSeparate all items using commas(,). Letters must be inside quotes (' '): > "))
        myList = list(eval(number1))  # transforming string into elements of a list

        y = isSorted(myList)
        print(y)

        user2 = input("Would you like to try another function? Type 'yes' or 'no' (lowercase) > ")
        if user2 == "yes":
            continue
        else:
            print("OK, bye!")
            break

    elif user == 2:
        print("Two words are anagrams if you can rearrange the letters from one to spell the other,\nsuch as the words 'bowl' and 'blow', for instance.\nNow, test two words to see if they are anagrams: ")
        str1 = input("Type the first word: ")
        str2 = input("Type the second word: ")
        g = anagram(str1,str2)
        print(g)

        user3 = input("Would you like to try another function? Type 'yes' or 'no' (lowercase) > ")
        if user3 == "yes":
            continue
        else:
            print("Ok, bye!")
            break

    elif user == 3:
        print("Type a list with duplicated values.\nWe will return only the unique values from this list.")
        values = (input("Type the values separated by commas(,): > "))
        orig = list(eval(values))  # transforming string into elements of a list

        h = removeDuplicates(orig)
        print(h)

        user4 = input("Would you like to try another function? Type 'yes' or 'no' (lowercase) > ")
        if user4 == "yes":
            continue
        else:
            print("Ok, bye!")
            break

    if user == 4:
        print("Let's calculate the sum of some squares?\nType a sequence of numbers and we will give you the sum of their squares.\nNumbers should be separated using commas(,): > ")
        num1 = (input("Type a list of numbers: > "))
        list1 = list(eval(num1))

        y = sumOfSquares(list1)
        print (y)

        user5 = input("Would you like to try another function? Type 'yes' or 'no' (lowercase) > ")
        if user5 == "yes":
            continue
        else:
            print("Ok, bye")
            break

    else:
        print("Ok, thank you for your time!")                                                                                                                                                                                                                                                        