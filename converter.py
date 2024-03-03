import csv
import json

def csv_to_json(csv_file, json_file):
    # Open the CSV file for reading
    with open(csv_file, 'r') as csvfile:
        # Set the delimiter to ","
        reader = csv.DictReader(csvfile, delimiter=',')

        # Initialize a list to store the data
        data = []

        # Iterate over the lines of the CSV file
        for row in reader:
            # Add each line to the data list
            data.append(row)

    # Open the JSON file for writing
    with open(json_file, 'w') as jsonfile:
        # Write data to JSON file
        json.dump(data, jsonfile, indent=4)

# Call the function to convert the CSV file to JSON
csv_to_json('data/osteoporosis.csv', 'data/osteoporosis.json')
