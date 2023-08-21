from gpt import SpecExtractor
import pandas as pd

df_i = pd.read_csv('sample_file.csv')

columns = ['CPU Model', 'GPU Model', 'RAM Capacity', 'Storage Type', 'Storage Capacity','price']
df = pd.DataFrame(columns=columns)

extractor = SpecExtractor()
ind = 1
tmp = df_i['title'][ind]
dict_result = extractor.extract_from_title(tmp)
dict_result['price']=df_i['price'][ind]

print(dict_result)