import urllib.request, json, ssl, time

ctx = ssl.create_default_context()

url = 'https://raw.githubusercontent.com/Yale-LILY/FOLIO/main/data/v0.0/folio-validation.jsonl'

for attempt in range(3):
    try:
        print(f"Attempt {attempt+1}...")
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        resp = urllib.request.urlopen(req, timeout=30, context=ctx)
        raw = resp.read().decode('utf-8')
        break
    except Exception as e:
        print(f"  Failed: {e}")
        if attempt < 2:
            time.sleep(3)
        else:
            raise

raw_lines = [l for l in raw.strip().split('\n') if l.strip()]
print(f"Downloaded {len(raw_lines)} lines")

items = []
answer_map = {"True": "True", "False": "False", "Uncertain": "Unknown"}

for i, line in enumerate(raw_lines):
    row = json.loads(line)
    premises = row['premises']
    if isinstance(premises, list):
        premises_text = ' '.join(premises)
    else:
        premises_text = str(premises)
    
    conclusion = row['conclusion']
    label = row['label']
    
    problem = "Given the following premises:\n" + premises_text.strip() + "\n\nDetermine whether the following conclusion is true, false, or uncertain:\n" + conclusion.strip()
    
    item = {
        "id": "folio_" + str(i),
        "problem": problem,
        "solution": "",
        "answer": answer_map.get(label, label),
        "level": "validation",
    }
    
    if 'premises-FOL' in row:
        item['premises_fol'] = row['premises-FOL']
    if 'conclusion-FOL' in row:
        item['conclusion_fol'] = row['conclusion-FOL']
    
    items.append(item)

with open('/root/symb_invariant_consensus/data/folio_full.json', 'w') as f:
    json.dump(items, f, indent=2)

print(f"FOLIO: {len(items)} problems saved")
ans_dist = {}
for x in items:
    a = x['answer']
    ans_dist[a] = ans_dist.get(a, 0) + 1
print(f"Answer distribution: {ans_dist}")
print(f"Sample keys: {list(items[0].keys())}")
