import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Data for three workstations
workstations = ['Bottling', 'Labeling', 'Packaging']
num_of_machines = [2, 4, 1]
efficiencies = [66000, 34500, 120000]
products = [count * efficiency for count, efficiency in zip(num_of_machines, efficiencies)]

# Creating figure and axes
fig, ax = plt.subplots()

# Initializing the bar chart with initial heights
bars = ax.bar(workstations, products, align='center')

# Function to initialize the animation
def init_animation():
    return bars

# Function to update the animation
def update_animation(i):
    global num_of_machines, products
    
    # Calculating the product of machine counts and efficiencies for each workstation
    products = [count * efficiency for count, efficiency in zip(num_of_machines, efficiencies)]
    
    # Finding the index of the workstation with the smallest product
    min_index = products.index(min(products))
    
    # Adding 1 to the machine count for the workstation with the smallest product
    num_of_machines[min_index] += 1
    
    # Updating the heights of the bars
    for i, bar in enumerate(bars):
        height = products[i]
        bar.set_height(height)
        if i == min_index:
            bar.set_color('red')  # Mark the shortest bar in red
        else:
            bar.set_color('blue')  # Other bars in blue
    
    # Scaling the y-axis based on the maximum product
    max_product = max(products)
    ax.set_ylim(0, max_product * 1.2)  # Additional 20% margin
    
    # Returning the bars for animation update
    return bars

# Creating the animation
animation = FuncAnimation(fig, update_animation, frames=30, init_func=init_animation, blit=True, interval=1000)

# Saving the animation to an mp4 file
animation.save('throat_shift.mp4', writer='ffmpeg')

# Displaying the animation
plt.show()
