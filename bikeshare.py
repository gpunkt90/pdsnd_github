import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
# Building lists for months and days to access them easily.
MONTH_DATA = ['all','january','february','march','april','may','june']
DAY_DATA = ['all','monday','tuesday','wednesday','friday','saturday','sunday']

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
    # 3 quite similar while loops including error handling
    while True:
        try:
            city = str(input("Please enter the name of the city you are interested in (Chicago, New York City or Washington): ").lower())
            if city not in CITY_DATA:
                print("Sorry, there is no data for the place you ask for.")
                continue
        except Error:
            print("Please only enter letters.")
            continue
        else: break              
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        try:
            month = str(input("Please enter the month you are interested in (January to June or all): ").lower())
            if month not in MONTH_DATA:
                print("Sorry, there is no data for the month you ask for.")
                continue
        except Error:
            print("Please only use valid inputs.")
            continue
        else: break
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day = str(input("Please enter the day you are interested in (Monday to Sunday or all): ").lower())
            if day not in DAY_DATA:
                print("Sorry, there is no data for the day you ask for.")
                continue
        except Error:
            print("Please only use valid inputs.")
            continue
        else: break
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
    # Making sure that the Start Time has the right format
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # Extracting month and day of the week to be compared to the inputs.
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour
    # Filters for filtering by month and day as long as "all" was not entered. Adding them to the DataFrame.
    if month != 'all':
        month = MONTH_DATA.index(month)
        df = df.loc[df['month'] == month]
    if day != 'all':
        df = df.loc[df['day_of_week'] == day.title()]
    return df
    
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # TO DO: display the most common month
    # Just a lot of repetitve looking for most common values in the respective columns.
    popular_month = df['month'].mode()[0]
    print("The most common month is: "+str(popular_month))
    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print("The most common day is: "+str(popular_day))
    # TO DO: display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print("The most common hour is: "+str(popular_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    # TO DO: display most commonly used start station
    popular_start = df['Start Station'].mode()[0]
    print("The most commonly used Start Station is: \n"+str(popular_start))
    # TO DO: display most commonly used end station
    popular_end = df['End Station'].mode()[0]
    print("The most commonly used End Station is: \n"+str(popular_end))
    # TO DO: display most frequent combination of start station and end station trip
    # The same as seen above just with a concatenation to build a proper output string.
    popular_combination = (df['Start Station'] + " ---> " + df['End Station']).mode()[0]
    print("The most commonly used combination of Start and End Station is: \n"+str(popular_combination))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    # TO DO: display total travel time
    # sum() instead of mode() to sum it up.
    total_time = df['Trip Duration'].sum()/3600
    total_time = "{:.2f}".format(total_time)
    print("The total duration of all selected trips is [h]: \n"+str(total_time))
    # TO DO: display mean travel time
    # mean() for calculating the average value.
    mean_time = df['Trip Duration'].mean()/60
    mean_time = "{:.2f}".format(mean_time)
    print("The average duration of all selected trips is [min]: \n"+str(mean_time))
    # mode() to find the most common rental duration.
    popular_duration = df['Trip Duration'].mode()[0]/60
    popular_duration = "{:.2f}".format(popular_duration)
    print("The most common rental duration of all selected trips is [min]: \n"+str(popular_duration))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df, city):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    # TO DO: Display counts of user types
    count_user_types = df['User Type'].value_counts()
    print("The count of user types is: \n"+str(count_user_types))

    # There is no gender or birth year data from Washington, so this has to be handled
    if city == "chicago" or city == "new york city":
    # TO DO: Display counts of gender
    # Value_counts() to count all the gender, as well as min() and max() to find the first and last birth year, mode() to find the most common one
        count_gender = df['Gender'].value_counts()
        print("The count of genders is: \n"+str(count_gender))
        # TO DO: Display earliest, most recent, and most common year of birth
        early_birth = int(df['Birth Year'].min())
        print("The earliest year of birth is: \n"+str(early_birth))
        late_birth = int(df['Birth Year'].max())
        print("The most recent year of birth is: \n"+str(late_birth))
        popular_birth = int(df['Birth Year'].mode()[0])
        print("The most common year of birth is: \n"+str(popular_birth))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def show_raw_data(df):
    # Displays 5 lines of raw data when user inputs anything and does not if user inputs no 
    # Args:
    #   (DataFrame) df - DataFrame from above (city data filtered by month and day)
    print(df.head())
    next = 0
    # While loop to show 5 additional lines of raw data.
    while True:
        raw_data = input("Would you like to see the next five rows of raw data? Type yes or no.\n")
        if raw_data.lower() != 'yes':
            return
        # Iteration to show the 5 next lines.
        next = next + 5
        print(df.iloc[next:next+5])
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        # While loop to show the first five rows of raw data.
        while True:
            raw_data = input("Would you like to see the first five rows of raw data? Type yes or no.\n")
            if raw_data.lower() != 'yes':
                break
            show_raw_data(df)
            break

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
        
if __name__ == "__main__":
	main()