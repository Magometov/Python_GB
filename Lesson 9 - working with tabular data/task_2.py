'''
    Задача 42: Узнать какая максимальная households в зоне минимального значения population.
'''
import pandas as pd


df = pd.read_csv('sample_data/california_housing_test.csv')

df[df['population']==df['population'].min()]['households'].max()