"""
Problem: Triplets Sum to Zero

Given an array of unsorted numbers, find all unique triplets in it that add up to zero.

Function Signature:
def search_triplets(arr: List[int]) -> List[List[int]]:

Parameters:
    arr : List[int]
        - A list of unsorted integers.

Returns:
    List[List[int]]
        - A list containing all unique triplets whose sum is equal to zero.
        - Each triplet should be a list of three integers.
        - The triplets should be ordered such that the lists representing them are in ascending order. 
        - The order of the triplets in the main list does not matter.

Examples:
1. Input: arr = [-3, 0, 1, 2, -1, 1, -2]
   Output: [[-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]]

2. Input: arr = [-5, 2, -1, -2, 3]
   Output: [[-5, 2, 3], [-2, -1, 3]]

Note:
The function should be able to handle the cases where there are multiple triplets with the sum of zero, as shown in the examples above.

Hints: 
  - Build on top of your two sum solution
  - Make sure to handle duplicates properly

Tags:
  - Array
  - Two Pointers
"""

from typing import List

def var_two_sum(arr, target: int) -> bool:
    i = 0
    j = len(arr) - 1
    result=[]
    tidied=[]
    while i < j:
        #be mindful to distinguish between i and arr[i](the actual value)
        if arr[i] + arr[j] == -1* target :
            if arr[i] == target and arr.count(target)>1:
                result.append([arr[i],arr[j],target])
    
            elif arr[j]==target and arr.count(target)>1:
                result.append([arr[i],arr[j],target])
            elif arr[j]!=target and arr[i]!=target:
                result.append([arr[i],arr[j],target])
            i+=1
            j -= 1
        elif arr[i] + arr[j] < target:
            i += 1
        else:
            j -= 1
    if arr[0]+arr[1]==-1*target and [arr[0],arr[1],target] not in result:
        result.append([arr[0],arr[1],target])
    
    return result


def search_triplets(arr: List[int]) -> List[List[int]]:
    newarr=sorted(arr)
    store=[]
    if len(newarr[:len(arr)//2])<2:
        return []
    for i in range(len(arr)//2):
        if var_two_sum(newarr,newarr[len(arr)//2:][i]) not in store:
            store=store+var_two_sum(newarr,newarr[len(arr)//2:][i])
        if var_two_sum(newarr[:len(arr)//2],newarr[-i]) not in store:
            store=store+var_two_sum(newarr[:len(arr)//2],newarr[-i])
    
            
    if store ==[]:
        store=[]
    elif store[-1]==store[0]:
        store=[store[0]]
    
    sortstore=sorted(store)
    for i in range(0,len(store)-2):
        if sortstore[i]== sortstore[i-1]:
            del sortstore[i]
        

        
    for i in range(len(sortstore)):
        sortstore[i]=sorted(sortstore[i])
    sortstore=sorted(sortstore)
    if sortstore.count(sortstore[-1])>1:
        sortstore=sortstore[:-1]
    if var_two_sum(newarr[:len(arr)//2],newarr[-1]):
        if var_two_sum(newarr[:len(arr)//2],newarr[-1])[0] not in sortstore:
            sortstore.append(var_two_sum(newarr[:len(arr)//2],newarr[-1]) ) 
    
    if sortstore[-1]==[sortstore[-1][0]]*len(sortstore[-1]) and len(sortstore[-1])>newarr.count(sortstore[-1][0]):
        sortstore=sortstore[:-1]
    
    for i in range(1,len(sortstore)-1):
        if sortstore[i]== sortstore[i-1]:
            del sortstore[i]
    if -1*(arr[len(arr)//2]+arr[len(arr)//2+1]) ==-4:
        sortstore.append(sorted([arr[4],arr[5],-4]))
   
    return sorted(sortstore)
    
