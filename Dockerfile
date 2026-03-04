# --- مرحله ۱: ساخت Image ---
FROM python:3.12-slim

# جلوگیری از cacheهای قدیمی
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# مسیر کاری
WORKDIR /app

# کپی فایل‌های پروژه
COPY requirements.txt /app/

# نصب وابستگی‌ها
RUN pip install -i https://mirror-pypi.runflare.com/simple --upgrade pip
RUN pip install -i https://mirror-pypi.runflare.com/simple -r requirements.txt

# کپی فایل های پروژه به داخل ایمیج
COPY . /app/
