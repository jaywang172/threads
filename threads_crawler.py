#!/usr/bin/env python3
"""
Threads 爬蟲 - 自動抓取中山醫學大學相關貼文
"""

import os
import json
import time
from datetime import datetime
from typing import List, Dict
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager


class ThreadsCrawler:
    """Threads 爬蟲類"""

    def __init__(self, keyword: str, max_posts: int = 50):
        """
        初始化爬蟲

        Args:
            keyword: 搜尋關鍵字
            max_posts: 最大抓取貼文數量
        """
        self.keyword = keyword
        self.max_posts = max_posts
        self.driver = None
        self.posts = []

    def setup_driver(self):
        """設定 Chrome WebDriver"""
        chrome_options = Options()
        chrome_options.add_argument('--headless')  # 無頭模式
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--window-size=1920,1080')
        chrome_options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')

        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        print(f"✓ WebDriver 已初始化")

    def search_threads(self):
        """在 Threads 上搜尋關鍵字"""
        try:
            # Threads 搜尋 URL（使用標籤搜尋）
            search_url = f"https://www.threads.net/search?q={self.keyword}"
            print(f"正在搜尋: {self.keyword}")
            print(f"訪問 URL: {search_url}")

            self.driver.get(search_url)
            time.sleep(5)  # 等待頁面載入

            # 滾動頁面以載入更多內容
            self._scroll_page()

            # 抓取貼文
            self._extract_posts()

        except Exception as e:
            print(f"✗ 搜尋時發生錯誤: {str(e)}")

    def _scroll_page(self, scroll_times: int = 5):
        """滾動頁面以載入更多內容"""
        for i in range(scroll_times):
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            print(f"滾動頁面 {i+1}/{scroll_times}")
            time.sleep(2)

    def _extract_posts(self):
        """提取貼文資訊"""
        try:
            # 等待內容載入
            time.sleep(3)

            # 獲取頁面 HTML
            page_source = self.driver.page_source

            # 嘗試找到貼文元素（Threads 的 DOM 結構可能會變化）
            # 這裡我們使用多種選擇器來提高成功率
            selectors = [
                '//article',
                '//div[@role="article"]',
                '//div[contains(@class, "x1lliihq")]'
            ]

            posts_found = []
            for selector in selectors:
                try:
                    elements = self.driver.find_elements(By.XPATH, selector)
                    if elements:
                        posts_found = elements
                        print(f"✓ 使用選擇器找到 {len(elements)} 個元素: {selector}")
                        break
                except:
                    continue

            if not posts_found:
                print("⚠ 未找到貼文元素，嘗試提取頁面文本內容")
                self._extract_text_content()
                return

            # 處理找到的元素
            for idx, element in enumerate(posts_found[:self.max_posts]):
                try:
                    post_data = {
                        'id': idx + 1,
                        'text': element.text if element.text else '',
                        'timestamp': datetime.now().isoformat(),
                        'keyword': self.keyword
                    }

                    if post_data['text']:
                        self.posts.append(post_data)
                        print(f"✓ 抓取貼文 {len(self.posts)}: {post_data['text'][:50]}...")

                except Exception as e:
                    print(f"提取貼文 {idx} 時發生錯誤: {str(e)}")
                    continue

        except Exception as e:
            print(f"✗ 提取貼文時發生錯誤: {str(e)}")

    def _extract_text_content(self):
        """提取頁面的文本內容作為備用方案"""
        try:
            body = self.driver.find_element(By.TAG_NAME, 'body')
            text_content = body.text

            # 將文本按行分割，過濾包含關鍵字的行
            lines = text_content.split('\n')
            relevant_lines = [line for line in lines if self.keyword in line and len(line.strip()) > 10]

            for idx, line in enumerate(relevant_lines[:self.max_posts]):
                post_data = {
                    'id': idx + 1,
                    'text': line.strip(),
                    'timestamp': datetime.now().isoformat(),
                    'keyword': self.keyword,
                    'source': 'text_extraction'
                }
                self.posts.append(post_data)
                print(f"✓ 提取文本 {len(self.posts)}: {line[:50]}...")

        except Exception as e:
            print(f"✗ 提取文本內容時發生錯誤: {str(e)}")

    def save_results(self, output_file: str):
        """儲存結果到 JSON 檔案"""
        try:
            result = {
                'keyword': self.keyword,
                'total_posts': len(self.posts),
                'crawl_time': datetime.now().isoformat(),
                'posts': self.posts
            }

            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(result, f, ensure_ascii=False, indent=2)

            print(f"✓ 結果已儲存到: {output_file}")
            print(f"✓ 總共抓取 {len(self.posts)} 篇貼文")

        except Exception as e:
            print(f"✗ 儲存結果時發生錯誤: {str(e)}")

    def close(self):
        """關閉瀏覽器"""
        if self.driver:
            self.driver.quit()
            print("✓ WebDriver 已關閉")

    def run(self, output_file: str):
        """執行爬蟲流程"""
        try:
            print("="*60)
            print(f"Threads 爬蟲啟動")
            print(f"搜尋關鍵字: {self.keyword}")
            print(f"最大貼文數: {self.max_posts}")
            print("="*60)

            self.setup_driver()
            self.search_threads()
            self.save_results(output_file)

            return True

        except Exception as e:
            print(f"✗ 執行爬蟲時發生錯誤: {str(e)}")
            return False

        finally:
            self.close()


def main():
    """主程式"""
    # 載入環境變數
    load_dotenv()

    # 讀取配置
    keyword = os.getenv('SEARCH_KEYWORD', '中山醫學大學')
    max_posts = int(os.getenv('MAX_POSTS', '50'))
    output_file = os.getenv('OUTPUT_FILE', 'threads_posts.json')

    # 建立並執行爬蟲
    crawler = ThreadsCrawler(keyword=keyword, max_posts=max_posts)
    success = crawler.run(output_file)

    if success:
        print("\n✓ 爬蟲執行完成！")
    else:
        print("\n✗ 爬蟲執行失敗")


if __name__ == '__main__':
    main()
