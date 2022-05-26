import pandas as pd

from pyodide.http import open_url

# df = pd.read_csv(open_url("https://raw.gitbusercontent.com/mwaskom/seaborn-data/master/diamonds.csv"))

df = pd.read_csv(open_url("/files/ccr_cif_details.csv"))

csv = Element('csv')

csv.write(df.shape)