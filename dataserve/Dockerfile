#Use an official Python runtime as a parent image
FROM python:3.6

WORKDIR /app
COPY . /app
RUN pip install --trusted-host pypi.python.org -r requirements.txt
EXPOSE 1883
EXPOSE 8883
EXPOSE 12504
ENV NAME World 
ENV AWS_DEFAULT_REGION us-west-2
CMD ["python", "data_serve.py"]
#CMD ["python"]