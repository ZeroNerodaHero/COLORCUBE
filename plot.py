import matplotlib.pyplot as plt

# Define the range of coordinates
x_range = range(100)
y_range = range(100)

# Create a figure and axis
fig, ax = plt.subplots()

# Loop through each point and assign a color based on its coordinates
for x in x_range:
    for y in y_range:
        # Calculate RGB values based on coordinates
        r = x / max(x_range)
        g = y / max(y_range)
        b = 1 - (x / max(x_range)) * (y / max(y_range))  # Example formula
        
        # Plot the point with the assigned color
        ax.scatter(x, y, color=(r, g, b))

# Show the plot
plt.show()

