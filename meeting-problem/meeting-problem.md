# meeting-problem
There are 2 or more people trying to schedule a meeting, but everyone has their own stuff to do on that day, they need a program to give them the available hours they have for scheduling this meeting.

> The meeting has a minimum duration of 30min
>
> Each person gives an array that contains the begining and ending of every event they have on that day (24H format)
```python
person_1 = [['10:00','11:00'],['14:00','14:30'],['15:30','17:30']]
person_2 = [['9:15','11:30'],['13:00','14:00'],['16:45','17:30'],['18:00','19:30']]
```
> and they also give their dailybounds that is the begging and ending of their work hours with their lunch time or something else.
```python
person_1_dailybounds = ['8:00',['12:00','13:00'],'18:00']
person_2_dailybounds = ['9:00',['12:00','13:00'],['15:15','16:30'],'20:15']
```
> The program should output an array with the available hours for the meeting.
```python
output = [['11:30','12:00'],['14:30','15:15'],['17:30','18:00']]
```

## Solutions

[Python]: Python/meeting-problem.py

* [Python]