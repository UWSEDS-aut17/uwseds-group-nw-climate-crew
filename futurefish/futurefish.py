
import os
import pandas as pd

DATA_STR = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        'data/tiny_site_test_dataset.csv')
DATA = pd.read_csv(DATA_STR)
