import pandas as pd
import psycopg2
from psycopg2 import sql

# 1. 엑셀 파일을 CSV로 변환
csv = './soeul_day_sex.csv'  # 엑셀 파일 경로
csv_file_path = './transfile/5/tbsh_gyeonggi_day_202308_광명시.csv'
# 엑셀 파일 읽기
df1 = pd.read_csv(csv_file_path)
# df1.to_csv(csv_file_path, index=False)
print(len(df1))
# df2 = pd.read_excel(excel_file_path, sheet_name=2)
# df3 = pd.concat([df1,df2])
# print(df3)
# CSV 파일로 저장 (필요한 경우)
# df3.to_csv(csv_file_path, index=False)
print("DONE")