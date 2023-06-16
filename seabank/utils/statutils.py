import pandas as pd
import numpy as np
import pmdarima as pm
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt

from abc import ABC, abstractmethod
from datetime import datetime
from typing import Literal

def from_dict(data: dict) -> pd.DataFrame:
    """Support data source from python dictionary"""
    df = pd.DataFrame.from_dict(data=data)
    return df

def from_list(data: list) -> pd.DataFrame:
    """Support data source from python list"""
    df = pd.DataFrame(data=data)
    return df

def from_csv(file:any) -> pd.DataFrame:
    """Support data source from CSV file"""
    df = pd.read_csv(filepath_or_buffer=file, index_col="pt_date", parse_dates=True)
    return df

def from_excel(file:any) -> pd.DataFrame:
    """Support data source from Excel file"""
    df = pd.read_excel(filepath_or_buffer=file)
    return df

def from_sql(sql:any, con:str) -> pd.DataFrame:
    """Support data source from SQL statements and its connection"""
    df = pd.read_sql(sql=sql, con=con)
    return df

def from_sas(file:any, format: Literal["sas7bdat", "xport"]=None) -> pd.DataFrame:
    """Support data source from SAS with default format sas7bdat"""
    df = pd.read_sas(filepath_or_buffer=file,format=format)
    return df

def from_spss(file:any) -> pd.DataFrame:
    """Support data source from SPSS"""
    df = pd.read_spss(path=file)
    return df

def split_data(data: list, nrows=0) -> tuple:
    # Split dataset to train set and test set
    msk = (data.index < len(data)-nrows)
    df_train = data[msk].copy()
    df_test = data[~msk].copy()

    return (df_train, df_test)

def do_log_transform(data):
    """Transform data to log"""
    data = np.log(data)
    return data

def do_data_interpolation(data):
    """Interpolate data in between"""
    df = data.interpolate()
    return df

def do_acf_testing(data, lags):
    """Autocorrelation Function"""
    acf_org = plot_acf(data, lags=lags)
    plt.show()

    return acf_org

def do_pacf_testing(data, lags):
    """ Partial Autocorrelation Function"""
    pacf_org = plot_pacf(data, lags=lags)
    plt.show()

    return pacf_org

def do_dicky_fuller_test(data):
    """ADF testing or Augmented Dicky-Fuller to obtain the fitness of data given before ARIMA model step"""
    adf_test = adfuller(data)
    result = {"ADF Statistics": adf_test[0], "p-value": adf_test[1], "Critical Values": [(k, v) for k,v in adf_test[4].items()]}
    return result

def manual_arima_test(data, p, d, q):
    """Perform MANUAL ARIMA by set p, q, d"""
    model = ARIMA(data, order=(p,d,q))
    model_fit = model.fit()
    model_fit.summary()

def auto_arima_test(data):
    """Perform AUTO ARIMA ordering and tests ARIMA"""
    auto_arima = pm.auto_arima(data, trace=True, step=True, seasonal=True, with_intercept=True)
    return (auto_arima, auto_arima.summary())

def forecast_arima(data, n=None):    
    """Perform forecast"""
    if n is None:
        n = len(data)
    
    forecast_auto = data.predict(n_periods=len(n))
    data['forecast_auto'] = [None] * len(data) + list(forecast_auto)

    return data['forecast_auto']

class InterfaceProcedure(ABC):
    """Interface for statistical procedures and methodologies uses."""

    @abstractmethod
    def run():
        """How data is output."""

    @abstractmethod
    def output_file():
        """Where the output file stored"""

class AutoArimaProcedure(InterfaceProcedure):
    """Auto Arima Procedures"""
    def __init__(self, data, split=0, output=None):
        """Obtain source data from initializer"""
        self.data = data
        self.nrows = split
        self.output = output
        self.prediction = False
        self.result = {}
    
    def output_file():
        pass

    def run(self):
        data = from_csv(self.data)
        train, test = split_data(data, nrows=self.nrows)
        model, summary = auto_arima_test(train)
        forecast = model.predict(n_periods=len(test))

        self.result['rundate'] = datetime.now()
        self.result['data'] = data 
        self.result["train"] = train
        self.result["test"] = test
        self.result["model"] = model.to_dict()
        self.result['prediction'] = [None] * len(train) + list(forecast)

        print(summary)

        return self


proc1 = AutoArimaProcedure("../file/input-python.csv", 3).run()
# print(proc1.result['prediction'])
print(proc1.result['model'])

pd.DataFrame(proc1.result['prediction']).to_csv("../file/output-python.csv", sep=",", header=False)
# pd.DataFrame(proc1.result['model']).to_csv("../file/output-model.csv", sep=",", header=False)