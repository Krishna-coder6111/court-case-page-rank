import json

from serpapi.google_search import GoogleSearch
from scrape_case_law import case_law_results
from save_case_law import save_case_law_results_to_csv

print(json.dumps(case_law_results(), indent=3))
save_case_law_results_to_csv()
