import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv", index_col = "date", parse_dates = True)

# Clean data
df = df.loc[(df["value"] >= df["value"].quantile(0.025)) &
            (df["value"] <= df["value"].quantile(0.975))]


def draw_line_plot():
    # Draw line plot

    fig, ax = plt.subplots(figsize = (20, 5))

    ax.plot(pd.to_datetime(df.index), df["value"])


    tick_dates = pd.date_range(start = "2016-07-01", end = "2020-01-01", freq = "6MS" )
    tick_labels = tick_dates.strftime('%Y-%m')  

    ax.set_xticks(tick_dates)
    ax.set_xticklabels(tick_labels)
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar["Year"] = df.index.year
    df_bar["Months"] = df.index.month_name()

    
    month_order = ["January", "February", "March", "April", "May", "June", 
                   "July", "August", "September", "October", "November", "December"]

    df_bar['Months'] = pd.Categorical(df_bar['Months'], categories=month_order, ordered=True)


    df_bar = df_bar.groupby(["Year","Months"], as_index = False)["value"].mean()

# Count of unique combinations
    
    fig = plt.figure()    
    sns.barplot(data=df_bar, x="Year", y="value", hue="Months", hue_order= month_order, fill = True)

    plt.xlabel("Years")
    plt.ylabel("Average Page Views")
    plt.xticks(rotation = 90)


    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    
    fig, axes = plt.subplots(1,2, figsize = (20,10))

    #1
    sns.boxplot(data = df_box, x = "year", y = "value", ax = axes[0] )
    axes[0].set_xlabel("Year")
    axes[0].set_ylabel("Page Views")
    axes[0].set_title('Year-wise Box Plot (Trend)')


    #2
    sns.boxplot(data = df_box, x = "month", y = "value", ax = axes[1], order = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"] )
    axes[1].set_xlabel("Month")
    axes[1].set_ylabel("Page Views")
    axes[1].set_title('Month-wise Box Plot (Seasonality)')

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
