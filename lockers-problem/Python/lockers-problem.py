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
#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625, 676, 729, 784, 841, 900, 961]