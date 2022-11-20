FROM python:3.7
COPY requirements.txt /opt/app/requirements.txt
WORKDIR /opt/app
RUN pip install -r requirements.txt
EXPOSE 8051
COPY . /opt/app
ENTRYPOINT ["streamlit", "run", "test.py", "--server.port=8501", "--server.address=0.0.0.0"]

#CMD [ "./test.py" ]