import sqlite3
conn = sqlite3.connect('library.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Книги (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Название TEXT NOT NULL,
    Автор TEXT NOT NULL,
    Жанр TEXT NOT NULL,
    Год_издания INTEGER NOT NULL,
    Количество_экземпляров INTEGER NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Читатели (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Имя TEXT NOT NULL,
    Фамилия TEXT NOT NULL,
    Дата_рождения DATE NOT NULL,
    Контактные_данные TEXT NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Выданные_книги (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Книга_ID INTEGER NOT NULL,
    Читатель_ID INTEGER NOT NULL,
    Дата_выдачи DATE NOT NULL,
    Дата_возврата DATE,
    FOREIGN KEY (Книга_ID) REFERENCES Книги(ID),
    FOREIGN KEY (Читатель_ID) REFERENCES Читатели(ID)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Штрафы (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Читатель_ID INTEGER NOT NULL,
    Сумма REAL NOT NULL,
    Дата_начисления DATE NOT NULL,
    FOREIGN KEY (Читатель_ID) REFERENCES Читатели(ID)
)
''')

conn.commit()
conn.close()


import sqlite3

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

add_book('Преступление и наказание', 'Фёдор Достоевский', 'Роман', 1866, 5)


