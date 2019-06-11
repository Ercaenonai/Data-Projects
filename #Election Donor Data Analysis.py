#Election Donor Data Analysis
import pandas as pd
from pandas import Series,DataFrame
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import requests
from io import StringIO
from datetime import datetime

donor_df = pd.read_csv('Election_Donor_Data.csv')

donor_df.info()

donor_df.head()

donor_df['contb_receipt_amt'].value_counts()


don_mean = donor_df['contb_receipt_amt'].mean()

don_std = donor_df['contb_receipt_amt'].std()

print ('The avg. donation was %.2f with a std of %.2f' %(don_mean,don_std))