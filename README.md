# Casper_imageProcessing_APP

```markdown
# Casper 圖片處理工具

一個基於 Python 的 Web 圖片處理系統，整合基礎圖片處理和 AI 增強功能。

## 功能特點

### 基礎影像處理
- 調整圖片尺寸和比例
  - 支援自定義寬高
  - 保持原始比例選項
- 批次裁切功能
  - 1:1 正方形
  - 4:3 規格
  - 16:9 寬螢幕
- 基礎參數調整
  - 亮度
  - 對比度
  - 飽和度
  - 色溫
- 影像品質優化
  - 銳利度調整
  - 雜訊抑制
  - 瑕疵修復

### AI 智慧處理
- 自動去背
  - 智慧物件識別
  - 背景移除
- 智慧補光
  - 自動亮度均衡
  - 陰影細節增強
- 瑕疵修復
  - 污點去除
  - 智慧修補

## 安裝要求

### 系統需求
- Python 3.8+
- pip 套件管理器

### 必要套件
- gradio
- opencv-python
- numpy

## 安裝步驟

1. 複製專案
```bash
git clone https://github.com/your-username/casper-image-processor.git
cd casper-image-processor
```

2. 建立虛擬環境
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
.\venv\Scripts\activate  # Windows
```

3. 安裝依賴
```bash
pip install -e .
```

## 使用方法

1. 啟動應用程式
```bash
python ui/app.py
```

2. 開啟瀏覽器訪問
```
http://localhost:7860
```

## 專案結構

```
casper-image-processor/
├── README.md
├── setup.py
├── requirements.txt
├── src/
│   ├── core/           # 核心處理功能
│   │   ├── resize.py   # 尺寸調整
│   │   ├── crop.py     # 裁切功能
│   │   ├── adjust.py   # 基礎調整
│   │   ├── enhance.py  # 影像增強
│   │   └── denoise.py  # 降噪處理
│   ├── ai/            # AI 增強功能
│   │   ├── remove_bg.py # 去背功能
│   │   ├── lighting.py  # 智慧補光
│   │   └── repair.py    # 瑕疵修復
│   └── utils/         # 工具函數
│       ├── validators.py
│       └── helpers.py
├── ui/                # 使用者介面
│   ├── app.py        # Gradio 主程式
│   └── assets/       # 靜態資源
└── tests/            # 測試檔案
```

## API 文件

### ImageResizer
```python
resize_image(image, width=None, height=None, aspect_ratio=True)
crop_image(image, aspect_ratio="1:1")
```

### ImageAdjuster
```python
adjust_brightness(image, value)
adjust_contrast(image, value)
adjust_saturation(image, value)
```

### ImageEnhancer
```python
sharpen(image, amount)
denoise(image, strength)
```

## 開發計劃

### 第一階段 (當前)
- [x] 基礎影像處理
- [x] Gradio UI 介面
- [ ] 單元測試

### 第二階段
- [ ] AI 模型整合
- [ ] 批次處理功能
- [ ] 檔案格式支援

### 第三階段
- [ ] 特效濾鏡
- [ ] 文字浮水印
- [ ] 智慧場景合成

## 貢獻指南

1. Fork 本專案
2. 建立特性分支
3. 提交更改
4. 發送 Pull Request

## 問題回報

如發現任何問題或建議，請在 GitHub Issues 回報。

## License

本專案採用 MIT License 授權。

## 作者

- Kevin Luo
```
