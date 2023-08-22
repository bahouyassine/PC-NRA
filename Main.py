from gpt import SpecExtractor
import pandas as pd

# Load data from a CSV file into a DataFrame
df = pd.read_csv('sample_file.csv')

# Display the first few rows of the DataFrame
print(df.head())

extractor = SpecExtractor()
dict_result = extractor.extract_from_title("PC with Ryzen 5 7600X and RTX 4060Ti. It has 16 GB RAM and a 1TB SSD")
print(dict_result['CPU_Model'])