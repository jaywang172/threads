#!/bin/bash

# 啟動虛擬環境
if [ -d "venv" ]; then
    source venv/bin/activate
    echo "✓ 虛擬環境已啟動"
else
    echo "✗ 請先執行 ./setup.sh 安裝環境"
    exit 1
fi

# 執行爬蟲
echo "開始執行 Threads 爬蟲..."
python threads_crawler.py

# 顯示結果
if [ -f "threads_posts.json" ]; then
    echo ""
    echo "======================================"
    echo "結果摘要："
    python -c "import json; data=json.load(open('threads_posts.json')); print(f'關鍵字: {data[\"keyword\"]}'); print(f'總貼文數: {data[\"total_posts\"]}'); print(f'抓取時間: {data[\"crawl_time\"]}')"
    echo "======================================"
fi
