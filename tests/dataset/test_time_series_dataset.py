import pytest
import pandas as pd
from dataset.time_series import Time_Series, TRAIN, INPUT
from dataset.time_series_dataset import Time_Series_Dataset

def init_data():
    data = pd.read_json("tests/testdata/BTC_BUSD-1h.json")
    columns = ["date", "open", "high", "low", "close", "volume"]
    data = pd.DataFrame(data.values, columns=columns)
    data['date'] =  pd.to_datetime(data["date"], unit="ms")
    return data
data = init_data()

def test_Time_Series_Dataset():
    ts_data = Time_Series(9)
    dataset = Time_Series_Dataset(TRAIN, ts_data=ts_data)
    # assert dataset.input_data.size() == ts_data(TRAIN, INPUT)