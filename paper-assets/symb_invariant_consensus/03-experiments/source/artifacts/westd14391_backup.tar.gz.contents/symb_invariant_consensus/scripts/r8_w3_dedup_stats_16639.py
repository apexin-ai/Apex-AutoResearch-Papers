import json, os, glob, statistics

CONDITIONS = [
    {"label": "Qwen2.5-14B / FOLIO", "model": "Qwen2.5-14B", "domain": "FOLIO",
     "path": "/root/symb_invariant_consensus/results/exp036_qwen25_14b_folio204/intermediates/"},
    {"label": "LLaMA-3.1-8B / FOLIO", "model": "LLaMA-3.1-8B", "domain": "FOLIO",
     "path": "/root/symb_invariant_consensus/results/exp-063-llama8b-folio204-16639/intermediates/"},
    {"label": "Qwen2.5-14B / PW", "model": "Qwen2.5-14B", "domain": "ProofWriter",
     "path": "/root/symb_invariant_consensus/results/exp032_qwen25_14b_pw600/intermediates/"},
    {"label": "LLaMA-3.1-8B / PW", "model": "LLaMA-3.1-8B", "domain": "ProofWriter",
     "path": "/root/symb_invariant_consensus/results/exp048_llama8b_pw600/intermediates/"},
    {"label": "Qwen3-14B / FOLIO", "model": "Qwen3-14B", "domain": "FOLIO",
     "path": "/root/symb_invariant_consensus/results/exp028b_qwen3_thinking_folio204/intermediates/"},
    {"label": "DeepSeek-R1-8B / FOLIO", "model": "DeepSeek-R1-8B", "domain": "FOLIO",
     "path": "/root/symb_invariant_consensus/results/exp064_deepseek_r1_qwen3_8b_folio204/intermediates/"},
]

out_dir = "/root/symb_invariant_consensus/results/r8_w3_dedup_statistics"
os.makedirs(out_dir, exist_ok=True)

results = []
for cond in CONDITIONS:
    path = cond["path"]
    if not os.path.isdir(path):
        print(f"SKIP (not found): {cond['label']} -> {path}")
        continue
    files = sorted(glob.glob(os.path.join(path, "*.json")))
    if not files:
        print(f"SKIP (empty): {cond['label']}")
        continue

    per_problem = []
    missing_stats = 0
    for f in files:
        pid = os.path.splitext(os.path.basename(f))[0]
        try:
            d = json.load(open(f))
        except Exception:
            continue
        cs = d.get("sica_result", {}).get("constraints_stats")
        if not cs or "total_extracted" not in cs:
            missing_stats += 1
            continue
        pre = cs["total_extracted"]
        post = cs["unique_after_dedup"]
        n_traces = cs.get("traces_with_constraints", 0)
        ratio = 1.0 - (post / pre) if pre > 0 else 0.0
        avg_per_trace = pre / n_traces if n_traces > 0 else 0.0
        per_problem.append({
            "problem_id": pid,
            "pre": pre,
            "post": post,
            "ratio": round(ratio, 4),
            "n_traces": n_traces,
            "avg_per_trace": round(avg_per_trace, 2),
        })

    if not per_problem:
        print(f"SKIP (no valid data): {cond['label']}")
        continue

    pres = [p["pre"] for p in per_problem]
    posts = [p["post"] for p in per_problem]
    ratios = [p["ratio"] for p in per_problem]
    per_traces = [p["avg_per_trace"] for p in per_problem]

    entry = {
        "model": cond["model"],
        "domain": cond["domain"],
        "label": cond["label"],
        "n_problems": len(per_problem),
        "missing_stats": missing_stats,
        "avg_pre_dedup": round(statistics.mean(pres), 2),
        "avg_post_dedup": round(statistics.mean(posts), 2),
        "avg_dedup_ratio": round(statistics.mean(ratios), 4),
        "median_dedup_ratio": round(statistics.median(ratios), 4),
        "std_dedup_ratio": round(statistics.stdev(ratios), 4) if len(ratios) > 1 else 0.0,
        "avg_per_trace": round(statistics.mean(per_traces), 2),
        "total_pre_dedup": sum(pres),
        "total_post_dedup": sum(posts),
        "overall_dedup_ratio": round(1.0 - sum(posts) / sum(pres), 4) if sum(pres) > 0 else 0.0,
        "per_problem": per_problem,
    }
    results.append(entry)
    print(f"OK: {cond['label']} — {len(per_problem)} problems, "
          f"avg pre={entry['avg_pre_dedup']}, avg post={entry['avg_post_dedup']}, "
          f"dedup ratio={entry['avg_dedup_ratio']:.2%}, avg/trace={entry['avg_per_trace']}")

with open(os.path.join(out_dir, "results_16639.json"), "w") as f:
    json.dump(results, f, indent=2)

print(f"\nSaved to {out_dir}/results_16639.json")
