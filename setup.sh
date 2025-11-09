#!/bin/bash

echo "======================================"
echo "Threads 爬蟲安裝腳本"
echo "======================================"
echo ""

# 檢查 Python 版本
echo "[1/5] 檢查 Python 版本..."
python_version=$(python3 --version 2>&1 | awk '{print $2}')
echo "✓ Python 版本: $python_version"
echo ""

# 建立虛擬環境
echo "[2/5] 建立虛擬環境..."
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo "✓ 虛擬環境已建立"
else
    echo "✓ 虛擬環境已存在"
fi
echo ""

# 啟動虛擬環境並安裝依賴
echo "[3/5] 安裝依賴套件..."
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
echo "✓ 依賴套件安裝完成"
echo ""

# 設定環境變數
echo "[4/5] 設定環境變數..."
if [ ! -f ".env" ]; then
    cp .env.example .env
    echo "✓ .env 檔案已建立"
else
    echo "✓ .env 檔案已存在"
fi
echo ""

# 完成
echo "[5/5] 安裝完成！"
echo ""
echo "======================================"
echo "使用方法："
echo "1. 編輯 .env 檔案設定參數"
echo "2. 啟動虛擬環境: source venv/bin/activate"
echo "3. 執行爬蟲: python threads_crawler.py"
echo "======================================"
