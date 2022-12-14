from collections import defaultdict
import json


class Thesaurus:

    def __init__(self):
        self.synonyms = defaultdict(set)  # Dictionary of all tokens in query w/ synonyms as values
        self.thesaurus_file = 'syns.jsonl' # Provided thesaurus could easily be changed
        self.list_synonyms = defaultdict(list)

    def add_synonyms(self, tokens: set) -> None:
        """
        Adds the synonyms for each query token into the defaultdict. Should be called
        after the query is tokenized.
        :param tokens: Tokens from the search query in a list.
        """
        for term in tokens:
            self.synonyms[term] = ''
            self.list_synonyms[term] = ''
        with open(self.thesaurus_file) as fp:
            for line in fp:
                obj = json.loads(line)
                if obj.get("term") in tokens:
                    self.synonyms[obj["term"]] = set(obj.get("syns"))
                    self.list_synonyms[obj["term"]] = obj.get("syns")

# test = Thesaurus()
# test.add_synonyms(["unable", "abducting"])
# print(test.synonyms)


