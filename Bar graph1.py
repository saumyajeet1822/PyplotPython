import matplotlib.pyplot as plt
import numpy as np

df={'C':10, 'java':15, 'Python':18}

fields = list(df.keys())
students = list(df.values())

fig = plt.figure(figsize = (10,5))

plt.bar(fields, students, color =("green","red", "yellow"), width =0.2)
plt.xlabel("Field of study")
plt.ylabel("No.of Study")
plt.title("Student studying list")

plt.show()
