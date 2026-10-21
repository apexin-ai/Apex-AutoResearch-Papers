# analysis docred bcs range matched

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 15
- **Recorded user turns:** 0
- **Tool calls:** 7
- **Original source:** `logs/chats/worker_analysis_docred_bcs_range_matched_20260519T170948.jsonl`
- **Structured JSON:** [`018dad298d6bdd5a24f2.json`](../../sessions/01/018dad298d6bdd5a24f2.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

15 recorded events

### Tool call

_source line 1 · 2026-05-19T17:11:29.458415+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__detect_image",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_docred_bcs_range_matched_20260519T170948",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__detect_image",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-19T17:11:29.458830+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_docred_bcs_range_matched_20260519T170948",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-19T17:11:29.459064+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-38874",
  "command": "find /root/schema-dag-extraction -type f -name \"*bcs*\" -o -name \"*docred*\" -o -name \"*expanded*\" 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_docred_bcs_range_matched_20260519T170948",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-38874",
    "command": "find /root/schema-dag-extraction -type f -name \"*bcs*\" -o -name \"*docred*\" -o -name \"*expanded*\" 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-19T17:11:29.459211+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_docred_bcs_range_matched_20260519T170948",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-19T17:11:29.459339+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-38874",
  "command": "find /root/schema-dag-extraction -type f -name \"*bcs*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_docred_bcs_range_matched_20260519T170948",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-38874",
    "command": "find /root/schema-dag-extraction -type f -name \"*bcs*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-19T17:11:29.459494+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/schema-dag-extraction/src/compute_bcs.py\\n/root/schema-dag-extraction/src/__pycache__/compute_bcs.cpython-312.pyc\\n/root/schema-dag-extraction/src/__pycache__/run_fewshot_bcs.cpython-312.pyc\\n/root/schema-dag-extraction/src/run_fewrel_v2_bcs.py\\n/root/schema-dag-extraction/src/compute_bcs.py.bak\\n/root/schema-dag-extraction/src/run_fewshot_bcs.py\\n/root/schema-dag-extraction/src/run_fewshot_bcs_v2.py\\n/root/schema-dag-extraction/src/run_docred_bcs_expanded.py\\n/root/schema-dag-extraction/artifacts/maven_bcs_matrix_qwen3.pt\\n/root/schema-dag-extraction/artifacts/fewnerd_bcs_matrix_minilm.pt\\n/root/schema-dag-extraction/artifacts/exp007/error_taxonomy_by_bcs.csv\\n/root/schema-dag-extraction/artifacts/exp_docred_confusability/bcs_fix_results.json\\n/root/schema-dag-extraction/artifacts/exp_docred_confusability/bcs_controlled_results.json\\n/root/schema-dag-extraction/artifacts/bcs_fix/bcs_fix_results.json\\n/root/schema-dag-extraction/artifacts/paper/fig_q1_ner_partial_bcs.pdf\\n/root/schema-dag-extraction/artifacts/paper/fig_q1_ner_partial_bcs.png\\n/root/schema-dag-extraction/artifacts/exp_docred_bcs_expanded/bcs_controlled_results.json\\n/root/schema-dag-extraction/logs/fewrel_v2_bcs.log\\n/root/schema-dag-extraction/logs/fewshot_bcs_mitigation.log\\n/root/schema-dag-extraction/results/per_type_bcs_f1_scatter.png\\n/root/schema-dag-extraction/scripts/gen_fig_bcs_scaling.py\\n/root/schema-dag-extraction/scripts/d037/d037_ner_v2_bcs_analysis.py\\n/root/schema-dag-extraction/scripts/d037/d037_ner_v2_bcs_analysis_results.json\\n/root/schema-dag-extraction/scripts/bcs_fix_recompute.py\\n/root/schema-dag-extraction/scripts/run_bcs_controlled_llama70b.py\\n/root/schema-dag-extraction/scripts/q3_bcs_distribution.py\\n/root/schema-dag-extraction/scripts/run_fewshot_bcs_experiment.py\\n/root/schema-dag-extraction/scripts/run_multiseed_bcs.sh\\n/root/schema-dag-extraction/figures/paper/fig_bcs_scaling.pdf
…[truncated 397 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_docred_bcs_range_matched_20260519T170948",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-19T17:11:29.459671+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-38874",
  "command": "cat /root/schema-dag-extraction/artifacts/exp_docred_bcs_expanded/bcs_controlled_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_docred_bcs_range_matched_20260519T170948",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-38874",
    "command": "cat /root/schema-dag-extraction/artifacts/exp_docred_bcs_expanded/bcs_controlled_results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-19T17:11:29.460120+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"bcs_count_16_high_bcs\\\": {\\n    \\\"batches\\\": [\\n      0.5064935064935064,\\n      0.4025974025974026,\\n      0.37662337662337664,\\n      0.4675324675324675,\\n      0.4805194805194805,\\n      0.4675324675324675,\\n      0.36363636363636365,\\n      0.2987012987012987,\\n      0.4805194805194805,\\n      0.4805194805194805,\\n      0.4155844155844156,\\n      0.4805194805194805,\\n      0.38961038961038963,\\n      0.33766233766233766,\\n      0.37662337662337664\\n    ],\\n    \\\"mean_acc\\\": 0.42164502164502166,\\n    \\\"std_acc\\\": 0.061258088143060524,\\n    \\\"bcs_values\\\": [\\n      0.6771903283894062,\\n      0.7205597172180812,\\n      0.7506259034077326,\\n      0.7453926106293997,\\n      0.7570966427524884,\\n      0.6901882817347844,\\n      0.6510756264130274,\\n      0.7203258109589418,\\n      0.7570966427524884,\\n      0.7570966427524884,\\n      0.7312004278103511,\\n      0.7570966427524884,\\n      0.751556758582592,\\n      0.7202082688609759,\\n      0.6510756264130274\\n    ],\\n    \\\"mean_bcs\\\": 0.7225190620952181,\\n    \\\"n_samples\\\": [\\n      77,\\n      77,\\n      77,\\n      77,\\n      77,\\n      77,\\n      77,\\n      77,\\n      77,\\n      77,\\n      77,\\n      77,\\n      77,\\n      77,\\n      77\\n    ]\\n  },\\n  \\\"bcs_count_16_low_bcs\\\": {\\n    \\\"batches\\\": [\\n      0.7105263157894737,\\n      0.6447368421052632,\\n      0.6710526315789473,\\n      0.7123287671232876,\\n      0.6578947368421053,\\n      0.6842105263157895,\\n      0.6842105263157895,\\n      0.6710526315789473,\\n      0.6973684210526315,\\n      0.6578947368421053,\\n      0.6710526315789473,\\n      0.6578947368421053,\\n      0.6447368421052632,\\n      0.6578947368421053,\\n      0.6578947368421053\\n    ],\\n    \\\"mean_acc\\\": 0.6720499879836581,\\n    \\\"std_acc\\\": 0.02087493552543715,\\n    \\\"bcs_values\\\": [\\n      0.380259021371603,\\n   
…[truncated 7098 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_docred_bcs_range_matched_20260519T170948",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-19T17:11:29.460351+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-38874",
  "command": "mkdir -p /root/schema-dag-extraction/analysis",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_docred_bcs_range_matched_20260519T170948",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-38874",
    "command": "mkdir -p /root/schema-dag-extraction/analysis",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-19T17:11:29.460491+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_docred_bcs_range_matched_20260519T170948",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-19T17:11:29.460666+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-38874",
  "command": "cat > /root/schema-dag-extraction/analysis/bcs_range_matched_interaction.py << 'PYEOF'\nimport json\nimport numpy as np\nfrom scipy import stats\n\nwith open(\"/root/schema-dag-extraction/artifacts/exp_docred_bcs_expanded/bcs_controlled_results.json\") as f:\n    data = json.load(f)\n\ndef collect_batches(count_level):\n    \"\"\"Combine high_bcs, low_bcs, random batches for a count level.\"\"\"\n    bcs_all, acc_all = [], []\n    for suffix in [\"high_bcs\", \"low_bcs\", \"random\"]:\n        key = f\"bcs_count_{count_level}_{suffix}\"\n        if key in data:\n            bcs_all.extend(data[key][\"bcs_values\"])\n            acc_all.extend(data[key][\"batches\"])\n    return np.array(bcs_all), np.array(acc_all)\n\ndef analyze(bcs, acc, label):\n    \"\"\"Compute BCS effect via median split, correlation, slope.\"\"\"\n    n = len(bcs)\n    median_bcs = np.median(bcs)\n    high_mask = bcs >= median_bcs\n    low_mask = bcs < median_bcs\n    high_bcs_mean_acc = acc[high_mask].mean()\n    low_bcs_mean_acc = acc[low_mask].mean()\n    bcs_effect = low_bcs_mean_acc - high_bcs_mean_acc  # low BCS = easier = higher acc\n    rho, p_rho = stats.spearmanr(bcs, acc)\n    slope, intercept, r, p_slope, se = stats.linregress(bcs, acc)\n    return {\n        \"label\": label,\n        \"n\": n,\n        \"bcs_range\": [float(bcs.min()), float(bcs.max())],\n        \"spread\": float(bcs.max() - bcs.min()),\n        \"bcs_effect\": bcs_effect,\n        \"rho\": rho,\n        \"p_rho\": p_rho,\n        \"slope\": slope,\n        \"p_slope\": p_slope,\n        \"high_bcs_mean_acc\": high_bcs_mean_acc,\n        \"low_bcs_mean_acc\": low_bcs_mean_acc,\n        \"median_bcs\": median_bcs,\n        \"n_high\": int(high_mask.sum()),\n        \"n_low\": int(low_mask.sum()),\n    }\n\ndef bootstrap_interaction(bcs_16, acc_16, bcs_32, acc_32, B=10000, seed=42):\n    \"\"\"Bootstrap CI for interaction = bcs_effect_16 - bcs_effect_32.\"\"\"\n    rng = np.random.RandomState(seed)\n    n16, n32 = len(bcs_16), len(bcs_32)\n    interactions = []\n    for _ in range(B):\n        idx16 = rng.randint(0, n16, n16)\n        idx32 = rng.randint(0, n32, n32)\n        b16, a16 = bcs_16[idx16], acc_16[idx16]\n        b32, a32 = bcs_32[idx32], acc_32[idx32]\n        med16 = np.median(b16)\n        eff16 = a16[b16 < med16].mean() - a16[b16 >= med16].mean()\n        med32 = np.median(b32)\n        eff32 = a32[b32 < med32].mean() - a32[b32 >= med32].mean()\n        interactions.append(eff16 - eff32)\n    interactions = np.array(interactions)\n    return float(np.percentile(interactions, 2.5)), float(np.percentile(interactions, 97.5))\n\ndef print_section(title, r16, r32, ci):\n    print(f\"\\n{'='*60}\")\n    print(f\" {title}\")\n    print(f\"{'='*60}\")\n    for r in [r16, r32]:\n        print(f\"  count_{r['label']}: n={r['n']}, BCS range=[{r['bcs_range'][0]:.3f}, {r['bcs_range'][1]:.3f}], \"\n              f\"spread={r['spread']:.3f}\")\n        print(f\"    median split: low_BCS(n={r['n_low']}) acc={r['low_bcs_mean_acc']:.4f}, \"\n              f\"high_BCS(n={r['n_high']}) acc={r['high_bcs_mean_acc']:.4f}\")\n        print(f\"    BCS effect = {r['bcs_effect']:.4f} ({r['bcs_effect']*100:.2f}pp)\")\n        print(f\"    Spearman ρ = {r['rho']:.4f} (p={r['p_rho']:.4e})\")\n        print(f\"    Linear slope = {r['slope']:.4f} (p={r['p_slope']:.4e})\")\n    interaction = r16[\"bcs_effect\"] - r32[\"bcs_effect\"]\n    print(f\"\\n  Interaction (BCS_effect_16 - BCS_effect_32) = {interaction:.4f} ({interaction*100:.2f}pp)\")\n    print(f\"  Bootstrap 95% CI: [{ci[0]*100:.2f}pp, {ci[1]*100:.2f}pp]\")\n    return interaction\n\n# === Collect all batches ===\nbcs_16, acc_16 = collect_batches(16)\nbcs_32, acc_32 = collect_batches(32)\n\n# === Before range matching ===\nr16_before = analyze(bcs_16, acc_16, \"16\")\nr32_before = analyze(bcs_32, acc_32, \"32\")\nci_before = bootstrap_interaction(bcs_16, acc_16, bcs_32, acc_32)\nint_before = print_section(\"Before Range Matching\", r16_before, r32_before, ci_before)\n\n# === Find overlap range ===\noverlap_lo = max(bcs_16.min(), bcs_32.min())\noverlap_hi = min(bcs_16.max(), bcs_32.max())\nprint(f\"\\n  BCS overlap range: [{overlap_lo:.4f}, {overlap_hi:.4f}] (spread={overlap_hi-overlap_lo:.4f})\")\n\n# === After range matching ===\nmask_16 = (bcs_16 >= overlap_lo) & (bcs_16 <= overlap_hi)\nmask_32 = (bcs_32 >= overlap_lo) & (bcs_32 <= overlap_hi)\nbcs_16m, acc_16m = bcs_16[mask_16], acc_16[mask_16]\nbcs_32m, acc_32m = bcs_32[mask_32], acc_32[mask_32]\n\nprint(f\"  Batches retained: count_16={mask_16.sum()}/{len(bcs_16)}, count_32={mask_32.sum()}/{len(bcs_32)}\")\n\nr16_after = analyze(bcs_16m, acc_16m, \"16\")\nr32_after = analyze(bcs_32m, acc_32m, \"32\")\nci_after = bootstrap_interaction(bcs_16m, acc_16m, bcs_32m, acc_32m)\nint_after = print_section(\"After Range Matching (BCS ∈ [{:.4f}, {:.4f}])\".format(overlap_lo, overlap_hi),\n                          r16_after, r32_after, ci_after)\n\n# === Conclusion ===\nprint(f\"\\n{'='*60}\")\nprint(f\" Conclusion\")\nprint(f\"{'='*60}\")\nprint(f\"  Interaction change: before {int_before*100:.2f}pp → after {int_after*100:.2f}pp \"\n      f\"(Δ = {(int_after - int_before)*100:.2f}pp)\")\nif abs(int_after) > 0.01 and ci_after[0] * ci_after[1] > 0:\n    print(f\"  Interaction remains significant after range matching → NOT an artifact of BCS range restriction\")\nelif abs(int_after) <= 0.01:\n    print(f\"  Interaction nearly vanishes after range matching → LIKELY an artifact of BCS range restriction\")\nelse:\n    print(f\"  Interaction CI includes zero after range matching → inconclusive\")\n\n# === Save to file ===\nresults = {\n    \"before_matching\": {\n        \"count_16\": r16_before, \"count_32\": r32_before,\n        \"interaction\": float(int_before), \"ci_95\": list(ci_before)\n    },\n    \"overlap_range\": [float(overlap_lo), float(overlap_hi)],\n    \"after_matching\": {\n        \"count_16\": r16_after, \"count_32\": r32_after,\n        \"interaction\": float(int_after), \"ci_95\": list(ci_after)\n    }\n}\nout_path = \"/root/schema-dag-extraction/analysis/bcs_range_matched_results.json\"\nwith open(out_path, \"w\") as f:\n    json.dump(results, f, indent=2)\nprint(f\"\\n  Results saved to {out_path}\")\nPYEOF",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_docred_bcs_range_matched_20260519T170948",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-38874",
    "command": "cat > /root/schema-dag-extraction/analysis/bcs_range_matched_interaction.py << 'PYEOF'\nimport json\nimport numpy as np\nfrom scipy import stats\n\nwith open(\"/root/schema-dag-extraction/artifacts/exp_docred_bcs_expanded/bcs_controlled_results.json\") as f:\n    data = json.load(f)\n\ndef collect_batches(count_level):\n    \"\"\"Combine high_bcs, low_bcs, random batches for a count level.\"\"\"\n    bcs_all, acc_all = [], []\n    for suffix in [\"high_bcs\", \"low_bcs\", \"random\"]:\n        key = f\"bcs_count_{count_level}_{suffix}\"\n        if key in data:\n            bcs_all.extend(data[key][\"bcs_values\"])\n            acc_all.extend(data[key][\"batches\"])\n    return np.array(bcs_all), np.array(acc_all)\n\ndef analyze(bcs, acc, label):\n    \"\"\"Compute BCS effect via median split, correlation, slope.\"\"\"\n    n = len(bcs)\n    median_bcs = np.median(bcs)\n    high_mask = bcs >= median_bcs\n    low_mask = bcs < median_bcs\n    high_bcs_mean_acc = acc[high_mask].mean()\n    low_bcs_mean_acc = acc[low_mask].mean()\n    bcs_effect = low_bcs_mean_acc - high_bcs_mean_acc  # low BCS = easier = higher acc\n    rho, p_rho = stats.spearmanr(bcs, acc)\n    slope, intercept, r, p_slope, se = stats.linregress(bcs, acc)\n    return {\n        \"label\": label,\n        \"n\": n,\n        \"bcs_range\": [float(bcs.min()), float(bcs.max())],\n        \"spread\": float(bcs.max() - bcs.min()),\n        \"bcs_effect\": bcs_effect,\n        \"rho\": rho,\n        \"p_rho\": p_rho,\n        \"slope\": slope,\n        \"p_slope\": p_slope,\n        \"high_bcs_mean_acc\": high_bcs_mean_acc,\n        \"low_bcs_mean_acc\": low_bcs_mean_acc,\n        \"median_bcs\": median_bcs,\n        \"n_high\": int(high_mask.sum()),\n        \"n_low\": int(low_mask.sum()),\n    }\n\ndef bootstrap_interaction(bcs_16, acc_16, bcs_32, acc_32, B=10000, seed=42):\n    \"\"\"Bootstrap CI for interaction = bcs_effect_16 - bcs_effect_32.\"\"\"\n    rng = np.random.RandomState(seed)\n    n16, n32 = len(bcs_16), len(bcs_32)\n    interactions = []\n    for _ in range(B):\n        idx16 = rng.randint(0, n16, n16)\n        idx32 = rng.randint(0, n32, n32)\n        b16, a16 = bcs_16[idx16], acc_16[idx16]\n        b32, a32 = bcs_32[idx32], acc_32[idx32]\n        med16 = np.median(b16)\n        eff16 = a16[b16 < med16].mean() - a16[b16 >= med16].mean()\n        med32 = np.median(b32)\n        eff32 = a32[b32 < med32].mean() - a32[b32 >= med32].mean()\n        interactions.append(eff16 - eff32)\n    interactions = np.array(interactions)\n    return float(np.percentile(interactions, 2.5)), float(np.percentile(interactions, 97.5))\n\ndef print_section(title, r16, r32, ci):\n    print(f\"\\n{'='*60}\")\n    print(f\" {title}\")\n    print(f\"{'='*60}\")\n    for r in [r16, r32]:\n        print(f\"  count_{r['label']}: n={r['n']}, BCS range=[{r['bcs_range'][0]:.3f}, {r['bcs_range'][1]:.3f}], \"\n              f\"spread={r['spread']:.3f}\")\n        print(f\"    median split: low_BCS(n={r['n_low']}) acc={r['low_bcs_mean_acc']:.4f}, \"\n              f\"high_BCS(n={r['n_high']}) acc={r['high_bcs_mean_acc']:.4f}\")\n        print(f\"    BCS effect = {r['bcs_effect']:.4f} ({r['bcs_effect']*100:.2f}pp)\")\n        print(f\"    Spearman ρ = {r['rho']:.4f} (p={r['p_rho']:.4e})\")\n        print(f\"    Linear slope = {r['slope']:.4f} (p={r['p_slope']:.4e})\")\n    interaction = r16[\"bcs_effect\"] - r32[\"bcs_effect\"]\n    print(f\"\\n  Interaction (BCS_effect_16 - BCS_effect_32) = {interaction:.4f} ({interaction*100:.2f}pp)\")\n    print(f\"  Bootstrap 95% CI: [{ci[0]*100:.2f}pp, {ci[1]*100:.2f}pp]\")\n    return interaction\n\n# === Collect all batches ===\nbcs_16, acc_16 = collect_batches(16)\nbcs_32, acc_32 = collect_batches(32)\n\n# === Before range matching ===\nr16_before = analyze(bcs_16, acc_16, \"16\")\nr32_before = analyze(bcs_32, acc_32, \"32\")\nci_before = bootstrap_interaction(bcs_16, acc_16, bcs_32, acc_32)\nint_before = print_section(\"Before Range Matching\", r16_before, r32_before, ci_before)\n\n# === Find overlap range ===\noverlap_lo = max(bcs_16.min(), bcs_32.min())\noverlap_hi = min(bcs_16.max(), bcs_32.max())\nprint(f\"\\n  BCS overlap range: [{overlap_lo:.4f}, {overlap_hi:.4f}] (spread={overlap_hi-overlap_lo:.4f})\")\n\n# === After range matching ===\nmask_16 = (bcs_16 >= overlap_lo) & (bcs_16 <= overlap_hi)\nmask_32 = (bcs_32 >= overlap_lo) & (bcs_32 <= overlap_hi)\nbcs_16m, acc_16m = bcs_16[mask_16], acc_16[mask_16]\nbcs_32m, acc_32m = bcs_32[mask_32], acc_32[mask_32]\n\nprint(f\"  Batches retained: count_16={mask_16.sum()}/{len(bcs_16)}, count_32={mask_32.sum()}/{len(bcs_32)}\")\n\nr16_after = analyze(bcs_16m, acc_16m, \"16\")\nr32_after = analyze(bcs_32m, acc_32m, \"32\")\nci_after = bootstrap_interaction(bcs_16m, acc_16m, bcs_32m, acc_32m)\nint_after = print_section(\"After Range Matching (BCS ∈ [{:.4f}, {:.4f}])\".format(overlap_lo, overlap_hi),\n                          r16_after, r32_after, ci_after)\n\n# === Conclusion ===\nprint(f\"\\n{'='*60}\")\nprint(f\" Conclusion\")\nprint(f\"{'='*60}\")\nprint(f\"  Interaction change: before {int_before*100:.2f}pp → after {int_after*100:.2f}pp \"\n      f\"(Δ = {(int_after - int_before)*100:.2f}pp)\")\nif abs(int_after) > 0.01 and ci_after[0] * ci_after[1] > 0:\n    print(f\"  Interaction remains significant after range matching → NOT an artifact of BCS range restriction\")\nelif abs(int_after) <= 0.01:\n    print(f\"  Interaction nearly vanishes after range matching → LIKELY an artifact of BCS range restriction\")\nelse:\n    print(f\"  Interaction CI includes zero after range matching → inconclusive\")\n\n# === Save to file ===\nresults = {\n    \"before_matching\": {\n        \"count_16\": r16_before, \"count_32\": r32_before,\n        \"interaction\": float(int_before), \"ci_95\": list(ci_before)\n    },\n    \"overlap_range\": [float(overlap_lo), float(overlap_hi)],\n    \"after_matching\": {\n        \"count_16\": r16_after, \"count_32\": r32_after,\n        \"interaction\": float(int_after), \"ci_95\": list(ci_after)\n    }\n}\nout_path = \"/root/schema-dag-extraction/analysis/bcs_range_matched_results.json\"\nwith open(out_path, \"w\") as f:\n    json.dump(results, f, indent=2)\nprint(f\"\\n  Results saved to {out_path}\")\nPYEOF",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-19T17:11:29.460896+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.39}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_docred_bcs_range_matched_20260519T170948",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-19T17:11:29.461034+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-38874",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python /root/schema-dag-extraction/analysis/bcs_range_matched_interaction.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_docred_bcs_range_matched_20260519T170948",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-38874",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python /root/schema-dag-extraction/analysis/bcs_range_matched_interaction.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-19T17:11:29.461200+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\n============================================================\\n Before Range Matching\\n============================================================\\n  count_16: n=55, BCS range=[0.380, 0.757], spread=0.377\\n    median split: low_BCS(n=27) acc=0.6569, high_BCS(n=28) acc=0.4974\\n    BCS effect = 0.1595 (15.95pp)\\n    Spearman ρ = -0.7623 (p=1.3738e-11)\\n    Linear slope = -0.7317 (p=8.9257e-14)\\n  count_32: n=55, BCS range=[0.432, 0.695], spread=0.262\\n    median split: low_BCS(n=27) acc=0.5501, high_BCS(n=28) acc=0.4657\\n    BCS effect = 0.0844 (8.44pp)\\n    Spearman ρ = -0.6929 (p=4.5608e-09)\\n    Linear slope = -0.6296 (p=1.5811e-12)\\n\\n  Interaction (BCS_effect_16 - BCS_effect_32) = 0.0752 (7.52pp)\\n  Bootstrap 95% CI: [1.49pp, 12.83pp]\\n\\n  BCS overlap range: [0.4325, 0.6950] (spread=0.2625)\\n  Batches retained: count_16=29/55, count_32=55/55\\n\\n============================================================\\n After Range Matching (BCS ∈ [0.4325, 0.6950])\\n============================================================\\n  count_16: n=29, BCS range=[0.478, 0.690], spread=0.212\\n    median split: low_BCS(n=14) acc=0.6337, high_BCS(n=15) acc=0.5400\\n    BCS effect = 0.0937 (9.37pp)\\n    Spearman ρ = -0.5958 (p=6.4936e-04)\\n    Linear slope = -1.3087 (p=5.2432e-05)\\n  count_32: n=55, BCS range=[0.432, 0.695], spread=0.262\\n    median split: low_BCS(n=27) acc=0.5501, high_BCS(n=28) acc=0.4657\\n    BCS effect = 0.0844 (8.44pp)\\n    Spearman ρ = -0.6929 (p=4.5608e-09)\\n    Linear slope = -0.6296 (p=1.5811e-12)\\n\\n  Interaction (BCS_effect_16 - BCS_effect_32) = 0.0093 (0.93pp)\\n  Bootstrap 95% CI: [-7.13pp, 7.44pp]\\n\\n============================================================\\n Conclusion\\n============================================================\\n  Interaction change: before 7.52pp → after 0.93pp (Δ = -6.59pp)\\n  Interaction nearly vanishes after range matching → LIKELY an 
…[truncated 233 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_docred_bcs_range_matched_20260519T170948",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-19T17:11:29.461559+00:00_

结果非常清晰：

```
=== Before Range Matching ===
count_16: n=55, BCS range=[0.380, 0.757], spread=0.377
  BCS effect = 15.95pp, ρ = -0.7623, slope = -0.7317
count_32: n=55, BCS range=[0.432, 0.695], spread=0.262
  BCS effect = 8.44pp,  ρ = -0.6929, slope = -0.6296
Interaction = 7.52pp, 95% CI: [1.49pp, 12.83pp]

=== After Range Matching (BCS ∈ [0.4325, 0.6950]) ===
count_16: n=29, BCS range=[0.478, 0.690], spread=0.212
  BCS effect = 9.37pp, ρ = -0.5958, slope = -1.3087
count_32: n=55, BCS range=[0.432, 0.695], spread=0.262
  BCS effect = 8.44pp, ρ = -0.6929, slope = -0.6296
Interaction = 0.93pp, 95% CI: [-7.13pp, 7.44pp]

=== Conclusion ===
Interaction change: 7.52pp → 0.93pp (Δ = -6.59pp)
```

**Reviewer 的担忧成立。** Range matching 后 interaction 从 7.52pp 降到 0.93pp（几乎为零），bootstrap CI 跨零 [-7.13pp, 7.44pp]。原始的 sub-additive interaction 基本是 BCS range restriction 的 artifact——count_16 有更宽的 BCS range（0.377 vs 0.262），使得 median split 能捕获更大的 BCS effect，而非 count 本身产生的调节效应。

值得注意的是 range-matched 后 count_16 的线性斜率（-1.31）反而比 count_32（-0.63）更陡，说明在可比 BCS 范围内，count_16 对 BCS 的敏感度更高而非更低。但这个差异的解读需谨慎，因为 count_16 只剩 29 个 batches（主要是 random 组）。

结果已保存到 `/root/schema-dag-extraction/analysis/bcs_range_matched_results.json`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_docred_bcs_range_matched_20260519T170948"
}
```

</details>

---
