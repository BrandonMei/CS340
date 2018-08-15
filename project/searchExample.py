import whoosh
import csv
from whoosh import index
from whoosh.index import open_dir
from whoosh.index import create_in
from whoosh.fields import *
import os, os.path
from whoosh.qparser import QueryParser
from whoosh.qparser import MultifieldParser


def search(indexer, searchTerm, searchColumns):
	with indexer.searcher() as searcher:
		words = searchColumns
		query = MultifieldParser(words, schema=indexer.schema).parse(searchTerm)
		results = searcher.search(query)
		print(results)
		for line in results:
			print("--------------------------")
			print(line)
			#print("--------------------------")
			#print(line['firstName'], line['lastName'])


def main():
	Keyword = "Junior"

	ix = index.open_dir("indexDir")

	searchField = ["Class"]

	search(ix, Keyword, searchField)



main()
