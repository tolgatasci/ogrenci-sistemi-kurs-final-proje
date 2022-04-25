import sqlite3
class Database:
    db = None
    def __init__(self, db_name="database.db"):
        self.db = sqlite3.connect(db_name)

    def __del__(self):
        self.db.close()

    # table_name = "table_name", columns = "name TEXT, age INTEGER""
    def create_table(self, table_name, columns):
        c = self.db.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS {} ({})".format(table_name, columns))
        self.db.commit()
        c.close()
    def run_query(self, query, params=()):
        c = self.db.cursor()
        c.execute(query, params)
        fetch = c.fetchall()
        c.close()
        return fetch
        # query = "insert into table_name (columns) values (values)"
    # columns kısmı hangi sütunların ekleneceğini belirtir.
    # insert into table_name (ad,yas) values ('tolga',30)
    def insert(self, query):
        c = self.db.cursor()
        c.execute(query)
        self.db.commit()
        c.close()
    def insert_field(self, query, params=()):
        c = self.db.cursor()
        c.execute(query, params)
        self.db.commit()
        c.close()

    # query =  "select * from table_name"
    def select(self, query):
        c = self.db.cursor()
        c.execute(query)
        fetch =  c.fetchall()
        c.close()
        return fetch
    # query = "update table_name set degisilcek_kolon = yeni deger where id = id_deger"
    # where ile değiştirceğimiz yeri belirtiyoruz. Bir veya birden fazla alana etki edebiliriz. Where olmaz ise tüm tabloya uygular.
    def update(self, query):
        c = self.db.cursor()
        c.execute(query)
        self.db.commit()
    # query = "delete from table_name where id = id_deger"
    # where ile değiştirceğimiz yeri belirtiyoruz. Bir veya birden fazla alana etki edebiliriz. Where olmaz ise tüm tabloya uygular.
    def delete(self, query):
        c = self.db.cursor()
        c.execute(query)
        self.db.commit()