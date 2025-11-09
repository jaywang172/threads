# 快速開始指南

這份指南將幫助你在 5 分鐘內開始使用 Threads 爬蟲。

## 方法一：使用自動安裝腳本（推薦）

### Linux/Mac 使用者

```bash
# 1. 執行安裝腳本
./setup.sh

# 2. 編輯配置（可選）
nano .env

# 3. 執行爬蟲
./run.sh
```

### Windows 使用者

```bash
# 1. 建立虛擬環境
python -m venv venv

# 2. 啟動虛擬環境
venv\Scripts\activate

# 3. 安裝依賴
pip install -r requirements.txt

# 4. 複製環境變數檔案
copy .env.example .env

# 5. 執行爬蟲
python threads_crawler.py
```

## 方法二：手動安裝

### 步驟 1: 安裝依賴

```bash
pip install -r requirements.txt
```

### 步驟 2: 設定環境變數

```bash
cp .env.example .env
```

編輯 `.env` 檔案：

```env
SEARCH_KEYWORD=中山醫學大學
MAX_POSTS=50
OUTPUT_FILE=threads_posts.json
```

### 步驟 3: 執行爬蟲

```bash
python threads_crawler.py
```

## 查看結果

爬蟲執行完成後，會產生一個 JSON 檔案（預設為 `threads_posts.json`）：

```bash
# 使用 cat 查看原始內容
cat threads_posts.json

# 使用 jq 美化輸出（需先安裝 jq）
cat threads_posts.json | jq .

# 使用 Python 查看
python -m json.tool threads_posts.json
```

## 常見參數調整

### 搜尋不同關鍵字

編輯 `.env`：
```env
SEARCH_KEYWORD=醫學系
```

### 抓取更多貼文

編輯 `.env`：
```env
MAX_POSTS=100
```

### 自訂輸出檔名

編輯 `.env`：
```env
OUTPUT_FILE=my_results.json
```

## 疑難排解

### 問題：找不到 Chrome 驅動

**解決方案**：程式會自動下載，請確保有網路連線。

### 問題：無法抓取資料

**解決方案**：
1. 檢查網路連線
2. 確認 Chrome 瀏覽器已安裝
3. 嘗試增加等待時間（修改程式中的 `time.sleep()` 值）

### 問題：權限錯誤

**解決方案**：
```bash
chmod +x setup.sh run.sh
```

## 下一步

- 閱讀完整的 [README.md](README.md) 了解更多功能
- 客製化爬蟲參數以符合你的需求
- 查看輸出的 JSON 檔案分析資料

---

需要幫助？請查看 [README.md](README.md) 的常見問題章節。
