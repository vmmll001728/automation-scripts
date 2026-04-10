# -*- coding: utf-8 -*-
"""
批量重命名文件
功能：给指定目录下的文件添加前缀或后缀
"""

import os
import shutil
from pathlib import Path

def batch_rename(directory, prefix="", suffix="", extension=None):
    """
    批量重命名文件
    
    Args:
        directory: 目标目录路径
        prefix: 文件名前缀
        suffix: 文件名后缀
        extension: 只处理指定扩展名的文件（如 ".txt"）
    """
    directory = Path(directory)
    
    if not directory.exists():
        print(f"❌ 目录不存在: {directory}")
        return
    
    count = 0
    for file_path in directory.iterdir():
        if file_path.is_file():
            # 检查扩展名
            if extension and file_path.suffix != extension:
                continue
            
            # 生成新文件名
            new_name = f"{prefix}{file_path.stem}{suffix}{file_path.suffix}"
            new_path = file_path.parent / new_name
            
            # 重命名
            file_path.rename(new_path)
            print(f"✅ {file_path.name} → {new_name}")
            count += 1
    
    print(f"\n🎉 完成！共重命名 {count} 个文件")

if __name__ == "__main__":
    # 使用示例
    # 给当前目录所有 .txt 文件添加 "备份_" 前缀
    batch_rename(".", prefix="备份_", suffix="", extension=".txt")
