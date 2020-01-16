from typing import Tuple

import pandas as pd


def load() -> Tuple[pd.DataFrame, pd.DataFrame]:
    train_df = pd.read_csv('../../resources/train.csv')
    test_df = pd.read_csv('../../resources/test.csv')
    return train_df, test_df
