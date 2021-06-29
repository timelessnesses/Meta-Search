FROM python:3
WORKDIR /app
COPY *.py .
COPY *.txt .
COPY *.log .
RUN pip install -r requirements.txt
EXPOSE 80
CMD ["python","main.py"]
