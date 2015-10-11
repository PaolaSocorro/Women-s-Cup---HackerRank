# Enter your code here. Read input from STDIN. Print output to STDOUT
import Queue
N = int(raw_input().strip())

n_pearls = raw_input().split()

pearls = Queue.PriorityQueue()

for i in n_pearls:
    pearls.put(int(i))
    

final_sum = 0


while pearls.qsize() > 1:
    min1 = pearls.get()
    min2 = pearls.get()
    sum_pearls = (min1 + min2) % ((10 ** 9) + 7)    # sum of two smallest pearls
    final_sum += sum_pearls                        # add this sum to running total
    pearls.put(sum_pearls)                         # update one of the pearls


print final_sum  % ((10 ** 9) + 7)