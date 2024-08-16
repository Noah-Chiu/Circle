import math,os,time,sys

def circle(r):
    xAxis = r*2+1

    yAxis = r*2+1

    canvas = [[None for i in range(xAxis)] for i in range(yAxis)]

    theta = math.pi/180.0

    for i in range(360):
        # print(i)

        x = r+r*(math.cos(theta*i))
        y = r+r*(math.sin(theta*i))

        # print(x, y)

        canvas[round(x)][round(y)] = "O"

    for i in range(xAxis):
        for j in range(yAxis):
            if canvas[i][j] is not None:
                print(canvas[i][j], end="")

            else:
                print(".", end="")
        print()

def main(argv, arc):
    if arc == 2:
        print(argv[1])
        circle(int(argv[1]))
    else:
        print("請輸入一筆參數")
    
if __name__ == '__main__':
    main(sys.argv, len(sys.argv))