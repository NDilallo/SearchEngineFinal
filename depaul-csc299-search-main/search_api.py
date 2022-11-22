import dataclasses
from typing import List
from Thesaurus import *
from collections import defaultdict


@dataclasses.dataclass
class Query:
    terms: defaultdict(set)
    num_results: int


@dataclasses.dataclass
class SearchResults:
    result_doc_ids: List[str]
