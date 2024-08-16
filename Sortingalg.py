import json

with open('ArrayDatasets/almost_sorted_list.json', 'r') as file:
    almost_sorted_list = json.load(file)

with open('ArrayDatasets/random_list.json', 'r') as file:
    random_list = json.load(file)

with open('ArrayDatasets/reverse_sorted_list.json', 'r') as file:
    reverse_sorted_list = json.load(file)

with open('ArrayDatasets/sorted_list.json', 'r') as file:
    sorted_list = json.load(file)

with open('ArrayDatasets/partially_sorted_list.json', 'r') as file:
    partially_sorted_list = json.load(file)

def selection_sort(arr):
    for i in range(len(arr)):
        m=i
        for j in range(i,len(arr)):
            if (arr[j] < arr[m]):
                m=j
        arr[i] , arr[m] = arr[m] , arr[i]
    return (arr)

def pysort(arr,cond=False):
    #If cond==True sort alreves
    if(cond):
        arr.sort(reverse = True)
    else:
        arr.sort()
    return arr


def quicksort(arr):
    if(len(arr)<=1):
       return arr
    pivot=arr[0]
   
    L = [x for x in arr if x < pivot]
    M = [x for x in arr if x == pivot]
    R = [x for x in arr if x > pivot]

    return quicksort(L) + M + quicksort(R)


def mergesort(arr):
    if (len(arr)<=1):
        return arr

    mid = len(arr)//2
    L=mergesort(arr[:mid])
    R=mergesort(arr[mid:])

    sorted_arr=[]
    i=j=0

    while(i < len(L) and j < len(R)):
        if L[i] < R [j]:
            sorted_arr.append(L[i])
            i+=1
        else:
            sorted_arr.append(R[j])
            j+=1

    sorted_arr.extend(L[i:])
    sorted_arr.extend(R[j:])

    return sorted_arr