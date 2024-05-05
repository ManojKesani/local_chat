import pandas as pd
import sys

# Define the path to the text file
text_file_path = "resume_corpus/resume_samples.txt"

# Define the path to save the CSV file
csv_file_path = "resume_corpus/resume_samples.csv"

# Define the columns for the DataFrame
columns = ["Reference ID", "Occupations", "Text Resume"]

# Read the text file and parse its contents
c = 0
with open(text_file_path, "r", encoding="latin-1") as file:
    lines = file.readlines()
    data = []
    for line in lines:
        fields = line.strip().split(":::")
        # print(len(fields))
        if len(fields) != 3:
            print("Error parsing line:")
            

        # data.append(fields)
    c+=1
    if c>5:
        print(c)
        sys.exit()

# Create a DataFrame
df = pd.DataFrame(data, columns=columns)

# Save the DataFrame as a CSV file
df.to_csv(csv_file_path, index=False)

print("CSV file saved successfully.")
