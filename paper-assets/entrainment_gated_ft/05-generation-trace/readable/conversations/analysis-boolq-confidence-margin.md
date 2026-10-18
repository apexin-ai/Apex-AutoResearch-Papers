# analysis boolq confidence margin

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 17
- **Recorded user turns:** 0
- **Tool calls:** 8
- **Original source:** `logs/chats/worker_analysis_boolq-confidence-margin_20260520T144742.jsonl`
- **Structured JSON:** [`03473e4b1a3dac203336.json`](../../sessions/03/03473e4b1a3dac203336.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

17 recorded events

### Tool call

_source line 1 · 2026-05-20T14:49:29.041998+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__register_artifact",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_boolq-confidence-margin_20260520T144742",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__register_artifact",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-20T14:49:29.042331+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_boolq-confidence-margin_20260520T144742",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-20T14:49:29.042498+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-48145",
  "command": "find /root/entrainment_gated_ft/lm_eval_clean/boolq -name \"boolq.jsonl\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_boolq-confidence-margin_20260520T144742",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-48145",
    "command": "find /root/entrainment_gated_ft/lm_eval_clean/boolq -name \"boolq.jsonl\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-20T14:49:29.042692+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/entrainment_gated_ft/lm_eval_clean/boolq/1.3B-100B-GatedDeltaNet-pure/samples/boolq.jsonl\\n/root/entrainment_gated_ft/lm_eval_clean/boolq/1.3B-100B-GatedDeltaNet-hybrid-24-1/samples/boolq.jsonl\\n/root/entrainment_gated_ft/lm_eval_clean/boolq/1.3B-100B-GatedDeltaNet-hybrid-12-1/samples/boolq.jsonl\\n/root/entrainment_gated_ft/lm_eval_clean/boolq/1.3B-100B-GatedDeltaNet-hybrid-6-1/samples/boolq.jsonl\\n/root/entrainment_gated_ft/lm_eval_clean/boolq/1.3B-100B-GatedDeltaNet-hybrid-3-1/samples/boolq.jsonl\\n/root/entrainment_gated_ft/lm_eval_clean/boolq/1.3B-100B-RetNet-pure/samples/boolq.jsonl\\n/root/entrainment_gated_ft/lm_eval_clean/boolq/1.3B-100B-RetNet-hybrid-24-1/samples/boolq.jsonl\\n/root/entrainment_gated_ft/lm_eval_clean/boolq/1.3B-100B-RetNet-hybrid-12-1/samples/boolq.jsonl\\n/root/entrainment_gated_ft/lm_eval_clean/boolq/1.3B-100B-RetNet-hybrid-6-1/samples/boolq.jsonl\\n/root/entrainment_gated_ft/lm_eval_clean/boolq/1.3B-100B-RetNet-hybrid-3-1/samples/boolq.jsonl\\n/root/entrainment_gated_ft/lm_eval_clean/boolq/1.3B-100B-HGRN2-pure/samples/boolq.jsonl\\n/root/entrainment_gated_ft/lm_eval_clean/boolq/1.3B-100B-HGRN2-hybrid-24-1/samples/boolq.jsonl\\n/root/entrainment_gated_ft/lm_eval_clean/boolq/1.3B-100B-HGRN2-hybrid-12-1/samples/boolq.jsonl\\n/root/entrainment_gated_ft/lm_eval_clean/boolq/1.3B-100B-HGRN2-hybrid-6-1/samples/boolq.jsonl\\n/root/entrainment_gated_ft/lm_eval_clean/boolq/1.3B-100B-HGRN2-hybrid-3-1/samples/boolq.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.1}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_boolq-confidence-margin_20260520T144742",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-20T14:49:29.042874+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-48145",
  "command": "head -1 /root/entrainment_gated_ft/lm_eval_clean/boolq/1.3B-100B-GatedDeltaNet-pure/samples/boolq.jsonl",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_boolq-confidence-margin_20260520T144742",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-48145",
    "command": "head -1 /root/entrainment_gated_ft/lm_eval_clean/boolq/1.3B-100B-GatedDeltaNet-pure/samples/boolq.jsonl",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-20T14:49:29.043077+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\\"doc_id\\\": 0, \\\"doc\\\": {\\\"question\\\": \\\"does ethanol take more energy make that produces\\\", \\\"passage\\\": \\\"Ethanol fuel -- All biomass goes through at least some of these steps: it needs to be grown, collected, dried, fermented, distilled, and burned. All of these steps require resources and an infrastructure. The total amount of energy input into the process compared to the energy released by burning the resulting ethanol fuel is known as the energy balance (or ``energy returned on energy invested''). Figures compiled in a 2007 report by National Geographic Magazine point to modest results for corn ethanol produced in the US: one unit of fossil-fuel energy is required to create 1.3 energy units from the resulting ethanol. The energy balance for sugarcane ethanol produced in Brazil is more favorable, with one unit of fossil-fuel energy required to create 8 from the ethanol. Energy balance estimates are not easily produced, thus numerous such reports have been generated that are contradictory. For instance, a separate survey reports that production of ethanol from sugarcane, which requires a tropical climate to grow productively, returns from 8 to 9 units of energy for each unit expended, as compared to corn, which only returns about 1.34 units of fuel energy for each unit of energy expended. A 2006 University of California Berkeley study, after analyzing six separate studies, concluded that producing ethanol from corn uses much less petroleum than producing gasoline.\\\", \\\"idx\\\": 0, \\\"label\\\": 0}, \\\"target\\\": 0, \\\"arguments\\\": [[\\\"Ethanol fuel -- All biomass goes through at least some of these steps: it needs to be grown, collected, dried, fermented, distilled, and burned. All of these steps require resources and an infrastructure. The total amount of energy input into the process compared to the energy released by burning the resulting ethanol fuel is known as the ene
…[truncated 3218 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_boolq-confidence-margin_20260520T144742",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-20T14:49:29.043318+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westb-48145",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 << 'PYEOF'\nimport json, os, numpy as np\nfrom scipy.stats import mannwhitneyu\n\nEVAL_BASE = \"/root/entrainment_gated_ft/lm_eval_clean/boolq\"\nARCHS = [\"GatedDeltaNet\", \"RetNet\", \"HGRN2\"]\nARCH_SHORT = {\"GatedDeltaNet\": \"GDN\", \"RetNet\": \"RetNet\", \"HGRN2\": \"HGRN2\"}\nHYBRID_CONFIG = {\"GatedDeltaNet\": \"hybrid-12-1\", \"RetNet\": \"hybrid-3-1\", \"HGRN2\": \"hybrid-3-1\"}\n\ndef load_samples(arch, ratio):\n    path = f\"{EVAL_BASE}/1.3B-100B-{arch}-{ratio}/samples/boolq.jsonl\"\n    if os.path.exists(path):\n        return [json.loads(l) for l in open(path)]\n    raise FileNotFoundError(f\"Not found: {path}\")\n\ndef extract_confidence(sample):\n    resps = sample[\"filtered_resps\"]\n    target = int(sample[\"target\"])\n    loglik = float(resps[target][0])\n    return abs(loglik)\n\ndef cohens_d(g1, g2):\n    n1, n2 = len(g1), len(g2)\n    m1, m2 = np.mean(g1), np.mean(g2)\n    s1, s2 = np.std(g1, ddof=1), np.std(g2, ddof=1)\n    pooled = np.sqrt(((n1-1)*s1**2 + (n2-1)*s2**2) / (n1+n2-2))\n    return (m1 - m2) / pooled if pooled > 0 else 0\n\nresults = {}\nfor arch in ARCHS:\n    short = ARCH_SHORT[arch]\n    hybrid_ratio = HYBRID_CONFIG[arch]\n    \n    pure = load_samples(arch, \"pure\")\n    hybrid = load_samples(arch, hybrid_ratio)\n    N = len(pure)\n    assert len(hybrid) == N, f\"Sample count mismatch: pure={N}, hybrid={len(hybrid)}\"\n    \n    # Match by doc_id\n    pure_by_id = {s[\"doc_id\"]: s for s in pure}\n    hybrid_by_id = {s[\"doc_id\"]: s for s in hybrid}\n    common_ids = sorted(set(pure_by_id.keys()) & set(hybrid_by_id.keys()))\n    \n    hurt_c, sr_c, helped_c, sw_c = [], [], [], []\n    for did in common_ids:\n        ps = pure_by_id[did]\n        hs = hybrid_by_id[did]\n        pa = int(ps[\"acc\"])\n        ha = int(hs[\"acc\"])\n        c = extract_confidence(ps)\n        \n        if pa == 1 and ha == 0: hurt_c.append(c)\n        elif pa == 1 and ha == 1: sr_c.append(c)\n        elif pa == 0 and ha == 1: helped_c.append(c)\n        else: sw_c.append(c)\n    \n    print(f\"\\n=== {short} (hybrid={hybrid_ratio}) ===\")\n    print(f\"  N={len(common_ids)}, hurt={len(hurt_c)}, stayed_right={len(sr_c)}, helped={len(helped_c)}, stayed_wrong={len(sw_c)}\")\n    \n    c1, c2 = {}, {}\n    \n    # Control 1: hurt vs stayed-right (within pure-correct)\n    if len(hurt_c) > 5 and len(sr_c) > 5:\n        U, p = mannwhitneyu(hurt_c, sr_c, alternative='two-sided')\n        d = cohens_d(hurt_c, sr_c)\n        r_rb = 1 - 2*U/(len(hurt_c)*len(sr_c))\n        c1 = {\"hurt_n\": len(hurt_c), \"stayed_right_n\": len(sr_c),\n              \"hurt_mean\": round(float(np.mean(hurt_c)),4), \"hurt_median\": round(float(np.median(hurt_c)),4),\n              \"stayed_right_mean\": round(float(np.mean(sr_c)),4), \"stayed_right_median\": round(float(np.median(sr_c)),4),\n              \"U\": float(U), \"p\": float(p), \"cohens_d\": round(float(d),4), \"r_rb\": round(float(r_rb),4),\n              \"direction\": \"hurt has HIGHER confidence (hypothesis supported)\" if np.mean(hurt_c) > np.mean(sr_c) else \"hurt has LOWER confidence\",\n              \"hypothesis_supported\": bool(np.mean(hurt_c) > np.mean(sr_c))}\n        print(f\"  C1 (hurt vs stayed_right): d={c1['cohens_d']}, p={c1['p']:.4e}, hurt_mean={c1['hurt_mean']}, sr_mean={c1['stayed_right_mean']}\")\n    else:\n        print(f\"  C1: insufficient samples (hurt={len(hurt_c)}, sr={len(sr_c)})\")\n    \n    # Control 2: helped vs stayed-wrong (within pure-wrong)\n    if len(helped_c) > 5 and len(sw_c) > 5:\n        U, p = mannwhitneyu(helped_c, sw_c, alternative='two-sided')\n        d = cohens_d(helped_c, sw_c)\n        r_rb = 1 - 2*U/(len(helped_c)*len(sw_c))\n        c2 = {\"helped_n\": len(helped_c), \"stayed_wrong_n\": len(sw_c),\n              \"helped_mean\": round(float(np.mean(helped_c)),4), \"helped_median\": round(float(np.median(helped_c)),4),\n              \"stayed_wrong_mean\": round(float(np.mean(sw_c)),4), \"stayed_wrong_median\": round(float(np.median(sw_c)),4),\n              \"U\": float(U), \"p\": float(p), \"cohens_d\": round(float(d),4), \"r_rb\": round(float(r_rb),4),\n              \"direction\": \"helped has LOWER confidence (hypothesis supported)\" if np.mean(helped_c) < np.mean(sw_c) else \"helped has HIGHER confidence\",\n              \"hypothesis_supported\": bool(np.mean(helped_c) < np.mean(sw_c))}\n        print(f\"  C2 (helped vs stayed_wrong): d={c2['cohens_d']}, p={c2['p']:.4e}, helped_mean={c2['helped_mean']}, sw_mean={c2['stayed_wrong_mean']}\")\n    else:\n        print(f\"  C2: insufficient samples (helped={len(helped_c)}, sw={len(sw_c)})\")\n    \n    results[short] = {\"hybrid_config\": f\"1.3B-100B-{arch}-{hybrid_ratio}\",\n                      \"control_1_pure_correct\": c1, \"control_2_pure_wrong\": c2}\n\noutput = {\n    \"analysis\": \"boolq_confidence_margin\",\n    \"benchmark\": \"boolq\",\n    \"n_samples\": len(common_ids),\n    \"method\": \"within-category controls (same as LAMBADA/ARC-Easy/HellaSwag)\",\n    \"confidence_proxy\": \"abs(correct_option_loglikelihood) from pure model\",\n    \"note\": \"BoolQ is binary (2 options). GDN uses h12-1; RetNet/HGRN2 use h3-1\",\n    \"results\": results\n}\n\nos.makedirs(\"/root/entrainment_gated_ft/analysis_output\", exist_ok=True)\nwith open(\"/root/entrainment_gated_ft/analysis_output/boolq_confidence_margin.json\", \"w\") as f:\n    json.dump(output, f, indent=2)\nprint(\"\\nJSON saved to /root/entrainment_gated_ft/analysis_output/boolq_confidence_margin.json\")\nPYEOF",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_boolq-confidence-margin_20260520T144742",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westb-48145",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 << 'PYEOF'\nimport json, os, numpy as np\nfrom scipy.stats import mannwhitneyu\n\nEVAL_BASE = \"/root/entrainment_gated_ft/lm_eval_clean/boolq\"\nARCHS = [\"GatedDeltaNet\", \"RetNet\", \"HGRN2\"]\nARCH_SHORT = {\"GatedDeltaNet\": \"GDN\", \"RetNet\": \"RetNet\", \"HGRN2\": \"HGRN2\"}\nHYBRID_CONFIG = {\"GatedDeltaNet\": \"hybrid-12-1\", \"RetNet\": \"hybrid-3-1\", \"HGRN2\": \"hybrid-3-1\"}\n\ndef load_samples(arch, ratio):\n    path = f\"{EVAL_BASE}/1.3B-100B-{arch}-{ratio}/samples/boolq.jsonl\"\n    if os.path.exists(path):\n        return [json.loads(l) for l in open(path)]\n    raise FileNotFoundError(f\"Not found: {path}\")\n\ndef extract_confidence(sample):\n    resps = sample[\"filtered_resps\"]\n    target = int(sample[\"target\"])\n    loglik = float(resps[target][0])\n    return abs(loglik)\n\ndef cohens_d(g1, g2):\n    n1, n2 = len(g1), len(g2)\n    m1, m2 = np.mean(g1), np.mean(g2)\n    s1, s2 = np.std(g1, ddof=1), np.std(g2, ddof=1)\n    pooled = np.sqrt(((n1-1)*s1**2 + (n2-1)*s2**2) / (n1+n2-2))\n    return (m1 - m2) / pooled if pooled > 0 else 0\n\nresults = {}\nfor arch in ARCHS:\n    short = ARCH_SHORT[arch]\n    hybrid_ratio = HYBRID_CONFIG[arch]\n    \n    pure = load_samples(arch, \"pure\")\n    hybrid = load_samples(arch, hybrid_ratio)\n    N = len(pure)\n    assert len(hybrid) == N, f\"Sample count mismatch: pure={N}, hybrid={len(hybrid)}\"\n    \n    # Match by doc_id\n    pure_by_id = {s[\"doc_id\"]: s for s in pure}\n    hybrid_by_id = {s[\"doc_id\"]: s for s in hybrid}\n    common_ids = sorted(set(pure_by_id.keys()) & set(hybrid_by_id.keys()))\n    \n    hurt_c, sr_c, helped_c, sw_c = [], [], [], []\n    for did in common_ids:\n        ps = pure_by_id[did]\n        hs = hybrid_by_id[did]\n        pa = int(ps[\"acc\"])\n        ha = int(hs[\"acc\"])\n        c = extract_confidence(ps)\n        \n        if pa == 1 and ha == 0: hurt_c.append(c)\n        elif pa == 1 and ha == 1: sr_c.append(c)\n        elif pa == 0 and ha == 1: helped_c.append(c)\n        else: sw_c.append(c)\n    \n    print(f\"\\n=== {short} (hybrid={hybrid_ratio}) ===\")\n    print(f\"  N={len(common_ids)}, hurt={len(hurt_c)}, stayed_right={len(sr_c)}, helped={len(helped_c)}, stayed_wrong={len(sw_c)}\")\n    \n    c1, c2 = {}, {}\n    \n    # Control 1: hurt vs stayed-right (within pure-correct)\n    if len(hurt_c) > 5 and len(sr_c) > 5:\n        U, p = mannwhitneyu(hurt_c, sr_c, alternative='two-sided')\n        d = cohens_d(hurt_c, sr_c)\n        r_rb = 1 - 2*U/(len(hurt_c)*len(sr_c))\n        c1 = {\"hurt_n\": len(hurt_c), \"stayed_right_n\": len(sr_c),\n              \"hurt_mean\": round(float(np.mean(hurt_c)),4), \"hurt_median\": round(float(np.median(hurt_c)),4),\n              \"stayed_right_mean\": round(float(np.mean(sr_c)),4), \"stayed_right_median\": round(float(np.median(sr_c)),4),\n              \"U\": float(U), \"p\": float(p), \"cohens_d\": round(float(d),4), \"r_rb\": round(float(r_rb),4),\n              \"direction\": \"hurt has HIGHER confidence (hypothesis supported)\" if np.mean(hurt_c) > np.mean(sr_c) else \"hurt has LOWER confidence\",\n              \"hypothesis_supported\": bool(np.mean(hurt_c) > np.mean(sr_c))}\n        print(f\"  C1 (hurt vs stayed_right): d={c1['cohens_d']}, p={c1['p']:.4e}, hurt_mean={c1['hurt_mean']}, sr_mean={c1['stayed_right_mean']}\")\n    else:\n        print(f\"  C1: insufficient samples (hurt={len(hurt_c)}, sr={len(sr_c)})\")\n    \n    # Control 2: helped vs stayed-wrong (within pure-wrong)\n    if len(helped_c) > 5 and len(sw_c) > 5:\n        U, p = mannwhitneyu(helped_c, sw_c, alternative='two-sided')\n        d = cohens_d(helped_c, sw_c)\n        r_rb = 1 - 2*U/(len(helped_c)*len(sw_c))\n        c2 = {\"helped_n\": len(helped_c), \"stayed_wrong_n\": len(sw_c),\n              \"helped_mean\": round(float(np.mean(helped_c)),4), \"helped_median\": round(float(np.median(helped_c)),4),\n              \"stayed_wrong_mean\": round(float(np.mean(sw_c)),4), \"stayed_wrong_median\": round(float(np.median(sw_c)),4),\n              \"U\": float(U), \"p\": float(p), \"cohens_d\": round(float(d),4), \"r_rb\": round(float(r_rb),4),\n              \"direction\": \"helped has LOWER confidence (hypothesis supported)\" if np.mean(helped_c) < np.mean(sw_c) else \"helped has HIGHER confidence\",\n              \"hypothesis_supported\": bool(np.mean(helped_c) < np.mean(sw_c))}\n        print(f\"  C2 (helped vs stayed_wrong): d={c2['cohens_d']}, p={c2['p']:.4e}, helped_mean={c2['helped_mean']}, sw_mean={c2['stayed_wrong_mean']}\")\n    else:\n        print(f\"  C2: insufficient samples (helped={len(helped_c)}, sw={len(sw_c)})\")\n    \n    results[short] = {\"hybrid_config\": f\"1.3B-100B-{arch}-{hybrid_ratio}\",\n                      \"control_1_pure_correct\": c1, \"control_2_pure_wrong\": c2}\n\noutput = {\n    \"analysis\": \"boolq_confidence_margin\",\n    \"benchmark\": \"boolq\",\n    \"n_samples\": len(common_ids),\n    \"method\": \"within-category controls (same as LAMBADA/ARC-Easy/HellaSwag)\",\n    \"confidence_proxy\": \"abs(correct_option_loglikelihood) from pure model\",\n    \"note\": \"BoolQ is binary (2 options). GDN uses h12-1; RetNet/HGRN2 use h3-1\",\n    \"results\": results\n}\n\nos.makedirs(\"/root/entrainment_gated_ft/analysis_output\", exist_ok=True)\nwith open(\"/root/entrainment_gated_ft/analysis_output/boolq_confidence_margin.json\", \"w\") as f:\n    json.dump(output, f, indent=2)\nprint(\"\\nJSON saved to /root/entrainment_gated_ft/analysis_output/boolq_confidence_margin.json\")\nPYEOF",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-20T14:49:29.043550+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\n=== GDN (hybrid=hybrid-12-1) ===\\n  N=3270, hurt=441, stayed_right=1471, helped=605, stayed_wrong=753\\n  C1 (hurt vs stayed_right): d=0.0407, p=4.6112e-01, hurt_mean=3.0033, sr_mean=2.9794\\n  C2 (helped vs stayed_wrong): d=-0.3568, p=1.6810e-10, helped_mean=3.5052, sw_mean=3.7321\\n\\n=== RetNet (hybrid=hybrid-3-1) ===\\n  N=3270, hurt=648, stayed_right=1351, helped=550, stayed_wrong=721\\n  C1 (hurt vs stayed_right): d=0.0055, p=9.5586e-01, hurt_mean=3.0838, sr_mean=3.0801\\n  C2 (helped vs stayed_wrong): d=-0.1584, p=5.4189e-02, helped_mean=3.5916, sw_mean=3.6962\\n\\n=== HGRN2 (hybrid=hybrid-3-1) ===\\n  N=3270, hurt=488, stayed_right=1388, helped=691, stayed_wrong=703\\n  C1 (hurt vs stayed_right): d=-0.0977, p=1.5414e-01, hurt_mean=2.9877, sr_mean=3.0607\\n  C2 (helped vs stayed_wrong): d=-0.3119, p=5.6051e-09, helped_mean=3.5538, sw_mean=3.7793\\n\\nJSON saved to /root/entrainment_gated_ft/analysis_output/boolq_confidence_margin.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.02}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_boolq-confidence-margin_20260520T144742",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-20T14:49:29.043771+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-48145",
  "command": "cat /root/entrainment_gated_ft/analysis_output/boolq_confidence_margin.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_boolq-confidence-margin_20260520T144742",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-48145",
    "command": "cat /root/entrainment_gated_ft/analysis_output/boolq_confidence_margin.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-20T14:49:29.044000+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"analysis\\\": \\\"boolq_confidence_margin\\\",\\n  \\\"benchmark\\\": \\\"boolq\\\",\\n  \\\"n_samples\\\": 3270,\\n  \\\"method\\\": \\\"within-category controls (same as LAMBADA/ARC-Easy/HellaSwag)\\\",\\n  \\\"confidence_proxy\\\": \\\"abs(correct_option_loglikelihood) from pure model\\\",\\n  \\\"note\\\": \\\"BoolQ is binary (2 options). GDN uses h12-1; RetNet/HGRN2 use h3-1\\\",\\n  \\\"results\\\": {\\n    \\\"GDN\\\": {\\n      \\\"hybrid_config\\\": \\\"1.3B-100B-GatedDeltaNet-hybrid-12-1\\\",\\n      \\\"control_1_pure_correct\\\": {\\n        \\\"hurt_n\\\": 441,\\n        \\\"stayed_right_n\\\": 1471,\\n        \\\"hurt_mean\\\": 3.0033,\\n        \\\"hurt_median\\\": 2.9844,\\n        \\\"stayed_right_mean\\\": 2.9794,\\n        \\\"stayed_right_median\\\": 2.9688,\\n        \\\"U\\\": 331850.5,\\n        \\\"p\\\": 0.4611229056287808,\\n        \\\"cohens_d\\\": 0.0407,\\n        \\\"r_rb\\\": -0.0231,\\n        \\\"direction\\\": \\\"hurt has HIGHER confidence (hypothesis supported)\\\",\\n        \\\"hypothesis_supported\\\": true\\n      },\\n      \\\"control_2_pure_wrong\\\": {\\n        \\\"helped_n\\\": 605,\\n        \\\"stayed_wrong_n\\\": 753,\\n        \\\"helped_mean\\\": 3.5052,\\n        \\\"helped_median\\\": 3.4844,\\n        \\\"stayed_wrong_mean\\\": 3.7321,\\n        \\\"stayed_wrong_median\\\": 3.7031,\\n        \\\"U\\\": 181900.5,\\n        \\\"p\\\": 1.6810211478328124e-10,\\n        \\\"cohens_d\\\": -0.3568,\\n        \\\"r_rb\\\": 0.2014,\\n        \\\"direction\\\": \\\"helped has LOWER confidence (hypothesis supported)\\\",\\n        \\\"hypothesis_supported\\\": true\\n      }\\n    },\\n    \\\"RetNet\\\": {\\n      \\\"hybrid_config\\\": \\\"1.3B-100B-RetNet-hybrid-3-1\\\",\\n      \\\"control_1_pure_correct\\\": {\\n        \\\"hurt_n\\\": 648,\\n        \\\"stayed_right_n\\\": 1351,\\n        \\\"hurt_mean\\\": 3.0838,\\n        \\\"hurt_median\\\": 3.062
…[truncated 2284 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_boolq-confidence-margin_20260520T144742",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-20T14:49:29.044157+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/paper_data/",
  "description": "Check artifacts directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_boolq-confidence-margin_20260520T144742",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/paper_data/",
    "description": "Check artifacts directory"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-20T14:49:29.044296+00:00_

analyze_exp007.py
bca_ci_data.json
boolq_jaccard_analysis.json
boolq_per_example.json
confidence_margin_analysis.json
confidence_margin_within_category.json
convergence_table.csv
cross_benchmark_confidence_margin.json
decoupling_data.csv
decoupling_pipeline_audit.md
exp007_340m_analysis.json
gdn_sensitivity_table.csv
hellaswag_alpha_by_ratio.json
hellaswag_jaccard_analysis.json
hellaswag_per_example.json
jaccard_upper_bound.json
per_example_table.csv
retnet_hgrn2_only_decoupling.json
within_arch_stability.json
within_scale_jaccard_results.txt

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_boolq-confidence-margin_20260520T144742",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-20T14:49:29.044446+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/paper_data/boolq_confidence_margin.json",
  "content": "{\n  \"analysis\": \"boolq_confidence_margin\",\n  \"benchmark\": \"boolq\",\n  \"n_samples\": 3270,\n  \"method\": \"within-category controls (same as LAMBADA/ARC-Easy/HellaSwag)\",\n  \"confidence_proxy\": \"abs(correct_option_loglikelihood) from pure model\",\n  \"note\": \"BoolQ is binary (2 options). GDN uses h12-1; RetNet/HGRN2 use h3-1\",\n  \"results\": {\n    \"GDN\": {\n      \"hybrid_config\": \"1.3B-100B-GatedDeltaNet-hybrid-12-1\",\n      \"control_1_pure_correct\": {\n        \"hurt_n\": 441,\n        \"stayed_right_n\": 1471,\n        \"hurt_mean\": 3.0033,\n        \"hurt_median\": 2.9844,\n        \"stayed_right_mean\": 2.9794,\n        \"stayed_right_median\": 2.9688,\n        \"U\": 331850.5,\n        \"p\": 0.4611229056287808,\n        \"cohens_d\": 0.0407,\n        \"r_rb\": -0.0231,\n        \"direction\": \"hurt has HIGHER confidence (hypothesis supported)\",\n        \"hypothesis_supported\": true\n      },\n      \"control_2_pure_wrong\": {\n        \"helped_n\": 605,\n        \"stayed_wrong_n\": 753,\n        \"helped_mean\": 3.5052,\n        \"helped_median\": 3.4844,\n        \"stayed_wrong_mean\": 3.7321,\n        \"stayed_wrong_median\": 3.7031,\n        \"U\": 181900.5,\n        \"p\": 1.681e-10,\n        \"cohens_d\": -0.3568,\n        \"r_rb\": 0.2014,\n        \"direction\": \"helped has LOWER confidence (hypothesis supported)\",\n        \"hypothesis_supported\": true\n      }\n    },\n    \"RetNet\": {\n      \"hybrid_config\": \"1.3B-100B-RetNet-hybrid-3-1\",\n      \"control_1_pure_correct\": {\n        \"hurt_n\": 648,\n        \"stayed_right_n\": 1351,\n        \"hurt_mean\": 3.0838,\n        \"hurt_median\": 3.0625,\n        \"stayed_right_mean\": 3.0801,\n        \"stayed_right_median\": 3.0156,\n        \"U\": 438393.0,\n        \"p\": 0.9558639202158401,\n        \"cohens_d\": 0.0055,\n        \"r_rb\": -0.0015,\n        \"direction\": \"hurt has HIGHER confidence (hypothesis supported)\",\n        \"hypothesis_supported\": true\n      },\n      \"control_2_pure_wrong\": {\n        \"helped_n\": 550,\n        \"stayed_wrong_n\": 721,\n        \"helped_mean\": 3.5916,\n        \"helped_median\": 3.5781,\n        \"stayed_wrong_mean\": 3.6962,\n        \"stayed_wrong_median\": 3.6094,\n        \"U\": 185792.5,\n        \"p\": 0.054188774900793234,\n        \"cohens_d\": -0.1584,\n        \"r_rb\": 0.063,\n        \"direction\": \"helped has LOWER confidence (hypothesis supported)\",\n        \"hypothesis_supported\": true\n      }\n    },\n    \"HGRN2\": {\n      \"hybrid_config\": \"1.3B-100B-HGRN2-hybrid-3-1\",\n      \"control_1_pure_correct\": {\n        \"hurt_n\": 488,\n        \"stayed_right_n\": 1388,\n        \"hurt_mean\": 2.9877,\n        \"hurt_median\": 2.9219,\n        \"stayed_right_mean\": 3.0607,\n        \"stayed_right_median\": 2.9844,\n        \"U\": 324003.5,\n        \"p\": 0.1541370105557747,\n        \"cohens_d\": -0.0977,\n        \"r_rb\": 0.0433,\n        \"direction\": \"hurt has LOWER confidence\",\n        \"hypothesis_supported\": false\n      },\n      \"control_2_pure_wrong\": {\n        \"helped_n\": 691,\n        \"stayed_wrong_n\": 703,\n        \"helped_mean\": 3.5538,\n        \"helped_median\": 3.5469,\n        \"stayed_wrong_mean\": 3.7793,\n        \"stayed_wrong_median\": 3.75,\n        \"U\": 199091.0,\n        \"p\": 5.605e-09,\n        \"cohens_d\": -0.3119,\n        \"r_rb\": 0.1803,\n        \"direction\": \"helped has LOWER confidence (hypothesis supported)\",\n        \"hypothesis_supported\": true\n      }\n    }\n  }\n}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_boolq-confidence-margin_20260520T144742",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/paper_data/boolq_confidence_margin.json",
    "content": "{\n  \"analysis\": \"boolq_confidence_margin\",\n  \"benchmark\": \"boolq\",\n  \"n_samples\": 3270,\n  \"method\": \"within-category controls (same as LAMBADA/ARC-Easy/HellaSwag)\",\n  \"confidence_proxy\": \"abs(correct_option_loglikelihood) from pure model\",\n  \"note\": \"BoolQ is binary (2 options). GDN uses h12-1; RetNet/HGRN2 use h3-1\",\n  \"results\": {\n    \"GDN\": {\n      \"hybrid_config\": \"1.3B-100B-GatedDeltaNet-hybrid-12-1\",\n      \"control_1_pure_correct\": {\n        \"hurt_n\": 441,\n        \"stayed_right_n\": 1471,\n        \"hurt_mean\": 3.0033,\n        \"hurt_median\": 2.9844,\n        \"stayed_right_mean\": 2.9794,\n        \"stayed_right_median\": 2.9688,\n        \"U\": 331850.5,\n        \"p\": 0.4611229056287808,\n        \"cohens_d\": 0.0407,\n        \"r_rb\": -0.0231,\n        \"direction\": \"hurt has HIGHER confidence (hypothesis supported)\",\n        \"hypothesis_supported\": true\n      },\n      \"control_2_pure_wrong\": {\n        \"helped_n\": 605,\n        \"stayed_wrong_n\": 753,\n        \"helped_mean\": 3.5052,\n        \"helped_median\": 3.4844,\n        \"stayed_wrong_mean\": 3.7321,\n        \"stayed_wrong_median\": 3.7031,\n        \"U\": 181900.5,\n        \"p\": 1.681e-10,\n        \"cohens_d\": -0.3568,\n        \"r_rb\": 0.2014,\n        \"direction\": \"helped has LOWER confidence (hypothesis supported)\",\n        \"hypothesis_supported\": true\n      }\n    },\n    \"RetNet\": {\n      \"hybrid_config\": \"1.3B-100B-RetNet-hybrid-3-1\",\n      \"control_1_pure_correct\": {\n        \"hurt_n\": 648,\n        \"stayed_right_n\": 1351,\n        \"hurt_mean\": 3.0838,\n        \"hurt_median\": 3.0625,\n        \"stayed_right_mean\": 3.0801,\n        \"stayed_right_median\": 3.0156,\n        \"U\": 438393.0,\n        \"p\": 0.9558639202158401,\n        \"cohens_d\": 0.0055,\n        \"r_rb\": -0.0015,\n        \"direction\": \"hurt has HIGHER confidence (hypothesis supported)\",\n        \"hypothesis_supported\": true\n      },\n      \"control_2_pure_wrong\": {\n        \"helped_n\": 550,\n        \"stayed_wrong_n\": 721,\n        \"helped_mean\": 3.5916,\n        \"helped_median\": 3.5781,\n        \"stayed_wrong_mean\": 3.6962,\n        \"stayed_wrong_median\": 3.6094,\n        \"U\": 185792.5,\n        \"p\": 0.054188774900793234,\n        \"cohens_d\": -0.1584,\n        \"r_rb\": 0.063,\n        \"direction\": \"helped has LOWER confidence (hypothesis supported)\",\n        \"hypothesis_supported\": true\n      }\n    },\n    \"HGRN2\": {\n      \"hybrid_config\": \"1.3B-100B-HGRN2-hybrid-3-1\",\n      \"control_1_pure_correct\": {\n        \"hurt_n\": 488,\n        \"stayed_right_n\": 1388,\n        \"hurt_mean\": 2.9877,\n        \"hurt_median\": 2.9219,\n        \"stayed_right_mean\": 3.0607,\n        \"stayed_right_median\": 2.9844,\n        \"U\": 324003.5,\n        \"p\": 0.1541370105557747,\n        \"cohens_d\": -0.0977,\n        \"r_rb\": 0.0433,\n        \"direction\": \"hurt has LOWER confidence\",\n        \"hypothesis_supported\": false\n      },\n      \"control_2_pure_wrong\": {\n        \"helped_n\": 691,\n        \"stayed_wrong_n\": 703,\n        \"helped_mean\": 3.5538,\n        \"helped_median\": 3.5469,\n        \"stayed_wrong_mean\": 3.7793,\n        \"stayed_wrong_median\": 3.75,\n        \"U\": 199091.0,\n        \"p\": 5.605e-09,\n        \"cohens_d\": -0.3119,\n        \"r_rb\": 0.1803,\n        \"direction\": \"helped has LOWER confidence (hypothesis supported)\",\n        \"hypothesis_supported\": true\n      }\n    }\n  }\n}\n"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-20T14:49:29.044619+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/paper_data/boolq_confidence_margin.json

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_boolq-confidence-margin_20260520T144742",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-20T14:49:29.044782+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "boolq_confidence_margin",
  "type": "data",
  "description": "BoolQ within-category confidence margin analysis: Mann-Whitney U + Cohen's d for hurt/stayed-right and helped/stayed-wrong splits. GDN h12-1, RetNet h3-1, HGRN2 h3-1.",
  "project": "entrainment_gated_ft",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/paper_data/boolq_confidence_margin.json",
  "tags": "['boolq', 'confidence_margin', 'within_category', 'paper_data']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_boolq-confidence-margin_20260520T144742",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "boolq_confidence_margin",
    "type": "data",
    "description": "BoolQ within-category confidence margin analysis: Mann-Whitney U + Cohen's d for hurt/stayed-right and helped/stayed-wrong splits. GDN h12-1, RetNet h3-1, HGRN2 h3-1.",
    "project": "entrainment_gated_ft",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/paper_data/boolq_confidence_margin.json",
    "tags": "['boolq', 'confidence_margin', 'within_category', 'paper_data']"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-20T14:49:29.044928+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260520_e18dd2\", \"name\": \"boolq_confidence_margin\", \"type\": \"data\", \"description\": \"BoolQ within-category confidence margin analysis: Mann-Whitney U + Cohen's d for hurt/stayed-right and helped/stayed-wrong splits. GDN h12-1, RetNet h3-1, HGRN2 h3-1.\", \"path\": \"projects/entrainment_gated_ft/artifacts/_project/data/boolq_confidence_margin.json\", \"url\": null, \"project\": \"entrainment_gated_ft\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-20T14:49:16.779716+00:00\", \"tags\": [\"boolq\", \"confidence_margin\", \"within_category\", \"paper_data\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_boolq-confidence-margin_20260520T144742",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-20T14:49:29.045099+00:00_

汇总表：

### Control 1: hurt vs stayed-right (within pure-correct)

| Arch | n(hurt) | n(SR) | hurt_mean | SR_mean | Cohen's d | p | hypothesis |
|------|---------|-------|-----------|---------|-----------|---|------------|
| GDN | 441 | 1471 | 3.003 | 2.979 | 0.041 | 0.461 | supported (n.s.) |
| RetNet | 648 | 1351 | 3.084 | 3.080 | 0.006 | 0.956 | supported (n.s.) |
| HGRN2 | 488 | 1388 | 2.988 | 3.061 | −0.098 | 0.154 | **not supported** |

### Control 2: helped vs stayed-wrong (within pure-wrong)

| Arch | n(helped) | n(SW) | helped_mean | SW_mean | Cohen's d | p | hypothesis |
|------|-----------|-------|-------------|---------|-----------|---|------------|
| GDN | 605 | 753 | 3.505 | 3.732 | −0.357 | **1.68e-10** | **supported** |
| RetNet | 550 | 721 | 3.592 | 3.696 | −0.158 | 0.054 | supported (marginal) |
| HGRN2 | 691 | 703 | 3.554 | 3.779 | −0.312 | **5.61e-09** | **supported** |

**要点**：
- **C1 全部不显著** — BoolQ 中 pure-correct 样本被 hurt 与否与 pure confidence 无关
- **C2 GDN/HGRN2 高度显著**（小到中等效应量 d≈0.31–0.36），helped 样本的 pure confidence 更低，符合"低信心样本更易被 hybrid 修正"的假设
- RetNet C2 borderline (p=0.054)，方向一致但效应量较小 (d=−0.16)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_boolq-confidence-margin_20260520T144742"
}
```

</details>

---
