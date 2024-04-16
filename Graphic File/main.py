import matplotlib.pyplot as plot

# Set up the lists.
labels = ["Java", "Python", "JavaScript", "C/C++", "SQL", "PHP", "C#"]
sizes = [22, 21, 14, 10, 6, 5, 3]
colors = ["#ed2b2d", "#4987b7", "#f2dc56", "#0c4a86", "#dd793b", "#7b7fb6", "#a177da"]

# Make the pie chart.
fig1, ax1 = plot.subplots()
patches, texts, autotexts = ax1.pie(sizes, colors=colors, labels=labels, autopct='%1.1f%%', startangle=90,
                                    explode=[0, 0.1, 0, 0, 0, 0, 0])

# Display the pie chart.
ax1.set(aspect="equal", title="Most Used Programming Languages\nLJ")
plot.tight_layout()
plot.show()
