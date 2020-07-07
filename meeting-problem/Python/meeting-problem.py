person_1 = [['10:00','11:00'],['14:00','14:30'],['15:30','17:30']]
person_2 = [['9:15','11:30'],['13:00','14:00'],['16:45','17:30'],['18:00','19:30']]

person_1_dailybounds = ['8:00',['12:00','13:00'],'18:00']
person_2_dailybounds = ['9:00',['12:00','13:00'],['15:15','16:30'],'20:15']

duration = 30

def conv_str_to_int(arr:list):
    for i in range(len(arr)):
        if(type(arr[i])==list):
            for j in range(len(arr[i])):
                h,m = arr[i][j].split(':')
                arr[i][j] = (int(h),int(m))
        else:
            h,m = arr[i].split(':')
            arr[i] = (int(h),int(m))
    return arr

def available_times(arr:list,arr_dailybounds:list):
    begin,end = arr_dailybounds[:1][0],arr_dailybounds[-1:][0]
    print(f'{begin} {end}')
    
    
    
    
    for h in range(begin[0],end[0]+1):
        if h==begin[0]:
            for m in range(begin[1],60):
                print(f'{h} {m}')
        else:
            for m in range(60):
                #print(f'{h} {m}')
                if h==end[0] and m==end[1]:
                    break




                
    return arr

available_times(conv_str_to_int(person_1),conv_str_to_int(person_1_dailybounds))
available_times(conv_str_to_int(person_2),conv_str_to_int(person_2_dailybounds))