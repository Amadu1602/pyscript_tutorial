import pandas as pd

from pyodide.http import open_url

df = pd.read_csv(open_url("https://raw.gitbuusercontent.com/mwaskom/seaborn-data/master/diamonds.csv"))

csv = Element('csv')

csv.write(df.shape)