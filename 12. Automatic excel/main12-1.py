import pandas as pd

df = pd.DataFrame([["김지우", "2002.02.26", "2023-0001"], 
                    ["이윤지", "2001.06.05", "2023-0002"],
                    ["김성식", "1967.11.09", "2023-0003"],
                    ["주영미", "1971.02.04", "2023-0004"]])


print(df)
df.to_excel(r'12. Automatic excel\list.xlsx', index=False, header=False)