# Accounting App

這是用於 GDG on campus NCU 社課教學的 repo

## Installation

1. clone 這份 repo 到你的電腦上:
   ```bash
   git clone https://github.com/sunset513/accounting_app.git

2. 切換到正確的路徑:
cd accounting_app

3. 建立 Docker 映像檔:
   ```bash
   docker build -t accounting_app .

4. 運行 Docker 容器:
   ```bash
   docker run -d -p 5000:5000 accounting_app
