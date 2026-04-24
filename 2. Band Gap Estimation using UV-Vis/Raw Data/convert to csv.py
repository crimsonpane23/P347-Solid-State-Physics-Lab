import pandas as pd
df = pd.read_csv(r'Polymer.txt', sep='\t', header=None, names=['Wavelength', 'Absorbance'])
df.to_excel('Polymer_data.xlsx', index=False)
