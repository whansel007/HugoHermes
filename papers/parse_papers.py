import xml.etree.ElementTree as ET

ns = {'a': 'http://www.w3.org/2005/Atom'}
tree = ET.parse('papers.xml')
root = tree.getroot()
for entry in root.findall('a:entry', ns):
    title = entry.find('a:title', ns).text.strip().replace('\n', ' ')
    arxiv_id = entry.find('a:id', ns).text.strip().split('/abs/')[-1]
    summary = entry.find('a:summary', ns).text.strip().replace('\n', ' ')
    print(f'TITLE: {title}')
    print(f'ID: {arxiv_id}')
    print(f'SUMMARY: {summary}')
    print('---')
