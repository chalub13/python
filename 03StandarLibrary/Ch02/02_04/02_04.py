# Statistics Module
import statistics
import math

agesData = [10, 14, 13, 12, 11, 10, 11, 10, 15]

print(statistics.mean(agesData))
print(statistics.mode(agesData))
print(statistics.median(agesData))

print(sorted(agesData))

print(statistics.variance(agesData))

print(statistics.stdev(agesData))
print(math.sqrt(statistics.variance(agesData)))
