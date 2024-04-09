# Function to extract the hour from a time string
def get_hour(time_str):
    hour = time_str.split(':')[0]
    return hour

# Open the file and read its contents
file = open('mbox.txt', 'r')
lines = file.readlines()

# Create a dictionary to store the counts of each hour
hour_counts = {}

# Iterate through the lines in the file
for line in lines:
    # Find the 'From ' line
    if line.startswith('From '):
        # Extract the time portion from the 'From ' line
        time_str = line.split()[5]
        # Extract the hour from the time string
        hour = get_hour(time_str)
        # Increment the count of the extracted hour in the dictionary
        hour_counts[hour] = hour_counts.get(hour, 0) + 1

# Sort the dictionary by its keys (the hours)
sorted_hours = sorted(hour_counts.items())

# Print the keys and values of the sorted dictionary
for hour, count in sorted_hours:
    print(hour, count)