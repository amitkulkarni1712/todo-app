FROM python:alpine3.7
COPY . /app
WORKDIR /app
RUN ls -l
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 5000
ENTRYPOINT [ "python" ]
CMD [ "todo.py" ]
