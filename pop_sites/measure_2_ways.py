import csv
import random
import time

def binary_search_col1(data, target):
    left, right = 0, len(data) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if data[mid][1] == target:
            return mid  # Found the target
        elif data[mid][1] < target:
            left = mid + 1
        else:
            right = mid - 1    
    return -1  # Target not found


# Create an empty list to store the CSV data
csv_data = []

# Specify the CSV file name
csv_file = 'top-1m-TLD.csv'

# Open the CSV file and read its contents
with open(csv_file, 'r', newline='') as file:
    csv_reader = csv.reader(file)
    rows = 0
    # Iterate through each row in the CSV file and append it to the list
    for row in csv_reader:
        rows = rows + 1
        csv_data.append(row)

#Get 10% of the second column into a list
mylist = []
for i in range(int(rows/10)):
    randelem = random.randint(0,rows)
    pickthis = csv_data[randelem][1]
    mylist.append(pickthis)


#Way 1: brute force: read linearly
start_time = time.time()
found = 0
for elem in mylist:
    for row in csv_data:
        if elem == row[1]:
            found = found + 1
            break
print(found)
end_time = time.time()
execution_time_ms = (end_time - start_time) * 1000
print(f"#1 execution time: {execution_time_ms:.2f} milliseconds")   

#Way 2: Sort the csv data and use binsearch
sorted_csv_data = sorted(csv_data, key=lambda x: x[1])
start_time = time.time()
found  = 0
for elem in mylist:
    index = binary_search_col1(sorted_csv_data, elem)
    if index:
        found = found + 1
print(found)
end_time = time.time()
execution_time_ms = (end_time - start_time) * 1000
print(f"#2 execution time: {execution_time_ms:.2f} milliseconds")
