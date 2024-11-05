import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.figure()

    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])

    # Create first line of best fit

    first_line = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    print(first_line.slope)

    plt.plot(range(1880,2051,1), range(1880,2051,1)*first_line.slope + first_line.intercept, color = "red")
    # Create second line of best fit
    
    second_line = linregress(df[df["Year"] >= 2000]["Year"], df[df["Year"] >= 2000]["CSIRO Adjusted Sea Level"])
    plt.plot(range(2000,2051,1), range(2000,2051,1)*second_line.slope + second_line.intercept, color = "green")



    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
