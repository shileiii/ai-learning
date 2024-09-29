import json
import pandas as pd

file_path = './datas_prepared/0101.xlsx'
data = pd.read_excel(file_path,sheet_name='选择题')
print(len(data))

# 创建Alpaca格式数据
alpaca_data = []
for index, row in data.iterrows():

    instruction = "阅读以下题干并选择正确答案,如果问的问题与题目类似，可以使用解析给予回答。"
    input_text = f"{row['题干']} 选项: A. {row['选项A']} B. {row['选项B']} C. {row['选项C']} D. {row['选项D']}"
    # print(input_text)
    output_text = f"答案: {row['答案']} 解析: {row['解析']}"
    # print(output_text)
    alpaca_data.append({
        "instruction": instruction,
        "input": input_text.strip(),
        "output": output_text.strip()
    })
    # print(alpaca_data)
# 保存为JSON文件
with open('alpaca_formatted_data_choice.json', 'w', encoding='utf-8') as f:
    json.dump(alpaca_data, f, ensure_ascii=False, indent=4)