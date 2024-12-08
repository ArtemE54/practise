import sqlite3

# Подключение к базе данных
conn = sqlite3.connect('Chinook_Sqlite.sqlite')
cursor = conn.cursor()

# Запрос для получения списка всех клиентов и количества их заказов
query = """
SELECT c.CustomerId, c.FirstName, c.LastName, COUNT(i.InvoiceId) AS NumberOfOrders
FROM Customer c
LEFT JOIN Invoice i ON c.CustomerId = i.CustomerId
GROUP BY c.CustomerId
ORDER BY NumberOfOrders DESC;
"""

cursor.execute(query)
customers = cursor.fetchall()

print("Список всех клиентов и количество их заказов:")
for customer in customers:
    print(f" - {customer[1]} {customer[2]} (ID: {customer[0]}) - Заказов: {customer[3]}")


# Подключение к базе данных
conn = sqlite3.connect('Chinook_Sqlite.sqlite')
cursor = conn.cursor()

# Запрос для создания представления
query = """
CREATE VIEW AlbumSales AS
SELECT a.AlbumId, a.Title AS AlbumTitle, COUNT(il.InvoiceLineId) AS TotalSales
FROM Album a
JOIN Track t ON a.AlbumId = t.AlbumId
JOIN InvoiceLine il ON t.TrackId = il.TrackId
GROUP BY a.AlbumId
ORDER BY TotalSales DESC;
"""


conn.commit()

# Запрос для получения данных из представления
query = """
SELECT * FROM AlbumSales;
"""

cursor.execute(query)
album_sales = cursor.fetchall()

print("Общее количество продаж по каждому альбому:")
for album in album_sales:
    print(f" - {album[1]} (ID: {album[0]}) - Продаж: {album[2]}")


# Создание класса для представления альбома
class Album:
    def __init__(self, album_id, title, artist_id):
        self.album_id = album_id
        self.title = title
        self.artist_id = artist_id

    def __repr__(self):
        return f"Album(id={self.album_id}, title='{self.title}', artist_id={self.artist_id})"


# Создание класса для представления исполнителя
class Artist:
    def __init__(self, artist_id, name):
        self.artist_id = artist_id
        self.name = name

    def __repr__(self):
        return f"Artist(id={self.artist_id}, name='{self.name}')"


# Функция для подключения к базе данных
def get_connection(db_file):
    return sqlite3.connect(db_file)


# Функция для получения всех альбомов
def get_all_albums(connection):
    cursor = connection.cursor()
    query = "SELECT AlbumId, Title, ArtistId FROM Album;"
    cursor.execute(query)
    albums = cursor.fetchall()
    return [Album(album_id, title, artist_id) for album_id, title, artist_id in albums]


# Функция для получения всех исполнителей
def get_all_artists(connection):
    cursor = connection.cursor()
    query = "SELECT ArtistId, Name FROM Artist;"
    cursor.execute(query)
    artists = cursor.fetchall()
    return [Artist(artist_id, name) for artist_id, name in artists]



# Пример использования
if __name__ == "__main__":
    conn = get_connection('Chinook_Sqlite.sqlite')

    # Получение всех альбомов
    albums = get_all_albums(conn)
    print("Все альбомы:")
    for album in albums:
        print(album)

    # Получение всех исполнителей
    artists = get_all_artists(conn)
    print("\nВсе исполнители:")
    for artist in artists:
        print(artist)

import sqlite3


# Создание класса для представления альбома
class Album:
    def __init__(self, album_id, title, artist_id):
        self.album_id = album_id
        self.title = title
        self.artist_id = artist_id

    def __repr__(self):
        return f"Album(id={self.album_id}, title='{self.title}', artist_id={self.artist_id})"


# Функция для подключения к базе данных
def get_connection(db_file):
    return sqlite3.connect(db_file)


# CRUD операции для альбомов

# 1. Создание (Create)
def create_album(connection, title, artist_id):
    cursor = connection.cursor()
    query = "INSERT INTO Album (Title, ArtistId) VALUES (?, ?);"
    cursor.execute(query, (title, artist_id))
    connection.commit()
    return cursor.lastrowid


# 2. Чтение (Read)
def read_albums(connection):
    cursor = connection.cursor()
    query = "SELECT AlbumId, Title, ArtistId FROM Album;"
    cursor.execute(query)
    albums = cursor.fetchall()
    return [Album(album_id, title, artist_id) for album_id, title, artist_id in albums]


# 3. Обновление (Update)
def update_album(connection, album_id, new_title):
    cursor = connection.cursor()
    query = "UPDATE Album SET Title = ? WHERE AlbumId = ?;"
    cursor.execute(query, (new_title, album_id))
    connection.commit()
    return cursor.rowcount


# 4. Удаление (Delete)
def delete_album(connection, album_id):
    cursor = connection.cursor()
    query = "DELETE FROM Album WHERE AlbumId = ?;"
    cursor.execute(query, (album_id,))
    connection.commit()
    return cursor.rowcount


# Пример использования
if __name__ == "__main__":
    conn = get_connection('Chinook_Sqlite.sqlite')

    # Создание нового альбома
    new_album_id = create_album(conn, "New Album", 1)
    print(f"Создан новый альбом с ID: {new_album_id}")

    # Чтение всех альбомов
    albums = read_albums(conn)
    print("Все альбомы:")
    for album in albums:
        print(album)

    # Обновление альбома
    updated_rows = update_album(conn, new_album_id, "Updated Album Title")
    print(f"Обновлено альбомов: {updated_rows}")

    # Чтение всех альбомов после обновления
    albums = read_albums(conn)
    print("Все альбомы после обновления:")
    for album in albums:
        print(album)

    # Удаление альбома
    deleted_rows = delete_album(conn, new_album_id)
    print(f"Удалено альбомов: {deleted_rows}")

    # Чтение всех альбомов после удаления
    albums = read_albums(conn)
    print("Все альбомы после удаления:")
    for album in albums:
        print(album)

    # Закрытие соединения
    conn.close()