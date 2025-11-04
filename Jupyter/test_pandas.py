import pandas as pd

# print(pd.__version__)

#Series:
# data = [100.2, 200.2, 400, 401]
#
# series = pd.Series(data, index=["a", "b", "c", "d"])
# series.loc["d"] = 402.76
#
# print(series[series > 200.3])

#dictonaries = key:value pairs
calories = {"day 1": 1750, "day 2": 2100, "day 3": 1700}

series = pd.Series(calories)
series.loc["day 3"] += 300
print(series)
