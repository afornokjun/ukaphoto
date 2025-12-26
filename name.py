import os
import json

# 常見的圖片副檔名（可自行增減）
IMAGE_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.gif', '.webp', '.bmp', '.tiff', '.tif'}

def main():
    # 取得目前工作目錄
    current_dir = os.getcwd()
    
    # 收集所有圖片檔名
    image_files = []
    
    for filename in os.listdir(current_dir):
        # 只看檔案（不是資料夾）
        if not os.path.isfile(os.path.join(current_dir, filename)):
            continue
            
        # 取得副檔名並轉小寫比對
        _, ext = os.path.splitext(filename)
        if ext.lower() in IMAGE_EXTENSIONS:
            image_files.append(filename)
    
    # 按檔名排序（字母+數字自然排序）
    image_files.sort()
    
    # 準備要寫的資料結構
    data = {
        "images": image_files
    }
    
    # 寫入 images.json（無論原本是否存在都會覆蓋）
    with open('images.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    count = len(image_files)
    if count == 0:
        print("目前資料夾沒有找到任何圖片檔，已產生空的 images.json")
    else:
        print(f"已完成！找到 {count} 張圖片，已產生/更新 images.json")


if __name__ == "__main__":
    main()
    # 執行完直接結束，不會要求按 Enter
