#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Google AdSense代码批量添加脚本
将AdSense代码添加到所有HTML文件的head部分
"""

import os
import re
from pathlib import Path

def add_adsense_to_file(file_path):
    """向单个文件添加Google AdSense代码"""
    print(f"正在添加AdSense代码: {file_path}")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Google AdSense代码
    adsense_code = '''    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-8794607118520437"
         crossorigin="anonymous"></script>'''
    
    # 检查是否已经包含AdSense代码
    if 'pagead2.googlesyndication.com' in content:
        print(f"⚠️  {file_path} 已包含AdSense代码，跳过")
        return
    
    # 查找Google AdSense meta标签的位置
    adsense_meta_pattern = r'(<!-- Google AdSense -->\s*<meta name="google-adsense-account" content="ca-pub-8794607118520437">)'
    
    if re.search(adsense_meta_pattern, content):
        # 如果找到AdSense meta标签，在其后添加script标签
        content = re.sub(
            adsense_meta_pattern,
            r'\1\n' + adsense_code,
            content
        )
        print(f"✅ 在AdSense meta标签后添加了script代码: {file_path}")
    else:
        # 如果没有找到AdSense meta标签，在Google Analytics后添加
        analytics_pattern = r'(<!-- Google Analytics -->\s*<script async src="https://www\.googletagmanager\.com/gtag/js\?id=G-CXH17REJKN"></script>\s*<script>.*?</script>\s*)'
        
        if re.search(analytics_pattern, content, re.DOTALL):
            # 在Google Analytics后添加完整的AdSense代码
            full_adsense_code = '''    <!-- Google AdSense -->
    <meta name="google-adsense-account" content="ca-pub-8794607118520437">
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-8794607118520437"
         crossorigin="anonymous"></script>
    
'''
            content = re.sub(
                analytics_pattern,
                r'\1' + full_adsense_code,
                content,
                flags=re.DOTALL
            )
            print(f"✅ 在Google Analytics后添加了完整AdSense代码: {file_path}")
        else:
            # 如果都没有找到，在head标签开始后添加
            head_pattern = r'(<head>)'
            if re.search(head_pattern, content):
                full_adsense_code = '''    <!-- Google AdSense -->
    <meta name="google-adsense-account" content="ca-pub-8794607118520437">
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-8794607118520437"
         crossorigin="anonymous"></script>
    
'''
                content = re.sub(
                    head_pattern,
                    r'\1\n' + full_adsense_code,
                    content
                )
                print(f"✅ 在head标签后添加了完整AdSense代码: {file_path}")
            else:
                print(f"❌ 无法找到合适的插入位置: {file_path}")
                return
    
    # 保存文件
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ AdSense代码添加完成: {file_path}")

def main():
    """主函数"""
    # 获取当前目录
    current_dir = Path('.')
    
    # 查找所有HTML文件
    html_files = list(current_dir.glob('*.html'))
    
    print(f"找到 {len(html_files)} 个HTML文件")
    print("开始添加Google AdSense代码...")
    print()
    
    # 处理每个HTML文件
    for html_file in html_files:
        try:
            add_adsense_to_file(html_file)
        except Exception as e:
            print(f"❌ 处理失败 {html_file}: {e}")
        print()
    
    print("🎉 Google AdSense代码添加完成！")
    print("\n添加内容包括：")
    print("✅ Google AdSense meta标签")
    print("✅ Google AdSense JavaScript代码")
    print("✅ 所有HTML文件已更新")

if __name__ == "__main__":
    main()
