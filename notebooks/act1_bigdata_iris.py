# -*- coding: utf-8 -*-
"""Act1-BIGDATA-Iris

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pp6L_0KL_nbQw8uru9qIsYx8zAHfQ7eK
"""

import pandas as pd
import numpy as np

iris = pd.read_csv("iris.data", names=["sepalLength","sepalWidth","petalLenght","petalWidth","class"])

iris.head()

iris.count()

iris.describe()

iris.info()

iris['sepalLength'].value_counts(dropna=False)

iris['sepalWidth'].value_counts(dropna=False)

iris['petalLenght'].value_counts(dropna=False)

iris['petalWidth'].value_counts(dropna=False)

iris['class'].value_counts(dropna=False)