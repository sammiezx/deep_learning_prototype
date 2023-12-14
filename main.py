import pandas as pd
df = pd.read_csv("/home/samir/Desktop/rudraAnalytics/sub_projects/churn/data.csv")

for x in df.columns:
    print(df[x].value_counts())
    print(f"""
        FOR {x}
        ####################################################
    """)