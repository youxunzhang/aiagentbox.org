#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
批量更新所有HTML页面的导航菜单
使其与首页保持一致
"""

import os
import re
from pathlib import Path

# 统一的导航菜单HTML（桌面端）
DESKTOP_NAV = '''                <div class="hidden md:flex items-center space-x-4 desktop-menu">
                    <a href="https://www.seodog.cn" class="text-blue-600 hover:underline text-sm font-semibold">首页</a>
                    <a href="img.html" class="text-blue-600 hover:underline text-sm font-semibold">AI图片</a>

                    <a href="words.html" class="text-blue-600 hover:underline text-sm font-semibold">AI文字</a>
                    <a href="chuhai.html" class="text-blue-600 hover:underline text-sm font-semibold">AI出海</a>
                    <a href="music.html" class="text-blue-600 hover:underline text-sm font-semibold">AI音乐</a>
                    <a href="designer.html" class="text-blue-600 hover:underline text-sm font-semibold">AI设计师</a>
                    <a href="ainum.html" class="text-blue-600 hover:underline text-sm font-semibold">AI数字人</a>
                    <a href="aiprompt.html" class="text-blue-600 hover:underline text-sm font-semibold">AI提示词</a>
                    <a href="ailearn.html" class="text-blue-600 hover:underline text-sm font-semibold">AI学习</a>
                    <a href="aioffice.html" class="text-blue-600 hover:underline text-sm font-semibold">AI办公</a>
                                                   <a href="aiagent.html" class="text-blue-600 hover:underline text-sm font-semibold">AI智能体</a>
                               <a href="aitimer.html" class="text-blue-600 hover:underline text-sm font-semibold">AI计时器</a>
                    <a href="aicommunity.html" class="text-blue-600 hover:underline text-sm font-semibold">AI社群</a>
                    <a href="social.html" class="text-blue-600 hover:underline text-sm font-semibold">社交媒体</a>
                    <a href="sitemap.html" class="text-blue-600 hover:underline text-sm font-semibold">网站地图</a>
                </div>'''

# 移动端导航菜单HTML
MOBILE_NAV = '''    <!-- Mobile Navigation -->
    <nav class="mobile-nav" id="mobileNav">
        <div class="mobile-nav-content">
            <a href="https://www.seodog.cn" onclick="closeMobileMenu()">首页</a>
                          <a href="img.html" onclick="closeMobileMenu()">AI图片</a>
              
              <a href="words.html" onclick="closeMobileMenu()">AI文字</a>
              <a href="chuhai.html" onclick="closeMobileMenu()">AI出海</a>
            <a href="music.html" onclick="closeMobileMenu()">AI音乐</a>
            <a href="designer.html" onclick="closeMobileMenu()">AI设计师</a>
            <a href="ainum.html" onclick="closeMobileMenu()">AI数字人</a>
            <a href="aiprompt.html" onclick="closeMobileMenu()">AI提示词</a>
            <a href="ailearn.html" onclick="closeMobileMenu()">AI学习</a>
            <a href="aioffice.html" onclick="closeMobileMenu()">AI办公</a>
                           <a href="aiagent.html" onclick="closeMobileMenu()">AI智能体</a>
               <a href="aitimer.html" onclick="closeMobileMenu()">AI计时器</a>
            <a href="aicommunity.html" onclick="closeMobileMenu()">AI社群</a>
            <a href="social.html" onclick="closeMobileMenu()">社交媒体</a>
            <a href="sitemap.html" onclick="closeMobileMenu()">网站地图</a>
        </div>
    </nav>'''

# 移动端导航CSS样式
MOBILE_NAV_CSS = '''        .mobile-nav {
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: rgba(255, 255, 255, 0.98);
            backdrop-filter: blur(20px);
            z-index: 40;
            transform: translateX(-100%);
            transition: transform 0.3s ease;
        }
        
        .mobile-nav.active {
            transform: translateX(0);
        }
        
        .mobile-nav-content {
            padding: 5rem 2rem 2rem;
            height: 100%;
            overflow-y: auto;
        }
        
        .mobile-nav a {
            display: block;
            padding: 1rem 0;
            font-size: 1.1rem;
            font-weight: 600;
            color: #374151;
            border-bottom: 1px solid #E5E7EB;
            transition: color 0.3s ease;
        }
        
        .mobile-nav a:hover {
            color: #3B82F6;
        }'''

# 移动端菜单JavaScript
MOBILE_NAV_JS = '''    <script>
        // 移动端菜单功能
        const mobileMenuButton = document.getElementById('mobileMenuButton');
        const mobileNav = document.getElementById('mobileNav');
        const body = document.body;

        function toggleMobileMenu() {
            mobileMenuButton.classList.toggle('active');
            mobileNav.classList.toggle('active');
            body.style.overflow = mobileNav.classList.contains('active') ? 'hidden' : '';
        }

        function closeMobileMenu() {
            mobileMenuButton.classList.remove('active');
            mobileNav.classList.remove('active');
            body.style.overflow = '';
        }

        mobileMenuButton.addEventListener('click', toggleMobileMenu);

        // 点击菜单外部关闭菜单
        mobileNav.addEventListener('click', function(e) {
            if (e.target === mobileNav) {
                closeMobileMenu();
            }
        });

        // 监听窗口大小变化，在大屏幕时关闭移动菜单
        window.addEventListener('resize', function() {
            if (window.innerWidth >= 768) {
                closeMobileMenu();
            }
        });

        // 触摸手势支持
        let touchStartX = 0;
        let touchEndX = 0;

        mobileNav.addEventListener('touchstart', function(e) {
            touchStartX = e.changedTouches[0].screenX;
        });

        mobileNav.addEventListener('touchend', function(e) {
            touchEndX = e.changedTouches[0].screenX;
            handleSwipe();
        });

        function handleSwipe() {
            const swipeThreshold = 50;
            const diff = touchStartX - touchEndX;
            
            if (Math.abs(diff) > swipeThreshold) {
                if (diff > 0) {
                    // 向左滑动，关闭菜单
                    closeMobileMenu();
                }
            }
        }
    </script>'''

def update_navigation_in_file(file_path):
    """更新单个文件的导航菜单"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # 1. 更新桌面端导航菜单
        # 查找并替换桌面端导航
        desktop_nav_pattern = r'<div class="hidden md:flex items-center space-x-4[^>]*>.*?</div>'
        if re.search(desktop_nav_pattern, content, re.DOTALL):
            content = re.sub(desktop_nav_pattern, DESKTOP_NAV, content, flags=re.DOTALL)
        else:
            # 如果没有找到，尝试查找更简单的模式
            simple_nav_pattern = r'<div class="hidden md:flex[^>]*>.*?</div>'
            if re.search(simple_nav_pattern, content, re.DOTALL):
                content = re.sub(simple_nav_pattern, DESKTOP_NAV, content, flags=re.DOTALL)
        
        # 2. 添加移动端菜单按钮（如果不存在）
        if 'mobile-menu-button' not in content:
            # 在桌面端导航后添加移动端按钮
            button_pattern = r'(</div>\s*</div>\s*</div>\s*</header>)'
            mobile_button = '''                <button class="mobile-menu-button md:hidden" id="mobileMenuButton">
                    <span></span>
                    <span></span>
                    <span></span>
                </button>
            </div>
        </div>
    </header>'''
            content = re.sub(button_pattern, mobile_button, content)
        
        # 3. 添加移动端导航菜单（如果不存在）
        if 'mobile-nav' not in content:
            # 在header后添加移动端导航
            header_pattern = r'(</header>)'
            content = re.sub(header_pattern, f'\\1\n\n{MOBILE_NAV}', content)
        
        # 4. 添加移动端导航CSS样式（如果不存在）
        if 'mobile-nav' not in content or '.mobile-nav' not in content:
            # 在</style>前添加CSS
            style_pattern = r'(</style>)'
            content = re.sub(style_pattern, f'{MOBILE_NAV_CSS}\n    </style>', content)
        
        # 5. 添加移动端导航JavaScript（如果不存在）
        if 'mobileMenuButton' not in content or 'toggleMobileMenu' not in content:
            # 在</body>前添加JavaScript
            body_pattern = r'(</body>)'
            content = re.sub(body_pattern, f'{MOBILE_NAV_JS}\n</body>', content)
        
        # 如果内容有变化，写回文件
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ 已更新: {file_path}")
            return True
        else:
            print(f"⏭️  无需更新: {file_path}")
            return False
            
    except Exception as e:
        print(f"❌ 更新失败 {file_path}: {str(e)}")
        return False

def main():
    """主函数"""
    # 获取当前目录下的所有HTML文件
    html_files = []
    for file in os.listdir('.'):
        if file.endswith('.html') and file != 'index.html':  # 跳过首页
            html_files.append(file)
    
    print(f"找到 {len(html_files)} 个HTML文件需要更新导航菜单")
    print("=" * 50)
    
    updated_count = 0
    for file_path in html_files:
        if update_navigation_in_file(file_path):
            updated_count += 1
    
    print("=" * 50)
    print(f"更新完成！共更新了 {updated_count} 个文件")

if __name__ == "__main__":
    main() 