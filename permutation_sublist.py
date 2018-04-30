def permutation(inputArray):
    ret = []
    permutation_helper(inputArray,[],ret)
    return ret
    
def permutation_helper(inputArray,chosen,ret):
    if not inputArray:
        ret.append(chosen)
    else:
        for i, v in enumerate(inputArray):
            permutation_helper(inputArray[:i]+inputArray[i+1:],chosen+[v], ret)


a = ["aba", 
 "bbb", 
 "bab"]

def allSublist(arr):
    ret = []
    allSublist_helper(arr,[],ret)
    return ret

def allSublist_helper(arr,chosen,ret):
    if not arr:
        ret.append(chosen)
    else:
        allSublist_helper(arr[1:],chosen,ret)
        allSublist_helper(arr[1:],chosen+[arr[0]],ret)

b = allSublist(a)
print(len(b))
print(b)







    



