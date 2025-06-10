import numpy as np
import matplotlib.pyplot as plt

# Unordered_data= [89, 47, 164, 296, 30, 215, 138, 78, 48, 39]
# # Your ordered data
# data = [30, 39, 47, 48, 78, 89, 138, 164, 215, 296]

# # Calculate five-number summary
# minimum = np.min(data)
# q1 = np.percentile(data, 25)  # First quartile (25th percentile)
# median = np.median(data)      # Second quartile (50th percentile)
# q3 = np.percentile(data, 75)  # Third quartile (75th percentile)
# maximum = np.max(data)

# # Display five-number summary
# print("Five-Number Summary:")
# print(f"Minimum: {minimum}")
# print(f"First Quartile (Q1): {q1}")
# print(f"Median (Q2): {median}")
# print(f"Third Quartile (Q3): {q3}")
# print(f"Maximum: {maximum}")

# # Create box plot
# plt.figure(figsize=(8, 6))
# plt.boxplot(data, vert=False, patch_artist=True)
# plt.title("Box Plot of the Data")
# plt.xlabel("Value")
# plt.yticks([1], ["Data"])
# plt.grid(axis='x', alpha=0.5)

# # Annotate the five-number summary on the plot
# plt.scatter([minimum, q1, median, q3, maximum], [1, 1, 1, 1, 1], color='red', zorder=3)
# plt.text(minimum, 1.1, f"Min: {minimum}", ha='center')
# plt.text(q1, 1.1, f"Q1: {q1}", ha='center')
# plt.text(median, 1.1, f"Median: {median}", ha='center')
# plt.text(q3, 1.1, f"Q3: {q3}", ha='center')
# plt.text(maximum, 1.1, f"Max: {maximum}", ha='center')

# plt.tight_layout()
# plt.show()


# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns

# # Your data
# data = [30, 39, 47, 48, 78, 89, 138, 164, 215, 296]

# # Convert to 2D array for heatmap (1 row, 10 columns)
# data_2d = np.array(data).reshape(1, -1)

# # Create heatmap
# plt.figure(figsize=(12, 3))
# sns.heatmap(data_2d, 
#             annot=True, 
#             fmt="d", 
#             cmap="YlOrRd", 
#             cbar=True,
#             linewidths=.5)

# plt.title("Value Heatmap of Ordered Data")
# plt.xlabel("Position in Ordered Sequence")
# plt.yticks([])
# plt.show()


import matplotlib.pyplot as plt
import numpy as np

# Your ordered data
data = [30, 39, 47, 48, 78, 89, 138, 164, 215, 296]
positions = np.arange(1, len(data)+1)  # Positions in the ordered sequence

# Create scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(positions, data, 
            c='darkblue',  # Color of points
            s=100,         # Size of points
            alpha=0.7,     # Transparency
            edgecolor='black')  # Border color

# Add labels and title
plt.title("Scatter Plot of Ordered Data", fontsize=14)
plt.xlabel("Position in Ordered Sequence", fontsize=12)
plt.ylabel("Value", fontsize=12)
plt.grid(True, alpha=0.3)

# Annotate each point with its value
for pos, val in zip(positions, data):
    plt.text(pos, val+5, str(val), 
             ha='center', 
             va='bottom', 
             fontsize=10)

# Customize x-axis ticks
plt.xticks(positions)

# Show plot
plt.tight_layout()
plt.show()