import ast
import pandas as pd

f = open("taquitos_brand_partial.txt", "r")
count = 1
newFile = []
for line in f:
    if count % 2 == 0:
        goodLine = ast.literal_eval(line) 
        # goodLine = line.strip('][').split(', ') 
        # print(goodLine)
        newFile.append(goodLine)
    count+=1

brandDataFrame = pd.DataFrame(newFile, columns = ["brand_name", "snack_name", "snack_url", "snack_taste_test","snack_smell_test", "amazon_link"])
# brandDataFrame.to_csv("Taquitos_brand_partial.csv", index=False)
print(brandDataFrame.nunique())