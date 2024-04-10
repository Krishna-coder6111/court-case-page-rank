import os
from urllib.parse import parse_qsl, urlsplit

from serpapi import GoogleSearch


def case_law_results():

    print("Extracting case law results..")

    params = {
        "api_key": GoogleSearch.SERP_API_KEY,  # SerpApi API key
        "engine": "google_scholar",       # Google Scholar search results
        "q": "e",               # search query = e because it is the most common letter in the English language
        "hl": "en",                       # language
        "start": "0",                     # first page
        "as_sdt": "2006"                  # case law results. "6" param will work the same way as "2006"
    } #todo randomize the date and get only a 100 citations
    search = GoogleSearch(params)

    case_law_results_data = []

    while True:
        results = search.get_dict()

        if "error" in results:
            break

        print(f"Currently extracting page #{results.get('serpapi_pagination', {}).get('current')}..")

        for result in results["organic_results"]:
            title = result.get("title")
            publication_info_summary = result["publication_info"]["summary"]
            result_id = result.get("result_id")
            link = result.get("link")
            result_type = result.get("type")
            snippet = result.get("snippet")

            try:
                file_title = result["resources"][0]["title"]
            except: file_title = None

            try:
                file_link = result["resources"][0]["link"]
            except: file_link = None

            try:
                file_format = result["resources"][0]["file_format"]
            except: file_format = None

            cited_by_count = result.get("inline_links", {}).get("cited_by", {}).get("total", {})
            cited_by_id = result.get("inline_links", {}).get("cited_by", {}).get("cites_id", {})
            cited_by_link = result.get("inline_links", {}).get("cited_by", {}).get("link", {})
            total_versions = result.get("inline_links", {}).get("versions", {}).get("total", {})
            all_versions_link = result.get("inline_links", {}).get("versions", {}).get("link", {})
            all_versions_id = result.get("inline_links", {}).get("versions", {}).get("cluster_id", {})

            case_law_results_data.append({
                "page_number": results['serpapi_pagination']['current'],
                "position": result["position"] + 1,
                "result_type": result_type,
                "title": title,
                "link": link,
                "result_id": result_id,
                "publication_info_summary": publication_info_summary,
                "snippet": snippet,
                "cited_by_count": cited_by_count,
                "cited_by_link": cited_by_link,
                "cited_by_id": cited_by_id,
                "file_format": file_format,
                "file_title": file_title,
                "file_link": file_link
            })

        if "next" in results.get("serpapi_pagination", {}):
            search.params_dict.update(dict(parse_qsl(urlsplit(results["serpapi_pagination"]["next"]).query)))
        else:
            break

    return case_law_results_data

