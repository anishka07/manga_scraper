# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import mysql.connector 

class MangaPipeline:
    
    def __init__(self) -> None:
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = mysql.connector.connect(host='localhost',
                                            user='root',
                                            passwd='yourpw',
                                            database='db_name')
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute('''DROP TABLE IF EXISTS manga_table''')
        self.curr.execute('''CREATE TABLE manga_table(≠
                          manga_title text,
                          manga_price text,
                          manga_image_source text
        )''')

    def enter_values(self, item):
        sql_statement = '''INSERT INTO manga_table(manga_title, manga_price, manga_image_source)
                          values (%s, %s, %s)'''
        print(sql_statement)
        self.curr.execute(sql_statement, (
            item['manga_title'],
            item['manga_price'],
            item['manga_imageurl']
        ))

    def process_item(self, item, spider):
        self.enter_values(item)
        self.conn.commit()
        return item
