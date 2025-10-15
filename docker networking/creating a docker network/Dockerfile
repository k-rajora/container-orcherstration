FROM python

WORKDIR /mysql

COPY . .

RUN pip install pymysql
RUN pip install cryptography

CMD [ "python","localsql.py" ]