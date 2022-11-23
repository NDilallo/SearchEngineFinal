from unittest import TestCase
from query_process import *
from tokenizer import *
from index import *
from Thesaurus import *
from eval import *


class TestQueryProcess(TestCase):
    def test_run(self):
        # tokenizer = NaiveTokenizer()
        # parser = NaiveQueryParser(tokenizer=tokenizer)
        # query = parser.parse_query("inducible tension protein", 10)
        # # print(query.terms, '\n', query.num_results)
        #
        # index = NaiveIndex(filename='corpusSmaller.jsonl')
        # index.read()
        #
        # search_result = index.search(query)
        # print(search_result)
        #
        # score = EvalEntry

        process = create_naive_query_process("corpus.jsonl")
        print(process.run("inducible tension protein", 5))
        # print(process.index.score)
        # print(process.query_parser.thesaurus.list_synonyms)
        # print(process.index.intersects)
        scores = give_score_with_thesaurus(process.index, process.query_parser.thesaurus.list_synonyms)
        #print(format_all_scores_for_display(scores))
        print(format_minScore_scores_for_display(scores, 7))

