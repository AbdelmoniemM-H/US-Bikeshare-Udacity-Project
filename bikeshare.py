import time
import pandas as pd
import numpy as np

city_data = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}
days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']


def get_filters():
    print('Hello! Let\'s explore some US bike share data!\n'
          '----------------------------------Instructions----------------------------------\n'
          'Enter a city name, then you will be prompted to enter a month name or all and lastly enter a day name or'
          ' type all \n'

          'Data limitation\n'
          '1- Data does include NaN values\n2- if you select Washington city, both gender and birth year are not '
          'available')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:

        city = input('Select city 1- Chicago  2- New York City 3- Washington : ').lower()
        if city in city_data:
            break
        else:
            print('Enter a valid city')

    while True:
        month = input(
            'Select month all, January, February, March, April, May, June :\n').lower()
        if month in months:
            break
        else:
            print('Enter a valid month')

    while True:
        day = input(
            'Select a day all, Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday: ').lower()
        if day in days:
            break
        elif day == 'all':
            print('All week days selected')
            break
        else:
            print("Enter a valid day")

    print('-' * 40)
    return city, month, day


def load_data(city, month, day):
    """"Load CSV files and load city, month, day values and return df"""
    df = pd.read_csv(city_data[city])
    # Data cleaning and manipulation

    # create month column
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month_name()

    # create weekday name column
    df['weekday'] = df['Start Time'].dt.day_name()

    # create hour column in 24hr format
    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':
        df = df[df['month'] == month.title()]

    # create day filter function
    if day != 'all':
        df = df[df['weekday'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print('Most common month is {} '.format(df['month'].mode()[0]))

    # display the most common day of week
    print('Most common day is {} '.format(df['weekday'].mode()[0]))

    # display the most common start hour
    print('Most common hour is {}'.format(df['hour'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    try:
        # display most commonly used start station
        print('Most common starting station : {}'.format(df['Start Station'].mode()[0]), '\n')
        # display most commonly used end station
        print('Most common Ending station : {}'.format(df['End Station'].mode()[0]), '\n')
        # display most frequent combination of start station and end station trip

        combined = df.groupby(['Start Station', 'End Station']).size().nlargest(5)

        print('Most 5 common combination of starting and ending stations \n', '-' * 20, '\n', combined)

    except:
        print('an error occurred')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    total_travel = int(df['Trip Duration'].sum() / 3600)
    # display total travel time
    print('Total travel time is : ', total_travel, ' Hours')

    # display max  trip duration
    print('Max trip duration is : ', int(df['Trip Duration'].max() / 60), 'Minutes')

    # display mean trip time
    print('Mean trip duration is : ', int(df['Trip Duration'].mean() / 60), 'Minutes')

    # display min travel duration
    print('Minimum ride duration is : ', int(df['Trip Duration'].min() / 60), 'Minutes')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bike share users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    user_count_values = df['User Type'].value_counts()
    try:
        gender_count_values = df['Gender'].fillna('Missing').value_counts()
        print('\nTotal gender count is :\n', gender_count_values)

    except:
        print('Gender information are not available in Washington, please try a Chicago or New York City ')

    print('-' * 20)

    try:  # Display earliest, most recent, and most common year of birth
        popular_birthyear = df['Birth Year'].mode()
        print('\nMost common year : ', int(popular_birthyear[0]))
        min_birthyear = df['Birth Year'].min()
        print('Earliest birth year : ', int(min_birthyear))
        max_birthyear = df['Birth Year'].max()
        print('Most recent birth year : ', int(max_birthyear))

    except:  # handle error that will occur when Washington is selected.
        print(print('Birth year information are not available, please try Chicago or New york city'))
    print('-' * 20)

    # Display counts of user types
    print('Count of user types is :\n\n', user_count_values)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def view_data(df):
    n = 0
    while True:
        try:
            view_more = input(' Would you like to view more data? yes - no ').lower()

            if view_more == 'no':
                break
            elif view_more == 'yes':
                n += 5
                print(df.head(n))
            else:
                print('Enter a valid choice')
        except:
            continue


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        print(df.head())
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        view_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
