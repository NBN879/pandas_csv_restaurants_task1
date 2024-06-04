import pandas as pd
import numpy as np

df = pd.read_csv('orders.csv', sep = ',')
print(df.head(2))

# 1. Сколько уникальных городов представлено в этом датафрейме?
# print(df.groupby('city_id')['city_id'].nunique().count())
uniq_city = df['city_id'].nunique()

# 2. Сколько ресторанов в таблице специализируются на рыбе?
vedndor_fish = df[df.spec == 'Рыба']['vendor_id'].nunique()

# 3. Сколько колонок в датафрейме имеют тип данных float64?
col_float64 = df.dtypes[df.dtypes == 'float64'].count()

# 4. Сколько дней у ресторана с идентификатором 40065 было менее 20 успешных заказов?
succ_days_cnt = df[(df.vendor_id == 40065) & (df.successful_orders < 20)]['date'].count()

# Ответ выведите целыми числами через запятую
res = [uniq_city, vedndor_fish, col_float64, succ_days_cnt]
print(', '.join(map(str, res)))
