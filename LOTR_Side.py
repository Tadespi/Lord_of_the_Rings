# Import Dependancies
import pandas as pd

# Import path and CSV files
folder_path = "../Lord_of_the_Rings/Resources/"

# Name the files
characters_file = "lotr_characters.csv"
scripts_file = "lotr_scripts.csv"
characters_df = pd.read_csv(folder_path + characters_file)
scripts_df = pd.read_csv(folder_path + scripts_file)

print("First 10 rows of Characters DataFrame:")
print(characters_df.head(10))

print("\nFirst 10 rows of Scripts DataFrame:")
print(scripts_df.head(10))

# Count the number of times each character is shown
character_count = scripts_df['char'].value_counts()

# Create a DataFrame from the character_count Series
character_count_df = pd.DataFrame(character_count)

# Rename the column to 'Count'
character_count_df.columns = ['Count']

# Display the table
print("Table of Character Counts:")
print(character_count_df)

# Find the character who spoke the most lines
most_lines_character = character_count.idxmax()
most_lines_count = character_count.max()

# Find the character who spoke the least lines
least_lines_character = character_count.idxmin()
least_lines_count = character_count.min()

# Display the result
print(f"\nThe character who spoke the most lines is '{most_lines_character}' with {most_lines_count} lines.")
print(f"The character who spoke the least lines is '{least_lines_character}' with {least_lines_count} lines.")

dialogue_by_movie = scripts_df.groupby('movie').size()

# Find the movie with the most dialogue spoken
most_dialogue_movie = dialogue_by_movie.idxmax()
total_dialogue = dialogue_by_movie.max()

# Display the result
print(f"\nThe movie with the most dialogue spoken is '{most_dialogue_movie}' with a total of {total_dialogue} lines.")

# Find the movie with the least dialogue spoken
least_dialogue_movie = dialogue_by_movie.idxmin()
total_dialogue = dialogue_by_movie.min()

# Display the result
print(f"The movie with the least dialogue spoken is '{least_dialogue_movie}' with a total of {total_dialogue} lines.")

# Calculate the frequency of each dialogue line
top_dialogue_line = scripts_df['dialog'].value_counts().idxmax()
total_occurrences = scripts_df['dialog'].value_counts().max()

# Display the result
print(f"The line said the most is: '{top_dialogue_line}'")
print(f"It is said a total of {total_occurrences} times.")