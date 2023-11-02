import time
import tracemalloc
import matplotlib.pyplot as plt

import brute_force
import knut_morris_pratt
import rabin_karp
import aho_corasick


def draw_graph_time():
    methods = [brute_force, knut_morris_pratt, rabin_karp, aho_corasick]
    titles = ['Brute Force', 'Knut-Morris-Pratt', 'Rabin-Karp', 'Aho-Corasick']

    for method, title in zip(methods, titles):
        x_time, y_time = [], []

        for i in range(10, 100000, 10000):
            time_sum = 0

            for j in range(1, i, 10000):
                start_time = time.time()
                string = 'a' * i
                sub_str = 'a' * j + 'b'
                method.find_substring(string, sub_str)
                end_time = time.time()

                time_sum += ((end_time - start_time) * 10 ** 3)

            x_time.append(i)
            y_time.append(time_sum)

        plt.subplot(2, 1, 2)
        plt.plot(x_time, y_time, label=title)
        plt.xlabel('Длина строки')
        plt.ylabel('Время')
        plt.legend()

    plt.show()


def draw_graph_memory():
    methods = [brute_force, knut_morris_pratt, rabin_karp, aho_corasick]
    titles = ['Brute Force', 'Knut-Morris-Pratt', 'Rabin-Karp', 'Aho-Corasick']

    for method, title in zip(methods, titles):
        x_memory, y_memory = [], []

        for i in range(10, 100000, 10000):
            memory_sum = 0

            for j in range(1, i, 10000):
                tracemalloc.start()
                string = 'a' * i
                sub_str = 'a' * j + 'b'
                method.find_substring(string, sub_str)
                memory_sum += tracemalloc.get_traced_memory()[0]

            x_memory.append(i)
            y_memory.append(memory_sum)

        plt.subplot(2, 1, 2)
        plt.plot(x_memory, y_memory, label=title)
        plt.xlabel('Длина строки')
        plt.ylabel('Память')
        plt.legend()

    plt.show()


draw_graph_time()
draw_graph_memory()