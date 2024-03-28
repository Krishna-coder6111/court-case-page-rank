
import csv
import pandas as pd
from serpapi import GoogleSearch
from urllib.parse import urlsplit, parse_qsl

def node_maker():
    '''
    This functionn removes 
    '''
    citation_graph  = {}
    df = pd.read_csv('google_scholar_case_law_results.csv')

    for index,row in df.iterrows():
        case_id = row['cited_by_id']
        cited_ids = []
        

        if case_id not in citation_graph:
            citation_graph[case_id] = cited_ids
        else:
            citation_graph[case_id].extend(cited_ids)
        
        citation_graph[case_id] = list(set(citation_graph[case_id]))
    
    return citation_graph


def adjacency_matrix(node_map):
    '''
    This function will take the hashmap from the node_maker function and
    create an adjacency matrix that will represent the graph of the court cases
    '''
    pass