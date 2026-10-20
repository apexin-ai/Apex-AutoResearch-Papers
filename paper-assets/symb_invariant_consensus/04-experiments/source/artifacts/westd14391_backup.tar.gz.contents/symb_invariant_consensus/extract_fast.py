"""Fast parallel constraint extraction using both vLLM servers."""
import json, os, sys, time, re
from concurrent.futures import ThreadPoolExecutor, as_completed
import httpx

sys.path.insert(0, '/root/symb_invariant_consensus')
from sica.constraint_extractor import LOGIC_EXTRACTION_PROMPT

SERVERS = [
    ("http://localhost:8001/v1", None),
    ("http://localhost:8002/v1", None),
]

# Get model IDs
for i, (base, _) in enumerate(SERVERS):
    r = httpx.get(f'{base}/models')
    mid = r.json()['data'][0]['id']
    SERVERS[i] = (base, mid)
    print(f'Server {i}: {base} model={mid}', flush=True)

INTERMEDIATES_DIR = '/root/symb_invariant_consensus/results/folio_204_14b/intermediates'
CONSTRAINTS_DIR = '/root/symb_invariant_consensus/results/folio_204_14b/per_trace_constraints'
RESULTS_FILE = '/root/symb_invariant_consensus/results/folio_204_14b/folio_204_results.json'
os.makedirs(CONSTRAINTS_DIR, exist_ok=True)

def normalize(ans):
    ans = str(ans).strip().lower()
    if ans in ('true', 'yes', 't'): return 'True'
    elif ans in ('false', 'no', 'f'): return 'False'
    elif ans in ('unknown', 'uncertain', 'u', 'undetermined'): return 'Unknown'
    return ans.capitalize()

def extract_one(trace_text, server_idx):
    base, model_id = SERVERS[server_idx % len(SERVERS)]
    prompt = LOGIC_EXTRACTION_PROMPT.format(trace=trace_text[:5000])
    payload = {
        'model': model_id,
        'messages': [{'role': 'user', 'content': prompt}],
        'max_tokens': 1500,
        'temperature': 0.1,
    }
    try:
        with httpx.Client(timeout=90) as client:
            resp = client.post(f'{base}/chat/completions', json=payload)
            resp.raise_for_status()
        raw = resp.json()['choices'][0]['message']['content']
        text = re.sub(r'<think>.*?</think>', '', raw, flags=re.DOTALL).strip()
        m = re.search(r'\{[\s\S]*\}', text)
        if not m:
            return {'error': 'no JSON', 'constraints': []}
        data = json.loads(m.group())
        return {'constraints': data.get('constraints', []), 'extracted_answer': data.get('answer', '')}
    except json.JSONDecodeError:
        return {'error': 'JSON parse', 'constraints': []}
    except Exception as e:
        return {'error': str(e)[:150], 'constraints': []}

def process_one_trace(args):
    pid, trace_idx, trace_text, answer, server_idx = args
    result = extract_one(trace_text, server_idx)
    return pid, trace_idx, answer, result

# Load problems
with open(RESULTS_FILE) as f:
    results_data = json.load(f)

# Build task list: all (pid, trace_idx, trace_text) tuples
all_tasks = []
skip_pids = set()
for r in results_data['results']:
    pid = r['problem_id']
    out_file = os.path.join(CONSTRAINTS_DIR, f'{pid}.json')
    if os.path.exists(out_file):
        try:
            existing = json.load(open(out_file))
            if any(len(t.get('constraints',[])) > 0 for t in existing.get('per_trace',[])):
                skip_pids.add(pid)
                continue
        except:
            pass
    
    with open(os.path.join(INTERMEDIATES_DIR, f'{pid}.json')) as f:
        intermed = json.load(f)
    traces = intermed['sica_result']['traces']
    for ti, t in enumerate(traces):
        all_tasks.append((pid, t['trace_idx'], t['trace'], normalize(t['answer']), ti % len(SERVERS)))

print(f'Tasks: {len(all_tasks)} traces from {len(all_tasks)//12} problems (skipping {len(skip_pids)} already done)', flush=True)

# Process in parallel
t_start = time.time()
done = 0
results_map = {}

with ThreadPoolExecutor(max_workers=8) as executor:
    futures = {executor.submit(process_one_trace, task): task for task in all_tasks}
    for future in as_completed(futures):
        pid, trace_idx, answer, result = future.result()
        if pid not in results_map:
            results_map[pid] = {}
        results_map[pid][trace_idx] = {
            'trace_idx': trace_idx,
            'answer': answer,
            'constraints': result.get('constraints', []),
            'extracted_answer': result.get('extracted_answer', ''),
            'error': result.get('error'),
        }
        done += 1
        
        # Check if problem is complete
        if len(results_map[pid]) == 12:
            gt = normalize(next(r['ground_truth'] for r in results_data['results'] if r['problem_id'] == pid))
            per_trace = [results_map[pid][i] for i in sorted(results_map[pid].keys())]
            with open(os.path.join(CONSTRAINTS_DIR, f'{pid}.json'), 'w') as f:
                json.dump({'pid': pid, 'gt': gt, 'per_trace': per_trace}, f, indent=2)
        
        if done % 48 == 0:
            elapsed = time.time() - t_start
            rate = done / elapsed
            eta = (len(all_tasks) - done) / rate / 60
            print(f'[{done}/{len(all_tasks)}] {rate:.1f} traces/s  ETA={eta:.1f}min', flush=True)

elapsed = time.time() - t_start
print(f'\nDone: {done} traces in {elapsed:.1f}s ({done/elapsed:.1f} traces/s)', flush=True)

# Quality
total_c = 0; empty = 0; errors = 0; n_traces = 0
for r in results_data['results']:
    fn = os.path.join(CONSTRAINTS_DIR, f"{r['problem_id']}.json")
    if not os.path.exists(fn): continue
    d = json.load(open(fn))
    for t in d['per_trace']:
        n_traces += 1
        nc = len(t.get('constraints', []))
        total_c += nc
        if nc == 0: empty += 1
        if t.get('error'): errors += 1

print(f'Total: {total_c} constraints ({total_c/max(n_traces,1):.1f}/trace)', flush=True)
print(f'Empty: {empty}/{n_traces} ({empty/max(n_traces,1)*100:.1f}%)  Errors: {errors}', flush=True)
print('EXTRACTION_COMPLETE', flush=True)
