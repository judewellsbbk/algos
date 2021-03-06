from random import randint
import time

def MaxPairwiseProduct(a, n):
    """This is the example solution given in the PDF"""
    product = 0
    for i in range(n):
        for j in range(i + 1, n):
            product = max(product, a[i]* a[j])
    return product

def findTwoLargest(listy):
    n = len(listy)
    index1 = 0 # Index1 will be the index of the biggest number in the array.
    index2 = 1 # Index2 will be the 2nd biggest number in the array.
    if listy[index2] > listy[index1]: # If index2 is bigger than index1 then swap their values
        index1, index2 = index2, index1 # Now we know that index1 is the position of the larger of the 2 values
    for i in range(2, n):
        if listy[i] > listy[index2]:
            if listy[i] > listy[index1]:
                index1, index2 = i, index1
            else:
                index2 = i
    #print("Jude function: ", listy[index1], " ", listy[index2], " Product: ", listy[index1] * listy[index2])

    return listy[index1] * listy[index2]



def findTwoLargest2(listy):
    first = listy[0]
    second = listy[1]
    if second > first:
        first, second = second, first

    for i in range(2, len(listy)):
        if listy[i] > second:
            if listy[i] >  first:
                first, second = listy[i], first
            else:
                second = listy[i]
    return first * second


def findTwoLargest3(listy):
    first = listy[0]
    second = listy[1]
    if second > first:
        first, second = second, first
    listy = listy[2:]
    for element in listy:
        if element > second:
            if element >  first:
                first, second = element, first
            else:
                second = element
    return first * second

def patrick_max_pairwise_product(s):
    '''Function to return max pairwise product'''
    gn = s[0]
    gnminus = 0
    for i in range(1, len(s)):
        if s[i] > gn:
            gnminus = gn
            gn = s[i]
        else:
            if s[i] > gnminus:
                gnminus = s[i]
            else:
                continue
    return(gn * gnminus)

def listyGen(n, m):
    # Generates lists for testing
    ls = []
    for i in range(n):
        ls.append(randint(1, m))
    return(ls)

listy = listyGen(200, 50)
n = len(listy)

findTwoLargest(listy)
MaxPairwiseProduct(listy, n)

def stressTest(iterations):
    """ The iterations argument is the number of lists generated to test the functions on.
    Within the function you can also change the max length and maximum possible integer in the list.


    """
    for i in range(iterations):
        nMax = 1000 # How long can the longest list be
        elementMax = 5000 # How large can the largest element be
        n = randint(2, nMax)
        m = randint(1, elementMax)
        listy = listyGen(n, m)
        if findTwoLargest(listy) == findTwoLargest3(listy):
            print("OK")
        else:
            print("Fail")
            print(listy)
            print(findTwoLargest(listy), findTwoLargest3(listy))
            return
    print("TEST PASSED")

#stressTest(10000)

def speedTest(newLists, iterations):
    """ The iterations argument is the number of lists generated to test the functions on.
    Within the function you can also change the max length and maximum possible integer in the list.


    """
    function1Time = 0
    function2Time = 0
    function3Time = 0
    patrickTime = 0
    for i in range(newLists):
        nMax = 10000 # How long can the longest list be
        elementMax = 5000 # How large can the largest element be
        n = randint(2, nMax)
        m = randint(1, elementMax)
        listy = listyGen(n, m)

        start = time.time()
        for _ in range (iterations):
            findTwoLargest(listy)
        function1Time += time.time() - start

        start = time.time()
        for _ in range (iterations):
            findTwoLargest2(listy)
        function2Time += time.time() - start

        start = time.time()
        for _ in range (iterations):
            findTwoLargest3(listy)
        function3Time += time.time() - start

        start = time.time()
        for _ in range (iterations):
            patrick_max_pairwise_product(listy)
        patrickTime += time.time() - start

    print("Function 1 time: ", function1Time, "\nFunction 2 time: ", function2Time, "\nFunction 3 time: ", function3Time, "\nPatrick's Function time: ", patrickTime)

speedTest(50, 1000)


"""
We go through each element in the array and check if it's bigger than index2 this = n - 2 comparisons minimum. 
But for some problems we have to do 2 comparisons: i > index2? followed by i>index1?

Whats the probability that the first number compared will be bigger than the value at index2? I would say around 66%

So there's a 66% chance that we do 2 comparisons for the first position.

This means that we have looked at 3 numbers in total and index1 and index2 are the largest of these 3:
on the next comparison whats the probability that the new number (i) is bigger than index2? I reckon there is now a 50% 
chance that it is bigger than index 2 and a 25% chance that it is bigger than index1.

How can we put this changing probability into a formula?

Probability that the compared number is bigger than index2 = 
2 / total number of positions compared.

"""
#code for calculating average number of comparisons:
def comparisonCalculator(n):
    total = n
    for i in range(2, n-1):
        total += 2/(2+i)
    return total

#print("n=100: ", comparisonCalculator(100))
#print("n=500: ", comparisonCalculator(500))
#print("n=1000: ", comparisonCalculator(1000))