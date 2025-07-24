import matplotlib.pyplot as plt

# Create a figure with multiple subplots
fig, axs = plt.subplots(2, 2)  # 2 rows, 2 columns of subplots

# Plot data in each subplot
axs[0, 0].plot([1, 2, 3], [1, 2, 3])
axs[0, 0].set_title('Plot 1')
axs[0, 1].plot([1, 2, 3], [1, 4, 9])
axs[0, 1].set_title('Plot 2')
axs[1, 0].plot([1, 2, 3], [1, 8, 27])
axs[1, 0].set_title('Plot 3')
axs[1, 1].plot([1, 2, 3], [1, 16, 81])
axs[1, 1].set_title('Plot 4')

# Apply tight_layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()
