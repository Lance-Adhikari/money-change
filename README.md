# Money Change

A Python solution that finds the fewest coins needed for a nonnegative integer amount using denominations **10, 5, and 1**.

[money_change.py](money_change.py) repeatedly takes the largest coin that fits the remaining amount. This greedy approach gives the minimum for these denominations.

The sample amount **28** needs **6 coins**: two 10s, one 5, and three 1s.
