# paper n2a downstream bootstrap

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 9
- **Recorded user turns:** 0
- **Tool calls:** 4
- **Original source:** `logs/chats/worker_paper_n2a-downstream-bootstrap_20260516T043728.jsonl`
- **Structured JSON:** [`f5d7dbad1e920cefc030.json`](../../sessions/f5/f5d7dbad1e920cefc030.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

9 recorded events

### Tool call

_source line 1 · 2026-05-16T04:38:31.250728+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/scripts/n2a_bootstrap_ci.py",
  "content": "\"\"\"N2a: Bootstrap CI + effect size for downstream perplexity comparisons.\"\"\"\nimport json\nimport itertools\nimport numpy as np\nfrom pathlib import Path\n\nnp.random.seed(2026)\n\nDATA = {\n    \"size_matched\": [2.367, 2.367, 2.367],\n    \"depth01\": [2.3877, 2.3869, 2.387],\n    \"all\": [2.335, 2.335, 2.3354],\n    \"binary_filtered\": [2.389, 2.389, 2.389],\n    \"depth0_only\": [2.6818, 2.68, 2.6817],\n}\n\nN_BOOT = 10_000\nN_PERM = 10_000\n\n\ndef cohens_d(a, b):\n    na, nb = len(a), len(b)\n    va, vb = np.var(a, ddof=1), np.var(b, ddof=1)\n    pooled_std = np.sqrt(((na - 1) * va + (nb - 1) * vb) / (na + nb - 2))\n    if pooled_std == 0:\n        return float(\"inf\") if np.mean(a) != np.mean(b) else 0.0\n    return (np.mean(a) - np.mean(b)) / pooled_std\n\n\ndef bootstrap_ci(a, b, n_boot=N_BOOT):\n    a, b = np.array(a), np.array(b)\n    obs_diff = np.mean(a) - np.mean(b)\n    diffs = np.empty(n_boot)\n    for i in range(n_boot):\n        sa = a[np.random.randint(0, len(a), len(a))]\n        sb = b[np.random.randint(0, len(b), len(b))]\n        diffs[i] = np.mean(sa) - np.mean(sb)\n    ci_lo, ci_hi = np.percentile(diffs, [2.5, 97.5])\n    return obs_diff, ci_lo, ci_hi, diffs\n\n\ndef permutation_test(a, b, n_perm=N_PERM):\n    a, b = np.array(a), np.array(b)\n    obs_diff = abs(np.mean(a) - np.mean(b))\n    combined = np.concatenate([a, b])\n    n_a = len(a)\n    count = 0\n    for _ in range(n_perm):\n        np.random.shuffle(combined)\n        perm_diff = abs(np.mean(combined[:n_a]) - np.mean(combined[n_a:]))\n        if perm_diff >= obs_diff:\n            count += 1\n    return count / n_perm\n\n\ndef exact_permutation_test(a, b):\n    \"\"\"Exact test enumerating all assignments (feasible for n=3+3=6).\"\"\"\n    a, b = np.array(a), np.array(b)\n    obs_diff = abs(np.mean(a) - np.mean(b))\n    combined = np.concatenate([a, b])\n    n = len(combined)\n    n_a = len(a)\n    count = 0\n    total = 0\n    for idx in itertools.combinations(range(n), n_a):\n        grp_a = combined[list(idx)]\n        perm_diff = abs(np.mean(grp_a) - np.mean(combined) * 2 + np.mean(grp_a))\n        # simpler: recompute\n        rest = np.delete(combined, list(idx))\n        perm_diff = abs(np.mean(grp_a) - np.mean(rest))\n        if perm_diff >= obs_diff - 1e-12:\n            count += 1\n        total += 1\n    return count / total\n\n\ndef compare_pair(name_a, name_b):\n    a, b = DATA[name_a], DATA[name_b]\n    obs_diff, ci_lo, ci_hi, _ = bootstrap_ci(a, b)\n    d = cohens_d(a, b)\n    p_perm = permutation_test(a, b)\n    p_exact = exact_permutation_test(a, b)\n    return {\n        \"group_a\": name_a,\n        \"group_b\": name_b,\n        \"mean_a\": round(float(np.mean(a)), 6),\n        \"mean_b\": round(float(np.mean(b)), 6),\n        \"mean_diff\": round(float(obs_diff), 6),\n        \"bootstrap_95ci\": [round(float(ci_lo), 6), round(float(ci_hi), 6)],\n        \"cohens_d\": round(float(d), 4),\n        \"permutation_p\": round(float(p_perm), 4),\n        \"exact_permutation_p\": round(float(p_exact), 4),\n        \"n_boot\": N_BOOT,\n        \"n_perm\": N_PERM,\n    }\n\n\nresults = {\"primary_comparison\": {}, \"pairwise\": [], \"caveat\": \"\"}\n\n# Primary: size_matched vs depth01\nprimary = compare_pair(\"size_matched\", \"depth01\")\nresults[\"primary_comparison\"] = primary\n\n# All pairwise\nnames = list(DATA.keys())\nfor i in range(len(names)):\n    for j in range(i + 1, len(names)):\n        results[\"pairwise\"].append(compare_pair(names[i], names[j]))\n\nresults[\"caveat\"] = (\n    \"n=3 per group. Bootstrap and permutation tests with such small samples \"\n    \"have limited resolution (exact permutation test has only C(6,3)=20 distinct \"\n    \"assignments, so minimum nonzero p=0.05). Results should be interpreted as \"\n    \"directional evidence, not definitive hypothesis tests.\"\n)\nresults[\"method\"] = {\n    \"bootstrap\": \"nonparametric percentile bootstrap, 10000 resamples\",\n    \"permutation\": \"two-sided permutation test on mean difference, 10000 random + exact enumeration\",\n    \"effect_size\": \"Cohen's d with pooled SD (ddof=1)\",\n}\n\nout_path = Path(\n    \"/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint\"\n    \"/artifacts/n2a_downstream_bootstrap.json\"\n)\nout_path.parent.mkdir(parents=True, exist_ok=True)\nwith open(out_path, \"w\") as f:\n    json.dump(results, f, indent=2)\n\n# Print summary\nprint(\"=== Primary: size_matched vs depth01 ===\")\np = results[\"primary_comparison\"]\nprint(f\"  Mean diff: {p['mean_diff']:.6f} (size_matched - depth01)\")\nprint(f\"  95% CI: [{p['bootstrap_95ci'][0]:.6f}, {p['bootstrap_95ci'][1]:.6f}]\")\nprint(f\"  Cohen's d: {p['cohens_d']:.4f}\")\nprint(f\"  Permutation p: {p['permutation_p']:.4f} (exact: {p['exact_permutation_p']:.4f})\")\n\nprint(f\"\\n=== All {len(results['pairwise'])} pairwise comparisons ===\")\nfor r in results[\"pairwise\"]:\n    print(\n        f\"  {r['group_a']:18s} vs {r['group_b']:18s} | \"\n        f\"diff={r['mean_diff']:+.6f} | d={r['cohens_d']:+.4f} | \"\n        f\"p_exact={r['exact_permutation_p']:.4f}\"\n    )\n\nprint(f\"\\nResults saved to {out_path}\")\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_n2a-downstream-bootstrap_20260516T043728",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/scripts/n2a_bootstrap_ci.py",
    "content": "\"\"\"N2a: Bootstrap CI + effect size for downstream perplexity comparisons.\"\"\"\nimport json\nimport itertools\nimport numpy as np\nfrom pathlib import Path\n\nnp.random.seed(2026)\n\nDATA = {\n    \"size_matched\": [2.367, 2.367, 2.367],\n    \"depth01\": [2.3877, 2.3869, 2.387],\n    \"all\": [2.335, 2.335, 2.3354],\n    \"binary_filtered\": [2.389, 2.389, 2.389],\n    \"depth0_only\": [2.6818, 2.68, 2.6817],\n}\n\nN_BOOT = 10_000\nN_PERM = 10_000\n\n\ndef cohens_d(a, b):\n    na, nb = len(a), len(b)\n    va, vb = np.var(a, ddof=1), np.var(b, ddof=1)\n    pooled_std = np.sqrt(((na - 1) * va + (nb - 1) * vb) / (na + nb - 2))\n    if pooled_std == 0:\n        return float(\"inf\") if np.mean(a) != np.mean(b) else 0.0\n    return (np.mean(a) - np.mean(b)) / pooled_std\n\n\ndef bootstrap_ci(a, b, n_boot=N_BOOT):\n    a, b = np.array(a), np.array(b)\n    obs_diff = np.mean(a) - np.mean(b)\n    diffs = np.empty(n_boot)\n    for i in range(n_boot):\n        sa = a[np.random.randint(0, len(a), len(a))]\n        sb = b[np.random.randint(0, len(b), len(b))]\n        diffs[i] = np.mean(sa) - np.mean(sb)\n    ci_lo, ci_hi = np.percentile(diffs, [2.5, 97.5])\n    return obs_diff, ci_lo, ci_hi, diffs\n\n\ndef permutation_test(a, b, n_perm=N_PERM):\n    a, b = np.array(a), np.array(b)\n    obs_diff = abs(np.mean(a) - np.mean(b))\n    combined = np.concatenate([a, b])\n    n_a = len(a)\n    count = 0\n    for _ in range(n_perm):\n        np.random.shuffle(combined)\n        perm_diff = abs(np.mean(combined[:n_a]) - np.mean(combined[n_a:]))\n        if perm_diff >= obs_diff:\n            count += 1\n    return count / n_perm\n\n\ndef exact_permutation_test(a, b):\n    \"\"\"Exact test enumerating all assignments (feasible for n=3+3=6).\"\"\"\n    a, b = np.array(a), np.array(b)\n    obs_diff = abs(np.mean(a) - np.mean(b))\n    combined = np.concatenate([a, b])\n    n = len(combined)\n    n_a = len(a)\n    count = 0\n    total = 0\n    for idx in itertools.combinations(range(n), n_a):\n        grp_a = combined[list(idx)]\n        perm_diff = abs(np.mean(grp_a) - np.mean(combined) * 2 + np.mean(grp_a))\n        # simpler: recompute\n        rest = np.delete(combined, list(idx))\n        perm_diff = abs(np.mean(grp_a) - np.mean(rest))\n        if perm_diff >= obs_diff - 1e-12:\n            count += 1\n        total += 1\n    return count / total\n\n\ndef compare_pair(name_a, name_b):\n    a, b = DATA[name_a], DATA[name_b]\n    obs_diff, ci_lo, ci_hi, _ = bootstrap_ci(a, b)\n    d = cohens_d(a, b)\n    p_perm = permutation_test(a, b)\n    p_exact = exact_permutation_test(a, b)\n    return {\n        \"group_a\": name_a,\n        \"group_b\": name_b,\n        \"mean_a\": round(float(np.mean(a)), 6),\n        \"mean_b\": round(float(np.mean(b)), 6),\n        \"mean_diff\": round(float(obs_diff), 6),\n        \"bootstrap_95ci\": [round(float(ci_lo), 6), round(float(ci_hi), 6)],\n        \"cohens_d\": round(float(d), 4),\n        \"permutation_p\": round(float(p_perm), 4),\n        \"exact_permutation_p\": round(float(p_exact), 4),\n        \"n_boot\": N_BOOT,\n        \"n_perm\": N_PERM,\n    }\n\n\nresults = {\"primary_comparison\": {}, \"pairwise\": [], \"caveat\": \"\"}\n\n# Primary: size_matched vs depth01\nprimary = compare_pair(\"size_matched\", \"depth01\")\nresults[\"primary_comparison\"] = primary\n\n# All pairwise\nnames = list(DATA.keys())\nfor i in range(len(names)):\n    for j in range(i + 1, len(names)):\n        results[\"pairwise\"].append(compare_pair(names[i], names[j]))\n\nresults[\"caveat\"] = (\n    \"n=3 per group. Bootstrap and permutation tests with such small samples \"\n    \"have limited resolution (exact permutation test has only C(6,3)=20 distinct \"\n    \"assignments, so minimum nonzero p=0.05). Results should be interpreted as \"\n    \"directional evidence, not definitive hypothesis tests.\"\n)\nresults[\"method\"] = {\n    \"bootstrap\": \"nonparametric percentile bootstrap, 10000 resamples\",\n    \"permutation\": \"two-sided permutation test on mean difference, 10000 random + exact enumeration\",\n    \"effect_size\": \"Cohen's d with pooled SD (ddof=1)\",\n}\n\nout_path = Path(\n    \"/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint\"\n    \"/artifacts/n2a_downstream_bootstrap.json\"\n)\nout_path.parent.mkdir(parents=True, exist_ok=True)\nwith open(out_path, \"w\") as f:\n    json.dump(results, f, indent=2)\n\n# Print summary\nprint(\"=== Primary: size_matched vs depth01 ===\")\np = results[\"primary_comparison\"]\nprint(f\"  Mean diff: {p['mean_diff']:.6f} (size_matched - depth01)\")\nprint(f\"  95% CI: [{p['bootstrap_95ci'][0]:.6f}, {p['bootstrap_95ci'][1]:.6f}]\")\nprint(f\"  Cohen's d: {p['cohens_d']:.4f}\")\nprint(f\"  Permutation p: {p['permutation_p']:.4f} (exact: {p['exact_permutation_p']:.4f})\")\n\nprint(f\"\\n=== All {len(results['pairwise'])} pairwise comparisons ===\")\nfor r in results[\"pairwise\"]:\n    print(\n        f\"  {r['group_a']:18s} vs {r['group_b']:18s} | \"\n        f\"diff={r['mean_diff']:+.6f} | d={r['cohens_d']:+.4f} | \"\n        f\"p_exact={r['exact_permutation_p']:.4f}\"\n    )\n\nprint(f\"\\nResults saved to {out_path}\")\n"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-16T04:38:31.251108+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/scripts/n2a_bootstrap_ci.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_n2a-downstream-bootstrap_20260516T043728",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-16T04:38:31.251286+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 scripts/n2a_bootstrap_ci.py",
  "description": "Run bootstrap CI + effect size analysis"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_n2a-downstream-bootstrap_20260516T043728",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 scripts/n2a_bootstrap_ci.py",
    "description": "Run bootstrap CI + effect size analysis"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-16T04:38:31.251438+00:00_

=== Primary: size_matched vs depth01 ===
  Mean diff: -0.020200 (size_matched - depth01)
  95% CI: [-0.020700, -0.019900]
  Cohen's d: -65.5375
  Permutation p: 0.0990 (exact: 0.1000)

=== All 10 pairwise comparisons ===
  size_matched       vs depth01            | diff=-0.020200 | d=-65.5375 | p_exact=0.1000
  size_matched       vs all                | diff=+0.031867 | d=+195.1427 | p_exact=0.1000
  size_matched       vs binary_filtered    | diff=-0.022000 | d=+inf | p_exact=0.1000
  size_matched       vs depth0_only        | diff=-0.314167 | d=-439.2043 | p_exact=0.1000
  depth01            vs all                | diff=+0.052067 | d=+149.2705 | p_exact=0.1000
  depth01            vs binary_filtered    | diff=-0.001800 | d=-5.8400 | p_exact=0.1000
  depth01            vs depth0_only        | diff=-0.293967 | d=-377.4184 | p_exact=0.1000
  all                vs binary_filtered    | diff=-0.053867 | d=-329.8646 | p_exact=0.1000
  all                vs depth0_only        | diff=-0.346033 | d=-471.6201 | p_exact=0.1000
  binary_filtered    vs depth0_only        | diff=-0.292167 | d=-408.4483 | p_exact=0.1000

Results saved to /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/n2a_downstream_bootstrap.json

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_n2a-downstream-bootstrap_20260516T043728",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-16T04:38:31.251611+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__register_artifact",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_n2a-downstream-bootstrap_20260516T043728",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__register_artifact",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-16T04:38:31.251753+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_n2a-downstream-bootstrap_20260516T043728",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-16T04:38:31.251870+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "n2a_downstream_bootstrap",
  "type": "data",
  "description": "Bootstrap CI, permutation test, and Cohen's d for downstream perplexity comparisons (5 variants, all pairwise). Primary: size_matched vs depth01.",
  "project": "gen-depth-fingerprint",
  "exp_id": "plan-004-v2",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/n2a_downstream_bootstrap.json",
  "tags": "['n2a', 'bootstrap', 'effect-size', 'downstream', 'statistics']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_n2a-downstream-bootstrap_20260516T043728",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "n2a_downstream_bootstrap",
    "type": "data",
    "description": "Bootstrap CI, permutation test, and Cohen's d for downstream perplexity comparisons (5 variants, all pairwise). Primary: size_matched vs depth01.",
    "project": "gen-depth-fingerprint",
    "exp_id": "plan-004-v2",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/n2a_downstream_bootstrap.json",
    "tags": "['n2a', 'bootstrap', 'effect-size', 'downstream', 'statistics']"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-16T04:38:31.252014+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260516_a4d103\", \"name\": \"n2a_downstream_bootstrap\", \"type\": \"data\", \"description\": \"Bootstrap CI, permutation test, and Cohen's d for downstream perplexity comparisons (5 variants, all pairwise). Primary: size_matched vs depth01.\", \"path\": \"projects/gen-depth-fingerprint/artifacts/plan-004-v2/data/n2a_downstream_bootstrap.json\", \"url\": null, \"project\": \"gen-depth-fingerprint\", \"exp_id\": \"plan-004-v2\", \"skill\": \"\", \"created_at\": \"2026-05-16T04:38:21.984882+00:00\", \"tags\": [\"n2a\", \"bootstrap\", \"effect-size\", \"downstream\", \"statistics\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_n2a-downstream-bootstrap_20260516T043728",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 9 · 2026-05-16T04:38:31.252172+00:00_

结果摘要：

**Primary comparison (size_matched vs depth01):**
- Mean diff: −0.0202 ppl (depth01 略差)
- 95% Bootstrap CI: [−0.0207, −0.0199]
- Cohen's d: −65.5 (极大效应量，但这是因为 within-group variance 极小——3 seeds 几乎一致)
- Exact permutation p = 0.10 (C(6,3)=20，最小非零 p=0.05，当前不显著)

**关键 caveat:** n=3/group 下 exact permutation test 只有 20 种排列，p 值分辨率极低（最小 0.05）。Cohen's d 数值巨大是因为 seed 间方差几乎为零，不代表实际效应大。CI 窄也是同理。论文中应表述为 "directional evidence with limited statistical power" 而非确定性结论。

所有 10 组 pairwise 比较已写入 `artifacts/n2a_downstream_bootstrap.json`，已注册为 `art_20260516_a4d103`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_n2a-downstream-bootstrap_20260516T043728"
}
```

</details>

---
