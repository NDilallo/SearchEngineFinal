from unittest import TestCase
from query_process import *
from tokenizer import *
from index import *


class TestQueryProcess(TestCase):

    def test_run(self):
        tokenizer = NaiveTokenizer()
        parser = NaiveQueryParser(tokenizer=tokenizer)
        index = NaiveIndex(filename='corpus.jsonl')
        formatter = NaiveResultFormatter()
        testQuery = QueryProcess(query_parser=parser, index=index, result_formatter=formatter)
        print(testQuery.run("the"))