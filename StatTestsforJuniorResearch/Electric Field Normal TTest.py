import pandas as pd
import matplotlib as plt
from scipy.stats import stats

electricfieldnormaldata = pd.read_csv("Electric Normal Graph Data.csv")
electricfieldnormaldata.describe()