import os
import pandas as pd

# Initialize global variables used across several different
# scripts
DATA_FILE = 'data/fish_vulnerability_new.csv'
CWD = os.path.dirname(os.path.abspath(__file__))
DATA_STR = os.path.join(CWD, DATA_FILE)
DATA = pd.read_csv(DATA_STR)
