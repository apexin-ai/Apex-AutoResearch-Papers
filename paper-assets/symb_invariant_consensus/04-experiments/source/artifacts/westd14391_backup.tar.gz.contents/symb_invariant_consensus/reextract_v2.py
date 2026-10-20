"""Re-extract constraints - trace-level parallelism for better vLLM batching."""
import json, os, sys, time, httpx
from concurrent.futures import ThreadPoolExecutor, as_completed

sys.path.insert(0, "/root/symb_invariant_consensus")
from sica.constraint_extractor import LOGIC_EXTRACTION_PROMPT

CONSTRAINTS_DIR = "/root/symb_invariant_consensus/results/folio_204_14b/per_trace_constraints"
INTERMEDIATES = "/root/symb_invariant_consensus/results/folio_204_14b/intermediates"
MODEL_ID = "/root/autodl-tmp/models/Qwen3-14B"
PORTS = [8001, 8002]

def parse_constraints(text):
    import re
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

def extract_trace(args):
    pid, trace_idx, trace_text, problem_text, worker_id = args
    port = PORTS[worker_id % len(PORTS)]
    prompt = LOGIC_EXTRACTION_PROMPT.format(trace=trace_text[:5000], problem=problem_text[:2000])
    url = f"http://localhost:{port}/v1/chat/completions"
    try:
        resp = httpx.post(url, json={
            "model": MODEL_ID,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.0, "max_tokens": 2048,
        }, timeout=120)
        resp.raise_for_status()
        raw = resp.json()["choices"][0]["message"]["content"]
        constraints = parse_constraints(raw)
        return pid, trace_idx, constraints, None
    except Exception as e:
        return pid, trace_idx, [], str(e)

def main():
    # Collect all traces that need re-extraction
    tasks = []
    problem_data = {}  # pid -> {gt, per_trace, problem_text}
    
    for fname in sorted(os.listdir(CONSTRAINTS_DIR)):
        if not fname.endswith(".json"): continue
        pid = fname.replace(".json", "")
        cfile = os.path.join(CONSTRAINTS_DIR, fname)
        cdata = json.load(open(cfile))
        
        has_errors = any(t.get('error') for t in cdata.get('per_trace', []))
        if not has_errors:
            continue
        
        ifile = os.path.join(INTERMEDIATES, f"{pid}.json")
        idata = json.load(open(ifile))
        problem_text = idata["problem"].get("problem", "")
        traces = idata["sica_result"]["traces"]
        
        problem_data[pid] = {"gt": cdata["gt"], "per_trace": cdata["per_trace"]}
        
        for i, t in enumerate(cdata["per_trace"]):
            if t.get("error"):
                tasks.append((pid, i, traces[i]["trace"], problem_text, len(tasks)))
    
    print(f"Re-extracting {len(tasks)} traces across {len(problem_data)} problems", flush=True)
    t0 = time.time()
    
    results = {}  # (pid, trace_idx) -> (constraints, error)
    done = 0
    
    with ThreadPoolExecutor(max_workers=24) as pool:
        futures = {pool.submit(extract_trace, task): task[:2] for task in tasks}
        for fut in as_completed(futures):
            pid, trace_idx, constraints, error = fut.result()
            results[(pid, trace_idx)] = (constraints, error)
            done += 1
            if done % 100 == 0:
                elapsed = time.time() - t0
                rate = done / elapsed
                remaining = (len(tasks) - done) / rate
                print(f"  [{done}/{len(tasks)}] rate={rate:.1f} traces/s  ETA={remaining:.1f}min", flush=True)
    
    elapsed = time.time() - t0
    print(f"\nExtraction done: {done} traces in {elapsed:.1f}s ({done/elapsed:.1f} traces/s)", flush=True)
    
    # Update files
    errors = 0
    for pid, pdata in problem_data.items():
        per_trace = pdata["per_trace"]
        for i, t in enumerate(per_trace):
            if (pid, i) in results:
                constraints, error = results[(pid, i)]
                per_trace[i] = {
                    "trace_idx": t["trace_idx"],
                    "answer": t["answer"],
                    "constraints": constraints,
                    "extracted_answer": t.get("extracted_answer", ""),
                    "error": error,
                }
                if error: errors += 1
        
        cfile = os.path.join(CONSTRAINTS_DIR, f"{pid}.json")
        with open(cfile, "w") as f:
            json.dump({"pid": pid, "gt": pdata["gt"], "per_trace": per_trace}, f, indent=2)
    
    # Verify
    ok = 0
    for fname in sorted(os.listdir(CONSTRAINTS_DIR)):
        if not fname.endswith(".json"): continue
        d = json.load(open(os.path.join(CONSTRAINTS_DIR, fname)))
        if any(len(t.get("constraints",[])) > 0 for t in d.get("per_trace",[])):
            ok += 1
    
    print(f"Errors remaining: {errors}")
    print(f"Problems with constraints: {ok}/204", flush=True)
    print("REEXTRACTION_COMPLETE", flush=True)

if __name__ == "__main__":
    main()
