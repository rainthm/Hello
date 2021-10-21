# -* coding: utf-8 -*-
import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:

    rw = RandomWalk(5000)
    rw.fill_walk()
    #set the size of the window
    plt.figure(figsize=(20, 12))

    point_numbers = list(range(rw.num_points))
    #plt.scatter(rw.x_v, rw.y_v, c=point_numbers,cmap=plt.cm.Blues, edgecolors='none', s = 1)
    plt.plot(rw.x_v, rw.y_v,linewidth=1)
    #Render the start and end point with special color
    plt.scatter(rw.x_v[0], rw.y_v[0], c='red', s=100)
    plt.scatter(rw.x_v[-1], rw.y_v[-1], c='green', s=100)

    #hide the axes
    #there are two ways
    #way 1
    frame = plt.gca()
    frame.axes.get_yaxis().set_visible(False)
    frame.axes.get_xaxis().set_visible(False)

    #way 2
    #plt.axis('off')
    plt.show()

    keep_running = input("to continue another run?(y/n):")
    if (keep_running == 'n' or keep_running == 'N'):
        break