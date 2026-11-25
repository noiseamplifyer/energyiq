
# def calculate_average(values):
#     pass

# def find_maximum(values):
#     pass

# def count_missing(values):
#     pass

# import pandas as pd

# df = pd.read_csv(
#     "data/raw/household_power_consumption.txt",
#     sep=";",
#     na_values="?"
# )

# df.head()
# df.shape
# df.info()
# df.describe()


# def analyze_power_data(power):
#     # your code
#     Total = len(power)
#     missing = 0
#     invalid = 0
#     valid_values = []
    
#     for value in power:
#         if value is None:
#             invalid += 1
#         elif value < 0:
#             missing += 1
#         else:
#             valid_values.append(value)
    
#     valid_count = len(valid_values)
#     maximum= max(valid_values)
#     minimum = min(valid_values)
#     avg = sum(valid_values) / valid_count
    
#     result = {
#         "Total": Total,
#         "missing" : missing,
#         "invalid" : invalid,
#         "valid" : valid_count,
#         "maximum" : maximum,
#         "minimum" : minimum,
#         "average" : avg
#     }

#     return result


# power = [1.2, 1.5, None, 2.1, -1.0, 1.8, None, 5.5]

# result = analyze_power_data(power)
# print("Total ", result["Total"])
# print("Valid ",result["valid"])
# print("Invalid ", result["invalid"])
# print("Missing ", result["missing"])
# print("Maximum ", result["maximum"])
# print("Minimum ", result["minimum"])
# print("Average ", result["average"])

# import numpy as np

# power = np.array([1.2, 1.5, 1.8, 2.1, 1.7, 5.8, 1.9])
# voltage = np.array([230.2, 231.5, 229.8, 245.7, 230.9])

# index = np.argmax(voltage)


# high_power = power[(power >= 2) & (power <= 4)]
# count = np.sum(power > 2 )

# print("High power", high_power)
# #power = np.array([1.2, 1.5, 1.8, 2.1, 1.7])
# print("count", count)

# print("Minimum:", np.min(power))
# print("Maximum:", np.max(power))
# print("Average:", np.mean(power))
# print("Median:", np.median(power))
# print("Standard deviation:", np.std(power))

# print("Voltage index", index)
# print("Max voltage", voltage[index])

#import numpy as np

# power = np.array([
#     1.2, 1.4, 1.5, 1.3,
#     1.6, 1.5, 9.8, 1.4,
#     1.6, 1.5, 1.3, 1.4,
#     1.7, 1.6, 0.2
# ])

# power = np.array( [1.2, 1.4, 1.5, 1.3, 9.8, 1.4, 0.2, 1.6 ])

# print("Total size", power.size)
# print("Average power", np.sum(power)/power.size)
# print("minimum", np.min(power))
# print("maximum", np.max(power))
# print("reading greater than 3 ", power[power > 3])
# print("reading less than 0.5 ", power[power < 0.5])
# print("Invalid power", power[(power >= 0.5) & (power <= 3)])
# print("Invalid power position", np.where(power[(power >= 0.5) & (power <= 3)]))
# print("Avg of valid power", sum(power[(power >= 0.5) & (power <= 3)])/power.size)

# import pandas as pd

# file_path = "data/raw/household_power_consumption.txt"

# df = pd.read_csv(
#     file_path,
#     sep=";",
#     na_values="?"
    
# )

# df.head()
# print(df.head())
# print(df.tail())
# print(df.shape)
# print(df.info())
# print(df.isna().sum())
