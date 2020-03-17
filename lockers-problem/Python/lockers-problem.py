#     1 2 3 4 5
#     f f f f f

# 1   t t t t t
# 2     f   f  
# 3       f    
# 4         t  
# 5           f
# res t f f t f
# [1,4]

def lockers(n:int):
    arr = []
    for i in range(n):
        arr.append(False)
    return arr

def open_close(arr:list):
    l = len(arr)
    for i in range(1,l+1):
        for j in range(1,l+1):
            #print(f"{j} {i}")
            if j%i==0:
                #print(f"{j} is multiple of {i}")
                if arr[j-1] == False:
                    arr[j-1] = True
                    #print("false_to_true")
                else:
                    arr[j-1] = False
                    #print("true_to_false")
    return arr

def show_opened(arr:list):
    l = len(arr)
    arr2 = []
    for i in range(1,l+1):
        if arr[i-1] == True:
            arr2.append(i)
    return arr2

show_opened(open_close(lockers(1000)))