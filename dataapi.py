import pandas as pd
import json
import os

def generate_fertility_json():
    excel_path = "C:\Users\31663\Desktop\blog-main\china-map\sum.xlsx"
    growth = pd.read_excel(excel_path, sheet_name="Sheet3")
    
    fertility_data = {}
    
    years = [col for col in growth.columns if isinstance(col, int)]

    for year in years:
        fertility_data[str(year)] = {}
        
        for idx, province in enumerate(growth['地区']):
            fertility_data[str(year)][province] = float(growth[year].iloc[idx])
    
    json_dir = "json"
    if not os.path.exists(json_dir):
        os.makedirs(json_dir)
    
    json_path = os.path.join(json_dir, "fertility_data.json")
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(fertility_data, f, ensure_ascii=False, indent=2)
    
    print(f"数据已保存到: {json_path}")

if __name__ == '__main__':
    generate_fertility_json()