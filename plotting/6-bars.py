#!/usr/bin/env python3
'''Stacking bar implementation'''
import numpy as np
import matplotlib.pyplot as plt


def bars():
    '''Function returns the groups of
    people, fruits, and colors in a stacked bars'''
    np.random.seed(5)
    fruit = np.random.randint(0, 20, (4, 3))
    plt.figure(figsize=(6.4, 4.8))

    people = ['Farrah', 'Fred', 'Felicia']
    colors = ['red', 'yellow', '#ff8000', '#ffe5b4']
    labels = ['apples', 'bananas', 'oranges', 'peaches']
    width = 0.5

    bottom_vals = np.zeros(3)

    for i in range(len(fruit)):
        plt.bar(people, fruit[i], width=width, 
                bottom=bottom_vals, color=colors[i], label=labels[i])
        bottom_vals += fruit[i]

    plt.ylabel('Quantity of Fruit')
    plt.title('Number of Fruit per Person')
    plt.yticks(list(range(0, 81, 10)))
    plt.ylim([0, 80])
    plt.legend()
    plt.show()
