import json, os, sys, time, re
import httpx

sys.path.insert(0, '/root/symb_invariant_consensus')
from sica.constraint_extractor import LOGIC_EXTRACTION_PROMPT

API_BASE = 'http://localhost:8001/v1'
INTERMEDIATES_DIR = '/root/symb_invariant_consensus/results/folio_204_14b/intermediates'
CONSTRAINTS_DIR = '/root/symb_invariant_consensus/results/folio_204_14b/per_trace_constraints'
RESULTS_FILE = '/root/symb_invariant_consensus/results/folio_204_14b/folio_204_results.json'

r = httpx.get(f'{API_BASE}/models')
MODEL_ID = r.json()['data'][0]['id']
print(f'Model: {MODEL_ID}', flush=True)

def normalize(ans):
    ans = str(ans).strip().lower()
    if ans in ('true', 'yes', 't'): return 'True'
    elif ans in ('false', 'no', 'f'): return 'False'
    elif ans in ('unknown', 'uncertain', 'u', 'undetermined'): return 'Unknown'
    return ans.capitalize()

def extract_one(trace_text):
    prompt = LOGIC_EXTRACTION_PROMPT.format(trace=trace_text)
    payload = {
        'model': MODEL_ID,
        'messages': [{'role': 'user', 'content': prompt}],
        'max_tokens': 2048,
        'temperature': 0.1,
    }
    try:
        resp = httpx.post(f'{API_BASE}/chat/completions', json=payload, timeout=120)
        resp.raise_for_status()
        raw = resp.json()['choices'][0]['message']['content']
        text = re.sub(r'<think>.*?</think>', '', raw, flags=re.DOTALL).strip()
        json_match = re.search(r'\{[\s\S]*\}', text)
        if not json_match:
            return {'error': 'no JSON', 'constraints': []}
        data = json.loads(json_match.group())
        return {'constraints': data.get('constraints', []), 'extracted_answer': data.get('answer', '')}
    except json.JSONDecodeError:
        return {'error': 'JSON parse', 'constraints': []}
    except Exception as e:
        return {'error': str(e)[:200], 'constraints': []}

with open(RESULTS_FILE) as f:
    results_data = json.load(f)

os.makedirs(CONSTRAINTS_DIR, exist_ok=True)
t_start = time.time()
done = 0
total = 204 * 12

for ri, r in enumerate(results_data['results']):
    pid = r['problem_id']
    out_file = os.path.join(CONSTRAINTS_DIR, f'{pid}.json')
    
    with open(os.path.join(INTERMEDIATES_DIR, f'{pid}.json')) as f:
        intermed = json.load(f)
    traces = intermed['sica_result']['traces']
    
    per_trace = []
    for t in traces:
        result = extract_one(t['trace'])
        per_trace.append({
            'trace_idx': t['trace_idx'],
            'answer': normalize(t['answer']),
            'constraints': result.get('constraints', []),
            'extracted_answer': result.get('extracted_answer', ''),
            'error': result.get('error'),
        })
        done += 1
    
    with open(out_file, 'w') as f:
        json.dump({'pid': pid, 'gt': normalize(r['ground_truth']), 'per_trace': per_trace}, f, indent=2)
    
    if (ri + 1) % 10 == 0:
        elapsed = time.time() - t_start
        rate = done / elapsed
        eta = (total - done) / rate
        nc = sum(len(t['constraints']) for t in per_trace)
        print(f'[{ri+1}/204] {done}/{total} traces  {rate:.1f}/s  ETA={eta:.0f}s  last_constraints={nc}', flush=True)

elapsed = time.time() - t_start
print(f'Done: {done} traces in {elapsed:.1f}s ({done/elapsed:.1f}/s)', flush=True)

total_c = 0
empty = 0
for r in results_data['results']:
    d = json.load(open(os.path.join(CONSTRAINTS_DIR, f"{r['problem_id']}.json")))
    for t in d['per_trace']:
        nc = len(t.get('constraints', []))
        total_c += nc
        if nc == 0: empty += 1

print(f'Constraints: {total_c} ({total_c/done:.1f}/trace)  Empty: {empty}/{done}', flush=True)
print('EXTRACTION_COMPLETE', flush=True)
