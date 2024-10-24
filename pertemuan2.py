import random
import statistics

rand_list = [random.randint(1, 100) for _ in range(10)]
rand_list.sort()
mean = statistics.mean(rand_list)
median = statistics.median(rand_list)
mode = statistics.mode(rand_list)

print(rand_list)
print(mean)
print(median)
print(mode)