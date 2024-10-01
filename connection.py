import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine
import matplotlib.font_manager as fm

# 한글 폰트 설정 (NanumGothic 사용 예시)
plt.rc('font', family='NanumGothic')  # 또는 'Malgun Gothic'과 같은 시스템에 설치된 폰트 사용

# SQLAlchemy 엔진을 사용하여 PostgreSQL 연결

# 쿼리 실행
query = """
SELECT * 
FROM tbsh_gyeonggi_day 
WHERE ta_ymd >= '20230801' AND ta_ymd < '20230901'
AND card_tpbuz_nm_1 = '음식'
ORDER BY ta_ymd DESC
limit 1000
"""

# SQLAlchemy를 통해 쿼리를 실행하고 데이터프레임으로 변환
df = pd.read_sql(query, engine)

# card_tpbuz_nm_2 별로 그룹화하여 카운트 계산
df_grouped = df.groupby('card_tpbuz_nm_2').size().reset_index(name='counts')

# 차트 그리기
plt.figure(figsize=(10, 6))
sns.barplot(x='card_tpbuz_nm_2', y='counts', data=df_grouped)

# 차트 제목과 라벨 추가
plt.title('Counts by card_tpbuz_nm_2', fontsize=16)
plt.xlabel('카드 업종 분류 (card_tpbuz_nm_2)', fontsize=14)  # 한글 라벨 추가
plt.ylabel('카운트', fontsize=14)  # 한글 라벨 추가

# x축 라벨이 겹치지 않도록 회전
plt.xticks(rotation=45)

# 차트 보여주기
plt.tight_layout()
plt.show()
