#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AI工具LOGO优化脚本
将首页AI工具的LOGO从emoji和简单文字优化为更美观的图标展示
"""

import re
import os

def optimize_tool_logos(file_path):
    """优化AI工具LOGO展示"""
    print(f"正在优化LOGO: {file_path}")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 定义LOGO优化映射
    logo_updates = {
        # 大模型
        r'<div class="tool-logo" style="background: linear-gradient\(135deg, var\(--neon-blue\), var\(--neon-cyan\)\);">豆</div>': 
        '<div class="tool-logo" style="background: linear-gradient(135deg, #FF6B6B, #FF8E53);">🫘</div>',
        
        r'<div class="tool-logo" style="background: linear-gradient\(135deg, var\(--neon-purple\), var\(--neon-pink\)\);">D</div>': 
        '<div class="tool-logo" style="background: linear-gradient(135deg, #8B5CF6, #7C3AED);">🔍</div>',
        
        r'<div class="tool-logo" style="background: linear-gradient\(135deg, var\(--neon-cyan\), var\(--neon-blue\)\);">G</div>': 
        '<div class="tool-logo" style="background: linear-gradient(135deg, #4285F4, #34A853);">🌐</div>',
        
        r'<div class="tool-logo" style="background: linear-gradient\(135deg, var\(--neon-pink\), var\(--neon-purple\)\);">P</div>': 
        '<div class="tool-logo" style="background: linear-gradient(135deg, #EC4899, #8B5CF6);">💡</div>',
        
        r'<div class="tool-logo" style="background: linear-gradient\(135deg, var\(--neon-blue\), var\(--neon-purple\)\);">🤖</div>': 
        '<div class="tool-logo" style="background: linear-gradient(135deg, #10B981, #8B5CF6);">🤖</div>',
        
        r'<div class="tool-logo" style="background: linear-gradient\(135deg, var\(--neon-pink\), var\(--neon-cyan\)\);">🧠</div>': 
        '<div class="tool-logo" style="background: linear-gradient(135deg, #F59E0B, #06B6D4);">🧠</div>',
        
        r'<div class="tool-logo" style="background: linear-gradient\(135deg, var\(--neon-blue\), var\(--neon-purple\)\);">🚀</div>': 
        '<div class="tool-logo" style="background: linear-gradient(135deg, #EF4444, #8B5CF6);">🚀</div>',
        
        # 国产AI产品
        r'<div class="tool-logo" style="background: linear-gradient\(135deg, #FF6B6B, #FF8E53\);">即</div>': 
        '<div class="tool-logo" style="background: linear-gradient(135deg, #FF6B6B, #FF8E53);">💭</div>',
        
        r'<div class="tool-logo" style="background: linear-gradient\(135deg, #4ECDC4, #44A08D\);">可</div>': 
        '<div class="tool-logo" style="background: linear-gradient(135deg, #4ECDC4, #44A08D);">✨</div>',
        
        r'<div class="tool-logo" style="background: linear-gradient\(135deg, #A8E6CF, #7FCDCD\);">智</div>': 
        '<div class="tool-logo" style="background: linear-gradient(135deg, #A8E6CF, #7FCDCD);">🧠</div>',
        
        r'<div class="tool-logo" style="background: linear-gradient\(135deg, #2932E1, #1E40AF\);">文</div>': 
        '<div class="tool-logo" style="background: linear-gradient(135deg, #2932E1, #1E40AF);">📝</div>',
        
        r'<div class="tool-logo" style="background: linear-gradient\(135deg, #FF6B35, #F7931E\);">通</div>': 
        '<div class="tool-logo" style="background: linear-gradient(135deg, #FF6B35, #F7931E);">🔗</div>',
        
        r'<div class="tool-logo" style="background: linear-gradient\(135deg, #00A651, #008F3A\);">星</div>': 
        '<div class="tool-logo" style="background: linear-gradient(135deg, #00A651, #008F3A);">⭐</div>',
        
        r'<div class="tool-logo" style="background: linear-gradient\(135deg, #667eea, #764ba2\);">月</div>': 
        '<div class="tool-logo" style="background: linear-gradient(135deg, #667eea, #764ba2);">🌙</div>',
        
        r'<div class="tool-logo" style="background: linear-gradient\(135deg, #00C851, #007E33\);">智</div>': 
        '<div class="tool-logo" style="background: linear-gradient(135deg, #00C851, #007E33);">🛡️</div>',
        
        r'<div class="tool-logo" style="background: linear-gradient\(135deg, #FF6B6B, #FF8E53\);">讯</div>': 
        '<div class="tool-logo" style="background: linear-gradient(135deg, #FF6B6B, #FF8E53);">🎤</div>',
        
        # 聊天模型
        r'<div class="tool-logo" style="background: linear-gradient\(135deg, var\(--neon-blue\), var\(--neon-purple\)\);">🏛️</div>': 
        '<div class="tool-logo" style="background: linear-gradient(135deg, #3B82F6, #8B5CF6);">🏛️</div>',
        
        r'<div class="tool-logo" style="background: linear-gradient\(135deg, var\(--neon-pink\), var\(--neon-cyan\)\);">💭</div>': 
        '<div class="tool-logo" style="background: linear-gradient(135deg, #EC4899, #06B6D4);">💭</div>',
        
        # 聚合模型
        r'<div class="tool-logo" style="background: linear-gradient\(135deg, #3B82F6, #1D4ED8\);">🔗</div>': 
        '<div class="tool-logo" style="background: linear-gradient(135deg, #3B82F6, #1D4ED8);">🔗</div>',
        
        r'<div class="tool-logo" style="background: linear-gradient\(135deg, #8B5CF6, #7C3AED\);">💬</div>': 
        '<div class="tool-logo" style="background: linear-gradient(135deg, #8B5CF6, #7C3AED);">💬</div>',
        
        r'<div class="tool-logo" style="background: linear-gradient\(135deg, #10B981, #059669\);">🔄</div>': 
        '<div class="tool-logo" style="background: linear-gradient(135deg, #10B981, #059669);">🔄</div>',
        
        r'<div class="tool-logo" style="background: linear-gradient\(135deg, #F59E0B, #D97706\);">G</div>': 
        '<div class="tool-logo" style="background: linear-gradient(135deg, #F59E0B, #D97706);">🛒</div>',
        
        r'<div class="tool-logo" style="background: linear-gradient\(135deg, #EF4444, #DC2626\);">U</div>': 
        '<div class="tool-logo" style="background: linear-gradient(135deg, #EF4444, #DC2626);">📋</div>',
        
        r'<div class="tool-logo" style="background: linear-gradient\(135deg, #06B6D4, #0891B2\);">M</div>': 
        '<div class="tool-logo" style="background: linear-gradient(135deg, #06B6D4, #0891B2);">🧠</div>',
        
        r'<div class="tool-logo" style="background: linear-gradient\(135deg, #EC4899, #DB2777\);">Q</div>': 
        '<div class="tool-logo" style="background: linear-gradient(135deg, #EC4899, #DB2777);">❓</div>',
        
        r'<div class="tool-logo" style="background: linear-gradient\(135deg, #8B5CF6, #7C3AED\);">S</div>': 
        '<div class="tool-logo" style="background: linear-gradient(135deg, #8B5CF6, #7C3AED);">🙏</div>',
        
        r'<div class="tool-logo" style="background: linear-gradient\(135deg, #3B82F6, #1D4ED8\);">S</div>': 
        '<div class="tool-logo" style="background: linear-gradient(135deg, #3B82F6, #1D4ED8);">🤝</div>',
        
        r'<div class="tool-logo" style="background: linear-gradient\(135deg, #F59E0B, #D97706\);">Y</div>': 
        '<div class="tool-logo" style="background: linear-gradient(135deg, #F59E0B, #D97706);">🖨️</div>',
        
        r'<div class="tool-logo" style="background: linear-gradient\(135deg, #EF4444, #DC2626\);">T</div>': 
        '<div class="tool-logo" style="background: linear-gradient(135deg, #EF4444, #DC2626);">🎨</div>',
        
        r'<div class="tool-logo" style="background: linear-gradient\(135deg, #06B6D4, #0891B2\);">W</div>': 
        '<div class="tool-logo" style="background: linear-gradient(135deg, #06B6D4, #0891B2);">⚡</div>',
        
        r'<div class="tool-logo" style="background: linear-gradient\(135deg, #8B5CF6, #7C3AED\);">V</div>': 
        '<div class="tool-logo" style="background: linear-gradient(135deg, #8B5CF6, #7C3AED);">🎯</div>',
        
        r'<div class="tool-logo" style="background: linear-gradient\(135deg, #EC4899, #DB2777\);">J</div>': 
        '<div class="tool-logo" style="background: linear-gradient(135deg, #EC4899, #DB2777);">🧬</div>',
        
        r'<div class="tool-logo" style="background: linear-gradient\(135deg, #E4405F, #C13584\);">I</div>': 
        '<div class="tool-logo" style="background: linear-gradient(135deg, #E4405F, #C13584);">📱</div>',
        
        r'<div class="tool-logo" style="background: linear-gradient\(135deg, #10B981, #059669\);">M</div>': 
        '<div class="tool-logo" style="background: linear-gradient(135deg, #10B981, #059669);">🎵</div>',
        
        # 图片处理
        r'<div class="tool-logo" style="background: linear-gradient\(135deg, #06B6D4, #0891B2\);">🖼️</div>': 
        '<div class="tool-logo" style="background: linear-gradient(135deg, #06B6D4, #0891B2);">🖼️</div>',
        
        r'<div class="tool-logo" style="background: linear-gradient\(135deg, #F97316, #EA580C\);">🎨</div>': 
        '<div class="tool-logo" style="background: linear-gradient(135deg, #F97316, #EA580C);">🎨</div>',
        
        r'<div class="tool-logo" style="background: linear-gradient\(135deg, #8B5CF6, #7C3AED\);">🔍</div>': 
        '<div class="tool-logo" style="background: linear-gradient(135deg, #8B5CF6, #7C3AED);">🔍</div>',
        
        r'<div class="tool-logo" style="background: linear-gradient\(135deg, #10B981, #059669\);">✂️</div>': 
        '<div class="tool-logo" style="background: linear-gradient(135deg, #10B981, #059669);">✂️</div>',
        
        r'<div class="tool-logo" style="background: linear-gradient\(135deg, var\(--neon-cyan\), var\(--neon-blue\)\);">📸</div>': 
        '<div class="tool-logo" style="background: linear-gradient(135deg, #06B6D4, #3B82F6);">📸</div>',
        
        r'<div class="tool-logo" style="background: linear-gradient\(135deg, #F59E0B, #D97706\);">🎭</div>': 
        '<div class="tool-logo" style="background: linear-gradient(135deg, #F59E0B, #D97706);">🎭</div>',
        
        r'<div class="tool-logo" style="background: linear-gradient\(135deg, #EF4444, #DC2626\);">💭</div>': 
        '<div class="tool-logo" style="background: linear-gradient(135deg, #EF4444, #DC2626);">💭</div>',
        
        # 视频处理
        r'<div class="tool-logo" style="background: linear-gradient\(135deg, #3B82F6, #1D4ED8\);">🎥</div>': 
        '<div class="tool-logo" style="background: linear-gradient(135deg, #3B82F6, #1D4ED8);">🎥</div>',
    }
    
    # 应用所有LOGO更新
    for old_logo, new_logo in logo_updates.items():
        content = re.sub(old_logo, new_logo, content)
    
    # 优化tool-logo的CSS样式
    content = re.sub(
        r'\.tool-logo\s*\{[^}]*\}',
        '''.tool-logo {
            width: 60px;
            height: 60px;
            border-radius: 16px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 24px;
            font-weight: bold;
            color: white;
            margin-bottom: 12px;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.12);
            border: 2px solid rgba(255, 255, 255, 0.2);
            backdrop-filter: blur(10px);
            transition: all 0.3s ease;
        }''',
        content
    )
    
    # 添加悬停效果
    content = re.sub(
        r'\.tool-card:hover\s*\{[^}]*\}',
        '''.tool-card:hover {
            transform: translateY(-8px);
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.15);
        }
        
        .tool-card:hover .tool-logo {
            transform: scale(1.1);
            box-shadow: 0 12px 40px rgba(0, 0, 0, 0.2);
        }''',
        content
    )
    
    # 保存更新后的内容
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ LOGO优化完成: {file_path}")

def main():
    """主函数"""
    print("🚀 开始优化AI工具LOGO...")
    
    # 优化首页
    if os.path.exists('index.html'):
        optimize_tool_logos('index.html')
    
    print("🎉 所有LOGO优化完成！")

if __name__ == "__main__":
    main()
