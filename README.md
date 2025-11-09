# Threads 爬蟲 - 中山醫學大學

這是一個自動化爬蟲程式，用於抓取 Threads 平台上有關中山醫學大學的貼文。

## 功能特色

- 🔍 自動搜尋 Threads 上的關鍵字貼文
- 📊 將結果儲存為 JSON 格式
- ⚙️ 可自訂搜尋關鍵字和抓取數量
- 🤖 使用 Selenium 模擬真實瀏覽器行為
- 📝 詳細的執行日誌

## 系統需求

- Python 3.8 或更高版本
- Chrome 瀏覽器（用於 Selenium WebDriver）
- 穩定的網路連線

## 安裝步驟

1. **克隆或下載此專案**

```bash
git clone <repository-url>
cd threads
```

2. **建立虛擬環境（建議）**

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

3. **安裝依賴套件**

```bash
pip install -r requirements.txt
```

4. **設定環境變數**

複製 `.env.example` 為 `.env` 並根據需求修改：

```bash
cp .env.example .env
```

編輯 `.env` 檔案：

```env
SEARCH_KEYWORD=中山醫學大學
MAX_POSTS=50
OUTPUT_FILE=threads_posts.json
```

## 使用方法

### 基本使用

```bash
python threads_crawler.py
```

### 自訂參數

修改 `.env` 檔案中的參數：

- `SEARCH_KEYWORD`: 搜尋關鍵字（預設：中山醫學大學）
- `MAX_POSTS`: 最大抓取貼文數量（預設：50）
- `OUTPUT_FILE`: 輸出檔案名稱（預設：threads_posts.json）

### 範例

搜尋「中山醫學大學」並抓取最多 100 篇貼文：

```env
SEARCH_KEYWORD=中山醫學大學
MAX_POSTS=100
OUTPUT_FILE=csmu_threads.json
```

然後執行：

```bash
python threads_crawler.py
```

## 輸出格式

程式會產生一個 JSON 檔案，包含以下資訊：

```json
{
  "keyword": "中山醫學大學",
  "total_posts": 50,
  "crawl_time": "2025-11-09T12:00:00",
  "posts": [
    {
      "id": 1,
      "text": "貼文內容...",
      "timestamp": "2025-11-09T12:00:00",
      "keyword": "中山醫學大學"
    }
  ]
}
```

## 注意事項

⚠️ **重要提醒**

1. **使用限制**: 此爬蟲僅用於學術研究和個人學習用途
2. **頻率控制**: 請勿過於頻繁執行，以免對 Threads 伺服器造成負擔
3. **服務條款**: 使用前請確認符合 Threads 的服務條款
4. **資料隱私**: 抓取的資料請妥善保管，不要公開或濫用

## 常見問題

### Q: 爬蟲無法抓取到資料？

A: 可能的原因：
- Threads 的 DOM 結構已更新（需要更新選擇器）
- 網路連線問題
- 需要登入才能查看內容

### Q: 如何增加抓取速度？

A: 可以調整以下參數：
- 減少 `time.sleep()` 的等待時間
- 增加滾動次數

### Q: 支援其他關鍵字嗎？

A: 是的！只需修改 `.env` 檔案中的 `SEARCH_KEYWORD` 參數即可。

## 技術架構

- **Selenium**: 網頁自動化框架
- **BeautifulSoup4**: HTML 解析
- **Requests**: HTTP 請求
- **WebDriver Manager**: 自動管理瀏覽器驅動

## 未來改進

- [ ] 支援多關鍵字搜尋
- [ ] 加入貼文時間、作者等詳細資訊
- [ ] 支援匯出為 CSV、Excel 格式
- [ ] 加入排程自動執行功能
- [ ] 支援代理伺服器設定
- [ ] 加入圖片下載功能

## 授權

MIT License

## 聯絡方式

如有問題或建議，歡迎提出 Issue。

---

**免責聲明**: 此工具僅供教育和研究用途。使用者應自行確保遵守相關法律法規和平台服務條款。
