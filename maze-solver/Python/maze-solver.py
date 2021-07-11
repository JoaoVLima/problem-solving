import matplotlib.pyplot as plt
import matplotlib.image as mpimg

PATH_TO_IMG = '../img/maze.png'

IMG = mpimg.imread(PATH_TO_IMG)

green_start = [0,0]
red_end = [len(IMG)-1,len(IMG[0])-1]
for i in range(len(IMG)):
    for j in range(len(IMG[i])):
        for r,g,b in [IMG[i][j]]: 
            if r==0.0 and g==1.0 and b==0.0:
                print(f'greno bingo i{i} j{j}')
                green_start = [i,j]
            if r==1.0 and g==0.0 and b==0.0:
                print(f'redo bingo i{i} j{j}')
                red_end = [i,j]

def lookAround(xy):
    if [IMG[xy[0]][xy[1]]] == [0.0,1.0,0.0]:
        print([IMG[xy[0] +1 ][xy[1]]])

lookAround(green_start)


#IMG[red_end[0]][red_end[1]] = [0.0,0.0,0.0]



plt.imshow(IMG)
plt.show()
