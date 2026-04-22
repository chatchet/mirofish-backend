# 新加坡时间: 2026-04-22 09:43
# =========================================
# 这个 Dockerfile 用来告诉 Zeabur / Docker：
# 1. 用什么基础环境
# 2. 复制哪些文件进去
# 3. 安装哪些依赖
# 4. 最后怎样启动程序
# =========================================

# 使用官方 Python 3.11 轻量镜像作为基础环境
FROM python:3.11-slim

# 设置容器里的工作目录
WORKDIR /app

# 先复制依赖文件
COPY requirements.txt .

# 安装 Python 依赖
RUN pip install --no-cache-dir -r requirements.txt

# 再复制当前项目的全部文件到容器里
COPY . .

# 声明容器会使用 5000 端口
EXPOSE 5000

# 启动 Flask 应用
CMD ["python", "app.py"]
