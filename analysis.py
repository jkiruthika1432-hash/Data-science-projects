import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("student_marks.csv")

df["Average"] = (df["Maths"] + df["Science"] + df["English"]) / 3

print(df)

highest = df.loc[df["Average"].idxmax()]
print("\nTop Student:")
print(highest)

plt.bar(df["Name"], df["Average"])
plt.title("Student Average Marks")
plt.xlabel("Students")
plt.ylabel("Average Marks")
plt.show()