import os
import requests
import time

# 确保目标目录存在
asset_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'integrations', 'asset')
os.makedirs(asset_dir, exist_ok=True)

# 需要下载的图片列表
images = [
    # Windsurf特定图片
    "1748830893954385333_CzTROKIE.webp",
    "1748830898813768514_uXa6TPNI.webp",
    "1748830902079561216_Reonkjkj.webp",
    "1748830906358464130_Xljgeb6R.webp",
    "1748830910152511142_Eqomifb7.webp",
    "1748830914185622709_JfI1oHXj.webp",
    "1748830918088257694_yEPMIEBw.png",
    "1748830922310863528_Vvtqnjfb.png",
    "1748830926758753125_NXc8pkhd.png",
]

# 下载图片
for image in images:
    url = f"https://d2g64w682n9w0w.cloudfront.net/media/images/{image}"
    target_path = os.path.join(asset_dir, image)
    
    # 检查文件是否已存在
    if os.path.exists(target_path):
        print(f"文件已存在: {target_path}")
        continue
    
    try:
        print(f"正在下载: {url}")
        response = requests.get(url, stream=True)
        response.raise_for_status()
        
        with open(target_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        
        print(f"下载完成: {target_path}")
        # 添加短暂延迟，避免请求过快
        time.sleep(0.5)
    
    except Exception as e:
        print(f"下载失败 {url}: {e}")

print("所有图片下载完成！")
