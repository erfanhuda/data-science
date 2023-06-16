import pandas as pd
import numpy as np
from statsmodels.tsa.arima_model import ARIMA
from statsmodels.tsa.stattools import adfuller
import matplotlib.pyplot as plt
from pmdarima import auto_arima
import warnings
import logging

# SETUP BASIC LOGGING
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s', datefmt="%Y-%m-%d %H:%M:%S")

# Read the csv file with datetime
df = pd.read_csv("../file/input-python.csv",index_col="pt_date", parse_dates=True)
df = df.dropna()
logging.info("Shape of data", df.shape)
df.head()

# Plot the data
df["odr_balance"].plot(figsize=(12,5))

# Check for the stationarity

def ad_test(dataset):
    dftest = adfuller(dataset, autolag= "AIC")
    logging.info("1. ADF :", dftest[0])
    logging.info("2. P-value :", dftest[1])
    logging.info("3. Num of Lags :", dftest[2])
    logging.info("4. Num of Observations Used for ADF Regression and Critical Values Calculation :", dftest[3])
    logging.info("5. Critical values :")

    for k, v in dftest[4].items():
        print("\t", k, ": ", v)

# ad_test(df["odr_balance"])
ad_test(df["odr_balance"])

# Figure out Order for ARIMA models
warnings.filterwarnings("ignore")
stepwise_fit = auto_arima(df["odr_balance"], trace=True, suppress_warnings=True, stepwise=True, m=1, max_order=15)
stepwise_fit.summary()

# Split data to train and test
nrows = 5
train = df.iloc[:-nrows]
test = df.iloc[-nrows:]
logging.info(df.shape)
logging.info(train.shape, test.shape )