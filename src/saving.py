import os
import shelve
from typing import Dict, Union
from datetime import datetime
from appdirs import user_data_dir
from manifest import NAME


HistoryLine = Dict[str, Union[datetime, str]]


DB_DIR = f'{user_data_dir()}/{NAME}'
DB_DATA = f'{DB_DIR}/data'
DB_HISTORY = f'{DB_DIR}/history'


DEFAULT_DATA = {
    'coef0': '1',
    'coef1': '0.5',
    'limit0': '0',
    'limit1': '100',
    'limit2': '600',
    'price0': '71.4',
    'price1': '129',
    'price2': '163.8'}


def create_dir_if_need() -> None:
    try:
        os.stat(DB_DIR)
    except FileNotFoundError:
        os.mkdir(DB_DIR)


def restore_data() -> Dict[str, str]:
    data = DEFAULT_DATA
    create_dir_if_need()
    with shelve.open(DB_DATA) as database:
        data.update(database)
    return data


def save_data(data: Dict[str, str]) -> None:
    create_dir_if_need()
    with shelve.open(DB_DATA) as database:
        database.update(data)


def restore_history() -> Dict[str, HistoryLine]:
    result: Dict[str, HistoryLine] = {}
    create_dir_if_need()
    with shelve.open(DB_HISTORY) as database:
        result.update(database)
    return result


def save_history(history: Dict[str, HistoryLine]) -> None:
    create_dir_if_need()
    with shelve.open(DB_HISTORY) as database:
        database.clear()
        database.update(history)
