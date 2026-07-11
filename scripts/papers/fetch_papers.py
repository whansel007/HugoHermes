from dotenv import load_dotenv
import urllib.request
import xml.etree.ElementTree as ET
import requests
import random
import os

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def send_message(message, chat_id, token):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id, 
        "text": message,
        "parse_mode": "HTML"}
    resp = requests.post(url, data=payload)
    resp.raise_for_status()
    return resp.json()

message = ""
def log(x):
    global message 
    message += x + "\n"

def log_paper(p, i=0):
    log(f"<b><a href='https://arxiv.org/abs/{p['id']}'>{i}. {p['title']}</a></b> <i>({p['primary_category']})</i>")
    log(f"<b>Abstract:</b>")
    log(f"{p['summary']} \n")

def get_papers(query, max_res):
    url = f"https://export.arxiv.org/api/query?search_query={query}&sortBy=submittedDate&sortOrder=descending&max_results={max_res}"
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "HermesAgent (w.hansel007@gmail.com)"}
    )
    
    with urllib.request.urlopen(req) as response:
        root = ET.parse(response).getroot()
    
    ns = {
        'a': 'http://www.w3.org/2005/Atom',
        'arxiv': 'http://arxiv.org/schemas/atom'
    }
    papers = []
    for entry in root.findall('a:entry', ns):
        title = entry.find('a:title', ns).text.strip().replace('\n', ' ')
        arxiv_id = entry.find('a:id', ns).text.strip().split('/abs/')[-1]
        summary = entry.find('a:summary', ns).text.strip()[:200].replace('\n', ' ') + '...'
        category_elem = entry.find('arxiv:primary_category', ns)
        primary_category = category_elem.get('term') if category_elem is not None else None
        papers.append({
            'title': title,
            'id': arxiv_id,
            'primary_category': primary_category,
            'summary': summary
        })
    return papers

# Grab the usual AI or Cybersecurity papers
papers = get_papers("cat:cs.AI+OR+cat:cs.LG+OR+cat:cs.CR", 3)

# Grab a random paper from a random field
CATEGORIES = [
    # Computer Science
    "cs.AI", "cs.AR", "cs.CC", "cs.CE", "cs.CG", "cs.CL", "cs.CR", "cs.CV",
    "cs.CY", "cs.DB", "cs.DC", "cs.DL", "cs.DM", "cs.DS", "cs.ET", "cs.FL",
    "cs.GL", "cs.GR", "cs.GT", "cs.HC", "cs.IR", "cs.IT", "cs.LG", "cs.LO",
    "cs.MA", "cs.MM", "cs.MS", "cs.NA", "cs.NE", "cs.NI", "cs.OH", "cs.OS",
    "cs.PF", "cs.PL", "cs.RO", "cs.SC", "cs.SD", "cs.SE", "cs.SI", "cs.SY",

    # Economics
    "econ.EM", "econ.GN", "econ.TH",

    # Electrical Engineering and Systems Science
    "eess.AS", "eess.IV", "eess.SP", "eess.SY",

    # Mathematics
    "math.AC", "math.AG", "math.AP", "math.AT", "math.CA", "math.CO",
    "math.CT", "math.CV", "math.DG", "math.DS", "math.FA", "math.GM",
    "math.GN", "math.GR", "math.GT", "math.HO", "math.IT", "math.KT",
    "math.LO", "math.MG", "math.MP", "math.NA", "math.NT", "math.OA",
    "math.OC", "math.PR", "math.QA", "math.RA", "math.RT", "math.SG",
    "math.SP", "math.ST",

    # Astrophysics
    "astro-ph.CO", "astro-ph.EP", "astro-ph.GA", "astro-ph.HE",
    "astro-ph.IM", "astro-ph.SR",

    # Condensed Matter
    "cond-mat.dis-nn", "cond-mat.mes-hall", "cond-mat.mtrl-sci",
    "cond-mat.other", "cond-mat.quant-gas", "cond-mat.soft",
    "cond-mat.stat-mech", "cond-mat.str-el", "cond-mat.supr-con",

    # General Relativity and Quantum Cosmology
    "gr-qc",

    # High Energy Physics
    "hep-ex", "hep-lat", "hep-ph", "hep-th",

    # Mathematical Physics
    "math-ph",

    # Nonlinear Sciences
    "nlin.AO", "nlin.CD", "nlin.CG", "nlin.PS", "nlin.SI",

    # Nuclear Physics
    "nucl-ex", "nucl-th",

    # Physics
    "physics.acc-ph", "physics.ao-ph", "physics.app-ph", "physics.atm-clus",
    "physics.atom-ph", "physics.bio-ph", "physics.chem-ph", "physics.class-ph",
    "physics.comp-ph", "physics.data-an", "physics.ed-ph", "physics.flu-dyn",
    "physics.gen-ph", "physics.geo-ph", "physics.hist-ph", "physics.ins-det",
    "physics.med-ph", "physics.optics", "physics.plasm-ph", "physics.pop-ph",
    "physics.soc-ph", "physics.space-ph",

    # Quantum Physics
    "quant-ph",

    # Quantitative Biology
    "q-bio.BM", "q-bio.CB", "q-bio.GN", "q-bio.MN", "q-bio.NC", "q-bio.OT",
    "q-bio.PE", "q-bio.QM", "q-bio.SC", "q-bio.TO",

    # Quantitative Finance
    "q-fin.CP", "q-fin.EC", "q-fin.GN", "q-fin.MF", "q-fin.PM", "q-fin.PR",
    "q-fin.RM", "q-fin.ST", "q-fin.TR",

    # Statistics
    "stat.AP", "stat.CO", "stat.ME", "stat.ML", "stat.OT", "stat.TH",
]
random_cat = CATEGORIES[random.randint(0, len(CATEGORIES)-1)]
random_paper = get_papers(f"cat:{random_cat}", 1)[0]
papers.append(random_paper)

# Print the paper info to be formatted
log("<b>🔎  Latest AI/CS/ML arXiv Papers :D</b>\n")
i = 1

for p in papers[:3]:
    log_paper(p,i)
    i+=1

log("<b>Wildcard paper! :O</b>")
log_paper(papers[-1],4)

# Send Message
send_message(message, chat_id=CHAT_ID, token=BOT_TOKEN)