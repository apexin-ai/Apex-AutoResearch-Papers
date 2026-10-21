"""Re-extract constraints - requests lib, better logging, save-as-you-go."""
import json, os, sys, time, random, re, requests
from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import Lock

sys.path.insert(0, "/root/symb_invariant_consensus")
from sica.constraint_extractor import LOGIC_EXTRACTION_PROMPT

CONSTRAINTS_DIR = "/root/symb_invariant_consensus/results/folio_204_14b/per_trace_constraints"
INTERMEDIATES = "/root/symb_invariant_consensus/results/folio_204_14b/intermediates"
MODEL_ID = "/root/autodl-tmp/models/Qwen3-14B"
PORTS = [8001, 8002]

file_lock = Lock()
counter = {"done": 0, "errors": 0}
counter_lock = Lock()

def parse_constraints(text):
    constraints = []
    for m in re.finditer(r'\{[^}]*"type"[^}]*"z3_formula"[^}]*\}', text, re.DOTALL):
        try:
            c = json.loads(m.group())
            if "z3_formula" in c and "expression" in c:
                constraints.append(c)
        except: pass
    if not constraints:
        for m in re.finditer(r'\{[^}]*"expression"[^}]*\}', text, re.DOTALL):
            try:
                c = json.loads(m.group())
                if "expression" in c:
                    constraints.append(c)
            except: pass
    return constraints

def extract_trace(pid, trace_idx, trace_text, problem_text, worker_id, t0, total):
    port = PORTS[worker_id % len(PORTS)]
    prompt = LOGIC_EXTRACTION_PROMPT.format(trace=trace_text[:5000], problem=problem_text[:2000])
    url = f"http://localhost:{port}/v1/chat/completions"
    constraints = []
    error = None
    try:
        resp = requests.post(url, json={
            "model": MODEL_ID,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.0, "max_tokens": 2048,
        }, timeout=120)
        resp.raise_for_status()
        raw = resp.json()["choices"][0]["message"]["content"]
        constraints = parse_constraints(raw)
    except Exception as e:
        error = str(e)[:200]
    
    with counter_lock:
        counter["done"] += 1
        if error: counter["errors"] += 1
        d = counter["done"]
        if d % 50 == 0 or d <= 10:
            elapsed = time.time() - t0
            rate = d / elapsed if elapsed > 0 else 0
            eta_s = (total - d) / rate if rate > 0 else 0
            print(f"  [{d}/{total}] rate={rate:.1f}/s  ETA={eta_s/60:.1f}min  errors={counter['errors']}", flush=True)
    
    return pid, trace_idx, constraints, error

def main():
    # Collect all traces needing re-extraction
    tasks = []
    problem_meta = {}  # pid -> gt
    
    for fname in sorted(os.listdir(CONSTRAINTS_DIR)):
        if not fname.endswith(".json"): continue
        pid = fname.replace(".json", "")
        cfile = os.path.join(CONSTRAINTS_DIR, fname)
        cdata = json.load(open(cfile))
        
        error_indices = [i for i, t in enumerate(cdata.get("per_trace", [])) if t.get("error")]
        if not error_indices:
            continue
        
        ifile = os.path.join(INTERMEDIATES, f"{pid}.json")
        idata = json.load(open(ifile))
        problem_text = idata["problem"].get("problem", "")
        traces = idata["sica_result"]["traces"]
        
        problem_meta[pid] = cdata["gt"]
        
        for i in error_indices:
            t = cdata["per_trace"][i]
            tasks.append({
                "pid": pid, "trace_idx": i,
                "trace_text": traces[i]["trace"],
                "problem_text": problem_text,
                "answer": t.get("answer", ""),
            })
    
    total = len(tasks)
    print(f"Re-extracting {total} traces across {len(problem_meta)} problems", flush=True)
    t0 = time.time()
    
    # Collect results by pid
    results_by_pid = {}  # pid -> {trace_idx: (constraints, error)}
    
    with ThreadPoolExecutor(max_workers=16) as pool:
        futures = {}
        for i, task in enumerate(tasks):
            fut = pool.submit(
                extract_trace,
                task["pid"], task["trace_idx"],
                task["trace_text"], task["problem_text"],
                i, t0, total
            )
            futures[fut] = task
        
        for fut in as_completed(futures):
            task = futures[fut]
            try:
                pid, trace_idx, constraints, error = fut.result()
                if pid not in results_by_pid:
                    results_by_pid[pid] = {}
                results_by_pid[pid][trace_idx] = (constraints, error)
            except Exception as e:
                pid = task["pid"]
                trace_idx = task["trace_idx"]
                if pid not in results_by_pid:
                    results_by_pid[pid] = {}
                results_by_pid[pid][trace_idx] = ([], str(e)[:200])
    
    elapsed = time.time() - t0
    print(f"\nExtraction done: {total} traces in {elapsed:.1f}s ({total/elapsed:.1f}/s)", flush=True)
    
    # Update constraint files
    for pid, trace_results in results_by_pid.items():
        cfile = os.path.join(CONSTRAINTS_DIR, f"{pid}.json")
        cdata = json.load(open(cfile))
        for trace_idx, (constraints, error) in trace_results.items():
            t = cdata["per_trace"][trace_idx]
            t["constraints"] = constraints
            t["error"] = error
        with open(cfile, "w") as f:
            json.dump(cdata, f, indent=2)
    
    # Verify
    ok = 0; still_errors = 0
    for fname in sorted(os.listdir(CONSTRAINTS_DIR)):
        if not fname.endswith(".json"): continue
        d = json.load(open(os.path.join(CONSTRAINTS_DIR, fname)))
        if any(len(t.get("constraints",[])) > 0 for t in d.get("per_trace",[])):
            ok += 1
        if any(t.get("error") for t in d.get("per_trace",[])):
            still_errors += 1
    
    print(f"Problems with constraints: {ok}/204")
    print(f"Problems still with errors: {still_errors}")
    print("REEXTRACTION_COMPLETE", flush=True)

if __name__ == "__main__":
    main()
