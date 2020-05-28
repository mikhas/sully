# AUTOGENERATED! DO NOT EDIT! File to edit: 00_eda.ipynb (unless otherwise specified).

__all__ = ['extract', 'findCategoricalCandidates', 'categoricalTally', 'timeOfDay', 'filename', 'save', 'load']

# Cell
from zipfile import ZipFile
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from pathlib import Path

# Cell

def extract(fn:Path):
    zfl = []

    if fn.is_file():
        with ZipFile(fn.as_posix(), 'r') as zf:
            zf.extractall(fn.parent)
            for curr in zf.filelist:
                zfl.append(fn.parent / curr.filename)
    else:
        zfl = [fn.parent / 'Bird Strikes Test.csv']

    loader = lambda fn: pd.read_csv(fn, low_memory=False, parse_dates=True)
    return {curr.name: loader(curr) for curr in zfl}

# Cell

def findCategoricalCandidates(data:pd.DataFrame, ratio:float=0.01)->pd.DataFrame:
    result = pd.DataFrame(
        [(col, len(data[col].unique())) for col in data.columns],
        columns=['name', 'size']
    ).sort_values(by='size')

    n = len(data)
    return result[result['size'] / n < ratio]

# Cell

def categoricalTally(data:pd.DataFrame, cat_candidates:list, limit:int=10)->pd.DataFrame:
    result_cols = ['column'] + [f'cat{i:02d}' for i  in range(limit)]
    result = pd.DataFrame(columns=result_cols)

    index = 0
    for col in cat_candidates:
        categories = data[col].unique()[:limit]
        result.loc[index] = ([col] + [(cat, len(data[data[col] == cat])) for cat in categories]
                                   + [None for i in range(len(categories), limit)])
        index += 1

    return result

# Cell
def timeOfDay(time_iv: pd.Interval)->str:
    if not isinstance(time_iv, pd.Interval):
        return None

    if (time_iv.left >= 2200 and time_iv.right < 2400) or (time_iv.left > 0 and time_iv.right < 400):
        return 'Night'

    if time_iv.left >= 400 and time_iv.right < 600:
        return 'Dawn'

    if time_iv.left >= 2000 and time_iv.right < 2200:
        return 'Dusk'

    return 'Day'

# Cell
def filename(name:str)->Path:
    return (Path().absolute() / 'models' / name).with_suffix('.pickle')

def save(data:pd.DataFrame, name:str):
    fn = filename(name)
    fn.parent.mkdir(parents=True, exist_ok=True)
    data.to_pickle(fn)

def load(name:str)->pd.DataFrame:
    fn = filename(name)
    return pd.read_pickle(fn) #, low_memory=False, parse_dates=True)