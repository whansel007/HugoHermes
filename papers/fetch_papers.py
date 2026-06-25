import urllib.request
import xml.etree.ElementTree as ET
import json
import datetime

def get_papers(query, max_res):
    url = f"https://export.arxiv.org/api/query?search_query={query}&sortBy=submittedDate&sortOrder=descending&max_results={max_res}"
    with urllib.request.urlopen(url) as response:
        root = ET.parse(response).getroot()
    
    ns = {'a': 'http://www.w3.org/2005/Atom'}
    papers = []
    for entry in root.findall('a:entry', ns):
        title = entry.find('a:title', ns).text.strip().replace('\n', ' ')
        arxiv_id = entry.find('a:id', ns).text.strip().split('/abs/')[-1]
        summary = entry.find('a:summary', ns).text.strip()[:200].replace('\n', ' ') + '...'
        papers.append({'title': title, 'id': arxiv_id, 'summary': summary})
    return papers

papers = get_papers("cat:cs.AI+OR+cat:cs.LG", 3)
# Just use one more from the same query for simplicity, 4th item
random_paper = get_papers("cat:cs.AI", 5)[4]
papers.append(random_paper)

print(json.dumps(papers))