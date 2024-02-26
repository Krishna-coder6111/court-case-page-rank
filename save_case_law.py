import pandas as pd
from scrape_case_law import case_law_results

def save_case_law_results_to_csv():
    print("Waiting for case law results to save..")
    pd.DataFrame(data=case_law_results()).to_csv("google_scholar_case_law_results.csv", encoding="utf-8", index=False)

    print("Case Law Results Saved.")