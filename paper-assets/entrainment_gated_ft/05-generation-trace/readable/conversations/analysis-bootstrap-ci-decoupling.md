# analysis bootstrap ci decoupling

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 21
- **Recorded user turns:** 0
- **Tool calls:** 10
- **Original source:** `logs/chats/worker_analysis_bootstrap-ci-decoupling_20260520T011928.jsonl`
- **Structured JSON:** [`41f64ea7b8f278c8f383.json`](../../sessions/41/41f64ea7b8f278c8f383.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

21 recorded events

### Tool call

_source line 1 · 2026-05-20T01:23:53.156620+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bootstrap-ci-decoupling_20260520T011928",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-20T01:23:53.157021+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bootstrap-ci-decoupling_20260520T011928",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-20T01:23:53.157194+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-48145",
  "command": "find /root/entrainment_gated_ft/lm_eval_clean/ -path \"*1.3b*\" -name \"*lambada*jsonl\" 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bootstrap-ci-decoupling_20260520T011928",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-48145",
    "command": "find /root/entrainment_gated_ft/lm_eval_clean/ -path \"*1.3b*\" -name \"*lambada*jsonl\" 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-20T01:23:53.157335+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bootstrap-ci-decoupling_20260520T011928",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-20T01:23:53.157467+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-48145",
  "command": "find /root/entrainment_gated_ft/lm_eval_clean/ -path \"*1.3b*\" -name \"*lambada*jsonl\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bootstrap-ci-decoupling_20260520T011928",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-48145",
    "command": "find /root/entrainment_gated_ft/lm_eval_clean/ -path \"*1.3b*\" -name \"*lambada*jsonl\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-20T01:23:53.157610+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/entrainment_gated_ft/lm_eval_clean/1.3b/GDN-h3-1-logsamples/samples/lambada_openai.jsonl\\n/root/entrainment_gated_ft/lm_eval_clean/1.3b/GDN-h24-1-logsamples/samples/lambada_openai.jsonl\\n/root/entrainment_gated_ft/lm_eval_clean/1.3b/GDN-h6-1-logsamples/samples/lambada_openai.jsonl\\n/root/entrainment_gated_ft/lm_eval_clean/exp007/1.3b/GDN-pure/samples/lambada_openai.jsonl\\n/root/entrainment_gated_ft/lm_eval_clean/exp007/1.3b/GDN-h12-1/samples/lambada_openai.jsonl\\n/root/entrainment_gated_ft/lm_eval_clean/exp007/1.3b/RetNet-h3-1/samples/lambada_openai.jsonl\\n/root/entrainment_gated_ft/lm_eval_clean/exp007/1.3b/RetNet-h6-1/samples/lambada_openai.jsonl\\n/root/entrainment_gated_ft/lm_eval_clean/exp007/1.3b/RetNet-h12-1/samples/lambada_openai.jsonl\\n/root/entrainment_gated_ft/lm_eval_clean/exp007/1.3b/RetNet-h24-1/samples/lambada_openai.jsonl\\n/root/entrainment_gated_ft/lm_eval_clean/exp007/1.3b/HGRN2-pure/samples/lambada_openai.jsonl\\n/root/entrainment_gated_ft/lm_eval_clean/exp007/1.3b/HGRN2-h3-1/samples/lambada_openai.jsonl\\n/root/entrainment_gated_ft/lm_eval_clean/exp007/1.3b/HGRN2-h6-1/samples/lambada_openai.jsonl\\n/root/entrainment_gated_ft/lm_eval_clean/exp007/1.3b/HGRN2-h12-1/samples/lambada_openai.jsonl\\n/root/entrainment_gated_ft/lm_eval_clean/exp007/1.3b/HGRN2-h24-1/samples/lambada_openai.jsonl\\n/root/entrainment_gated_ft/lm_eval_clean/exp007/1.3b/RetNet-pure/samples/lambada_openai.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.26}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bootstrap-ci-decoupling_20260520T011928",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-20T01:23:53.157820+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-48145",
  "command": "head -2 /root/entrainment_gated_ft/lm_eval_clean/exp007/1.3b/GDN-pure/samples/lambada_openai.jsonl",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bootstrap-ci-decoupling_20260520T011928",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-48145",
    "command": "head -2 /root/entrainment_gated_ft/lm_eval_clean/exp007/1.3b/GDN-pure/samples/lambada_openai.jsonl",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-20T01:23:53.158003+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\\"doc_id\\\": 0, \\\"doc\\\": {\\\"text\\\": \\\"In my palm is a clear stone, and inside it is a small ivory statuette. A guardian angel.\\\\n\\\\n\\\\\\\"Figured if you're going to be out at night getting hit by cars, you might as well have some backup.\\\\\\\"\\\\n\\\\nI look at him, feeling stunned. Like this is some sort of sign. But as I stare at Harlin, his mouth curved in a confident grin, I don't care about signs\\\"}, \\\"target\\\": \\\" signs\\\", \\\"arguments\\\": [[\\\"In my palm is a clear stone, and inside it is a small ivory statuette. A guardian angel.\\\\n\\\\n\\\\\\\"Figured if you're going to be out at night getting hit by cars, you might as well have some backup.\\\\\\\"\\\\n\\\\nI look at him, feeling stunned. Like this is some sort of sign. But as I stare at Harlin, his mouth curved in a confident grin, I don't care about\\\", \\\" signs\\\"]], \\\"resps\\\": [[[-1.828125, false]]], \\\"filtered_resps\\\": [[-1.828125, false]], \\\"filter\\\": \\\"none\\\", \\\"metrics\\\": [\\\"perplexity\\\", \\\"acc\\\"], \\\"doc_hash\\\": \\\"d5d2ee0c7bb2325b1a3b782dd2f946222c370109812c56acc7da70b662a6a60c\\\", \\\"prompt_hash\\\": \\\"8d638394e95544a75ea75bfa8cedd5fb71d5e65dfac9758cad35a0d5fa6e296c\\\", \\\"target_hash\\\": \\\"697dfd086e17614160f34474ccf8681ad12ae5839865fc979ac177eb5bba0a48\\\", \\\"perplexity\\\": -1.828125, \\\"acc\\\": 0}\\n{\\\"doc_id\\\": 1, \\\"doc\\\": {\\\"text\\\": \\\"Give me a minute to change and I'll meet you at the docks.\\\\\\\" She'd forced those words through her teeth.\\\\n\\\\n\\\\\\\"No need to change. We won't be that long.\\\\\\\"\\\\n\\\\nShane gripped her arm and started leading her to the dock.\\\\n\\\\n\\\\\\\"I can make it there on my own, Shane\\\"}, \\\"target\\\": \\\" Shane\\\", \\\"arguments\\\": [[\\\"Give me a minute to change and I'll meet you at the docks.\\\\\\\" She'd forced those words through her teeth.\\\\n\\\\n\\\\\\\"No need to change. 
…[truncated 775 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bootstrap-ci-decoupling_20260520T011928",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-20T01:23:53.158224+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-48145",
  "command": "wc -l /root/entrainment_gated_ft/lm_eval_clean/exp007/1.3b/GDN-pure/samples/lambada_openai.jsonl",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bootstrap-ci-decoupling_20260520T011928",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-48145",
    "command": "wc -l /root/entrainment_gated_ft/lm_eval_clean/exp007/1.3b/GDN-pure/samples/lambada_openai.jsonl",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-20T01:23:53.158370+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"5153 /root/entrainment_gated_ft/lm_eval_clean/exp007/1.3b/GDN-pure/samples/lambada_openai.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.34}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bootstrap-ci-decoupling_20260520T011928",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-20T01:23:53.158515+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__save_project_file",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bootstrap-ci-decoupling_20260520T011928",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__save_project_file",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-20T01:23:53.158654+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bootstrap-ci-decoupling_20260520T011928",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-20T01:23:53.159077+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westb-48145",
  "command": "cat << 'SCRIPTEOF' > /root/entrainment_gated_ft/bootstrap_ci_decoupling.py\nimport json\nimport numpy as np\nfrom itertools import combinations\nimport time\n\nSEED = 42\nN_BOOTSTRAP = 10000\nN_EXAMPLES = 5153\nARCHS = [\"GDN\", \"RetNet\", \"HGRN2\"]\nRATIOS = [\"pure\", \"h24_1\", \"h12_1\", \"h6_1\", \"h3_1\"]\n\nBASE = \"/root/entrainment_gated_ft/lm_eval_clean\"\nFILES = {\n    (\"GDN\", \"pure\"): f\"{BASE}/exp007/1.3b/GDN-pure/samples/lambada_openai.jsonl\",\n    (\"GDN\", \"h24_1\"): f\"{BASE}/1.3b/GDN-h24-1-logsamples/samples/lambada_openai.jsonl\",\n    (\"GDN\", \"h12_1\"): f\"{BASE}/exp007/1.3b/GDN-h12-1/samples/lambada_openai.jsonl\",\n    (\"GDN\", \"h6_1\"): f\"{BASE}/1.3b/GDN-h6-1-logsamples/samples/lambada_openai.jsonl\",\n    (\"GDN\", \"h3_1\"): f\"{BASE}/1.3b/GDN-h3-1-logsamples/samples/lambada_openai.jsonl\",\n    (\"RetNet\", \"pure\"): f\"{BASE}/exp007/1.3b/RetNet-pure/samples/lambada_openai.jsonl\",\n    (\"RetNet\", \"h24_1\"): f\"{BASE}/exp007/1.3b/RetNet-h24-1/samples/lambada_openai.jsonl\",\n    (\"RetNet\", \"h12_1\"): f\"{BASE}/exp007/1.3b/RetNet-h12-1/samples/lambada_openai.jsonl\",\n    (\"RetNet\", \"h6_1\"): f\"{BASE}/exp007/1.3b/RetNet-h6-1/samples/lambada_openai.jsonl\",\n    (\"RetNet\", \"h3_1\"): f\"{BASE}/exp007/1.3b/RetNet-h3-1/samples/lambada_openai.jsonl\",\n    (\"HGRN2\", \"pure\"): f\"{BASE}/exp007/1.3b/HGRN2-pure/samples/lambada_openai.jsonl\",\n    (\"HGRN2\", \"h24_1\"): f\"{BASE}/exp007/1.3b/HGRN2-h24-1/samples/lambada_openai.jsonl\",\n    (\"HGRN2\", \"h12_1\"): f\"{BASE}/exp007/1.3b/HGRN2-h12-1/samples/lambada_openai.jsonl\",\n    (\"HGRN2\", \"h6_1\"): f\"{BASE}/exp007/1.3b/HGRN2-h6-1/samples/lambada_openai.jsonl\",\n    (\"HGRN2\", \"h3_1\"): f\"{BASE}/exp007/1.3b/HGRN2-h3-1/samples/lambada_openai.jsonl\",\n}\n\n\ndef load_acc(path):\n    acc = np.zeros(N_EXAMPLES, dtype=np.int8)\n    with open(path) as f:\n        for line in f:\n            row = json.loads(line)\n            acc[row[\"doc_id\"]] = int(row[\"acc\"])\n    return acc\n\n\ndef main():\n    t0 = time.time()\n    rng = np.random.default_rng(SEED)\n\n    print(\"Loading data...\")\n    acc_data = {}\n    for arch in ARCHS:\n        acc_data[arch] = {}\n        for ratio in RATIOS:\n            acc_data[arch][ratio] = load_acc(FILES[(arch, ratio)])\n            print(f\"  {arch}-{ratio}: acc={acc_data[arch][ratio].mean():.5f}\")\n\n    print(\"\\n--- Point estimates ---\")\n    sigma_point = {}\n    for ratio in RATIOS:\n        accs = [acc_data[arch][ratio].mean() for arch in ARCHS]\n        sigma_point[ratio] = float(np.std(accs, ddof=0))\n        print(f\"sigma({ratio}) = {sigma_point[ratio]:.5f}  accs={[round(a,5) for a in accs]}\")\n\n    j_helped_point = {}\n    j_hurt_point = {}\n    for ratio in RATIOS[1:]:\n        helped = {}\n        hurt = {}\n        for arch in ARCHS:\n            helped[arch] = (acc_data[arch][ratio] == 1) & (acc_data[arch][\"pure\"] == 0)\n            hurt[arch] = (acc_data[arch][ratio] == 0) & (acc_data[arch][\"pure\"] == 1)\n        j_h, j_r = [], []\n        for a1, a2 in combinations(ARCHS, 2):\n            ih = np.sum(helped[a1] & helped[a2])\n            uh = np.sum(helped[a1] | helped[a2])\n            j_h.append(ih / uh if uh > 0 else 0.0)\n            ir = np.sum(hurt[a1] & hurt[a2])\n            ur = np.sum(hurt[a1] | hurt[a2])\n            j_r.append(ir / ur if ur > 0 else 0.0)\n        j_helped_point[ratio] = float(np.mean(j_h))\n        j_hurt_point[ratio] = float(np.mean(j_r))\n        print(f\"J_helped({ratio}) = {j_helped_point[ratio]:.4f}, J_hurt({ratio}) = {j_hurt_point[ratio]:.4f}\")\n\n    print(f\"\\nBootstrapping {N_BOOTSTRAP} resamples...\")\n    boot_indices = rng.integers(0, N_EXAMPLES, size=(N_BOOTSTRAP, N_EXAMPLES))\n\n    # sigma bootstrap (vectorized)\n    sigma_boot = {}\n    for ratio in RATIOS:\n        mat = np.stack([acc_data[arch][ratio] for arch in ARCHS])  # (3, 5153)\n        boot_samples = mat[:, boot_indices]  # (3, 10000, 5153)\n        boot_means = boot_samples.mean(axis=2)  # (3, 10000)\n        sigma_boot[ratio] = boot_means.std(axis=0, ddof=0)  # (10000,)\n    print(\"  sigma bootstrap done.\")\n\n    # Jaccard bootstrap (vectorized)\n    j_helped_boot = {}\n    j_hurt_boot = {}\n    for ratio in RATIOS[1:]:\n        helped_boot = {}\n        hurt_boot = {}\n        for arch in ARCHS:\n            r_b = acc_data[arch][ratio][boot_indices]  # (10000, 5153)\n            p_b = acc_data[arch][\"pure\"][boot_indices]  # (10000, 5153)\n            helped_boot[arch] = (r_b == 1) & (p_b == 0)\n            hurt_boot[arch] = (r_b == 0) & (p_b == 1)\n\n        jh_pairs, jr_pairs = [], []\n        for a1, a2 in combinations(ARCHS, 2):\n            ih = (helped_boot[a1] & helped_boot[a2]).sum(axis=1).astype(np.float64)\n            uh = (helped_boot[a1] | helped_boot[a2]).sum(axis=1).astype(np.float64)\n            jh_pairs.append(np.where(uh > 0, ih / uh, 0.0))\n            ir = (hurt_boot[a1] & hurt_boot[a2]).sum(axis=1).astype(np.float64)\n            ur = (hurt_boot[a1] | hurt_boot[a2]).sum(axis=1).astype(np.float64)\n            jr_pairs.append(np.where(ur > 0, ir / ur, 0.0))\n\n        j_helped_boot[ratio] = np.mean(jh_pairs, axis=0)\n        j_hurt_boot[ratio] = np.mean(jr_pairs, axis=0)\n        print(f\"  Jaccard bootstrap for {ratio} done.\")\n\n    # Compute CIs\n    results = {\"sigma\": {}, \"J_helped\": {}, \"J_hurt\": {}}\n\n    print(\"\\n=== 95% Bootstrap CIs ===\\n\")\n    print(\"sigma (architecture std):\")\n    for ratio in RATIOS:\n        lo, hi = np.percentile(sigma_boot[ratio], [2.5, 97.5])\n        results[\"sigma\"][ratio] = {\n            \"point\": round(sigma_point[ratio], 5),\n            \"ci_lower\": round(float(lo), 5),\n            \"ci_upper\": round(float(hi), 5),\n        }\n        print(f\"  {ratio:8s}: {sigma_point[ratio]:.5f}  [{lo:.5f}, {hi:.5f}]\")\n\n    print(\"\\nJ_helped (mean pairwise Jaccard):\")\n    for ratio in RATIOS[1:]:\n        lo, hi = np.percentile(j_helped_boot[ratio], [2.5, 97.5])\n        results[\"J_helped\"][ratio] = {\n            \"point\": round(j_helped_point[ratio], 4),\n            \"ci_lower\": round(float(lo), 4),\n            \"ci_upper\": round(float(hi), 4),\n        }\n        print(f\"  {ratio:8s}: {j_helped_point[ratio]:.4f}  [{lo:.4f}, {hi:.4f}]\")\n\n    print(\"\\nJ_hurt (mean pairwise Jaccard):\")\n    for ratio in RATIOS[1:]:\n        lo, hi = np.percentile(j_hurt_boot[ratio], [2.5, 97.5])\n        results[\"J_hurt\"][ratio] = {\n            \"point\": round(j_hurt_point[ratio], 4),\n            \"ci_lower\": round(float(lo), 4),\n            \"ci_upper\": round(float(hi), 4),\n        }\n        print(f\"  {ratio:8s}: {j_hurt_point[ratio]:.4f}  [{lo:.4f}, {hi:.4f}]\")\n\n    # Key finding\n    s_pure = results[\"sigma\"][\"pure\"]\n    s_h3 = results[\"sigma\"][\"h3_1\"]\n    sigma_nonoverlap = s_pure[\"ci_lower\"] > s_h3[\"ci_upper\"] or s_h3[\"ci_lower\"] > s_pure[\"ci_upper\"]\n\n    j_ranges = [(results[\"J_helped\"][r][\"ci_lower\"], results[\"J_helped\"][r][\"ci_upper\"]) for r in RATIOS[1:]]\n    j_all_overlap = all(\n        not (j_ranges[i][0] > j_ranges[j][1] or j_ranges[j][0] > j_ranges[i][1])\n        for i in range(len(j_ranges)) for j in range(i + 1, len(j_ranges))\n    )\n\n    if sigma_nonoverlap and j_all_overlap:\n        finding = \"sigma CIs non-overlapping between pure and h3-1 (true signal) vs J CIs overlapping across ratios (flat) -> supports decoupling\"\n    elif sigma_nonoverlap:\n        finding = \"sigma CIs non-overlapping between pure and h3-1; J CIs partially non-overlapping\"\n    else:\n        finding = \"sigma CIs overlapping between pure and h3-1 -- weaker decoupling evidence\"\n\n    results[\"key_finding\"] = finding\n    print(f\"\\nKey finding: {finding}\")\n    print(f\"Elapsed: {time.time() - t0:.1f}s\")\n\n    with open(\"/root/entrainment_gated_ft/bootstrap_ci_results.json\", \"w\") as f:\n        json.dump(results, f, indent=2)\n    print(\"Saved to bootstrap_ci_results.json\")\n\n\nif __name__ == \"__main__\":\n    main()\nSCRIPTEOF\necho \"Script written.\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bootstrap-ci-decoupling_20260520T011928",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westb-48145",
    "command": "cat << 'SCRIPTEOF' > /root/entrainment_gated_ft/bootstrap_ci_decoupling.py\nimport json\nimport numpy as np\nfrom itertools import combinations\nimport time\n\nSEED = 42\nN_BOOTSTRAP = 10000\nN_EXAMPLES = 5153\nARCHS = [\"GDN\", \"RetNet\", \"HGRN2\"]\nRATIOS = [\"pure\", \"h24_1\", \"h12_1\", \"h6_1\", \"h3_1\"]\n\nBASE = \"/root/entrainment_gated_ft/lm_eval_clean\"\nFILES = {\n    (\"GDN\", \"pure\"): f\"{BASE}/exp007/1.3b/GDN-pure/samples/lambada_openai.jsonl\",\n    (\"GDN\", \"h24_1\"): f\"{BASE}/1.3b/GDN-h24-1-logsamples/samples/lambada_openai.jsonl\",\n    (\"GDN\", \"h12_1\"): f\"{BASE}/exp007/1.3b/GDN-h12-1/samples/lambada_openai.jsonl\",\n    (\"GDN\", \"h6_1\"): f\"{BASE}/1.3b/GDN-h6-1-logsamples/samples/lambada_openai.jsonl\",\n    (\"GDN\", \"h3_1\"): f\"{BASE}/1.3b/GDN-h3-1-logsamples/samples/lambada_openai.jsonl\",\n    (\"RetNet\", \"pure\"): f\"{BASE}/exp007/1.3b/RetNet-pure/samples/lambada_openai.jsonl\",\n    (\"RetNet\", \"h24_1\"): f\"{BASE}/exp007/1.3b/RetNet-h24-1/samples/lambada_openai.jsonl\",\n    (\"RetNet\", \"h12_1\"): f\"{BASE}/exp007/1.3b/RetNet-h12-1/samples/lambada_openai.jsonl\",\n    (\"RetNet\", \"h6_1\"): f\"{BASE}/exp007/1.3b/RetNet-h6-1/samples/lambada_openai.jsonl\",\n    (\"RetNet\", \"h3_1\"): f\"{BASE}/exp007/1.3b/RetNet-h3-1/samples/lambada_openai.jsonl\",\n    (\"HGRN2\", \"pure\"): f\"{BASE}/exp007/1.3b/HGRN2-pure/samples/lambada_openai.jsonl\",\n    (\"HGRN2\", \"h24_1\"): f\"{BASE}/exp007/1.3b/HGRN2-h24-1/samples/lambada_openai.jsonl\",\n    (\"HGRN2\", \"h12_1\"): f\"{BASE}/exp007/1.3b/HGRN2-h12-1/samples/lambada_openai.jsonl\",\n    (\"HGRN2\", \"h6_1\"): f\"{BASE}/exp007/1.3b/HGRN2-h6-1/samples/lambada_openai.jsonl\",\n    (\"HGRN2\", \"h3_1\"): f\"{BASE}/exp007/1.3b/HGRN2-h3-1/samples/lambada_openai.jsonl\",\n}\n\n\ndef load_acc(path):\n    acc = np.zeros(N_EXAMPLES, dtype=np.int8)\n    with open(path) as f:\n        for line in f:\n            row = json.loads(line)\n            acc[row[\"doc_id\"]] = int(row[\"acc\"])\n    return acc\n\n\ndef main():\n    t0 = time.time()\n    rng = np.random.default_rng(SEED)\n\n    print(\"Loading data...\")\n    acc_data = {}\n    for arch in ARCHS:\n        acc_data[arch] = {}\n        for ratio in RATIOS:\n            acc_data[arch][ratio] = load_acc(FILES[(arch, ratio)])\n            print(f\"  {arch}-{ratio}: acc={acc_data[arch][ratio].mean():.5f}\")\n\n    print(\"\\n--- Point estimates ---\")\n    sigma_point = {}\n    for ratio in RATIOS:\n        accs = [acc_data[arch][ratio].mean() for arch in ARCHS]\n        sigma_point[ratio] = float(np.std(accs, ddof=0))\n        print(f\"sigma({ratio}) = {sigma_point[ratio]:.5f}  accs={[round(a,5) for a in accs]}\")\n\n    j_helped_point = {}\n    j_hurt_point = {}\n    for ratio in RATIOS[1:]:\n        helped = {}\n        hurt = {}\n        for arch in ARCHS:\n            helped[arch] = (acc_data[arch][ratio] == 1) & (acc_data[arch][\"pure\"] == 0)\n            hurt[arch] = (acc_data[arch][ratio] == 0) & (acc_data[arch][\"pure\"] == 1)\n        j_h, j_r = [], []\n        for a1, a2 in combinations(ARCHS, 2):\n            ih = np.sum(helped[a1] & helped[a2])\n            uh = np.sum(helped[a1] | helped[a2])\n            j_h.append(ih / uh if uh > 0 else 0.0)\n            ir = np.sum(hurt[a1] & hurt[a2])\n            ur = np.sum(hurt[a1] | hurt[a2])\n            j_r.append(ir / ur if ur > 0 else 0.0)\n        j_helped_point[ratio] = float(np.mean(j_h))\n        j_hurt_point[ratio] = float(np.mean(j_r))\n        print(f\"J_helped({ratio}) = {j_helped_point[ratio]:.4f}, J_hurt({ratio}) = {j_hurt_point[ratio]:.4f}\")\n\n    print(f\"\\nBootstrapping {N_BOOTSTRAP} resamples...\")\n    boot_indices = rng.integers(0, N_EXAMPLES, size=(N_BOOTSTRAP, N_EXAMPLES))\n\n    # sigma bootstrap (vectorized)\n    sigma_boot = {}\n    for ratio in RATIOS:\n        mat = np.stack([acc_data[arch][ratio] for arch in ARCHS])  # (3, 5153)\n        boot_samples = mat[:, boot_indices]  # (3, 10000, 5153)\n        boot_means = boot_samples.mean(axis=2)  # (3, 10000)\n        sigma_boot[ratio] = boot_means.std(axis=0, ddof=0)  # (10000,)\n    print(\"  sigma bootstrap done.\")\n\n    # Jaccard bootstrap (vectorized)\n    j_helped_boot = {}\n    j_hurt_boot = {}\n    for ratio in RATIOS[1:]:\n        helped_boot = {}\n        hurt_boot = {}\n        for arch in ARCHS:\n            r_b = acc_data[arch][ratio][boot_indices]  # (10000, 5153)\n            p_b = acc_data[arch][\"pure\"][boot_indices]  # (10000, 5153)\n            helped_boot[arch] = (r_b == 1) & (p_b == 0)\n            hurt_boot[arch] = (r_b == 0) & (p_b == 1)\n\n        jh_pairs, jr_pairs = [], []\n        for a1, a2 in combinations(ARCHS, 2):\n            ih = (helped_boot[a1] & helped_boot[a2]).sum(axis=1).astype(np.float64)\n            uh = (helped_boot[a1] | helped_boot[a2]).sum(axis=1).astype(np.float64)\n            jh_pairs.append(np.where(uh > 0, ih / uh, 0.0))\n            ir = (hurt_boot[a1] & hurt_boot[a2]).sum(axis=1).astype(np.float64)\n            ur = (hurt_boot[a1] | hurt_boot[a2]).sum(axis=1).astype(np.float64)\n            jr_pairs.append(np.where(ur > 0, ir / ur, 0.0))\n\n        j_helped_boot[ratio] = np.mean(jh_pairs, axis=0)\n        j_hurt_boot[ratio] = np.mean(jr_pairs, axis=0)\n        print(f\"  Jaccard bootstrap for {ratio} done.\")\n\n    # Compute CIs\n    results = {\"sigma\": {}, \"J_helped\": {}, \"J_hurt\": {}}\n\n    print(\"\\n=== 95% Bootstrap CIs ===\\n\")\n    print(\"sigma (architecture std):\")\n    for ratio in RATIOS:\n        lo, hi = np.percentile(sigma_boot[ratio], [2.5, 97.5])\n        results[\"sigma\"][ratio] = {\n            \"point\": round(sigma_point[ratio], 5),\n            \"ci_lower\": round(float(lo), 5),\n            \"ci_upper\": round(float(hi), 5),\n        }\n        print(f\"  {ratio:8s}: {sigma_point[ratio]:.5f}  [{lo:.5f}, {hi:.5f}]\")\n\n    print(\"\\nJ_helped (mean pairwise Jaccard):\")\n    for ratio in RATIOS[1:]:\n        lo, hi = np.percentile(j_helped_boot[ratio], [2.5, 97.5])\n        results[\"J_helped\"][ratio] = {\n            \"point\": round(j_helped_point[ratio], 4),\n            \"ci_lower\": round(float(lo), 4),\n            \"ci_upper\": round(float(hi), 4),\n        }\n        print(f\"  {ratio:8s}: {j_helped_point[ratio]:.4f}  [{lo:.4f}, {hi:.4f}]\")\n\n    print(\"\\nJ_hurt (mean pairwise Jaccard):\")\n    for ratio in RATIOS[1:]:\n        lo, hi = np.percentile(j_hurt_boot[ratio], [2.5, 97.5])\n        results[\"J_hurt\"][ratio] = {\n            \"point\": round(j_hurt_point[ratio], 4),\n            \"ci_lower\": round(float(lo), 4),\n            \"ci_upper\": round(float(hi), 4),\n        }\n        print(f\"  {ratio:8s}: {j_hurt_point[ratio]:.4f}  [{lo:.4f}, {hi:.4f}]\")\n\n    # Key finding\n    s_pure = results[\"sigma\"][\"pure\"]\n    s_h3 = results[\"sigma\"][\"h3_1\"]\n    sigma_nonoverlap = s_pure[\"ci_lower\"] > s_h3[\"ci_upper\"] or s_h3[\"ci_lower\"] > s_pure[\"ci_upper\"]\n\n    j_ranges = [(results[\"J_helped\"][r][\"ci_lower\"], results[\"J_helped\"][r][\"ci_upper\"]) for r in RATIOS[1:]]\n    j_all_overlap = all(\n        not (j_ranges[i][0] > j_ranges[j][1] or j_ranges[j][0] > j_ranges[i][1])\n        for i in range(len(j_ranges)) for j in range(i + 1, len(j_ranges))\n    )\n\n    if sigma_nonoverlap and j_all_overlap:\n        finding = \"sigma CIs non-overlapping between pure and h3-1 (true signal) vs J CIs overlapping across ratios (flat) -> supports decoupling\"\n    elif sigma_nonoverlap:\n        finding = \"sigma CIs non-overlapping between pure and h3-1; J CIs partially non-overlapping\"\n    else:\n        finding = \"sigma CIs overlapping between pure and h3-1 -- weaker decoupling evidence\"\n\n    results[\"key_finding\"] = finding\n    print(f\"\\nKey finding: {finding}\")\n    print(f\"Elapsed: {time.time() - t0:.1f}s\")\n\n    with open(\"/root/entrainment_gated_ft/bootstrap_ci_results.json\", \"w\") as f:\n        json.dump(results, f, indent=2)\n    print(\"Saved to bootstrap_ci_results.json\")\n\n\nif __name__ == \"__main__\":\n    main()\nSCRIPTEOF\necho \"Script written.\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-20T01:23:53.159393+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Script written.\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bootstrap-ci-decoupling_20260520T011928",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-20T01:23:53.159549+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westb-48145",
  "command": "cd /root/entrainment_gated_ft && python3 bootstrap_ci_decoupling.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bootstrap-ci-decoupling_20260520T011928",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westb-48145",
    "command": "cd /root/entrainment_gated_ft && python3 bootstrap_ci_decoupling.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-20T01:23:53.159715+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Encountered a bad command exit code!\\n\\nCommand: 'cd /root/entrainment_gated_ft && python3 bootstrap_ci_decoupling.py'\\n\\nExit code: 127\\n\\nStdout:\\n\\n\\n\\nStderr:\\n\\nbash: line 1: python3: command not found\\n\\n\", \"metadata\": {\"elapsed_seconds\": 1.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bootstrap-ci-decoupling_20260520T011928",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-20T01:23:53.159855+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-48145",
  "command": "ls /root/miniconda3/bin/python3",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bootstrap-ci-decoupling_20260520T011928",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-48145",
    "command": "ls /root/miniconda3/bin/python3",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-20T01:23:53.159983+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/miniconda3/bin/python3\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.31}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bootstrap-ci-decoupling_20260520T011928",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-20T01:23:53.160103+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westb-48145",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/entrainment_gated_ft && python3 bootstrap_ci_decoupling.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bootstrap-ci-decoupling_20260520T011928",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westb-48145",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/entrainment_gated_ft && python3 bootstrap_ci_decoupling.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-20T01:23:53.160257+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Loading data...\\n  GDN-pure: acc=0.54337\\n  GDN-h24_1: acc=0.53988\\n  GDN-h12_1: acc=0.53580\\n  GDN-h6_1: acc=0.50961\\n  GDN-h3_1: acc=0.51329\\n  RetNet-pure: acc=0.51737\\n  RetNet-h24_1: acc=0.51523\\n  RetNet-h12_1: acc=0.50670\\n  RetNet-h6_1: acc=0.49680\\n  RetNet-h3_1: acc=0.50243\\n  HGRN2-pure: acc=0.48399\\n  HGRN2-h24_1: acc=0.49990\\n  HGRN2-h12_1: acc=0.50320\\n  HGRN2-h6_1: acc=0.51116\\n  HGRN2-h3_1: acc=0.51426\\n\\n--- Point estimates ---\\nsigma(pure) = 0.02431  accs=[np.float64(0.54337), np.float64(0.51737), np.float64(0.48399)]\\nsigma(h24_1) = 0.01647  accs=[np.float64(0.53988), np.float64(0.51523), np.float64(0.4999)]\\nsigma(h12_1) = 0.01462  accs=[np.float64(0.5358), np.float64(0.5067), np.float64(0.5032)]\\nsigma(h6_1) = 0.00643  accs=[np.float64(0.50961), np.float64(0.4968), np.float64(0.51116)]\\nsigma(h3_1) = 0.00537  accs=[np.float64(0.51329), np.float64(0.50243), np.float64(0.51426)]\\nJ_helped(h24_1) = 0.0945, J_hurt(h24_1) = 0.0860\\nJ_helped(h12_1) = 0.0954, J_hurt(h12_1) = 0.0775\\nJ_helped(h6_1) = 0.0904, J_hurt(h6_1) = 0.0980\\nJ_helped(h3_1) = 0.0964, J_hurt(h3_1) = 0.0932\\n\\nBootstrapping 10000 resamples...\\n  sigma bootstrap done.\\n  Jaccard bootstrap for h24_1 done.\\n  Jaccard bootstrap for h12_1 done.\\n  Jaccard bootstrap for h6_1 done.\\n  Jaccard bootstrap for h3_1 done.\\n\\n=== 95% Bootstrap CIs ===\\n\\nsigma (architecture std):\\n  pure    : 0.02431  [0.01930, 0.02955]\\n  h24_1   : 0.01647  [0.01162, 0.02172]\\n  h12_1   : 0.01462  [0.00969, 0.02019]\\n  h6_1    : 0.00643  [0.00240, 0.01165]\\n  h3_1    : 0.00537  [0.00180, 0.01057]\\n\\nJ_helped (mean pairwise Jaccard):\\n  h24_1   : 0.0945  [0.0826, 0.1066]\\n  h12_1   : 0.0954  [0.0834, 0.1075]\\n  h6_1    : 0.0904  [0.0790, 0.1023]\\n  h3_1    : 0.0964  [0.0844, 0.1088]\\n\\nJ_hurt (mean pairwise Jaccard):\\n  h24_1   : 0.0860  [0.0745, 0.0978]\\n  h12_1   : 0.0775  [0.0667, 0.0891]\\n  h6_1    : 0
…[truncated 368 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bootstrap-ci-decoupling_20260520T011928",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-20T01:23:53.160478+00:00_

完成。结果汇总：

### σ (architecture std) — 95% Bootstrap CI

| Ratio | Point | 95% CI |
|-------|-------|--------|
| pure | 0.02431 | [0.01930, 0.02955] |
| h24-1 | 0.01647 | [0.01162, 0.02172] |
| h12-1 | 0.01462 | [0.00969, 0.02019] |
| h6-1 | 0.00643 | [0.00240, 0.01165] |
| h3-1 | 0.00537 | [0.00180, 0.01057] |

### J_helped (mean pairwise Jaccard) — 95% CI

| Ratio | Point | 95% CI |
|-------|-------|--------|
| h24-1 | 0.0945 | [0.0826, 0.1066] |
| h12-1 | 0.0954 | [0.0834, 0.1075] |
| h6-1 | 0.0904 | [0.0790, 0.1023] |
| h3-1 | 0.0964 | [0.0844, 0.1088] |

### J_hurt (mean pairwise Jaccard) — 95% CI

| Ratio | Point | 95% CI |
|-------|-------|--------|
| h24-1 | 0.0860 | [0.0745, 0.0978] |
| h12-1 | 0.0775 | [0.0667, 0.0891] |
| h6-1 | 0.0980 | [0.0857, 0.1105] |
| h3-1 | 0.0932 | [0.0814, 0.1057] |

### Key Finding

**σ CIs non-overlapping between pure and h3-1** (pure lower bound 0.01930 > h3-1 upper bound 0.01057) **→ 显著下降**。同时 **J CIs 在所有 ratio 间完全重叠 → Jaccard 保持 flat**。

统计证据支持 decoupling：attention 增加时 accuracy variance 显著收敛，但 example-level 帮助/伤害的架构间 overlap 模式不变。

结果已保存到 `/root/entrainment_gated_ft/bootstrap_ci_results.json`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_bootstrap-ci-decoupling_20260520T011928"
}
```

</details>

---
