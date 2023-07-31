import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

def plot_bar_chart():
    cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
    population = [8537673, 3979576, 2693976, 2129784, 1680992]

    fig, ax = plt.subplots()
    ax.bar(cities, population)
    ax.set_xlabel('City')
    ax.set_ylabel('Population')
    ax.set_title('Population of Different Cities')

    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Create the tkinter window
window = tk.Tk()
window.title("Bar Chart")

# Call the function to plot the bar chart
plot_bar_chart()

# Run the tkinter main loop
window.mainloop()
