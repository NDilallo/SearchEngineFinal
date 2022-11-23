# depaul-csc299-search
Search project for DePaul CSC 299

Group Members: Nick Dilallo, Serhat Cingilli, Fritz Nastor


Classes/Files and functions that we have changed: 

eval file: 
            
            Added give_score_with_thesaurus method
                        - Calculated a standardized score for a matching document based on the strength of its
                          relation to the query. If the document contained the original query word, 5 points
                          was added to the total score for that document. If it had to rely on a thesaurus 
                        synonym, it lost 1 point for each word down the synonym list it had to travel down to 
                        a minimum of 1. We interpreted the earlier words in the thesaurus as stronger synonyms.

            Added format_all_scores_for_display method
                        - Presented the scores in a more readable/presentable way
            Added format_minScore_scores_for_display method
                        - Formats all the scores above the given minimum into a readable form

index file: 

            Added new field to __init__: 
                - self.intersects - holds the intersections of the query and the doc
                This was needed for use in calc. the scores
            Updated search method:
                    - Creates a set that contains all query terms and their synonyms. Goes through each document
                    and takes the intersection of the previously mentioned set and the document tokens (it adds this
                    intersection to the new self.intersects field here). If the size of this intersection is bigger 
                    than that of the original query terms, we determine the document to be a suitable fit and add 
                    its id to the search results.
            Updated read method:
                    - Changed to utilize readlines() so that it could actually read our file (corpus.jsonl)

query_process file:

            Updated NaiveQueryParser:
                - __init__: added field for holding the corresponding thesaurus. This was needed for our scoring process
                - parse_query: terms field of returned query is now a defaultdict(set) that contains the query terms
                                as keys and their synonyms as values in a set
                - create_naive_query_process: Creates a NaiveIndex instead of ListBased... since that is the implementation
                                                we used.

search_api file:

            Updated Query dataclass:
                - terms field now hold a defualtDict(set) which has all query terms as keys and their synonyms as values

Thesaurus file:

            Entirely new:
                A Thesaurus object which holds words and their synonyms using a thesaurus. 
                __init__: self.synonyms - Dictionary of all tokens in query w/ synonyms as values
                          self.thesaurus_file - filename pointing to our thesaurus
                          self.list_synonyms - Same as self.synonyms but holds values in a list format since maintaining
                                                their order was needed for calculating scores algorithm
                add_synonyms: Adds the synonyms for each query token into the defaultdict w/ their corresponding base words

test_query file:

            Our testfile/function used for intermediate testing. Still includes many commented out lines
            so that our testing process/thought process throughout could be seen. Mainly used print statements 
            to determine if things were coming out accurately and held the proper data.

Evaluation: Did adding synonyms improve search results relevance?
            
            Yes, adding synonyms did imporve search results relevance overall. As can be seen by printing the scores
            of matching documents, only a small number of documents contain all of the original words in the query. 
            By adding synonyms, documents without perfect scores (relied on synonyms) are included. Assuming the
            given synonyms are good, these documents should be equally as relevant, or at the very least, contain
            many relevant search terms. With our format_minScore_scores_for_display, you can choose the level of
            relevance you want in your documents (num of query tokens * 5 == perfect, 0 == no relevance).