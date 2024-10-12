import pandas as pd

"""
Displays Bike Share statistics related to its users. 

Args:
    df (pandas.Dataframe): The dataframe to retrieve the data from

Returns:
    N/A
"""
def display_user_stats(df):
    types = df["user_type"]
    counts = types.value_counts()
    for key in counts.keys().to_list():
        print(f"> There are {counts[key]:,d} \"{key.lower()}\" Bike Share users")

    genders = df["gender"]
    counts = genders.value_counts()

    for key in counts.keys().to_list():
        # Skip "nan" genders
        if key.lower() == "nan":
            continue
        print(f"> There are {counts[key]:,d} {key.lower()} Bike Share users")
    
    birth_year = df["birth_year"]
    years = birth_year.unique()
    years = years[years != 0]
    minimum = years.min()
    if not minimum <= 0:
        print(f"> The earliest year of birth among users is {minimum}")

    birth_year = df["birth_year"]
    years = birth_year.unique()
    years = years[years != 0]
    most_recent = years.max()
    if not most_recent <= 0:
        print(f"> The most recent year of birth among users is {most_recent}")

    birth_year = df["birth_year"]
    birth_year = birth_year[birth_year != 0]
    counts = birth_year.value_counts()
    most_common = counts.nlargest().index[0]
    if not most_common <= 0:
        print(f"> The most common year of birth among users is {most_common}")    

"""
Displays Bike Share statistics related to trip duration. 

Args:
    df (pandas.Dataframe): The dataframe to retrieve the data from

Returns:
    N/A
"""
def display_trip_duration_stats(df):
    travel_times = df["trip_duration"]
    print(f"> The total travel time is {(travel_times.sum() / 60):,.2f} minutes")

    travel_times = df["trip_duration"]
    print(f"> On average, a trip takes {(travel_times.mean() / 60):,.2f} minutes to complete")

"""
Displays Bike Share statistics related to stations and trips. 

Args:
    df (pandas.Dataframe): The dataframe to retrieve the data from

Returns:
    N/A
"""
def display_popular_stations_and_trips(df):
    start_station = df["start_station"]
    counts = start_station.value_counts()
    station = counts.nlargest().index[0]
    amount = counts.nlargest().iloc[0]
    print(f"> The most common starting station is \"{station}\" with {amount:,d} departures")

    start_station = df["end_station"]
    counts = start_station.value_counts()
    station = counts.nlargest().index[0]
    amount = counts.nlargest().iloc[0]
    print(f"> The most common ending station is \"{station}\" with {amount:,d} arrivals")

    start_end_stations = df["start_station"] + " and " + df["end_station"]
    counts = start_end_stations.value_counts()
    trip = counts.nlargest().index[0]
    amount = counts.nlargest().iloc[0]
    print(f"> The most common trip from start to end is between \"{trip}\" with {amount:,d} travels")

"""
Displays Bike Share statistics related to popular times of travel. 

Args:
    df (pandas.Dataframe): The dataframe to retrieve the data from

Returns:
    N/A
"""
def display_popular_times_of_travel(df):
    counts = df["month"].value_counts()
    month = counts.nlargest().index[0]
    amount = counts.nlargest().iloc[0]
    print(f"> The most common month of travel is {month} with {amount:,d} travels")

    counts = df["weekday"].value_counts()
    day = counts.nlargest().index[0]
    amount = counts.nlargest().iloc[0]
    print(f"> The most common day of travel is {day} with {amount:,d} travels")

    counts = df["hour"].value_counts()
    hour = counts.nlargest().index[0]
    hour = f"{hour - 12}:00 PM" if hour >= 12 else f"{hour}:00 AM"
    amount = counts.nlargest().iloc[0]
    print(f"> The most common hour of travel is {hour} with {amount:,d} travels")

"""
Cleans the given Bike Share dataframe. 

Args:
    df (pandas.Dataframe): The dataframe to clean

Returns:
    pandas.Dataframe: The cleaned dataframe
"""
def clean_data(df):
    # Rename columns for better clarity
    df = df.rename(columns={
        "Unnamed: 0" : "id", 
        "Start Time" : "start_time", 
        "End Time" : "end_time", 
        "Trip Duration" : "trip_duration", 
        "Start Station" : "start_station", 
        "End Station" : "end_station", 
        "User Type" : "user_type", 
        "Gender" : "gender", 
        "Birth Year" : "birth_year"
    })

    # For Washington (which does not have gender and birth_year columns)
    if "gender" not in df:
        df["gender"] = "NaN"
    
    if "birth_year" not in df:
        df["birth_year"] = -1

    # Handle erroneous values in birth_year column
    df["birth_year"] = df["birth_year"].fillna(0)

    # Convert columns into appropriate data types
    df["id"] = df["id"].astype(int)
    df["start_time"] = pd.to_datetime(df['start_time'])
    df["end_time"] = pd.to_datetime(df['end_time'])
    df["trip_duration"] = df["trip_duration"].astype(float)
    df["start_station"] = df["start_station"].astype(str)
    df["end_station"] = df["end_station"].astype(str)
    df["user_type"] = df["user_type"].astype(str)
    df["gender"] = df["gender"].astype(str)
    df["birth_year"] = df["birth_year"].astype(int)

    
    # Create additional columns for easier referencing of year, month, day, weekday, and hour
    df["year"] = df["start_time"].dt.year
    df["month"] = df["start_time"].dt.month_name()
    df["day"] = df["start_time"].dt.day
    df["weekday"] = df["start_time"].dt.day_name()
    df["hour"] = df["start_time"].dt.hour

    return df

"""
Displays Bike Share raw data 5 rows at a time based on the chosen dataset. 

Args:
    df (pandas.Dataframe): The dataframe to retrieve the data from

Returns:
    N/A
"""
def display_raw_data(df):
    display_next_set = True
    for i, row in df.iterrows():
        print(f"--------------<< #{i} >>--------------")
        print(row)
        if (i + 1) % 5 == 0:
            print("\nDo you want to see the next 5? [Y/n]")
            while True:
                try:
                    show_next = input(": ").lower()
                    if show_next == "y":
                        pass
                    elif show_next == "n":
                        display_next_set = False
                    else:
                        raise ValueError
                except ValueError:
                    print("Invalid choice. Try again.")
                else:
                    break

        if not display_next_set:
            break
        if i == len(df) - 1:
            print(f"----------------------------------------------------------------------")
            print("End of raw data.")
    print(f"----------------------------------------------------------------------\n")
                