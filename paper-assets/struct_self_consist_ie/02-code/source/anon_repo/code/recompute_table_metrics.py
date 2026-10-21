#!/usr/bin/env python3
import json, numpy as np
from scipy import stats as scipy_stats

def load_data(path):
    with open(path) as f:
        return [json.loads(line) for line in f if line.strip()]

def entity_set(output):
    ents = output.get("entities", [])
    return set((e["text"], e["type"]) for e in ents)

def compute_f1(pred_set, gold_set):
    if not pred_set and not gold_set:
        return 1.0
    if not pred_set or not gold_set:
        return 0.0
    tp = len(pred_set & gold_set)
    p = tp / len(pred_set)
    r = tp / len(gold_set)
    if p + r == 0:
        return 0.0
    return 2 * p * r / (p + r)

def analyze_dataset(data, label):
    total = len(data)
    filtered = [d for d in data if len(d["gold"].get("entities", [])) > 0]
    N = len(filtered)
    n_samples = len(filtered[0]["samples"]) if filtered else 0
    print(f"\n{'='*60}")
    print(f"{label}: total={total}, gold-filtered n={N}, N_samples={n_samples}")
    print(f"{'='*60}")
    greedy_f1s, oracle_f1s, mean_lps, max_lps, lp_sel_f1s = [], [], [], [], []
    degen_count = 0
    for d in filtered:
        gold_set = entity_set(d["gold"])
        greedy_set = entity_set(d["greedy"])
        gf1 = compute_f1(greedy_set, gold_set)
        greedy_f1s.append(gf1)
        logprobs = d.get("logprobs", [])
        if not logprobs:
            logprobs = [s.get("mean_logprob", s.get("cumulative_logprob", -999)/max(s.get("n_tokens",1),1)) for s in d["samples"]]
        sample_f1s = [compute_f1(entity_set(s), gold_set) for s in d["samples"]]
        oracle_f1s.append(max(sample_f1s))
        mean_lps.append(float(np.mean(logprobs)))
        max_lps.append(float(np.max(logprobs)))
        lp_sel_f1s.append(sample_f1s[int(np.argmax(logprobs))])
        if len(set(sample_f1s)) == 1:
            degen_count += 1
    greedy_f1s = np.array(greedy_f1s)
    oracle_f1s = np.array(oracle_f1s)
    lp_sel_f1s = np.array(lp_sel_f1s)
    mean_lps = np.array(mean_lps)
    max_lps = np.array(max_lps)
    gm = float(greedy_f1s.mean())
    om = float(oracle_f1s.mean())
    hd = (om - gm) * 100
    dp = degen_count / N * 100
    lsm = float(lp_sel_f1s.mean())
    ld = (lsm - gm) * 100
    rm, pm = scipy_stats.spearmanr(mean_lps, greedy_f1s)
    rx, px = scipy_stats.spearmanr(max_lps, greedy_f1s)
    print(f"  greedy_F1  = {gm:.6f}")
    print(f"  oracle_F1  = {om:.6f}")
    print(f"  headroom   = {hd:.2f}pp")
    print(f"  degen%     = {dp:.1f}% ({degen_count}/{N})")
    print(f"  mean_LP rho= {float(rm):.6f} (p={float(pm):.2e})")
    print(f"  max_LP rho = {float(rx):.6f} (p={float(px):.2e})")
    print(f"  LP_sel_F1  = {lsm:.6f}")
    print(f"  LP_delta   = {ld:+.2f}pp")
    return {"n":N,"greedy":round(gm,6),"oracle":round(om,6),"headroom":round(hd,2),"degen":round(dp,1),"mean_lp_rho":round(float(rm),6),"max_lp_rho":round(float(rx),6),"lp_sel":round(lsm,6),"lp_delta":round(ld,2)}

base = "/root/autodl-tmp/struct_self_consist_ie/output"
fewnerd = load_data(f"{base}/exp_021_inference/samples.jsonl")
fr = analyze_dataset(fewnerd, "Few-NERD")
conll = load_data(f"{base}/exp002_conll2003/samples.jsonl")
cr = analyze_dataset(conll, "CoNLL")
print("\n" + "="*60)
print("SUMMARY")
print("="*60)
print(json.dumps({"fewnerd": fr, "conll": cr}, indent=2))
