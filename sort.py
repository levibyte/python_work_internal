def swap_if(array):
    print("swaapping")
    if array[0] > array[1]:
       array[0],array[1] = array[1],array[0]
    #return array

def mergeSort(array):
    if len(array) > 1:
        if len(array) == 2:
                #array = 
                swap_if(array)
        else:
            mid = len(array)//2
            A = array[mid:]
            B = array[:mid]
            
            mergeSort(A);
            mergeSort(B);
            
            i = j = k = 0;
            while i < len(A) and j < len(B):
                if A[i] <= B[j]:
                    array[k] = A[i]
                    i+=1
                else:
                    array[k] = B[j]
                    j+=1
                k+=1
            
            while i < len(A): 
                arr[k] = A[i] 
                i+=1
                k+=1
            
            while j < len(B): 
                arr[k] = B[j] 
                j+=1
                k+=1
                
    return array

def printList(array):
    print(array)
    
if __name__== "__main__":
    #arr = [12, 11] 
    arr = [12, 11, 13, 5, 6, 7] 
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
