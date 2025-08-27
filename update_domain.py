#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
域名更新脚本 - 将seodog.cn替换为aiagentbox.com
"""

import os
import re
from pathlib import Path

def update_domain_in_file(file_path):
    """更新单个文件中的域名引用"""
    print(f"正在更新域名: {file_path}")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 更新各种域名引用
    replacements = [
        # 绝对路径URL
        (r'https://www\.seodog\.cn', 'https://aiagentbox.com'),
        (r'https://seodog\.cn', 'https://aiagentbox.com'),
        (r'http://www\.seodog\.cn', 'https://aiagentbox.com'),
        (r'http://seodog\.cn', 'https://aiagentbox.com'),
        
        # 相对路径（保持相对路径）
        (r'href="https://www\.seodog\.cn"', 'href="index.html"'),
        (r'href="https://seodog\.cn"', 'href="index.html"'),
        
        # 邮箱地址
        (r'contact@seodog\.cn', 'contact@aiagentbox.com'),
        (r'admin@seodog\.cn', 'admin@aiagentbox.com'),
        
        # 文本中的域名引用
        (r'seodog\.cn', 'aiagentbox.com'),
        (r'www\.seodog\.cn', 'aiagentbox.com'),
        
        # 结构化数据中的URL
        (r'"url": "https://www\.seodog\.cn"', '"url": "https://aiagentbox.com"'),
        (r'"url": "https://seodog\.cn"', '"url": "https://aiagentbox.com"'),
        
        # Open Graph标签
        (r'<meta property="og:url" content="https://www\.seodog\.cn', '<meta property="og:url" content="https://aiagentbox.com'),
        (r'<meta property="og:url" content="https://seodog\.cn', '<meta property="og:url" content="https://aiagentbox.com'),
        
        # 规范链接
        (r'<link rel="canonical" href="https://www\.seodog\.cn', '<link rel="canonical" href="https://aiagentbox.com'),
        (r'<link rel="canonical" href="https://seodog\.cn', '<link rel="canonical" href="https://aiagentbox.com'),
        
        # Twitter Card
        (r'<meta name="twitter:url" content="https://www\.seodog\.cn', '<meta name="twitter:url" content="https://aiagentbox.com'),
        (r'<meta name="twitter:url" content="https://seodog\.cn', '<meta name="twitter:url" content="https://aiagentbox.com'),
    ]
    
    for old_pattern, new_pattern in replacements:
        content = re.sub(old_pattern, new_pattern, content, flags=re.IGNORECASE)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ 域名更新完成: {file_path}")

def update_sitemap_domain():
    """更新sitemap.xml中的域名"""
    sitemap_file = Path('sitemap.xml')
    if sitemap_file.exists():
        print(f"正在更新sitemap域名: {sitemap_file}")
        
        with open(sitemap_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 更新sitemap中的域名
        content = re.sub(r'https://aiagentbox\.org', 'https://aiagentbox.com', content)
        
        with open(sitemap_file, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ sitemap域名更新完成: {sitemap_file}")

def update_robots_domain():
    """更新robots.txt中的域名"""
    robots_file = Path('robots.txt')
    if robots_file.exists():
        print(f"正在更新robots域名: {robots_file}")
        
        with open(robots_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 更新robots.txt中的域名
        content = re.sub(r'https://aiagentbox\.org', 'https://aiagentbox.com', content)
        
        with open(robots_file, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ robots域名更新完成: {robots_file}")

def main():
    """主函数"""
    # 获取当前目录
    current_dir = Path('.')
    
    # 查找所有HTML文件
    html_files = list(current_dir.glob('*.html'))
    
    print(f"找到 {len(html_files)} 个HTML文件")
    print("开始更新域名...")
    
    # 更新每个HTML文件
    for html_file in html_files:
        try:
            update_domain_in_file(html_file)
        except Exception as e:
            print(f"❌ 更新失败 {html_file}: {e}")
    
    # 更新sitemap和robots文件
    update_sitemap_domain()
    update_robots_domain()
    
    print("\n🎉 域名更新完成！")
    print("\n更新内容包括：")
    print("✅ 所有HTML文件中的域名引用")
    print("✅ sitemap.xml中的域名")
    print("✅ robots.txt中的域名")
    print("✅ 邮箱地址")
    print("✅ 结构化数据中的URL")
    print("✅ Open Graph和Twitter Card标签")

if __name__ == "__main__":
    main()
