import pandas as pd
import matplotlib.pyplot as plt

# Function to read data from CSV
def read_data(filepath):
    """Reads CSV file and returns a DataFrame."""
    return pd.read_csv(filepath)

# Function to calculate total fake cases (FRF + Mistake/Civil)
def calculate_fake_cases(rape_df):
    """Calculates total fake cases for Rape."""
    rape_df['Total_Fake_Cases'] = rape_df['FRF'] + rape_df['Mistake/Civil']
    return rape_df

# Function to calculate total convicted cases
def calculate_convicted_cases(rape_df):
    """Calculates total convicted cases for Rape."""
    rape_df['Total_Convicted'] = rape_df['Convicted']
    return rape_df

# Function to calculate percentage of fake cases out of completed trials
def calculate_fake_percentage(rape_df):
    """Calculates percentage of fake cases out of total completed trials for Rape."""
    rape_df['Fake_Percentage'] = (rape_df['Total_Fake_Cases'] / rape_df['Completed Trials']) * 100
    return rape_df

# Function to calculate percentage of convicted cases out of completed trials
def calculate_convicted_percentage(rape_df):
    """Calculates percentage of convicted cases out of total completed trials for Rape."""
    rape_df['Convicted_Percentage'] = (rape_df['Total_Convicted'] / rape_df['Completed Trials']) * 100
    return rape_df

# Function to calculate fake % out of (fake + convicted cases)
def calculate_fake_out_of_fake_plus_convicted(rape_df):
    """Calculates fake % out of (fake + convicted cases) for Rape."""
    rape_df['Fake_out_of_FakePlusConvicted'] = (rape_df['Total_Fake_Cases'] / 
                                                (rape_df['Total_Fake_Cases'] + rape_df['Total_Convicted'])) * 100
    return rape_df

# Function to calculate promise to marry % out of all reported rape cases
def calculate_promise_to_marry_percentage(rape_df):
    """Calculates percentage of rape cases based on false promise to marry out of all reported rape cases."""
    rape_df['Promise_to_Marry_Percentage'] = (rape_df['Promise to Marry'] / rape_df['Reported']) * 100
    return rape_df

# Function to add source info to all graphs
def add_source():
    """Adds source information to the graph."""
    plt.figtext(0.9, 0.02, "Source: NCRB Reports (Crime in India) 2016-22", horizontalalignment='right')

# Function to annotate values on the plot
def annotate_values(x, y, is_percentage=False):
    """Annotates each point with its corresponding value."""
    for (i, j) in zip(x, y):
        value = f"{j:.2f}%" if is_percentage else str(int(j))
        plt.text(i, j - (0.02 * max(y)), value, fontsize=9, ha='center', weight='bold')

# Function to plot the total reported cases
def plot_reported_cases(rape_df):
    """Plots the trend of total reported rape cases."""
    plt.figure(figsize=(8, 5))
    plt.plot(rape_df['Year'], rape_df['Reported'], label='Total Reported Cases', color='b', marker='o')
    plt.xticks(rape_df['Year'])  # Show all years on x-axis
    plt.title('Trend of Total Reported Rape Cases')
    plt.xlabel('Year')
    plt.ylabel('Number of Cases')
    plt.grid(True)
    plt.legend()
    annotate_values(rape_df['Year'], rape_df['Reported'])  # Annotate values
    add_source()  # Add source information
    plt.subplots_adjust(top=0.9, bottom=0.15)  # Adjust spacing to add more room
    plt.ylim(rape_df['Reported'].min() * 0.9, rape_df['Reported'].max() * 1.1)  # Increase y-axis padding
    plt.show()

# Function to plot pie chart for percentages for the year 2022
def plot_promise_to_marry_pie(rape_df):
    """Plots pie chart for the percentage of promise to marry cases for the year 2022."""
    total_reported_2022 = rape_df.loc[rape_df['Year'] == 2022, 'Reported'].values[0]
    promise_to_marry_percentage_2022 = rape_df.loc[rape_df['Year'] == 2022, 'Promise to Marry'].values[0]
    percentage = (promise_to_marry_percentage_2022 / total_reported_2022) * 100

    plt.figure(figsize=(8, 5))
    plt.pie([percentage, 100 - percentage], 
            labels=['False Promise to Marry', 'Other Rape Cases'], 
            autopct='%1.1f%%', startangle=90, colors=['lightblue', 'lightcoral'])
    plt.title('2022 Percentage of Rape Cases on False Promise to Marry')
    add_source()  # Add source information
    plt.show()

# Function to plot trend of promise-to-marry percentage
def plot_promise_to_marry_trend(rape_df):
    """Plots the trend of rape cases based on false promise to marry as a percentage of all reported rape cases."""
    plt.figure(figsize=(8, 5))
    plt.plot(rape_df['Year'], rape_df['Promise_to_Marry_Percentage'], label='% False Promise to Marry', color='g', marker='o')
    plt.xticks(rape_df['Year'])  # Show all years on x-axis
    plt.title('Trend of Rape Cases on False Promise to Marry % out of All Reported')
    plt.xlabel('Year')
    plt.ylabel('Percentage (%)')
    plt.grid(True)
    plt.legend()
    annotate_values(rape_df['Year'], rape_df['Promise_to_Marry_Percentage'], is_percentage=True)  # Annotate values
    add_source()  # Add source information
    plt.subplots_adjust(top=0.9, bottom=0.15)  # Adjust spacing to add more room
    plt.ylim(rape_df['Promise_to_Marry_Percentage'].min() * 0.9, rape_df['Promise_to_Marry_Percentage'].max() * 1.1)  # Increase y-axis padding
    plt.show()

# Function to plot trends of fake vs convicted cases
def plot_fake_vs_convicted(rape_df):
    """Plots trends of fake vs convicted cases for Rape."""
    plt.figure(figsize=(8, 5))
    plt.plot(rape_df['Year'], rape_df['Total_Fake_Cases'], label='Total Fake Cases', color='r', marker='o')
    plt.plot(rape_df['Year'], rape_df['Total_Convicted'], label='Total Convicted Cases', color='g', marker='o')
    plt.xticks(rape_df['Year'])  # Show all years on x-axis
    plt.title('Trend of Fake vs Convicted Rape Cases')
    plt.xlabel('Year')
    plt.ylabel('Number of Cases')
    plt.grid(True)
    plt.legend()
    annotate_values(rape_df['Year'], rape_df['Total_Fake_Cases'])  # Annotate values for fake cases
    annotate_values(rape_df['Year'], rape_df['Total_Convicted'])  # Annotate values for convicted cases
    add_source()  # Add source information
    plt.subplots_adjust(top=0.9, bottom=0.15)  # Adjust spacing to add more room
    min_val = rape_df[['Total_Fake_Cases', 'Total_Convicted']].min().min() * 0.9
    plt.ylim(min_val, rape_df[['Total_Fake_Cases', 'Total_Convicted']].max().max() * 1.1)  # 10% padding below minimum value
    plt.show()

# Function to plot fake % out of (fake + convicted)
def plot_fake_out_of_fake_plus_convicted(rape_df):
    """Plots the trend of fake % out of (fake + convicted cases) for Rape."""
    plt.figure(figsize=(8, 5))
    plt.plot(rape_df['Year'], rape_df['Fake_out_of_FakePlusConvicted'], label='Fake % of (Fake + Convicted)', color='b', marker='o')
    plt.xticks(rape_df['Year'])  # Show all years on x-axis
    plt.title('Trend of Fake % out of (Fake + Convicted)')
    plt.xlabel('Year')
    plt.ylabel('Percentage (%)')
    plt.grid(True)
    plt.legend()
    annotate_values(rape_df['Year'], rape_df['Fake_out_of_FakePlusConvicted'], is_percentage=True)  # Annotate values
    add_source()  # Add source information
    plt.subplots_adjust(top=0.9, bottom=0.15)  # Adjust spacing to add more room
    min_val = rape_df['Fake_out_of_FakePlusConvicted'].min() * 0.9
    plt.ylim(min_val, rape_df['Fake_out_of_FakePlusConvicted'].max().max() * 1.1)  # 10% padding below minimum value
    plt.show()

# Function to plot fake and convicted percentages
def plot_fake_and_convicted_percentage(rape_df):
    """Plots fake and convicted percentages out of completed trials."""
    plt.figure(figsize=(8, 5))
    plt.plot(rape_df['Year'], rape_df['Fake_Percentage'], label='Fake % of Completed Trials', color='r', marker='o')
    plt.plot(rape_df['Year'], rape_df['Convicted_Percentage'], label='Convicted % of Completed Trials', color='g', marker='o')
    plt.xticks(rape_df['Year'])  # Show all years on x-axis
    plt.title('Trend of Fake % vs Convicted % of Completed Trials')
    plt.xlabel('Year')
    plt.ylabel('Percentage (%)')
    plt.grid(True)
    plt.legend()
    annotate_values(rape_df['Year'], rape_df['Fake_Percentage'], is_percentage=True)  # Annotate values for fake percentage
    annotate_values(rape_df['Year'], rape_df['Convicted_Percentage'], is_percentage=True)  # Annotate values for convicted percentage
    add_source()  # Add source information
    plt.subplots_adjust(top=0.9, bottom=0.15)  # Adjust spacing to add more room
    min_val = rape_df[['Fake_Percentage', 'Convicted_Percentage']].min().min() * 0.9
    plt.ylim(min_val, rape_df[['Fake_Percentage', 'Convicted_Percentage']].max().max() * 1.1)  # 10% padding below minimum value
    plt.show()

# Function to plot pie chart for fake % out of (fake + convicted) for the year 2022
def plot_fake_out_of_fake_plus_convicted_pie(rape_df):
    """Plots pie chart for the percentage of fake cases out of (fake + convicted) for the year 2022."""
    fake_cases_2022 = rape_df.loc[rape_df['Year'] == 2022, 'Total_Fake_Cases'].values[0]
    convicted_cases_2022 = rape_df.loc[rape_df['Year'] == 2022, 'Total_Convicted'].values[0]

    plt.figure(figsize=(8, 5))
    plt.pie([fake_cases_2022, convicted_cases_2022], 
            labels=['Fake Cases', 'Convicted Cases'], 
            autopct='%1.1f%%', startangle=90, colors=['lightgreen', 'lightyellow'])
    plt.title('2022 Percentage of Fake Cases out of (Fake + Convicted)')
    add_source()  # Add source information
    plt.show()

# Main function to execute the plotting
def main():
    # Path to CSV file
    rape_path = 'DataVis-FakeRape/datavis-csv/rape.csv'

    # Read data from CSV file
    rape_df = read_data(rape_path)

    # Calculate various statistics
    rape_df = calculate_fake_cases(rape_df)
    rape_df = calculate_convicted_cases(rape_df)
    rape_df = calculate_fake_percentage(rape_df)
    rape_df = calculate_convicted_percentage(rape_df)
    rape_df = calculate_fake_out_of_fake_plus_convicted(rape_df)
    rape_df = calculate_promise_to_marry_percentage(rape_df)

    # Plotting all trends and charts
    plot_reported_cases(rape_df)
    plot_fake_vs_convicted(rape_df)
    plot_fake_and_convicted_percentage(rape_df)
    plot_fake_out_of_fake_plus_convicted_pie(rape_df)
    plot_fake_out_of_fake_plus_convicted(rape_df)
    plot_promise_to_marry_pie(rape_df)
    plot_promise_to_marry_trend(rape_df)

# Run the main function
main()
