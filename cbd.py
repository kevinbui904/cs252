#Written by Thien K. M. Bui
#cs252 Fall 2023

import random

#Given n-sized list containing 'cat', 'bird', or 'dog', sort them 
# in cbd (cat dog bird) order in O(n) time without using helper arrays
def main():
    for test_number in range(100000):
        n = 100
        sorted = []
        lst = []

        sorted = ['dog', 'dog', 'dog', 'cat', 'bird', 'bird', 'bird', 'cat', 'bird', 'dog']
        for i in range(n):
            choice = random.choice(['cat', 'bird', 'dog'])
            sorted.append(choice)
            lst.append(choice)

        first_bird = first_dog = None

        if sorted[0] == 'bird':
            first_bird = 0
        elif sorted[0] == 'dog':
            first_dog = 0
        for i in range(1, n):
            if sorted[i] == "dog" and first_dog is None:
                first_dog = i
            if sorted[i] == "bird" and first_bird is None:
                #this is an edge case that only happens when the first bird is found after a sequence of dogs
                if sorted[i-1] == "dog":
                    sorted[i], sorted[first_dog] = sorted[first_dog], sorted[i]
                    first_bird = first_dog
                    first_dog += 1 
                else:
                    first_bird = i
            else:
                if sorted[i] == 'cat':
                    if sorted[i - 1] == 'bird':
                        sorted[first_bird], sorted[i] = sorted[i], sorted[first_bird]
                        first_bird += 1
                    elif sorted[i - 1] == 'dog':
                        if first_bird is not None:
                            sorted[first_bird], sorted[i] = sorted[i], sorted[first_bird]
                            sorted[first_dog], sorted[i] = sorted[i], sorted[first_dog]
                            first_bird += 1
                            first_dog += 1
                        else:
                            sorted[first_dog], sorted[i] = sorted[i], sorted[first_dog]
                            first_dog += 1
                elif sorted[i] == 'bird':
                    if sorted[i - 1] == 'dog':
                        sorted[first_dog], sorted[i] = sorted[i], sorted[first_dog]
                        first_dog += 1

        #testing code
                    
        for i in range(1,n):
            if sorted[i-1] == "bird" and sorted[i] == "cat":
                print("INCORRECT 2")
                print("lst:", lst)
                print("sorted: ", sorted)
                quit()
            if sorted[i-1] == "dog" and sorted[i] == "cat":
                print("INCORRECT 3")
                print("lst:", lst)
                print("sorted: ", sorted)
                quit()
            if sorted[i-1] == "dog" and sorted[i] == "bird":
                print("INCORRECT 4")
                print("lst:", lst)
                print("sorted: ", sorted)
                quit()

            sorted[i-1] = sorted[i]

if __name__ =='__main__':
    main()