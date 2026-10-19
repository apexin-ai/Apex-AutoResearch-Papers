import json

BASE = "/root/fml-bench/benchmark_results/aide/Fairness_and_Bias_aif360"
SEQS = {}
for ts in ("20260918_105845", "20260918_153616"):
    d = json.load(open(f"{BASE}/{ts}/summary.json"))
    vs = d.get("val_steps") or []
    seq = []
    for v in vs:
        try:
            seq.append(round(float(v["val_result"]["results"]["compas"]["means"]["abs_aod_mean"]), 6))
        except Exception:
            seq.append(None)
    SEQS[ts] = seq
    print(ts, "n =", len(seq))

a, b = SEQS["20260918_105845"], SEQS["20260918_153616"]
print("两条 val 序列完全一致:", a == b)
print("A 前 10:", a[:10])
print("B 前 10:", b[:10])
diff = [(i, x, y) for i, (x, y) in enumerate(zip(a, b)) if x != y]
print("首个不同位置:", diff[0] if diff else "无")
