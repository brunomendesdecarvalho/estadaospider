# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3


class EstadaospiderPipeline(object):
    def __init__(self):
        self.criar_conexao()
        self.criar_tabela()

    def criar_conexao(self):
        self.con = sqlite3.connect("manchetes_estadao.db")
        self.cursor = self.con.cursor()

    def criar_tabela(self):
        self.cursor.execute("""DROP TABLE IF EXISTS manchetes_estadao""")
        self.cursor.execute("""create table manchetes_estadao(
            Manchete text,
	        Link text
            )
        """)

    def process_item(self, item, spider):
        self.guardar_db(item)
        return item

    def guardar_db(self, item):
        self.cursor.execute("""insert into manchetes_estadao values(
                ?, ?
            )""",
            (
		item['Manchete'],
		item['Link'],
		    ))

        self.con.commit()
        return item
