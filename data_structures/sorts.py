#Selection Sort Code
import random

def swap(indexOne,indexTwo,lst):
    #hold the value of one of the indices
    temp = lst[indexOne]

    # swap the held index with the other index
    lst[indexOne] = lst[indexTwo]

    #swap the second index with the temp stored value
    lst[indexTwo] = temp
def generateList(num):
    #generate a list of random numbers
    #paramater determines the length of the list
    lst = []
    for x in range(num):
        lst.append(random.randrange(0,1000))
    return lst
def selectionSort(lst):
    #select each element in the array
    for i in range(0,len(lst)):
        #mark the expansion of the frontier (sorted vs unsorted)
        startIndex  =  i
        minIndex = i
        #select each element after the current element
        for j in range(i+1,len(lst)):
            #check if any element is less than it
            if lst[j] < lst[minIndex]:
                minIndex = j
        swap(startIndex,minIndex,lst)
def bubbleSort(lst):
    for i in range(0,len(lst)):
        for j in range(0,i):
            if lst[j] > lst[i]:
                swap(i,j,lst)
def insertionSort(arr):

    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):

        key = arr[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key
def mergeSort(lst,size):
  if size <2:
    return 0
  mid = len(lst)//2
  lstA = lst[:mid]
  lstB = lst[mid:]
  mergeSort(lstA,len(lstA))
  mergeSort(lstB,len(lstB))
  merge(lstA,lstB,lst)
def merge(A,B,C):
  sizeA = len(A)
  sizeB = len(B)
  i = 0
  j = 0
  k = 0
  while i < len(A) and j < len(B):
      if A[i] <= B[j]:
          C[k] = A[i]
          k+=1
          i+=1
      else:
          C[k] = B[j]
          k+=1
          j+=1
  while i < len(A):
     C[k] = A[i]
     k+=1
     i+=1
  while j < len(B):
     C[k] = B[j]
     k+=1
     j+=1
def quicksort(lst,left,right):
    if left<right:
        #divide
        pivot_pos = parition(lst,left,right)
        #conquer
        quicksort(lst,left,pivot_pos-1)
        quicksort(lst,pivot_pos+1,right)
def parition(lst,left,right):
    
    pivot_val = lst[right]
    pivot_pos = right
    right-=1

    while left <= right:
        if lst[left] <= pivot_val:
            left+=1
        elif lst[right] >= pivot_val:
            right-=1
        else:
            swap(left,right,lst)

    swap(left,pivot_pos,lst)
    return left
def main():
    lst = generateList(10)
    print(lst)
    quicksort(lst,0,len(lst)-1)
    print(lst)



main()
