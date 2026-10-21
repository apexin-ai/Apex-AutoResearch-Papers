"""Extract per-trace constraints from LLaMA-8B FOLIO-204 intermediates (traces 0-3 only).
Uses existing Mistral-7B vLLM servers for extraction."""
import json, os, sys, time, re
from concurrent.futures import ThreadPoolExecutor, as_completed
import httpx

sys.path.insert(0, '/root/symb_invariant_consensus')
from sica.constraint_extractor import LOGIC_EXTRACTION_PROMPT

SERVERS = [
    'http://localhost:8020/v1',
    'http://localhost:8021/v1',
    'http://localhost:8012/v1',
    'http://localhost:8013/v1',
]

MODEL_IDS = []
for base in SERVERS:
    try:
        r = httpx.get(f'{base}/models', timeout=5)
        mid = r.json()['data'][0]['id']
        MODEL_IDS.append(mid)
        print(f'{base}: model={mid}')
    except Exception as e:
        MODEL_IDS.append(None)
        print(f'{base}: FAILED - {e}')

INTERMEDIATES_DIR = '/root/symb_invariant_consensus/results/exp-063-llama8b-folio204-16639/intermediates'
OUTPUT_FILE = '/root/symb_invariant_consensus/results/exp-063-llama8b-folio204-16639/llama_constraints_t0t3.json'
TRACES_TO_EXTRACT = [0, 1, 2, 3]

def normalize(ans):
    ans = str(ans).strip().lower()
    if ans in ('true', 'yes', 't'): return 'True'
    elif ans in ('false', 'no', 'f'): return 'False'
    elif ans in ('unknown', 'uncertain', 'u', 'undetermined'): return 'Unknown'
    return ans.capitalize()

def extract_one(trace_text, server_idx):
    base = SERVERS[server_idx % len(SERVERS)]
    model_id = MODEL_IDS[server_idx % len(MODEL_IDS)]
    if not model_id:
        return {'error': 'server down', 'constraints': []}
    prompt = LOGIC_EXTRACTION_PROMPT.format(trace=trace_text[:5000])
    payload = {
        'model': model_id,
        'messages': [{'role': 'user', 'content': prompt}],
        'max_tokens': 1500,
        'temperature': 0.1,
    }
    try:
        with httpx.Client(timeout=120) as client:
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

def process_task(args):
    pid, trace_idx, trace_text, answer, task_id = args
    result = extract_one(trace_text, task_id)
    return pid, trace_idx, answer, result

all_tasks = []
pid_gt = {}
for i in range(204):
    fp = os.path.join(INTERMEDIATES_DIR, f'folio_{i}.json')
    if not os.path.exists(fp):
        print(f'MISSING: {fp}')
        continue
    with open(fp) as f:
        data = json.load(f)
    pid = data['problem']['id']
    gt = data['problem']['answer']
    pid_gt[pid] = normalize(gt)
    traces = data['sica_result']['traces']
    trace_map = {t['trace_idx']: t for t in traces}
    for tidx in TRACES_TO_EXTRACT:
        if tidx in trace_map:
            t = trace_map[tidx]
            all_tasks.append((pid, tidx, t['trace'], normalize(t.get('answer', '')), len(all_tasks)))

print(f'Total tasks: {len(all_tasks)} ({len(pid_gt)} problems x {len(TRACES_TO_EXTRACT)} traces)')
t_start = time.time()

results = {}
done = 0
errors = 0
with ThreadPoolExecutor(max_workers=16) as pool:
    futures = {pool.submit(process_task, task): task for task in all_tasks}
    for fut in as_completed(futures):
        pid, trace_idx, answer, result = fut.result()
        if pid not in results:
            results[pid] = {'pid': pid, 'gt': pid_gt[pid], 'per_trace': []}
        results[pid]['per_trace'].append({
            'trace_idx': trace_idx,
            'answer': answer,
            'constraints': result.get('constraints', []),
        })
        done += 1
        if result.get('error'):
            errors += 1
        if done % 100 == 0:
            elapsed = time.time() - t_start
            rate = done / elapsed
            eta = (len(all_tasks) - done) / rate if rate > 0 else 0
            print(f'  {done}/{len(all_tasks)} done, {rate:.1f}/s, ETA {eta:.0f}s, errors={errors}', flush=True)

for pid in results:
    results[pid]['per_trace'].sort(key=lambda x: x['trace_idx'])

with open(OUTPUT_FILE, 'w') as f:
    json.dump(results, f, indent=2)

elapsed = time.time() - t_start
n_constraints = sum(len(c) for p in results.values() for t in p['per_trace'] for c in [t['constraints']])
print(f'Done: {len(results)} problems, {done} traces, {n_constraints} constraints, {errors} errors, {elapsed:.1f}s')
print(f'Saved to {OUTPUT_FILE}')
