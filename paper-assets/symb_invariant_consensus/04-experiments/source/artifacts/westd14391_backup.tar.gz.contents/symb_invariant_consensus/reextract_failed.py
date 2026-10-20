"""Re-extract constraints for problems that had errors (404 from downed vLLM)."""
import json, os, sys, time, httpx
from concurrent.futures import ThreadPoolExecutor, as_completed

sys.path.insert(0, "/root/symb_invariant_consensus")
from sica.constraint_extractor import LOGIC_EXTRACTION_PROMPT

CONSTRAINTS_DIR = "/root/symb_invariant_consensus/results/folio_204_14b/per_trace_constraints"
INTERMEDIATES = "/root/symb_invariant_consensus/results/folio_204_14b/intermediates"
MODEL_ID = "/root/autodl-tmp/models/Qwen3-14B"
PORTS = [8001, 8002]

def needs_reextract(cfile):
    d = json.load(open(cfile))
    return any(t.get('error') for t in d.get('per_trace', []))

def extract_one(trace_text, problem_text, port):
    prompt = LOGIC_EXTRACTION_PROMPT.format(trace=trace_text[:5000], problem=problem_text[:2000])
    url = f"http://localhost:{port}/v1/chat/completions"
    resp = httpx.post(url, json={
        "model": MODEL_ID,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.0, "max_tokens": 2048,
    }, timeout=120)
    resp.raise_for_status()
    return resp.json()["choices"][0]["message"]["content"]

def parse_constraints(text):
    constraints = []
    import re
    for m in re.finditer(r'\{[^}]*"type"[^}]*"z3_formula"[^}]*\}', text, re.DOTALL):
        try:
            c = json.loads(m.group())
            if "z3_formula" in c and "expression" in c:
                constraints.append(c)
        except:
            pass
    if not constraints:
        for m in re.finditer(r'\{[^}]*"expression"[^}]*\}', text, re.DOTALL):
            try:
                c = json.loads(m.group())
                if "expression" in c:
                    constraints.append(c)
            except:
                pass
    return constraints

def process_problem(pid, port_idx):
    port = PORTS[port_idx % len(PORTS)]
    ifile = os.path.join(INTERMEDIATES, f"{pid}.json")
    cfile = os.path.join(CONSTRAINTS_DIR, f"{pid}.json")
    
    idata = json.load(open(ifile))
    problem_text = idata["problem"].get("problem", "")
    traces = idata["sica_result"]["traces"]
    
    old = json.load(open(cfile))
    per_trace = old["per_trace"]
    
    updated = 0
    for i, t in enumerate(per_trace):
        if not t.get("error"):
            continue
        trace_text = traces[i]["trace"]
        try:
            raw = extract_one(trace_text, problem_text, port)
            constraints = parse_constraints(raw)
            per_trace[i] = {
                "trace_idx": t["trace_idx"],
                "answer": t["answer"],
                "constraints": constraints,
                "extracted_answer": t.get("extracted_answer", ""),
                "error": None,
            }
            updated += 1
        except Exception as e:
            per_trace[i]["error"] = str(e)
    
    with open(cfile, "w") as f:
        json.dump({"pid": pid, "gt": old["gt"], "per_trace": per_trace}, f, indent=2)
    return pid, updated

def main():
    failed = []
    for fname in sorted(os.listdir(CONSTRAINTS_DIR)):
        if not fname.endswith(".json"): continue
        cfile = os.path.join(CONSTRAINTS_DIR, fname)
        if needs_reextract(cfile):
            failed.append(fname.replace(".json", ""))
    
    print(f"Re-extracting {len(failed)} problems with errors", flush=True)
    t0 = time.time()
    done = 0
    
    with ThreadPoolExecutor(max_workers=8) as pool:
        futures = {pool.submit(process_problem, pid, i): pid 
                   for i, pid in enumerate(failed)}
        for fut in as_completed(futures):
            pid = futures[fut]
            try:
                _, updated = fut.result()
                done += 1
                if done % 20 == 0:
                    elapsed = time.time() - t0
                    rate = done / elapsed if elapsed > 0 else 0
                    remaining = (len(failed) - done) / rate if rate > 0 else 0
                    print(f"  [{done}/{len(failed)}] rate={rate:.1f}/prob ETA={remaining:.1f}min", flush=True)
            except Exception as e:
                done += 1
                print(f"  FAIL {pid}: {e}", flush=True)
    
    elapsed = time.time() - t0
    print(f"\nRe-extraction done: {done} problems in {elapsed:.1f}s", flush=True)
    
    # Verify
    ok = 0
    for fname in sorted(os.listdir(CONSTRAINTS_DIR)):
        if not fname.endswith(".json"): continue
        d = json.load(open(os.path.join(CONSTRAINTS_DIR, fname)))
        if any(len(t.get("constraints",[])) > 0 for t in d.get("per_trace",[])):
            ok += 1
    print(f"Problems with constraints: {ok}/204", flush=True)
    print("REEXTRACTION_COMPLETE", flush=True)

if __name__ == "__main__":
    main()
