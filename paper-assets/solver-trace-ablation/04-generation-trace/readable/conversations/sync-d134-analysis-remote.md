# sync d134 analysis remote

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 0
- **Tool calls:** 5
- **Original source:** `logs/chats/worker_sync_d134-analysis-remote_20260518T140325.jsonl`
- **Structured JSON:** [`1d7d192eb44fef97c3a6.json`](../../sessions/1d/1d7d192eb44fef97c3a6.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

11 recorded events

### Tool call

_source line 1 · 2026-05-18T14:05:30.335043+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/scripts/d134_analysis.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_sync_d134-analysis-remote_20260518T140325",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/scripts/d134_analysis.py"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-18T14:05:30.335583+00:00_

1	#!/usr/bin/env python3
2	"""D134 experiment analysis: multi-seed ISR vs Random, 4B GRPO training.
3	Reads taxonomy data from classify.json, taxonomy.json, or top-level taxonomy files.
4	Computes summary stats and statistical tests.
5	"""
6	
7	import argparse
8	import json
9	import re
10	import sys
11	from pathlib import Path
12	
13	import numpy as np
14	import pandas as pd
15	from scipy import stats
16	
17	CONDITION_MAP = [
18	    ("d134_4b_isr", "ISR"),
19	    ("d134_4b_random", "RANDOM"),
20	    ("plan002_additive", "ISR"),
21	    ("plan018_additive_random", "RANDOM"),
22	    ("plan018_random", "RANDOM"),
23	]
24	
25	
26	MODE_PREFIXES = {
27	    "d134_only": ["d134_4b"],
28	    "all": ["d134_4b", "plan002_additive_b01", "plan018_additive_random_b01", "plan018_random"],
29	}
30	
31	
32	def parse_args():
33	    p = argparse.ArgumentParser(description="D134 multi-seed analysis and statistical tests")
34	    p.add_argument("--data_dir", type=str, default="/root/autodl-tmp/outputs",
35	                   help="Directory containing experiment outputs")
36	    p.add_argument("--mode", type=str, default="d134_only", choices=list(MODE_PREFIXES),
37	                   help="d134_only = matched 5+5 design (default); all = include original seeds")
38	    p.add_argument("--prefix", type=str, default=None,
39	                   help="(Legacy) Single prefix filter; overrides mode/prefixes")
40	    p.add_argument("--prefixes", type=str, default=None,
41	                   help="Comma-separated prefixes; overrides --mode")
42	    p.add_argument("--output", type=str, default=None,
43	                   help="Write markdown summary to this file")
44	    p.add_argument("--n_perm", type=int, default=10000,
45	                   help="Number of permutations for permutation test")
46	    p.add_argument("--seed", type=int, default=42,
47	                   help="Random seed for permutation test")
48	    return p.parse_args()
49	
50	
51	def match_condition(name: str) -> str | None:
52	 
…[truncated 15612 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_sync_d134-analysis-remote_20260518T140325",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-18T14:05:30.335825+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_execute",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_sync_d134-analysis-remote_20260518T140325",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_execute",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-18T14:05:30.335975+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_sync_d134-analysis-remote_20260518T140325",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-18T14:05:30.336206+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-39279",
  "command": "cat > /root/solver-trace-ablation/scripts/d134_analysis.py << 'HEREDOC_EOF'\n#!/usr/bin/env python3\n\"\"\"D134 experiment analysis: multi-seed ISR vs Random, 4B GRPO training.\nReads taxonomy data from classify.json, taxonomy.json, or top-level taxonomy files.\nComputes summary stats and statistical tests.\n\"\"\"\n\nimport argparse\nimport json\nimport re\nimport sys\nfrom pathlib import Path\n\nimport numpy as np\nimport pandas as pd\nfrom scipy import stats\n\nCONDITION_MAP = [\n    (\"d134_4b_isr\", \"ISR\"),\n    (\"d134_4b_random\", \"RANDOM\"),\n    (\"plan002_additive\", \"ISR\"),\n    (\"plan018_additive_random\", \"RANDOM\"),\n    (\"plan018_random\", \"RANDOM\"),\n]\n\n\nMODE_PREFIXES = {\n    \"d134_only\": [\"d134_4b\"],\n    \"all\": [\"d134_4b\", \"plan002_additive_b01\", \"plan018_additive_random_b01\", \"plan018_random\"],\n}\n\n\ndef parse_args():\n    p = argparse.ArgumentParser(description=\"D134 multi-seed analysis and statistical tests\")\n    p.add_argument(\"--data_dir\", type=str, default=\"/root/autodl-tmp/outputs\",\n                   help=\"Directory containing experiment outputs\")\n    p.add_argument(\"--mode\", type=str, default=\"d134_only\", choices=list(MODE_PREFIXES),\n                   help=\"d134_only = matched 5+5 design (default); all = include original seeds\")\n    p.add_argument(\"--prefix\", type=str, default=None,\n                   help=\"(Legacy) Single prefix filter; overrides mode/prefixes\")\n    p.add_argument(\"--prefixes\", type=str, default=None,\n                   help=\"Comma-separated prefixes; overrides --mode\")\n    p.add_argument(\"--output\", type=str, default=None,\n                   help=\"Write markdown summary to this file\")\n    p.add_argument(\"--n_perm\", type=int, default=10000,\n                   help=\"Number of permutations for permutation test\")\n    p.add_argument(\"--seed\", type=int, default=42,\n                   help=\"Random seed for permutation test\")\n    return p.parse_args()\n\n\ndef match_condition(name: str) -> str | None:\n    best_prefix = \"\"\n    best_cond = None\n    for prefix, cond in CONDITION_MAP:\n        if name.startswith(prefix) and len(prefix) > len(best_prefix):\n            best_prefix = prefix\n            best_cond = cond\n    return best_cond\n\n\ndef extract_seed(name: str) -> int | None:\n    m = re.search(r'_s(\\d+)', name)\n    return int(m.group(1)) if m else None\n\n\ndef load_eval_results(path: Path) -> dict | None:\n    if not path.exists():\n        return None\n    with open(path) as f:\n        data = json.load(f)\n    if \"eval_results\" in data:\n        return data[\"eval_results\"]\n    return data\n\n\ndef load_taxonomy_unified(path: Path) -> dict | None:\n    with open(path) as f:\n        raw = json.load(f)\n    t = raw.get(\"taxonomy\", {})\n    proved = t.get(\"proved\", 0)\n    if proved == 0:\n        return None\n    h7 = t.get(\"H7\", 0)\n    h1 = t.get(\"H1_exact\", 0)\n    h8 = t.get(\"H8\", 0)\n    genuine = t.get(\"genuine\", 0)\n    return {\n        \"n_total\": 100,\n        \"n_proved\": proved,\n        \"h7_total_count\": h7,\n        \"h7_total_rate\": h7 / proved,\n        \"h1_strict_count\": h1,\n        \"h8_conjunction_collapse_count\": h8,\n        \"genuine_count\": genuine,\n        \"genuine_rate\": genuine / proved,\n        \"content_independent_count\": 0,\n    }\n\n\ndef load_taxonomy_verification(path: Path) -> dict | None:\n    with open(path) as f:\n        raw = json.load(f)\n    proved = raw.get(\"proved\", 0)\n    if proved == 0:\n        return None\n    tax = raw.get(\"taxonomy\", {})\n    h7 = tax.get(\"h7\", {}).get(\"count\", 0)\n    h1 = tax.get(\"h1_exact\", {}).get(\"count\", 0)\n    h8 = tax.get(\"h8\", {}).get(\"count\", 0)\n    genuine = tax.get(\"genuine\", {}).get(\"count\", 0)\n    return {\n        \"n_total\": raw.get(\"total\", 100),\n        \"n_proved\": proved,\n        \"h7_total_count\": h7,\n        \"h7_total_rate\": h7 / proved,\n        \"h1_strict_count\": h1,\n        \"h8_conjunction_collapse_count\": h8,\n        \"genuine_count\": genuine,\n        \"genuine_rate\": genuine / proved,\n        \"content_independent_count\": 0,\n    }\n\n\ndef discover_runs(data_dir: Path, prefixes: list[str]) -> list[dict]:\n    runs = []\n    seen = set()\n\n    for entry in sorted(data_dir.iterdir()):\n        name = entry.name\n        if not any(name.startswith(p) for p in prefixes):\n            continue\n\n        cond = match_condition(name)\n        seed_val = extract_seed(name)\n        if cond is None or seed_val is None:\n            continue\n        key = (cond, seed_val)\n        if key in seen:\n            continue\n\n        data = None\n        if entry.is_dir():\n            for fname in [\"classify.json\", \"taxonomy.json\"]:\n                data = load_eval_results(entry / fname)\n                if data is not None:\n                    break\n            if data is None:\n                continue\n        elif entry.is_file():\n            if name.endswith(\"_taxonomy_unified.json\"):\n                data = load_taxonomy_unified(entry)\n            elif name.endswith(\"_taxonomy_verification.json\"):\n                data = load_taxonomy_verification(entry)\n            if data is None:\n                continue\n        else:\n            continue\n\n        seen.add(key)\n        runs.append({\n            \"dir_name\": name,\n            \"seed\": seed_val,\n            \"condition\": cond,\n            \"data\": data,\n        })\n\n    return runs\n\n\ndef compute_row(run: dict) -> dict:\n    d = run[\"data\"]\n    n_proved = d.get(\"n_proved\", 0)\n    n_total = d.get(\"n_total\", 100)\n    h7 = d.get(\"h7_total_count\", 0)\n    h7_rate = d.get(\"h7_total_rate\", h7 / n_proved if n_proved > 0 else 0.0)\n    h1 = d.get(\"h1_strict_count\", 0)\n    h8 = d.get(\"h8_conjunction_collapse_count\", 0)\n    genuine = d.get(\"genuine_count\", 0)\n    genuine_rate = d.get(\"genuine_rate\", genuine / n_proved if n_proved > 0 else 0.0)\n    ci = d.get(\"content_independent_count\", 0)\n    snh = max(genuine - ci, 0)\n    snh_rate = snh / n_proved if n_proved > 0 else 0.0\n\n    return {\n        \"seed\": run[\"seed\"],\n        \"condition\": run[\"condition\"],\n        \"n_total\": n_total,\n        \"PR\": n_proved,\n        \"H7_count\": h7,\n        \"H7_rate\": h7_rate,\n        \"H1_count\": h1,\n        \"H8_count\": h8,\n        \"genuine_count\": genuine,\n        \"genuine_rate\": genuine_rate,\n        \"CI_count\": ci,\n        \"SNH_count\": snh,\n        \"SNH_rate\": snh_rate,\n    }\n\n\ndef build_table(runs: list[dict]) -> pd.DataFrame:\n    rows = [compute_row(r) for r in runs]\n    df = pd.DataFrame(rows)\n    df = df.sort_values([\"condition\", \"seed\"]).reset_index(drop=True)\n    return df\n\n\ndef fisher_h7_domination(df: pd.DataFrame) -> dict:\n    results = {}\n    for cond in [\"ISR\", \"RANDOM\"]:\n        sub = df[df[\"condition\"] == cond]\n        results[cond] = {\n            \"n\": len(sub),\n            \"h7_dom\": int((sub[\"H7_rate\"] >= 0.5).sum()),\n            \"not_h7_dom\": int((sub[\"H7_rate\"] < 0.5).sum()),\n        }\n\n    table = np.array([\n        [results[\"ISR\"][\"h7_dom\"], results[\"ISR\"][\"not_h7_dom\"]],\n        [results[\"RANDOM\"][\"h7_dom\"], results[\"RANDOM\"][\"not_h7_dom\"]],\n    ])\n    odds_ratio, p_value = stats.fisher_exact(table, alternative=\"greater\")\n    return {\n        \"table\": table.tolist(),\n        \"ISR\": results[\"ISR\"],\n        \"RANDOM\": results[\"RANDOM\"],\n        \"odds_ratio\": odds_ratio,\n        \"p_value\": p_value,\n    }\n\n\ndef permutation_test_genuine(df: pd.DataFrame, n_perm: int = 10000,\n                              rng_seed: int = 42) -> dict:\n    isr = df[df[\"condition\"] == \"ISR\"][\"genuine_rate\"].values\n    rand = df[df[\"condition\"] == \"RANDOM\"][\"genuine_rate\"].values\n    observed = isr.mean() - rand.mean()\n\n    pooled = np.concatenate([isr, rand])\n    n_isr = len(isr)\n    rng = np.random.default_rng(rng_seed)\n\n    count = 0\n    for _ in range(n_perm):\n        perm = rng.permutation(pooled)\n        diff = perm[:n_isr].mean() - perm[n_isr:].mean()\n        if diff >= observed:\n            count += 1\n\n    return {\n        \"observed_diff\": float(observed),\n        \"p_value\": count / n_perm,\n        \"n_perm\": n_perm,\n        \"isr_mean\": float(isr.mean()),\n        \"random_mean\": float(rand.mean()),\n    }\n\n\ndef mannwhitney_h7(df: pd.DataFrame) -> dict:\n    isr = df[df[\"condition\"] == \"ISR\"][\"H7_rate\"].values\n    rand = df[df[\"condition\"] == \"RANDOM\"][\"H7_rate\"].values\n    u_stat, p_value = stats.mannwhitneyu(isr, rand, alternative=\"greater\")\n    return {\n        \"U\": float(u_stat),\n        \"p_value\": float(p_value),\n        \"isr_median\": float(np.median(isr)),\n        \"random_median\": float(np.median(rand)),\n    }\n\n\ndef condition_stats(df: pd.DataFrame) -> pd.DataFrame:\n    metrics = [\"PR\", \"H7_rate\", \"genuine_rate\", \"SNH_rate\"]\n    rows = []\n    for cond in [\"ISR\", \"RANDOM\"]:\n        sub = df[df[\"condition\"] == cond]\n        row = {\"condition\": cond, \"n_seeds\": len(sub)}\n        for m in metrics:\n            vals = sub[m].values\n            row[f\"{m}_mean\"] = vals.mean()\n            row[f\"{m}_std\"] = vals.std(ddof=1) if len(vals) > 1 else 0.0\n        rows.append(row)\n    return pd.DataFrame(rows)\n\n\ndef format_pct(val: float) -> str:\n    return f\"{val*100:.1f}%\"\n\n\ndef format_mean_std(mean: float, std: float, pct: bool = False) -> str:\n    if pct:\n        return f\"{mean*100:.1f} +/- {std*100:.1f}%\"\n    return f\"{mean:.1f} +/- {std:.1f}\"\n\n\ndef print_per_seed_table(df: pd.DataFrame):\n    print(\"\\n\" + \"=\" * 90)\n    print(\"  PER-SEED RESULTS\")\n    print(\"=\" * 90)\n    cols = [\"condition\", \"seed\", \"PR\", \"H7_count\", \"H7_rate\", \"H1_count\",\n            \"H8_count\", \"genuine_count\", \"genuine_rate\", \"CI_count\", \"SNH_count\", \"SNH_rate\"]\n    fmt = df[cols].copy()\n    fmt[\"H7_rate\"] = fmt[\"H7_rate\"].apply(format_pct)\n    fmt[\"genuine_rate\"] = fmt[\"genuine_rate\"].apply(format_pct)\n    fmt[\"SNH_rate\"] = fmt[\"SNH_rate\"].apply(format_pct)\n    print(fmt.to_string(index=False))\n\n\ndef print_condition_stats(cond_df: pd.DataFrame):\n    print(\"\\n\" + \"=\" * 90)\n    print(\"  CONDITION-LEVEL STATISTICS\")\n    print(\"=\" * 90)\n    for _, row in cond_df.iterrows():\n        print(f\"\\n  {row['condition']} (n={int(row['n_seeds'])} seeds):\")\n        print(f\"    PR:           {format_mean_std(row['PR_mean'], row['PR_std'])}\")\n        print(f\"    H7 rate:      {format_mean_std(row['H7_rate_mean'], row['H7_rate_std'], pct=True)}\")\n        print(f\"    Genuine rate: {format_mean_std(row['genuine_rate_mean'], row['genuine_rate_std'], pct=True)}\")\n        print(f\"    S-NH rate:    {format_mean_std(row['SNH_rate_mean'], row['SNH_rate_std'], pct=True)}\")\n\n\ndef print_tests(fisher, perm, mw):\n    print(\"\\n\" + \"=\" * 90)\n    print(\"  STATISTICAL TESTS\")\n    print(\"=\" * 90)\n\n    print(\"\\n  1. H7 Domination Fisher Exact Test (H7-dominated = H7% >= 50%)\")\n    print(f\"     ISR:    {fisher['ISR']['h7_dom']} dominated / {fisher['ISR']['n']} seeds\")\n    print(f\"     RANDOM: {fisher['RANDOM']['h7_dom']} dominated / {fisher['RANDOM']['n']} seeds\")\n    print(f\"     Contingency: {fisher['table']}\")\n    print(f\"     Odds ratio: {fisher['odds_ratio']:.4f}\")\n    print(f\"     p-value (one-sided, greater): {fisher['p_value']:.4f}\")\n\n    print(f\"\\n  2. Genuine Rate Permutation Test (n_perm={perm['n_perm']})\")\n    print(f\"     ISR mean genuine rate:    {perm['isr_mean']*100:.2f}%\")\n    print(f\"     RANDOM mean genuine rate: {perm['random_mean']*100:.2f}%\")\n    print(f\"     Observed diff: {perm['observed_diff']*100:.2f} pp\")\n    print(f\"     p-value: {perm['p_value']:.4f}\")\n\n    print(f\"\\n  3. H7 Rate Mann-Whitney U Test\")\n    print(f\"     ISR median H7 rate:    {mw['isr_median']*100:.1f}%\")\n    print(f\"     RANDOM median H7 rate: {mw['random_median']*100:.1f}%\")\n    print(f\"     U statistic: {mw['U']:.1f}\")\n    print(f\"     p-value (one-sided, greater): {mw['p_value']:.4f}\")\n\n\ndef generate_markdown(df: pd.DataFrame, cond_df: pd.DataFrame,\n                      fisher: dict, perm: dict, mw: dict) -> str:\n    lines = []\n    lines.append(\"## D134 4B GRPO: ISR vs Random (multi-seed)\\n\")\n\n    lines.append(\"### Per-Seed Results\\n\")\n    lines.append(\"| Condition | Seed | PR | H7 | H7% | H1 | H8 | Genuine | Gen% | CI | S-NH | S-NH% |\")\n    lines.append(\"|-----------|------|----|----|-----|----|----|---------|------|----|------|-------|\")\n    for _, r in df.iterrows():\n        lines.append(\n            f\"| {r['condition']} | {r['seed']} | {r['PR']} | {r['H7_count']} | \"\n            f\"{r['H7_rate']*100:.1f} | {r['H1_count']} | {r['H8_count']} | \"\n            f\"{r['genuine_count']} | {r['genuine_rate']*100:.1f} | {r['CI_count']} | \"\n            f\"{r['SNH_count']} | {r['SNH_rate']*100:.1f} |\"\n        )\n\n    lines.append(\"\\n### Condition Summary (mean +/- std)\\n\")\n    lines.append(\"| Condition | n | PR | H7% | Genuine% | S-NH% |\")\n    lines.append(\"|-----------|---|----|-----|----------|-------|\")\n    for _, r in cond_df.iterrows():\n        lines.append(\n            f\"| {r['condition']} | {int(r['n_seeds'])} | \"\n            f\"{r['PR_mean']:.1f}+/-{r['PR_std']:.1f} | \"\n            f\"{r['H7_rate_mean']*100:.1f}+/-{r['H7_rate_std']*100:.1f} | \"\n            f\"{r['genuine_rate_mean']*100:.1f}+/-{r['genuine_rate_std']*100:.1f} | \"\n            f\"{r['SNH_rate_mean']*100:.1f}+/-{r['SNH_rate_std']*100:.1f} |\"\n        )\n\n    if fisher and perm and mw:\n        lines.append(\"\\n### Statistical Tests\\n\")\n        lines.append(f\"**1. H7 Domination Fisher Exact Test** (H7-dominated = H7% >= 50%)\")\n        lines.append(f\"- ISR: {fisher['ISR']['h7_dom']}/{fisher['ISR']['n']} dominated | \"\n                     f\"RANDOM: {fisher['RANDOM']['h7_dom']}/{fisher['RANDOM']['n']} dominated\")\n        lines.append(f\"- OR = {fisher['odds_ratio']:.4f}, p = {fisher['p_value']:.4f}\\n\")\n\n        lines.append(f\"**2. Genuine Rate Permutation Test** (n={perm['n_perm']})\")\n        lines.append(f\"- ISR: {perm['isr_mean']*100:.2f}% vs RANDOM: {perm['random_mean']*100:.2f}%\")\n        lines.append(f\"- Diff = {perm['observed_diff']*100:.2f} pp, p = {perm['p_value']:.4f}\\n\")\n\n        lines.append(f\"**3. H7 Rate Mann-Whitney U**\")\n        lines.append(f\"- ISR median: {mw['isr_median']*100:.1f}% vs RANDOM median: {mw['random_median']*100:.1f}%\")\n        lines.append(f\"- U = {mw['U']:.1f}, p = {mw['p_value']:.4f}\")\n\n    return \"\\n\".join(lines) + \"\\n\"\n\n\ndef main():\n    args = parse_args()\n    data_dir = Path(args.data_dir)\n\n    if not data_dir.exists():\n        print(f\"ERROR: data directory {data_dir} does not exist\", file=sys.stderr)\n        sys.exit(1)\n\n    if args.prefix:\n        prefixes = [args.prefix]\n    elif args.prefixes:\n        prefixes = [p.strip() for p in args.prefixes.split(\",\")]\n    else:\n        prefixes = MODE_PREFIXES[args.mode]\n    print(f\"Mode: {args.mode} | Prefixes: {prefixes}\")\n\n    runs = discover_runs(data_dir, prefixes)\n    if not runs:\n        print(f\"ERROR: no runs found in {data_dir} with prefixes {prefixes}\", file=sys.stderr)\n        sys.exit(1)\n\n    isr_count = sum(1 for r in runs if r[\"condition\"] == \"ISR\")\n    rand_count = sum(1 for r in runs if r[\"condition\"] == \"RANDOM\")\n    print(f\"Found {len(runs)} runs: {isr_count} ISR, {rand_count} RANDOM\")\n    for r in runs:\n        print(f\"  {r['condition']:6s} s{r['seed']} <- {r['dir_name']}\")\n\n    df = build_table(runs)\n    print_per_seed_table(df)\n\n    cond_df = condition_stats(df)\n    print_condition_stats(cond_df)\n\n    if isr_count < 2 or rand_count < 2:\n        print(\"\\nWARNING: need >= 2 seeds per condition for statistical tests, skipping.\",\n              file=sys.stderr)\n        if args.output:\n            md = generate_markdown(df, cond_df, {}, {}, {})\n            Path(args.output).write_text(md)\n            print(f\"\\nMarkdown written to {args.output}\")\n        return\n\n    fisher = fisher_h7_domination(df)\n    perm = permutation_test_genuine(df, n_perm=args.n_perm, rng_seed=args.seed)\n    mw = mannwhitney_h7(df)\n\n    print_tests(fisher, perm, mw)\n\n    md = generate_markdown(df, cond_df, fisher, perm, mw)\n    print(\"\\n\" + \"=\" * 90)\n    print(\"  MARKDOWN OUTPUT\")\n    print(\"=\" * 90)\n    print(md)\n\n    if args.output:\n        Path(args.output).parent.mkdir(parents=True, exist_ok=True)\n        Path(args.output).write_text(md)\n        print(f\"Markdown written to {args.output}\")\n\n\nif __name__ == \"__main__\":\n    main()\nHEREDOC_EOF",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_sync_d134-analysis-remote_20260518T140325",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-39279",
    "command": "cat > /root/solver-trace-ablation/scripts/d134_analysis.py << 'HEREDOC_EOF'\n#!/usr/bin/env python3\n\"\"\"D134 experiment analysis: multi-seed ISR vs Random, 4B GRPO training.\nReads taxonomy data from classify.json, taxonomy.json, or top-level taxonomy files.\nComputes summary stats and statistical tests.\n\"\"\"\n\nimport argparse\nimport json\nimport re\nimport sys\nfrom pathlib import Path\n\nimport numpy as np\nimport pandas as pd\nfrom scipy import stats\n\nCONDITION_MAP = [\n    (\"d134_4b_isr\", \"ISR\"),\n    (\"d134_4b_random\", \"RANDOM\"),\n    (\"plan002_additive\", \"ISR\"),\n    (\"plan018_additive_random\", \"RANDOM\"),\n    (\"plan018_random\", \"RANDOM\"),\n]\n\n\nMODE_PREFIXES = {\n    \"d134_only\": [\"d134_4b\"],\n    \"all\": [\"d134_4b\", \"plan002_additive_b01\", \"plan018_additive_random_b01\", \"plan018_random\"],\n}\n\n\ndef parse_args():\n    p = argparse.ArgumentParser(description=\"D134 multi-seed analysis and statistical tests\")\n    p.add_argument(\"--data_dir\", type=str, default=\"/root/autodl-tmp/outputs\",\n                   help=\"Directory containing experiment outputs\")\n    p.add_argument(\"--mode\", type=str, default=\"d134_only\", choices=list(MODE_PREFIXES),\n                   help=\"d134_only = matched 5+5 design (default); all = include original seeds\")\n    p.add_argument(\"--prefix\", type=str, default=None,\n                   help=\"(Legacy) Single prefix filter; overrides mode/prefixes\")\n    p.add_argument(\"--prefixes\", type=str, default=None,\n                   help=\"Comma-separated prefixes; overrides --mode\")\n    p.add_argument(\"--output\", type=str, default=None,\n                   help=\"Write markdown summary to this file\")\n    p.add_argument(\"--n_perm\", type=int, default=10000,\n                   help=\"Number of permutations for permutation test\")\n    p.add_argument(\"--seed\", type=int, default=42,\n                   help=\"Random seed for permutation test\")\n    return p.parse_args()\n\n\ndef match_condition(name: str) -> str | None:\n    best_prefix = \"\"\n    best_cond = None\n    for prefix, cond in CONDITION_MAP:\n        if name.startswith(prefix) and len(prefix) > len(best_prefix):\n            best_prefix = prefix\n            best_cond = cond\n    return best_cond\n\n\ndef extract_seed(name: str) -> int | None:\n    m = re.search(r'_s(\\d+)', name)\n    return int(m.group(1)) if m else None\n\n\ndef load_eval_results(path: Path) -> dict | None:\n    if not path.exists():\n        return None\n    with open(path) as f:\n        data = json.load(f)\n    if \"eval_results\" in data:\n        return data[\"eval_results\"]\n    return data\n\n\ndef load_taxonomy_unified(path: Path) -> dict | None:\n    with open(path) as f:\n        raw = json.load(f)\n    t = raw.get(\"taxonomy\", {})\n    proved = t.get(\"proved\", 0)\n    if proved == 0:\n        return None\n    h7 = t.get(\"H7\", 0)\n    h1 = t.get(\"H1_exact\", 0)\n    h8 = t.get(\"H8\", 0)\n    genuine = t.get(\"genuine\", 0)\n    return {\n        \"n_total\": 100,\n        \"n_proved\": proved,\n        \"h7_total_count\": h7,\n        \"h7_total_rate\": h7 / proved,\n        \"h1_strict_count\": h1,\n        \"h8_conjunction_collapse_count\": h8,\n        \"genuine_count\": genuine,\n        \"genuine_rate\": genuine / proved,\n        \"content_independent_count\": 0,\n    }\n\n\ndef load_taxonomy_verification(path: Path) -> dict | None:\n    with open(path) as f:\n        raw = json.load(f)\n    proved = raw.get(\"proved\", 0)\n    if proved == 0:\n        return None\n    tax = raw.get(\"taxonomy\", {})\n    h7 = tax.get(\"h7\", {}).get(\"count\", 0)\n    h1 = tax.get(\"h1_exact\", {}).get(\"count\", 0)\n    h8 = tax.get(\"h8\", {}).get(\"count\", 0)\n    genuine = tax.get(\"genuine\", {}).get(\"count\", 0)\n    return {\n        \"n_total\": raw.get(\"total\", 100),\n        \"n_proved\": proved,\n        \"h7_total_count\": h7,\n        \"h7_total_rate\": h7 / proved,\n        \"h1_strict_count\": h1,\n        \"h8_conjunction_collapse_count\": h8,\n        \"genuine_count\": genuine,\n        \"genuine_rate\": genuine / proved,\n        \"content_independent_count\": 0,\n    }\n\n\ndef discover_runs(data_dir: Path, prefixes: list[str]) -> list[dict]:\n    runs = []\n    seen = set()\n\n    for entry in sorted(data_dir.iterdir()):\n        name = entry.name\n        if not any(name.startswith(p) for p in prefixes):\n            continue\n\n        cond = match_condition(name)\n        seed_val = extract_seed(name)\n        if cond is None or seed_val is None:\n            continue\n        key = (cond, seed_val)\n        if key in seen:\n            continue\n\n        data = None\n        if entry.is_dir():\n            for fname in [\"classify.json\", \"taxonomy.json\"]:\n                data = load_eval_results(entry / fname)\n                if data is not None:\n                    break\n            if data is None:\n                continue\n        elif entry.is_file():\n            if name.endswith(\"_taxonomy_unified.json\"):\n                data = load_taxonomy_unified(entry)\n            elif name.endswith(\"_taxonomy_verification.json\"):\n                data = load_taxonomy_verification(entry)\n            if data is None:\n                continue\n        else:\n            continue\n\n        seen.add(key)\n        runs.append({\n            \"dir_name\": name,\n            \"seed\": seed_val,\n            \"condition\": cond,\n            \"data\": data,\n        })\n\n    return runs\n\n\ndef compute_row(run: dict) -> dict:\n    d = run[\"data\"]\n    n_proved = d.get(\"n_proved\", 0)\n    n_total = d.get(\"n_total\", 100)\n    h7 = d.get(\"h7_total_count\", 0)\n    h7_rate = d.get(\"h7_total_rate\", h7 / n_proved if n_proved > 0 else 0.0)\n    h1 = d.get(\"h1_strict_count\", 0)\n    h8 = d.get(\"h8_conjunction_collapse_count\", 0)\n    genuine = d.get(\"genuine_count\", 0)\n    genuine_rate = d.get(\"genuine_rate\", genuine / n_proved if n_proved > 0 else 0.0)\n    ci = d.get(\"content_independent_count\", 0)\n    snh = max(genuine - ci, 0)\n    snh_rate = snh / n_proved if n_proved > 0 else 0.0\n\n    return {\n        \"seed\": run[\"seed\"],\n        \"condition\": run[\"condition\"],\n        \"n_total\": n_total,\n        \"PR\": n_proved,\n        \"H7_count\": h7,\n        \"H7_rate\": h7_rate,\n        \"H1_count\": h1,\n        \"H8_count\": h8,\n        \"genuine_count\": genuine,\n        \"genuine_rate\": genuine_rate,\n        \"CI_count\": ci,\n        \"SNH_count\": snh,\n        \"SNH_rate\": snh_rate,\n    }\n\n\ndef build_table(runs: list[dict]) -> pd.DataFrame:\n    rows = [compute_row(r) for r in runs]\n    df = pd.DataFrame(rows)\n    df = df.sort_values([\"condition\", \"seed\"]).reset_index(drop=True)\n    return df\n\n\ndef fisher_h7_domination(df: pd.DataFrame) -> dict:\n    results = {}\n    for cond in [\"ISR\", \"RANDOM\"]:\n        sub = df[df[\"condition\"] == cond]\n        results[cond] = {\n            \"n\": len(sub),\n            \"h7_dom\": int((sub[\"H7_rate\"] >= 0.5).sum()),\n            \"not_h7_dom\": int((sub[\"H7_rate\"] < 0.5).sum()),\n        }\n\n    table = np.array([\n        [results[\"ISR\"][\"h7_dom\"], results[\"ISR\"][\"not_h7_dom\"]],\n        [results[\"RANDOM\"][\"h7_dom\"], results[\"RANDOM\"][\"not_h7_dom\"]],\n    ])\n    odds_ratio, p_value = stats.fisher_exact(table, alternative=\"greater\")\n    return {\n        \"table\": table.tolist(),\n        \"ISR\": results[\"ISR\"],\n        \"RANDOM\": results[\"RANDOM\"],\n        \"odds_ratio\": odds_ratio,\n        \"p_value\": p_value,\n    }\n\n\ndef permutation_test_genuine(df: pd.DataFrame, n_perm: int = 10000,\n                              rng_seed: int = 42) -> dict:\n    isr = df[df[\"condition\"] == \"ISR\"][\"genuine_rate\"].values\n    rand = df[df[\"condition\"] == \"RANDOM\"][\"genuine_rate\"].values\n    observed = isr.mean() - rand.mean()\n\n    pooled = np.concatenate([isr, rand])\n    n_isr = len(isr)\n    rng = np.random.default_rng(rng_seed)\n\n    count = 0\n    for _ in range(n_perm):\n        perm = rng.permutation(pooled)\n        diff = perm[:n_isr].mean() - perm[n_isr:].mean()\n        if diff >= observed:\n            count += 1\n\n    return {\n        \"observed_diff\": float(observed),\n        \"p_value\": count / n_perm,\n        \"n_perm\": n_perm,\n        \"isr_mean\": float(isr.mean()),\n        \"random_mean\": float(rand.mean()),\n    }\n\n\ndef mannwhitney_h7(df: pd.DataFrame) -> dict:\n    isr = df[df[\"condition\"] == \"ISR\"][\"H7_rate\"].values\n    rand = df[df[\"condition\"] == \"RANDOM\"][\"H7_rate\"].values\n    u_stat, p_value = stats.mannwhitneyu(isr, rand, alternative=\"greater\")\n    return {\n        \"U\": float(u_stat),\n        \"p_value\": float(p_value),\n        \"isr_median\": float(np.median(isr)),\n        \"random_median\": float(np.median(rand)),\n    }\n\n\ndef condition_stats(df: pd.DataFrame) -> pd.DataFrame:\n    metrics = [\"PR\", \"H7_rate\", \"genuine_rate\", \"SNH_rate\"]\n    rows = []\n    for cond in [\"ISR\", \"RANDOM\"]:\n        sub = df[df[\"condition\"] == cond]\n        row = {\"condition\": cond, \"n_seeds\": len(sub)}\n        for m in metrics:\n            vals = sub[m].values\n            row[f\"{m}_mean\"] = vals.mean()\n            row[f\"{m}_std\"] = vals.std(ddof=1) if len(vals) > 1 else 0.0\n        rows.append(row)\n    return pd.DataFrame(rows)\n\n\ndef format_pct(val: float) -> str:\n    return f\"{val*100:.1f}%\"\n\n\ndef format_mean_std(mean: float, std: float, pct: bool = False) -> str:\n    if pct:\n        return f\"{mean*100:.1f} +/- {std*100:.1f}%\"\n    return f\"{mean:.1f} +/- {std:.1f}\"\n\n\ndef print_per_seed_table(df: pd.DataFrame):\n    print(\"\\n\" + \"=\" * 90)\n    print(\"  PER-SEED RESULTS\")\n    print(\"=\" * 90)\n    cols = [\"condition\", \"seed\", \"PR\", \"H7_count\", \"H7_rate\", \"H1_count\",\n            \"H8_count\", \"genuine_count\", \"genuine_rate\", \"CI_count\", \"SNH_count\", \"SNH_rate\"]\n    fmt = df[cols].copy()\n    fmt[\"H7_rate\"] = fmt[\"H7_rate\"].apply(format_pct)\n    fmt[\"genuine_rate\"] = fmt[\"genuine_rate\"].apply(format_pct)\n    fmt[\"SNH_rate\"] = fmt[\"SNH_rate\"].apply(format_pct)\n    print(fmt.to_string(index=False))\n\n\ndef print_condition_stats(cond_df: pd.DataFrame):\n    print(\"\\n\" + \"=\" * 90)\n    print(\"  CONDITION-LEVEL STATISTICS\")\n    print(\"=\" * 90)\n    for _, row in cond_df.iterrows():\n        print(f\"\\n  {row['condition']} (n={int(row['n_seeds'])} seeds):\")\n        print(f\"    PR:           {format_mean_std(row['PR_mean'], row['PR_std'])}\")\n        print(f\"    H7 rate:      {format_mean_std(row['H7_rate_mean'], row['H7_rate_std'], pct=True)}\")\n        print(f\"    Genuine rate: {format_mean_std(row['genuine_rate_mean'], row['genuine_rate_std'], pct=True)}\")\n        print(f\"    S-NH rate:    {format_mean_std(row['SNH_rate_mean'], row['SNH_rate_std'], pct=True)}\")\n\n\ndef print_tests(fisher, perm, mw):\n    print(\"\\n\" + \"=\" * 90)\n    print(\"  STATISTICAL TESTS\")\n    print(\"=\" * 90)\n\n    print(\"\\n  1. H7 Domination Fisher Exact Test (H7-dominated = H7% >= 50%)\")\n    print(f\"     ISR:    {fisher['ISR']['h7_dom']} dominated / {fisher['ISR']['n']} seeds\")\n    print(f\"     RANDOM: {fisher['RANDOM']['h7_dom']} dominated / {fisher['RANDOM']['n']} seeds\")\n    print(f\"     Contingency: {fisher['table']}\")\n    print(f\"     Odds ratio: {fisher['odds_ratio']:.4f}\")\n    print(f\"     p-value (one-sided, greater): {fisher['p_value']:.4f}\")\n\n    print(f\"\\n  2. Genuine Rate Permutation Test (n_perm={perm['n_perm']})\")\n    print(f\"     ISR mean genuine rate:    {perm['isr_mean']*100:.2f}%\")\n    print(f\"     RANDOM mean genuine rate: {perm['random_mean']*100:.2f}%\")\n    print(f\"     Observed diff: {perm['observed_diff']*100:.2f} pp\")\n    print(f\"     p-value: {perm['p_value']:.4f}\")\n\n    print(f\"\\n  3. H7 Rate Mann-Whitney U Test\")\n    print(f\"     ISR median H7 rate:    {mw['isr_median']*100:.1f}%\")\n    print(f\"     RANDOM median H7 rate: {mw['random_median']*100:.1f}%\")\n    print(f\"     U statistic: {mw['U']:.1f}\")\n    print(f\"     p-value (one-sided, greater): {mw['p_value']:.4f}\")\n\n\ndef generate_markdown(df: pd.DataFrame, cond_df: pd.DataFrame,\n                      fisher: dict, perm: dict, mw: dict) -> str:\n    lines = []\n    lines.append(\"## D134 4B GRPO: ISR vs Random (multi-seed)\\n\")\n\n    lines.append(\"### Per-Seed Results\\n\")\n    lines.append(\"| Condition | Seed | PR | H7 | H7% | H1 | H8 | Genuine | Gen% | CI | S-NH | S-NH% |\")\n    lines.append(\"|-----------|------|----|----|-----|----|----|---------|------|----|------|-------|\")\n    for _, r in df.iterrows():\n        lines.append(\n            f\"| {r['condition']} | {r['seed']} | {r['PR']} | {r['H7_count']} | \"\n            f\"{r['H7_rate']*100:.1f} | {r['H1_count']} | {r['H8_count']} | \"\n            f\"{r['genuine_count']} | {r['genuine_rate']*100:.1f} | {r['CI_count']} | \"\n            f\"{r['SNH_count']} | {r['SNH_rate']*100:.1f} |\"\n        )\n\n    lines.append(\"\\n### Condition Summary (mean +/- std)\\n\")\n    lines.append(\"| Condition | n | PR | H7% | Genuine% | S-NH% |\")\n    lines.append(\"|-----------|---|----|-----|----------|-------|\")\n    for _, r in cond_df.iterrows():\n        lines.append(\n            f\"| {r['condition']} | {int(r['n_seeds'])} | \"\n            f\"{r['PR_mean']:.1f}+/-{r['PR_std']:.1f} | \"\n            f\"{r['H7_rate_mean']*100:.1f}+/-{r['H7_rate_std']*100:.1f} | \"\n            f\"{r['genuine_rate_mean']*100:.1f}+/-{r['genuine_rate_std']*100:.1f} | \"\n            f\"{r['SNH_rate_mean']*100:.1f}+/-{r['SNH_rate_std']*100:.1f} |\"\n        )\n\n    if fisher and perm and mw:\n        lines.append(\"\\n### Statistical Tests\\n\")\n        lines.append(f\"**1. H7 Domination Fisher Exact Test** (H7-dominated = H7% >= 50%)\")\n        lines.append(f\"- ISR: {fisher['ISR']['h7_dom']}/{fisher['ISR']['n']} dominated | \"\n                     f\"RANDOM: {fisher['RANDOM']['h7_dom']}/{fisher['RANDOM']['n']} dominated\")\n        lines.append(f\"- OR = {fisher['odds_ratio']:.4f}, p = {fisher['p_value']:.4f}\\n\")\n\n        lines.append(f\"**2. Genuine Rate Permutation Test** (n={perm['n_perm']})\")\n        lines.append(f\"- ISR: {perm['isr_mean']*100:.2f}% vs RANDOM: {perm['random_mean']*100:.2f}%\")\n        lines.append(f\"- Diff = {perm['observed_diff']*100:.2f} pp, p = {perm['p_value']:.4f}\\n\")\n\n        lines.append(f\"**3. H7 Rate Mann-Whitney U**\")\n        lines.append(f\"- ISR median: {mw['isr_median']*100:.1f}% vs RANDOM median: {mw['random_median']*100:.1f}%\")\n        lines.append(f\"- U = {mw['U']:.1f}, p = {mw['p_value']:.4f}\")\n\n    return \"\\n\".join(lines) + \"\\n\"\n\n\ndef main():\n    args = parse_args()\n    data_dir = Path(args.data_dir)\n\n    if not data_dir.exists():\n        print(f\"ERROR: data directory {data_dir} does not exist\", file=sys.stderr)\n        sys.exit(1)\n\n    if args.prefix:\n        prefixes = [args.prefix]\n    elif args.prefixes:\n        prefixes = [p.strip() for p in args.prefixes.split(\",\")]\n    else:\n        prefixes = MODE_PREFIXES[args.mode]\n    print(f\"Mode: {args.mode} | Prefixes: {prefixes}\")\n\n    runs = discover_runs(data_dir, prefixes)\n    if not runs:\n        print(f\"ERROR: no runs found in {data_dir} with prefixes {prefixes}\", file=sys.stderr)\n        sys.exit(1)\n\n    isr_count = sum(1 for r in runs if r[\"condition\"] == \"ISR\")\n    rand_count = sum(1 for r in runs if r[\"condition\"] == \"RANDOM\")\n    print(f\"Found {len(runs)} runs: {isr_count} ISR, {rand_count} RANDOM\")\n    for r in runs:\n        print(f\"  {r['condition']:6s} s{r['seed']} <- {r['dir_name']}\")\n\n    df = build_table(runs)\n    print_per_seed_table(df)\n\n    cond_df = condition_stats(df)\n    print_condition_stats(cond_df)\n\n    if isr_count < 2 or rand_count < 2:\n        print(\"\\nWARNING: need >= 2 seeds per condition for statistical tests, skipping.\",\n              file=sys.stderr)\n        if args.output:\n            md = generate_markdown(df, cond_df, {}, {}, {})\n            Path(args.output).write_text(md)\n            print(f\"\\nMarkdown written to {args.output}\")\n        return\n\n    fisher = fisher_h7_domination(df)\n    perm = permutation_test_genuine(df, n_perm=args.n_perm, rng_seed=args.seed)\n    mw = mannwhitney_h7(df)\n\n    print_tests(fisher, perm, mw)\n\n    md = generate_markdown(df, cond_df, fisher, perm, mw)\n    print(\"\\n\" + \"=\" * 90)\n    print(\"  MARKDOWN OUTPUT\")\n    print(\"=\" * 90)\n    print(md)\n\n    if args.output:\n        Path(args.output).parent.mkdir(parents=True, exist_ok=True)\n        Path(args.output).write_text(md)\n        print(f\"Markdown written to {args.output}\")\n\n\nif __name__ == \"__main__\":\n    main()\nHEREDOC_EOF",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-18T14:05:30.336505+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.17}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_sync_d134-analysis-remote_20260518T140325",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-18T14:05:30.336663+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-39279",
  "command": "/root/miniconda3/bin/python /root/solver-trace-ablation/scripts/d134_analysis.py --help",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_sync_d134-analysis-remote_20260518T140325",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-39279",
    "command": "/root/miniconda3/bin/python /root/solver-trace-ablation/scripts/d134_analysis.py --help",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-18T14:05:30.336820+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-39279",
  "command": "cd /root/solver-trace-ablation && /root/miniconda3/bin/python scripts/d134_analysis.py --mode d134_only --data_dir /root/autodl-tmp/outputs",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_sync_d134-analysis-remote_20260518T140325",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-39279",
    "command": "cd /root/solver-trace-ablation && /root/miniconda3/bin/python scripts/d134_analysis.py --mode d134_only --data_dir /root/autodl-tmp/outputs",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-18T14:05:30.336961+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"usage: d134_analysis.py [-h] [--data_dir DATA_DIR] [--mode {d134_only,all}]\\n                        [--prefix PREFIX] [--prefixes PREFIXES]\\n                        [--output OUTPUT] [--n_perm N_PERM] [--seed SEED]\\n\\nD134 multi-seed analysis and statistical tests\\n\\noptions:\\n  -h, --help            show this help message and exit\\n  --data_dir DATA_DIR   Directory containing experiment outputs\\n  --mode {d134_only,all}\\n                        d134_only = matched 5+5 design (default); all =\\n                        include original seeds\\n  --prefix PREFIX       (Legacy) Single prefix filter; overrides mode/prefixes\\n  --prefixes PREFIXES   Comma-separated prefixes; overrides --mode\\n  --output OUTPUT       Write markdown summary to this file\\n  --n_perm N_PERM       Number of permutations for permutation test\\n  --seed SEED           Random seed for permutation test\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.46}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_sync_d134-analysis-remote_20260518T140325",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-18T14:05:30.337181+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Mode: d134_only | Prefixes: ['d134_4b']\\nFound 3 runs: 3 ISR, 0 RANDOM\\n  ISR    s47 <- d134_4b_isr_b01_s47\\n  ISR    s48 <- d134_4b_isr_b01_s48\\n  ISR    s49 <- d134_4b_isr_b01_s49\\n\\n==========================================================================================\\n  PER-SEED RESULTS\\n==========================================================================================\\ncondition  seed  PR  H7_count H7_rate  H1_count  H8_count  genuine_count genuine_rate  CI_count  SNH_count SNH_rate\\n      ISR    47  97        83   85.6%         1        10              3         3.1%         8          0     0.0%\\n      ISR    48  66        66  100.0%         0         0              0         0.0%         2          0     0.0%\\n      ISR    49  86        73   84.9%         6         6              1         1.2%         0          1     1.2%\\n\\n==========================================================================================\\n  CONDITION-LEVEL STATISTICS\\n==========================================================================================\\n\\n  ISR (n=3 seeds):\\n    PR:           83.0 +/- 15.7\\n    H7 rate:      90.2 +/- 8.5%\\n    Genuine rate: 1.4 +/- 1.6%\\n    S-NH rate:    0.4 +/- 0.7%\\n\\n  RANDOM (n=0 seeds):\\n    PR:           nan +/- 0.0\\n    H7 rate:      nan +/- 0.0%\\n    Genuine rate: nan +/- 0.0%\\n    S-NH rate:    nan +/- 0.0%\\n\", \"stderr\": \"/root/solver-trace-ablation/scripts/d134_analysis.py:278: RuntimeWarning: Mean of empty slice.\\n  row[f\\\"{m}_mean\\\"] = vals.mean()\\n/root/miniconda3/lib/python3.12/site-packages/numpy/_core/_methods.py:145: RuntimeWarning: invalid value encountered in scalar divide\\n  ret = ret.dtype.type(ret / rcount)\\n\\nWARNING: need >= 2 seeds per condition for statistical tests, skipping.\\n\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.58}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_sync_d134-analysis-remote_20260518T140325",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-18T14:05:30.337375+00:00_

同步完成。

- `--help` 确认 `--mode` 参数存在（choices: d134_only, all）
- Dry run 结果：找到 3 个 ISR runs（s47/s48/s49），0 个 RANDOM runs。ISR 侧 H7 rate 均值 90.2%，genuine rate 均值 1.4%。因 RANDOM 侧无数据，统计检验跳过。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_sync_d134-analysis-remote_20260518T140325"
}
```

</details>

---
