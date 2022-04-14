FROM python:3.8
WORKDIR /code
COPY req.txt .
RUN pip install -r ./req.txt
COPY server.py .
CMD [ "python", "./server.py" ]

