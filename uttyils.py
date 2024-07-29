import sqlite3
from datetime import date

def connect_db():
    return sqlite3.connect('library.db')

def add_book(title, author, genre, year, copies):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO Книги (Название, Автор, Жанр, Год_издания, Количество_экземпляров)
        VALUES (?, ?, ?, ?, ?)
    ''', (title, author, genre, year, copies))
    conn.commit()
    conn.close()

def add_reader(first_name, last_name, birth_date, contact_info):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO Читатели (Имя, Фамилия, Дата_рождения, Контактные_данные)
        VALUES (?, ?, ?, ?)
    ''', (first_name, last_name, birth_date, contact_info))
    conn.commit()
    conn.close()

def issue_book(book_id, reader_id, issue_date):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO Выданные_книги (Книга_ID, Читатель_ID, Дата_выдачи)
        VALUES (?, ?, ?)
    ''', (book_id, reader_id, issue_date))
    cursor.execute('''
        UPDATE Книги
        SET Количество_экземпляров = Количество_экземпляров - 1
        WHERE ID = ?
    ''', (book_id,))
    conn.commit()
    conn.close()

def return_book(issue_id, return_date):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE Выданные_книги
        SET Дата_возврата = ?
        WHERE ID = ?
    ''', (return_date, issue_id))
    cursor.execute('''
        SELECT Книга_ID FROM Выданные_книги
        WHERE ID = ?
    ''', (issue_id,))
    book_id = cursor.fetchone()[0]
    cursor.execute('''
        UPDATE Книги
        SET Количество_экземпляров = Количество_экземпляров + 1
        WHERE ID = ?
    ''', (book_id,))
    conn.commit()
    conn.close()

def add_fine(reader_id, amount, fine_date):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO Штрафы (Читатель_ID, Сумма, Дата_начисления)
        VALUES (?, ?, ?)
    ''', (reader_id, amount, fine_date))
    conn.commit()
    conn.close()

def get_all_books():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Книги')
    books = cursor.fetchall()
    conn.close()
    return books

def get_all_readers():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Читатели')
    readers = cursor.fetchall()
    conn.close()
    return readers

def get_all_issued_books():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Выданные_книги')
    issued_books = cursor.fetchall()
    conn.close()
    return issued_books

def get_all_fines():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Штрафы')
    fines = cursor.fetchall()
    conn.close()
    return fines

if __name__ == "__main__":
    add_book('Преступление и наказание', 'Фёдор Достоевский', 'Роман', 1866, 5)
    add_book('Война и мир', 'Лев Толстой', 'Роман', 1869, 3)
    add_reader('Иван', 'Иванов', '1990-01-01', 'ivanov@example.com')
    add_reader('Петр', 'Петров', '1985-05-15', 'petrov@example.com')
    issue_book(1, 1, date.today().isoformat())
    return_book(1, date.today().isoformat())
    add_fine(1, 100.0, date.today().isoformat())
    print(get_all_books())
    print(get_all_readers())
    print(get_all_issued_books())
    print(get_all_fines())
