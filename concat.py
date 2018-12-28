from __future__ import print_function
import pandas as pd
import numpy as np

# concatenating
# ignore index
df1 = pd.DataFrame(np.ones((3,4))*0, columns=['a','b','c','d'])
df2 = pd.DataFrame(np.ones((3,4))*1, columns=['a','b','c','d'])
df3 = pd.DataFrame(np.ones((3,4))*2, columns=['a','b','c','d'])
res1 = pd.concat([df1, df2, df3], axis=0, ignore_index=True)

# join, ('inner', 'outer')
df1 = pd.DataFrame(np.ones((3,4))*0, columns=['a','b','c','d'], index=[1,2,3])
df2 = pd.DataFrame(np.ones((3,4))*1, columns=['b','c','d', 'e'], index=[2,3,4])
res2 = pd.concat([df1, df2], axis=1, join='outer')
res3 = pd.concat([df1, df2], axis=1, join='inner')

# join_axes
res4 = pd.concat([df1, df2], axis=1, join_axes=[df1.index])

# append
df1 = pd.DataFrame(np.ones((3,4))*0, columns=['a','b','c','d'])
df2 = pd.DataFrame(np.ones((3,4))*1, columns=['a','b','c','d'])
df2 = pd.DataFrame(np.ones((3,4))*1, columns=['b','c','d', 'e'], index=[2,3,4])
res5 = df1.append(df2, ignore_index=True)
res6 = df1.append([df2, df3])

s1 = pd.Series([1,2,3,4], index=['a','b','c','d'])
res7 = df1.append(s1, ignore_index=True)

print(res5)