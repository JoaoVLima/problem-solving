person_1 = [['10:00','11:00'],['14:00','14:30'],['15:30','17:30']]
person_2 = [['9:15','11:30'],['13:00','14:00'],['16:45','17:30'],['18:00','19:30']]

person_1_dailybounds = ['8:00',['12:00','13:00'],'18:00']
person_2_dailybounds = ['9:00',['12:00','13:00'],['15:15','16:30'],'20:15']

duration = 30

def conv_str_to_int(arr):
    for i in arr:
        for j in i:
            hour,minutes = [int(h) for h in j.split(':')]

conv_str_to_int(person_1)
conv_str_to_int(person_2)