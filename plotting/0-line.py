#!/usr/bin/env python3
"""This module provides a function to plot a cubic line graph."""
import numpy as np
import matplotlib.pyplot as plt


def line():
    """Plots a red cubic line graph with the x-axis ranging from 0 to 10."""
    y = np.arange(0, 11) ** 3
    plt.figure(figsize=(6.4, 4.8))
    x = np.arange(0, 11)
    plt.plot(x, y, color='red')
    plt.xlim(0, 10)
    plt.show()
