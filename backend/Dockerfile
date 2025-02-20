FROM python:3.12-alpine
WORKDIR /app
RUN apk add --no-cache git grep file libc6-compat
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000:5000
ENV FLASK_APP=app.py
ENV FLASK_ENV=production
CMD ["flask", "run","--debug", "--host=0.0.0.0"]