# import pandas as pd

# data = [10, 20, 30, 40]

# ps = pd.Series(data)
# print(ps, type(ps))



# import pandas as pd

# data = {
#     "Subject": ["Python", "Java", "C++"],
#     "Marks": [90, 80, 87],
#     "Grade": ['A', 'B', 'B']
# }

# df = pd.DataFrame(data)
# print(df, type(df))



# print(pd.__version__)



# import pandas as pd

# data = [90, 80, 87, 45, 74]

# df = pd.Series(data, index = ['a', 'b', 'c', 'd', 'e'])
# print(df['c'], type(df))



# import pandas as pd

# data = {'day1': [400, 500], 'day2': 450}

# df = pd.Series(data)
# print(df, type(df))



# import pandas as pd

# data = {'day1': [400, 500], 'day2': 450, 'day3': 430}

# df = pd.Series(data)
# print(df)
# res = df.tolist()
# print(res, type(res))



import pandas as pd

data = {
    'marks': [420, 380, 390],
    'duration': [50, 40, 45]
}

df = pd.DataFrame(data)
print(df.loc[0])
print(df.loc[[0]])
print(df.loc[[0, 2, 1]])



# import pandas as pd

# data = {
#     'marks': [420, 380, 390],
#     'duration': [50, 40, 45]
# }

# df = pd.DataFrame(data, index = ['d1', 'd2', 'd3'])
# print(df.loc[['d1', 'd3', 'd2']])



# import pandas as pd

# data = {
#     'subject': ['Python', 'C++', 'Java'],
#     'marks': [420, 380, 390],
#     'duration': [50, 40, 45]
# }

# df = pd.DataFrame(data)
# print(df)

# df.columns = ['s1', 's2', 's3']
# print(df)