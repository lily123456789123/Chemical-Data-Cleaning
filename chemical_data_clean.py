# 化工实验数据清洗
import pandas as pd
import numpy as np

# 模拟反应温度数据（含异常值）
data = {'batch': [1, 2, 3, 4, 5],
        'temp_C': [120, 135, 999, 128, -100]}  # 999和-100是异常值
df = pd.DataFrame(data)

# 清洗规则：温度在0-200℃为有效值
df['valid'] = df['temp_C'].between(0, 200)
clean_df = df[df['valid']].drop('valid', axis=1)

print("清洗后数据：\n", clean_df)
clean_df.to_csv('cleaned_chemical_data.csv')  # 保存结果