# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.3'
#       jupytext_version: 1.0.2
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

import pandas as pd
import numpy as np
# Se usa math para truncar los valores decimales obtenidos
import math
from sklearn import linear_model

df = pd.read_excel("salary.xlsx")

df

df.exp=df.exp.fillna(0)
df

# +

mediantest=math.floor(df.test.mean())
# -

mediantest

df.test=df.test.fillna(mediantest)

df

# Ojo a esta función, que es cosecha propia
df.exp[2:8] = df.exp[2:8].apply(w2n.word_to_num)

df

reg = linear_model.LinearRegression()
reg.fit(df[['exp','test','inter']],df.salary)

reg.predict([[2,9,6]])

reg.predict([[12,10,10]])

print("Hello world")


