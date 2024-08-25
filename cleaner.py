import os

# Define the directory
directory = 'data/'

# List all files in the directory
for filename in os.listdir(directory):
    # Check if the file ends with .log
    if filename.endswith('.log'):
        # Construct full file path
        file_path = os.path.join(directory, filename)
        # Remove the file
        os.remove(file_path)

print("All .log files have been removed.")
