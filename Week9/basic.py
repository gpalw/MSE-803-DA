import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
print("Current working directory:", os.getcwd())

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 40]
plt.plot(x, y, marker="o")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Basic Line Plot")
# plt.show()
plt.savefig("Bar_Line.png")


plt.figure(figsize=(6, 4))
categories = ["A", "B", "C", "D", "E"]
vars = [7, 10, 15, 19, 25]
plt.bar(categories, vars, color="green")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.title("Bar Plot")
plt.savefig("Bar_Plot.png")


categories = ["A", "B", "C", "D", "E"]
vars = [7, 10, 15, 19, 25]
plt.figure(figsize=(6, 6))
plt.pie(
    vars,
    labels=categories,
    autopct="%1.1f%%",
    startangle=140,
    colors=["blue", "green", "red", "purple", "orange"],
)
plt.xlabel("Categories")
plt.ylabel("Values")
plt.title("Pie Chart")
plt.savefig("Pie Chart.png")
