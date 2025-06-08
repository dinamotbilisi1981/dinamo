import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import ttk
import mysql.connector

DB_NAME = "book_scraper"
TABLE_NAME = "books"

def create_database():
    conn = mysql.connector.connect(host="localhost", user="root", password="")
    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS " + DB_NAME)
    conn.commit()
    cursor.close()
    conn.close()

def scrape_books():
    url = "https://books.toscrape.com/catalogue/page-1.html"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    books = []
    articles = soup.find_all("article", class_="product_pod")
    
    for article in articles:
        title = article.h3.a["title"]
        price = article.find("p", class_="price_color").text
        availability = article.find("p", class_="instock availability").text.strip()
        rating = article.p["class"][1] 
        books.append((title, price, availability, rating))
    
    return books

def save_books_to_mysql(books):
    conn = mysql.connector.connect(host="localhost", user="root", password="", database=DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
            id INT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(255),
            price VARCHAR(20),
            availability VARCHAR(100),
            rating VARCHAR(20)
        )
    """)
    
    cursor.execute(f"DELETE FROM {TABLE_NAME}")
    
    for book in books:
        cursor.execute(f"""
            INSERT INTO {TABLE_NAME} (title, price, availability, rating)
            VALUES (%s, %s, %s, %s)
        """, book)

    conn.commit()
    cursor.close()
    conn.close()

def show_books_gui(books):
    window = tk.Tk()
    window.title("Books to Scrape")

    tree = ttk.Treeview(window, columns=("Title", "Price", "Availability", "Rating"), show="headings")
    tree.heading("Title", text="Title")
    tree.heading("Price", text="Price")
    tree.heading("Availability", text="Availability")
    tree.heading("Rating", text="Rating")
    
    for book in books:
        tree.insert("", "end", values=book)
    
    tree.pack(fill=tk.BOTH, expand=True)
    window.mainloop()

create_database()
books_data = scrape_books()
if books_data:
    save_books_to_mysql(books_data)
    show_books_gui(books_data)
else:
    print("No books found.")