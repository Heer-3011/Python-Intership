# Resolution Streak
# Given an array of arrays, where each sub-array represents a day of your resolution activities and contains three integers: the number of steps walked that day, the minutes of screen time that day, and the number of pages read that day; determine if you are keeping your resolutions.

# The first sub-array is day 1, and second day 2, and so on.
# A day is considered successful if all three of the following goals are met:

# You walked at least 10,000 steps.
# You had no more than 120 minutes of screen time.
# You read at least five pages.
# If all of the given days are successful, return "Resolution on track: N day streak." Where N is the number of successful days.

# If one or more days is not a success, return "Resolution failed on day X: N day streak.". Where X is the day number of the first unsuccessful day, and N is the number of successful days before the first unsuccessful day.

# Run the Tests (Ctrl + Enter)
# Reset this lesson
# Get Help
# Tests
# Waiting:1. resolution_streak([[10500, 75, 15], [11000, 90, 10], [10650, 100, 9]]) should return "Resolution on track: 3 day streak."
# Waiting:2. resolution_streak([[10000, 120, 5], [10950, 121, 11]]) should return "Resolution failed on day 2: 1 day streak."
# Waiting:3. resolution_streak([[15000, 110, 8], [12300, 60, 13], [10100, 120, 4], [9000, 125, 4]]) should return "Resolution failed on day 3: 2 day streak."
def resolution(list1):
    # print(list1)
    # print(len(list1))

    for i in list1:
        if i[0]>=10000 and i[1]<120 and i[2]>=5:
            print(f"Resolution on track: {len(list1)} day streak.")
        else:
            print(f"Resolution failed on day {i}: {list1.index(i)} day streak")
            break
resolution([[15000, 110, 8], [12300, 60, 13], [10100, 120, 4], [9000, 125, 4]])