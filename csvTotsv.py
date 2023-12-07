#csv를 tsv로 변환
import pandas as pd
path = './train_test_data/train_passage.csv' # 파일 경로 설정
df = pd.read_csv(path, sep = ",", engine='python', encoding = "utf-8")
df.dropna(axis=0)
df.to_csv('train.tsv', sep='\t', encoding="utf-8", index=False)

