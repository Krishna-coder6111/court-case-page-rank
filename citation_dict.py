import time
from urllib.parse import parse_qsl, urlencode, urlsplit
import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup
from serpapi import GoogleSearch

# def fetch_citations(case_link):
#     """
#     Fetches all the citations from the google scholar case link
#     """
#     response = requests.get(case_link)
#     response.raise_for_status() # check for http errors

#     soup = BeautifulSoup(response.content, 'html.parser')
#     citation_elements = soup.find_all('div', class_='gs_ri')
#     citations = []
#     for element in citation_elements:
#         citation_link = element.find('a')['href']
#         cited_by_id = extract_id_from_link(citation_link)
#         citations.append(cited_by_id)
#     return citations

def fetch_citations_serpapi(case_id):
    """
    Fetches citations using the SerpApi library
    """
    params = {
        "api_key": GoogleSearch.SERP_API_KEY,      # Replace with your actual key 
        "engine": "google_scholar",         # Specify the citation engine
        "cites": case_id ,                      # goes to id citation page                    # Set the case link as the query
        "hl": "en",                       # language
        "start": "0",                     # first page
        # "as_sdt": "2006" 
    }

    search = GoogleSearch(params)                
    citations = []

    while True:
        results = search.get_dict()              

        if "error" in results:                    
            break
        
        print(f"Currently extracting page #{results.get('serpapi_pagination', {}).get('current')}..")

        for result in results["organic_results"]:
            cited_by_id = result.get("inline_links", {}).get("cited_by", {}).get("cites_id", {})
            # link = result.get("inline_links", {}).get("cited_by", {}).get("link", {})
            # link = result.get("link")
            # cited_by_id = extract_id_from_link(link) 
            # still got the same null values
            citations.append(cited_by_id)

        if "next" in results.get("serpapi_pagination", {}):
            search.params_dict.update(dict(parse_qsl(urlsplit(results["serpapi_pagination"]["next"]).query)))
        else:
            break
    return citations

def extract_id_from_link(link):
    """
    Extracts the id from the link
    """
    query = urlsplit(link).query
    print(query)
    query_dict = dict(parse_qsl(query))
    print(query_dict)
    return query_dict['cites']

# def update_url_for_page(base_url, page_num):
#     """
#     Updates the url to include the page number
#     """
#     parsed_url = urlsplit(base_url)
#     query_params = dict(parse_qsl(parsed_url.query))
#     query_params['start'] = (page_num - 1) * 10  # Assuming 10 results per page
#     new_query_string = urlencode(query_params)
#     return parsed_url._replace(query=new_query_string).geturl()

# def get_all_case_links(start_url, num_pages=2):
#     citations = []
#     current_url = start_url
#     page_num = 0

#     while True:
#         page_num += 1
#         print(f"Fetching page: {page_num}")
#         print(f"Original URL: {start_url}")  # Add this line


#         # Fetch case links from the current page
#         new_citations = fetch_citations(current_url)
#         citations += new_citations
#         print(new_citations)

#         # Check if we should stop fetching
#         if not new_citations:  # Example: Stop if no results are found 
#             print("No more pages found.")
#             break

#         # Update the URL for the next page
#         current_url = update_url_for_page(start_url, page_num + 1)

#         time.sleep(3) +   time.sleep(np.random.random()*2)
        

#     return citations 


'''
    This function will search the cited links in {google_scholar_case_law_results.csv} for all the pages and 
    for each snippet, 
    it will find the id of the court case 
    and add it to a hashmap with the id as the key 
    and value  as a list of cited link ids.
    test that all links were parsed by checking the length of the value with cited by count column
'''
if __name__ == '__main__':
    df = pd.read_csv('google_scholar_case_law_results.csv')

    #todo get the dictionary from the csv
    adjacency_data = {}

    # Iterate over the 'cited_by_id' column
    for index, row in df.iterrows():
        #todo if the cited by id is not already present in the adjacency_data, add it to the adjacency_data
        case_id = str(row['cited_by_id'])  
        citations = fetch_citations_serpapi(case_id)
        adjacency_data[case_id] = citations
        print(f"Citations for case ID {case_id}: {citations}")
    adjacency_df = pd.DataFrame(adjacency_data)
    adjacency_df.to_csv('adjacency_matrix.csv', index=False)
# if __name__ == '__main__':
#     # Example usage
#     #TODO convert to for loop that gets cited_by_link from the csv and then calls fetch_citations
#     case_link = "https://scholar.google.com/scholar?cites=3908441666771801163&as_sdt=2005&sciodt=2006&hl=en"
#     case_id = "3908441666771801163"
#     result_id = "wAWXnlpHJ94J"
#     citations = fetch_citations_serpapi(case_id)
#     print(citations) 

citations = ['6784444020641335081', '1583556804840013293', '10082344911867294248', '16787914492556885305', '5986003311604430639', '7808879240538460858','13049238382028246811', '4174734966299528173', '15980914471863582859', '17922144102891119274']


['3712199782663842138', '4514828035130080000', '1431245020905989514', '5492551306867143864', '11680241615353995589', '4219719661474558993', '2865266543904598145', '6760448793637598287', '1605141320356749871', '14443806859803604083', '11346997121285226352', {}, {}, {}, {}, '7286478791266207373', {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, '12935780648816362370', '12862678941636877199', '16119205960004697371', '4318538769214862914', {}]




