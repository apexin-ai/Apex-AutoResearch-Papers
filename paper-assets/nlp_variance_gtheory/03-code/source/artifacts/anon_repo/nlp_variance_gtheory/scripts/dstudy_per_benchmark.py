import json, math, os

def vc(d, key):
    v = d.get(key, {})
    return max(0.0, v["estimate"] if isinstance(v, dict) else v)

def dstudy(s2_item, s2_mi, s2_ti, s2_pi, s2_si, s2_oi, s2_res, design, n_actual):
    nM, nT, nP, nS, nO = design
    sigma2_delta = (s2_mi/nM + s2_ti/nT + s2_pi/nP + s2_si/nS +
                    (s2_oi/nO if nO > 0 else 0) + s2_res/(nM*nT*nP*nS*nO))
    sigma2_Delta = sigma2_delta * n_actual
    conditions = nM * nT * nP * nS * nO

    ns = [25, 50, 75, 100, 116, 150, 200, 300, 500, 1000]
    curve = {str(n): round(s2_item / (s2_item + sigma2_Delta / n), 6) for n in ns}

    gvals = [s2_item / (s2_item + sigma2_Delta / n) for n in ns]
    mono = all(gvals[i] <= gvals[i+1] for i in range(len(gvals)-1))

    n_G80_exact = 4.0 * sigma2_Delta / s2_item
    n_G80 = math.ceil(n_G80_exact)
    G_200 = round(s2_item / (s2_item + sigma2_Delta / 200), 6)

    return {
        "conditions": conditions,
        "sigma2_delta_per_item": round(sigma2_delta, 10),
        "sigma2_delta": round(sigma2_Delta, 8),
        "n_G80": n_G80,
        "G_200": G_200,
        "d_study_curve": curve,
        "monotonic": mono
    }

MULTI  = (8, 2, 6, 6, 4)
PART4  = (1, 1, 2, 2, 1)
SINGLE = (1, 1, 1, 1, 1)

base = "./results/exp004_8model_analysis"

def load_benchmark(name):
    if name == "arc":
        with open(f"{base}/per_benchmark_gstudy_arc.json") as f:
            d = json.load(f)
        return d["variance_components"], d["n_levels"], d["n_models"]
    elif name == "hellaswag":
        with open(f"{base}/per_benchmark_gstudy_hellaswag_2temp.json") as f:
            d = json.load(f)
        return d["variance_components"], d["n_levels"], d["n_models"]
    elif name == "gsm8k":
        with open(f"{base}/per_benchmark_gstudy_ff.json") as f:
            d = json.load(f)
        bm = d["benchmarks"]["gsm8k"]
        return bm["variance_components"], bm["n_levels"], bm["n_models"]
    elif name == "math":
        with open(f"{base}/math_8model_verified.json") as f:
            d = json.load(f)
        return d["variance_components"], d["n_levels"], d["n_models"]

all_results = {}

for bm_name in ["arc", "hellaswag", "gsm8k", "math"]:
    vcs, nlevels, nmodels = load_benchmark(bm_name)
    n_actual = nlevels["item_id"]

    s2_item = vc(vcs, "item_id")
    s2_mi   = vc(vcs, "model:item_id")
    s2_ti   = vc(vcs, "temperature:item_id")
    s2_pi   = vc(vcs, "prompt_template:item_id")
    s2_si   = vc(vcs, "seed:item_id")
    s2_oi   = vc(vcs, "ordering:item_id")
    s2_res  = vc(vcs, "residual")

    result = {
        "benchmark": bm_name,
        "n_models": nmodels,
        "n_items_actual": n_actual,
        "variance_components": {
            "item": round(s2_item, 10),
            "model_item": round(s2_mi, 10),
            "temperature_item": round(s2_ti, 10),
            "prompt_item": round(s2_pi, 10),
            "seed_item": round(s2_si, 10),
            "ordering_item": round(s2_oi, 10),
            "residual": round(s2_res, 10)
        },
        "multi_facet": dstudy(s2_item, s2_mi, s2_ti, s2_pi, s2_si, s2_oi, s2_res, MULTI, n_actual),
        "partial_4": dstudy(s2_item, s2_mi, s2_ti, s2_pi, s2_si, s2_oi, s2_res, PART4, n_actual),
        "single_condition": dstudy(s2_item, s2_mi, s2_ti, s2_pi, s2_si, s2_oi, s2_res, SINGLE, n_actual),
    }
    result["ratio_single_vs_multi"] = round(
        result["single_condition"]["n_G80"] / result["multi_facet"]["n_G80"], 1
    )

    outpath = f"{base}/dstudy_{bm_name}.json"
    with open(outpath, "w") as f:
        json.dump(result, f, indent=2)
    print(f"Saved: {outpath}")
    all_results[bm_name] = result

# Summary
print("\n=== D-STUDY SUMMARY ===")
header = f"{'Benchmark':<12} {'Multi':>6} {'Part4':>6} {'Single':>7} {'Ratio':>6} {'MG200':>8} {'PG200':>8} {'SG200':>8}"
print(header)
for bm in ["arc", "hellaswag", "gsm8k", "math"]:
    r = all_results[bm]
    m = r["multi_facet"]
    p = r["partial_4"]
    s = r["single_condition"]
    ratio = r["ratio_single_vs_multi"]
    print(f"{bm:<12} {m['n_G80']:>6} {p['n_G80']:>6} {s['n_G80']:>7} {ratio:>5.1f}x {m['G_200']:>8.4f} {p['G_200']:>8.4f} {s['G_200']:>8.4f}")

print("\n=== VERIFICATION vs THREE_IN_ONE ===")
tio = {"arc": 98, "hellaswag": 171, "gsm8k": 128, "math": 101}
for bm in ["arc", "hellaswag", "gsm8k", "math"]:
    my = all_results[bm]["multi_facet"]["n_G80"]
    t = tio[bm]
    status = "MATCH" if my == t else f"MISMATCH (diff={my-t})"
    print(f"  {bm:<12} mine={my:>4}  three_in_one={t:>4}  {status}")

print("\n=== MONOTONICITY CHECK ===")
for bm in ["arc", "hellaswag", "gsm8k", "math"]:
    r = all_results[bm]
    for d in ["multi_facet", "partial_4", "single_condition"]:
        print(f"  {bm:<12} {d:<18} monotonic={r[d]['monotonic']}")

# Verify multi-facet curves against original JSON curves
print("\n=== VERIFY MULTI-FACET vs ORIGINAL JSON ===")
arc_ref = {"25": 0.507319, "50": 0.67314, "100": 0.804643, "200": 0.891748, "1000": 0.976297}
hs_ref  = {"25": 0.459025, "50": 0.629221, "100": 0.77242, "200": 0.871599, "1000": 0.97138}
gsm_ref = {"25": 0.440223, "50": 0.611326, "100": 0.758786, "200": 0.862852, "1000": 0.96919}

for bm, ref in [("arc", arc_ref), ("hellaswag", hs_ref), ("gsm8k", gsm_ref)]:
    my_curve = all_results[bm]["multi_facet"]["d_study_curve"]
    max_diff = 0
    for n, jg in ref.items():
        if n in my_curve:
            diff = abs(my_curve[n] - jg)
            max_diff = max(max_diff, diff)
    ok = "OK" if max_diff < 0.0001 else "DRIFT"
    print(f"  {bm:<12} max_diff={max_diff:.7f} {ok}")
