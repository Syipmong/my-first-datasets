import pandas as pd 

name = "Yipmong"
age = 22

def info_user(name, age):
    return f'{name} is {age} years old.'

test_path = 'download.csv'

test_read = pd.read_csv(test_path)

test_data = test_read.iloc[:,2:]

print(test_data)

