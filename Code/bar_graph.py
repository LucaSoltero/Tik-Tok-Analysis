# Author: Luca Soltero
# Email: lsoltero@usc.edu
# Course: Introduction to Econometrics (ECON 318) USC

from Analysis import dataFrame
import matplotlib.pyplot as plt
df = dataFrame()

avg_durs = df.groupby("dur")

duration = [i[0] for i in avg_durs]

# create bar graph
fig, ax = plt.subplots()
ax.bar(duration, df["dur"].value_counts(), color="red")
plt.xlabel('Duration of Tik Tok\'s')
plt.ylabel('Amount of Data Points with given Duration')
plt.title("Distribution of Tik Tok Duration")
plt.show()