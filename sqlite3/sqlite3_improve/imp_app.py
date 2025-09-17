import sqlite3
import imp_database

db = imp_database.Database('test.db')
db.TEST_drop_test()
db.init()

test_data = [
                ('one', 1),
                ('two', 2),
    ]

db.insert_many_test(test_data)

db.show_all_test()

result = db.search_test("name", "one")
db.show_fetch_result(result)

db.close()