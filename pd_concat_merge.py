import pandas as pd

raw_data = {
    'subject_id': ['1', '2', '3', '4', '5'],
    'first_name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
    'last_name': ['Anderson', 'Ackerman', 'Ali', 'Aoni', 'Atiches']
}
df_a = pd.DataFrame(raw_data, columns = ['subject_id', 'first_name', 'last_name'])
df_a.index = [0,1,2,3,4]
print(df_a)

raw_data = {
    'subject_id': ['4', '5', '6', '7', '8'],
    'first_name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
    'last_name': ['Bonder', 'Black', 'Balwner', 'Brice', 'Btisan']
}
df_b = pd.DataFrame(raw_data, columns = ['subject_id', 'first_name', 'last_name'])
df_b.index = [2,3,4,5,6]
print(df_b)

df_new = pd.concat([df_a, df_b], axis = 0)
print(df_new)

df_new = pd.concat([df_a, df_b], axis = 1)
print(df_new)

df_new = pd.concat([df_a, df_b], axis = 1, join = 'inner')
print(df_new)

df_new_ = pd.merge(df_a, df_b, on='subject_id')
print(df_new_)