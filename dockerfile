FROM python:latest

VOLUME /app
WORKDIR /app

#install dependencies
RUN pip install --upgrade pip
RUN pip install requests
RUN pip install bs4
RUN pip install lxml

#command to run on container start
CMD ["python","ltt_web_scraping.py"]