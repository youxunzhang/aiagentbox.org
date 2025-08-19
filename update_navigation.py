#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
批量更新网站导航和样式
"""

import os
import re
from pathlib import Path

def update_html_file(file_path):
    """更新单个HTML文件的导航和样式"""
    print(f"正在更新: {file_path}")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 更新头部LOGO样式
    content = re.sub(
        r'<div class="w-10 h-10 bg-gradient-to-r from-blue-500 to-purple-600 rounded-xl flex items-center justify-center shadow-lg">',
        '<div class="w-16 h-12 bg-gradient-to-r from-blue-500 via-purple-600 to-pink-600 rounded-xl flex items-center justify-center shadow-lg transform hover:scale-105 transition-all duration-300">',
        content
    )
    
    # 更新头部LOGO图标大小
    content = re.sub(
        r'<span class="text-white font-bold text-lg">🤖</span>',
        '<span class="text-white font-bold text-xl">🤖</span>',
        content
    )
    
    # 更新标题样式
    content = re.sub(
        r'<h1 class="text-2xl font-bold bg-gradient-to-r from-blue-600 to-purple-600 bg-clip-text text-transparent">\s*AI工具导航\s*</h1>',
        '''<div class="flex flex-col">
                        <h1 class="text-3xl font-bold bg-gradient-to-r from-blue-600 via-purple-600 to-pink-600 bg-clip-text text-transparent">
                            AI工具导航
                        </h1>
                        <p class="text-sm text-gray-600 mt-1">最全面的人工智能工具集合</p>
                    </div>''',
        content
    )
    
    # 更新工具卡片内边距
    content = re.sub(
        r'class="tool-card p-4 rounded-xl hover:shadow-lg transition-all"',
        'class="tool-card p-6 rounded-xl hover:shadow-lg transition-all"',
        content
    )
    
    # 更新网格间距
    content = re.sub(
        r'<div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-5 gap-4 p-8">',
        '<div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-5 gap-6 p-8">',
        content
    )
    
    # 更新工具LOGO样式
    content = re.sub(
        r'\.tool-logo \{\s*width: 48px;\s*height: 48px;',
        '.tool-logo {\n            width: 64px;\n            height: 48px;',
        content
    )
    
    # 更新工具LOGO字体大小
    content = re.sub(
        r'font-size: 20px;',
        'font-size: 24px;',
        content
    )
    
    # 更新工具LOGO下边距
    content = re.sub(
        r'margin-bottom: 8px;',
        'margin-bottom: 12px;',
        content
    )
    
    # 更新移动端工具LOGO
    content = re.sub(
        r'\.tool-logo \{\s*width: 28px;\s*height: 28px;\s*font-size: 14px;',
        '.tool-logo {\n                width: 48px;\n                height: 36px;\n                font-size: 18px;',
        content
    )
    
    # 更新小屏幕工具LOGO
    content = re.sub(
        r'\.tool-logo \{\s*width: 24px;\s*height: 24px;\s*font-size: 12px;',
        '.tool-logo {\n                width: 40px;\n                height: 30px;\n                font-size: 16px;',
        content
    )
    
    # 更新工具卡片最小高度
    content = re.sub(
        r'min-height: 120px;',
        'min-height: 140px;',
        content
    )
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ 已更新: {file_path}")

def main():
    """主函数"""
    # 获取当前目录
    current_dir = Path('.')
    
    # 查找所有HTML文件
    html_files = list(current_dir.glob('*.html'))
    
    print(f"找到 {len(html_files)} 个HTML文件")
    
    # 更新每个文件
    for html_file in html_files:
        try:
            update_html_file(html_file)
        except Exception as e:
            print(f"❌ 更新失败 {html_file}: {e}")
    
    print("\n🎉 所有文件更新完成！")

if __name__ == "__main__":
    main() 