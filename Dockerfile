# Step 1: Base image (Python 3.11 recommended)
FROM python:3.11-slim

# Step 2: Set work directory
WORKDIR /app

# Step 3: Install system dependencies
RUN apt-get update && apt-get install -y \
    libpq-dev gcc --no-install-recommends \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Step 4: Copy project files
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Step 5: Expose port (Render will override)
EXPOSE 8000

# Step 6: Run migrations + server
CMD ["bash", "-c", "python manage.py migrate && gunicorn course_service.wsgi:application --bind 0.0.0.0:$PORT"]
