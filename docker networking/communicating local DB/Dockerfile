FROM python

WORKDIR /my-sql-server

COPY . .

RUN pip install pymysql

CMD [ "python","localsql.py" ]