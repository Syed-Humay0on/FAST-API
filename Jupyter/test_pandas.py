import pandas as pd

# print(pd.__version__)

#Series:
data = [100.2, 200.2, 400, 401]

series = pd.Series(data, index=["a", "b", "c", "d"])
series.loc["d"] = 402.76

print(series)
