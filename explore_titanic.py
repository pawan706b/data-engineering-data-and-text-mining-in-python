# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 19:57:50 2024

@author: pawan
"""

import pandas as pd
import seaborn as sns

train_df = pd.read_csv("data/titanic_data/train.csv")
test_df = pd.read_csv("data/titanic_data/test.csv")

sns.pairplot(train_df, hue='Survived')