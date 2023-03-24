with open('insert all members csv here', 'r') as file:
    # Read all the lines of the file into a list
    lines = file.readlines()

# Filter out the inactive members and write them to the inactive file
with open('insert inactive members csv here', 'a') as inactive_file:
    with open('insert all members csv here, 'w') as members_file:
        for line in lines:
            if 'inactive' in line.lower():
                inactive_file.write(line)
            else:
                members_file.write(line)

import pandas as pd

a = pd.read_csv('insert all members csv here')
empty_status = a.loc[a['Status:'].isnull()]
if len(empty_status) > 1:
    print("There are " + str(len(empty_status['Name:'])) + " names with empty status. Please check")
