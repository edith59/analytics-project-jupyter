FROM python:latest
COPY . /code/
WORKDIR /code
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt
CMD ["python", "-u", "data_transformation.py"]