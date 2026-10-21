# code distributional tests

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 0
- **Tool calls:** 6
- **Original source:** `logs/chats/worker_code_distributional-tests_20260517T142156.jsonl`
- **Structured JSON:** [`cfafb23fcc5a2d4c6def.json`](../../sessions/cf/cfafb23fcc5a2d4c6def.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

13 recorded events

### Tool call

_source line 1 · 2026-05-17T14:23:07.726330+00:00_

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
  "session": "worker_code_distributional-tests_20260517T142156",
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

_source line 2 · 2026-05-17T14:23:07.726630+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_distributional-tests_20260517T142156",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-17T14:23:07.726821+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-5090",
  "command": "source /root/miniconda3/bin/activate && head -3 /root/gen-depth-fingerprint/data/features_all_models.csv && echo \"---\" && wc -l /root/gen-depth-fingerprint/data/features_all_models.csv",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_distributional-tests_20260517T142156",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-5090",
    "command": "source /root/miniconda3/bin/activate && head -3 /root/gen-depth-fingerprint/data/features_all_models.csv && echo \"---\" && wc -l /root/gen-depth-fingerprint/data/features_all_models.csv",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-17T14:23:07.726970+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"model_name,seed_id,depth,entropy_mean,entropy_std,entropy_min,entropy_max,tail_decay,ttr,hapax_ratio\\npythia-2.8b,0,0,2.7516980171203613,1.744314193725586,0.003396987915039,8.1875,-0.0023380015550609,0.6565656565656566,0.5454545454545454\\npythia-2.8b,0,1,2.616674900054932,1.59860098361969,0.0011329650878906,7.59375,-0.002411389477936,0.5532994923857868,0.4010152284263959\\n---\\n27530 /root/gen-depth-fingerprint/data/features_all_models.csv\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.19}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_distributional-tests_20260517T142156",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-17T14:23:07.727097+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-5090",
  "command": "source /root/miniconda3/bin/activate && python -c \"\nimport pandas as pd\ndf = pd.read_csv('/root/gen-depth-fingerprint/data/features_all_models.csv')\nprint('Shape:', df.shape)\nprint('Depth value counts:')\nprint(df['depth'].value_counts().sort_index())\n\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_distributional-tests_20260517T142156",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-5090",
    "command": "source /root/miniconda3/bin/activate && python -c \"\nimport pandas as pd\ndf = pd.read_csv('/root/gen-depth-fingerprint/data/features_all_models.csv')\nprint('Shape:', df.shape)\nprint('Depth value counts:')\nprint(df['depth'].value_counts().sort_index())\n\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-17T14:23:07.727260+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Shape: (27529, 10)\\nDepth value counts:\\ndepth\\n0    5972\\n1    5918\\n2    5599\\n3    5181\\n4    4859\\nName: count, dtype: int64\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.73}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_distributional-tests_20260517T142156",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-17T14:23:07.727438+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat > /root/gen-depth-fingerprint/distributional_tests.py << 'SCRIPT'\n\"\"\"S2 Location Shift distributional tests: KS (pairwise) + Levene (3-group) on 3-class depth grouping.\"\"\"\n\nimport json\nimport numpy as np\nimport pandas as pd\nfrom scipy import stats\nfrom pathlib import Path\n\nDATA_PATH = Path(\"/root/gen-depth-fingerprint/data/features_all_models.csv\")\nOUT_PATH = Path(\"/root/gen-depth-fingerprint/results/distributional_tests.json\")\nOUT_PATH.parent.mkdir(parents=True, exist_ok=True)\n\nFEATURES = [\"entropy_mean\", \"entropy_std\", \"entropy_min\", \"entropy_max\", \"tail_decay\", \"ttr\", \"hapax_ratio\"]\nPAIRS = [(\"gen0\", \"gen1\"), (\"gen0\", \"gen2plus\"), (\"gen1\", \"gen2plus\")]\nN_KS_TESTS = len(FEATURES) * len(PAIRS)  # 21\nALPHA = 0.05\n\ndf = pd.read_csv(DATA_PATH)\n\ngroups = {\n    \"gen0\": df[df[\"depth\"] == 0],\n    \"gen1\": df[df[\"depth\"] == 1],\n    \"gen2plus\": df[df[\"depth\"] >= 2],\n}\n\nn_samples = {k: len(v) for k, v in groups.items()}\n\nks_results = {}\nfor feat in FEATURES:\n    ks_results[feat] = {}\n    for g1, g2 in PAIRS:\n        stat, p = stats.ks_2samp(groups[g1][feat].dropna(), groups[g2][feat].dropna())\n        p_corr = min(p * N_KS_TESTS, 1.0)\n        ks_results[feat][f\"{g1}_vs_{g2}\"] = {\n            \"statistic\": round(stat, 6),\n            \"p_value\": float(f\"{p:.6e}\"),\n            \"p_corrected\": float(f\"{p_corr:.6e}\"),\n            \"significant\": p_corr < ALPHA,\n        }\n\nlevene_results = {}\nfor feat in FEATURES:\n    stat, p = stats.levene(\n        groups[\"gen0\"][feat].dropna(),\n        groups[\"gen1\"][feat].dropna(),\n        groups[\"gen2plus\"][feat].dropna(),\n    )\n    levene_results[feat] = {\n        \"statistic\": round(stat, 6),\n        \"p_value\": float(f\"{p:.6e}\"),\n        \"significant\": p < ALPHA,\n    }\n\n# Summary classification\nlocation_shift_shape_preserved = []\nlocation_shift_shape_shift = []\nno_shift = []\n\nfor feat in FEATURES:\n    any_ks_sig = any(ks_results[feat][f\"{g1}_vs_{g2}\"][\"significant\"] for g1, g2 in PAIRS)\n    levene_sig = levene_results[feat][\"significant\"]\n\n    if any_ks_sig and not levene_sig:\n        location_shift_shape_preserved.append(feat)\n    elif any_ks_sig and levene_sig:\n        location_shift_shape_shift.append(feat)\n    else:\n        no_shift.append(feat)\n\noutput = {\n    \"experiment\": \"distributional_tests_s2\",\n    \"date\": \"2026-05-17\",\n    \"n_samples\": n_samples,\n    \"ks_tests\": ks_results,\n    \"levene_tests\": levene_results,\n    \"summary\": {\n        \"location_shift_shape_preserved\": location_shift_shape_preserved,\n        \"location_shift_shape_shift\": location_shift_shape_shift,\n        \"no_shift\": no_shift,\n    },\n}\n\nwith open(OUT_PATH, \"w\") as f:\n    json.dump(output, f, indent=2)\n\n# Print summary\nprint(f\"N samples: gen0={n_samples['gen0']}, gen1={n_samples['gen1']}, gen2plus={n_samples['gen2plus']}\")\nprint(f\"\\nBonferroni correction: {N_KS_TESTS} tests, alpha={ALPHA}\")\nprint(\"\\n=== KS Tests (pairwise, corrected p) ===\")\nfor feat in FEATURES:\n    sigs = []\n    for g1, g2 in PAIRS:\n        r = ks_results[feat][f\"{g1}_vs_{g2}\"]\n        marker = \"*\" if r[\"significant\"] else \" \"\n        sigs.append(f\"  {g1} vs {g2}: D={r['statistic']:.4f}, p_corr={r['p_corrected']:.2e} {marker}\")\n    print(f\"\\n{feat}:\")\n    for s in sigs:\n        print(s)\n\nprint(\"\\n=== Levene's Tests (3-group) ===\")\nfor feat in FEATURES:\n    r = levene_results[feat]\n    marker = \"*\" if r[\"significant\"] else \" \"\n    print(f\"  {feat}: W={r['statistic']:.4f}, p={r['p_value']:.2e} {marker}\")\n\nprint(\"\\n=== Summary Classification ===\")\nprint(f\"  Location shift + shape preserved: {location_shift_shape_preserved}\")\nprint(f\"  Location shift + shape shift:     {location_shift_shape_shift}\")\nprint(f\"  No shift:                         {no_shift}\")\nprint(f\"\\nResults saved to {OUT_PATH}\")\nSCRIPT",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_distributional-tests_20260517T142156",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat > /root/gen-depth-fingerprint/distributional_tests.py << 'SCRIPT'\n\"\"\"S2 Location Shift distributional tests: KS (pairwise) + Levene (3-group) on 3-class depth grouping.\"\"\"\n\nimport json\nimport numpy as np\nimport pandas as pd\nfrom scipy import stats\nfrom pathlib import Path\n\nDATA_PATH = Path(\"/root/gen-depth-fingerprint/data/features_all_models.csv\")\nOUT_PATH = Path(\"/root/gen-depth-fingerprint/results/distributional_tests.json\")\nOUT_PATH.parent.mkdir(parents=True, exist_ok=True)\n\nFEATURES = [\"entropy_mean\", \"entropy_std\", \"entropy_min\", \"entropy_max\", \"tail_decay\", \"ttr\", \"hapax_ratio\"]\nPAIRS = [(\"gen0\", \"gen1\"), (\"gen0\", \"gen2plus\"), (\"gen1\", \"gen2plus\")]\nN_KS_TESTS = len(FEATURES) * len(PAIRS)  # 21\nALPHA = 0.05\n\ndf = pd.read_csv(DATA_PATH)\n\ngroups = {\n    \"gen0\": df[df[\"depth\"] == 0],\n    \"gen1\": df[df[\"depth\"] == 1],\n    \"gen2plus\": df[df[\"depth\"] >= 2],\n}\n\nn_samples = {k: len(v) for k, v in groups.items()}\n\nks_results = {}\nfor feat in FEATURES:\n    ks_results[feat] = {}\n    for g1, g2 in PAIRS:\n        stat, p = stats.ks_2samp(groups[g1][feat].dropna(), groups[g2][feat].dropna())\n        p_corr = min(p * N_KS_TESTS, 1.0)\n        ks_results[feat][f\"{g1}_vs_{g2}\"] = {\n            \"statistic\": round(stat, 6),\n            \"p_value\": float(f\"{p:.6e}\"),\n            \"p_corrected\": float(f\"{p_corr:.6e}\"),\n            \"significant\": p_corr < ALPHA,\n        }\n\nlevene_results = {}\nfor feat in FEATURES:\n    stat, p = stats.levene(\n        groups[\"gen0\"][feat].dropna(),\n        groups[\"gen1\"][feat].dropna(),\n        groups[\"gen2plus\"][feat].dropna(),\n    )\n    levene_results[feat] = {\n        \"statistic\": round(stat, 6),\n        \"p_value\": float(f\"{p:.6e}\"),\n        \"significant\": p < ALPHA,\n    }\n\n# Summary classification\nlocation_shift_shape_preserved = []\nlocation_shift_shape_shift = []\nno_shift = []\n\nfor feat in FEATURES:\n    any_ks_sig = any(ks_results[feat][f\"{g1}_vs_{g2}\"][\"significant\"] for g1, g2 in PAIRS)\n    levene_sig = levene_results[feat][\"significant\"]\n\n    if any_ks_sig and not levene_sig:\n        location_shift_shape_preserved.append(feat)\n    elif any_ks_sig and levene_sig:\n        location_shift_shape_shift.append(feat)\n    else:\n        no_shift.append(feat)\n\noutput = {\n    \"experiment\": \"distributional_tests_s2\",\n    \"date\": \"2026-05-17\",\n    \"n_samples\": n_samples,\n    \"ks_tests\": ks_results,\n    \"levene_tests\": levene_results,\n    \"summary\": {\n        \"location_shift_shape_preserved\": location_shift_shape_preserved,\n        \"location_shift_shape_shift\": location_shift_shape_shift,\n        \"no_shift\": no_shift,\n    },\n}\n\nwith open(OUT_PATH, \"w\") as f:\n    json.dump(output, f, indent=2)\n\n# Print summary\nprint(f\"N samples: gen0={n_samples['gen0']}, gen1={n_samples['gen1']}, gen2plus={n_samples['gen2plus']}\")\nprint(f\"\\nBonferroni correction: {N_KS_TESTS} tests, alpha={ALPHA}\")\nprint(\"\\n=== KS Tests (pairwise, corrected p) ===\")\nfor feat in FEATURES:\n    sigs = []\n    for g1, g2 in PAIRS:\n        r = ks_results[feat][f\"{g1}_vs_{g2}\"]\n        marker = \"*\" if r[\"significant\"] else \" \"\n        sigs.append(f\"  {g1} vs {g2}: D={r['statistic']:.4f}, p_corr={r['p_corrected']:.2e} {marker}\")\n    print(f\"\\n{feat}:\")\n    for s in sigs:\n        print(s)\n\nprint(\"\\n=== Levene's Tests (3-group) ===\")\nfor feat in FEATURES:\n    r = levene_results[feat]\n    marker = \"*\" if r[\"significant\"] else \" \"\n    print(f\"  {feat}: W={r['statistic']:.4f}, p={r['p_value']:.2e} {marker}\")\n\nprint(\"\\n=== Summary Classification ===\")\nprint(f\"  Location shift + shape preserved: {location_shift_shape_preserved}\")\nprint(f\"  Location shift + shape shift:     {location_shift_shape_shift}\")\nprint(f\"  No shift:                         {no_shift}\")\nprint(f\"\\nResults saved to {OUT_PATH}\")\nSCRIPT",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-17T14:23:07.727632+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.32}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_distributional-tests_20260517T142156",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-17T14:23:07.727766+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-5090",
  "command": "source /root/miniconda3/bin/activate && cd /root/gen-depth-fingerprint && python distributional_tests.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_distributional-tests_20260517T142156",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-5090",
    "command": "source /root/miniconda3/bin/activate && cd /root/gen-depth-fingerprint && python distributional_tests.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-17T14:23:07.727912+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Encountered a bad command exit code!\\n\\nCommand: 'source /root/miniconda3/bin/activate && cd /root/gen-depth-fingerprint && python distributional_tests.py'\\n\\nExit code: 1\\n\\nStdout:\\n\\n\\n\\nStderr:\\n\\n    yield from chunks\\n  File \\\"/root/miniconda3/lib/python3.12/json/encoder.py\\\", line 406, in _iterencode_dict\\n    yield from chunks\\n  [Previous line repeated 1 more time]\\n  File \\\"/root/miniconda3/lib/python3.12/json/encoder.py\\\", line 439, in _iterencode\\n    o = _default(o)\\n        ^^^^^^^^^^^\\n  File \\\"/root/miniconda3/lib/python3.12/json/encoder.py\\\", line 180, in default\\n    raise TypeError(f'Object of type {o.__class__.__name__} '\\nTypeError: Object of type bool is not JSON serializable\\n\\n\", \"metadata\": {\"elapsed_seconds\": 1.93}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_distributional-tests_20260517T142156",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-17T14:23:07.728070+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-5090",
  "command": "sed -i 's/\"significant\": p_corr < ALPHA,/\"significant\": bool(p_corr < ALPHA),/' /root/gen-depth-fingerprint/distributional_tests.py && sed -i 's/\"significant\": p < ALPHA,/\"significant\": bool(p < ALPHA),/' /root/gen-depth-fingerprint/distributional_tests.py && source /root/miniconda3/bin/activate && cd /root/gen-depth-fingerprint && python distributional_tests.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_distributional-tests_20260517T142156",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-5090",
    "command": "sed -i 's/\"significant\": p_corr < ALPHA,/\"significant\": bool(p_corr < ALPHA),/' /root/gen-depth-fingerprint/distributional_tests.py && sed -i 's/\"significant\": p < ALPHA,/\"significant\": bool(p < ALPHA),/' /root/gen-depth-fingerprint/distributional_tests.py && source /root/miniconda3/bin/activate && cd /root/gen-depth-fingerprint && python distributional_tests.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-17T14:23:07.728225+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"N samples: gen0=5972, gen1=5918, gen2plus=15639\\n\\nBonferroni correction: 21 tests, alpha=0.05\\n\\n=== KS Tests (pairwise, corrected p) ===\\n\\nentropy_mean:\\n  gen0 vs gen1: D=0.2774, p_corr=1.72e-200 *\\n  gen0 vs gen2plus: D=0.7215, p_corr=0.00e+00 *\\n  gen1 vs gen2plus: D=0.5369, p_corr=0.00e+00 *\\n\\nentropy_std:\\n  gen0 vs gen1: D=0.2255, p_corr=1.26e-131 *\\n  gen0 vs gen2plus: D=0.2310, p_corr=6.17e-202 *\\n  gen1 vs gen2plus: D=0.2850, p_corr=7.94e-308 *\\n\\nentropy_min:\\n  gen0 vs gen1: D=0.1530, p_corr=7.29e-60 *\\n  gen0 vs gen2plus: D=0.4425, p_corr=0.00e+00 *\\n  gen1 vs gen2plus: D=0.3070, p_corr=0.00e+00 *\\n\\nentropy_max:\\n  gen0 vs gen1: D=0.2042, p_corr=1.47e-107 *\\n  gen0 vs gen2plus: D=0.1833, p_corr=3.43e-126 *\\n  gen1 vs gen2plus: D=0.0434, p_corr=3.80e-06 *\\n\\ntail_decay:\\n  gen0 vs gen1: D=0.0507, p_corr=9.31e-06 *\\n  gen0 vs gen2plus: D=0.0790, p_corr=1.32e-22 *\\n  gen1 vs gen2plus: D=0.0521, p_corr=3.06e-09 *\\n\\nttr:\\n  gen0 vs gen1: D=0.7135, p_corr=0.00e+00 *\\n  gen0 vs gen2plus: D=0.8045, p_corr=0.00e+00 *\\n  gen1 vs gen2plus: D=0.5175, p_corr=0.00e+00 *\\n\\nhapax_ratio:\\n  gen0 vs gen1: D=0.7042, p_corr=0.00e+00 *\\n  gen0 vs gen2plus: D=0.8148, p_corr=0.00e+00 *\\n  gen1 vs gen2plus: D=0.5160, p_corr=0.00e+00 *\\n\\n=== Levene's Tests (3-group) ===\\n  entropy_mean: W=1739.5137, p=0.00e+00 *\\n  entropy_std: W=1222.6881, p=0.00e+00 *\\n  entropy_min: W=23.9999, p=3.86e-11 *\\n  entropy_max: W=39.6868, p=6.15e-18 *\\n  tail_decay: W=178.7578, p=7.35e-78 *\\n  ttr: W=1623.1644, p=0.00e+00 *\\n  hapax_ratio: W=707.2465, p=3.01e-300 *\\n\\n=== Summary Classification ===\\n  Location shift + shape preserved: []\\n  Location shift + shape shift:     ['entropy_mean', 'entropy_std', 'entropy_min', 'entropy_max', 'tail_decay', 'ttr', 'hapax_ratio']\\n  No shift:                         []\\n\\nResults saved to /root/gen-depth-fingerprint/results/distributional_te
…[truncated 115 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_distributional-tests_20260517T142156",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-17T14:23:07.728400+00:00_

完成。结果：

**所有 7 个特征的 KS 检验全部显著**（Bonferroni 校正后 p ≈ 0），确认 depth 维度上存在 location shift。

**Levene 检验也全部显著**（p < 1e-10），说明方差也随 depth 变化。

**分类汇总：**
- Location shift + shape preserved: **无**（预期的 entropy_mean/ttr/hapax_ratio 没有出现在这里）
- Location shift + shape shift: **全部 7 个特征**
- No shift: **无**

这意味着 depth 不仅移动分布中心，还改变分布形状（方差）。所有特征都呈现全面漂移，而非简单的 location-only shift。结果已写入 `/root/gen-depth-fingerprint/results/distributional_tests.json`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_code_distributional-tests_20260517T142156"
}
```

</details>

---
