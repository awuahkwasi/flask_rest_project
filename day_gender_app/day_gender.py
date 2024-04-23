def get_day_of_week_from_input():
    name = input("Enter the name: ").lower()
    if not name:
        print("Please enter a name.")
        return

    day_of_week, gender = get_day_of_week(name)
    if day_of_week == "Unknown" or gender == "Unknown":
        print("The name provided is not a day-name in Ghana")
    else:
        print(f"Day: {day_of_week}")
        print(f"Gender: {gender}")

def get_day_of_week(name):
    name_lower = name.lower()
    if name_lower in ['kwasi', 'akwasi', 'kwesi', 'akwesi']:
        return "Sunday", "Male"
    elif name_lower in ['akosua', 'akos']:
        return "Sunday", "Female"
    elif name_lower in ['kwadwo', 'kojo']:
        return "Monday", "Male"
    elif name_lower in ['adwoa', 'adjoa']:
        return "Monday", "Female"
    elif name_lower in ['kwabena', 'kobby', 'cobbie', 'kobbie', 'kobbina', 'cobbinah', 'cobbina']:
        return "Tuesday", "Male"
    elif name_lower == 'abena':
        return "Tuesday", "Female"
    elif name_lower in ['kwaku', 'kweku']:
        return "Wednesday", "Male"
    elif name_lower in ['akua', 'kuukua']:
        return "Wednesday", "Female"
    elif name_lower in ['yaw', 'kwaw', 'kwao']:
        return "Thursday", "Male"
    elif name_lower == 'yaa':
        return "Thursday", "Female"
    elif name_lower in ['kofi', 'fiifi']:
        return "Friday", "Male"
    elif name_lower in ['afia', 'afua', 'maafia', 'maafua', 'afi']:
        return "Friday", "Female"
    elif name_lower == 'kwame':
        return "Saturday", "Male"
    elif name_lower == 'ama':
        return "Saturday", "Female"
    else:
        return "Unknown", "Unknown"

# Check if the file is being run directly
if __name__ == "__main__":
    get_day_of_week_from_input()
