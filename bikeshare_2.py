import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'newyork': 'new_york_city.csv',
              'washington': 'washington.csv' }
MONTH = {}
MONTH = {'january':1, 'february':2, 'march':3, 'april':4,
            'may':5, 'june':6, 'july':7, 'august':8,
            'september':9, 'october':10, 'november':11,
            'december':12, 'all':'all'}
WEEKDAY = {'monday':0, 'tuesday':1, 'wednesday':2, 'thursday':3, 'friday':4, 'saturday':5, 'sunday':6, 'all':'all'}

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

# get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    flag = 'True'
    while flag == 'True':
        print("Please enter a city from the below choices")
        try:
            city = input("(Chicago, Washington, NewYork) :  ").lower()
            if city in CITY_DATA:
                flag = "False"
        except:
            print("Exception raised, enter a valid entry")
    flag = 'True'
    while flag == 'True':
        try:
            month = input("Please enter a month :  ").lower()
            if month in MONTH:
                # month = MONTH.index(month)+1
                month = MONTH[month]
                flag = "False"
        except:
            print("Exception raised, enter a valid entry")
    # get user input for day of week (all, monday, tuesday, ... sunday)
    flag = 'True'
    while flag == 'True':
        try:
            day = input("Please enter the day of the week :  ").lower()
            if day in WEEKDAY:
                # day = WEEKDAY.index(day)+1
                day = WEEKDAY[day]
                flag = "False"
        except:
            print("Exception raised, enter a valid entry")
    flag = "True"
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
    df = pd.read_csv(CITY_DATA[city])
    df_raw = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['weekday'] = df['Start Time'].dt.weekday
    df['Start_End_Stations'] ='FROM  ('+df['Start Station']+')  TO  ('+df['End Station']+')'

    if month!='all':
        df1 = (df['month'] == month)
        df = df[df1]
        del df1
    if day!='all':
        df1=(df['weekday'] == day)
        df = df[df1]
        del df1
    # print(df.head())
    return df, df_raw


def time_stats(df,month,day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    month_tmp = df['month'].mode()[0]
    print(month_tmp)
    month_words = [k for k, v in MONTH.items() if v == month_tmp][0]
    print("The Most common month of travel is :  {}".format(month_words.title()))

    # display the most common day of weekday
    day_tmp = df['weekday'].mode()[0]
    day_words = [k for k, v in WEEKDAY.items() if v == day_tmp][0]
    print("The Most common weekday of travel is :  {}".format(day_words.title()))

    # display the most common start hour
    print("The Most common hour of travel is at :  {}:00".format(df['Start Time'].dt.hour.mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print("The Most common used Starting station is :  {}".format(df['Start Station'].mode()[0]))

    # display most commonly used end station
    print("The Most common used Ending station is :  {}".format(df['End Station'].mode()[0]))

    # display most frequent combination of start station and end station trip
    print("The most frequent start-end station combination is : {}".format(df['Start_End_Stations'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print("Total travel time :  {} seconds".format(df['Trip Duration'].sum()))

    # display mean travel time
    print("Mean travel time :  {} seconds".format(round(df['Trip Duration'].mean(),2)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print("Total counts of user types : {}".format(df['User Type'].value_counts()))

    # Display counts of gender
    if city != 'washington':
        print("Total counts of gender : {}".format(df['Gender'].value_counts()))
    # Display earliest, most recent, and most common year of birth
        print("Earliest year of birth : {}".format(int(df['Birth Year'].min())))
        print("Recent year of birth : {}".format(int(df['Birth Year'].max())))
        print("Most common year of birth : {}".format(int(df['Birth Year'].mode()[0])))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        statistics_d = statistics_s = statistics_t = statistics_u = ''

        df,df_raw = load_data(city, month, day)
        # print(df.head())
        raw_input = input("Would you like to see raw sample data?(Y/N) :")
        start=0
        end=5
        print(start)
        print(end)
        show_more = 'y'
        if raw_input.lower() == 'y':
            while show_more.lower() == 'y':
                print(df_raw.iloc[start:end])
                start+=5
                end+=5
                show_more = input("Would you like to more sample data?(Y/N) :")


        statistics_t = input("Do you want to see the time related stats?(Y/N) :").lower()
        if statistics_t == 'y':
            time_stats(df,month,day)
        statistics_s = input("Do you want to see the station related stats?(Y/N) :").lower()
        if statistics_s == 'y':
            station_stats(df)
        statistics_d = input("Do you want to see the trip duration related stats?(Y/N) :").lower()
        if statistics_d == 'y':
            trip_duration_stats(df)
        statistics_u = input("Do you want to see the user related stats?(Y/N) :").lower()
        if statistics_u == 'y':
            user_stats(df,city)

        restart = input('\nWould you like to restart? Enter Y or N.\n')
        if restart.lower() != 'y':
            break
# NOTE:

if __name__ == "__main__":
	main()
