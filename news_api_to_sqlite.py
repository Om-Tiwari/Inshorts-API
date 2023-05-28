import sqlite3
from scraper import getNews


def create_database():
    conn = sqlite3.connect('educationNews.db')
    c = conn.cursor()

    # Create the news table
    c.execute('''
        CREATE TABLE IF NOT EXISTS educationNews (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            imageUrl TEXT,
            content TEXT,
            author TEXT,
            date TEXT,
            time TEXT,
            readMoreUrl TEXT
        )
    ''')

    conn.commit()
    conn.close()


def save_news_to_database(news_dict):
    conn = sqlite3.connect('educationNews.db')
    c = conn.cursor()

    news_list = news_dict['data']
    for news in news_list:
        c.execute('''
            INSERT INTO educationNews (title, imageUrl, content, author, date, time, readMoreUrl)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (
            news['title'],
            news['imageUrl'],
            news['content'],
            news['author'],
            news['date'],
            news['time'],
            news['readMoreUrl']
        ))

    conn.commit()
    conn.close()


def main():
    create_database()
    category = 'education'
    news_dict = getNews(category)
    save_news_to_database(news_dict)
    print("News saved to database successfully.")


if __name__ == '__main__':
    main()
