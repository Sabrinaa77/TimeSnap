# 使用 Python 3.10 作為基礎映像
FROM python:3.10-slim

# 設定工作目錄
WORKDIR /app

# 複製需求檔案
COPY requirements.txt .

# 安裝套件
RUN pip install --no-cache-dir -r requirements.txt

# 複製整個專案
COPY . .

# 對外開放 8000 port
EXPOSE 8000

# 預設啟動指令
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
