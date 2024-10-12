import pandas as pd
from library import *

def main():
    STATES = ["Chicago", "New York City", "Washington"]
    FILTERS = ["Month", "Day", "Both", "No"]
    MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    FILTER_MONTH = 0
    FILTER_DAY = 1
    FILTER_BOTH = 2
    FILTER_NONE = 3

    restart_program = True
    state_choice = -1
    filter_choice = -1
    month_choice = None
    day_choice = None
    df = None

    while restart_program:
        print("    ____  _ __           _____ __                       _____ __        __       __")
        print("   / __ )(_) /_____     / ___// /_  ____ _________     / ___// /_____ _/ /______/ /")
        print("  / __  / / //_/ _ \\    \\__ \\/ __ \\/ __ `/ ___/ _ \\    \\__ \\/ __/ __ `/ __/ ___/ / ")
        print(" / /_/ / / ,< /  __/   ___/ / / / / /_/ / /  /  __/   ___/ / /_/ /_/ / /_(__  )_/  ")
        print("/_____/_/_/|_|\\___/   /____/_/ /_/\\__,_/_/   \\___/   /____/\\__/\\__,_/\\__/____(_)   ")
        print()
        
        print("Which state do you want to check out?")
        for i, state in enumerate(STATES):
            print(f"[{i}] - {state}")

        while True:
            try:
                # Ask for state input
                state_choice = int(input(": "))
                if state_choice >= 0 and state_choice < len(STATES):
                    print(f"You selected {STATES[state_choice]}.\n")

                    # Generate file name (i.e., "./data/new_york_city.csv")
                    file_name = "./data/" + "_".join(STATES[state_choice].split(" ")) + ".csv"
                    # Load dataframe
                    df = pd.read_csv(file_name)
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Invalid choice. Try again.")

        print("Do you want to filter by month, day, both, or not at all?")
        for i, filter in enumerate(FILTERS):
            print(f"[{i}] - {filter}")

        while True:
            try:
                # Ask for filter options
                filter_choice = int(input(": "))
                if filter_choice >= 0 and filter_choice < len(FILTERS):
                    print(f"You selected {FILTERS[filter_choice]}.\n")
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Invalid choice. Try again.")

        if filter_choice == FILTER_MONTH or filter_choice == FILTER_BOTH:
            print("Which month would you like to filter in? (i.e., January)")
            while True:
                try:
                    # If filtering by month, prompt for a month
                    month_choice = input(": ")
                    if month_choice in MONTHS:
                        print(f"You selected {month_choice}.\n")
                        break
                    else:
                        raise ValueError
                except ValueError:
                    print("Invalid choice. Try again")

        if filter_choice == FILTER_DAY or filter_choice == FILTER_BOTH:
            print("Which day of the week? (i.e., Wednesday)")
            while True:
                try:
                    # If filtering by day, prompt for a week day
                    day_choice = input(": ")
                    if day_choice in DAYS:
                        print(f"You selected {day_choice}.\n")
                        break
                    else:
                        raise ValueError
                except ValueError:
                    print("Invalid choice. Try again")

        print("Do you want to view the raw data? [Y/n]")
        while True:
            try:
                # Ask if the user wants to view the raw data
                raw_data = input(": ").lower()
                if raw_data == "y":
                    # Display the raw data
                    display_raw_data(df)
                    break
                elif raw_data == "n":
                    print("Raw data will not be shown.\n")
                    break
                else:
                    raise ValueError
            except ValueError:
                    print("Invalid choice. Try again")

        # Clean the dataframe
        df = clean_data(df)

        # Display non-filtered statistics
        print(f"<< Bike Share Statistics >>")
        print("For the non-filterable data...")
        display_popular_times_of_travel(df)

        # Display filtered statistics (if applicable)
        filtered_df = df
        if month_choice is not None:
            filtered_df = filtered_df[filtered_df["month"] == month_choice]

        if day_choice is not None:
            filtered_df = filtered_df[filtered_df["weekday"] == day_choice]

        print()
        print(f"<< Filter/s -> State: {STATES[state_choice]}, Month: {month_choice}, Day: {day_choice} >>")
        print("For the filtered data...")

        # If the resulting filtered dataframe is empty
        if len(filtered_df) == 0:
            print("No data was found given the filters provided... Please try again :-(\n")
        else:
            display_popular_stations_and_trips(filtered_df)
            display_trip_duration_stats(filtered_df)
            display_user_stats(filtered_df)
            print()

        print("Do you want to try again? [Y/N] ")
        while True:
            try:
                # Ask user if they would like to restart the program
                restart_program = input(": ").lower()
                if (restart_program == "y"):
                    print()
                    break
                elif restart_program == "n":
                    restart_program = False
                    break
                else:
                    raise ValueError
            except ValueError:
                    print("Invalid choice. Try again")

if __name__ == "__main__":
    main()