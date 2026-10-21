"""Parallel per-trace constraint extraction from stored FOLIO 204 traces."""
import json, os, sys, time, re
from concurrent.futures import ThreadPoolExecutor, as_completed
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

client = httpx.Client(timeout=120)

def normalize(ans):
    ans = str(ans).strip().lower()
    if ans in ('true', 'yes', 't'): return 'True'
    elif ans in ('false', 'no', 'f'): return 'False'
    elif ans in ('unknown', 'uncertain', 'u', 'undetermined'): return 'Unknown'
    return ans.capitalize()

def extract_one(trace_text):
    prompt = LOGIC_EXTRACTION_PROMPT.format(trace=trace_text[:6000])
    payload = {
        'model': MODEL_ID,
        'messages': [{'role': 'user', 'content': prompt}],
        'max_tokens': 2048,
        'temperature': 0.1,
    }
    try:
        resp = client.post(f'{API_BASE}/chat/completions', json=payload)
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

def process_problem(pid, gt, traces):
    """Process all traces for one problem."""
    out_file = os.path.join(CONSTRAINTS_DIR, f'{pid}.json')
    
    # Check if already done (with non-error constraints)
    if os.path.exists(out_file):
        try:
            existing = json.load(open(out_file))
            has_data = any(len(t.get('constraints',[])) > 0 for t in existing.get('per_trace',[]))
            if has_data and len(existing.get('per_trace',[])) == len(traces):
                return pid, True  # skip
        except:
            pass
    
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
    
    with open(out_file, 'w') as f:
        json.dump({'pid': pid, 'gt': gt, 'per_trace': per_trace}, f, indent=2)
    
    nc = sum(len(t['constraints']) for t in per_trace)
    return pid, nc

# Load all problems
with open(RESULTS_FILE) as f:
    results_data = json.load(f)

os.makedirs(CONSTRAINTS_DIR, exist_ok=True)

tasks = []
for r in results_data['results']:
    pid = r['problem_id']
    with open(os.path.join(INTERMEDIATES_DIR, f'{pid}.json')) as f:
        intermed = json.load(f)
    tasks.append((pid, normalize(r['ground_truth']), intermed['sica_result']['traces']))

print(f'Processing {len(tasks)} problems with 4 parallel workers...', flush=True)
t_start = time.time()
done = 0
skipped = 0

with ThreadPoolExecutor(max_workers=4) as executor:
    futures = {executor.submit(process_problem, pid, gt, traces): pid for pid, gt, traces in tasks}
    for future in as_completed(futures):
        pid, result = future.result()
        done += 1
        if result is True:
            skipped += 1
        if done % 20 == 0:
            elapsed = time.time() - t_start
            rate = (done - skipped) / elapsed if elapsed > 0 and done > skipped else 0
            remaining = len(tasks) - done
            eta = remaining / rate / 60 if rate > 0 else 0
            print(f'[{done}/{len(tasks)}] skipped={skipped} rate={rate:.2f} prob/s  ETA={eta:.1f}min', flush=True)

elapsed = time.time() - t_start
print(f'\nDone: {done} problems ({skipped} skipped) in {elapsed:.1f}s', flush=True)

# Quality report
total_c = 0
empty = 0
errors = 0
n_traces = 0
for r in results_data['results']:
    d = json.load(open(os.path.join(CONSTRAINTS_DIR, f"{r['problem_id']}.json")))
    for t in d['per_trace']:
        n_traces += 1
        nc = len(t.get('constraints', []))
        total_c += nc
        if nc == 0: empty += 1
        if t.get('error'): errors += 1

print(f'Constraints: {total_c} ({total_c/n_traces:.1f}/trace)', flush=True)
print(f'Empty: {empty}/{n_traces} ({empty/n_traces*100:.1f}%)  Errors: {errors}', flush=True)
print('EXTRACTION_COMPLETE', flush=True)
