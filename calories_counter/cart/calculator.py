def calculator(gender, weight, height, age, physical_activity_choice):
    physical_activity = 0
    result = 0
    if physical_activity_choice == '2':
        physical_activity = 1.2
    elif physical_activity_choice == '3':
        physical_activity = 1.375
    elif physical_activity_choice == '4':
        physical_activity = 1.55
    elif physical_activity_choice == '5':
        physical_activity = 1.725
    elif physical_activity_choice == '6' or physical_activity_choice == '7':
        physical_activity = 1.9

    if gender == '1':  # Male
        result = (10 * weight + 6.25 * height - 5 * age + 5) * physical_activity
    elif gender == '2':  # Female
        result = (10 * weight + 6.25 * height - 5 * age - 161) * physical_activity
    return result
