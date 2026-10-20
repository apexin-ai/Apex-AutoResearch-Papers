import os, json, csv, re

base_dir = "/root/autodl-tmp/exp001/eval_results/"
BENCHMARKS = ["mmlu", "gsm8k", "arc_challenge", "humaneval"]

METRIC_KEYS = {
    "mmlu": "accuracy",
    "gsm8k": "accuracy",
    "arc_challenge": "accuracy",
    "humaneval": "pass@1",
}

def parse_config(name):
    info = {"model_scale": "", "dosage": "", "seed": "none", "version": "1",
            "aligned": False, "paraphrased": False}
    if "0.5B-Instruct" in name:
        info["model_scale"] = "0.5B-Instruct"
    elif "0.5B" in name:
        info["model_scale"] = "0.5B"
    elif "1.5B" in name:
        info["model_scale"] = "1.5B"
    elif "3B" in name:
        info["model_scale"] = "3B"

    m = re.search(r'_(d\d+)', name)
    if m:
        info["dosage"] = m.group(1)
    elif "base" in name.lower() or "raw" in name.lower() or "Instruct" in name:
        info["dosage"] = "base"

    m = re.search(r'_s(\d+)', name)
    if m:
        info["seed"] = m.group(1)

    m = re.search(r'_v(\d+)', name)
    if m:
        info["version"] = m.group(1)

    info["aligned"] = "aligned" in name.lower()
    info["paraphrased"] = "para" in name.lower()
    return info

def is_deprecated(name):
    if "DEPRECATED" in name:
        return True
    if "base_pretrained" in name:
        return True
    # D018: 3B d000 s42 v3 LoRA damage
    if "3B_d000_s42_v3" in name or "3B_d000_v3_s42" in name:
        return True
    return False

rows = []
empty_dirs = []

for d in sorted(os.listdir(base_dir)):
    full = os.path.join(base_dir, d)
    if not os.path.isdir(full):
        continue
    result_file = os.path.join(full, "eval_results.json")
    if not os.path.exists(result_file):
        empty_dirs.append(d)
        continue

    with open(result_file) as f:
        data = json.load(f)

    benchmarks = data.get("benchmarks", data)
    info = parse_config(d)
    row = {
        "config": d,
        "model_scale": info["model_scale"],
        "dosage": info["dosage"],
        "seed": info["seed"],
        "version": info["version"],
        "aligned": info["aligned"],
        "paraphrased": info["paraphrased"],
        "deprecated": is_deprecated(d),
    }

    for bench in BENCHMARKS:
        val = None
        if bench in benchmarks:
            bdata = benchmarks[bench]
            if isinstance(bdata, dict):
                metric_key = METRIC_KEYS.get(bench, "accuracy")
                val = bdata.get(metric_key)
                if val is None:
                    for fallback in ["accuracy", "pass@1", "score"]:
                        if fallback in bdata:
                            val = bdata[fallback]
                            break
            else:
                val = bdata
        row[bench] = val

    has_item = any(
        isinstance(benchmarks.get(b), dict) and "per_item" in benchmarks.get(b, {})
        for b in BENCHMARKS if b in benchmarks
    )
    has_cm = any(
        isinstance(benchmarks.get(b), dict) and "per_item" in benchmarks.get(b, {})
        for b in BENCHMARKS if b in benchmarks
    )
    row["has_item_responses"] = has_item
    row["has_correctness_matrix"] = has_cm

    avail = [b for b in BENCHMARKS if row.get(b) is not None]
    row["benchmarks_available"] = ",".join(avail)
    row["num_benchmarks"] = len(avail)
    rows.append(row)

fieldnames = ["config", "model_scale", "dosage", "seed", "version",
              "aligned", "paraphrased", "deprecated",
              "mmlu", "gsm8k", "arc_challenge", "humaneval",
              "has_item_responses", "has_correctness_matrix",
              "benchmarks_available", "num_benchmarks"]

outpath = "/root/autodl-tmp/exp001/eval_summary_matrix.csv"
with open(outpath, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print(f"Written {len(rows)} rows to {outpath}")
print(f"\nEmpty dirs (no eval_results.json): {len(empty_dirs)}")
for ed in empty_dirs:
    print(f"  {ed}")

print(f"\nDeprecated configs:")
for r in rows:
    if r["deprecated"]:
        reason = []
        if "DEPRECATED" in r["config"]:
            reason.append("marked DEPRECATED in dirname")
        if "base_pretrained" in r["config"]:
            reason.append("base_pretrained reference")
        if "3B_d000_s42_v3" in r["config"] or "3B_d000_v3_s42" in r["config"]:
            reason.append("D018 LoRA hyperparameter damage")
        print(f"  {r['config']}: {'; '.join(reason)}")

print(f"\nBenchmark coverage (non-deprecated only):")
nd_rows = [r for r in rows if not r["deprecated"]]
for bench in BENCHMARKS:
    aligned_count = sum(1 for r in nd_rows if r["aligned"] and r[bench] is not None)
    irt_count = sum(1 for r in nd_rows if r[bench] is not None)
    print(f"  {bench}: N_aligned={aligned_count}, N_irt={irt_count}")
