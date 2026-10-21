"""Compute LP-best F1 vs Greedy F1 for N-scaling analysis (micro-average)."""
import json, os, sys

DATA_ROOT = "/root/autodl-tmp/struct_self_consist_ie/output"
CONFIGS = [
    ("SciERC", 8, "scierc_mf4v2_seed42", 42),
    ("SciERC", 16, "exp_001_seed42_v2", 42),
    ("SciERC", 32, "scierc_n32_s42", 42),
    ("SciERC", 64, "scierc_n64_seed42", 42),
    ("CoNLL", 8, "conll_mf4v2_seed123", 123),
    ("CoNLL", 16, "conll_n16_s456", 456),
    ("CoNLL", 32, "conll_n32_s42", 42),
    ("CoNLL", 64, "conll_n64_seed42", 42),
    ("FewNERD", 8, "fewnerd_mf4v2_seed42_v3", 42),
    ("FewNERD", 16, "fewnerd_n16_s42", 42),
]

def extract_entities(d):
    return frozenset((e["text"], e["type"], e["start"], e["end"]) for e in d.get("entities", []))

def micro_f1(results):
    tp = sum(r[0] for r in results)
    np_ = sum(r[1] for r in results)
    ng = sum(r[2] for r in results)
    p = tp / np_ if np_ > 0 else 0
    r = tp / ng if ng > 0 else 0
    return 2*p*r/(p+r) if (p+r) > 0 else 0

def analyze(filepath, N):
    with open(filepath) as f:
        instances = [json.loads(line) for line in f]
    lp_res, gr_res = [], []
    n_inst = 0
    for inst in instances:
        gold = extract_entities(inst["gold"])
        if not gold:
            continue
        n_inst += 1
        samples = inst["samples"][:N]
        mlps = [s["mean_logprob"] for s in samples]
        best = max(range(len(samples)), key=lambda i: mlps[i])
        pred_lp = extract_entities(samples[best])
        pred_gr = extract_entities(samples[0])
        lp_res.append((len(pred_lp & gold), len(pred_lp), len(gold)))
        gr_res.append((len(pred_gr & gold), len(pred_gr), len(gold)))
    return micro_f1(lp_res), micro_f1(gr_res), n_inst

header = f"{'Dataset':<10} {'N':>4} {'LP-best F1':>11} {'Greedy F1':>10} {'LP d(pp)':>9} {'#inst':>7} {'seed':>5}"
print(header)
print("-" * 60)
lines = []
for ds, N, dn, seed in CONFIGS:
    fp = os.path.join(DATA_ROOT, dn, "samples.jsonl")
    if not os.path.exists(fp):
        print(f"{ds:<10} {N:>4} MISSING"); continue
    print(f"  computing {ds} N={N}...", file=sys.stderr, flush=True)
    lp, gr, ni = analyze(fp, N)
    line = f"{ds:<10} {N:>4} {lp*100:>10.2f}% {gr*100:>9.2f}% {(lp-gr)*100:>+8.2f} {ni:>7} {seed:>5}"
    print(line); lines.append(line)

out = os.path.join(DATA_ROOT, "lp_best_n_scaling_results.txt")
with open(out, "w") as f:
    f.write(header+"\n"+"-"*60+"\n")
    for l in lines: f.write(l+"\n")
    f.write("\nNotes:\n- CoNLL N=8: seed123, CoNLL N=16: seed456 (seed42 N/A)\n- Micro-avg F1, gold-nonempty instances, 4-tuple entity match\n")
print(f"\nSaved: {out}")
