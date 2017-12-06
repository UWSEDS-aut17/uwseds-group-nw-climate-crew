
import os
import pandas as pd

DATA_FILE = 'model/fish_vulnerability.csv'
CWD = os.path.dirname(os.path.abspath(__file__))
DATA_STR = os.path.join(CWD, DATA_FILE)
DATA = pd.read_csv(DATA_STR)

