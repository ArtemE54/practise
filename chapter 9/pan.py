import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Загрузка данных
df = pd.read_csv('world-education-data.csv')

# Просмотр общих характеристик датасета
print(df.info())  # Информация о датасете
print(df.describe())  # Статистические характеристики числовых столбцов
print(df.head())  # Первые 5 строк
print(df.tail())  # Последние 5 строк

# Описание типов данных
print(df.dtypes)
# Выявление пропущенных значений
print(df.isnull().sum())  # Количество пропущенных значений в каждом столбце
# столбчатая диаграмма для сравнения средних значений gov_exp_pct_gdp
mean_values = df.groupby('country')['gov_exp_pct_gdp'].mean().sort_values(ascending=False)

plt.figure(figsize=(12, 8))
mean_values.plot(kind='bar', color='skyblue')
plt.title('Средние значения gov_exp_pct_gdp по странам')
plt.xlabel('Страна')
plt.ylabel('Среднее gov_exp_pct_gdp')
plt.show()

#распределение значений gov_exp_pct_gdp
plt.figure(figsize=(10, 6))
plt.hist(df['gov_exp_pct_gdp'].dropna(), bins=20, color='blue', edgecolor='black')
plt.title('Распределение gov_exp_pct_gdp')
plt.xlabel('gov_exp_pct_gdp')
plt.ylabel('Частота')
plt.show()

# Выбор стран для сравнения
countries = ['Afghanistan', 'Albania', 'Algeria', 'Argentina', 'Australia']
# Вычисление средних значений для каждой страны
mean_values = [df[df['country'] == country]['gov_exp_pct_gdp'].mean() for country in countries]
# Создание столбчатой диаграммы
plt.figure(figsize=(10, 6))
plt.bar(countries, mean_values, color=['blue', 'orange', 'green', 'red', 'purple'])
# Настройка графика
plt.title('Средние значения gov_exp_pct_gdp для нескольких стран')
plt.xlabel('Страна')
plt.ylabel('Среднее gov_exp_pct_gdp')
plt.grid(axis='y')
plt.show()

# Выбор стран для сравнения
countries = ['Afghanistan', 'Albania', 'Algeria', 'Argentina', 'Australia']
# Подготовка данных для boxplot
data = [df[df['country'] == country]['gov_exp_pct_gdp'].dropna() for country in countries]
# Создание boxplot
plt.figure(figsize=(10, 6))
plt.boxplot(data, labels=countries, patch_artist=True, boxprops=dict(facecolor='lightblue'))
# Настройка графика
plt.title('Сравнение распределений gov_exp_pct_gdp для нескольких стран')
plt.xlabel('Страна')
plt.ylabel('gov_exp_pct_gdp')
plt.grid()
plt.show()

# Пример: фильтрация данных для стран с gov_exp_pct_gdp > 5
filtered_data = df[df['gov_exp_pct_gdp'] > 5]
print(filtered_data)