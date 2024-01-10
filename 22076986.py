# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 22:52:27 2024

@author: Harikrishnan Marimuthu
"""
# Importing packages:
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# File name of the CSV file:
file_name = "auction.csv"

# Read the data from the CSV file into a DataFrame:
data = pd.read_csv(file_name)

# Data preprocessing:
data['Country'] = data['Country'].str.strip()
data['Winning bid'] = pd.to_numeric(data['Winning bid'], errors='coerce')
data['Winning bid'].fillna(data['Base price'], inplace=True)

# Set the background color and customize the plotting style:
background_color = 'lightcyan'
sns.set_style("whitegrid")
plt.rcParams.update({
    'font.size': 18,
    'axes.titleweight': 'bold',
    'font.family': 'Arial',
    'axes.labelweight': 'bold',
    'figure.facecolor': background_color,
    'axes.facecolor': background_color,
    'savefig.facecolor': background_color,
})

# Define functions for creating various plots:


def plot_avg_bid_by_year(data):
    """
    Create a bar plot showing the average winning bid by year.

    Args:
        data (DataFrame): The DataFrame containing auction data.
    """
    avg_bid_by_year = data.groupby('Year')['Winning bid'].mean()

    plt.bar(avg_bid_by_year.index, avg_bid_by_year.values,
            color='indianred', label='Average Winning Bid')

    for i, value in enumerate(avg_bid_by_year.values):
        plt.text(avg_bid_by_year.index[i], value + 0.5,
                 f'{value:.2f}', ha='center', va='bottom', fontsize=12)

    plt.title('Average Winning Bid by Year', fontsize=18, pad=8)
    plt.xlabel('Year', fontsize=14, labelpad=10)
    plt.ylabel('Average Winning Bid', fontsize=14, labelpad=20)
    plt.xticks(rotation=0, fontsize=12)
    plt.yticks(fontsize=12)
    plt.legend(fontsize=14)


def plot_players_by_country(data):
    """
    Create a bar plot showing the count of players bought by country.

    Args:
        data (DataFrame): The DataFrame containing auction data.
    """
    players_by_country = data['Country'].value_counts().head(10)
    percentage_labels = [(count / len(data)) *
                         100 for count in players_by_country.values]

    sns.barplot(x=percentage_labels,
                y=players_by_country.index, palette="RdYlBu")

    for i, value in enumerate(players_by_country.values):
        plt.text(percentage_labels[i] + 0.5, i,
                 f'{percentage_labels[i]:.1f}%', ha='left', va='center',
                 fontsize=12)

    plt.title('Count of Players Bought by Country', fontsize=18, pad=8)
    plt.xlabel('Percentage of Players', fontsize=14, labelpad=10)
    plt.ylabel('Country', fontsize=14)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)


def plot_base_price_trend(data):
    """
    Create a line plot showing the trend of base price over years.

    Args:
        data (DataFrame): The DataFrame containing auction data.
    """
    base_price_trend = data.groupby('Year')['Base price'].mean()
    sns.lineplot(x=base_price_trend.index, y=base_price_trend.values,
                 marker='o', linestyle='-', color='brown',
                 label='Average Base Price', linewidth=2.5)
    plt.title('Trend of Base Price Over Years', fontsize=18, pad=5)
    plt.xlabel('Year', fontsize=14, labelpad=20)
    plt.ylabel('Average Base Price', fontsize=14, labelpad=20)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.legend(fontsize=14)


def plot_top_teams(data):
    """
    Create a pie chart showing the distribution of players among the top 5 teams.

    Args:
        data (DataFrame): The DataFrame containing auction data.
    """
    top_teams = data['Team'].value_counts().head(5)
    colors = sns.color_palette("RdYlBu")
    explode_values = [0.15, 0.05, 0.05, 0.05, 0.05]
    hole_size = 0.7
    wedges, texts, autotexts = plt.pie(top_teams, autopct='%1.2f%%',
                                       startangle=90, colors=colors,
                                       explode=explode_values,
                                       wedgeprops=dict(width=hole_size))
    for autotext in autotexts:
        autotext.set_fontsize(12)
        autotext.set_weight('bold')
    plt.title('Distribution of Players among Top 5 Teams', fontsize=18, pad=5)
    plt.ylabel('')
    legend = plt.legend(wedges, top_teams.index, title='Teams',
                        loc='center left', bbox_to_anchor=(1, 0, 0.5, 1),
                        fontsize=12)
    legend.get_title().set_fontsize(14)
    legend.get_title().set_fontweight('bold')
    plt.text(0, 0, "Top 5 Teams", ha='center',
             va='center', fontsize=10, weight='bold')


# Creating a figure with subplots:
plt.figure(figsize=(40, 30))

# Subplot 1: Average Winning Bid by Year
ax1 = plt.subplot(2, 2, 1)
plot_avg_bid_by_year(data)
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)

# Subplot 2: Count of Players Bought by Country
ax2 = plt.subplot(2, 2, 2)
plot_players_by_country(data)
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)

# Subplot 3: Trend of Base Price Over Years
ax3 = plt.subplot(2, 2, 3)
plot_base_price_trend(data)
ax3.spines['top'].set_visible(False)
ax3.spines['right'].set_visible(False)

# Subplot 4: Distribution of Players among Top 5 Teams
ax4 = plt.subplot(2, 2, 4)
plot_top_teams(data)
ax4.spines['top'].set_visible(False)
ax4.spines['right'].set_visible(False)

# Setting a title for the entire figure:
plt.suptitle('IPL Auction Analysis 2013-2023', fontsize=30, weight='bold')

# Defining visual styling for highlighted text in the plot:
highlighted_text_params = {
    'facecolor': 'skyblue',
    'alpha': 0.7,
    'edgecolor': 'black',
    'boxstyle': 'round,pad=1'
}

# Defining text for the plot description:
description = """
This visual analysis provides a comprehensive overview of key trends and patterns in the IPL auctions over a decade, focusing on the dynamics of player valuations, country representation, and team compositions.

    ** Average Winning Bid by Year: **
    - Tracks the year-wise shifts in the average winning bids, unveiling the changing economic landscape and investment patterns in the IPL.

    ** Count of Players Bought by Country: **
    - Showcases the top countries in terms of player representation, highlighting the global diversity and talent pool in the IPL.

    ** Trend of Base Price Over Years: **
    - Reveals the progression in average base prices, shedding light on the evolving market valuation of players across years.

    ** Distribution of Players among Top 5 Teams: **
    - Illustrates the distribution of players in the top five teams, offering a perspective on team strategies and dominance.
"""

plt.figtext(0.09, -0.15, description, ha='left', va='center',
            fontsize=16, wrap=True, weight='bold')
plt.figtext(0.75, 0.92, "Name: Harikrishnan Marimuthu\nStudent ID: 22076986",
            ha='left', va='center',
            fontsize=16, weight='bold', bbox=highlighted_text_params)

# Adjusting layout and displaying the plot:
plt.tight_layout(pad=4.0)
plt.subplots_adjust(top=0.82, bottom=0.1, left=0.1,
                    right=0.9, hspace=0.35, wspace=0.35)
#plt.savefig("22076986.png", dpi=300, bbox_inches='tight')

plt.show()
