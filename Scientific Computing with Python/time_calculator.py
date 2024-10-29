def add_time(start, duration, day = ""):
    """#+
    Calculate the new time after adding a duration to a start time, optionally considering the day of the week.#+

    Parameters:#+
    start (str): The start time in the format 'HH:MM AM/PM'.#+
    duration (str): The duration to add in the format 'HH:MM'.#+
    day (str, optional): The starting day of the week. Defaults to an empty string.#+
#+
    Returns:#+
    str: The new time in the format 'HH:MM AM/PM', optionally followed by the day of the week and/or the number of days later.#+
    """#+
    # Set a list with all days of the week
    days_of_week = ("monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday" )

    # The approach will be to compute the start hour and the duration to minutes

    # Turn the input into a list with three items: hour, minutes and AM/PM
    start_list = start.replace(":"," ").split()
    # Sum the hours and the minutes
    start_in_minutes= int(start_list[0])*60 + int(start_list[1]) 
    # Add 12 hours if it's PM
    if start_list[2] == "PM":
        start_in_minutes += 12*60

    # Now do the same with duration
    duration_list = duration.split(':')
    duration_in_minutes = int(duration_list[0])*60 + int(duration_list[1])

    #Now we can add both durations
    total_time_minutes = start_in_minutes + duration_in_minutes

    # We obtain a number that we can split into days, hours and minutes using // and %
    days = total_time_minutes // (24*60)
    days_modulus = total_time_minutes % (24*60)
    hours = days_modulus // 60
    minutes = days_modulus % 60

    # Now that we have the amount of days , hours and minutes transcurred, we can start printing

    #For days
    days_string = ""
    if days > 1:
        days_string = f"({days} days later)"
    elif days == 1:
        days_string = f"(next day)"


    #For hours and minutes
    time_string = ""
    if hours > 12:
        time_string = f"{hours-12}:{minutes:02d} PM"
    elif hours == 12:
        time_string = f"{hours}:{minutes :02d} PM"
    elif hours == 0:
        time_string = f"12:{minutes :02d} AM"
    else:
        time_string = f"{hours}:{minutes :02d} AM"

    #For week days
    next_week_day_string = ""
    if day:
        week_day_index = days_of_week.index(day.lower())
        next_week_day_index = (week_day_index + days) % 7
        next_week_day_string = f", {days_of_week[next_week_day_index].capitalize()}"

    # Different return for different cases
    if days < 1 and not day:
        return f"{time_string}"
    elif days >= 1 and not day:
        return f"{time_string} {days_string}"
    elif days < 1 and day:
        return f"{time_string}{next_week_day_string}"
    elif days >= 1 and day:
        return f"{time_string}{next_week_day_string} {days_string}"

print(add_time('3:30 PM', '2:12', 'Monday'))
