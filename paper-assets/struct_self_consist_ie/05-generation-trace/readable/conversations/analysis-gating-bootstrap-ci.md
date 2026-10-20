# analysis gating bootstrap ci

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 47
- **Recorded user turns:** 0
- **Tool calls:** 23
- **Original source:** `logs/chats/worker_analysis_gating_bootstrap_ci_20260519T101033.jsonl`
- **Structured JSON:** [`b9abe1a91afd4e28630e.json`](../../sessions/b9/b9abe1a91afd4e28630e.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

47 recorded events

### Tool call

_source line 1 · 2026-05-19T10:14:26.395738+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__ssh_read_only",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_gating_bootstrap_ci_20260519T101033",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__ssh_read_only",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-19T10:14:26.396068+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_gating_bootstrap_ci_20260519T101033",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-19T10:14:26.396296+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "ls -la /root/autodl-tmp/struct_self_consist_ie/output/dev_set_lp_probe/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_gating_bootstrap_ci_20260519T101033",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "ls -la /root/autodl-tmp/struct_self_consist_ie/output/dev_set_lp_probe/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-19T10:14:26.396456+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 11292\\ndrwxr-xr-x   2 root root     177 May 19 13:26 .\\ndrwxr-xr-x 183 root root   12288 May 19 15:26 ..\\n-rw-r--r--   1 root root  895014 May 19 13:25 conll2003_dev_samples.jsonl\\n-rw-r--r--   1 root root    1438 May 19 13:26 dev_vs_test_routing.json\\n-rw-r--r--   1 root root  830689 May 19 13:26 fewnerd_dev_samples.jsonl\\n-rw-r--r--   1 root root   88069 May 19 13:26 run.log\\n-rw-r--r--   1 root root 9720394 May 19 13:24 scierc_dev_samples.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.05}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_gating_bootstrap_ci_20260519T101033",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-19T10:14:26.396589+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/dev_set_lp_probe/dev_vs_test_routing.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_gating_bootstrap_ci_20260519T101033",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/dev_set_lp_probe/dev_vs_test_routing.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-19T10:14:26.396759+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"scierc\\\": {\\n    \\\"dev_alignment\\\": {\\n      \\\"mean_rho\\\": 0.21387969609972546,\\n      \\\"adjusted_score\\\": 0.16721503513251265,\\n      \\\"valid_ratio\\\": 0.7818181818181819,\\n      \\\"n_valid\\\": 215,\\n      \\\"n_probe\\\": 275\\n    },\\n    \\\"dev_adjusted_score\\\": 0.16721503513251265,\\n    \\\"dev_routing\\\": \\\"greedy\\\",\\n    \\\"test_adjusted_score\\\": 0.15776560554600277,\\n    \\\"test_routing\\\": \\\"greedy\\\",\\n    \\\"consistent\\\": true,\\n    \\\"threshold\\\": 0.3,\\n    \\\"n_dev_instances\\\": 275,\\n    \\\"n_samples\\\": 8,\\n    \\\"elapsed_seconds\\\": 160.1\\n  },\\n  \\\"conll2003\\\": {\\n    \\\"dev_alignment\\\": {\\n      \\\"mean_rho\\\": 0.29382321549550544,\\n      \\\"adjusted_score\\\": 0.0646411074090112,\\n      \\\"valid_ratio\\\": 0.22,\\n      \\\"n_valid\\\": 11,\\n      \\\"n_probe\\\": 50\\n    },\\n    \\\"dev_adjusted_score\\\": 0.0646411074090112,\\n    \\\"dev_routing\\\": \\\"greedy\\\",\\n    \\\"test_adjusted_score\\\": 0.16594068723061328,\\n    \\\"test_routing\\\": \\\"greedy\\\",\\n    \\\"consistent\\\": true,\\n    \\\"threshold\\\": 0.3,\\n    \\\"n_dev_instances\\\": 50,\\n    \\\"n_samples\\\": 8,\\n    \\\"elapsed_seconds\\\": 34.6\\n  },\\n  \\\"fewnerd\\\": {\\n    \\\"dev_alignment\\\": {\\n      \\\"mean_rho\\\": 0.6145563453606696,\\n      \\\"adjusted_score\\\": 0.5162273301029624,\\n      \\\"valid_ratio\\\": 0.84,\\n      \\\"n_valid\\\": 42,\\n      \\\"n_probe\\\": 50\\n    },\\n    \\\"dev_adjusted_score\\\": 0.5162273301029624,\\n    \\\"dev_routing\\\": \\\"LP\\\",\\n    \\\"test_adjusted_score\\\": 0.4677404427069925,\\n    \\\"test_routing\\\": \\\"LP\\\",\\n    \\\"consistent\\\": true,\\n    \\\"threshold\\\": 0.3,\\n    \\\"n_dev_instances\\\": 50,\\n    \\\"n_samples\\\": 8,\\n    \\\"elapsed_seconds\\\": 46.1\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\"
…[truncated 32 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_gating_bootstrap_ci_20260519T101033",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-19T10:14:26.396933+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "head -1 /root/autodl-tmp/struct_self_consist_ie/output/dev_set_lp_probe/fewnerd_dev_samples.jsonl",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_gating_bootstrap_ci_20260519T101033",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "head -1 /root/autodl-tmp/struct_self_consist_ie/output/dev_set_lp_probe/fewnerd_dev_samples.jsonl",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-19T10:14:26.397340+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\\"id\\\": \\\"fewnerd_dev_11270\\\", \\\"text\\\": \\\"The fermentation of the lactobacillus produces a cloudy appearance , stronger-tasting and spicier flavour compared to ginger ale .\\\", \\\"gold\\\": {\\\"entities\\\": [{\\\"text\\\": \\\"lactobacillus\\\", \\\"type\\\": \\\"other\\\", \\\"start\\\": 24, \\\"end\\\": 37}, {\\\"text\\\": \\\"ginger ale\\\", \\\"type\\\": \\\"product\\\", \\\"start\\\": 118, \\\"end\\\": 128}], \\\"relations\\\": [], \\\"events\\\": []}, \\\"samples\\\": [{\\\"entities\\\": [], \\\"relations\\\": [], \\\"events\\\": [], \\\"cumulative_logprob\\\": -1.1370331048956075, \\\"n_tokens\\\": 14, \\\"mean_logprob\\\": -0.08121665034968625, \\\"token_logprobs\\\": [0.0, 0.0, -2.3841855067985307e-07, -1.1370315551757812, 0.0, 0.0, 0.0, -1.311301275563892e-06, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], \\\"token_texts\\\": [\\\"{\\\\\\\"\\\", \\\"entities\\\", \\\"\\\\\\\":\\\", \\\" [],\\\", \\\" \\\\\\\"\\\", \\\"relations\\\", \\\"\\\\\\\":\\\", \\\" [],\\\", \\\" \\\\\\\"\\\", \\\"events\\\", \\\"\\\\\\\":\\\", \\\" []\\\", \\\"}\\\", \\\"<|im_end|>\\\"]}, {\\\"entities\\\": [], \\\"relations\\\": [], \\\"events\\\": [], \\\"cumulative_logprob\\\": -1.223612427710549, \\\"n_tokens\\\": 14, \\\"mean_logprob\\\": -0.08740088769361064, \\\"token_logprobs\\\": [0.0, 0.0, -2.3841855067985307e-07, -1.2236108779907227, 0.0, 0.0, 0.0, -1.311301275563892e-06, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], \\\"token_texts\\\": [\\\"{\\\\\\\"\\\", \\\"entities\\\", \\\"\\\\\\\":\\\", \\\" [],\\\", \\\" \\\\\\\"\\\", \\\"relations\\\", \\\"\\\\\\\":\\\", \\\" [],\\\", \\\" \\\\\\\"\\\", \\\"events\\\", \\\"\\\\\\\":\\\", \\\" []\\\", \\\"}\\\", \\\"<|im_end|>\\\"]}, {\\\"entities\\\": [{\\\"text\\\": \\\"ginger ale\\\", \\\"type\\\": \\\"product\\\", \\\"start\\\": 118, \\\"end\\\": 128}], \\\"relations\\\": [], \\\"events\\\": [], \\\"cumulative_logprob\\\": -3.9874921726353136, \\\"n_tokens\\\": 43, \\\"mean_logpro
…[truncated 9361 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_gating_bootstrap_ci_20260519T101033",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-19T10:14:26.397532+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "wc -l /root/autodl-tmp/struct_self_consist_ie/output/dev_set_lp_probe/fewnerd_dev_samples.jsonl",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_gating_bootstrap_ci_20260519T101033",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "wc -l /root/autodl-tmp/struct_self_consist_ie/output/dev_set_lp_probe/fewnerd_dev_samples.jsonl",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-19T10:14:26.397671+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"50 /root/autodl-tmp/struct_self_consist_ie/output/dev_set_lp_probe/fewnerd_dev_samples.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_gating_bootstrap_ci_20260519T101033",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-19T10:14:26.397796+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "wc -l /root/autodl-tmp/struct_self_consist_ie/output/dev_set_lp_probe/scierc_dev_samples.jsonl",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_gating_bootstrap_ci_20260519T101033",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "wc -l /root/autodl-tmp/struct_self_consist_ie/output/dev_set_lp_probe/scierc_dev_samples.jsonl",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-19T10:14:26.397920+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "wc -l /root/autodl-tmp/struct_self_consist_ie/output/dev_set_lp_probe/conll2003_dev_samples.jsonl",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_gating_bootstrap_ci_20260519T101033",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "wc -l /root/autodl-tmp/struct_self_consist_ie/output/dev_set_lp_probe/conll2003_dev_samples.jsonl",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-19T10:14:26.398044+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"275 /root/autodl-tmp/struct_self_consist_ie/output/dev_set_lp_probe/scierc_dev_samples.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.64}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_gating_bootstrap_ci_20260519T101033",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-19T10:14:26.398182+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"50 /root/autodl-tmp/struct_self_consist_ie/output/dev_set_lp_probe/conll2003_dev_samples.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.42}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_gating_bootstrap_ci_20260519T101033",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-19T10:14:26.398404+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat > /root/autodl-tmp/struct_self_consist_ie/scripts/gating_bootstrap.py << 'PYEOF'\nimport json\nimport numpy as np\nfrom scipy.stats import spearmanr\nfrom pathlib import Path\nimport warnings\nwarnings.filterwarnings(\"ignore\")\n\nDATA_DIR = Path(\"/root/autodl-tmp/struct_self_consist_ie/output/dev_set_lp_probe\")\nOUT_DIR = Path(\"/root/autodl-tmp/struct_self_consist_ie/output/gating_bootstrap\")\nOUT_DIR.mkdir(parents=True, exist_ok=True)\n\nDATASETS = [\"scierc\", \"conll2003\", \"fewnerd\"]\nB = 1000\nTHRESHOLDS = [0.2, 0.25, 0.3, 0.35, 0.4]\nnp.random.seed(42)\n\ndef compute_entity_f1(pred_entities, gold_entities):\n    \"\"\"Compute entity-level F1 (strict match: text + type + span).\"\"\"\n    def to_set(ents):\n        return set((e[\"text\"], e[\"type\"], e[\"start\"], e[\"end\"]) for e in ents)\n    pred_set = to_set(pred_entities)\n    gold_set = to_set(gold_entities)\n    if len(pred_set) == 0 and len(gold_set) == 0:\n        return 1.0\n    if len(pred_set) == 0 or len(gold_set) == 0:\n        return 0.0\n    tp = len(pred_set & gold_set)\n    prec = tp / len(pred_set) if pred_set else 0.0\n    rec = tp / len(gold_set) if gold_set else 0.0\n    if prec + rec == 0:\n        return 0.0\n    return 2 * prec * rec / (prec + rec)\n\ndef load_dataset(name):\n    \"\"\"Load dataset and compute per-instance (logprobs, f1s, spearman_rho).\"\"\"\n    fpath = DATA_DIR / f\"{name}_dev_samples.jsonl\"\n    instances = []\n    with open(fpath) as f:\n        for line in f:\n            rec = json.loads(line)\n            gold_ents = rec[\"gold\"][\"entities\"]\n            samples = rec[\"samples\"]\n            lps = [s[\"mean_logprob\"] for s in samples]\n            f1s = [compute_entity_f1(s[\"entities\"], gold_ents) for s in samples]\n            \n            # Check degeneracy: all samples identical output\n            unique_f1s = set(f1s)\n            unique_lps = set(lps)\n            is_degenerate = len(unique_f1s) <= 1 or len(unique_lps) <= 1\n            \n            rho = np.nan\n            if not is_degenerate and len(lps) >= 3:\n                rho_val, _ = spearmanr(lps, f1s)\n                if not np.isnan(rho_val):\n                    rho = rho_val\n            \n            instances.append({\n                \"id\": rec[\"id\"],\n                \"rho\": rho,\n                \"is_valid\": not np.isnan(rho),\n                \"is_degenerate\": is_degenerate,\n                \"n_unique_f1\": len(unique_f1s),\n                \"n_unique_lp\": len(unique_lps),\n                \"mean_f1\": np.mean(f1s),\n                \"greedy_f1\": compute_entity_f1(rec[\"greedy\"][\"entities\"], gold_ents),\n                \"f1s\": f1s,\n                \"lps\": lps,\n            })\n    return instances\n\ndef bootstrap_spearman(instances, B=1000):\n    \"\"\"Bootstrap resample instances, compute mean rho per resample.\"\"\"\n    valid_rhos = np.array([inst[\"rho\"] for inst in instances if inst[\"is_valid\"]])\n    n_valid = len(valid_rhos)\n    n_total = len(instances)\n    \n    if n_valid < 3:\n        return {\n            \"mean_rho\": float(np.mean(valid_rhos)) if n_valid > 0 else None,\n            \"ci_lower\": None, \"ci_upper\": None,\n            \"n_valid\": n_valid, \"n_total\": n_total,\n            \"bootstrap_means\": []\n        }\n    \n    # Bootstrap on ALL instances (including invalid -> contribute 0 to adjusted score)\n    all_rhos = np.array([inst[\"rho\"] if inst[\"is_valid\"] else 0.0 for inst in instances])\n    bootstrap_means = []\n    for _ in range(B):\n        idx = np.random.randint(0, n_total, size=n_total)\n        resampled = all_rhos[idx]\n        # Adjusted score = mean of resampled (invalid instances contribute 0)\n        bootstrap_means.append(float(np.mean(resampled)))\n    \n    bootstrap_means = np.array(bootstrap_means)\n    ci_lower = float(np.percentile(bootstrap_means, 2.5))\n    ci_upper = float(np.percentile(bootstrap_means, 97.5))\n    \n    # Also bootstrap just valid rhos for mean_rho CI\n    valid_bootstrap = []\n    for _ in range(B):\n        idx = np.random.randint(0, n_valid, size=n_valid)\n        valid_bootstrap.append(float(np.mean(valid_rhos[idx])))\n    valid_bootstrap = np.array(valid_bootstrap)\n    \n    return {\n        \"mean_rho\": float(np.mean(valid_rhos)),\n        \"adjusted_score\": float(np.mean(all_rhos)),\n        \"ci_lower_adjusted\": ci_lower,\n        \"ci_upper_adjusted\": ci_upper,\n        \"ci_lower_rho\": float(np.percentile(valid_bootstrap, 2.5)),\n        \"ci_upper_rho\": float(np.percentile(valid_bootstrap, 97.5)),\n        \"n_valid\": n_valid,\n        \"n_total\": n_total,\n        \"valid_ratio\": n_valid / n_total,\n        \"degeneracy_rate\": sum(1 for i in instances if i[\"is_degenerate\"]) / n_total,\n    }\n\ndef threshold_sensitivity(instances, thresholds):\n    \"\"\"For each threshold, determine routing decision using bootstrap.\"\"\"\n    valid_rhos = np.array([inst[\"rho\"] for inst in instances if inst[\"is_valid\"]])\n    n_total = len(instances)\n    all_rhos = np.array([inst[\"rho\"] if inst[\"is_valid\"] else 0.0 for inst in instances])\n    \n    results = {}\n    for th in thresholds:\n        # Point estimate\n        adjusted = float(np.mean(all_rhos))\n        point_decision = \"LP\" if adjusted > th else \"greedy\"\n        \n        # Bootstrap stability: how often does the decision flip?\n        lp_count = 0\n        for _ in range(B):\n            idx = np.random.randint(0, n_total, size=n_total)\n            boot_adj = float(np.mean(all_rhos[idx]))\n            if boot_adj > th:\n                lp_count += 1\n        \n        stability = max(lp_count, B - lp_count) / B\n        \n        results[str(th)] = {\n            \"adjusted_score\": adjusted,\n            \"point_decision\": point_decision,\n            \"lp_fraction\": lp_count / B,\n            \"greedy_fraction\": (B - lp_count) / B,\n            \"routing_stability\": stability,\n        }\n    return results\n\ndef analyze_greedy_fallback(instances):\n    \"\"\"Analyze when construction fails and greedy is the fallback.\"\"\"\n    degenerate_instances = [i for i in instances if i[\"is_degenerate\"]]\n    valid_instances = [i for i in instances if i[\"is_valid\"]]\n    \n    # For degenerate instances: check if all samples produce same output\n    all_zero_f1 = [i for i in degenerate_instances if i[\"mean_f1\"] == 0.0]\n    all_perfect_f1 = [i for i in degenerate_instances if i[\"mean_f1\"] == 1.0]\n    \n    # Greedy vs sample mean F1 comparison\n    greedy_wins = sum(1 for i in instances if i[\"greedy_f1\"] > i[\"mean_f1\"])\n    sample_wins = sum(1 for i in instances if i[\"mean_f1\"] > i[\"greedy_f1\"])\n    ties = sum(1 for i in instances if i[\"greedy_f1\"] == i[\"mean_f1\"])\n    \n    # For valid instances: negative rho means LP would pick wrong answer\n    if valid_instances:\n        negative_rho = [i for i in valid_instances if i[\"rho\"] < 0]\n        negative_frac = len(negative_rho) / len(valid_instances)\n    else:\n        negative_frac = 0.0\n    \n    return {\n        \"n_degenerate\": len(degenerate_instances),\n        \"n_total\": len(instances),\n        \"degeneracy_rate\": len(degenerate_instances) / len(instances),\n        \"degenerate_all_zero_f1\": len(all_zero_f1),\n        \"degenerate_all_perfect_f1\": len(all_perfect_f1),\n        \"greedy_vs_sample_mean\": {\n            \"greedy_wins\": greedy_wins,\n            \"sample_wins\": sample_wins,\n            \"ties\": ties,\n        },\n        \"negative_rho_fraction\": negative_frac,\n        \"mean_greedy_f1\": float(np.mean([i[\"greedy_f1\"] for i in instances])),\n        \"mean_sample_f1\": float(np.mean([i[\"mean_f1\"] for i in instances])),\n    }\n\n# Main analysis\nresults = {}\nfor ds in DATASETS:\n    print(f\"\\n{'='*60}\")\n    print(f\"Dataset: {ds}\")\n    print(f\"{'='*60}\")\n    \n    instances = load_dataset(ds)\n    \n    # Bootstrap CI\n    boot = bootstrap_spearman(instances, B=B)\n    print(f\"  mean_rho = {boot['mean_rho']:.4f}, \"\n          f\"CI(rho) = [{boot['ci_lower_rho']:.4f}, {boot['ci_upper_rho']:.4f}]\")\n    print(f\"  adjusted_score = {boot['adjusted_score']:.4f}, \"\n          f\"CI(adj) = [{boot['ci_lower_adjusted']:.4f}, {boot['ci_upper_adjusted']:.4f}]\")\n    print(f\"  valid_ratio = {boot['valid_ratio']:.4f}, degeneracy = {boot['degeneracy_rate']:.4f}\")\n    \n    # Threshold sensitivity\n    thresh = threshold_sensitivity(instances, THRESHOLDS)\n    print(f\"\\n  Threshold sensitivity:\")\n    for th, v in thresh.items():\n        print(f\"    τ={th}: decision={v['point_decision']}, \"\n              f\"LP%={v['lp_fraction']:.3f}, stability={v['routing_stability']:.3f}\")\n    \n    # Greedy fallback\n    fallback = analyze_greedy_fallback(instances)\n    print(f\"\\n  Greedy fallback:\")\n    print(f\"    degeneracy_rate = {fallback['degeneracy_rate']:.4f}\")\n    print(f\"    greedy_f1 = {fallback['mean_greedy_f1']:.4f}, sample_f1 = {fallback['mean_sample_f1']:.4f}\")\n    print(f\"    greedy_wins={fallback['greedy_vs_sample_mean']['greedy_wins']}, \"\n          f\"sample_wins={fallback['greedy_vs_sample_mean']['sample_wins']}, \"\n          f\"ties={fallback['greedy_vs_sample_mean']['ties']}\")\n    print(f\"    negative_rho_fraction = {fallback['negative_rho_fraction']:.4f}\")\n    \n    results[ds] = {\n        \"bootstrap\": boot,\n        \"threshold_sensitivity\": thresh,\n        \"greedy_fallback\": fallback,\n    }\n\n# Routing stability summary across thresholds\nprint(f\"\\n{'='*60}\")\nprint(\"ROUTING STABILITY SUMMARY\")\nprint(f\"{'='*60}\")\nfor th in THRESHOLDS:\n    decisions = {ds: results[ds][\"threshold_sensitivity\"][str(th)][\"point_decision\"] for ds in DATASETS}\n    stabilities = {ds: results[ds][\"threshold_sensitivity\"][str(th)][\"routing_stability\"] for ds in DATASETS}\n    print(f\"τ={th}: {decisions}  stability={stabilities}\")\n\n# Find robust threshold range\nprint(f\"\\nRobust range analysis:\")\nfor th in THRESHOLDS:\n    all_stable = all(\n        results[ds][\"threshold_sensitivity\"][str(th)][\"routing_stability\"] >= 0.95 \n        for ds in DATASETS\n    )\n    print(f\"  τ={th}: all_stable_95%={all_stable}\")\n\n# Save\nwith open(OUT_DIR / \"gating_analysis.json\", \"w\") as f:\n    json.dump(results, f, indent=2)\nprint(f\"\\nSaved to {OUT_DIR / 'gating_analysis.json'}\")\nPYEOF\npython3 /root/autodl-tmp/struct_self_consist_ie/scripts/gating_bootstrap.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_gating_bootstrap_ci_20260519T101033",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat > /root/autodl-tmp/struct_self_consist_ie/scripts/gating_bootstrap.py << 'PYEOF'\nimport json\nimport numpy as np\nfrom scipy.stats import spearmanr\nfrom pathlib import Path\nimport warnings\nwarnings.filterwarnings(\"ignore\")\n\nDATA_DIR = Path(\"/root/autodl-tmp/struct_self_consist_ie/output/dev_set_lp_probe\")\nOUT_DIR = Path(\"/root/autodl-tmp/struct_self_consist_ie/output/gating_bootstrap\")\nOUT_DIR.mkdir(parents=True, exist_ok=True)\n\nDATASETS = [\"scierc\", \"conll2003\", \"fewnerd\"]\nB = 1000\nTHRESHOLDS = [0.2, 0.25, 0.3, 0.35, 0.4]\nnp.random.seed(42)\n\ndef compute_entity_f1(pred_entities, gold_entities):\n    \"\"\"Compute entity-level F1 (strict match: text + type + span).\"\"\"\n    def to_set(ents):\n        return set((e[\"text\"], e[\"type\"], e[\"start\"], e[\"end\"]) for e in ents)\n    pred_set = to_set(pred_entities)\n    gold_set = to_set(gold_entities)\n    if len(pred_set) == 0 and len(gold_set) == 0:\n        return 1.0\n    if len(pred_set) == 0 or len(gold_set) == 0:\n        return 0.0\n    tp = len(pred_set & gold_set)\n    prec = tp / len(pred_set) if pred_set else 0.0\n    rec = tp / len(gold_set) if gold_set else 0.0\n    if prec + rec == 0:\n        return 0.0\n    return 2 * prec * rec / (prec + rec)\n\ndef load_dataset(name):\n    \"\"\"Load dataset and compute per-instance (logprobs, f1s, spearman_rho).\"\"\"\n    fpath = DATA_DIR / f\"{name}_dev_samples.jsonl\"\n    instances = []\n    with open(fpath) as f:\n        for line in f:\n            rec = json.loads(line)\n            gold_ents = rec[\"gold\"][\"entities\"]\n            samples = rec[\"samples\"]\n            lps = [s[\"mean_logprob\"] for s in samples]\n            f1s = [compute_entity_f1(s[\"entities\"], gold_ents) for s in samples]\n            \n            # Check degeneracy: all samples identical output\n            unique_f1s = set(f1s)\n            unique_lps = set(lps)\n            is_degenerate = len(unique_f1s) <= 1 or len(unique_lps) <= 1\n            \n            rho = np.nan\n            if not is_degenerate and len(lps) >= 3:\n                rho_val, _ = spearmanr(lps, f1s)\n                if not np.isnan(rho_val):\n                    rho = rho_val\n            \n            instances.append({\n                \"id\": rec[\"id\"],\n                \"rho\": rho,\n                \"is_valid\": not np.isnan(rho),\n                \"is_degenerate\": is_degenerate,\n                \"n_unique_f1\": len(unique_f1s),\n                \"n_unique_lp\": len(unique_lps),\n                \"mean_f1\": np.mean(f1s),\n                \"greedy_f1\": compute_entity_f1(rec[\"greedy\"][\"entities\"], gold_ents),\n                \"f1s\": f1s,\n                \"lps\": lps,\n            })\n    return instances\n\ndef bootstrap_spearman(instances, B=1000):\n    \"\"\"Bootstrap resample instances, compute mean rho per resample.\"\"\"\n    valid_rhos = np.array([inst[\"rho\"] for inst in instances if inst[\"is_valid\"]])\n    n_valid = len(valid_rhos)\n    n_total = len(instances)\n    \n    if n_valid < 3:\n        return {\n            \"mean_rho\": float(np.mean(valid_rhos)) if n_valid > 0 else None,\n            \"ci_lower\": None, \"ci_upper\": None,\n            \"n_valid\": n_valid, \"n_total\": n_total,\n            \"bootstrap_means\": []\n        }\n    \n    # Bootstrap on ALL instances (including invalid -> contribute 0 to adjusted score)\n    all_rhos = np.array([inst[\"rho\"] if inst[\"is_valid\"] else 0.0 for inst in instances])\n    bootstrap_means = []\n    for _ in range(B):\n        idx = np.random.randint(0, n_total, size=n_total)\n        resampled = all_rhos[idx]\n        # Adjusted score = mean of resampled (invalid instances contribute 0)\n        bootstrap_means.append(float(np.mean(resampled)))\n    \n    bootstrap_means = np.array(bootstrap_means)\n    ci_lower = float(np.percentile(bootstrap_means, 2.5))\n    ci_upper = float(np.percentile(bootstrap_means, 97.5))\n    \n    # Also bootstrap just valid rhos for mean_rho CI\n    valid_bootstrap = []\n    for _ in range(B):\n        idx = np.random.randint(0, n_valid, size=n_valid)\n        valid_bootstrap.append(float(np.mean(valid_rhos[idx])))\n    valid_bootstrap = np.array(valid_bootstrap)\n    \n    return {\n        \"mean_rho\": float(np.mean(valid_rhos)),\n        \"adjusted_score\": float(np.mean(all_rhos)),\n        \"ci_lower_adjusted\": ci_lower,\n        \"ci_upper_adjusted\": ci_upper,\n        \"ci_lower_rho\": float(np.percentile(valid_bootstrap, 2.5)),\n        \"ci_upper_rho\": float(np.percentile(valid_bootstrap, 97.5)),\n        \"n_valid\": n_valid,\n        \"n_total\": n_total,\n        \"valid_ratio\": n_valid / n_total,\n        \"degeneracy_rate\": sum(1 for i in instances if i[\"is_degenerate\"]) / n_total,\n    }\n\ndef threshold_sensitivity(instances, thresholds):\n    \"\"\"For each threshold, determine routing decision using bootstrap.\"\"\"\n    valid_rhos = np.array([inst[\"rho\"] for inst in instances if inst[\"is_valid\"]])\n    n_total = len(instances)\n    all_rhos = np.array([inst[\"rho\"] if inst[\"is_valid\"] else 0.0 for inst in instances])\n    \n    results = {}\n    for th in thresholds:\n        # Point estimate\n        adjusted = float(np.mean(all_rhos))\n        point_decision = \"LP\" if adjusted > th else \"greedy\"\n        \n        # Bootstrap stability: how often does the decision flip?\n        lp_count = 0\n        for _ in range(B):\n            idx = np.random.randint(0, n_total, size=n_total)\n            boot_adj = float(np.mean(all_rhos[idx]))\n            if boot_adj > th:\n                lp_count += 1\n        \n        stability = max(lp_count, B - lp_count) / B\n        \n        results[str(th)] = {\n            \"adjusted_score\": adjusted,\n            \"point_decision\": point_decision,\n            \"lp_fraction\": lp_count / B,\n            \"greedy_fraction\": (B - lp_count) / B,\n            \"routing_stability\": stability,\n        }\n    return results\n\ndef analyze_greedy_fallback(instances):\n    \"\"\"Analyze when construction fails and greedy is the fallback.\"\"\"\n    degenerate_instances = [i for i in instances if i[\"is_degenerate\"]]\n    valid_instances = [i for i in instances if i[\"is_valid\"]]\n    \n    # For degenerate instances: check if all samples produce same output\n    all_zero_f1 = [i for i in degenerate_instances if i[\"mean_f1\"] == 0.0]\n    all_perfect_f1 = [i for i in degenerate_instances if i[\"mean_f1\"] == 1.0]\n    \n    # Greedy vs sample mean F1 comparison\n    greedy_wins = sum(1 for i in instances if i[\"greedy_f1\"] > i[\"mean_f1\"])\n    sample_wins = sum(1 for i in instances if i[\"mean_f1\"] > i[\"greedy_f1\"])\n    ties = sum(1 for i in instances if i[\"greedy_f1\"] == i[\"mean_f1\"])\n    \n    # For valid instances: negative rho means LP would pick wrong answer\n    if valid_instances:\n        negative_rho = [i for i in valid_instances if i[\"rho\"] < 0]\n        negative_frac = len(negative_rho) / len(valid_instances)\n    else:\n        negative_frac = 0.0\n    \n    return {\n        \"n_degenerate\": len(degenerate_instances),\n        \"n_total\": len(instances),\n        \"degeneracy_rate\": len(degenerate_instances) / len(instances),\n        \"degenerate_all_zero_f1\": len(all_zero_f1),\n        \"degenerate_all_perfect_f1\": len(all_perfect_f1),\n        \"greedy_vs_sample_mean\": {\n            \"greedy_wins\": greedy_wins,\n            \"sample_wins\": sample_wins,\n            \"ties\": ties,\n        },\n        \"negative_rho_fraction\": negative_frac,\n        \"mean_greedy_f1\": float(np.mean([i[\"greedy_f1\"] for i in instances])),\n        \"mean_sample_f1\": float(np.mean([i[\"mean_f1\"] for i in instances])),\n    }\n\n# Main analysis\nresults = {}\nfor ds in DATASETS:\n    print(f\"\\n{'='*60}\")\n    print(f\"Dataset: {ds}\")\n    print(f\"{'='*60}\")\n    \n    instances = load_dataset(ds)\n    \n    # Bootstrap CI\n    boot = bootstrap_spearman(instances, B=B)\n    print(f\"  mean_rho = {boot['mean_rho']:.4f}, \"\n          f\"CI(rho) = [{boot['ci_lower_rho']:.4f}, {boot['ci_upper_rho']:.4f}]\")\n    print(f\"  adjusted_score = {boot['adjusted_score']:.4f}, \"\n          f\"CI(adj) = [{boot['ci_lower_adjusted']:.4f}, {boot['ci_upper_adjusted']:.4f}]\")\n    print(f\"  valid_ratio = {boot['valid_ratio']:.4f}, degeneracy = {boot['degeneracy_rate']:.4f}\")\n    \n    # Threshold sensitivity\n    thresh = threshold_sensitivity(instances, THRESHOLDS)\n    print(f\"\\n  Threshold sensitivity:\")\n    for th, v in thresh.items():\n        print(f\"    τ={th}: decision={v['point_decision']}, \"\n              f\"LP%={v['lp_fraction']:.3f}, stability={v['routing_stability']:.3f}\")\n    \n    # Greedy fallback\n    fallback = analyze_greedy_fallback(instances)\n    print(f\"\\n  Greedy fallback:\")\n    print(f\"    degeneracy_rate = {fallback['degeneracy_rate']:.4f}\")\n    print(f\"    greedy_f1 = {fallback['mean_greedy_f1']:.4f}, sample_f1 = {fallback['mean_sample_f1']:.4f}\")\n    print(f\"    greedy_wins={fallback['greedy_vs_sample_mean']['greedy_wins']}, \"\n          f\"sample_wins={fallback['greedy_vs_sample_mean']['sample_wins']}, \"\n          f\"ties={fallback['greedy_vs_sample_mean']['ties']}\")\n    print(f\"    negative_rho_fraction = {fallback['negative_rho_fraction']:.4f}\")\n    \n    results[ds] = {\n        \"bootstrap\": boot,\n        \"threshold_sensitivity\": thresh,\n        \"greedy_fallback\": fallback,\n    }\n\n# Routing stability summary across thresholds\nprint(f\"\\n{'='*60}\")\nprint(\"ROUTING STABILITY SUMMARY\")\nprint(f\"{'='*60}\")\nfor th in THRESHOLDS:\n    decisions = {ds: results[ds][\"threshold_sensitivity\"][str(th)][\"point_decision\"] for ds in DATASETS}\n    stabilities = {ds: results[ds][\"threshold_sensitivity\"][str(th)][\"routing_stability\"] for ds in DATASETS}\n    print(f\"τ={th}: {decisions}  stability={stabilities}\")\n\n# Find robust threshold range\nprint(f\"\\nRobust range analysis:\")\nfor th in THRESHOLDS:\n    all_stable = all(\n        results[ds][\"threshold_sensitivity\"][str(th)][\"routing_stability\"] >= 0.95 \n        for ds in DATASETS\n    )\n    print(f\"  τ={th}: all_stable_95%={all_stable}\")\n\n# Save\nwith open(OUT_DIR / \"gating_analysis.json\", \"w\") as f:\n    json.dump(results, f, indent=2)\nprint(f\"\\nSaved to {OUT_DIR / 'gating_analysis.json'}\")\nPYEOF\npython3 /root/autodl-tmp/struct_self_consist_ie/scripts/gating_bootstrap.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-19T10:14:26.398863+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Encountered a bad command exit code!\\n\\nCommand: 'cat > /root/autodl-tmp/struct_self_consist_ie/scripts/gating_bootstrap.py << \\\\'PYEOF\\\\'\\\\nimport json\\\\nimport numpy as np\\\\nfrom scipy.stats import spearmanr\\\\nfrom pathlib import Path\\\\nimport warnings\\\\nwarnings.filterwarnings(\\\"ignore\\\")\\\\n\\\\nDATA_DIR = Path(\\\"/root/autodl-tmp/struct_self_consist_ie/output/dev_set_lp_probe\\\")\\\\nOUT_DIR = Path(\\\"/root/autodl-tmp/struct_self_consist_ie/output/gating_bootstrap\\\")\\\\nOUT_DIR.mkdir(parents=True, exist_ok=True)\\\\n\\\\nDATASETS = [\\\"scierc\\\", \\\"conll2003\\\", \\\"fewnerd\\\"]\\\\nB = 1000\\\\nTHRESHOLDS = [0.2, 0.25, 0.3, 0.35, 0.4]\\\\nnp.random.seed(42)\\\\n\\\\ndef compute_entity_f1(pred_entities, gold_entities):\\\\n    \\\"\\\"\\\"Compute entity-level F1 (strict match: text + type + span).\\\"\\\"\\\"\\\\n    def to_set(ents):\\\\n        return set((e[\\\"text\\\"], e[\\\"type\\\"], e[\\\"start\\\"], e[\\\"end\\\"]) for e in ents)\\\\n    pred_set = to_set(pred_entities)\\\\n    gold_set = to_set(gold_entities)\\\\n    if len(pred_set) == 0 and len(gold_set) == 0:\\\\n        return 1.0\\\\n    if len(pred_set) == 0 or len(gold_set) == 0:\\\\n        return 0.0\\\\n    tp = len(pred_set & gold_set)\\\\n    prec = tp / len(pred_set) if pred_set else 0.0\\\\n    rec = tp / len(gold_set) if gold_set else 0.0\\\\n    if prec + rec == 0:\\\\n        return 0.0\\\\n    return 2 * prec * rec / (prec + rec)\\\\n\\\\ndef load_dataset(name):\\\\n    \\\"\\\"\\\"Load dataset and compute per-instance (logprobs, f1s, spearman_rho).\\\"\\\"\\\"\\\\n    fpath = DATA_DIR / f\\\"{name}_dev_samples.jsonl\\\"\\\\n    instances = []\\\\n    with open(fpath) as f:\\\\n        for line in f:\\\\n            rec = json.loads(line)\\\\n            gold_ents = rec[\\\"gold\\\"][\\\"entities\\\"]\\\\n            samples = rec[\\\"samples\\\"]\\\\n            lps = [s[\\\"mean_logprob\\\
…[truncated 10336 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_gating_bootstrap_ci_20260519T101033",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-19T10:14:26.399065+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "ls /root/autodl-tmp/struct_self_consist_ie/scripts/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_gating_bootstrap_ci_20260519T101033",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "ls /root/autodl-tmp/struct_self_consist_ie/scripts/",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-19T10:14:26.399224+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "which python",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_gating_bootstrap_ci_20260519T101033",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "which python",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-19T10:14:26.399361+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"adalp_analysis.py\\nanalyze_lp_range_cdf_n529.py\\nanalyze_zero_f1.py\\nanalyze_zero_f1_detail.py\\nc3_lp_range_cdf.py\\ncalibration_baseline.py\\ncompute_within_rho_exp021.py\\nepsilon_sweep.py\\nexp_028_postprocess\\nexp_029a_postprocess\\nexp_029b_postprocess\\ngating_bootstrap.py\\nn_scaling_gf_maxlp.py\\npaired_n8_baseline.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.96}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_gating_bootstrap_ci_20260519T101033",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-19T10:14:26.399485+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: 'which' is not in the read-only allowlist. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_gating_bootstrap_ci_20260519T101033",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-19T10:14:26.399629+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /root/autodl-tmp/struct_self_consist_ie/scripts/gating_bootstrap.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_gating_bootstrap_ci_20260519T101033",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat /root/autodl-tmp/struct_self_consist_ie/scripts/gating_bootstrap.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-19T10:14:26.399898+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"import json\\nimport numpy as np\\nfrom scipy.stats import spearmanr\\nfrom pathlib import Path\\nimport warnings\\nwarnings.filterwarnings(\\\"ignore\\\")\\n\\nDATA_DIR = Path(\\\"/root/autodl-tmp/struct_self_consist_ie/output/dev_set_lp_probe\\\")\\nOUT_DIR = Path(\\\"/root/autodl-tmp/struct_self_consist_ie/output/gating_bootstrap\\\")\\nOUT_DIR.mkdir(parents=True, exist_ok=True)\\n\\nDATASETS = [\\\"scierc\\\", \\\"conll2003\\\", \\\"fewnerd\\\"]\\nB = 1000\\nTHRESHOLDS = [0.2, 0.25, 0.3, 0.35, 0.4]\\nnp.random.seed(42)\\n\\ndef compute_entity_f1(pred_entities, gold_entities):\\n    \\\"\\\"\\\"Compute entity-level F1 (strict match: text + type + span).\\\"\\\"\\\"\\n    def to_set(ents):\\n        return set((e[\\\"text\\\"], e[\\\"type\\\"], e[\\\"start\\\"], e[\\\"end\\\"]) for e in ents)\\n    pred_set = to_set(pred_entities)\\n    gold_set = to_set(gold_entities)\\n    if len(pred_set) == 0 and len(gold_set) == 0:\\n        return 1.0\\n    if len(pred_set) == 0 or len(gold_set) == 0:\\n        return 0.0\\n    tp = len(pred_set & gold_set)\\n    prec = tp / len(pred_set) if pred_set else 0.0\\n    rec = tp / len(gold_set) if gold_set else 0.0\\n    if prec + rec == 0:\\n        return 0.0\\n    return 2 * prec * rec / (prec + rec)\\n\\ndef load_dataset(name):\\n    \\\"\\\"\\\"Load dataset and compute per-instance (logprobs, f1s, spearman_rho).\\\"\\\"\\\"\\n    fpath = DATA_DIR / f\\\"{name}_dev_samples.jsonl\\\"\\n    instances = []\\n    with open(fpath) as f:\\n        for line in f:\\n            rec = json.loads(line)\\n            gold_ents = rec[\\\"gold\\\"][\\\"entities\\\"]\\n            samples = rec[\\\"samples\\\"]\\n            lps = [s[\\\"mean_logprob\\\"] for s in samples]\\n            f1s = [compute_entity_f1(s[\\\"entities\\\"], gold_ents) for s in samples]\\n            \\n            # Check degeneracy: all samples identical output\\n            unique_f1s = set(f1s)\\n          
…[truncated 7272 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_gating_bootstrap_ci_20260519T101033",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-19T10:14:26.400063+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "find /usr/bin /usr/local/bin /root -maxdepth 3 -name \"python*\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_gating_bootstrap_ci_20260519T101033",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "find /usr/bin /usr/local/bin /root -maxdepth 3 -name \"python*\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-19T10:14:26.400219+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/miniconda3/bin/python3.12\\n/root/miniconda3/bin/python3.12-config\\n/root/miniconda3/conda-meta/python-3.12.3-h996f2a0_1.json\\n/root/miniconda3/pkgs/python-3.12.3-h996f2a0_1.conda\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_gating_bootstrap_ci_20260519T101033",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-19T10:14:26.400371+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-5090",
  "command": "/root/miniconda3/bin/python3.12 /root/autodl-tmp/struct_self_consist_ie/scripts/gating_bootstrap.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_gating_bootstrap_ci_20260519T101033",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-5090",
    "command": "/root/miniconda3/bin/python3.12 /root/autodl-tmp/struct_self_consist_ie/scripts/gating_bootstrap.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-19T10:14:26.400535+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\n============================================================\\nDataset: scierc\\n============================================================\\n  mean_rho = 0.2139, CI(rho) = [0.1460, 0.2806]\\n  adjusted_score = 0.1672, CI(adj) = [0.1162, 0.2203]\\n  valid_ratio = 0.7818, degeneracy = 0.2182\\n\\n  Threshold sensitivity:\\n    τ=0.2: decision=greedy, LP%=0.122, stability=0.878\\n    τ=0.25: decision=greedy, LP%=0.003, stability=0.997\\n    τ=0.3: decision=greedy, LP%=0.000, stability=1.000\\n    τ=0.35: decision=greedy, LP%=0.000, stability=1.000\\n    τ=0.4: decision=greedy, LP%=0.000, stability=1.000\\n\\n  Greedy fallback:\\n    degeneracy_rate = 0.2182\\n    greedy_f1 = 0.6346, sample_f1 = 0.5962\\n    greedy_wins=123, sample_wins=90, ties=62\\n    negative_rho_fraction = 0.3302\\n\\n============================================================\\nDataset: conll2003\\n============================================================\\n  mean_rho = 0.2938, CI(rho) = [-0.0612, 0.6204]\\n  adjusted_score = 0.0646, CI(adj) = [-0.0088, 0.1558]\\n  valid_ratio = 0.2200, degeneracy = 0.7800\\n\\n  Threshold sensitivity:\\n    τ=0.2: decision=greedy, LP%=0.001, stability=0.999\\n    τ=0.25: decision=greedy, LP%=0.000, stability=1.000\\n    τ=0.3: decision=greedy, LP%=0.000, stability=1.000\\n    τ=0.35: decision=greedy, LP%=0.000, stability=1.000\\n    τ=0.4: decision=greedy, LP%=0.000, stability=1.000\\n\\n  Greedy fallback:\\n    degeneracy_rate = 0.7800\\n    greedy_f1 = 0.9340, sample_f1 = 0.9174\\n    greedy_wins=9, sample_wins=1, ties=40\\n    negative_rho_fraction = 0.2727\\n\\n============================================================\\nDataset: fewnerd\\n============================================================\\n  mean_rho = 0.6146, CI(rho) = [0.4588, 0.7591]\\n  adjusted_score = 0.5162, CI(adj) = [0.3737, 0.6483]\\n  valid_ratio = 0.8400, degeneracy = 0.1600\\n\\n  Threshold sensitivity:\\n    τ=0.2: d
…[truncated 1652 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_gating_bootstrap_ci_20260519T101033",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-19T10:14:26.400724+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__save_project_file",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_gating_bootstrap_ci_20260519T101033",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__save_project_file",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-19T10:14:26.400853+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_gating_bootstrap_ci_20260519T101033",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-19T10:14:26.400977+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "gating_bootstrap_analysis",
  "type": "data",
  "description": "Bootstrap CI (B=1000) for LP-alignment gating protocol: per-dataset spearman rho CIs, threshold sensitivity analysis (τ∈[0.2,0.4]), greedy fallback analysis with degeneracy rates",
  "project": "struct_self_consist_ie",
  "source_path": "/root/autodl-tmp/struct_self_consist_ie/output/gating_bootstrap/gating_analysis.json",
  "tags": "['R24-N2', 'gating', 'bootstrap', 'rebuttal']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_gating_bootstrap_ci_20260519T101033",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "gating_bootstrap_analysis",
    "type": "data",
    "description": "Bootstrap CI (B=1000) for LP-alignment gating protocol: per-dataset spearman rho CIs, threshold sensitivity analysis (τ∈[0.2,0.4]), greedy fallback analysis with degeneracy rates",
    "project": "struct_self_consist_ie",
    "source_path": "/root/autodl-tmp/struct_self_consist_ie/output/gating_bootstrap/gating_analysis.json",
    "tags": "['R24-N2', 'gating', 'bootstrap', 'rebuttal']"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-19T10:14:26.401153+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"source_path not found: /root/autodl-tmp/struct_self_consist_ie/output/gating_bootstrap/gating_analysis.json\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_gating_bootstrap_ci_20260519T101033",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-19T10:14:26.401330+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/gating_bootstrap/gating_analysis.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_gating_bootstrap_ci_20260519T101033",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/gating_bootstrap/gating_analysis.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-19T10:14:26.401603+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"scierc\\\": {\\n    \\\"bootstrap\\\": {\\n      \\\"mean_rho\\\": 0.21387969609972546,\\n      \\\"adjusted_score\\\": 0.16721503513251265,\\n      \\\"ci_lower_adjusted\\\": 0.11619564183200498,\\n      \\\"ci_upper_adjusted\\\": 0.22032865964571993,\\n      \\\"ci_lower_rho\\\": 0.14604201725493113,\\n      \\\"ci_upper_rho\\\": 0.28060432735553137,\\n      \\\"n_valid\\\": 215,\\n      \\\"n_total\\\": 275,\\n      \\\"valid_ratio\\\": 0.7818181818181819,\\n      \\\"degeneracy_rate\\\": 0.21818181818181817\\n    },\\n    \\\"threshold_sensitivity\\\": {\\n      \\\"0.2\\\": {\\n        \\\"adjusted_score\\\": 0.16721503513251265,\\n        \\\"point_decision\\\": \\\"greedy\\\",\\n        \\\"lp_fraction\\\": 0.122,\\n        \\\"greedy_fraction\\\": 0.878,\\n        \\\"routing_stability\\\": 0.878\\n      },\\n      \\\"0.25\\\": {\\n        \\\"adjusted_score\\\": 0.16721503513251265,\\n        \\\"point_decision\\\": \\\"greedy\\\",\\n        \\\"lp_fraction\\\": 0.003,\\n        \\\"greedy_fraction\\\": 0.997,\\n        \\\"routing_stability\\\": 0.997\\n      },\\n      \\\"0.3\\\": {\\n        \\\"adjusted_score\\\": 0.16721503513251265,\\n        \\\"point_decision\\\": \\\"greedy\\\",\\n        \\\"lp_fraction\\\": 0.0,\\n        \\\"greedy_fraction\\\": 1.0,\\n        \\\"routing_stability\\\": 1.0\\n      },\\n      \\\"0.35\\\": {\\n        \\\"adjusted_score\\\": 0.16721503513251265,\\n        \\\"point_decision\\\": \\\"greedy\\\",\\n        \\\"lp_fraction\\\": 0.0,\\n        \\\"greedy_fraction\\\": 1.0,\\n        \\\"routing_stability\\\": 1.0\\n      },\\n      \\\"0.4\\\": {\\n        \\\"adjusted_score\\\": 0.16721503513251265,\\n        \\\"point_decision\\\": \\\"greedy\\\",\\n        \\\"lp_fraction\\\": 0.0,\\n        \\\"greedy_fraction\\\": 1.0,\\n        \\\"routing_stability\\\": 1.0\\n      }\\n    },\\n    \\\"greedy_fallback\\\": {\\n      \\\"n_degenerate\\\": 60,\
…[truncated 5361 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_gating_bootstrap_ci_20260519T101033",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-19T10:14:26.401798+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "gating_bootstrap_analysis",
  "type": "data",
  "description": "Bootstrap CI (B=1000) for LP-alignment gating protocol: per-dataset spearman rho CIs, threshold sensitivity (τ∈[0.2,0.4]), greedy fallback with degeneracy rates",
  "project": "struct_self_consist_ie",
  "content_filename": "gating_analysis.json",
  "tags": "['R24-N2', 'gating', 'bootstrap', 'rebuttal']",
  "content": "{\n  \"scierc\": {\n    \"bootstrap\": {\n      \"mean_rho\": 0.2139,\n      \"adjusted_score\": 0.1672,\n      \"ci_adjusted\": [0.1162, 0.2203],\n      \"ci_rho\": [0.1460, 0.2806],\n      \"n_valid\": 215, \"n_total\": 275,\n      \"valid_ratio\": 0.782, \"degeneracy_rate\": 0.218\n    },\n    \"threshold_sensitivity\": {\n      \"0.2\": {\"decision\": \"greedy\", \"stability\": 0.878},\n      \"0.25\": {\"decision\": \"greedy\", \"stability\": 0.997},\n      \"0.3\": {\"decision\": \"greedy\", \"stability\": 1.0},\n      \"0.35\": {\"decision\": \"greedy\", \"stability\": 1.0},\n      \"0.4\": {\"decision\": \"greedy\", \"stability\": 1.0}\n    },\n    \"greedy_fallback\": {\n      \"degeneracy_rate\": 0.218,\n      \"greedy_f1\": 0.6346, \"sample_f1\": 0.5962,\n      \"negative_rho_fraction\": 0.330\n    }\n  },\n  \"conll2003\": {\n    \"bootstrap\": {\n      \"mean_rho\": 0.2938,\n      \"adjusted_score\": 0.0646,\n      \"ci_adjusted\": [-0.0088, 0.1558],\n      \"ci_rho\": [-0.0612, 0.6204],\n      \"n_valid\": 11, \"n_total\": 50,\n      \"valid_ratio\": 0.22, \"degeneracy_rate\": 0.78\n    },\n    \"threshold_sensitivity\": {\n      \"0.2\": {\"decision\": \"greedy\", \"stability\": 0.999},\n      \"0.25\": {\"decision\": \"greedy\", \"stability\": 1.0},\n      \"0.3\": {\"decision\": \"greedy\", \"stability\": 1.0},\n      \"0.35\": {\"decision\": \"greedy\", \"stability\": 1.0},\n      \"0.4\": {\"decision\": \"greedy\", \"stability\": 1.0}\n    },\n    \"greedy_fallback\": {\n      \"degeneracy_rate\": 0.78,\n      \"greedy_f1\": 0.934, \"sample_f1\": 0.917,\n      \"negative_rho_fraction\": 0.273\n    }\n  },\n  \"fewnerd\": {\n    \"bootstrap\": {\n      \"mean_rho\": 0.6146,\n      \"adjusted_score\": 0.5162,\n      \"ci_adjusted\": [0.3737, 0.6483],\n      \"ci_rho\": [0.4588, 0.7591],\n      \"n_valid\": 42, \"n_total\": 50,\n      \"valid_ratio\": 0.84, \"degeneracy_rate\": 0.16\n    },\n    \"threshold_sensitivity\": {\n      \"0.2\": {\"decision\": \"LP\", \"stability\": 1.0},\n      \"0.25\": {\"decision\": \"LP\", \"stability\": 1.0},\n      \"0.3\": {\"decision\": \"LP\", \"stability\": 0.996},\n      \"0.35\": {\"decision\": \"LP\", \"stability\": 0.985},\n      \"0.4\": {\"decision\": \"LP\", \"stability\": 0.937}\n    },\n    \"greedy_fallback\": {\n      \"degeneracy_rate\": 0.16,\n      \"greedy_f1\": 0.7595, \"sample_f1\": 0.6249,\n      \"negative_rho_fraction\": 0.143\n    }\n  },\n  \"robust_threshold_range\": \"[0.25, 0.35]\"\n}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_gating_bootstrap_ci_20260519T101033",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "gating_bootstrap_analysis",
    "type": "data",
    "description": "Bootstrap CI (B=1000) for LP-alignment gating protocol: per-dataset spearman rho CIs, threshold sensitivity (τ∈[0.2,0.4]), greedy fallback with degeneracy rates",
    "project": "struct_self_consist_ie",
    "content_filename": "gating_analysis.json",
    "tags": "['R24-N2', 'gating', 'bootstrap', 'rebuttal']",
    "content": "{\n  \"scierc\": {\n    \"bootstrap\": {\n      \"mean_rho\": 0.2139,\n      \"adjusted_score\": 0.1672,\n      \"ci_adjusted\": [0.1162, 0.2203],\n      \"ci_rho\": [0.1460, 0.2806],\n      \"n_valid\": 215, \"n_total\": 275,\n      \"valid_ratio\": 0.782, \"degeneracy_rate\": 0.218\n    },\n    \"threshold_sensitivity\": {\n      \"0.2\": {\"decision\": \"greedy\", \"stability\": 0.878},\n      \"0.25\": {\"decision\": \"greedy\", \"stability\": 0.997},\n      \"0.3\": {\"decision\": \"greedy\", \"stability\": 1.0},\n      \"0.35\": {\"decision\": \"greedy\", \"stability\": 1.0},\n      \"0.4\": {\"decision\": \"greedy\", \"stability\": 1.0}\n    },\n    \"greedy_fallback\": {\n      \"degeneracy_rate\": 0.218,\n      \"greedy_f1\": 0.6346, \"sample_f1\": 0.5962,\n      \"negative_rho_fraction\": 0.330\n    }\n  },\n  \"conll2003\": {\n    \"bootstrap\": {\n      \"mean_rho\": 0.2938,\n      \"adjusted_score\": 0.0646,\n      \"ci_adjusted\": [-0.0088, 0.1558],\n      \"ci_rho\": [-0.0612, 0.6204],\n      \"n_valid\": 11, \"n_total\": 50,\n      \"valid_ratio\": 0.22, \"degeneracy_rate\": 0.78\n    },\n    \"threshold_sensitivity\": {\n      \"0.2\": {\"decision\": \"greedy\", \"stability\": 0.999},\n      \"0.25\": {\"decision\": \"greedy\", \"stability\": 1.0},\n      \"0.3\": {\"decision\": \"greedy\", \"stability\": 1.0},\n      \"0.35\": {\"decision\": \"greedy\", \"stability\": 1.0},\n      \"0.4\": {\"decision\": \"greedy\", \"stability\": 1.0}\n    },\n    \"greedy_fallback\": {\n      \"degeneracy_rate\": 0.78,\n      \"greedy_f1\": 0.934, \"sample_f1\": 0.917,\n      \"negative_rho_fraction\": 0.273\n    }\n  },\n  \"fewnerd\": {\n    \"bootstrap\": {\n      \"mean_rho\": 0.6146,\n      \"adjusted_score\": 0.5162,\n      \"ci_adjusted\": [0.3737, 0.6483],\n      \"ci_rho\": [0.4588, 0.7591],\n      \"n_valid\": 42, \"n_total\": 50,\n      \"valid_ratio\": 0.84, \"degeneracy_rate\": 0.16\n    },\n    \"threshold_sensitivity\": {\n      \"0.2\": {\"decision\": \"LP\", \"stability\": 1.0},\n      \"0.25\": {\"decision\": \"LP\", \"stability\": 1.0},\n      \"0.3\": {\"decision\": \"LP\", \"stability\": 0.996},\n      \"0.35\": {\"decision\": \"LP\", \"stability\": 0.985},\n      \"0.4\": {\"decision\": \"LP\", \"stability\": 0.937}\n    },\n    \"greedy_fallback\": {\n      \"degeneracy_rate\": 0.16,\n      \"greedy_f1\": 0.7595, \"sample_f1\": 0.6249,\n      \"negative_rho_fraction\": 0.143\n    }\n  },\n  \"robust_threshold_range\": \"[0.25, 0.35]\"\n}"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-19T10:14:26.401977+00:00_

Error executing tool register_artifact: 1 validation error for register_artifactArguments
content
  Input should be a valid string [type=string_type, input_value={'scierc': {'bootstrap': ..._range': '[0.25, 0.35]'}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.12/v/string_type

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_gating_bootstrap_ci_20260519T101033",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-19T10:14:26.402120+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "gating_bootstrap_analysis",
  "type": "data",
  "description": "Bootstrap CI (B=1000) for LP-alignment gating protocol: per-dataset spearman rho CIs, threshold sensitivity (τ∈[0.2,0.4]), greedy fallback with degeneracy rates. Full JSON on server: /root/autodl-tmp/struct_self_consist_ie/output/gating_bootstrap/gating_analysis.json",
  "project": "struct_self_consist_ie",
  "content_filename": "gating_analysis_summary.json",
  "tags": "['R24-N2', 'gating', 'bootstrap', 'rebuttal']",
  "content": "{\"scierc\":{\"bootstrap\":{\"mean_rho\":0.2139,\"adjusted_score\":0.1672,\"ci_adjusted\":[0.1162,0.2203],\"ci_rho\":[0.1460,0.2806],\"n_valid\":215,\"n_total\":275,\"valid_ratio\":0.782,\"degeneracy_rate\":0.218},\"routing\":\"greedy\",\"stability_at_0.3\":1.0},\"conll2003\":{\"bootstrap\":{\"mean_rho\":0.2938,\"adjusted_score\":0.0646,\"ci_adjusted\":[-0.0088,0.1558],\"ci_rho\":[-0.0612,0.6204],\"n_valid\":11,\"n_total\":50,\"valid_ratio\":0.22,\"degeneracy_rate\":0.78},\"routing\":\"greedy\",\"stability_at_0.3\":1.0},\"fewnerd\":{\"bootstrap\":{\"mean_rho\":0.6146,\"adjusted_score\":0.5162,\"ci_adjusted\":[0.3737,0.6483],\"ci_rho\":[0.4588,0.7591],\"n_valid\":42,\"n_total\":50,\"valid_ratio\":0.84,\"degeneracy_rate\":0.16},\"routing\":\"LP\",\"stability_at_0.3\":0.996},\"robust_threshold_range\":\"[0.25, 0.35]\"}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_gating_bootstrap_ci_20260519T101033",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "gating_bootstrap_analysis",
    "type": "data",
    "description": "Bootstrap CI (B=1000) for LP-alignment gating protocol: per-dataset spearman rho CIs, threshold sensitivity (τ∈[0.2,0.4]), greedy fallback with degeneracy rates. Full JSON on server: /root/autodl-tmp/struct_self_consist_ie/output/gating_bootstrap/gating_analysis.json",
    "project": "struct_self_consist_ie",
    "content_filename": "gating_analysis_summary.json",
    "tags": "['R24-N2', 'gating', 'bootstrap', 'rebuttal']",
    "content": "{\"scierc\":{\"bootstrap\":{\"mean_rho\":0.2139,\"adjusted_score\":0.1672,\"ci_adjusted\":[0.1162,0.2203],\"ci_rho\":[0.1460,0.2806],\"n_valid\":215,\"n_total\":275,\"valid_ratio\":0.782,\"degeneracy_rate\":0.218},\"routing\":\"greedy\",\"stability_at_0.3\":1.0},\"conll2003\":{\"bootstrap\":{\"mean_rho\":0.2938,\"adjusted_score\":0.0646,\"ci_adjusted\":[-0.0088,0.1558],\"ci_rho\":[-0.0612,0.6204],\"n_valid\":11,\"n_total\":50,\"valid_ratio\":0.22,\"degeneracy_rate\":0.78},\"routing\":\"greedy\",\"stability_at_0.3\":1.0},\"fewnerd\":{\"bootstrap\":{\"mean_rho\":0.6146,\"adjusted_score\":0.5162,\"ci_adjusted\":[0.3737,0.6483],\"ci_rho\":[0.4588,0.7591],\"n_valid\":42,\"n_total\":50,\"valid_ratio\":0.84,\"degeneracy_rate\":0.16},\"routing\":\"LP\",\"stability_at_0.3\":0.996},\"robust_threshold_range\":\"[0.25, 0.35]\"}"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-19T10:14:26.402311+00:00_

Error executing tool register_artifact: 1 validation error for register_artifactArguments
content
  Input should be a valid string [type=string_type, input_value={'scierc': {'bootstrap': ..._range': '[0.25, 0.35]'}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.12/v/string_type

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_gating_bootstrap_ci_20260519T101033",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-19T10:14:26.402460+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "gating_bootstrap_analysis",
  "type": "data",
  "description": "Bootstrap CI (B=1000) for LP-alignment gating protocol. Full data on server: /root/autodl-tmp/struct_self_consist_ie/output/gating_bootstrap/gating_analysis.json",
  "project": "struct_self_consist_ie",
  "content": "SciERC: rho=0.214 CI[0.146,0.281], adj=0.167 CI[0.116,0.220] -> greedy (stability=1.0 at tau=0.3)\nCoNLL2003: rho=0.294 CI[-0.061,0.620], adj=0.065 CI[-0.009,0.156] -> greedy (stability=1.0, 78% degeneracy)\nFewNERD: rho=0.615 CI[0.459,0.759], adj=0.516 CI[0.374,0.648] -> LP (stability=0.996 at tau=0.3)\nRobust threshold range: [0.25, 0.35] (all datasets stable >= 95%)\nRouting decisions identical across all thresholds [0.2, 0.4]",
  "content_filename": "gating_analysis_summary.txt",
  "tags": "['R24-N2', 'gating', 'bootstrap', 'rebuttal']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_gating_bootstrap_ci_20260519T101033",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "gating_bootstrap_analysis",
    "type": "data",
    "description": "Bootstrap CI (B=1000) for LP-alignment gating protocol. Full data on server: /root/autodl-tmp/struct_self_consist_ie/output/gating_bootstrap/gating_analysis.json",
    "project": "struct_self_consist_ie",
    "content": "SciERC: rho=0.214 CI[0.146,0.281], adj=0.167 CI[0.116,0.220] -> greedy (stability=1.0 at tau=0.3)\nCoNLL2003: rho=0.294 CI[-0.061,0.620], adj=0.065 CI[-0.009,0.156] -> greedy (stability=1.0, 78% degeneracy)\nFewNERD: rho=0.615 CI[0.459,0.759], adj=0.516 CI[0.374,0.648] -> LP (stability=0.996 at tau=0.3)\nRobust threshold range: [0.25, 0.35] (all datasets stable >= 95%)\nRouting decisions identical across all thresholds [0.2, 0.4]",
    "content_filename": "gating_analysis_summary.txt",
    "tags": "['R24-N2', 'gating', 'bootstrap', 'rebuttal']"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-19T10:14:26.402609+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260519_77765d\", \"name\": \"gating_bootstrap_analysis\", \"type\": \"data\", \"description\": \"Bootstrap CI (B=1000) for LP-alignment gating protocol. Full data on server: /root/autodl-tmp/struct_self_consist_ie/output/gating_bootstrap/gating_analysis.json\", \"path\": \"projects/struct_self_consist_ie/artifacts/_project/data/gating_analysis_summary.txt\", \"url\": null, \"project\": \"struct_self_consist_ie\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-19T10:13:20.473750+00:00\", \"tags\": [\"R24-N2\", \"gating\", \"bootstrap\", \"rebuttal\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_gating_bootstrap_ci_20260519T101033",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-19T10:14:26.402755+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "file": "memory.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_gating_bootstrap_ci_20260519T101033",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "file": "memory.md"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-19T10:14:26.402876+00:00_

Error executing tool read_project_file: 1 validation error for read_project_fileArguments
project
  Field required [type=missing, input_value={'file': 'memory.md'}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.12/v/missing

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_gating_bootstrap_ci_20260519T101033",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-19T10:14:26.402995+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_gating_bootstrap_ci_20260519T101033",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_project_file",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-19T10:14:26.403113+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_gating_bootstrap_ci_20260519T101033",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-19T10:14:26.403251+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "memory.md",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_gating_bootstrap_ci_20260519T101033",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "file": "memory.md",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-19T10:14:26.403448+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/memory.md\", \"content\": \"## SciERC-Qwen4B 论文 Framing 决策（2026-05-18, Director 指令）\\n\\nSciERC-Qwen4B (degen=10.4%, ρ=0.189, LP delta=-2.23pp) **不是** Two-Condition 框架的反例。ρ=0.189 属于 weak alignment，Two-Condition Theory 预测在 weak alignment 下 LP selection 无效，这是预期失败。论文不要 frame 成 counterexample，而是作为 weak alignment 的 expected negative case。\\n\\n## 🔴 退化率定义修正（2026-05-18, CRITICAL）\\n\\n旧 report.json 中的 \\\"degen_rate\\\" 实际是 `sample_f1_pct_zero`（样本级 F1=0 百分比），**不是**退化率（实例级 constant-F1 gold-filtered）。两者数值差异巨大：\\n\\n| 数据集 | 旧值(sample_f1_pct_zero) | 真实退化率(unified) | 差距 |\\n|--------|--------------------------|---------------------|------|\\n| Qwen CoNLL s42 | 7.6% | 48.4% | +40.9pp |\\n| LLaMA CoNLL s42 | 4.3% | 86.5% | +82.2pp |\\n| SciERC T=0.5 | 10.3% | 41.4% | +31.1pp |\\n| Qwen SciERC s42 | 12.6% | 17.8% | +5.2pp |\\n\\n关键影响：\\n1. CoNLL 是高退化率数据集（~48-55% Qwen, ~86% LLaMA），不是低退化率\\n2. T 消融趋势正确方向：T=0.5(41.4%) > T=0.8(23.8%) > T=1.0(17.8%) > T=1.2(14.9%)，退化率随温度升高单调下降\\n3. **所有论文引用的退化率必须来自 unified_metrics.compute_degeneracy()，禁止从旧 report.json 取值**\\n\\n## FewNERD unified 退化率（2026-05-18, 4-seed 最终版）\\n\\n4-seed 统计（unified_metrics.compute_degeneracy, N=8, 32565 gold-filtered inst）：\\n- seed=42: **13.75%**, seed=123: **13.1%**, seed=456: **12.1%**, seed=789: **11.77%**\\n- 4-seed mean: **12.69%** [95% CI: 11.24%, 14.14%]\\n- LP Δ: +1.36/+1.44/+1.37/+1.36pp, mean=**+1.38pp** [95% CI: +1.32, +1.44]\\n- Greedy F1: 0.7481 [0.7475, 0.7487], Oracle F1: 0.8739 [0.8695, 0.8783]\\n- DGS: seed789 +1.43pp vs greedy\\n\\n历史错误值：10.13%（旧 full_signal_analysis.json 用未迁移脚本生成），7.06%（exp_027 N=16 子集）。\\n\\nmulti-seed 对比统一用 exp_021_inference (N=8, 全集 37648→32565 gold-filtered)，不用 exp_027_fewnerd_n16 (N=16, 5000→4351 子集)。\\n\\n## Epoch DGS 分析结果（2026-05-18）\\n\\nSciERC 不同 epoch/rank 下退化率与 DGS 增益的关系（已用 unified_metrics 验证）：\\n\\n| 设置 | 退化率 | Greedy | DGS | DGS-Greedy | Or
…[truncated 4938 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_gating_bootstrap_ci_20260519T101033",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-19T10:14:26.403661+00:00_

called mcp__agent-ml-research__save_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__save_project_file</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "memory.md",
  "content": "## SciERC-Qwen4B 论文 Framing 决策（2026-05-18, Director 指令）\n\nSciERC-Qwen4B (degen=10.4%, ρ=0.189, LP delta=-2.23pp) **不是** Two-Condition 框架的反例。ρ=0.189 属于 weak alignment，Two-Condition Theory 预测在 weak alignment 下 LP selection 无效，这是预期失败。论文不要 frame 成 counterexample，而是作为 weak alignment 的 expected negative case。\n\n## 🔴 退化率定义修正（2026-05-18, CRITICAL）\n\n旧 report.json 中的 \"degen_rate\" 实际是 `sample_f1_pct_zero`（样本级 F1=0 百分比），**不是**退化率（实例级 constant-F1 gold-filtered）。两者数值差异巨大：\n\n| 数据集 | 旧值(sample_f1_pct_zero) | 真实退化率(unified) | 差距 |\n|--------|--------------------------|---------------------|------|\n| Qwen CoNLL s42 | 7.6% | 48.4% | +40.9pp |\n| LLaMA CoNLL s42 | 4.3% | 86.5% | +82.2pp |\n| SciERC T=0.5 | 10.3% | 41.4% | +31.1pp |\n| Qwen SciERC s42 | 12.6% | 17.8% | +5.2pp |\n\n关键影响：\n1. CoNLL 是高退化率数据集（~48-55% Qwen, ~86% LLaMA），不是低退化率\n2. T 消融趋势正确方向：T=0.5(41.4%) > T=0.8(23.8%) > T=1.0(17.8%) > T=1.2(14.9%)，退化率随温度升高单调下降\n3. **所有论文引用的退化率必须来自 unified_metrics.compute_degeneracy()，禁止从旧 report.json 取值**\n\n## FewNERD unified 退化率（2026-05-18, 4-seed 最终版）\n\n4-seed 统计（unified_metrics.compute_degeneracy, N=8, 32565 gold-filtered inst）：\n- seed=42: **13.75%**, seed=123: **13.1%**, seed=456: **12.1%**, seed=789: **11.77%**\n- 4-seed mean: **12.69%** [95% CI: 11.24%, 14.14%]\n- LP Δ: +1.36/+1.44/+1.37/+1.36pp, mean=**+1.38pp** [95% CI: +1.32, +1.44]\n- Greedy F1: 0.7481 [0.7475, 0.7487], Oracle F1: 0.8739 [0.8695, 0.8783]\n- DGS: seed789 +1.43pp vs greedy\n\n历史错误值：10.13%（旧 full_signal_analysis.json 用未迁移脚本生成），7.06%（exp_027 N=16 子集）。\n\nmulti-seed 对比统一用 exp_021_inference (N=8, 全集 37648→32565 gold-filtered)，不用 exp_027_fewnerd_n16 (N=16, 5000→4351 子集)。\n\n## Epoch DGS 分析结果（2026-05-18）\n\nSciERC 不同 epoch/rank 下退化率与 DGS 增益的关系（已用 unified_metrics 验证）：\n\n| 设置 | 退化率 | Greedy | DGS | DGS-Greedy | Oracle Headroom |\n|------|--------|--------|-----|------------|-----------------|\n| 3-epoch | 6.4% | 0.6501 | 0.6383 | -1.18pp n.s. | 14.97pp |\n| 5-epoch | 17.8% | 0.6439 | 0.6513 | +0.74pp n.s. | 13.19pp |\n| 10-epoch | 47.8% | 0.6467 | 0.6567 | +0.99pp sig | 8.64pp |\n| rank=8 | 7.2% | 0.6397 | 0.6350 | -0.47pp n.s. | 16.01pp |\n\n## Oracle F1 聚合方式差异（2026-05-18）\n\n旧 `run_mvp_pilot.py` 用 corpus-level micro-averaged F1（先聚合 TP/FP/FN 再算 F1），unified_metrics 用 per-instance F1（逐实例算 F1 后取均值）。论文统一用 per-instance F1。\n\n## 统一 F1 修复（2026-05-18）\n\nF1 不一致的根因：DGS 脚本指向旧数据路径 exp001_n16_seed42（应为 exp_012_rerun_1024），adaptive_temperature 用了不同数据源 + structural-identity 退化定义。已通过 unified_metrics.py 统一修复。修复后 DGS 正确数字：SciERC +0.74pp, FewNERD +1.37pp, CoNLL -0.81pp。\n\n## Feature Bottleneck 结论（2026-05-18）\n\n5 个 confidence signal 的判别力天花板限制了所有 selection 方法。MLP/RF 无法超越 LR 或 greedy。CCS（级联选择）、Entity Consensus、Adaptive Temperature 均为 negative。这支持 diagnostic（而非 prescriptive method）的论文 framing。\n\n## 跨模型验证（2026-05-18, 更新 2026-05-19）\n\nLLaMA-3.1-8B 在 SciERC（3 seeds）和 CoNLL 上确认：structural signal（SJ/FK/VC/EM）ρ >> LP ρ，与 Qwen 一致。\n\n**LLaMA FewNERD（2026-05-19, 3 seeds）**：pattern 不同——LP 是唯一正向 selection signal (+0.36pp)，所有 structural signals 负向（SJ -0.52, FK -0.53, EM -1.02, VC -2.39）。degeneracy 23.36%（远高于 Qwen 12.69%）。推测原因：LLaMA 在 T=1.0 产出更多 degenerate sets，structural signals 被 noise 淹没。LP robustness 跨模型一致（Qwen 和 LLaMA 上均为正向信号）。\n\n## F1 审计表分析（2026-05-18）\n\n24 条 unified F1 审计记录全部 status=verified，**无 delta > 1pp**（最大 +0.85pp 4B-SciERC）。论文数字不需紧急修改，但应统一使用 unified 值。\n\n### Canonical 数值清单（论文关键位置）\n\n**主实验（Qwen3-8B SciERC, 3 seeds）：**\n- seed42: greedy=0.6439, oracle=0.7758, headroom=13.19pp, degen=17.77%\n- seed123: greedy=0.6442, oracle=0.8172, headroom=17.30pp, degen=17.2%\n- seed456: greedy=0.6439, oracle=0.8229, headroom=17.90pp, degen=20.42%\n\n**主实验（Qwen3-8B CoNLL, 3 seeds）：**\n- seed42: greedy=0.9070, oracle=0.9581, headroom=5.11pp, degen=48.44%\n- seed123: greedy=0.9065, oracle=0.9586, headroom=5.21pp, degen=47.10%\n- seed456: greedy=0.9071, oracle=0.9567, headroom=4.96pp, degen=55.44%\n\n**主实验（Qwen3-8B FewNERD, 4 seeds）：**\n- seed42: greedy=0.7478, oracle=0.8719, headroom=12.41pp, degen=13.75%\n- seed123: greedy=0.7483, oracle=0.8768, headroom=12.85pp, degen=13.1%\n- seed456: greedy=0.7484, oracle=0.8755, headroom=12.71pp, degen=12.1%\n- seed789: greedy=0.7478, oracle=0.8714, headroom=12.37pp, degen=11.77%\n- **4-seed mean**: greedy=0.7481, oracle=0.8739, LP Δ=+1.38pp [+1.32,+1.44]\n\n**跨模型（LLaMA SciERC, 3 seeds）：**\n- seed42: greedy=0.6460, oracle=0.7748, headroom=12.88pp, degen=24.95%\n- seed123: greedy=0.6454, oracle=0.7657, headroom=12.03pp, degen=26.65%\n- seed456: greedy=0.6459, oracle=0.7631, headroom=11.72pp, degen=27.41%\n\n**跨模型（LLaMA CoNLL, 3 seeds）：**\n- seed42: greedy=0.9239, oracle=0.9482, headroom=2.43pp, degen=86.47%\n- seed123: greedy=0.9238, oracle=0.9494, headroom=2.56pp, degen=86.36%\n- seed456: greedy=0.9242, oracle=0.9488, headroom=2.46pp, degen=86.72%\n\n**跨模型（LLaMA FewNERD, 3 seeds）：**\n- seed42: greedy=0.7841, oracle=0.8854, headroom=10.13pp, degen=27.32%\n- seed123: greedy=0.7840, oracle=0.8839, headroom=9.99pp, degen=24.63%\n- seed456: greedy=0.7844, oracle=0.8835, headroom=9.91pp, degen=18.13%\n- **3-seed mean**: greedy=0.7842, oracle=0.8843, LP Δ=+0.36pp, DGS=-0.35pp\n\n**模型规模（Qwen3-4B）：**\n- SciERC: greedy=0.6622, oracle=0.7925, headroom=13.03pp, degen=10.4%\n- CoNLL: greedy=0.9236, oracle=0.9394, headroom=1.58pp, degen=90.57%\n\n**温度消融（SciERC）：**\n- T=0.5: oracle=0.7395, headroom=9.05pp, degen=41.4%\n- T=0.8: oracle=0.7690, headroom=12.51pp, degen=23.82%\n- T=1.2: oracle=0.7888, headroom=14.63pp, degen=14.93%\n\n**采样数消融：** N=16 seed42: oracle=0.8194 (degen=12.10%), N=32: oracle=0.8396 (degen=7.18%)\n\n**训练消融：** 3-epoch: oracle=0.7998 (degen=6.4%), 10-epoch: oracle=0.7331 (degen=47.8%), rank=8: oracle=0.7998 (degen=7.18%)\n\n### 退化率缺口：已全部补齐 ✅\nrank=8: 7.18%, N=32: 7.18%, N=16 s42: 12.10%, FewNERD N=8 s42: 13.75%\n\n## Entity Construction 公平评估（2026-05-19）\n\n原版 entity_construction.py 在 test set 上 sweep θ，导致对比不公平（greedy/LP selection 无此优势）。修正为 5-fold CV + bootstrap B=10000。\n\n关键方法学决策：\n- **θ=2/N（uniform threshold）是正确选择**：θ=0.5 majority vote 过于保守，在 CoNLL (-0.66pp) 和 FewNERD (-2.89pp) 反而降低 F1\n- **🔴 Adaptive combination 已作废**（2026-05-19 审计）：per-instance 门控信号 `compute_lp_alignment` 使用 gold F1 计算 spearman(LP, gold_F1)，属于 gold label 泄漏。+4-5pp 结果不能写入论文\n- **CoNLL construction 不显著**（+0.10pp, p=0.303）：高退化率（~50%）可能抑制 construction 增益，因为过半实例的 N 个样本产出相同实体集，construction 无新实体可聚合\n- **RE 任务 borderline**（+1.69pp, p=0.049）：可 claim \"marginally significant\"，但需谨慎措辞\n- **N=8 也显著**：SciERC LP-weighted confirm +1.67pp (p=0.004)，FewNERD LP-weighted CV +0.88pp (p=0.000)。Construction 在主实验设置下已有效\n\n## Gating Protocol Bootstrap CI（2026-05-19, R24-N2 加固）\n\nDev set LP-alignment gating protocol bootstrap 分析（B=1000），数据来自 output/dev_set_lp_probe/。\n\n**Bootstrap 95% CI（adjusted score = mean_rho × valid_ratio）：**\n\n| 数据集 | mean_ρ | CI(ρ) | adjusted | CI(adj) | valid% | degen% | routing |\n|--------|--------|-------|----------|---------|--------|--------|---------|\n| SciERC | 0.214 | [0.146, 0.281] | 0.167 | [0.116, 0.220] | 78.2% | 21.8% | greedy |\n| CoNLL | 0.294 | [-0.061, 0.620] | 0.065 | [-0.009, 0.156] | 22.0% | 78.0% | greedy |\n| FewNERD | 0.615 | [0.459, 0.759] | 0.516 | [0.374, 0.648] | 84.0% | 16.0% | LP |\n\n**Threshold 敏感性（routing decisions 在 τ∈[0.2, 0.4] 全范围内一致）：**\n- Robust range（all datasets stability ≥ 95%）：**τ ∈ [0.25, 0.35]**，选定 τ=0.3 位于中心\n- τ=0.2 时 SciERC 不稳定（87.8%），τ=0.4 时 FewNERD 略降（93.7%）\n\n**Greedy fallback 分析：**\n- CoNLL 78% degeneracy → construction 无效（样本几乎相同）→ greedy 是正确 fallback\n- SciERC 33% negative ρ among valid instances → LP selection 不可靠 → greedy justified\n- FewNERD 仅 14.3% negative ρ，16% degeneracy → LP well-justified\n\n**关键结论**：gating protocol 在 bootstrap 下高度稳定，τ=0.3 选择 robust，routing decisions 不随 threshold 变化。CoNLL 的 greedy fallback 由极高退化率驱动。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_gating_bootstrap_ci_20260519T101033",
  "tool": "mcp__agent-ml-research__save_project_file",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "file": "memory.md",
    "content": "## SciERC-Qwen4B 论文 Framing 决策（2026-05-18, Director 指令）\n\nSciERC-Qwen4B (degen=10.4%, ρ=0.189, LP delta=-2.23pp) **不是** Two-Condition 框架的反例。ρ=0.189 属于 weak alignment，Two-Condition Theory 预测在 weak alignment 下 LP selection 无效，这是预期失败。论文不要 frame 成 counterexample，而是作为 weak alignment 的 expected negative case。\n\n## 🔴 退化率定义修正（2026-05-18, CRITICAL）\n\n旧 report.json 中的 \"degen_rate\" 实际是 `sample_f1_pct_zero`（样本级 F1=0 百分比），**不是**退化率（实例级 constant-F1 gold-filtered）。两者数值差异巨大：\n\n| 数据集 | 旧值(sample_f1_pct_zero) | 真实退化率(unified) | 差距 |\n|--------|--------------------------|---------------------|------|\n| Qwen CoNLL s42 | 7.6% | 48.4% | +40.9pp |\n| LLaMA CoNLL s42 | 4.3% | 86.5% | +82.2pp |\n| SciERC T=0.5 | 10.3% | 41.4% | +31.1pp |\n| Qwen SciERC s42 | 12.6% | 17.8% | +5.2pp |\n\n关键影响：\n1. CoNLL 是高退化率数据集（~48-55% Qwen, ~86% LLaMA），不是低退化率\n2. T 消融趋势正确方向：T=0.5(41.4%) > T=0.8(23.8%) > T=1.0(17.8%) > T=1.2(14.9%)，退化率随温度升高单调下降\n3. **所有论文引用的退化率必须来自 unified_metrics.compute_degeneracy()，禁止从旧 report.json 取值**\n\n## FewNERD unified 退化率（2026-05-18, 4-seed 最终版）\n\n4-seed 统计（unified_metrics.compute_degeneracy, N=8, 32565 gold-filtered inst）：\n- seed=42: **13.75%**, seed=123: **13.1%**, seed=456: **12.1%**, seed=789: **11.77%**\n- 4-seed mean: **12.69%** [95% CI: 11.24%, 14.14%]\n- LP Δ: +1.36/+1.44/+1.37/+1.36pp, mean=**+1.38pp** [95% CI: +1.32, +1.44]\n- Greedy F1: 0.7481 [0.7475, 0.7487], Oracle F1: 0.8739 [0.8695, 0.8783]\n- DGS: seed789 +1.43pp vs greedy\n\n历史错误值：10.13%（旧 full_signal_analysis.json 用未迁移脚本生成），7.06%（exp_027 N=16 子集）。\n\nmulti-seed 对比统一用 exp_021_inference (N=8, 全集 37648→32565 gold-filtered)，不用 exp_027_fewnerd_n16 (N=16, 5000→4351 子集)。\n\n## Epoch DGS 分析结果（2026-05-18）\n\nSciERC 不同 epoch/rank 下退化率与 DGS 增益的关系（已用 unified_metrics 验证）：\n\n| 设置 | 退化率 | Greedy | DGS | DGS-Greedy | Oracle Headroom |\n|------|--------|--------|-----|------------|-----------------|\n| 3-epoch | 6.4% | 0.6501 | 0.6383 | -1.18pp n.s. | 14.97pp |\n| 5-epoch | 17.8% | 0.6439 | 0.6513 | +0.74pp n.s. | 13.19pp |\n| 10-epoch | 47.8% | 0.6467 | 0.6567 | +0.99pp sig | 8.64pp |\n| rank=8 | 7.2% | 0.6397 | 0.6350 | -0.47pp n.s. | 16.01pp |\n\n## Oracle F1 聚合方式差异（2026-05-18）\n\n旧 `run_mvp_pilot.py` 用 corpus-level micro-averaged F1（先聚合 TP/FP/FN 再算 F1），unified_metrics 用 per-instance F1（逐实例算 F1 后取均值）。论文统一用 per-instance F1。\n\n## 统一 F1 修复（2026-05-18）\n\nF1 不一致的根因：DGS 脚本指向旧数据路径 exp001_n16_seed42（应为 exp_012_rerun_1024），adaptive_temperature 用了不同数据源 + structural-identity 退化定义。已通过 unified_metrics.py 统一修复。修复后 DGS 正确数字：SciERC +0.74pp, FewNERD +1.37pp, CoNLL -0.81pp。\n\n## Feature Bottleneck 结论（2026-05-18）\n\n5 个 confidence signal 的判别力天花板限制了所有 selection 方法。MLP/RF 无法超越 LR 或 greedy。CCS（级联选择）、Entity Consensus、Adaptive Temperature 均为 negative。这支持 diagnostic（而非 prescriptive method）的论文 framing。\n\n## 跨模型验证（2026-05-18, 更新 2026-05-19）\n\nLLaMA-3.1-8B 在 SciERC（3 seeds）和 CoNLL 上确认：structural signal（SJ/FK/VC/EM）ρ >> LP ρ，与 Qwen 一致。\n\n**LLaMA FewNERD（2026-05-19, 3 seeds）**：pattern 不同——LP 是唯一正向 selection signal (+0.36pp)，所有 structural signals 负向（SJ -0.52, FK -0.53, EM -1.02, VC -2.39）。degeneracy 23.36%（远高于 Qwen 12.69%）。推测原因：LLaMA 在 T=1.0 产出更多 degenerate sets，structural signals 被 noise 淹没。LP robustness 跨模型一致（Qwen 和 LLaMA 上均为正向信号）。\n\n## F1 审计表分析（2026-05-18）\n\n24 条 unified F1 审计记录全部 status=verified，**无 delta > 1pp**（最大 +0.85pp 4B-SciERC）。论文数字不需紧急修改，但应统一使用 unified 值。\n\n### Canonical 数值清单（论文关键位置）\n\n**主实验（Qwen3-8B SciERC, 3 seeds）：**\n- seed42: greedy=0.6439, oracle=0.7758, headroom=13.19pp, degen=17.77%\n- seed123: greedy=0.6442, oracle=0.8172, headroom=17.30pp, degen=17.2%\n- seed456: greedy=0.6439, oracle=0.8229, headroom=17.90pp, degen=20.42%\n\n**主实验（Qwen3-8B CoNLL, 3 seeds）：**\n- seed42: greedy=0.9070, oracle=0.9581, headroom=5.11pp, degen=48.44%\n- seed123: greedy=0.9065, oracle=0.9586, headroom=5.21pp, degen=47.10%\n- seed456: greedy=0.9071, oracle=0.9567, headroom=4.96pp, degen=55.44%\n\n**主实验（Qwen3-8B FewNERD, 4 seeds）：**\n- seed42: greedy=0.7478, oracle=0.8719, headroom=12.41pp, degen=13.75%\n- seed123: greedy=0.7483, oracle=0.8768, headroom=12.85pp, degen=13.1%\n- seed456: greedy=0.7484, oracle=0.8755, headroom=12.71pp, degen=12.1%\n- seed789: greedy=0.7478, oracle=0.8714, headroom=12.37pp, degen=11.77%\n- **4-seed mean**: greedy=0.7481, oracle=0.8739, LP Δ=+1.38pp [+1.32,+1.44]\n\n**跨模型（LLaMA SciERC, 3 seeds）：**\n- seed42: greedy=0.6460, oracle=0.7748, headroom=12.88pp, degen=24.95%\n- seed123: greedy=0.6454, oracle=0.7657, headroom=12.03pp, degen=26.65%\n- seed456: greedy=0.6459, oracle=0.7631, headroom=11.72pp, degen=27.41%\n\n**跨模型（LLaMA CoNLL, 3 seeds）：**\n- seed42: greedy=0.9239, oracle=0.9482, headroom=2.43pp, degen=86.47%\n- seed123: greedy=0.9238, oracle=0.9494, headroom=2.56pp, degen=86.36%\n- seed456: greedy=0.9242, oracle=0.9488, headroom=2.46pp, degen=86.72%\n\n**跨模型（LLaMA FewNERD, 3 seeds）：**\n- seed42: greedy=0.7841, oracle=0.8854, headroom=10.13pp, degen=27.32%\n- seed123: greedy=0.7840, oracle=0.8839, headroom=9.99pp, degen=24.63%\n- seed456: greedy=0.7844, oracle=0.8835, headroom=9.91pp, degen=18.13%\n- **3-seed mean**: greedy=0.7842, oracle=0.8843, LP Δ=+0.36pp, DGS=-0.35pp\n\n**模型规模（Qwen3-4B）：**\n- SciERC: greedy=0.6622, oracle=0.7925, headroom=13.03pp, degen=10.4%\n- CoNLL: greedy=0.9236, oracle=0.9394, headroom=1.58pp, degen=90.57%\n\n**温度消融（SciERC）：**\n- T=0.5: oracle=0.7395, headroom=9.05pp, degen=41.4%\n- T=0.8: oracle=0.7690, headroom=12.51pp, degen=23.82%\n- T=1.2: oracle=0.7888, headroom=14.63pp, degen=14.93%\n\n**采样数消融：** N=16 seed42: oracle=0.8194 (degen=12.10%), N=32: oracle=0.8396 (degen=7.18%)\n\n**训练消融：** 3-epoch: oracle=0.7998 (degen=6.4%), 10-epoch: oracle=0.7331 (degen=47.8%), rank=8: oracle=0.7998 (degen=7.18%)\n\n### 退化率缺口：已全部补齐 ✅\nrank=8: 7.18%, N=32: 7.18%, N=16 s42: 12.10%, FewNERD N=8 s42: 13.75%\n\n## Entity Construction 公平评估（2026-05-19）\n\n原版 entity_construction.py 在 test set 上 sweep θ，导致对比不公平（greedy/LP selection 无此优势）。修正为 5-fold CV + bootstrap B=10000。\n\n关键方法学决策：\n- **θ=2/N（uniform threshold）是正确选择**：θ=0.5 majority vote 过于保守，在 CoNLL (-0.66pp) 和 FewNERD (-2.89pp) 反而降低 F1\n- **🔴 Adaptive combination 已作废**（2026-05-19 审计）：per-instance 门控信号 `compute_lp_alignment` 使用 gold F1 计算 spearman(LP, gold_F1)，属于 gold label 泄漏。+4-5pp 结果不能写入论文\n- **CoNLL construction 不显著**（+0.10pp, p=0.303）：高退化率（~50%）可能抑制 construction 增益，因为过半实例的 N 个样本产出相同实体集，construction 无新实体可聚合\n- **RE 任务 borderline**（+1.69pp, p=0.049）：可 claim \"marginally significant\"，但需谨慎措辞\n- **N=8 也显著**：SciERC LP-weighted confirm +1.67pp (p=0.004)，FewNERD LP-weighted CV +0.88pp (p=0.000)。Construction 在主实验设置下已有效\n\n## Gating Protocol Bootstrap CI（2026-05-19, R24-N2 加固）\n\nDev set LP-alignment gating protocol bootstrap 分析（B=1000），数据来自 output/dev_set_lp_probe/。\n\n**Bootstrap 95% CI（adjusted score = mean_rho × valid_ratio）：**\n\n| 数据集 | mean_ρ | CI(ρ) | adjusted | CI(adj) | valid% | degen% | routing |\n|--------|--------|-------|----------|---------|--------|--------|---------|\n| SciERC | 0.214 | [0.146, 0.281] | 0.167 | [0.116, 0.220] | 78.2% | 21.8% | greedy |\n| CoNLL | 0.294 | [-0.061, 0.620] | 0.065 | [-0.009, 0.156] | 22.0% | 78.0% | greedy |\n| FewNERD | 0.615 | [0.459, 0.759] | 0.516 | [0.374, 0.648] | 84.0% | 16.0% | LP |\n\n**Threshold 敏感性（routing decisions 在 τ∈[0.2, 0.4] 全范围内一致）：**\n- Robust range（all datasets stability ≥ 95%）：**τ ∈ [0.25, 0.35]**，选定 τ=0.3 位于中心\n- τ=0.2 时 SciERC 不稳定（87.8%），τ=0.4 时 FewNERD 略降（93.7%）\n\n**Greedy fallback 分析：**\n- CoNLL 78% degeneracy → construction 无效（样本几乎相同）→ greedy 是正确 fallback\n- SciERC 33% negative ρ among valid instances → LP selection 不可靠 → greedy justified\n- FewNERD 仅 14.3% negative ρ，16% degeneracy → LP well-justified\n\n**关键结论**：gating protocol 在 bootstrap 下高度稳定，τ=0.3 选择 robust，routing decisions 不随 threshold 变化。CoNLL 的 greedy fallback 由极高退化率驱动。"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-19T10:14:26.403904+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/memory.md\", \"saved\": true}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_gating_bootstrap_ci_20260519T101033",
  "tool": "mcp__agent-ml-research__save_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 47 · 2026-05-19T10:14:26.404073+00:00_

全部完成。结果汇总：

### Bootstrap CI (B=1000)

| 数据集 | mean ρ | 95% CI(ρ) | adjusted | 95% CI(adj) | routing |
|--------|--------|-----------|----------|-------------|---------|
| SciERC | 0.214 | [0.146, 0.281] | 0.167 | [0.116, 0.220] | **greedy** |
| CoNLL | 0.294 | [-0.061, 0.620] | 0.065 | [-0.009, 0.156] | **greedy** |
| FewNERD | 0.615 | [0.459, 0.759] | 0.516 | [0.374, 0.648] | **LP** |

### Threshold 敏感性
- Routing decisions 在 **τ∈[0.2, 0.4] 全范围一致**（SciERC/CoNLL 始终 greedy，FewNERD 始终 LP）
- Robust range（all stability ≥ 95%）：**τ ∈ [0.25, 0.35]**，τ=0.3 正好居中

### Greedy Fallback
- CoNLL 78% degeneracy → 样本几乎相同，construction 无新实体可聚合 → greedy 是唯一合理选择
- SciERC 33% negative ρ → LP 不可靠
- FewNERD 仅 14.3% negative ρ，16% degeneracy → LP well-justified

结果保存在 `output/gating_bootstrap/gating_analysis.json`（服务器端）和 artifact `gating_bootstrap_analysis`，memory.md 已更新。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_gating_bootstrap_ci_20260519T101033"
}
```

</details>

---
