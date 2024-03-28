# Court Case PageRank
## Overview
Making a PageRank for court cases. Might also implement a google search algorithm
Approach will be to link the cases with theri references. 
1. We will webscrape the google scholar case website and get the how cited from each website.
2. We will use unique caseid as the identifier

Normal PR: keep going with prob. delt, teleport with prob delt uniformly
Our pr: since cant go from old to new cases by time. 


## References
<https://kristery.github.io/docs/WSDMCup2016_paper_7.pdf>
<https://link.springer.com/content/pdf/10.1007/s11192-007-1908-4.pdf>


cases dict : 
{
    cases: {
        id: 
    }
}

<h3 class="gs_rt" ontouchstart="gs_evt_dsp(event)"><img src="/intl/en/scholar/images/1x/lod3.png" srcset="/intl/en/scholar/images/2x/lod3.png 1.5x" alt="Discusses cited case at length" title="Discusses cited case at length" height="14" width="18"><a id="IWfMvRyhNYgJ" href="/scholar_case?case=9814928107739309857&amp;hl=en&amp;as_sdt=40000005&amp;sciodt=40000006">Schumacher v. SC DATA CENTER, INC.</a></h3>
<img src="/intl/en/scholar/images/1x/lod3.png" srcset="/intl/en/scholar/images/2x/lod3.png 1.5x" alt="Discusses cited case at length" title="Discusses cited case at length" height="14" width="18">
