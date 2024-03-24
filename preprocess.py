import csv

# Function to read CSV file, extract lyrics, and write to text file
def extract_lyrics(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        with open(output_file, 'w', encoding='utf-8') as txtfile:
            for row in reader:
                lyrics = row['text']
                txtfile.write(lyrics)
                txtfile.write('\n\n')  # Adding new lines between lyrics of different songs

# Input and output file paths
input_file = 'data/spotify_millsongdata.csv'
output_file = 'data/spotify_dataset.txt'

# Call the function
extract_lyrics(input_file, output_file)