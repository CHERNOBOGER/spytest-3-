import sqlite3
import pytest

@pytest.fixture
def sqlite_db(tmpdir):
    db_path = tmpdir.join("test.db")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    yield cursor
    conn.close()

def test_insert_and_select(sqlite_db):
    sqlite_db.execute("CREATE TABLE test (id INTEGER PRIMARY KEY, name TEXT)")
    sqlite_db.execute("INSERT INTO test (name) VALUES (?)", ("Alice",))
    sqlite_db.execute("INSERT INTO test (name) VALUES (?)", ("Bob",))
    
    sqlite_db.execute("SELECT * FROM test")
    rows = sqlite_db.fetchall()
    
    assert len(rows) == 2
    assert rows[0][1] == "Alice"
    assert rows[1][1] == "Bob"
    print("Test insert_and_select: PASSED")