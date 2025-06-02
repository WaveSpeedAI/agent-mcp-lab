import os
import requests
import time

# 确保目标目录存在
asset_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'integrations', 'asset')
os.makedirs(asset_dir, exist_ok=True)

# 需要下载的结果图片列表
images = [
    "1748705463160818023_uZ2iVayO.webp",
    "1748705471235905591_5TPMIGDz.webp",
    "1748705479698088610_zAFCxurn.webp",
    "1748705488729110114_MQ0XTPLI.webp",
    "1748705498771081684_AKT3eU3c.webp",
    "1748705508822359769_ddmjgc9s.webp",
    "1748705519167844613_RhFByuqm.webp",
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

print("所有结果图片下载完成！")
