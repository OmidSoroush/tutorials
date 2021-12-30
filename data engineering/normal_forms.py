import pandas as pd
import numpy as np

df = pd.DataFrame({'Name': ['Mario', 'Glenn', 'Steve'], 'Subjects': [
    ['English', 'Math'], ['Math'], ['Science', 'English']]})

lens = list(map(len, df['Subjects'].values))

res = pd.DataFrame({'Name': np.repeat(
    df['Name'], lens), 'Subject': np.concatenate(df['Subjects'].values)})

