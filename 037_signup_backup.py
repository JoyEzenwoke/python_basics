import json
import pandas as pd
with open("035_signup_data.json", "r") as file:
    signup_data = json.load(file)
df = pd.DataFrame(signup_data)
df.to_excel("038_first_exam_result.xlsx", index=False)
print("Excel file '038_first_exam_result.xlsx' created successfully.")
