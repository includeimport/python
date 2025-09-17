import sqlite3

class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()

    def init(self):
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS test (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                age INTEGER
                )""")

    def close(self):
        self.conn.close()

    def insert_test(self, name: str, age: int):
        self.cur.execute(
            "INSERT INTO test (name, age) VALUES (?,?)", 
            (name, age)
        )

    def insert_many_test(self, data):
        self.cur.executemany(
            "INSERT INTO test (name, age) VALUES (?,?)",
            data
        )

    def fetch_all_test(self):
        self.cur.execute("SELECT * FROM test")
        return self.cur.fetchall()

    def show_all_test(self):
        test_records = self.fetch_all_test()

        for record in test_records:
            print(record)

    def search_test(self, column: str, value: str|int):
        allowed_columns = {"name", "age"}
        if column not in allowed_columns:
            raise ValueError(f"not allowed column: {column}")

        # (value,) "," 콤마를 사용해야 튜플이 된다.
        self.cur.execute(f"SELECT * FROM test WHERE {column} = ?", (value,))
        return self.cur.fetchall()

    def show_fetch_result(self, rows):
        for row in rows:
            print(row)

    def TEST_drop_test(self):
        self.cur.execute("DROP TABLE IF EXISTS test")
