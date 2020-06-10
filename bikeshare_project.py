# Developed by Tolga Sulubulut
import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
   
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Enter the city name (Chicago, New York City, Washington) that you want to list its data: ").lower()
        if city in ['chicago','new york city','washington']:
            break
        else:
            print("\nPlease just write one of this city names: Chicago, New York City or Washington\n")
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("Enter the specific month name that you want to list its data or enter \'all\' to apply no month filter: ").lower()
        if month in ['january','february','march','april','may','june','all']:
            break
        else:
            print("\nPlease just write name of months or 'all' for not using month filter \n")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Enter the specific day name that you want to list its data or enter 'all' to apply no day filter: ").lower()
        if day in ['sunday','monday','tuesday','wednesday','thursday','friday','saturday','all']:
            break
        else:
            print("\nPlease just write name of days or 'all' for not using day filter \n")

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    print('Most Common Month: ',most_common_month)
    
    # TO DO: display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    print('Most Common Day: ',most_common_day)
    
    # TO DO: display the most common start hour
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
    most_common_hour = df['hour'].mode()[0]
    print('Most Common Hour: ',most_common_hour)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print("Most Common Start Station: ",most_common_start_station)

    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print("Most Common End Station: ",most_common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['comb_of_station'] = df['Start Station'] + ' & ' + df['End Station']
    most_common_comb_of_station = df['comb_of_station'].mode()[0]
    print("Most Common Combination of Station: ",most_common_comb_of_station)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    Total_trip_duration = df['Trip Duration'].sum()
    seconds = Total_trip_duration
    hours = seconds // (60*60)
    seconds %= (60*60)
    minutes = seconds // 60
    seconds %= 60
    print('Total Travel Time: %s hours %s minutes %s seconds' % (hours, minutes, seconds) )

    # TO DO: display mean travel time
    Mean_trip_duration = df['Trip Duration'].mean()
    seconds = Mean_trip_duration
    hours = seconds // (60*60)
    seconds %= (60*60)
    minutes = seconds // 60
    seconds %= 60
    print('Mean Travel Time: %s hours %s minutes %s seconds' % (hours, minutes, seconds) )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Counts of User Types:\n')
    print(user_types)

    if city != 'washington':
    # TO DO: Display counts of gender
        gender = df['Gender'].value_counts()
        print('\nCounts of Gender:\n')
        print(gender)

    # TO DO: Display earliest, most recent, and most common year of birth
        earliest_year_of_birth = int(df['Birth Year'].min())
        most_recent_year_of_birth = int(df['Birth Year'].max())
        most_common_year_of_birth = int(df['Birth Year'].mode()[0])
        print("\nEarliest Year of Birth: ",earliest_year_of_birth)
        print("Most Recent Year of Birth: ",most_recent_year_of_birth)
        print("Most Common Year of Birth: ",most_common_year_of_birth)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df,city):
    """Displays raw data abput bikeshare."""
    index_df = 0
    if city != 'washington':
        end_column = 9
    else: end_column = 7
    
    # If user want to see raw data,it will show to 5 lines of raw data and again ask the user same question.
    while True:

        raw_data_request = input("Do you want to see raw data ? (Yes or No): ").lower()
        if raw_data_request == 'yes' :
            print(df.iloc[ index_df : index_df+5 , 1 : end_column ])
            index_df += 5
            continue
        elif raw_data_request == 'no' :
            break
        else :
            print("\nPlease just write 'Yes' or 'No'.\n")
            
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        display_data(df,city)
        restart = input('\nWould you like to restart? Enter Yes or No.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
