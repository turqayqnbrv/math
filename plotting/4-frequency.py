#!/usr/bin/env python3
'''Histogram usage'''
import numpy as np
import matplotlib.pyplot as plt


def frequency():
    '''The function plots a frequency of the grades'''
    np.random.seed(5)
    student_grades = np.random.normal(68, 15, 50)
    plt.figure(figsize=(6.4, 4.8))

    bin_edges = np.arange(0, 110, 10)
    plt.hist(student_grades, bins=bin_edges, edgecolor='black')
    
    plt.xlabel("Grades")
    plt.ylabel("Number of Students")
    plt.title("Project A")
    plt.xlim(0, 100)
    plt.show()
