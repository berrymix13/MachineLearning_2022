# -*- coding: utf-8 -*-
"""01_단순선형회귀.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LpXJ6s2Aw3DW0tLZSL5DUEaHzUklThev

# 단순 선형 회귀
"""

import pandas as pd
import numpy as np

df = pd.read_csv('randomservices.txt', sep = '\t')
df.head()

"""- 아버지와 아들의 키만 발췌
- 컬럼명을 Father와 Son으로 변경
- 단위변경 inch -> cm
"""

df = df[df.Gender == 'M']
df = df[['Father', 'Height']]
# df = df[df.Gender == 'M'][['Father', 'Height']]  로 쓸 수 있다.
df.rename(columns = {'Height' : 'Son'}, inplace=True)
df = df * 2.54
df = df.reset_index(drop = True)
df.head()

import matplotlib.pyplot as plt
plt.scatter(df.Father, df.Son)
plt.xlabel('Father')
plt.ylabel('Son')
plt.title('Father , Son', fontsize = 15)
plt.show()

"""#### 회귀선 구하고 그리기
- 최소자승법
"""

# 1차식 회귀선
# 가중치, 오차항
weight, bias = np.polyfit(df.Father, df.Son, 1)
weight, bias

# 2차식 회귀선
np.polyfit(df.Father, df.Son, 2)

xs = np.array([156, 201])
ys = xs * weight + bias
ys

plt.scatter(df.Father, df.Son)
plt.plot(xs, ys, 'r-' , lw = 3, label = 'Linear')

plt.xlabel('Father')
plt.ylabel('Son')
plt.title('Father , Son', fontsize = 15)
plt.legend()
plt.show()

import seaborn as sns
sns.regplot(x='Father', y='Son', data = df);

"""### sklearn 으로 회귀선 구하기"""

from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.get_params()

# 학습
lr.fit(df.Father.values.reshape(-1,1), df.Son)

lr.fit(df[['Father']], df.Son)

# coefficient(계수)- weight , intercept(절편) - bias
lr.coef_ , lr.intercept_

# 잔차제곱합(RSS)
lr._residues

# 평가 - 결정계수 : R squared
lr.score(df[['Father']], df.Son)

from sklearn.metrics import r2_score
pred = lr.predict(df[['Father']])
r2_score(df.Son, pred)