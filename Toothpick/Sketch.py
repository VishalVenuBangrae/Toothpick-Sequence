from graphics import *
from Toothpick import *
import sys
import time


def main():
    width = height = 1000
    toothpick_list = []
    iterations = sys.argv[1]
    win = GraphWin("Toothpick", width, height)
    win.setBackground("white")
    t1 = Toothpick(width/2, height/2, "horizontal")
    toothpick_list.append(t1)
    t1.show(win)
    temp_no = 1
    print("Iteration #0: Toothpicks added in this iteration: 1, Total #toothpicks: 1")
    for i in range(int(iterations)):
        temp = []
        time.sleep(0.4)
        for t1 in toothpick_list:
            toothpick_A = t1.add_toothpick_A(toothpick_list)
            toothpick_B = t1.add_toothpick_B(toothpick_list)

            if toothpick_A is not None:
                toothpick_A.show(win)
                temp.append(toothpick_A)

            if toothpick_B is not None:
                toothpick_B.show(win)
                temp.append(toothpick_B)

        toothpick_list.extend(temp)
        print(
            f"Iteration #{i + 1} #Toothpicks added in this iteration: {len(toothpick_list) - temp_no}, Total #toothpicks: {len(toothpick_list)}")
        temp_no = len(toothpick_list)

    win.getMouse()
    win.close()


if __name__ == "__main__":
    main()
