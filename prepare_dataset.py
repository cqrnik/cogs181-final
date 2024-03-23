import csv
import random

# Function to read CSV file, extract lyrics, and write to text file
def extract_random_lyrics(input_file, output_file, num_samples=1000):
    with open(input_file, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        rows = list(reader)
        # Shuffle the rows randomly
        random.shuffle(rows)
        with open(output_file, 'w', encoding='utf-8') as txtfile:
            for i in range(min(num_samples, len(rows))):  # Ensure we don't exceed the number of rows
                lyrics = rows[i]['text']
                txtfile.write(lyrics)
                txtfile.write('\n\n')  # Adding new lines between lyrics of different songs

# Input and output file paths
input_file = 'data/spotify_millsongdata.csv'
output_file = 'data/random_1000_lyrics.txt'

# Call the function with 1,000 random samples
extract_random_lyrics(input_file, output_file)