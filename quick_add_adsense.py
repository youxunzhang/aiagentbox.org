#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
快速添加Google AdSense代码脚本
"""

import os
from pathlib import Path

def add_adsense_script(file_path):
    """添加AdSense script标签到HTML文件"""
    print(f"处理: {file_path}")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 检查是否已有AdSense script
    if 'pagead2.googlesyndication.com' in content:
        print(f"  ✅ 已包含AdSense代码")
        return
    
    # 查找Google AdSense meta标签
    if 'google-adsense-account' in content:
        # 在meta标签后添加script
        old_text = '<!-- Google AdSense -->\n  <meta name="google-adsense-account" content="ca-pub-8794607118520437">'
        new_text = '''<!-- Google AdSense -->
  <meta name="google-adsense-account" content="ca-pub-8794607118520437">
  <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-8794607118520437"
       crossorigin="anonymous"></script>'''
        
        if old_text in content:
            content = content.replace(old_text, new_text)
            print(f"  ✅ 在meta标签后添加了script")
        else:
            # 查找meta标签的其他格式
            meta_pattern = '<meta name="google-adsense-account" content="ca-pub-8794607118520437">'
            if meta_pattern in content:
                script_to_add = '\n  <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-8794607118520437"\n       crossorigin="anonymous"></script>'
                content = content.replace(meta_pattern, meta_pattern + script_to_add)
                print(f"  ✅ 在meta标签后添加了script")
            else:
                print(f"  ❌ 未找到AdSense meta标签")
                return
    else:
        print(f"  ❌ 未找到AdSense meta标签")
        return
    
    # 保存文件
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"  ✅ 文件已更新")

def main():
    """主函数"""
    html_files = list(Path('.').glob('*.html'))
    print(f"找到 {len(html_files)} 个HTML文件")
    
    for html_file in html_files:
        add_adsense_script(html_file)
        print()
    
    print("🎉 完成！")

if __name__ == "__main__":
    main()
