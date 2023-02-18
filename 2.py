import os
import pandas as pd


def find_xlsx( path_to_dir, suffix=".xlsx" ):
    filenames = os.listdir(path_to_dir)
    return [ filename for filename in filenames if filename.endswith( suffix ) ]

tables = find_xlsx('.')

if not os.path.exists("rst"):
    os.makedirs("rst")

for i_t, t in enumerate(tables):
    
    df = pd.read_excel(tables[i_t], engine='openpyxl')
    courses = df['選修課程'].unique()
    classes = df['班級'].unique()
    columns = ['班級', '座號', '選修課程']
    orders = ['班級排序', '課程排序']


    path = "rst/"+"({})".format(orders[0]) + tables[i_t]

    writer = pd.ExcelWriter(path, engine='openpyxl') # 指定引擎openpyxl


    for i, c in enumerate(classes):
        tmp_df = df[df['班級']==classes[i]][columns]
        tmp_df.to_excel(writer, sheet_name=str(classes[i]), index=False) # 存到指定的sheet
    print(path)
    writer.save() 

    print('='*20)
