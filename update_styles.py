#!/usr/bin/env python3
import os
import re

# 新的样式定义
new_styles = '''    <style>
        :root {
            --primary-blue: #3B82F6;
            --primary-indigo: #6366F1;
            --primary-purple: #8B5CF6;
            --primary-pink: #EC4899;
            --primary-rose: #F43F5E;
            --primary-orange: #F97316;
            --primary-amber: #F59E0B;
            --primary-yellow: #EAB308;
            --primary-lime: #84CC16;
            --primary-green: #22C55E;
            --primary-emerald: #10B981;
            --primary-teal: #14B8A6;
            --primary-cyan: #06B6D4;
            --primary-sky: #0EA5E9;
            --gray-50: #F9FAFB;
            --gray-100: #F3F4F6;
            --gray-200: #E5E7EB;
            --gray-300: #D1D5DB;
            --gray-400: #9CA3AF;
            --gray-500: #6B7280;
            --gray-600: #4B5563;
            --gray-700: #374151;
            --gray-800: #1F2937;
            --gray-900: #111827;
        }
        
        body {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Helvetica Neue', Arial, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: var(--gray-900);
            line-height: 1.6;
        }
        
        .glass-effect {
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(20px);
            border: 1px solid rgba(255, 255, 255, 0.3);
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
        }
        
        .site-card, .tool-card, .link-card, .music-card, .game-card, .platform-card, .word-card, .sitemap-card, .apple-link {
            transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(20px);
            border: 1px solid rgba(255, 255, 255, 0.3);
            border-radius: 1rem;
            position: relative;
            overflow: hidden;
        }
        
        .site-card::before, .tool-card::before, .link-card::before, .music-card::before, .game-card::before, .platform-card::before, .word-card::before, .sitemap-card::before, .apple-link::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 3px;
            background: linear-gradient(90deg, var(--primary-blue), var(--primary-purple));
            transform: scaleX(0);
            transition: transform 0.3s ease;
        }
        
        .site-card:hover, .tool-card:hover, .link-card:hover, .music-card:hover, .game-card:hover, .platform-card:hover, .word-card:hover, .sitemap-card:hover, .apple-link:hover {
            transform: translateY(-8px) scale(1.02);
            box-shadow: 0 25px 50px rgba(0, 0, 0, 0.15);
            background: rgba(255, 255, 255, 0.98);
        }
        
        .site-card:hover::before, .tool-card:hover::before, .link-card:hover::before, .music-card:hover::before, .game-card:hover::before, .platform-card:hover::before, .word-card:hover::before, .sitemap-card:hover::before, .apple-link:hover::before {
            transform: scaleX(1);
        }
        
        .gradient-text {
            background: linear-gradient(135deg, var(--primary-blue), var(--primary-purple), var(--primary-pink));
            background-size: 200% 200%;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            animation: gradientShift 3s ease infinite;
        }
        
        @keyframes gradientShift {
            0%, 100% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
        }
        
        .floating-animation {
            animation: floating 6s ease-in-out infinite;
        }
        
        @keyframes floating {
            0%, 100% { transform: translateY(0px); }
            50% { transform: translateY(-10px); }
        }
        
        .section-container {
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(20px);
            border: 1px solid rgba(255, 255, 255, 0.3);
            border-radius: 1.5rem;
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
        }
        
        .fade-in {
            animation: fadeIn 0.8s cubic-bezier(0.4, 0, 0.2, 1);
        }
        
        @keyframes fadeIn {
            from { 
                opacity: 0; 
                transform: translateY(30px) scale(0.95); 
            }
            to { 
                opacity: 1; 
                transform: translateY(0) scale(1); 
            }
        }
        
        .stagger-animation {
            animation: staggerFadeIn 0.6s cubic-bezier(0.4, 0, 0.2, 1) forwards;
        }
        
        @keyframes staggerFadeIn {
            from { 
                opacity: 0; 
                transform: translateY(20px); 
            }
            to { 
                opacity: 1; 
                transform: translateY(0); 
            }
        }
        
        .category-header {
            background: linear-gradient(90deg, var(--primary-blue), var(--primary-purple));
            color: white;
            border-radius: 1rem 1rem 0 0;
        }
        
        .search-box {
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(20px);
            border: 2px solid rgba(59, 130, 246, 0.2);
            transition: all 0.3s ease;
            border-radius: 1rem;
        }
        
        .search-box:focus {
            border-color: var(--primary-blue);
            box-shadow: 0 0 0 4px rgba(59, 130, 246, 0.1);
        }
        
        @media (max-width: 768px) {
            .tool-card, .site-card, .link-card, .music-card, .game-card, .platform-card, .word-card, .sitemap-card, .apple-link { 
                margin-bottom: 12px; 
            }
        }
    </style>'''

# 需要更新的HTML文件列表
html_files = [
    'chuhai.html',
    'img.html'
]

def update_html_file(filename):
    """更新HTML文件的样式"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 查找并替换style标签
        style_pattern = r'<style>.*?</style>'
        if re.search(style_pattern, content, re.DOTALL):
            content = re.sub(style_pattern, new_styles, content, flags=re.DOTALL)
            print(f"✅ 已更新 {filename} 的样式")
        else:
            print(f"⚠️  {filename} 中未找到style标签")
        
        # 保存更新后的文件
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
            
    except Exception as e:
        print(f"❌ 更新 {filename} 时出错: {e}")

def main():
    print("🚀 开始批量更新HTML文件样式...")
    
    for filename in html_files:
        if os.path.exists(filename):
            update_html_file(filename)
        else:
            print(f"❌ 文件 {filename} 不存在")
    
    print("✨ 批量更新完成！")

if __name__ == "__main__":
    main() 