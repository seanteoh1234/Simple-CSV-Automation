with open('E:/members.csv', 'r') as file:
    # Read all the lines of the file into a list
    lines = file.readlines()

# Filter out the inactive members and write them to the inactive file
with open('E:/inactive.csv', 'a') as inactive_file:
    with open('E:/members.csv', 'w') as members_file:
        for line in lines:
            if 'inactive' in line.lower():
                inactive_file.write(line)
            else:
                members_file.write(line)

import pandas as pd

a = pd.read_csv('E:/members.csv')
empty_status = a.loc[a['Status:'].isnull()]
if len(empty_status) > 1:
    print("There are " + str(len(empty_status['Name:'])) + " names with empty status. Please check")
