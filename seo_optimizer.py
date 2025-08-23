#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SEO优化脚本 - 批量更新所有HTML文件的SEO元素
"""

import os
import re
from pathlib import Path
from datetime import datetime

def optimize_seo_metadata(file_path):
    """优化单个HTML文件的SEO元数据"""
    print(f"正在优化SEO: {file_path}")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 更新标题标签
    content = re.sub(
        r'<title>.*?</title>',
        '<title>AI工具导航 - 最全面的人工智能工具集合 | 免费AI工具大全 | ChatGPT、Midjourney、DALL-E</title>',
        content
    )
    
    # 更新描述标签
    content = re.sub(
        r'<meta name="description" content=".*?"',
        '<meta name="description" content="AI工具导航是专业的人工智能工具导航网站，收录1000+最全面的AI工具，包括ChatGPT、Midjourney、DALL-E、AI写作工具、AI绘画工具、AI视频工具、AI音频工具、AI办公工具、AI学习工具、AI设计工具、AI编程工具等，帮助您快速找到最适合的AI助手和工具，提升工作效率"',
        content
    )
    
    # 更新关键词标签
    content = re.sub(
        r'<meta name="keywords" content=".*?"',
        '<meta name="keywords" content="AI工具导航,人工智能工具导航,AI工具网站,AI导航,免费AI工具,人工智能工具,AI助手,大模型,ChatGPT,Midjourney,DALL-E,AI写作工具,AI绘画工具,AI视频工具,AI音频工具,AI办公工具,AI学习工具,AI设计工具,AI编程工具,AI图片处理,AI视频制作,AI文字处理,AI音乐工具,AI设计师工具,AI数字人,文心一言,通义千问"',
        content
    )
    
    # 添加规范链接
    if '<link rel="canonical"' not in content:
        content = re.sub(
            r'<head>',
            '<head>\n    <link rel="canonical" href="https://aiagentbox.org/">',
            content
        )
    
    # 添加Open Graph标签
    if '<meta property="og:title"' not in content:
        og_tags = '''
    <!-- Open Graph / Facebook -->
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://aiagentbox.org/">
    <meta property="og:title" content="AI工具导航 - 最全面的人工智能工具集合 | 免费AI工具大全">
    <meta property="og:description" content="AI工具导航是专业的人工智能工具导航网站，收录1000+最全面的AI工具，包括ChatGPT、Midjourney、DALL-E等，帮助您快速找到最适合的AI助手和工具">
    <meta property="og:image" content="https://aiagentbox.org/og-image.jpg">
    <meta property="og:image:width" content="1200">
    <meta property="og:image:height" content="630">
    <meta property="og:site_name" content="AI工具导航">
    <meta property="og:locale" content="zh_CN">'''
        content = re.sub(
            r'<meta name="keywords".*?>',
            r'\g<0>' + og_tags,
            content
        )
    
    # 添加Twitter Card标签
    if '<meta name="twitter:card"' not in content:
        twitter_tags = '''
    <!-- Twitter -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:url" content="https://aiagentbox.org/">
    <meta name="twitter:title" content="AI工具导航 - 最全面的人工智能工具集合">
    <meta name="twitter:description" content="AI工具导航是专业的人工智能工具导航网站，收录1000+最全面的AI工具">
    <meta name="twitter:image" content="https://aiagentbox.org/twitter-image.jpg">'''
        content = re.sub(
            r'<meta property="og:locale".*?>',
            r'\g<0>' + twitter_tags,
            content
        )
    
    # 添加结构化数据
    if 'application/ld+json' not in content:
        structured_data = '''
    <!-- 结构化数据 -->
    <script type="application/ld+json">
    {
        "@context": "https://schema.org",
        "@type": "WebSite",
        "name": "AI工具导航",
        "description": "最全面的人工智能工具导航网站，收录1000+AI工具",
        "url": "https://aiagentbox.org",
        "potentialAction": {
            "@type": "SearchAction",
            "target": "https://aiagentbox.org/search?q={search_term_string}",
            "query-input": "required name=search_term_string"
        }
    }
    </script>'''
        content = re.sub(
            r'</head>',
            structured_data + '\n</head>',
            content
        )
    
    # 优化H1-H6标签
    content = re.sub(
        r'<h1[^>]*>AI工具导航</h1>',
        '<h1 class="gradient-text text-5xl md:text-7xl font-bold mb-6 leading-tight">AI工具导航</h1>',
        content
    )
    
    # 添加alt属性到图片
    content = re.sub(
        r'<img([^>]*?)>',
        r'<img\1 alt="AI工具导航">',
        content
    )
    
    # 添加nofollow到外部链接
    content = re.sub(
        r'<a href="https://([^"]*)"([^>]*?)>',
        r'<a href="https://\1"\2 rel="nofollow">',
        content
    )
    
    # 添加更新时间
    current_time = datetime.now().strftime("%Y-%m-%d")
    content = re.sub(
        r'<meta name="author" content="AI工具导航">',
        f'<meta name="author" content="AI工具导航">\n    <meta name="last-modified" content="{current_time}">',
        content
    )
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ SEO优化完成: {file_path}")

def add_internal_links(content):
    """添加内部链接"""
    # 添加相关页面链接
    internal_links = '''
    <!-- 相关页面链接 -->
    <div class="related-pages mt-8">
        <h3 class="text-lg font-semibold mb-4">相关页面</h3>
        <div class="grid grid-cols-2 md:grid-cols-4 gap-4">
            <a href="img.html" class="text-blue-600 hover:underline">AI图片处理</a>
            <a href="words.html" class="text-blue-600 hover:underline">AI写作工具</a>
            <a href="music.html" class="text-blue-600 hover:underline">AI音乐制作</a>
            <a href="designer.html" class="text-blue-600 hover:underline">AI设计工具</a>
        </div>
    </div>'''
    
    return content.replace('</main>', internal_links + '\n</main>')

def optimize_content_structure(file_path):
    """优化内容结构"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 添加更多H2、H3标签
    content = re.sub(
        r'<h2>([^<]+)</h2>',
        r'<h2 class="text-2xl font-bold mb-6 text-gray-800">\1</h2>',
        content
    )
    
    content = re.sub(
        r'<h3>([^<]+)</h3>',
        r'<h3 class="text-xl font-semibold mb-4 text-gray-700">\1</h3>',
        content
    )
    
    # 添加内部链接
    content = add_internal_links(content)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

def main():
    """主函数"""
    # 获取当前目录
    current_dir = Path('.')
    
    # 查找所有HTML文件
    html_files = list(current_dir.glob('*.html'))
    
    print(f"找到 {len(html_files)} 个HTML文件")
    print("开始SEO优化...")
    
    # 优化每个文件
    for html_file in html_files:
        try:
            optimize_seo_metadata(html_file)
            optimize_content_structure(html_file)
        except Exception as e:
            print(f"❌ 优化失败 {html_file}: {e}")
    
    print("\n🎉 SEO优化完成！")
    print("\n优化内容包括：")
    print("✅ 元数据优化（标题、描述、关键词）")
    print("✅ Open Graph标签")
    print("✅ Twitter Card标签")
    print("✅ 结构化数据")
    print("✅ 规范链接")
    print("✅ 内部链接优化")
    print("✅ 图片alt属性")
    print("✅ 外部链接nofollow")
    print("✅ 内容结构优化")

if __name__ == "__main__":
    main()
