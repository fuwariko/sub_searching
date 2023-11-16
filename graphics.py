import time
import tracemalloc
import matplotlib.pyplot as plt
from random import choice
from string import ascii_letters

import brute_force
import knut_morris_pratt
import rabin_karp
import aho_corasick
import z_function


def draw_graph_time(method):
    x_time, y_time = [], []

    for i in range(10, 100000, 10000):
        time_sum = 0

        for j in range(1, i, 10000):
            str = ''.join(choice(ascii_letters) for _ in range(i))
            sub_str = ''.join(choice(ascii_letters) for _ in range(j))
            start_time = time.time()
            method.find_substring(str, sub_str)
            end_time = time.time()
            time_sum += ((end_time - start_time) * 10 ** 3)

        x_time.append(i)
        y_time.append(time_sum)

    return [x_time, y_time]


def draw_graph_memory(method):
    x_memory, y_memory = [], []

    for i in range(10, 100000, 10000):
        memory_sum = 0

        for j in range(1, i, 10000):
            str = ''.join(choice(ascii_letters) for _ in range(i))
            sub_str = ''.join(choice(ascii_letters) for _ in range(j))
            tracemalloc.start()
            method.find_substring(str, sub_str)
            memory_sum += tracemalloc.get_traced_memory()[0]

        x_memory.append(i)
        y_memory.append(memory_sum)

    return [x_memory, y_memory]


def draw_time_graphs():
    methods = [brute_force, knut_morris_pratt, rabin_karp, aho_corasick, z_function]
    titles = ['Brute Force', 'Knut-Morris-Pratt', 'Rabin-Karp', 'Aho-Corasick', "z-function"]
    k = 1

    for method, title in zip(methods, titles):
        x, y = draw_graph_time(method)
        plt.subplot(5, 2, k)
        plt.plot(x, y, label=title)
        plt.xlabel('Длина строки')
        plt.ylabel('Время')
        plt.legend()
        k = k + 1

    plt.show()


def draw_memory_graphs():
    methods = [brute_force, knut_morris_pratt, rabin_karp, aho_corasick, z_function]
    titles = ['Brute Force', 'Knut-Morris-Pratt', 'Rabin-Karp', 'Aho-Corasick', "z-function"]
    k = 1

    for method, title in zip(methods, titles):
        x, y = draw_graph_memory(method)
        plt.subplot(5, 2, k)
        plt.plot(x, y, label=title)
        plt.xlabel('Длина строки')
        plt.ylabel('Память')
        plt.legend()
        k = k + 1

    plt.show()


draw_time_graphs()
draw_memory_graphs()
