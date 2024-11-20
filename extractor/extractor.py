import os
import re

# Automatically detect the file path
current_directory = os.getcwd()
input_file_name = "data.json"
output_file_name = "tokens.txt"

input_file_path = os.path.join(current_directory, input_file_name)
output_file_path = os.path.join(current_directory, output_file_name)

# Regex pattern to find tokens
token_pattern = r"Token:\s([a-zA-Z0-9\.\-_]+)"

try:
    # Check if the input file exists
    if not os.path.exists(input_file_path):
        raise FileNotFoundError(f"{input_file_name} not found in {current_directory}")

    # Read the input file and extract tokens
    tokens = []
    with open(input_file_path, "r") as file:
        content = file.read()
        tokens = re.findall(token_pattern, content)

    # Write the tokens to the output file
    with open(output_file_path, "w") as output_file:
        for token in tokens:
            output_file.write(token + "\n")

    print(f"Extracted {len(tokens)} tokens and saved them to {output_file_path}")
except FileNotFoundError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")