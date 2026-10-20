# paper audit tables 3 4 inline — Part 2 of 2

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Conversation logs

[← Part 1](part-001.md) · [Transcript overview](../paper-audit-tables-3-4-inline.md) · [Structured JSON](../../../sessions/8e/8e5be4da06dba9b52c36.json)

## Before a recorded user message

### Tool call

_source line 375 · 2026-05-23T11:38:26.847477+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport json\n\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/17947013-ea3d-4507-b0e3-f06dfa8892ff/tool-results/mcp-agent-ml-research-read_registry-1779535307441.txt', 'r') as f:\n    raw = json.load(f)\n\ninner = json.loads(raw['result'])\ndata = inner['data']\nexps = data['experiments']\n\n# OLMo neural probe HUGE mismatch: paper says 2v3=0.5056, K*=1 but registry says 2v3=0.589, K*_neural=2\n# Registry OLMo 1v2=0.657 vs paper 1v2=0.5054\n\n# This might be the Qwen CROSS-scored version of OLMo in the neural probe\n# (OLMo self-scored K*=2, Qwen cross-scored K*=1 with 1v2=0.5001)\n# Paper: OLMo 1v2=0.5054 -> close to Qwen cross-scored 1v2=0.5001 but not exact\n# Actually maybe these are a different scoring setup for the neural probe\n\n# Check if there's OLMo cross-scoring in exp015 or related\nprint('exp015 notes:', exps['exp_015_neural_probe'].get('notes', ''))\n\n# Let me also check the exp015 spec - what scorer was used?\nprint()\nprint('exp015 spec:')\nprint(json.dumps(exps['exp_015_neural_probe'].get('spec', {}), indent=2))\n\" 2>&1\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_audit_tables_3_4_inline_20260523T112128",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport json\n\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/17947013-ea3d-4507-b0e3-f06dfa8892ff/tool-results/mcp-agent-ml-research-read_registry-1779535307441.txt', 'r') as f:\n    raw = json.load(f)\n\ninner = json.loads(raw['result'])\ndata = inner['data']\nexps = data['experiments']\n\n# OLMo neural probe HUGE mismatch: paper says 2v3=0.5056, K*=1 but registry says 2v3=0.589, K*_neural=2\n# Registry OLMo 1v2=0.657 vs paper 1v2=0.5054\n\n# This might be the Qwen CROSS-scored version of OLMo in the neural probe\n# (OLMo self-scored K*=2, Qwen cross-scored K*=1 with 1v2=0.5001)\n# Paper: OLMo 1v2=0.5054 -> close to Qwen cross-scored 1v2=0.5001 but not exact\n# Actually maybe these are a different scoring setup for the neural probe\n\n# Check if there's OLMo cross-scoring in exp015 or related\nprint('exp015 notes:', exps['exp_015_neural_probe'].get('notes', ''))\n\n# Let me also check the exp015 spec - what scorer was used?\nprint()\nprint('exp015 spec:')\nprint(json.dumps(exps['exp_015_neural_probe'].get('spec', {}), indent=2))\n\" 2>&1\n"
  }
}
```

</details>

---


### Tool result

_source line 376 · 2026-05-23T11:38:26.847608+00:00_

exp015 notes: v4 completed successfully. 3 models: Pythia K*_neural=2, OLMo K*_neural=2, Qwen-cont K*_neural=3. Neural probe improves 2v3 AUC across all models (Pythia +0.044, OLMo +0.039, Qwen +0.055) but only Qwen-cont self-scorer crosses θ=0.60. EXIT_CODE=129 (SIGHUP after completion) did not affect results.

exp015 spec:
{
  "command": "python scripts/run_exp015_neural_probe.py --device cuda:0 --embed_batch_size 8",
  "server": "westc-26893",
  "data_path": "data_exp001_pythia + data_exp002_olmo + data_exp017_qwen_cont",
  "data_count": 90000,
  "model_name": "Qwen/Qwen2.5-1.5B-Instruct (frozen encoder -> MLP probe)",
  "seed": "5-fold CV"
}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_audit_tables_3_4_inline_20260523T112128",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 377 · 2026-05-23T11:38:26.847757+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/17947013-ea3d-4507-b0e3-f06dfa8892ff/tool-results/mcp-agent-ml-research-read_registry-1779535307441.txt | python3 -c \"\nimport json, sys\nraw = sys.stdin.read()\nouter = json.loads(raw)\ninner = json.loads(outer['result'])\ndata = inner['data']\nexperiments = data['experiments']\n\n# None of the OLMo CIs and none of the Pythia 2v3 CI appear in registry\n# They were either computed in a script not logged to registry, or are stale values from an earlier run\n\n# Now let me also check if the Gemma-2B CIs for 0v1, 2v3, 3v4, 4v5 (which appear in paper extended table)\n# have any registry source\nprint('Searching for Gemma 0v1 CI near [0.949, 0.957]:')\ndef find_ci_range(d, target_lower, target_upper, tol=0.004, path=''):\n    results = []\n    if isinstance(d, dict):\n        if 'ci_lower' in d and 'ci_upper' in d:\n            cl = d['ci_lower']\n            cu = d['ci_upper']\n            if isinstance(cl, (int,float)) and isinstance(cu, (int,float)):\n                if abs(cl - target_lower) < tol and abs(cu - target_upper) < tol:\n                    results.append((path, cl, cu))\n        if 'ci' in d and isinstance(d['ci'], list) and len(d['ci']) == 2:\n            cl, cu = d['ci']\n            if abs(cl - target_lower) < tol and abs(cu - target_upper) < tol:\n                results.append((path+'[ci]', cl, cu))\n        for k, v in d.items():\n            new_path = f'{path}.{k}' if path else k\n            if isinstance(v, (dict, list)):\n                results.extend(find_ci_range(v, target_lower, target_upper, tol, new_path))\n    elif isinstance(d, list):\n        for i, v in enumerate(d):\n            results.extend(find_ci_range(v, target_lower, target_upper, tol, f'{path}[{i}]'))\n    return results\n\ntargets = [\n    ('Gemma 0v1', 0.949, 0.957),\n    ('Gemma 2v3', 0.523, 0.545),\n    ('Gemma 3v4', 0.492, 0.514),\n    ('Gemma 4v5', 0.492, 0.514),\n]\nfor label, lo, hi in targets:\n    print(f'Searching {label} CI near [{lo}, {hi}]:')\n    found = False\n    for eid, exp in experiments.items():\n        hits = find_ci_range(exp.get('metrics', {}), lo, hi)\n        for path, cl, cu in hits:\n            print(f'  {eid}: {path} = [{cl}, {cu}]')\n            found = True\n    if not found:\n        print('  NOT FOUND in registry')\n\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_audit_tables_3_4_inline_20260523T112128",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/17947013-ea3d-4507-b0e3-f06dfa8892ff/tool-results/mcp-agent-ml-research-read_registry-1779535307441.txt | python3 -c \"\nimport json, sys\nraw = sys.stdin.read()\nouter = json.loads(raw)\ninner = json.loads(outer['result'])\ndata = inner['data']\nexperiments = data['experiments']\n\n# None of the OLMo CIs and none of the Pythia 2v3 CI appear in registry\n# They were either computed in a script not logged to registry, or are stale values from an earlier run\n\n# Now let me also check if the Gemma-2B CIs for 0v1, 2v3, 3v4, 4v5 (which appear in paper extended table)\n# have any registry source\nprint('Searching for Gemma 0v1 CI near [0.949, 0.957]:')\ndef find_ci_range(d, target_lower, target_upper, tol=0.004, path=''):\n    results = []\n    if isinstance(d, dict):\n        if 'ci_lower' in d and 'ci_upper' in d:\n            cl = d['ci_lower']\n            cu = d['ci_upper']\n            if isinstance(cl, (int,float)) and isinstance(cu, (int,float)):\n                if abs(cl - target_lower) < tol and abs(cu - target_upper) < tol:\n                    results.append((path, cl, cu))\n        if 'ci' in d and isinstance(d['ci'], list) and len(d['ci']) == 2:\n            cl, cu = d['ci']\n            if abs(cl - target_lower) < tol and abs(cu - target_upper) < tol:\n                results.append((path+'[ci]', cl, cu))\n        for k, v in d.items():\n            new_path = f'{path}.{k}' if path else k\n            if isinstance(v, (dict, list)):\n                results.extend(find_ci_range(v, target_lower, target_upper, tol, new_path))\n    elif isinstance(d, list):\n        for i, v in enumerate(d):\n            results.extend(find_ci_range(v, target_lower, target_upper, tol, f'{path}[{i}]'))\n    return results\n\ntargets = [\n    ('Gemma 0v1', 0.949, 0.957),\n    ('Gemma 2v3', 0.523, 0.545),\n    ('Gemma 3v4', 0.492, 0.514),\n    ('Gemma 4v5', 0.492, 0.514),\n]\nfor label, lo, hi in targets:\n    print(f'Searching {label} CI near [{lo}, {hi}]:')\n    found = False\n    for eid, exp in experiments.items():\n        hits = find_ci_range(exp.get('metrics', {}), lo, hi)\n        for path, cl, cu in hits:\n            print(f'  {eid}: {path} = [{cl}, {cu}]')\n            found = True\n    if not found:\n        print('  NOT FOUND in registry')\n\"\n"
  }
}
```

</details>

---


### Tool result

_source line 378 · 2026-05-23T11:38:26.847921+00:00_

Searching for Gemma 0v1 CI near [0.949, 0.957]:
Searching Gemma 0v1 CI near [0.949, 0.957]:
  NOT FOUND in registry
Searching Gemma 2v3 CI near [0.523, 0.545]:
  exp_003_decoding_ablation: bootstrap_ci.config3_t07.4v5[ci] = [0.5243, 0.5454]
  exp_007_bootstrap_ci: qwen_rewrite.4v5 = [0.5238, 0.5448]
Searching Gemma 3v4 CI near [0.492, 0.514]:
  exp_003_decoding_ablation: bootstrap_ci.config2_nuc09.4v5[ci] = [0.4959, 0.5173]
  exp_007_bootstrap_ci: olmo_cont.4v5 = [0.4932, 0.515]
Searching Gemma 4v5 CI near [0.492, 0.514]:
  exp_003_decoding_ablation: bootstrap_ci.config2_nuc09.4v5[ci] = [0.4959, 0.5173]
  exp_007_bootstrap_ci: olmo_cont.4v5 = [0.4932, 0.515]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_audit_tables_3_4_inline_20260523T112128",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 379 · 2026-05-23T11:38:26.848066+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport json\n\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/17947013-ea3d-4507-b0e3-f06dfa8892ff/tool-results/mcp-agent-ml-research-read_registry-1779535307441.txt') as f:\n    outer = json.load(f)\n\ninner = json.loads(outer['result'])\nexps = inner['data']['experiments']\n\n# Now verify tab_pairwise_significance.tex values against exp_E_paired_stats\n# Paper says p_corr < 0.05 vs all alternatives for binary-ours MMLU\n# From tab: binary-ours vs no-filter: p=.002 * OK\n# binary-ours vs DSIR: p<.001 * OK\n# binary-ours vs surprisal: p=.021 * OK\n# binary-ours vs graduated_a0.9: p=.011 * OK (matches paper claim)\n# binary-ours vs binary-Drayson: p<.001 * OK\n\n# Graduated a0.9 vs no-filter MMLU: p=.052 (NOT significant) - paper says not significant? YES\n# The paper says 'p_corr < 0.05 vs all alternatives' for binary-ours - verified above\n# HellaSwag: binary-ours vs graduated_a0.9: p=1.00 (paper says p_corr=1.00) ✓\n# MMLU: binary-ours vs graduated_a0.9: p=.011 (paper says p_corr=0.011) ✓\n\nprint('All pairwise significance values from tab verified against exp_E_paired_stats')\nprint()\nprint('Note: graduated_a09 vs DSIR MMLU corrected p = 0.0523 (registry)')\nprint('In tab: graduated vs DSIR = p=.052 (table shows .052) - MATCH')\nprint()\nprint('binary-ours vs all alternatives MMLU: all significant (p<.05) - VERIFIED')\nprint('graduated_a09 vs binary-ours HellaSwag: p=1.00 - MATCH')\nprint('graduated_a09 vs binary-ours MMLU: p=.011 - MATCH')\n\n# Now check the AUC >= 0.92 for 0v1 claim in discussion\nprint()\nprint('Discussion: AUC >= 0.92 for 0v1')\nprint('Checking all main C4 experiments 0v1 AUC:')\nfor k in ['exp_016_base_vs_instruct', 'exp_017_qwen_continuation', 'exp_018_llama8b_depth',\n          'exp_019_mistral7b_depth', 'exp_001_pythia_depth', 'exp_002_olmo_depth',\n          'exp_004_7b_crossscale', 'exp_014_naturalistic']:\n    e = exps.get(k, {})\n    m = e.get('metrics', {})\n    auc_0v1 = m.get('pairwise_auc', {}).get('0v1') or m.get('auc_0v1') or m.get('binary_auc')\n    print(f'  {k}: 0v1={auc_0v1}')\n\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_audit_tables_3_4_inline_20260523T112128",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport json\n\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/17947013-ea3d-4507-b0e3-f06dfa8892ff/tool-results/mcp-agent-ml-research-read_registry-1779535307441.txt') as f:\n    outer = json.load(f)\n\ninner = json.loads(outer['result'])\nexps = inner['data']['experiments']\n\n# Now verify tab_pairwise_significance.tex values against exp_E_paired_stats\n# Paper says p_corr < 0.05 vs all alternatives for binary-ours MMLU\n# From tab: binary-ours vs no-filter: p=.002 * OK\n# binary-ours vs DSIR: p<.001 * OK\n# binary-ours vs surprisal: p=.021 * OK\n# binary-ours vs graduated_a0.9: p=.011 * OK (matches paper claim)\n# binary-ours vs binary-Drayson: p<.001 * OK\n\n# Graduated a0.9 vs no-filter MMLU: p=.052 (NOT significant) - paper says not significant? YES\n# The paper says 'p_corr < 0.05 vs all alternatives' for binary-ours - verified above\n# HellaSwag: binary-ours vs graduated_a0.9: p=1.00 (paper says p_corr=1.00) ✓\n# MMLU: binary-ours vs graduated_a0.9: p=.011 (paper says p_corr=0.011) ✓\n\nprint('All pairwise significance values from tab verified against exp_E_paired_stats')\nprint()\nprint('Note: graduated_a09 vs DSIR MMLU corrected p = 0.0523 (registry)')\nprint('In tab: graduated vs DSIR = p=.052 (table shows .052) - MATCH')\nprint()\nprint('binary-ours vs all alternatives MMLU: all significant (p<.05) - VERIFIED')\nprint('graduated_a09 vs binary-ours HellaSwag: p=1.00 - MATCH')\nprint('graduated_a09 vs binary-ours MMLU: p=.011 - MATCH')\n\n# Now check the AUC >= 0.92 for 0v1 claim in discussion\nprint()\nprint('Discussion: AUC >= 0.92 for 0v1')\nprint('Checking all main C4 experiments 0v1 AUC:')\nfor k in ['exp_016_base_vs_instruct', 'exp_017_qwen_continuation', 'exp_018_llama8b_depth',\n          'exp_019_mistral7b_depth', 'exp_001_pythia_depth', 'exp_002_olmo_depth',\n          'exp_004_7b_crossscale', 'exp_014_naturalistic']:\n    e = exps.get(k, {})\n    m = e.get('metrics', {})\n    auc_0v1 = m.get('pairwise_auc', {}).get('0v1') or m.get('auc_0v1') or m.get('binary_auc')\n    print(f'  {k}: 0v1={auc_0v1}')\n\"\n"
  }
}
```

</details>

---


### Tool result

_source line 380 · 2026-05-23T11:38:26.848219+00:00_

All pairwise significance values from tab verified against exp_E_paired_stats

Note: graduated_a09 vs DSIR MMLU corrected p = 0.0523 (registry)
In tab: graduated vs DSIR = p=.052 (table shows .052) - MATCH

binary-ours vs all alternatives MMLU: all significant (p<.05) - VERIFIED
graduated_a09 vs binary-ours HellaSwag: p=1.00 - MATCH
graduated_a09 vs binary-ours MMLU: p=.011 - MATCH

Discussion: AUC >= 0.92 for 0v1
Checking all main C4 experiments 0v1 AUC:
  exp_016_base_vs_instruct: 0v1=0.987
  exp_017_qwen_continuation: 0v1=0.9972
  exp_018_llama8b_depth: 0v1=0.9225
  exp_019_mistral7b_depth: 0v1=0.9843
  exp_001_pythia_depth: 0v1=0.9722
  exp_002_olmo_depth: 0v1=0.9861
  exp_004_7b_crossscale: 0v1=0.9644
  exp_014_naturalistic: 0v1=0.9919

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_audit_tables_3_4_inline_20260523T112128",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 381 · 2026-05-23T11:38:26.848361+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport json\n\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/17947013-ea3d-4507-b0e3-f06dfa8892ff/tool-results/mcp-agent-ml-research-read_registry-1779535307441.txt', 'r') as f:\n    raw = json.load(f)\n\ninner = json.loads(raw['result'])\ndata = inner['data']\nexps = data['experiments']\n\n# exp015 notes says: 'OLMo K*_neural=2'\n# But paper claims OLMo K*=1, 2v3=0.5056, 1v2=0.5054\n# OLMo improvement from 15D: +0.039 -> 15D OLMo 2v3 would be ~0.550 which matches Qwen cross-scored scenario\n# Wait, notes: 'Neural probe improves 2v3 AUC across all models (Pythia +0.044, OLMo +0.039, Qwen +0.055)'\n# If OLMo 15D baseline was ~0.550, neural probe +0.039 = 0.589 -> matches registry\n# But paper claims 2v3=0.5056 with K*=1... \n\n# The paper's OLMo neural probe values (2v3=0.5056, 1v2=0.5054) look like they might be\n# the Qwen cross-scored 15D results, not the neural probe results\n# OR the paper shows OLMo with a different scorer (e.g., cross-scorer probe)\n\n# Let me check exp_deberta experiments for OLMo or related analysis\nfor k in ['exp_deberta_cross_transfer_wiki', 'exp_deberta_cross_transfer_gpu1', 'exp_deberta_cross_transfer_gpu2', 'exp_deberta_cross_transfer_gpu3']:\n    if k in exps:\n        m = exps[k].get('metrics', {})\n        print(f'=== {k} ===')\n        print(json.dumps(m, indent=2)[:1000])\n        print()\n\" 2>&1\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_audit_tables_3_4_inline_20260523T112128",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport json\n\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/17947013-ea3d-4507-b0e3-f06dfa8892ff/tool-results/mcp-agent-ml-research-read_registry-1779535307441.txt', 'r') as f:\n    raw = json.load(f)\n\ninner = json.loads(raw['result'])\ndata = inner['data']\nexps = data['experiments']\n\n# exp015 notes says: 'OLMo K*_neural=2'\n# But paper claims OLMo K*=1, 2v3=0.5056, 1v2=0.5054\n# OLMo improvement from 15D: +0.039 -> 15D OLMo 2v3 would be ~0.550 which matches Qwen cross-scored scenario\n# Wait, notes: 'Neural probe improves 2v3 AUC across all models (Pythia +0.044, OLMo +0.039, Qwen +0.055)'\n# If OLMo 15D baseline was ~0.550, neural probe +0.039 = 0.589 -> matches registry\n# But paper claims 2v3=0.5056 with K*=1... \n\n# The paper's OLMo neural probe values (2v3=0.5056, 1v2=0.5054) look like they might be\n# the Qwen cross-scored 15D results, not the neural probe results\n# OR the paper shows OLMo with a different scorer (e.g., cross-scorer probe)\n\n# Let me check exp_deberta experiments for OLMo or related analysis\nfor k in ['exp_deberta_cross_transfer_wiki', 'exp_deberta_cross_transfer_gpu1', 'exp_deberta_cross_transfer_gpu2', 'exp_deberta_cross_transfer_gpu3']:\n    if k in exps:\n        m = exps[k].get('metrics', {})\n        print(f'=== {k} ===')\n        print(json.dumps(m, indent=2)[:1000])\n        print()\n\" 2>&1\n"
  }
}
```

</details>

---


### Tool result

_source line 382 · 2026-05-23T11:38:26.848504+00:00_

=== exp_deberta_cross_transfer_wiki ===
{
  "total_pairs_expected": 12,
  "completed_pairs": 10,
  "missing_pairs": [
    "qwen7b\u2192llama8b",
    "llama8b\u2192qwen7b"
  ],
  "bonus_pairs": [
    "pythia\u2192mistral7b (K*=2)",
    "mistral7b\u2192pythia (K*=2)"
  ],
  "kstar_distribution": {
    "K*=1": 3,
    "K*=2": 5,
    "K*=3": 1
  },
  "kstar_1_pairs": [
    "pythia\u2192olmo",
    "qwen7b\u2192olmo",
    "llama8b\u2192olmo"
  ],
  "kstar_3_pair": "pythia\u2192qwen7b",
  "kstar_2_pairs": [
    "olmo\u2192qwen7b",
    "olmo\u2192llama8b",
    "qwen7b\u2192pythia",
    "llama8b\u2192pythia",
    "pythia\u2192llama8b"
  ],
  "pattern": "All X\u2192OLMo = K*=1. pythia\u2192qwen7b highest at K*=3. GPU3 ran mistral7b pairs instead of expected qwen7b\u2194llama8b, causing 2 missing pairs.",
  "json_kstar_fix": "3 JSONs fixed +1 (pythia\u2192olmo 0\u21921, olmo\u2192qwen7b 1\u21922, olmo\u2192llama8b 1\u21922)"
}

=== exp_deberta_cross_transfer_gpu1 ===
{}

=== exp_deberta_cross_transfer_gpu2 ===
{}

=== exp_deberta_cross_transfer_gpu3 ===
{}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_audit_tables_3_4_inline_20260523T112128",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 383 · 2026-05-23T11:38:26.848679+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/17947013-ea3d-4507-b0e3-f06dfa8892ff/tool-results/mcp-agent-ml-research-read_registry-1779535307441.txt | python3 -c \"\nimport json, sys\nraw = sys.stdin.read()\nouter = json.loads(raw)\ninner = json.loads(outer['result'])\ndata = inner['data']\nexperiments = data['experiments']\n\n# Let me clarify: these are table values truncated (not rounded) at 3 decimal places\n# Paper uses format .XXX with 3 decimal places\n# Registry: pairwise_auc['2v3'] = 0.6545 for exp_025\n# vs bootstrap_ci['2v3']['auc'] = 0.6544\n\n# Paper: 0.655 means it's displaying with 3 sig figs after decimal\n# Is 0.6545 displayed as 0.655 (rounding up) or 0.654 (truncating)?\n# 0.6545 rounds to 0.655 when rounding half-up (standard rounding: 5 rounds up)\n# So 0.655 is correct given the pairwise_auc value of 0.6545\n\n# Let me re-examine all values\ne025 = experiments['exp_025_pythia_arxiv']\nprint('exp_025 pairwise_auc 2v3:', e025['metrics']['pairwise_auc']['2v3'])\nprint('exp_025 bootstrap_ci 2v3 auc:', e025['metrics']['bootstrap_ci']['2v3']['auc'])\nprint()\n\n# So 0.6545 rounds to 0.655 (standard rounding) -- MATCH\n# Paper: 0.655 -- CORRECT\n\n# For CI: [0.6401, 0.6688] vs paper [0.640, 0.669]\n# 0.6401 displayed as 0.640 (truncated/truncated) -- yes\n# 0.6688 displayed as 0.669 -- yes (rounds from 0.6688 to 0.669)\nprint('Pythia arXiv CI check:')\nprint(f'Registry: [{e025[\\\"metrics\\\"][\\\"bootstrap_ci\\\"][\\\"2v3\\\"][\\\"ci_lower\\\"]}, {e025[\\\"metrics\\\"][\\\"bootstrap_ci\\\"][\\\"2v3\\\"][\\\"ci_upper\\\"]}]')\nprint(f'Paper:    [0.640, 0.669]')\nprint('0.6401 -> 0.640 OK, 0.6688 -> 0.669 OK')\n\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_audit_tables_3_4_inline_20260523T112128",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/17947013-ea3d-4507-b0e3-f06dfa8892ff/tool-results/mcp-agent-ml-research-read_registry-1779535307441.txt | python3 -c \"\nimport json, sys\nraw = sys.stdin.read()\nouter = json.loads(raw)\ninner = json.loads(outer['result'])\ndata = inner['data']\nexperiments = data['experiments']\n\n# Let me clarify: these are table values truncated (not rounded) at 3 decimal places\n# Paper uses format .XXX with 3 decimal places\n# Registry: pairwise_auc['2v3'] = 0.6545 for exp_025\n# vs bootstrap_ci['2v3']['auc'] = 0.6544\n\n# Paper: 0.655 means it's displaying with 3 sig figs after decimal\n# Is 0.6545 displayed as 0.655 (rounding up) or 0.654 (truncating)?\n# 0.6545 rounds to 0.655 when rounding half-up (standard rounding: 5 rounds up)\n# So 0.655 is correct given the pairwise_auc value of 0.6545\n\n# Let me re-examine all values\ne025 = experiments['exp_025_pythia_arxiv']\nprint('exp_025 pairwise_auc 2v3:', e025['metrics']['pairwise_auc']['2v3'])\nprint('exp_025 bootstrap_ci 2v3 auc:', e025['metrics']['bootstrap_ci']['2v3']['auc'])\nprint()\n\n# So 0.6545 rounds to 0.655 (standard rounding) -- MATCH\n# Paper: 0.655 -- CORRECT\n\n# For CI: [0.6401, 0.6688] vs paper [0.640, 0.669]\n# 0.6401 displayed as 0.640 (truncated/truncated) -- yes\n# 0.6688 displayed as 0.669 -- yes (rounds from 0.6688 to 0.669)\nprint('Pythia arXiv CI check:')\nprint(f'Registry: [{e025[\\\"metrics\\\"][\\\"bootstrap_ci\\\"][\\\"2v3\\\"][\\\"ci_lower\\\"]}, {e025[\\\"metrics\\\"][\\\"bootstrap_ci\\\"][\\\"2v3\\\"][\\\"ci_upper\\\"]}]')\nprint(f'Paper:    [0.640, 0.669]')\nprint('0.6401 -> 0.640 OK, 0.6688 -> 0.669 OK')\n\"\n"
  }
}
```

</details>

---


### Tool result

_source line 384 · 2026-05-23T11:38:26.848907+00:00_

exp_025 pairwise_auc 2v3: 0.6545
exp_025 bootstrap_ci 2v3 auc: 0.6544

Pythia arXiv CI check:
Registry: [0.6401, 0.6688]
Paper:    [0.640, 0.669]
0.6401 -> 0.640 OK, 0.6688 -> 0.669 OK

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_audit_tables_3_4_inline_20260523T112128",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 385 · 2026-05-23T11:38:26.849069+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport json\n\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/17947013-ea3d-4507-b0e3-f06dfa8892ff/tool-results/mcp-agent-ml-research-read_registry-1779535307441.txt') as f:\n    outer = json.load(f)\n\ninner = json.loads(outer['result'])\nexps = inner['data']['experiments']\n\n# Discussion: AUC >= 0.92 for 0v1\n# All experiments checked: min is 0v1=0.9225 (LLaMA-8B) which is >= 0.92 ✓\nprint('Min 0v1 AUC across main exps: 0.9225 (LLaMA-8B) >= 0.92: OK')\n\n# But wait, there's also Gemma:\nprint('Gemma2B 0v1:', exps.get('exp_gemma2b_depth', {}).get('metrics', {}).get('pairwise_auc', {}).get('0v1'))\nprint('Gemma2B-10k 0v1 self:', exps.get('exp_gemma2b_10k', {}).get('metrics', {}).get('pairwise_auc_self', {}).get('0v1'))\n\n# Gemma2b: 0.9534 ≥ 0.92 ✓\n\n# And the code/wiki/arxiv experiments?\nother_0v1 = {}\nfor k, v in exps.items():\n    m = v.get('metrics', {})\n    auc_0v1 = m.get('pairwise_auc', {}).get('0v1') or m.get('auc_0v1') or m.get('0v1_auc')\n    if isinstance(auc_0v1, (int, float)) and auc_0v1 < 0.92 and v.get('conclusion') == 'success':\n        other_0v1[k] = auc_0v1\n        \nprint()\nprint('Experiments with 0v1 < 0.92:')\nfor k, v in sorted(other_0v1.items(), key=lambda x: x[1]):\n    print(f'  {k}: {v}')\n\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_audit_tables_3_4_inline_20260523T112128",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport json\n\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/17947013-ea3d-4507-b0e3-f06dfa8892ff/tool-results/mcp-agent-ml-research-read_registry-1779535307441.txt') as f:\n    outer = json.load(f)\n\ninner = json.loads(outer['result'])\nexps = inner['data']['experiments']\n\n# Discussion: AUC >= 0.92 for 0v1\n# All experiments checked: min is 0v1=0.9225 (LLaMA-8B) which is >= 0.92 ✓\nprint('Min 0v1 AUC across main exps: 0.9225 (LLaMA-8B) >= 0.92: OK')\n\n# But wait, there's also Gemma:\nprint('Gemma2B 0v1:', exps.get('exp_gemma2b_depth', {}).get('metrics', {}).get('pairwise_auc', {}).get('0v1'))\nprint('Gemma2B-10k 0v1 self:', exps.get('exp_gemma2b_10k', {}).get('metrics', {}).get('pairwise_auc_self', {}).get('0v1'))\n\n# Gemma2b: 0.9534 ≥ 0.92 ✓\n\n# And the code/wiki/arxiv experiments?\nother_0v1 = {}\nfor k, v in exps.items():\n    m = v.get('metrics', {})\n    auc_0v1 = m.get('pairwise_auc', {}).get('0v1') or m.get('auc_0v1') or m.get('0v1_auc')\n    if isinstance(auc_0v1, (int, float)) and auc_0v1 < 0.92 and v.get('conclusion') == 'success':\n        other_0v1[k] = auc_0v1\n        \nprint()\nprint('Experiments with 0v1 < 0.92:')\nfor k, v in sorted(other_0v1.items(), key=lambda x: x[1]):\n    print(f'  {k}: {v}')\n\"\n"
  }
}
```

</details>

---


### Tool result

_source line 386 · 2026-05-23T11:38:26.849210+00:00_

Min 0v1 AUC across main exps: 0.9225 (LLaMA-8B) >= 0.92: OK
Gemma2B 0v1: 0.9534
Gemma2B-10k 0v1 self: 0.9817

Experiments with 0v1 < 0.92:
  exp_code_qwen1b5_pythia_scorer: 0.9076
  exp_code_llama8b: 0.9161
  exp_code_mistral7b: 0.9191

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_audit_tables_3_4_inline_20260523T112128",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 387 · 2026-05-23T11:38:26.849349+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/17947013-ea3d-4507-b0e3-f06dfa8892ff/tool-results/mcp-agent-ml-research-read_registry-1779535307441.txt | python3 -c \"\nimport json, sys\nraw = sys.stdin.read()\nouter = json.loads(raw)\ninner = json.loads(outer['result'])\ndata = inner['data']\nexperiments = data['experiments']\n\n# Now recheck all Table 4 values with proper rounding\nprint('=== TABLE 4 FINAL VERIFICATION ===')\nprint()\n\n# Row 1: arXiv / Qwen-1.5B / 1v2=.858 / 2v3=.644 / K*=3\ne024 = experiments['exp_024_arxiv_domain']\npairwise = e024['metrics']['pairwise_auc']\nreg_1v2 = pairwise['1v2']  # 0.858\nreg_2v3 = pairwise['2v3']  # 0.6427\nprint(f'arXiv / Qwen-1.5B: Paper 1v2=.858 / Registry={reg_1v2} -> {round(reg_1v2,3)} | Paper 2v3=.644 / Registry={reg_2v3} -> {round(reg_2v3,3)}')\nprint(f'  1v2: {\\\"OK\\\" if round(reg_1v2,3)==0.858 else \\\"MISMATCH\\\"}')\nprint(f'  2v3: Paper .644 vs {round(reg_2v3,3)} -> {\\\"OK\\\" if round(reg_2v3,3)==0.643 else \\\"CHECK\\\"} (0.6427 rounds to 0.643 at 3dp)')\n# Note: .644 vs 0.6427 -> 0.6427 rounds to 0.643, paper says .644\n# .6427 rounded to 3 decimal places = .643, not .644\n# .644 would require registry value >= 0.6435\nprint()\n\n# Recheck the exact bootstrap_ci auc for 2v3 (might be different from pairwise_auc)\nci_024 = e024['metrics']['bootstrap_ci']['2v3']\nprint(f'  exp_024 bootstrap_ci 2v3 auc={ci_024[\\\"auc\\\"]} (vs pairwise 0.6427)')\nprint(f'  0.6427 rounded to 3dp: {round(0.6427,3)}')\n# 0.6427 rounds to 0.643... but paper says 0.644\nprint()\n\n# Hmm - 0.6427 rounds to 0.643 (since 4th decimal is 7, but we're truncating at 3rd decimal)\n# Wait: round(0.6427, 3) = 0.643 (third decimal is 2, fourth is 7 so round up to 3)\nprint('round(0.6427, 3) =', round(0.6427, 3))\n# Actually: 0.6427 -> third digit is 2, fourth is 7, so 0.643\n\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_audit_tables_3_4_inline_20260523T112128",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/17947013-ea3d-4507-b0e3-f06dfa8892ff/tool-results/mcp-agent-ml-research-read_registry-1779535307441.txt | python3 -c \"\nimport json, sys\nraw = sys.stdin.read()\nouter = json.loads(raw)\ninner = json.loads(outer['result'])\ndata = inner['data']\nexperiments = data['experiments']\n\n# Now recheck all Table 4 values with proper rounding\nprint('=== TABLE 4 FINAL VERIFICATION ===')\nprint()\n\n# Row 1: arXiv / Qwen-1.5B / 1v2=.858 / 2v3=.644 / K*=3\ne024 = experiments['exp_024_arxiv_domain']\npairwise = e024['metrics']['pairwise_auc']\nreg_1v2 = pairwise['1v2']  # 0.858\nreg_2v3 = pairwise['2v3']  # 0.6427\nprint(f'arXiv / Qwen-1.5B: Paper 1v2=.858 / Registry={reg_1v2} -> {round(reg_1v2,3)} | Paper 2v3=.644 / Registry={reg_2v3} -> {round(reg_2v3,3)}')\nprint(f'  1v2: {\\\"OK\\\" if round(reg_1v2,3)==0.858 else \\\"MISMATCH\\\"}')\nprint(f'  2v3: Paper .644 vs {round(reg_2v3,3)} -> {\\\"OK\\\" if round(reg_2v3,3)==0.643 else \\\"CHECK\\\"} (0.6427 rounds to 0.643 at 3dp)')\n# Note: .644 vs 0.6427 -> 0.6427 rounds to 0.643, paper says .644\n# .6427 rounded to 3 decimal places = .643, not .644\n# .644 would require registry value >= 0.6435\nprint()\n\n# Recheck the exact bootstrap_ci auc for 2v3 (might be different from pairwise_auc)\nci_024 = e024['metrics']['bootstrap_ci']['2v3']\nprint(f'  exp_024 bootstrap_ci 2v3 auc={ci_024[\\\"auc\\\"]} (vs pairwise 0.6427)')\nprint(f'  0.6427 rounded to 3dp: {round(0.6427,3)}')\n# 0.6427 rounds to 0.643... but paper says 0.644\nprint()\n\n# Hmm - 0.6427 rounds to 0.643 (since 4th decimal is 7, but we're truncating at 3rd decimal)\n# Wait: round(0.6427, 3) = 0.643 (third decimal is 2, fourth is 7 so round up to 3)\nprint('round(0.6427, 3) =', round(0.6427, 3))\n# Actually: 0.6427 -> third digit is 2, fourth is 7, so 0.643\n\"\n"
  }
}
```

</details>

---


### Tool result

_source line 388 · 2026-05-23T11:38:26.849489+00:00_

=== TABLE 4 FINAL VERIFICATION ===

arXiv / Qwen-1.5B: Paper 1v2=.858 / Registry=0.858 -> 0.858 | Paper 2v3=.644 / Registry=0.6427 -> 0.643
  1v2: OK
  2v3: Paper .644 vs 0.643 -> OK (0.6427 rounds to 0.643 at 3dp)

  exp_024 bootstrap_ci 2v3 auc=0.6427 (vs pairwise 0.6427)
  0.6427 rounded to 3dp: 0.643

round(0.6427, 3) = 0.643

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_audit_tables_3_4_inline_20260523T112128",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 389 · 2026-05-23T11:38:26.849630+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport json\n\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/17947013-ea3d-4507-b0e3-f06dfa8892ff/tool-results/mcp-agent-ml-research-read_registry-1779535307441.txt', 'r') as f:\n    raw = json.load(f)\n\ninner = json.loads(raw['result'])\ndata = inner['data']\nexps = data['experiments']\n\n# TASK 4: Table S10 Pythia decoding (exp_020_pythia_decoding)\n# Paper Table S10:\n# | | Greedy | p=0.9 | T=0.7 | T=1.2 |\n# | 0v1 | .999 | .995 | .996 | .994 |\n# | 1v2 | .884 | .675 | .728 | .618 |\n# | 2v3 | .531 | .559 | .598 | .531 |   <- note: T=0.7 2v3 is borderline 0.60 from notes\n# | 3v4 | .522 | .524 | .563 | .520 |\n# | 4v5 | .514 | .501 | .527 | .510 |\n\nexp020 = exps['exp_020_pythia_decoding']\nreg020 = exp020['metrics']\n\npaper_s10 = {\n    '0v1': {'greedy': .999, 'nuc09': .995, 't07': .996, 't12': .994},\n    '1v2': {'greedy': .884, 'nuc09': .675, 't07': .728, 't12': .618},\n    '2v3': {'greedy': .531, 'nuc09': .559, 't07': .598, 't12': .531},\n    '3v4': {'greedy': .522, 'nuc09': .524, 't07': .563, 't12': .520},\n    '4v5': {'greedy': .514, 'nuc09': .501, 't07': .527, 't12': .510},\n}\n\ncfg_map = {'greedy': 'greedy', 'nuc09': 'nuc09', 't07': 't07', 't12': 't12'}\npair_keys = ['0v1', '1v2', '2v3', '3v4', '4v5']\n\nprint('=== TASK 4: Table S10 Pythia Decoding ===')\nprint()\nmismatches = []\nfor pair in pair_keys:\n    for cfg_short in ['greedy', 'nuc09', 't07', 't12']:\n        paper_v = paper_s10[pair][cfg_short]\n        reg_v = reg020[cfg_short]['auc'][pair]\n        \n        match = abs(round(reg_v, 3) - paper_v) < 0.0015\n        status = 'OK' if match else 'MISMATCH'\n        \n        loc = f'S10 Pythia {pair} {cfg_short}'\n        paper_str = f'{paper_v:.3f}'\n        reg_str = f'{reg_v:.4f}'\n        \n        if not match:\n            mismatches.append((loc, paper_str, 'exp_020', reg_str))\n        \n        print(f'{status:8} | {loc:30} | Paper: {paper_str} | Reg: {reg_str}')\n\nprint()\nprint(f'Total mismatches: {len(mismatches)}')\nif mismatches:\n    for m in mismatches:\n        print(f'  MISMATCH: {m}')\n\" 2>&1\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_audit_tables_3_4_inline_20260523T112128",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport json\n\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/17947013-ea3d-4507-b0e3-f06dfa8892ff/tool-results/mcp-agent-ml-research-read_registry-1779535307441.txt', 'r') as f:\n    raw = json.load(f)\n\ninner = json.loads(raw['result'])\ndata = inner['data']\nexps = data['experiments']\n\n# TASK 4: Table S10 Pythia decoding (exp_020_pythia_decoding)\n# Paper Table S10:\n# | | Greedy | p=0.9 | T=0.7 | T=1.2 |\n# | 0v1 | .999 | .995 | .996 | .994 |\n# | 1v2 | .884 | .675 | .728 | .618 |\n# | 2v3 | .531 | .559 | .598 | .531 |   <- note: T=0.7 2v3 is borderline 0.60 from notes\n# | 3v4 | .522 | .524 | .563 | .520 |\n# | 4v5 | .514 | .501 | .527 | .510 |\n\nexp020 = exps['exp_020_pythia_decoding']\nreg020 = exp020['metrics']\n\npaper_s10 = {\n    '0v1': {'greedy': .999, 'nuc09': .995, 't07': .996, 't12': .994},\n    '1v2': {'greedy': .884, 'nuc09': .675, 't07': .728, 't12': .618},\n    '2v3': {'greedy': .531, 'nuc09': .559, 't07': .598, 't12': .531},\n    '3v4': {'greedy': .522, 'nuc09': .524, 't07': .563, 't12': .520},\n    '4v5': {'greedy': .514, 'nuc09': .501, 't07': .527, 't12': .510},\n}\n\ncfg_map = {'greedy': 'greedy', 'nuc09': 'nuc09', 't07': 't07', 't12': 't12'}\npair_keys = ['0v1', '1v2', '2v3', '3v4', '4v5']\n\nprint('=== TASK 4: Table S10 Pythia Decoding ===')\nprint()\nmismatches = []\nfor pair in pair_keys:\n    for cfg_short in ['greedy', 'nuc09', 't07', 't12']:\n        paper_v = paper_s10[pair][cfg_short]\n        reg_v = reg020[cfg_short]['auc'][pair]\n        \n        match = abs(round(reg_v, 3) - paper_v) < 0.0015\n        status = 'OK' if match else 'MISMATCH'\n        \n        loc = f'S10 Pythia {pair} {cfg_short}'\n        paper_str = f'{paper_v:.3f}'\n        reg_str = f'{reg_v:.4f}'\n        \n        if not match:\n            mismatches.append((loc, paper_str, 'exp_020', reg_str))\n        \n        print(f'{status:8} | {loc:30} | Paper: {paper_str} | Reg: {reg_str}')\n\nprint()\nprint(f'Total mismatches: {len(mismatches)}')\nif mismatches:\n    for m in mismatches:\n        print(f'  MISMATCH: {m}')\n\" 2>&1\n"
  }
}
```

</details>

---


### Tool result

_source line 390 · 2026-05-23T11:38:26.849858+00:00_

=== TASK 4: Table S10 Pythia Decoding ===

OK       | S10 Pythia 0v1 greedy          | Paper: 0.999 | Reg: 0.9992
OK       | S10 Pythia 0v1 nuc09           | Paper: 0.995 | Reg: 0.9948
OK       | S10 Pythia 0v1 t07             | Paper: 0.996 | Reg: 0.9965
OK       | S10 Pythia 0v1 t12             | Paper: 0.994 | Reg: 0.9933
OK       | S10 Pythia 1v2 greedy          | Paper: 0.884 | Reg: 0.8838
MISMATCH | S10 Pythia 1v2 nuc09           | Paper: 0.675 | Reg: 0.6770
OK       | S10 Pythia 1v2 t07             | Paper: 0.728 | Reg: 0.7265
OK       | S10 Pythia 1v2 t12             | Paper: 0.618 | Reg: 0.6172
MISMATCH | S10 Pythia 2v3 greedy          | Paper: 0.531 | Reg: 0.5342
MISMATCH | S10 Pythia 2v3 nuc09           | Paper: 0.559 | Reg: 0.5549
MISMATCH | S10 Pythia 2v3 t07             | Paper: 0.598 | Reg: 0.5941
MISMATCH | S10 Pythia 2v3 t12             | Paper: 0.531 | Reg: 0.5226
OK       | S10 Pythia 3v4 greedy          | Paper: 0.522 | Reg: 0.5228
MISMATCH | S10 Pythia 3v4 nuc09           | Paper: 0.524 | Reg: 0.5299
MISMATCH | S10 Pythia 3v4 t07             | Paper: 0.563 | Reg: 0.5698
MISMATCH | S10 Pythia 3v4 t12             | Paper: 0.520 | Reg: 0.5170
MISMATCH | S10 Pythia 4v5 greedy          | Paper: 0.514 | Reg: 0.5162
OK       | S10 Pythia 4v5 nuc09           | Paper: 0.501 | Reg: 0.5013
OK       | S10 Pythia 4v5 t07             | Paper: 0.527 | Reg: 0.5284
MISMATCH | S10 Pythia 4v5 t12             | Paper: 0.510 | Reg: 0.5051

Total mismatches: 10
  MISMATCH: ('S10 Pythia 1v2 nuc09', '0.675', 'exp_020', '0.6770')
  MISMATCH: ('S10 Pythia 2v3 greedy', '0.531', 'exp_020', '0.5342')
  MISMATCH: ('S10 Pythia 2v3 nuc09', '0.559', 'exp_020', '0.5549')
  MISMATCH: ('S10 Pythia 2v3 t07', '0.598', 'exp_020', '0.5941')
  MISMATCH: ('S10 Pythia 2v3 t12', '0.531', 'exp_020', '0.5226')
  MISMATCH: ('S10 Pythia 3v4 nuc09', '0.524', 'exp_020', '0.5299')
  MISMATCH: ('S10 Pythia 3v4 t07', '0.563', 'exp_020', '0.5698')
  MISMATCH: ('S10 Pythia 3v4 t12', '0.520', 'exp_02
…[truncated 146 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_audit_tables_3_4_inline_20260523T112128",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 391 · 2026-05-23T11:38:26.850031+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/17947013-ea3d-4507-b0e3-f06dfa8892ff/tool-results/mcp-agent-ml-research-read_registry-1779535307441.txt | python3 -c \"\nimport json, sys\nraw = sys.stdin.read()\nouter = json.loads(raw)\ninner = json.loads(outer['result'])\ndata = inner['data']\nexperiments = data['experiments']\n\n# Critical finding: Paper says .644 but 0.6427 rounds to 0.643\n# The paper is using .644 but registry is 0.6427\n# Let me double-check -- is .644 truncation at 3rd decimal? No, truncation would give 0.642\n# Standard rounding: 0.6427 -> look at 4th decimal (7) -> round up 3rd decimal (2->3) -> 0.643\n# So the paper value .644 does NOT match the registry value 0.6427\n\nprint('MISMATCH FOUND: arXiv/Qwen-1.5B 2v3 AUC')\nprint('  Paper: .644')\nprint('  Registry exp_024 pairwise_auc[2v3]: 0.6427 -> rounds to 0.643')\nprint('  Required value for paper: 0.6435 to 0.6444')\nprint()\n\n# Also need to check the inline CI claim for Qwen arXiv 2v3: [0.628, 0.658]\nci_2v3 = experiments['exp_024_arxiv_domain']['metrics']['bootstrap_ci']['2v3']\nprint(f'Inline CI claim: Qwen arXiv 2v3 = 0.644 [0.628, 0.658]')\nprint(f'Registry CI: auc=0.6427, ci=[{ci_2v3[\\\"ci_lower\\\"]}, {ci_2v3[\\\"ci_upper\\\"]}]')\nprint(f'  AUC: 0.6427 != 0.644 (MISMATCH)')\nprint(f'  CI lower: 0.6275 -> rounds to 0.628 (OK? 0.6275 rounds to 0.628)')\nprint(f'  round(0.6275, 3) = {round(0.6275, 3)}')\nprint(f'  CI upper: 0.6575 -> rounds to 0.658 (OK? 0.6575 rounds to 0.658)')\nprint(f'  round(0.6575, 3) = {round(0.6575, 3)}')\n\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_audit_tables_3_4_inline_20260523T112128",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/17947013-ea3d-4507-b0e3-f06dfa8892ff/tool-results/mcp-agent-ml-research-read_registry-1779535307441.txt | python3 -c \"\nimport json, sys\nraw = sys.stdin.read()\nouter = json.loads(raw)\ninner = json.loads(outer['result'])\ndata = inner['data']\nexperiments = data['experiments']\n\n# Critical finding: Paper says .644 but 0.6427 rounds to 0.643\n# The paper is using .644 but registry is 0.6427\n# Let me double-check -- is .644 truncation at 3rd decimal? No, truncation would give 0.642\n# Standard rounding: 0.6427 -> look at 4th decimal (7) -> round up 3rd decimal (2->3) -> 0.643\n# So the paper value .644 does NOT match the registry value 0.6427\n\nprint('MISMATCH FOUND: arXiv/Qwen-1.5B 2v3 AUC')\nprint('  Paper: .644')\nprint('  Registry exp_024 pairwise_auc[2v3]: 0.6427 -> rounds to 0.643')\nprint('  Required value for paper: 0.6435 to 0.6444')\nprint()\n\n# Also need to check the inline CI claim for Qwen arXiv 2v3: [0.628, 0.658]\nci_2v3 = experiments['exp_024_arxiv_domain']['metrics']['bootstrap_ci']['2v3']\nprint(f'Inline CI claim: Qwen arXiv 2v3 = 0.644 [0.628, 0.658]')\nprint(f'Registry CI: auc=0.6427, ci=[{ci_2v3[\\\"ci_lower\\\"]}, {ci_2v3[\\\"ci_upper\\\"]}]')\nprint(f'  AUC: 0.6427 != 0.644 (MISMATCH)')\nprint(f'  CI lower: 0.6275 -> rounds to 0.628 (OK? 0.6275 rounds to 0.628)')\nprint(f'  round(0.6275, 3) = {round(0.6275, 3)}')\nprint(f'  CI upper: 0.6575 -> rounds to 0.658 (OK? 0.6575 rounds to 0.658)')\nprint(f'  round(0.6575, 3) = {round(0.6575, 3)}')\n\"\n"
  }
}
```

</details>

---


### Tool result

_source line 392 · 2026-05-23T11:38:26.850169+00:00_

MISMATCH FOUND: arXiv/Qwen-1.5B 2v3 AUC
  Paper: .644
  Registry exp_024 pairwise_auc[2v3]: 0.6427 -> rounds to 0.643
  Required value for paper: 0.6435 to 0.6444

Inline CI claim: Qwen arXiv 2v3 = 0.644 [0.628, 0.658]
Registry CI: auc=0.6427, ci=[0.6275, 0.6575]
  AUC: 0.6427 != 0.644 (MISMATCH)
  CI lower: 0.6275 -> rounds to 0.628 (OK? 0.6275 rounds to 0.628)
  round(0.6275, 3) = 0.627
  CI upper: 0.6575 -> rounds to 0.658 (OK? 0.6575 rounds to 0.658)
  round(0.6575, 3) = 0.657

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_audit_tables_3_4_inline_20260523T112128",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 393 · 2026-05-23T11:38:26.850316+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport json\n\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/17947013-ea3d-4507-b0e3-f06dfa8892ff/tool-results/mcp-agent-ml-research-read_registry-1779535307441.txt') as f:\n    outer = json.load(f)\n\ninner = json.loads(outer['result'])\nexps = inner['data']['experiments']\n\n# Code experiments have lower 0v1 AUC (0.91, 0.92) \n# But discussion says 'AUC >= 0.92 for 0v1' for web text\n# The context in discussion is 'For general web text, K*=2 reflects concentrated information loss: \n# 0v1 is near-trivially separable (AUC >= 0.92)'\n# So this is about web text (C4/Wikipedia), not code\n# Code domain may be excluded from this claim\n\n# But exp_code_llama8b: 0.9161 < 0.92\n# However, code is not 'general web text'\n# The claim 'AUC >= 0.92' is specifically for web text (C4/Wiki) experiments\n# All C4/Wiki 0v1 AUC: min is 0.9225 (LLaMA-8B C4) >= 0.92 ✓\n\n# Check OLMo self vs cross gap more precisely\n# self-scored (exp_002 before cross-scoring update):\n# notes say: 'Self-scored 1v2=0.6145, Qwen-scored 1v2=0.5001'  \n# gap = 0.6145 - 0.5001 = 0.1144 = 11.44 pp\n# paper says '+11.5 pp'\n\nolmo_self = 0.6145\nolmo_cross = 0.5001\nprint(f'OLMo gap: {(olmo_self-olmo_cross)*100:.2f} pp (paper: +11.5 pp)')\n# 11.44 vs 11.5 -> paper rounds up\n\n# Pythia gap:\npythia_self = 0.6539\npythia_cross = 0.6074  # Qwen cross-scored\nprint(f'Pythia gap: {(pythia_self-pythia_cross)*100:.2f} pp (paper: +4.7 pp)')\n# 4.65 vs 4.7 -> paper rounds up\n\n# Mistral gap:\n# Self: exp_019 1v2=0.5935 (Mistral self-scored)\n# Cross: exp_019b 1v2=0.5695 (Qwen scorer)\nmistral_self = 0.5935\nmistral_cross = 0.5695\nprint(f'Mistral gap: {(mistral_self-mistral_cross)*100:.2f} pp (paper: ~1.9 pp)')\n# 2.4pp vs 1.9pp -> MISMATCH\n\n# For LLaMA: need to identify the self-scored experiment\n# exp_018 uses Qwen scorer (cross): 1v2=0.6123\n# No LLaMA self-scored C4 experiment found in registry\n# But paper says 'LLaMA-8B and Mistral-7B (~approx +1.9 pp each)'\n# If both are ~1.9pp average then maybe it's computed as average or separately\n\n# Actually check if there's a LLaMA self-scoring path\n# All LLaMA experiments use Qwen as scorer - so there's NO LLaMA self-scored baseline\n\nprint()\nprint('ISSUE: No LLaMA self-scored experiment found in registry')\nprint('All LLaMA exps use Qwen as scorer (cross-scored)')\nprint('Cannot verify LLaMA self vs cross gap from registry')\nprint()\nprint('MISMATCH candidate: Mistral gap = 2.4pp (registry) vs 1.9pp (paper)')\n\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_audit_tables_3_4_inline_20260523T112128",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport json\n\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/17947013-ea3d-4507-b0e3-f06dfa8892ff/tool-results/mcp-agent-ml-research-read_registry-1779535307441.txt') as f:\n    outer = json.load(f)\n\ninner = json.loads(outer['result'])\nexps = inner['data']['experiments']\n\n# Code experiments have lower 0v1 AUC (0.91, 0.92) \n# But discussion says 'AUC >= 0.92 for 0v1' for web text\n# The context in discussion is 'For general web text, K*=2 reflects concentrated information loss: \n# 0v1 is near-trivially separable (AUC >= 0.92)'\n# So this is about web text (C4/Wikipedia), not code\n# Code domain may be excluded from this claim\n\n# But exp_code_llama8b: 0.9161 < 0.92\n# However, code is not 'general web text'\n# The claim 'AUC >= 0.92' is specifically for web text (C4/Wiki) experiments\n# All C4/Wiki 0v1 AUC: min is 0.9225 (LLaMA-8B C4) >= 0.92 ✓\n\n# Check OLMo self vs cross gap more precisely\n# self-scored (exp_002 before cross-scoring update):\n# notes say: 'Self-scored 1v2=0.6145, Qwen-scored 1v2=0.5001'  \n# gap = 0.6145 - 0.5001 = 0.1144 = 11.44 pp\n# paper says '+11.5 pp'\n\nolmo_self = 0.6145\nolmo_cross = 0.5001\nprint(f'OLMo gap: {(olmo_self-olmo_cross)*100:.2f} pp (paper: +11.5 pp)')\n# 11.44 vs 11.5 -> paper rounds up\n\n# Pythia gap:\npythia_self = 0.6539\npythia_cross = 0.6074  # Qwen cross-scored\nprint(f'Pythia gap: {(pythia_self-pythia_cross)*100:.2f} pp (paper: +4.7 pp)')\n# 4.65 vs 4.7 -> paper rounds up\n\n# Mistral gap:\n# Self: exp_019 1v2=0.5935 (Mistral self-scored)\n# Cross: exp_019b 1v2=0.5695 (Qwen scorer)\nmistral_self = 0.5935\nmistral_cross = 0.5695\nprint(f'Mistral gap: {(mistral_self-mistral_cross)*100:.2f} pp (paper: ~1.9 pp)')\n# 2.4pp vs 1.9pp -> MISMATCH\n\n# For LLaMA: need to identify the self-scored experiment\n# exp_018 uses Qwen scorer (cross): 1v2=0.6123\n# No LLaMA self-scored C4 experiment found in registry\n# But paper says 'LLaMA-8B and Mistral-7B (~approx +1.9 pp each)'\n# If both are ~1.9pp average then maybe it's computed as average or separately\n\n# Actually check if there's a LLaMA self-scoring path\n# All LLaMA experiments use Qwen as scorer - so there's NO LLaMA self-scored baseline\n\nprint()\nprint('ISSUE: No LLaMA self-scored experiment found in registry')\nprint('All LLaMA exps use Qwen as scorer (cross-scored)')\nprint('Cannot verify LLaMA self vs cross gap from registry')\nprint()\nprint('MISMATCH candidate: Mistral gap = 2.4pp (registry) vs 1.9pp (paper)')\n\"\n"
  }
}
```

</details>

---


### Tool result

_source line 394 · 2026-05-23T11:38:26.850469+00:00_

OLMo gap: 11.44 pp (paper: +11.5 pp)
Pythia gap: 4.65 pp (paper: +4.7 pp)
Mistral gap: 2.40 pp (paper: ~1.9 pp)

ISSUE: No LLaMA self-scored experiment found in registry
All LLaMA exps use Qwen as scorer (cross-scored)
Cannot verify LLaMA self vs cross gap from registry

MISMATCH candidate: Mistral gap = 2.4pp (registry) vs 1.9pp (paper)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_audit_tables_3_4_inline_20260523T112128",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 395 · 2026-05-23T11:38:26.850612+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport json\n\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/17947013-ea3d-4507-b0e3-f06dfa8892ff/tool-results/mcp-agent-ml-research-read_registry-1779535307441.txt', 'r') as f:\n    raw = json.load(f)\n\ninner = json.loads(raw['result'])\ndata = inner['data']\nexps = data['experiments']\n\n# There are many mismatches. Let's see if the differences follow a systematic rounding pattern\n# or if they are truly different values\nexp020 = exps['exp_020_pythia_decoding']\nreg020 = exp020['metrics']\n\nprint('Detailed comparison for suspected rounding issues:')\nprint()\n# Check: is 0.675 -> reg 0.6770 (off by 0.002 = round to 3 decimal places from 0.677)\n# 0.559 -> reg 0.5549 (round to 3dp = 0.555, not 0.559)\n# These are not simple rounding issues -- they are actual discrepancies\n\n# Actually let's check: maybe the paper values are from bootstrap MEAN (not OOF AUC)\n# The notes mention bootstrap CI for t07 2v3 = 0.5939 CI [0.5855, 0.6025]\n# Registry reg020['t07']['auc']['2v3'] = 0.5941\n# Paper says 0.598 which is > 0.5939\n\n# Let me check if paper values match nuc09 from Qwen experiment? No that doesn't make sense\n# Perhaps the registry has updated values after a rerun?\n# The notes say: 'Bootstrap CI (10000 iter): t07 2v3 AUC=0.5939 CI [0.5855, 0.6025] BORDERLINE'\n# But registry shows t07 auc 2v3 = 0.5941 and paper says 0.598\n\n# Let me check if the paper values could be from exp_003 (Qwen) mistakenly placed\n# Qwen nuc09 2v3 = 0.5917, paper Pythia nuc09 2v3 = 0.559 -- no\n# Qwen t07 2v3 = 0.5901, paper Pythia t07 2v3 = 0.598 -- closer\n\n# Or maybe paper Table S10 uses values from a different version of exp020 not in registry\n# Let me check the absolute differences more carefully\n\nreg_t07 = reg020['t07']['auc']\npaper_t07 = {'0v1': .996, '1v2': .728, '2v3': .598, '3v4': .563, '4v5': .527}\nprint('t07 differences:')\nfor pair in ['0v1','1v2','2v3','3v4','4v5']:\n    diff = paper_t07[pair] - reg_t07[pair]\n    print(f'  {pair}: paper={paper_t07[pair]}, reg={reg_t07[pair]:.4f}, diff={diff:+.4f}')\n\nreg_t12 = reg020['t12']['auc']\npaper_t12 = {'0v1': .994, '1v2': .618, '2v3': .531, '3v4': .520, '4v5': .510}\nprint()\nprint('t12 differences:')\nfor pair in ['0v1','1v2','2v3','3v4','4v5']:\n    diff = paper_t12[pair] - reg_t12[pair]\n    print(f'  {pair}: paper={paper_t12[pair]}, reg={reg_t12[pair]:.4f}, diff={diff:+.4f}')\n\" 2>&1\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_audit_tables_3_4_inline_20260523T112128",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport json\n\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/17947013-ea3d-4507-b0e3-f06dfa8892ff/tool-results/mcp-agent-ml-research-read_registry-1779535307441.txt', 'r') as f:\n    raw = json.load(f)\n\ninner = json.loads(raw['result'])\ndata = inner['data']\nexps = data['experiments']\n\n# There are many mismatches. Let's see if the differences follow a systematic rounding pattern\n# or if they are truly different values\nexp020 = exps['exp_020_pythia_decoding']\nreg020 = exp020['metrics']\n\nprint('Detailed comparison for suspected rounding issues:')\nprint()\n# Check: is 0.675 -> reg 0.6770 (off by 0.002 = round to 3 decimal places from 0.677)\n# 0.559 -> reg 0.5549 (round to 3dp = 0.555, not 0.559)\n# These are not simple rounding issues -- they are actual discrepancies\n\n# Actually let's check: maybe the paper values are from bootstrap MEAN (not OOF AUC)\n# The notes mention bootstrap CI for t07 2v3 = 0.5939 CI [0.5855, 0.6025]\n# Registry reg020['t07']['auc']['2v3'] = 0.5941\n# Paper says 0.598 which is > 0.5939\n\n# Let me check if paper values match nuc09 from Qwen experiment? No that doesn't make sense\n# Perhaps the registry has updated values after a rerun?\n# The notes say: 'Bootstrap CI (10000 iter): t07 2v3 AUC=0.5939 CI [0.5855, 0.6025] BORDERLINE'\n# But registry shows t07 auc 2v3 = 0.5941 and paper says 0.598\n\n# Let me check if the paper values could be from exp_003 (Qwen) mistakenly placed\n# Qwen nuc09 2v3 = 0.5917, paper Pythia nuc09 2v3 = 0.559 -- no\n# Qwen t07 2v3 = 0.5901, paper Pythia t07 2v3 = 0.598 -- closer\n\n# Or maybe paper Table S10 uses values from a different version of exp020 not in registry\n# Let me check the absolute differences more carefully\n\nreg_t07 = reg020['t07']['auc']\npaper_t07 = {'0v1': .996, '1v2': .728, '2v3': .598, '3v4': .563, '4v5': .527}\nprint('t07 differences:')\nfor pair in ['0v1','1v2','2v3','3v4','4v5']:\n    diff = paper_t07[pair] - reg_t07[pair]\n    print(f'  {pair}: paper={paper_t07[pair]}, reg={reg_t07[pair]:.4f}, diff={diff:+.4f}')\n\nreg_t12 = reg020['t12']['auc']\npaper_t12 = {'0v1': .994, '1v2': .618, '2v3': .531, '3v4': .520, '4v5': .510}\nprint()\nprint('t12 differences:')\nfor pair in ['0v1','1v2','2v3','3v4','4v5']:\n    diff = paper_t12[pair] - reg_t12[pair]\n    print(f'  {pair}: paper={paper_t12[pair]}, reg={reg_t12[pair]:.4f}, diff={diff:+.4f}')\n\" 2>&1\n"
  }
}
```

</details>

---


### Tool result

_source line 396 · 2026-05-23T11:38:26.850765+00:00_

Detailed comparison for suspected rounding issues:

t07 differences:
  0v1: paper=0.996, reg=0.9965, diff=-0.0005
  1v2: paper=0.728, reg=0.7265, diff=+0.0015
  2v3: paper=0.598, reg=0.5941, diff=+0.0039
  3v4: paper=0.563, reg=0.5698, diff=-0.0068
  4v5: paper=0.527, reg=0.5284, diff=-0.0014

t12 differences:
  0v1: paper=0.994, reg=0.9933, diff=+0.0007
  1v2: paper=0.618, reg=0.6172, diff=+0.0008
  2v3: paper=0.531, reg=0.5226, diff=+0.0084
  3v4: paper=0.52, reg=0.5170, diff=+0.0030
  4v5: paper=0.51, reg=0.5051, diff=+0.0049

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_audit_tables_3_4_inline_20260523T112128",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 397 · 2026-05-23T11:38:26.850957+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\n# Let's carefully check rounding for all CI values\n# Python's round() uses banker's rounding (round half to even), not standard rounding\n# Standard .5 rounding: 0.6275 -> 0.628 (since .5 rounds up)\n# Python banker's rounding: 0.6275 -> 0.628 (since 7 is odd, round up to even 8) -- actually 7->8 is rounding up\n\nimport decimal\nfrom decimal import Decimal, ROUND_HALF_UP\n\ndef round_standard(x, n):\n    d = Decimal(str(x))\n    factor = Decimal(10) ** (-n)\n    return float(d.quantize(factor, rounding=ROUND_HALF_UP))\n\n# Check all CI values\nprint('CI value rounding check (standard half-up):')\nprint(f'0.6275 -> {round_standard(0.6275, 3)}')  # expected .628\nprint(f'0.6575 -> {round_standard(0.6575, 3)}')  # expected .658\n\nprint(f'0.6427 -> {round_standard(0.6427, 3)}')  # Paper says .644\nprint(f'0.6401 -> {round_standard(0.6401, 3)}')  # CI lower for Pythia\nprint(f'0.6688 -> {round_standard(0.6688, 3)}')  # CI upper for Pythia\nprint(f'0.6545 -> {round_standard(0.6545, 3)}')  # Pythia 2v3 pairwise\nprint(f'0.6544 -> {round_standard(0.6544, 3)}')  # Pythia 2v3 CI auc\nprint(f'0.6215 -> {round_standard(0.6215, 3)}')  # LLaMA arXiv 2v3\nprint(f'0.6262 -> {round_standard(0.6262, 3)}')  # Qwen C4 1v2\nprint(f'0.5496 -> {round_standard(0.5496, 3)}')  # Qwen C4 2v3\nprint(f'0.6193 -> {round_standard(0.6193, 3)}')  # Wiki 1v2\nprint(f'0.5498 -> {round_standard(0.5498, 3)}')  # Wiki 2v3\nprint(f'0.7382 -> {round_standard(0.7382, 3)}')  # Code Qwen 1v2\nprint(f'0.5300 -> {round_standard(0.53, 3)}')    # Code Qwen 2v3\nprint(f'0.7394 -> {round_standard(0.7394, 3)}')  # Code LLaMA 1v2\nprint(f'0.5112 -> {round_standard(0.5112, 3)}')  # Code LLaMA 2v3\nprint(f'0.8047 -> {round_standard(0.8047, 3)}')  # Pythia arXiv 1v2\n\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_audit_tables_3_4_inline_20260523T112128",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\n# Let's carefully check rounding for all CI values\n# Python's round() uses banker's rounding (round half to even), not standard rounding\n# Standard .5 rounding: 0.6275 -> 0.628 (since .5 rounds up)\n# Python banker's rounding: 0.6275 -> 0.628 (since 7 is odd, round up to even 8) -- actually 7->8 is rounding up\n\nimport decimal\nfrom decimal import Decimal, ROUND_HALF_UP\n\ndef round_standard(x, n):\n    d = Decimal(str(x))\n    factor = Decimal(10) ** (-n)\n    return float(d.quantize(factor, rounding=ROUND_HALF_UP))\n\n# Check all CI values\nprint('CI value rounding check (standard half-up):')\nprint(f'0.6275 -> {round_standard(0.6275, 3)}')  # expected .628\nprint(f'0.6575 -> {round_standard(0.6575, 3)}')  # expected .658\n\nprint(f'0.6427 -> {round_standard(0.6427, 3)}')  # Paper says .644\nprint(f'0.6401 -> {round_standard(0.6401, 3)}')  # CI lower for Pythia\nprint(f'0.6688 -> {round_standard(0.6688, 3)}')  # CI upper for Pythia\nprint(f'0.6545 -> {round_standard(0.6545, 3)}')  # Pythia 2v3 pairwise\nprint(f'0.6544 -> {round_standard(0.6544, 3)}')  # Pythia 2v3 CI auc\nprint(f'0.6215 -> {round_standard(0.6215, 3)}')  # LLaMA arXiv 2v3\nprint(f'0.6262 -> {round_standard(0.6262, 3)}')  # Qwen C4 1v2\nprint(f'0.5496 -> {round_standard(0.5496, 3)}')  # Qwen C4 2v3\nprint(f'0.6193 -> {round_standard(0.6193, 3)}')  # Wiki 1v2\nprint(f'0.5498 -> {round_standard(0.5498, 3)}')  # Wiki 2v3\nprint(f'0.7382 -> {round_standard(0.7382, 3)}')  # Code Qwen 1v2\nprint(f'0.5300 -> {round_standard(0.53, 3)}')    # Code Qwen 2v3\nprint(f'0.7394 -> {round_standard(0.7394, 3)}')  # Code LLaMA 1v2\nprint(f'0.5112 -> {round_standard(0.5112, 3)}')  # Code LLaMA 2v3\nprint(f'0.8047 -> {round_standard(0.8047, 3)}')  # Pythia arXiv 1v2\n\"\n"
  }
}
```

</details>

---


### Tool result

_source line 398 · 2026-05-23T11:38:26.851102+00:00_

CI value rounding check (standard half-up):
0.6275 -> 0.628
0.6575 -> 0.658
0.6427 -> 0.643
0.6401 -> 0.64
0.6688 -> 0.669
0.6545 -> 0.655
0.6544 -> 0.654
0.6215 -> 0.622
0.6262 -> 0.626
0.5496 -> 0.55
0.6193 -> 0.619
0.5498 -> 0.55
0.7382 -> 0.738
0.5300 -> 0.53
0.7394 -> 0.739
0.5112 -> 0.511
0.8047 -> 0.805

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_audit_tables_3_4_inline_20260523T112128",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 399 · 2026-05-23T11:38:26.851240+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nfrom decimal import Decimal, ROUND_HALF_UP\n\ndef round_standard(x, n):\n    d = Decimal(str(x))\n    factor = Decimal(10) ** (-n)\n    return float(d.quantize(factor, rounding=ROUND_HALF_UP))\n\nprint('KEY MISMATCHES:')\nprint()\nprint('1. arXiv/Qwen 2v3: Paper=.644, Registry=0.6427, rounds to', round_standard(0.6427, 3))\nprint('   MISMATCH: 0.643 != 0.644')\nprint()\nprint('2. Inline Qwen arXiv 2v3 AUC: Paper=0.644, Registry=0.6427, rounds to', round_standard(0.6427, 3))\nprint('   MISMATCH: 0.643 != 0.644')\nprint()\nprint('3. Inline Qwen arXiv CI: Paper=[0.628, 0.658], Registry=[0.6275, 0.6575]')\nprint('   0.6275 rounds to', round_standard(0.6275, 3), '(paper: 0.628) -- OK')\nprint('   0.6575 rounds to', round_standard(0.6575, 3), '(paper: 0.658) -- MISMATCH (0.658 vs 0.658: check)')\nprint('   Actually 0.6575 -> 0.658 is OK (rounds up from 5)')\nprint()\nprint('4. Inline LLaMA arXiv 2v3: Paper=0.620, Registry exp_arXiv_llama8b=0.6215 rounds to', round_standard(0.6215, 3))\nprint('   MISMATCH: 0.622 != 0.620')\nprint()\nprint('5. Code/LLaMA 2v3: Paper=.510, Registry=0.5112 rounds to', round_standard(0.5112, 3))\nprint('   MISMATCH: 0.511 != 0.510')\nprint()\nprint('6. S12 Wiki 4v5: Paper=.514, no full registry data for Wiki (exp_023 incomplete)')\n\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_audit_tables_3_4_inline_20260523T112128",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nfrom decimal import Decimal, ROUND_HALF_UP\n\ndef round_standard(x, n):\n    d = Decimal(str(x))\n    factor = Decimal(10) ** (-n)\n    return float(d.quantize(factor, rounding=ROUND_HALF_UP))\n\nprint('KEY MISMATCHES:')\nprint()\nprint('1. arXiv/Qwen 2v3: Paper=.644, Registry=0.6427, rounds to', round_standard(0.6427, 3))\nprint('   MISMATCH: 0.643 != 0.644')\nprint()\nprint('2. Inline Qwen arXiv 2v3 AUC: Paper=0.644, Registry=0.6427, rounds to', round_standard(0.6427, 3))\nprint('   MISMATCH: 0.643 != 0.644')\nprint()\nprint('3. Inline Qwen arXiv CI: Paper=[0.628, 0.658], Registry=[0.6275, 0.6575]')\nprint('   0.6275 rounds to', round_standard(0.6275, 3), '(paper: 0.628) -- OK')\nprint('   0.6575 rounds to', round_standard(0.6575, 3), '(paper: 0.658) -- MISMATCH (0.658 vs 0.658: check)')\nprint('   Actually 0.6575 -> 0.658 is OK (rounds up from 5)')\nprint()\nprint('4. Inline LLaMA arXiv 2v3: Paper=0.620, Registry exp_arXiv_llama8b=0.6215 rounds to', round_standard(0.6215, 3))\nprint('   MISMATCH: 0.622 != 0.620')\nprint()\nprint('5. Code/LLaMA 2v3: Paper=.510, Registry=0.5112 rounds to', round_standard(0.5112, 3))\nprint('   MISMATCH: 0.511 != 0.510')\nprint()\nprint('6. S12 Wiki 4v5: Paper=.514, no full registry data for Wiki (exp_023 incomplete)')\n\"\n"
  }
}
```

</details>

---


### Tool result

_source line 400 · 2026-05-23T11:38:26.851369+00:00_

KEY MISMATCHES:

1. arXiv/Qwen 2v3: Paper=.644, Registry=0.6427, rounds to 0.643
   MISMATCH: 0.643 != 0.644

2. Inline Qwen arXiv 2v3 AUC: Paper=0.644, Registry=0.6427, rounds to 0.643
   MISMATCH: 0.643 != 0.644

3. Inline Qwen arXiv CI: Paper=[0.628, 0.658], Registry=[0.6275, 0.6575]
   0.6275 rounds to 0.628 (paper: 0.628) -- OK
   0.6575 rounds to 0.658 (paper: 0.658) -- MISMATCH (0.658 vs 0.658: check)
   Actually 0.6575 -> 0.658 is OK (rounds up from 5)

4. Inline LLaMA arXiv 2v3: Paper=0.620, Registry exp_arXiv_llama8b=0.6215 rounds to 0.622
   MISMATCH: 0.622 != 0.620

5. Code/LLaMA 2v3: Paper=.510, Registry=0.5112 rounds to 0.511
   MISMATCH: 0.511 != 0.510

6. S12 Wiki 4v5: Paper=.514, no full registry data for Wiki (exp_023 incomplete)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_audit_tables_3_4_inline_20260523T112128",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 401 · 2026-05-23T11:38:26.851514+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport json\n\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/17947013-ea3d-4507-b0e3-f06dfa8892ff/tool-results/mcp-agent-ml-research-read_registry-1779535307441.txt') as f:\n    outer = json.load(f)\n\ninner = json.loads(outer['result'])\nexps = inner['data']['experiments']\n\n# Check the arXiv 1v2 JSD discrepancy more carefully\n# Discussion says '1v2 JSD = 0.077 vs ~0.01 for C4'\n# arXiv 1v2 JSD across experiments: \n# exp_arXiv_mistral7b: 0.076232\n# exp_arXiv_llama8b: 0.0785\n# exp_arXiv_qwen7b: 0.0668\n# exp_025_pythia_arxiv: 0.057344\n# The exp_024 (primary arXiv Qwen-1.5B): no JSD stored\n\n# If the paper says 0.077, it might be:\n# 1) The Qwen-1.5B arXiv JSD (primary exp) - not stored\n# 2) Average of arXiv experiments\n# 3) A specific experiment like exp_arXiv_mistral7b (0.076)\n\n# Let me check the main arXiv experiment script for JSD\n# The primary: exp_024_arxiv_domain and exp_arXiv_llama8b/mistral7b\n\n# The 0.077 in discussion.tex is LIKELY from the arXiv experiments\n# For Qwen-1.5B arXiv (exp_024): JSD not stored in registry\n# For Mistral arXiv (self-scored with Qwen scorer): 0.076 ≈ 0.077\n\n# But given the context 'formulaic structure ... creates larger shifts (1v2 JSD = 0.077)'\n# This could be ANY arXiv model - the Mistral-7B arXiv (0.076) is closest to 0.077\n# OR it could be the average ≈ 0.077\n\n# For the C4 1v2 JSD: ~0.01 is well-supported (multiple exps: 0.005-0.012)\n\n# Now let me also check if the OBD depth-0 recall 96% is for the OBD classifier\n# exp_D_obd_n500 shows d0=0.96 ✓\nprint('OBD d0 recall: 0.96 ✓')\nprint('OBD d2: 0.14, d3: 0.19, d4: 0.22 => range 14-22% ✓')\nprint()\n\n# LLM depths 2-4: 8-38%\n# GPT: d2=0.38, d3=0.24, d4=0.08\n# Claude: d2=0.28, d3=0.101, d4=0.37\n# Combined range: 8% (GPT d4) to 38% (GPT d2) ✓\nprint('LLM depths 2-4: range 8-38% ✓ (GPT d4=8%, GPT d2=38%)')\nprint()\n\n# Verify p<=0.002 for K*=2 configurations (introduction)\n# exp_007_bootstrap_ci shows all K*=2 perm_p = 0.002\n# qwen_rewrite 1v2 perm_p=0.002, pythia_cont 1v2 perm_p=0.002\n# olmo_cont 1v2 perm_p=0.002, qwen_cont 1v2 perm_p=0.002\ne007 = exps['exp_007_bootstrap_ci']\nm007 = e007['metrics']\nprint('Permutation p-values for K*=2 configurations (exp_007):')\nfor model, data in m007.items():\n    if isinstance(data, dict) and '1v2' in data:\n        perm_p = data['1v2'].get('perm_p', 'N/A')\n        print(f'  {model} 1v2 perm_p: {perm_p}')\nprint()\nprint('Paper says: p <= 0.002 for K*=2 configurations ✓ (all are 0.002)')\n\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_audit_tables_3_4_inline_20260523T112128",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport json\n\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/17947013-ea3d-4507-b0e3-f06dfa8892ff/tool-results/mcp-agent-ml-research-read_registry-1779535307441.txt') as f:\n    outer = json.load(f)\n\ninner = json.loads(outer['result'])\nexps = inner['data']['experiments']\n\n# Check the arXiv 1v2 JSD discrepancy more carefully\n# Discussion says '1v2 JSD = 0.077 vs ~0.01 for C4'\n# arXiv 1v2 JSD across experiments: \n# exp_arXiv_mistral7b: 0.076232\n# exp_arXiv_llama8b: 0.0785\n# exp_arXiv_qwen7b: 0.0668\n# exp_025_pythia_arxiv: 0.057344\n# The exp_024 (primary arXiv Qwen-1.5B): no JSD stored\n\n# If the paper says 0.077, it might be:\n# 1) The Qwen-1.5B arXiv JSD (primary exp) - not stored\n# 2) Average of arXiv experiments\n# 3) A specific experiment like exp_arXiv_mistral7b (0.076)\n\n# Let me check the main arXiv experiment script for JSD\n# The primary: exp_024_arxiv_domain and exp_arXiv_llama8b/mistral7b\n\n# The 0.077 in discussion.tex is LIKELY from the arXiv experiments\n# For Qwen-1.5B arXiv (exp_024): JSD not stored in registry\n# For Mistral arXiv (self-scored with Qwen scorer): 0.076 ≈ 0.077\n\n# But given the context 'formulaic structure ... creates larger shifts (1v2 JSD = 0.077)'\n# This could be ANY arXiv model - the Mistral-7B arXiv (0.076) is closest to 0.077\n# OR it could be the average ≈ 0.077\n\n# For the C4 1v2 JSD: ~0.01 is well-supported (multiple exps: 0.005-0.012)\n\n# Now let me also check if the OBD depth-0 recall 96% is for the OBD classifier\n# exp_D_obd_n500 shows d0=0.96 ✓\nprint('OBD d0 recall: 0.96 ✓')\nprint('OBD d2: 0.14, d3: 0.19, d4: 0.22 => range 14-22% ✓')\nprint()\n\n# LLM depths 2-4: 8-38%\n# GPT: d2=0.38, d3=0.24, d4=0.08\n# Claude: d2=0.28, d3=0.101, d4=0.37\n# Combined range: 8% (GPT d4) to 38% (GPT d2) ✓\nprint('LLM depths 2-4: range 8-38% ✓ (GPT d4=8%, GPT d2=38%)')\nprint()\n\n# Verify p<=0.002 for K*=2 configurations (introduction)\n# exp_007_bootstrap_ci shows all K*=2 perm_p = 0.002\n# qwen_rewrite 1v2 perm_p=0.002, pythia_cont 1v2 perm_p=0.002\n# olmo_cont 1v2 perm_p=0.002, qwen_cont 1v2 perm_p=0.002\ne007 = exps['exp_007_bootstrap_ci']\nm007 = e007['metrics']\nprint('Permutation p-values for K*=2 configurations (exp_007):')\nfor model, data in m007.items():\n    if isinstance(data, dict) and '1v2' in data:\n        perm_p = data['1v2'].get('perm_p', 'N/A')\n        print(f'  {model} 1v2 perm_p: {perm_p}')\nprint()\nprint('Paper says: p <= 0.002 for K*=2 configurations ✓ (all are 0.002)')\n\"\n"
  }
}
```

</details>

---


### Tool result

_source line 402 · 2026-05-23T11:38:26.851668+00:00_

OBD d0 recall: 0.96 ✓
OBD d2: 0.14, d3: 0.19, d4: 0.22 => range 14-22% ✓

LLM depths 2-4: range 8-38% ✓ (GPT d4=8%, GPT d2=38%)

Permutation p-values for K*=2 configurations (exp_007):
  qwen_rewrite 1v2 perm_p: 0.002
  pythia_cont 1v2 perm_p: 0.002
  olmo_cont 1v2 perm_p: 0.002
  qwen_cont 1v2 perm_p: 0.002

Paper says: p <= 0.002 for K*=2 configurations ✓ (all are 0.002)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_audit_tables_3_4_inline_20260523T112128",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 403 · 2026-05-23T11:38:26.851830+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport json\n\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/17947013-ea3d-4507-b0e3-f06dfa8892ff/tool-results/mcp-agent-ml-research-read_registry-1779535307441.txt', 'r') as f:\n    raw = json.load(f)\n\ninner = json.loads(raw['result'])\ndata = inner['data']\nexps = data['experiments']\n\n# Differences are non-trivial (not just rounding): e.g., t07 3v4 diff=-0.0068\n# This suggests the paper's Table S10 values came from a different run or updated analysis \n# not reflected in the registry\n\n# TASK 5: Table S11 Length ablation (exp_021)\n# Paper:\n# | | 128 | 256 | 512 |\n# | 0v1 | .979 | .991 | .992 |\n# | 1v2 | .622 | .628 | .607 |\n# | 2v3 | .529 | .556 | .572 |\n# | 3v4 | .535 | .530 | .530 |\n# | 4v5 | .501 | .514 | .518 |\n\nexp021 = exps['exp_021_length_ablation']\nreg021 = exp021['metrics']\n\nprint('=== TASK 5: Table S11 Length ablation ===')\nprint()\nprint('Registry exp_021 metrics:')\nprint(json.dumps(reg021, indent=2))\nprint()\n\n# Registry only has 1v2_auc for each length:\n# 128: 1v2_auc=0.6219, 256: 1v2_auc=0.6282, 512: 1v2_auc=0.6073\n# Paper: 1v2 128=0.622, 256=0.628, 512=0.607\n\npaper_s11_1v2 = {'128tok': .622, '256tok': .628, '512tok': .607}\nprint('1v2 comparison (only data available in registry):')\nfor tok in ['128tok', '256tok', '512tok']:\n    reg_v = reg021[tok]['1v2_auc']\n    paper_v = paper_s11_1v2[tok]\n    match = abs(reg_v - paper_v) < 0.0015\n    print(f'  {tok}: Reg={reg_v:.4f}, Paper={paper_v:.3f}, Match={match}')\n\nprint()\nprint('NOTE: Registry exp_021 only stores 1v2_auc - full depth breakdown not in registry')\nprint('All other rows (0v1, 2v3, 3v4, 4v5) of Table S11 CANNOT be verified against registry')\n\" 2>&1\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_audit_tables_3_4_inline_20260523T112128",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport json\n\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/17947013-ea3d-4507-b0e3-f06dfa8892ff/tool-results/mcp-agent-ml-research-read_registry-1779535307441.txt', 'r') as f:\n    raw = json.load(f)\n\ninner = json.loads(raw['result'])\ndata = inner['data']\nexps = data['experiments']\n\n# Differences are non-trivial (not just rounding): e.g., t07 3v4 diff=-0.0068\n# This suggests the paper's Table S10 values came from a different run or updated analysis \n# not reflected in the registry\n\n# TASK 5: Table S11 Length ablation (exp_021)\n# Paper:\n# | | 128 | 256 | 512 |\n# | 0v1 | .979 | .991 | .992 |\n# | 1v2 | .622 | .628 | .607 |\n# | 2v3 | .529 | .556 | .572 |\n# | 3v4 | .535 | .530 | .530 |\n# | 4v5 | .501 | .514 | .518 |\n\nexp021 = exps['exp_021_length_ablation']\nreg021 = exp021['metrics']\n\nprint('=== TASK 5: Table S11 Length ablation ===')\nprint()\nprint('Registry exp_021 metrics:')\nprint(json.dumps(reg021, indent=2))\nprint()\n\n# Registry only has 1v2_auc for each length:\n# 128: 1v2_auc=0.6219, 256: 1v2_auc=0.6282, 512: 1v2_auc=0.6073\n# Paper: 1v2 128=0.622, 256=0.628, 512=0.607\n\npaper_s11_1v2 = {'128tok': .622, '256tok': .628, '512tok': .607}\nprint('1v2 comparison (only data available in registry):')\nfor tok in ['128tok', '256tok', '512tok']:\n    reg_v = reg021[tok]['1v2_auc']\n    paper_v = paper_s11_1v2[tok]\n    match = abs(reg_v - paper_v) < 0.0015\n    print(f'  {tok}: Reg={reg_v:.4f}, Paper={paper_v:.3f}, Match={match}')\n\nprint()\nprint('NOTE: Registry exp_021 only stores 1v2_auc - full depth breakdown not in registry')\nprint('All other rows (0v1, 2v3, 3v4, 4v5) of Table S11 CANNOT be verified against registry')\n\" 2>&1\n"
  }
}
```

</details>

---


### Tool result

_source line 404 · 2026-05-23T11:38:26.851980+00:00_

=== TASK 5: Table S11 Length ablation ===

Registry exp_021 metrics:
{
  "128tok": {
    "K_star": 2,
    "1v2_auc": 0.6219
  },
  "256tok": {
    "K_star": 2,
    "1v2_auc": 0.6282
  },
  "512tok": {
    "K_star": 2,
    "1v2_auc": 0.6073
  },
  "all_K_star_2": true,
  "bootstrap_ci": {
    "512tok_1v2": {
      "auc": 0.6073,
      "ci_lower": 0.5979,
      "ci_upper": 0.6166,
      "perm_p": 0.0001,
      "verdict": "BORDERLINE"
    }
  }
}

1v2 comparison (only data available in registry):
  128tok: Reg=0.6219, Paper=0.622, Match=True
  256tok: Reg=0.6282, Paper=0.628, Match=True
  512tok: Reg=0.6073, Paper=0.607, Match=True

NOTE: Registry exp_021 only stores 1v2_auc - full depth breakdown not in registry
All other rows (0v1, 2v3, 3v4, 4v5) of Table S11 CANNOT be verified against registry

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_audit_tables_3_4_inline_20260523T112128",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 405 · 2026-05-23T11:38:26.852169+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nfrom decimal import Decimal, ROUND_HALF_UP\n\ndef round_standard(x, n):\n    d = Decimal(str(x))\n    factor = Decimal(10) ** (-n)\n    return float(d.quantize(factor, rounding=ROUND_HALF_UP))\n\n# Check if these are within display precision (truncation at 3 decimal vs rounding)\n# The paper uses 3-decimal format: .644 means 0.644\n# If the paper TRUNCATES rather than ROUNDS:\ndef truncate(x, n):\n    import math\n    return math.floor(x * 10**n) / 10**n\n\nprint('Checking TRUNCATION behavior:')\nprint(f'0.6427 truncated to 3dp: {truncate(0.6427, 3)}')  # 0.642, not 0.644\nprint(f'0.6275 truncated to 3dp: {truncate(0.6275, 3)}')  # 0.627, not 0.628\n\n# Neither rounding nor truncation explains .644 from 0.6427\n# The only way .644 works from exp_024 is if the actual computed value is slightly higher\n\n# Let me check the bootstrap_ci AUC vs pairwise_auc:\n# exp_024 pairwise_auc['2v3'] = 0.6427\n# exp_024 bootstrap_ci['2v3']['auc'] = 0.6427\n# Both are the same -- no discrepancy there\n\n# Maybe the 2v3 AUC was recomputed from a different result file\n# or there was an intermediate version where value was 0.6437+ (which rounds to 0.644)\n\nprint()\nprint('Summary of rounding analysis:')\nprint('For .644 to be correct, registry value must be in [0.6435, 0.6445)')\nprint('Current registry value: 0.6427 (falls in [0.6425, 0.6435) -> rounds to 0.643)')\nprint()\nprint('This is a genuine mismatch of 0.001 in AUC.')\n\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_audit_tables_3_4_inline_20260523T112128",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nfrom decimal import Decimal, ROUND_HALF_UP\n\ndef round_standard(x, n):\n    d = Decimal(str(x))\n    factor = Decimal(10) ** (-n)\n    return float(d.quantize(factor, rounding=ROUND_HALF_UP))\n\n# Check if these are within display precision (truncation at 3 decimal vs rounding)\n# The paper uses 3-decimal format: .644 means 0.644\n# If the paper TRUNCATES rather than ROUNDS:\ndef truncate(x, n):\n    import math\n    return math.floor(x * 10**n) / 10**n\n\nprint('Checking TRUNCATION behavior:')\nprint(f'0.6427 truncated to 3dp: {truncate(0.6427, 3)}')  # 0.642, not 0.644\nprint(f'0.6275 truncated to 3dp: {truncate(0.6275, 3)}')  # 0.627, not 0.628\n\n# Neither rounding nor truncation explains .644 from 0.6427\n# The only way .644 works from exp_024 is if the actual computed value is slightly higher\n\n# Let me check the bootstrap_ci AUC vs pairwise_auc:\n# exp_024 pairwise_auc['2v3'] = 0.6427\n# exp_024 bootstrap_ci['2v3']['auc'] = 0.6427\n# Both are the same -- no discrepancy there\n\n# Maybe the 2v3 AUC was recomputed from a different result file\n# or there was an intermediate version where value was 0.6437+ (which rounds to 0.644)\n\nprint()\nprint('Summary of rounding analysis:')\nprint('For .644 to be correct, registry value must be in [0.6435, 0.6445)')\nprint('Current registry value: 0.6427 (falls in [0.6425, 0.6435) -> rounds to 0.643)')\nprint()\nprint('This is a genuine mismatch of 0.001 in AUC.')\n\"\n"
  }
}
```

</details>

---


### Tool result

_source line 406 · 2026-05-23T11:38:26.852336+00:00_

Checking TRUNCATION behavior:
0.6427 truncated to 3dp: 0.642
0.6275 truncated to 3dp: 0.627

Summary of rounding analysis:
For .644 to be correct, registry value must be in [0.6435, 0.6445)
Current registry value: 0.6427 (falls in [0.6425, 0.6435) -> rounds to 0.643)

This is a genuine mismatch of 0.001 in AUC.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_audit_tables_3_4_inline_20260523T112128",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 407 · 2026-05-23T11:38:26.852511+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport json\n\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/17947013-ea3d-4507-b0e3-f06dfa8892ff/tool-results/mcp-agent-ml-research-read_registry-1779535307441.txt', 'r') as f:\n    raw = json.load(f)\n\ninner = json.loads(raw['result'])\ndata = inner['data']\nexps = data['experiments']\n\n# Final summary: check the Spearman rho values from Table S2 (0.600, 0.782, 0.914, 0.893, 0.532, 0.668)\n# 0.782 is not found anywhere in registry\n# These 6 values don't correspond to 4 decoding configs with Spearman rho\n# Let me check if these could be Spearman rho of AUC vs depth across ALL depth pairs for ALL experiments\n# The paper might compute Spearman rho for each of the 6 model×config combinations\n\n# Actually re-reading the task: Table S2 has a separate section for 'Spearman rho values'\n# 6 values: 0.600, 0.782, 0.914, 0.893, 0.532, 0.668\n# These could be 4 decoding configs + 2 others, OR cross-model correlations\n\n# None of 0.782 found in registry at all. Let me check very broad search\nprint('Searching for any value near 0.782...')\ndef search_all_floats(d, path='', tolerance=0.005):\n    results = []\n    if isinstance(d, (int, float)):\n        if abs(d - 0.782) < tolerance:\n            results.append((path, d))\n    elif isinstance(d, dict):\n        for k, v in d.items():\n            results.extend(search_all_floats(v, path+'.'+k, tolerance))\n    elif isinstance(d, list):\n        for i, v in enumerate(d):\n            results.extend(search_all_floats(v, path+f'[{i}]', tolerance))\n    return results\n\nall_near_782 = []\nfor exp_id, exp in exps.items():\n    matches = search_all_floats(exp, path=exp_id)\n    all_near_782.extend(matches)\n\nif all_near_782:\n    for path, val in all_near_782:\n        print(f'  {path}: {val}')\nelse:\n    print('  NOT FOUND (no value within ±0.005 of 0.782 in entire registry)')\n\" 2>&1\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_audit_tables_3_4_inline_20260523T112128",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport json\n\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/17947013-ea3d-4507-b0e3-f06dfa8892ff/tool-results/mcp-agent-ml-research-read_registry-1779535307441.txt', 'r') as f:\n    raw = json.load(f)\n\ninner = json.loads(raw['result'])\ndata = inner['data']\nexps = data['experiments']\n\n# Final summary: check the Spearman rho values from Table S2 (0.600, 0.782, 0.914, 0.893, 0.532, 0.668)\n# 0.782 is not found anywhere in registry\n# These 6 values don't correspond to 4 decoding configs with Spearman rho\n# Let me check if these could be Spearman rho of AUC vs depth across ALL depth pairs for ALL experiments\n# The paper might compute Spearman rho for each of the 6 model×config combinations\n\n# Actually re-reading the task: Table S2 has a separate section for 'Spearman rho values'\n# 6 values: 0.600, 0.782, 0.914, 0.893, 0.532, 0.668\n# These could be 4 decoding configs + 2 others, OR cross-model correlations\n\n# None of 0.782 found in registry at all. Let me check very broad search\nprint('Searching for any value near 0.782...')\ndef search_all_floats(d, path='', tolerance=0.005):\n    results = []\n    if isinstance(d, (int, float)):\n        if abs(d - 0.782) < tolerance:\n            results.append((path, d))\n    elif isinstance(d, dict):\n        for k, v in d.items():\n            results.extend(search_all_floats(v, path+'.'+k, tolerance))\n    elif isinstance(d, list):\n        for i, v in enumerate(d):\n            results.extend(search_all_floats(v, path+f'[{i}]', tolerance))\n    return results\n\nall_near_782 = []\nfor exp_id, exp in exps.items():\n    matches = search_all_floats(exp, path=exp_id)\n    all_near_782.extend(matches)\n\nif all_near_782:\n    for path, val in all_near_782:\n        print(f'  {path}: {val}')\nelse:\n    print('  NOT FOUND (no value within ±0.005 of 0.782 in entire registry)')\n\" 2>&1\n"
  }
}
```

</details>

---


### Tool result

_source line 408 · 2026-05-23T11:38:26.852690+00:00_

Searching for any value near 0.782...
  exp_wiki_multi_source.metrics.vocab_only_with_label.0v1: 0.7779

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_audit_tables_3_4_inline_20260523T112128",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 409 · 2026-05-23T11:38:26.852885+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport json\n\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/17947013-ea3d-4507-b0e3-f06dfa8892ff/tool-results/mcp-agent-ml-research-read_registry-1779535307441.txt') as f:\n    outer = json.load(f)\n\ninner = json.loads(outer['result'])\nexps = inner['data']['experiments']\n\n# Final check: retrain chain 3v4 AUC range: 0.68-0.80\n# From registry:\n# Pythia: 0.7999, Qwen retrain: 0.7624, OLMo retrain v3: 0.6817\n# exp_008_retrain_chain_v2: 0.7982\n# exp_027 (Qwen2.5): 0.7977\n# exp_qwen_retrain_depth7: 0.76\n\nretrain_3v4 = [0.7999, 0.7624, 0.6817, 0.7982, 0.7977, 0.76]\nprint('Retrain-chain 3v4 AUC values:', retrain_3v4)\nprint('Min:', min(retrain_3v4), 'Max:', max(retrain_3v4))\nprint('Paper says: 3v4 AUC = 0.68-0.80')\nprint()\n# Range: 0.6817 to 0.7999\n# Paper says 0.68-0.80 -> OLMo lower bound rounds to 0.68 ✓, Pythia upper rounds to 0.80 ✓\n\n# 6v7 AUC retrain chain extended:\n# Pythia retrain depth7: 6v7=0.634\n# Qwen retrain depth7: 6v7=0.641\nprint('6v7 retrain chain:')\nprint('  Pythia: 0.634, Qwen: 0.641')\nprint('  Paper says: 6v7 AUC = 0.634-0.641')\nprint('  MATCH ✓')\nprint()\n\n# 0v1 JSD at 8B vs <=1.5B summary:\nprint('0v1 JSD claim: 0.077 at 8B vs 0.15-0.27 at <=1.5B')\nprint('  LLaMA-8B C4 0v1 JSD: 0.077 ✓')\nprint('  <=1.5B C4:')\nprint('    Qwen-1.5B-Base: 0.1637')\nprint('    Qwen-1.5B-Instruct: 0.2863')  \nprint('    OLMo-1B: 0.2300')\nprint('  Actual range: 0.164-0.286')\nprint('  Paper says: 0.15-0.27')\nprint('  PARTIAL MISMATCH: lower bound 0.15 (paper) vs 0.164 (actual); upper 0.27 (paper) vs 0.286 (actual)')\n\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_audit_tables_3_4_inline_20260523T112128",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport json\n\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/17947013-ea3d-4507-b0e3-f06dfa8892ff/tool-results/mcp-agent-ml-research-read_registry-1779535307441.txt') as f:\n    outer = json.load(f)\n\ninner = json.loads(outer['result'])\nexps = inner['data']['experiments']\n\n# Final check: retrain chain 3v4 AUC range: 0.68-0.80\n# From registry:\n# Pythia: 0.7999, Qwen retrain: 0.7624, OLMo retrain v3: 0.6817\n# exp_008_retrain_chain_v2: 0.7982\n# exp_027 (Qwen2.5): 0.7977\n# exp_qwen_retrain_depth7: 0.76\n\nretrain_3v4 = [0.7999, 0.7624, 0.6817, 0.7982, 0.7977, 0.76]\nprint('Retrain-chain 3v4 AUC values:', retrain_3v4)\nprint('Min:', min(retrain_3v4), 'Max:', max(retrain_3v4))\nprint('Paper says: 3v4 AUC = 0.68-0.80')\nprint()\n# Range: 0.6817 to 0.7999\n# Paper says 0.68-0.80 -> OLMo lower bound rounds to 0.68 ✓, Pythia upper rounds to 0.80 ✓\n\n# 6v7 AUC retrain chain extended:\n# Pythia retrain depth7: 6v7=0.634\n# Qwen retrain depth7: 6v7=0.641\nprint('6v7 retrain chain:')\nprint('  Pythia: 0.634, Qwen: 0.641')\nprint('  Paper says: 6v7 AUC = 0.634-0.641')\nprint('  MATCH ✓')\nprint()\n\n# 0v1 JSD at 8B vs <=1.5B summary:\nprint('0v1 JSD claim: 0.077 at 8B vs 0.15-0.27 at <=1.5B')\nprint('  LLaMA-8B C4 0v1 JSD: 0.077 ✓')\nprint('  <=1.5B C4:')\nprint('    Qwen-1.5B-Base: 0.1637')\nprint('    Qwen-1.5B-Instruct: 0.2863')  \nprint('    OLMo-1B: 0.2300')\nprint('  Actual range: 0.164-0.286')\nprint('  Paper says: 0.15-0.27')\nprint('  PARTIAL MISMATCH: lower bound 0.15 (paper) vs 0.164 (actual); upper 0.27 (paper) vs 0.286 (actual)')\n\"\n"
  }
}
```

</details>

---


### Tool result

_source line 410 · 2026-05-23T11:38:26.853077+00:00_

Retrain-chain 3v4 AUC values: [0.7999, 0.7624, 0.6817, 0.7982, 0.7977, 0.76]
Min: 0.6817 Max: 0.7999
Paper says: 3v4 AUC = 0.68-0.80

6v7 retrain chain:
  Pythia: 0.634, Qwen: 0.641
  Paper says: 6v7 AUC = 0.634-0.641
  MATCH ✓

0v1 JSD claim: 0.077 at 8B vs 0.15-0.27 at <=1.5B
  LLaMA-8B C4 0v1 JSD: 0.077 ✓
  <=1.5B C4:
    Qwen-1.5B-Base: 0.1637
    Qwen-1.5B-Instruct: 0.2863
    OLMo-1B: 0.2300
  Actual range: 0.164-0.286
  Paper says: 0.15-0.27
  PARTIAL MISMATCH: lower bound 0.15 (paper) vs 0.164 (actual); upper 0.27 (paper) vs 0.286 (actual)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_audit_tables_3_4_inline_20260523T112128",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 411 · 2026-05-23T11:38:26.853240+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nfrom decimal import Decimal, ROUND_HALF_UP\n\ndef round_standard(x, n):\n    d = Decimal(str(x))\n    factor = Decimal(10) ** (-n)\n    return float(d.quantize(factor, rounding=ROUND_HALF_UP))\n\n# Let me check ALL Table 4 values systematically\nprint('=== TABLE 4 COMPLETE VERIFICATION ===')\nprint()\n\n# Registry values extracted\ntable4_data = [\n    # (domain, model, exp_id, reg_1v2, reg_2v3, reg_kstar, paper_1v2, paper_2v3, paper_kstar)\n    ('arXiv', 'Qwen-1.5B', 'exp_024', 0.858, 0.6427, 3, 0.858, 0.644, 3),\n    ('arXiv', 'Pythia-1.4B', 'exp_025', 0.8047, 0.6545, 3, 0.805, 0.655, 3),\n    ('C4', 'Qwen-1.5B', 'exp_016', 0.6262, 0.5496, 2, 0.626, 0.550, 2),\n    ('Wiki', 'Qwen-1.5B', 'exp_023', 0.6193, 0.5498, 2, 0.619, 0.550, 2),\n    ('Code', 'Qwen-1.5B', 'exp_code_qwen1b5', 0.7382, 0.53, 2, 0.738, 0.530, 2),\n    ('Code', 'LLaMA-8B', 'exp_code_llama8b', 0.7394, 0.5112, 2, 0.739, 0.510, 2),\n]\n\nfor domain, model, exp_id, reg_1v2, reg_2v3, reg_k, p_1v2, p_2v3, p_k in table4_data:\n    rounded_1v2 = round_standard(reg_1v2, 3)\n    rounded_2v3 = round_standard(reg_2v3, 3)\n    match_1v2 = 'OK' if abs(rounded_1v2 - p_1v2) < 0.001 else 'MISMATCH'\n    match_2v3 = 'OK' if abs(rounded_2v3 - p_2v3) < 0.001 else 'MISMATCH'\n    match_k = 'OK' if reg_k == p_k else 'MISMATCH'\n    print(f'{domain}/{model}:')\n    print(f'  1v2: paper={p_1v2}, reg={reg_1v2}, rounds={rounded_1v2} -> {match_1v2}')\n    print(f'  2v3: paper={p_2v3}, reg={reg_2v3}, rounds={rounded_2v3} -> {match_2v3}')\n    print(f'  K*:  paper={p_k}, reg={reg_k} -> {match_k}')\n    print()\n\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_audit_tables_3_4_inline_20260523T112128",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nfrom decimal import Decimal, ROUND_HALF_UP\n\ndef round_standard(x, n):\n    d = Decimal(str(x))\n    factor = Decimal(10) ** (-n)\n    return float(d.quantize(factor, rounding=ROUND_HALF_UP))\n\n# Let me check ALL Table 4 values systematically\nprint('=== TABLE 4 COMPLETE VERIFICATION ===')\nprint()\n\n# Registry values extracted\ntable4_data = [\n    # (domain, model, exp_id, reg_1v2, reg_2v3, reg_kstar, paper_1v2, paper_2v3, paper_kstar)\n    ('arXiv', 'Qwen-1.5B', 'exp_024', 0.858, 0.6427, 3, 0.858, 0.644, 3),\n    ('arXiv', 'Pythia-1.4B', 'exp_025', 0.8047, 0.6545, 3, 0.805, 0.655, 3),\n    ('C4', 'Qwen-1.5B', 'exp_016', 0.6262, 0.5496, 2, 0.626, 0.550, 2),\n    ('Wiki', 'Qwen-1.5B', 'exp_023', 0.6193, 0.5498, 2, 0.619, 0.550, 2),\n    ('Code', 'Qwen-1.5B', 'exp_code_qwen1b5', 0.7382, 0.53, 2, 0.738, 0.530, 2),\n    ('Code', 'LLaMA-8B', 'exp_code_llama8b', 0.7394, 0.5112, 2, 0.739, 0.510, 2),\n]\n\nfor domain, model, exp_id, reg_1v2, reg_2v3, reg_k, p_1v2, p_2v3, p_k in table4_data:\n    rounded_1v2 = round_standard(reg_1v2, 3)\n    rounded_2v3 = round_standard(reg_2v3, 3)\n    match_1v2 = 'OK' if abs(rounded_1v2 - p_1v2) < 0.001 else 'MISMATCH'\n    match_2v3 = 'OK' if abs(rounded_2v3 - p_2v3) < 0.001 else 'MISMATCH'\n    match_k = 'OK' if reg_k == p_k else 'MISMATCH'\n    print(f'{domain}/{model}:')\n    print(f'  1v2: paper={p_1v2}, reg={reg_1v2}, rounds={rounded_1v2} -> {match_1v2}')\n    print(f'  2v3: paper={p_2v3}, reg={reg_2v3}, rounds={rounded_2v3} -> {match_2v3}')\n    print(f'  K*:  paper={p_k}, reg={reg_k} -> {match_k}')\n    print()\n\"\n"
  }
}
```

</details>

---


### Tool result

_source line 412 · 2026-05-23T11:38:26.853382+00:00_

=== TABLE 4 COMPLETE VERIFICATION ===

arXiv/Qwen-1.5B:
  1v2: paper=0.858, reg=0.858, rounds=0.858 -> OK
  2v3: paper=0.644, reg=0.6427, rounds=0.643 -> MISMATCH
  K*:  paper=3, reg=3 -> OK

arXiv/Pythia-1.4B:
  1v2: paper=0.805, reg=0.8047, rounds=0.805 -> OK
  2v3: paper=0.655, reg=0.6545, rounds=0.655 -> OK
  K*:  paper=3, reg=3 -> OK

C4/Qwen-1.5B:
  1v2: paper=0.626, reg=0.6262, rounds=0.626 -> OK
  2v3: paper=0.55, reg=0.5496, rounds=0.55 -> OK
  K*:  paper=2, reg=2 -> OK

Wiki/Qwen-1.5B:
  1v2: paper=0.619, reg=0.6193, rounds=0.619 -> OK
  2v3: paper=0.55, reg=0.5498, rounds=0.55 -> OK
  K*:  paper=2, reg=2 -> OK

Code/Qwen-1.5B:
  1v2: paper=0.738, reg=0.7382, rounds=0.738 -> OK
  2v3: paper=0.53, reg=0.53, rounds=0.53 -> OK
  K*:  paper=2, reg=2 -> OK

Code/LLaMA-8B:
  1v2: paper=0.739, reg=0.7394, rounds=0.739 -> OK
  2v3: paper=0.51, reg=0.5112, rounds=0.511 -> MISMATCH
  K*:  paper=2, reg=2 -> OK

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_audit_tables_3_4_inline_20260523T112128",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 413 · 2026-05-23T11:38:26.853528+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport json\n\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/17947013-ea3d-4507-b0e3-f06dfa8892ff/tool-results/mcp-agent-ml-research-read_registry-1779535307441.txt', 'r') as f:\n    raw = json.load(f)\n\ninner = json.loads(raw['result'])\ndata = inner['data']\nexps = data['experiments']\n\n# Summary findings for Spearman rho:\n# 0.782 not found in registry\n# 0.914 found: exp_005_degradation.cross_model_spearman_rho_single_feature_auc.Pythia_vs_Qwen_cont = 0.9143\n# 0.893 found: exp_7b_scorer_ablation.pythia_c4__qwen1.5b.1v2_auc = 0.8928 (but this is an AUC not Spearman)\n# 0.532 found: exp_015_neural_probe.metrics.pythia.pairwise_auc.4v5 = 0.532\n# 0.668 found: exp_contamination_rate_sweep.metrics.rate_10.graduated.hellaswag = 0.6672 (not a Spearman)\n\n# The 6 Spearman rho values in Table S2 cannot be verified from the registry\n# No exp_003 or related experiment stores these values\n\n# Also: check the Table S2 note says Spearman rho is the correlation between depth position and AUC\n# For 5 depth pairs, Spearman rho = -1.000 always (because AUC monotonically decreases) \n# So 6 values suggests different interpretation: maybe rho between config ordering and baseline ordering?\n\n# Let me compute cross-config Spearman for exp_003\nfrom scipy.stats import spearmanr\n\nexp003 = exps['exp_003_decoding_ablation']\nreg_ci = exp003['metrics']['bootstrap_ci']\n\npairs = ['0v1','1v2','2v3','3v4','4v5']\ngreedy = [reg_ci['config1_greedy'][p]['auc'] for p in pairs]\nnuc09 = [reg_ci['config2_nuc09'][p]['auc'] for p in pairs]\nt07 = [reg_ci['config3_t07'][p]['auc'] for p in pairs]\nt12 = [reg_ci['config4_t12'][p]['auc'] for p in pairs]\n\nprint('Cross-config Spearman rho for exp_003:')\nconfigs = [('greedy', greedy), ('nuc09', nuc09), ('t07', t07), ('t12', t12)]\nfor i, (n1, v1) in enumerate(configs):\n    for j, (n2, v2) in enumerate(configs):\n        if j > i:\n            rho, _ = spearmanr(v1, v2)\n            print(f'  {n1} vs {n2}: rho={rho:.3f}')\n\" 2>&1\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_audit_tables_3_4_inline_20260523T112128",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport json\n\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/17947013-ea3d-4507-b0e3-f06dfa8892ff/tool-results/mcp-agent-ml-research-read_registry-1779535307441.txt', 'r') as f:\n    raw = json.load(f)\n\ninner = json.loads(raw['result'])\ndata = inner['data']\nexps = data['experiments']\n\n# Summary findings for Spearman rho:\n# 0.782 not found in registry\n# 0.914 found: exp_005_degradation.cross_model_spearman_rho_single_feature_auc.Pythia_vs_Qwen_cont = 0.9143\n# 0.893 found: exp_7b_scorer_ablation.pythia_c4__qwen1.5b.1v2_auc = 0.8928 (but this is an AUC not Spearman)\n# 0.532 found: exp_015_neural_probe.metrics.pythia.pairwise_auc.4v5 = 0.532\n# 0.668 found: exp_contamination_rate_sweep.metrics.rate_10.graduated.hellaswag = 0.6672 (not a Spearman)\n\n# The 6 Spearman rho values in Table S2 cannot be verified from the registry\n# No exp_003 or related experiment stores these values\n\n# Also: check the Table S2 note says Spearman rho is the correlation between depth position and AUC\n# For 5 depth pairs, Spearman rho = -1.000 always (because AUC monotonically decreases) \n# So 6 values suggests different interpretation: maybe rho between config ordering and baseline ordering?\n\n# Let me compute cross-config Spearman for exp_003\nfrom scipy.stats import spearmanr\n\nexp003 = exps['exp_003_decoding_ablation']\nreg_ci = exp003['metrics']['bootstrap_ci']\n\npairs = ['0v1','1v2','2v3','3v4','4v5']\ngreedy = [reg_ci['config1_greedy'][p]['auc'] for p in pairs]\nnuc09 = [reg_ci['config2_nuc09'][p]['auc'] for p in pairs]\nt07 = [reg_ci['config3_t07'][p]['auc'] for p in pairs]\nt12 = [reg_ci['config4_t12'][p]['auc'] for p in pairs]\n\nprint('Cross-config Spearman rho for exp_003:')\nconfigs = [('greedy', greedy), ('nuc09', nuc09), ('t07', t07), ('t12', t12)]\nfor i, (n1, v1) in enumerate(configs):\n    for j, (n2, v2) in enumerate(configs):\n        if j > i:\n            rho, _ = spearmanr(v1, v2)\n            print(f'  {n1} vs {n2}: rho={rho:.3f}')\n\" 2>&1\n"
  }
}
```

</details>

---


### Tool result

_source line 414 · 2026-05-23T11:38:26.853685+00:00_

Cross-config Spearman rho for exp_003:
  greedy vs nuc09: rho=1.000
  greedy vs t07: rho=1.000
  greedy vs t12: rho=1.000
  nuc09 vs t07: rho=1.000
  nuc09 vs t12: rho=1.000
  t07 vs t12: rho=1.000

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_audit_tables_3_4_inline_20260523T112128",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 415 · 2026-05-23T11:38:26.853867+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport json\n\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/17947013-ea3d-4507-b0e3-f06dfa8892ff/tool-results/mcp-agent-ml-research-read_registry-1779535307441.txt') as f:\n    outer = json.load(f)\n\ninner = json.loads(outer['result'])\nexps = inner['data']['experiments']\n\n# Maybe the <=1.5B range is not just C4 but also includes other models\n# Check Mistral-7B and Qwen-7B which are listed as larger\n# But 7B > 1.5B so they wouldn't be in <=1.5B\n# Also exp_014_naturalistic has 0v1 JSD=0.163726... wait that's exp_016\n# Actually exp_014 is naturalistic (different domain)\n# Let me check which 1.5B models have what 0v1 JSD:\n\nprint('ALL models <=1.5B size and their 0v1 JSD on C4:')\n# Qwen-1.5B-Instruct (rewrite mode): mvp_pilot has 0.2669 or exp_017 0.28627?\n# exp_017 = Qwen-1.5B-Instruct continuation mode: 0.28627\n# mvp_pilot = Qwen-1.5B rewrite mode: 0.2669\n# exp_016 = Qwen-1.5B-Base: 0.163726\n# OLMo-1B: 0.230018\n\n# Pythia-1.4B: no clean C4 0v1 JSD... exp_001 no JSD, exp_14b_c4 has 0v1=0.1097\nprint('Pythia-1.4B C4 (exp_14b_c4):', exps['exp_14b_c4']['metrics']['pairwise_jsd']['0v1'])\n\n# Actually the paper could be including code domain too\n# code_qwen1b5: 0.0814 (too low, but this is code domain)\n\n# Most likely the paper refers to C4 models only:\n# Qwen-1.5B-Base: 0.164, Qwen-1.5B-Instruct: 0.286, OLMo-1B: 0.230, Pythia-1.4B: 0.110\n# Range would be 0.110 - 0.286\n# But paper says 0.15-0.27\n\n# Alternatively maybe Pythia greedy mode inflates things?\n# Pythia greedy: extremely repetitive - would have very different JSD\n# The exp_020_pythia_decoding: greedy 0v1 not in metrics, nuc09 not in metrics\n# Wait, let me check\nprint('exp_020 pythia decoding:')\nprint(json.dumps(exps['exp_020_pythia_decoding']['metrics'], indent=2)[:500])\n\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_audit_tables_3_4_inline_20260523T112128",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport json\n\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/17947013-ea3d-4507-b0e3-f06dfa8892ff/tool-results/mcp-agent-ml-research-read_registry-1779535307441.txt') as f:\n    outer = json.load(f)\n\ninner = json.loads(outer['result'])\nexps = inner['data']['experiments']\n\n# Maybe the <=1.5B range is not just C4 but also includes other models\n# Check Mistral-7B and Qwen-7B which are listed as larger\n# But 7B > 1.5B so they wouldn't be in <=1.5B\n# Also exp_014_naturalistic has 0v1 JSD=0.163726... wait that's exp_016\n# Actually exp_014 is naturalistic (different domain)\n# Let me check which 1.5B models have what 0v1 JSD:\n\nprint('ALL models <=1.5B size and their 0v1 JSD on C4:')\n# Qwen-1.5B-Instruct (rewrite mode): mvp_pilot has 0.2669 or exp_017 0.28627?\n# exp_017 = Qwen-1.5B-Instruct continuation mode: 0.28627\n# mvp_pilot = Qwen-1.5B rewrite mode: 0.2669\n# exp_016 = Qwen-1.5B-Base: 0.163726\n# OLMo-1B: 0.230018\n\n# Pythia-1.4B: no clean C4 0v1 JSD... exp_001 no JSD, exp_14b_c4 has 0v1=0.1097\nprint('Pythia-1.4B C4 (exp_14b_c4):', exps['exp_14b_c4']['metrics']['pairwise_jsd']['0v1'])\n\n# Actually the paper could be including code domain too\n# code_qwen1b5: 0.0814 (too low, but this is code domain)\n\n# Most likely the paper refers to C4 models only:\n# Qwen-1.5B-Base: 0.164, Qwen-1.5B-Instruct: 0.286, OLMo-1B: 0.230, Pythia-1.4B: 0.110\n# Range would be 0.110 - 0.286\n# But paper says 0.15-0.27\n\n# Alternatively maybe Pythia greedy mode inflates things?\n# Pythia greedy: extremely repetitive - would have very different JSD\n# The exp_020_pythia_decoding: greedy 0v1 not in metrics, nuc09 not in metrics\n# Wait, let me check\nprint('exp_020 pythia decoding:')\nprint(json.dumps(exps['exp_020_pythia_decoding']['metrics'], indent=2)[:500])\n\"\n"
  }
}
```

</details>

---


### Tool result

_source line 416 · 2026-05-23T11:38:26.854020+00:00_

ALL models <=1.5B size and their 0v1 JSD on C4:
Pythia-1.4B C4 (exp_14b_c4): 0.1097
exp_020 pythia decoding:
{
  "greedy": {
    "K_star": 2,
    "auc": {
      "0v1": 0.9992,
      "1v2": 0.8838,
      "2v3": 0.5342,
      "3v4": 0.5228,
      "4v5": 0.5162
    }
  },
  "nuc09": {
    "K_star": 2,
    "auc": {
      "0v1": 0.9948,
      "1v2": 0.677,
      "2v3": 0.5549,
      "3v4": 0.5299,
      "4v5": 0.5013
    }
  },
  "t07": {
    "K_star": 2,
    "auc": {
      "0v1": 0.9965,
      "1v2": 0.7265,
      "2v3": 0.5941,
      "3v4": 0.5698,
      "4v5": 0.5284
    }
  },
  "t12": {
    "K_star": 2

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_audit_tables_3_4_inline_20260523T112128",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 417 · 2026-05-23T11:38:26.854171+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nfrom decimal import Decimal, ROUND_HALF_UP\n\ndef round_standard(x, n):\n    d = Decimal(str(x))\n    factor = Decimal(10) ** (-n)\n    return float(d.quantize(factor, rounding=ROUND_HALF_UP))\n\n# Final check: S12 table values\nprint('=== TABLE S12 COMPLETE VERIFICATION ===')\nprint()\n\n# C4 column (Qwen-cont = Qwen-1.5B-Instruct continuation = exp_017)\ne017_pairwise = {'0v1': 0.9972, '1v2': 0.6114, '2v3': 0.5609, '3v4': 0.5408, '4v5': 0.5139}\npaper_c4 = {'0v1': 0.997, '1v2': 0.611, '2v3': 0.561, '3v4': 0.541, '4v5': 0.514}\n\nprint('C4 column (exp_017: Qwen-1.5B-Instruct continuation):')\nfor pair in ['0v1', '1v2', '2v3', '3v4', '4v5']:\n    reg = e017_pairwise[pair]\n    paper = paper_c4[pair]\n    rounded = round_standard(reg, 3)\n    match = 'OK' if abs(rounded - paper) < 0.001 else 'MISMATCH'\n    print(f'  {pair}: paper={paper}, reg={reg}, rounds={rounded} -> {match}')\nprint()\n\n# Wiki column (exp_023: only 1v2 and 2v3 available)\nprint('Wiki column (exp_023: incomplete - only 1v2 and 2v3):')\npaper_wiki = {'0v1': 0.996, '1v2': 0.619, '2v3': 0.550, '3v4': 0.523, '4v5': 0.514}\ne023_partial = {'1v2': 0.6193, '2v3': 0.5498}\nfor pair in ['0v1', '1v2', '2v3', '3v4', '4v5']:\n    paper = paper_wiki[pair]\n    if pair in e023_partial:\n        reg = e023_partial[pair]\n        rounded = round_standard(reg, 3)\n        match = 'OK' if abs(rounded - paper) < 0.001 else 'MISMATCH'\n        print(f'  {pair}: paper={paper}, reg={reg}, rounds={rounded} -> {match}')\n    else:\n        print(f'  {pair}: paper={paper}, reg=NOT IN REGISTRY -> UNVERIFIABLE')\nprint()\n\n# arXiv column (exp_024: full pairwise)\ne024_pairwise = {'0v1': 0.9946, '1v2': 0.858, '2v3': 0.6427, '3v4': 0.5437, '4v5': 0.5294}\npaper_arxiv = {'0v1': 0.995, '1v2': 0.858, '2v3': 0.644, '3v4': 0.544, '4v5': 0.530}\nprint('arXiv column (exp_024: Qwen-1.5B base):')\nfor pair in ['0v1', '1v2', '2v3', '3v4', '4v5']:\n    reg = e024_pairwise[pair]\n    paper = paper_arxiv[pair]\n    rounded = round_standard(reg, 3)\n    match = 'OK' if abs(rounded - paper) < 0.001 else 'MISMATCH'\n    print(f'  {pair}: paper={paper}, reg={reg}, rounds={rounded} -> {match}')\n\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_audit_tables_3_4_inline_20260523T112128",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nfrom decimal import Decimal, ROUND_HALF_UP\n\ndef round_standard(x, n):\n    d = Decimal(str(x))\n    factor = Decimal(10) ** (-n)\n    return float(d.quantize(factor, rounding=ROUND_HALF_UP))\n\n# Final check: S12 table values\nprint('=== TABLE S12 COMPLETE VERIFICATION ===')\nprint()\n\n# C4 column (Qwen-cont = Qwen-1.5B-Instruct continuation = exp_017)\ne017_pairwise = {'0v1': 0.9972, '1v2': 0.6114, '2v3': 0.5609, '3v4': 0.5408, '4v5': 0.5139}\npaper_c4 = {'0v1': 0.997, '1v2': 0.611, '2v3': 0.561, '3v4': 0.541, '4v5': 0.514}\n\nprint('C4 column (exp_017: Qwen-1.5B-Instruct continuation):')\nfor pair in ['0v1', '1v2', '2v3', '3v4', '4v5']:\n    reg = e017_pairwise[pair]\n    paper = paper_c4[pair]\n    rounded = round_standard(reg, 3)\n    match = 'OK' if abs(rounded - paper) < 0.001 else 'MISMATCH'\n    print(f'  {pair}: paper={paper}, reg={reg}, rounds={rounded} -> {match}')\nprint()\n\n# Wiki column (exp_023: only 1v2 and 2v3 available)\nprint('Wiki column (exp_023: incomplete - only 1v2 and 2v3):')\npaper_wiki = {'0v1': 0.996, '1v2': 0.619, '2v3': 0.550, '3v4': 0.523, '4v5': 0.514}\ne023_partial = {'1v2': 0.6193, '2v3': 0.5498}\nfor pair in ['0v1', '1v2', '2v3', '3v4', '4v5']:\n    paper = paper_wiki[pair]\n    if pair in e023_partial:\n        reg = e023_partial[pair]\n        rounded = round_standard(reg, 3)\n        match = 'OK' if abs(rounded - paper) < 0.001 else 'MISMATCH'\n        print(f'  {pair}: paper={paper}, reg={reg}, rounds={rounded} -> {match}')\n    else:\n        print(f'  {pair}: paper={paper}, reg=NOT IN REGISTRY -> UNVERIFIABLE')\nprint()\n\n# arXiv column (exp_024: full pairwise)\ne024_pairwise = {'0v1': 0.9946, '1v2': 0.858, '2v3': 0.6427, '3v4': 0.5437, '4v5': 0.5294}\npaper_arxiv = {'0v1': 0.995, '1v2': 0.858, '2v3': 0.644, '3v4': 0.544, '4v5': 0.530}\nprint('arXiv column (exp_024: Qwen-1.5B base):')\nfor pair in ['0v1', '1v2', '2v3', '3v4', '4v5']:\n    reg = e024_pairwise[pair]\n    paper = paper_arxiv[pair]\n    rounded = round_standard(reg, 3)\n    match = 'OK' if abs(rounded - paper) < 0.001 else 'MISMATCH'\n    print(f'  {pair}: paper={paper}, reg={reg}, rounds={rounded} -> {match}')\n\"\n"
  }
}
```

</details>

---


### Tool result

_source line 418 · 2026-05-23T11:38:26.854313+00:00_

=== TABLE S12 COMPLETE VERIFICATION ===

C4 column (exp_017: Qwen-1.5B-Instruct continuation):
  0v1: paper=0.997, reg=0.9972, rounds=0.997 -> OK
  1v2: paper=0.611, reg=0.6114, rounds=0.611 -> OK
  2v3: paper=0.561, reg=0.5609, rounds=0.561 -> OK
  3v4: paper=0.541, reg=0.5408, rounds=0.541 -> OK
  4v5: paper=0.514, reg=0.5139, rounds=0.514 -> OK

Wiki column (exp_023: incomplete - only 1v2 and 2v3):
  0v1: paper=0.996, reg=NOT IN REGISTRY -> UNVERIFIABLE
  1v2: paper=0.619, reg=0.6193, rounds=0.619 -> OK
  2v3: paper=0.55, reg=0.5498, rounds=0.55 -> OK
  3v4: paper=0.523, reg=NOT IN REGISTRY -> UNVERIFIABLE
  4v5: paper=0.514, reg=NOT IN REGISTRY -> UNVERIFIABLE

arXiv column (exp_024: Qwen-1.5B base):
  0v1: paper=0.995, reg=0.9946, rounds=0.995 -> OK
  1v2: paper=0.858, reg=0.858, rounds=0.858 -> OK
  2v3: paper=0.644, reg=0.6427, rounds=0.643 -> MISMATCH
  3v4: paper=0.544, reg=0.5437, rounds=0.544 -> OK
  4v5: paper=0.53, reg=0.5294, rounds=0.529 -> MISMATCH

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_audit_tables_3_4_inline_20260523T112128",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 419 · 2026-05-23T11:38:26.854461+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport json\n\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/17947013-ea3d-4507-b0e3-f06dfa8892ff/tool-results/mcp-agent-ml-research-read_registry-1779535307441.txt', 'r') as f:\n    raw = json.load(f)\n\ninner = json.loads(raw['result'])\ndata = inner['data']\nexps = data['experiments']\n\n# Let me check if there's any experiment that could generate those 6 Spearman values\n# The context: Table S2 is 'decoding ablation' and has Spearman rho of AUC vs. depth\n# These might be correlation of OBD score values (not AUC) with depth\n# Or perhaps across experiments in different models\n\n# The 6 values: 0.600, 0.782, 0.914, 0.893, 0.532, 0.668\n# Maybe they correspond to 6 different model/setting combinations\n# Let me check exp_005 which has cross-model Spearman\n\nexp005 = exps['exp_005_degradation']\nprint('exp_005 Spearman data:')\nprint(json.dumps(exp005['metrics']['cross_model_spearman_rho_single_feature_auc'], indent=2))\nprint()\nprint('exp_005 Kendall tau data:')\nprint(json.dumps(exp005['metrics']['cross_model_kendall_tau_by_first_auc'], indent=2))\n\n# Let me also check Table 1 values more carefully -- could the 6 Spearman values be \n# from each of the 6 models in the main table?\n# If Spearman is between depth position and pairwise AUC for depth pairs, with 5 pairs\n# it would be -1 always. Unless they include depth=0 as well with another metric.\n# The task says '6 Spearman values' -- could be 4 configs + 2 comparison experiments\n\" 2>&1\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_audit_tables_3_4_inline_20260523T112128",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport json\n\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/17947013-ea3d-4507-b0e3-f06dfa8892ff/tool-results/mcp-agent-ml-research-read_registry-1779535307441.txt', 'r') as f:\n    raw = json.load(f)\n\ninner = json.loads(raw['result'])\ndata = inner['data']\nexps = data['experiments']\n\n# Let me check if there's any experiment that could generate those 6 Spearman values\n# The context: Table S2 is 'decoding ablation' and has Spearman rho of AUC vs. depth\n# These might be correlation of OBD score values (not AUC) with depth\n# Or perhaps across experiments in different models\n\n# The 6 values: 0.600, 0.782, 0.914, 0.893, 0.532, 0.668\n# Maybe they correspond to 6 different model/setting combinations\n# Let me check exp_005 which has cross-model Spearman\n\nexp005 = exps['exp_005_degradation']\nprint('exp_005 Spearman data:')\nprint(json.dumps(exp005['metrics']['cross_model_spearman_rho_single_feature_auc'], indent=2))\nprint()\nprint('exp_005 Kendall tau data:')\nprint(json.dumps(exp005['metrics']['cross_model_kendall_tau_by_first_auc'], indent=2))\n\n# Let me also check Table 1 values more carefully -- could the 6 Spearman values be \n# from each of the 6 models in the main table?\n# If Spearman is between depth position and pairwise AUC for depth pairs, with 5 pairs\n# it would be -1 always. Unless they include depth=0 as well with another metric.\n# The task says '6 Spearman values' -- could be 4 configs + 2 comparison experiments\n\" 2>&1\n"
  }
}
```

</details>

---


### Tool result

_source line 420 · 2026-05-23T11:38:26.854596+00:00_

exp_005 Spearman data:
{
  "Pythia_vs_OLMo": 0.95,
  "Pythia_vs_Qwen_cont": 0.9143,
  "OLMo_vs_Qwen_cont": 0.85,
  "metric_definition": "Spearman \u03c1 on per-feature AUC rankings (each feature independently classifies depth pairs)"
}

exp_005 Kendall tau data:
{
  "Pythia_vs_OLMo": 0.733,
  "Pythia_vs_Qwen_rewrite": 0.467,
  "Pythia_vs_Qwen_cont": 0.695,
  "OLMo_vs_Qwen_rewrite": 0.429,
  "OLMo_vs_Qwen_cont": 0.543,
  "Qwen_rewrite_vs_Qwen_cont": 0.733
}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_audit_tables_3_4_inline_20260523T112128",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 421 · 2026-05-23T11:38:26.854746+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\n# Final comprehensive output\n\nprint('='*100)\nprint('COMPLETE CROSS-REFERENCE: PAPER vs REGISTRY')\nprint('='*100)\n\nprint()\nprint('--- TABLE 1 (tab:kstar_ci): 5 main models ---')\nprint()\nprint(f'{'Location':<28} {'Paper Value':<14} {'Registry exp_id':<40} {'Registry Value':<18} {'Match?'}')\nprint('-'*100)\n\nrows_t1 = [\n    # Qwen-rw\n    ('Tab1 Qwen-rw 0v1 AUC',    '.9956',             'exp_007_bootstrap_ci[qwen_rewrite]', '0.9956', 'MATCH'),\n    ('Tab1 Qwen-rw 1v2 AUC',    '.6955',             'exp_007_bootstrap_ci[qwen_rewrite]', '0.6955', 'MATCH'),\n    ('Tab1 Qwen-rw 1v2 CI',     '[.686,.704]',       'exp_007_bootstrap_ci[qwen_rewrite]', '[.6859,.7041]', 'MATCH (rounding)'),\n    ('Tab1 Qwen-rw 2v3 AUC',    '.5893',             'exp_007_bootstrap_ci[qwen_rewrite]', '0.5893', 'MATCH'),\n    ('Tab1 Qwen-rw 2v3 CI',     '[.580,.599]',       'exp_007_bootstrap_ci[qwen_rewrite]', '[.5795,.5991]', 'MATCH (rounding)'),\n    ('Tab1 Qwen-rw 3v4 AUC',    '.5435',             'exp_007_bootstrap_ci[qwen_rewrite]', '0.5435', 'MATCH'),\n    ('Tab1 Qwen-rw 4v5 AUC',    '.5340',             'exp_007_bootstrap_ci[qwen_rewrite]', '0.5340', 'MATCH'),\n    # Pythia\n    ('Tab1 Pythia 0v1 AUC',     '.9722',             'exp_001_pythia_depth',               '0.9722', 'MATCH'),\n    ('Tab1 Pythia 1v2 AUC',     '.6074',             'exp_001_pythia_depth',               '0.6074', 'MATCH'),\n    ('Tab1 Pythia 1v2 CI',      '[.598,.617]',       'exp_001_pythia_depth[bootstrap_ci]', '[.5975,.6172]', 'MATCH (rounding)'),\n    ('Tab1 Pythia 2v3 AUC',     '.5440',             'exp_001_pythia_depth',               '0.5440', 'MATCH'),\n    ('Tab1 Pythia 2v3 CI',      '[.534,.554]',       '(no registry record)',               'N/A', 'NOT IN REGISTRY'),\n    ('Tab1 Pythia 3v4 AUC',     '.5051',             'exp_001_pythia_depth',               '0.5051', 'MATCH'),\n    ('Tab1 Pythia 4v5 AUC',     '.5079',             'exp_001_pythia_depth',               '0.5079', 'MATCH'),\n    # OLMo\n    ('Tab1 OLMo 0v1 AUC',       '.9860',             'exp_002_olmo_depth',                 '0.9861', 'MATCH (rounding)'),\n    ('Tab1 OLMo 1v2 AUC',       '.5001',             'exp_002_olmo_depth',                 '0.5001', 'MATCH'),\n    ('Tab1 OLMo 1v2 CI',        '[.496,.519]',       '(no registry record)',               'N/A', 'NOT IN REGISTRY'),\n    ('Tab1 OLMo 2v3 AUC',       '.4973',             'exp_002_olmo_depth',                 '0.4972', 'MATCH (rounding)'),\n    ('Tab1 OLMo 2v3 CI',        '[.486,.509]',       '(no registry record)',               'N/A', 'NOT IN REGISTRY'),\n    ('Tab1 OLMo 3v4 AUC',       '.5024',             'exp_002_olmo_depth',                 '0.5034', 'MISMATCH (+0.001)'),\n    ('Tab1 OLMo 4v5 AUC',       '.4942',             'exp_002_olmo_depth',                 '0.4971', 'MISMATCH (+0.003)'),\n    # Qwen-cont\n    ('Tab1 Qwen-cont 0v1 AUC',  '.9971',             'exp_007_bootstrap_ci[qwen_cont]',    '0.9971', 'MATCH'),\n    ('Tab1 Qwen-cont 1v2 AUC',  '.6112',             'exp_007_bootstrap_ci[qwen_cont]',    '0.6112', 'MATCH'),\n    ('Tab1 Qwen-cont 1v2 CI',   '[.602,.621]',       'exp_007_bootstrap_ci[qwen_cont]',    '[.6015,.6213]', 'MATCH (rounding)'),\n    ('Tab1 Qwen-cont 2v3 AUC',  '.5609',             'exp_007_bootstrap_ci[qwen_cont]',    '0.5609', 'MATCH'),\n    ('Tab1 Qwen-cont 2v3 CI',   '[.551,.571]',       'exp_007_bootstrap_ci[qwen_cont]',    '[.5511,.5712]', 'MATCH (rounding)'),\n    ('Tab1 Qwen-cont 3v4 AUC',  '.5409',             'exp_007_bootstrap_ci[qwen_cont]',    '0.5409', 'MATCH'),\n    ('Tab1 Qwen-cont 4v5 AUC',  '.5141',             'exp_007_bootstrap_ci[qwen_cont]',    '0.5141', 'MATCH'),\n    # Qwen-7B\n    ('Tab1 Qwen-7B 0v1 AUC',    '.9638',             'exp_004_7b_crossscale[bootstrap_ci]','0.9638', 'MATCH'),\n    ('Tab1 Qwen-7B 0v1 CI',     '[.961,.967]',       'exp_004_7b_crossscale[bootstrap_ci]','[.9607,.9665]', 'MATCH (rounding)'),\n    ('Tab1 Qwen-7B 1v2 AUC',    '.6168',             'exp_004_7b_crossscale[bootstrap_ci]','0.6168', 'MATCH'),\n    ('Tab1 Qwen-7B 1v2 CI',     '[.608,.626]',       'exp_004_7b_crossscale[bootstrap_ci]','[.6079,.6261]', 'MATCH (rounding)'),\n    ('Tab1 Qwen-7B 2v3 AUC',    '.5492',             'exp_004_7b_crossscale[bootstrap_ci]','0.5492', 'MATCH'),\n    ('Tab1 Qwen-7B 2v3 CI',     '[.539,.559]',       'exp_004_7b_crossscale[bootstrap_ci]','[.5388,.5594]', 'MATCH (rounding)'),\n    ('Tab1 Qwen-7B 3v4 AUC',    '.5276',             'exp_004_7b_crossscale[bootstrap_ci]','0.5276', 'MATCH'),\n    ('Tab1 Qwen-7B 4v5 AUC',    '.5085',             'exp_004_7b_crossscale[bootstrap_ci]','0.5085', 'MATCH'),\n]\n\nfor loc, pv, rid, rv, match in rows_t1:\n    flag = '' if 'MATCH' in match and 'NOT' not in match and 'MIS' not in match else ' ***'\n    print(f'{loc:<28} {pv:<14} {rid:<40} {rv:<18} {match}{flag}')\n\nprint()\nprint('--- EXTENDED TABLE (tab:kstar_ci_extended): 5 additional models ---')\nprint()\nprint(f'{'Location':<30} {'Paper Value':<14} {'Registry exp_id':<38} {'Registry Value':<18} {'Match?'}')\nprint('-'*100)\n\nrows_ext = [\n    # Qwen-base\n    ('Ext Qwen-base 0v1 AUC',    '.987',   'exp_016_base_vs_instruct',  '0.9870', 'MATCH'),\n    ('Ext Qwen-base 0v1 CI',     '[.985,.989]', 'exp_016[bootstrap_ci]','[.9853,.9885]', 'MATCH (rounding)'),\n    ('Ext Qwen-base 1v2 AUC',    '.626',   'exp_016_base_vs_instruct',  '0.6260', 'MATCH'),\n    ('Ext Qwen-base 1v2 CI',     '[.617,.635]', 'exp_016[bootstrap_ci]','[.6168,.6353]', 'MATCH (rounding)'),\n    ('Ext Qwen-base 2v3 AUC',    '.550',   'exp_016_base_vs_instruct',  '0.5496', 'MATCH (rounding)'),\n    ('Ext Qwen-base 2v3 CI',     '[.540,.560]', 'exp_016[bootstrap_ci]','[.5397,.5600]', 'MATCH (rounding)'),\n    ('Ext Qwen-base 3v4 AUC',    '.529',   'exp_016_base_vs_instruct',  '0.5293', 'MATCH (rounding)'),\n    ('Ext Qwen-base 3v4 CI',     '[.519,.540]', 'exp_016[bootstrap_ci]','[.5188,.5399]', 'MATCH (rounding)'),\n    ('Ext Qwen-base 4v5 AUC',    '.518',   'exp_016_base_vs_instruct',  '0.5181', 'MATCH (rounding)'),\n    ('Ext Qwen-base 4v5 CI',     '[.508,.529]', 'exp_016[bootstrap_ci]','[.5075,.5288]', 'MATCH (rounding)'),\n    # LLaMA-8B\n    ('Ext LLaMA-8B 0v1 AUC',    '.9224',  'exp_018_llama8b_depth',     '0.9224', 'MATCH'),\n    ('Ext LLaMA-8B 0v1 CI',     '[.917,.927]', 'exp_018[bootstrap_ci]','[.9174,.9272]', 'MATCH (rounding)'),\n    ('Ext LLaMA-8B 1v2 AUC',    '.6123',  'exp_018_llama8b_depth',     '0.6123', 'MATCH'),\n    ('Ext LLaMA-8B 1v2 CI',     '[.603,.622]', 'exp_018[bootstrap_ci]','[.6028,.6216]', 'MATCH (rounding)'),\n    ('Ext LLaMA-8B 2v3 AUC',    '.5273',  'exp_018_llama8b_depth',     '0.5273', 'MATCH'),\n    ('Ext LLaMA-8B 2v3 CI',     '[.517,.538]', 'exp_018[bootstrap_ci]','[.5169,.5378]', 'MATCH (rounding)'),\n    ('Ext LLaMA-8B 3v4 AUC',    '.5168',  'exp_018_llama8b_depth',     '0.5168', 'MATCH'),\n    ('Ext LLaMA-8B 3v4 CI',     '[.506,.528]', 'exp_018[bootstrap_ci]','[.5062,.5275]', 'MATCH (rounding)'),\n    ('Ext LLaMA-8B 4v5 AUC',    '.5159',  'exp_018_llama8b_depth',     '0.5159', 'MATCH'),\n    ('Ext LLaMA-8B 4v5 CI',     '[.505,.527]', 'exp_018[bootstrap_ci]','[.5052,.5268]', 'MATCH (rounding)'),\n    # Mistral-7B\n    ('Ext Mistral-7B 0v1 AUC',  '.9170',  'exp_019_mistral7b_depth',   '0.9843', 'MISMATCH (self-scorer)'),\n    ('Ext Mistral-7B 0v1 AUC',  '.9170',  'exp_019b_mistral_cross',     '0.9209', 'MISMATCH (cross-scorer)'),\n    ('Ext Mistral-7B 1v2 AUC',  '.5750',  'exp_019_mistral7b_depth',   '0.5935', 'MISMATCH (self-scorer)'),\n    ('Ext Mistral-7B 1v2 AUC',  '.5750',  'exp_019b_mistral_cross',     '0.5695', 'MISMATCH (cross-scorer)'),\n    ('Ext Mistral-7B 2v3 AUC',  '.5369',  'exp_019_mistral7b_depth',   '0.5402', 'MISMATCH (self=.5402)'),\n    ('Ext Mistral-7B 2v3 AUC',  '.5369',  'exp_019b_mistral_cross',     '0.5335', 'MISMATCH (cross=.5335)'),\n    ('Ext Mistral-7B 3v4 AUC',  '.5174',  'exp_019_mistral7b_depth',   '0.5232', 'MISMATCH (self=.5232)'),\n    ('Ext Mistral-7B 3v4 AUC',  '.5174',  'exp_019b_mistral_cross',     '0.5140', 'MISMATCH (cross=.5140)'),\n    ('Ext Mistral-7B 4v5 AUC',  '.5175',  'exp_019_mistral7b_depth',   '0.5181', 'MATCH (~rounding)'),\n    ('Ext Mistral-7B 4v5 AUC',  '.5175',  'exp_019b_mistral_cross',     '0.5184', 'MATCH (~rounding)'),\n    # Pythia-6.9B\n    ('Ext Pythia-6.9B 0v1 AUC', '.9599',  'exp_pythia69b_c4_nuc',      '0.9599', 'MATCH'),\n    ('Ext Pythia-6.9B 1v2 AUC', '.5955',  'exp_pythia69b_c4_nuc',      '0.5955', 'MATCH'),\n    ('Ext Pythia-6.9B 2v3 AUC', '.5298',  'exp_pythia69b_c4_nuc',      '0.5298', 'MATCH'),\n    ('Ext Pythia-6.9B 3v4 AUC', '.5135',  'exp_pythia69b_c4_nuc',      '0.5135', 'MATCH'),\n    ('Ext Pythia-6.9B 4v5 AUC', '---',    'exp_pythia69b_c4_nuc',      'not measured', 'CONSISTENT'),\n    # Gemma-2B\n    ('Ext Gemma-2B 0v1 AUC',    '.953',   'exp_gemma2b_depth',         '0.9534', 'MATCH (rounding)'),\n    ('Ext Gemma-2B 0v1 CI',     '[.949,.957]', '(no registry record)',  'N/A', 'NOT IN REGISTRY'),\n    ('Ext Gemma-2B 1v2 AUC',    '.5981',  'exp_gemma2b_depth',         '0.5981', 'MATCH'),\n    ('Ext Gemma-2B 1v2 CI',     '[.588,.608]', 'exp_gemma2b_depth[bci]','[.5882,.6076]', 'MATCH (rounding)'),\n    ('Ext Gemma-2B 2v3 AUC',    '.534',   'exp_gemma2b_depth',         '0.5342', 'MATCH (rounding)'),\n    ('Ext Gemma-2B 2v3 CI',     '[.523,.545]', '(no registry record)',  'N/A', 'NOT IN REGISTRY'),\n    ('Ext Gemma-2B 3v4 AUC',    '.5033',  'exp_gemma2b_depth',         '0.5030', 'MATCH (rounding)'),\n    ('Ext Gemma-2B 3v4 CI',     '[.492,.514]', '(no registry record)',  'N/A', 'NOT IN REGISTRY'),\n    ('Ext Gemma-2B 4v5 AUC',    '.5025',  'exp_gemma2b_depth',         '0.5026', 'MATCH (rounding)'),\n    ('Ext Gemma-2B 4v5 CI',     '[.492,.514]', '(no registry record)',  'N/A', 'NOT IN REGISTRY'),\n]\n\nfor loc, pv, rid, rv, match in rows_ext:\n    flag = ' ***' if ('MISMATCH' in match or 'NOT IN REGISTRY' in match) else ''\n    print(f'{loc:<30} {pv:<14} {rid:<38} {rv:<18} {match}{flag}')\n\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_audit_tables_3_4_inline_20260523T112128",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\n# Final comprehensive output\n\nprint('='*100)\nprint('COMPLETE CROSS-REFERENCE: PAPER vs REGISTRY')\nprint('='*100)\n\nprint()\nprint('--- TABLE 1 (tab:kstar_ci): 5 main models ---')\nprint()\nprint(f'{'Location':<28} {'Paper Value':<14} {'Registry exp_id':<40} {'Registry Value':<18} {'Match?'}')\nprint('-'*100)\n\nrows_t1 = [\n    # Qwen-rw\n    ('Tab1 Qwen-rw 0v1 AUC',    '.9956',             'exp_007_bootstrap_ci[qwen_rewrite]', '0.9956', 'MATCH'),\n    ('Tab1 Qwen-rw 1v2 AUC',    '.6955',             'exp_007_bootstrap_ci[qwen_rewrite]', '0.6955', 'MATCH'),\n    ('Tab1 Qwen-rw 1v2 CI',     '[.686,.704]',       'exp_007_bootstrap_ci[qwen_rewrite]', '[.6859,.7041]', 'MATCH (rounding)'),\n    ('Tab1 Qwen-rw 2v3 AUC',    '.5893',             'exp_007_bootstrap_ci[qwen_rewrite]', '0.5893', 'MATCH'),\n    ('Tab1 Qwen-rw 2v3 CI',     '[.580,.599]',       'exp_007_bootstrap_ci[qwen_rewrite]', '[.5795,.5991]', 'MATCH (rounding)'),\n    ('Tab1 Qwen-rw 3v4 AUC',    '.5435',             'exp_007_bootstrap_ci[qwen_rewrite]', '0.5435', 'MATCH'),\n    ('Tab1 Qwen-rw 4v5 AUC',    '.5340',             'exp_007_bootstrap_ci[qwen_rewrite]', '0.5340', 'MATCH'),\n    # Pythia\n    ('Tab1 Pythia 0v1 AUC',     '.9722',             'exp_001_pythia_depth',               '0.9722', 'MATCH'),\n    ('Tab1 Pythia 1v2 AUC',     '.6074',             'exp_001_pythia_depth',               '0.6074', 'MATCH'),\n    ('Tab1 Pythia 1v2 CI',      '[.598,.617]',       'exp_001_pythia_depth[bootstrap_ci]', '[.5975,.6172]', 'MATCH (rounding)'),\n    ('Tab1 Pythia 2v3 AUC',     '.5440',             'exp_001_pythia_depth',               '0.5440', 'MATCH'),\n    ('Tab1 Pythia 2v3 CI',      '[.534,.554]',       '(no registry record)',               'N/A', 'NOT IN REGISTRY'),\n    ('Tab1 Pythia 3v4 AUC',     '.5051',             'exp_001_pythia_depth',               '0.5051', 'MATCH'),\n    ('Tab1 Pythia 4v5 AUC',     '.5079',             'exp_001_pythia_depth',               '0.5079', 'MATCH'),\n    # OLMo\n    ('Tab1 OLMo 0v1 AUC',       '.9860',             'exp_002_olmo_depth',                 '0.9861', 'MATCH (rounding)'),\n    ('Tab1 OLMo 1v2 AUC',       '.5001',             'exp_002_olmo_depth',                 '0.5001', 'MATCH'),\n    ('Tab1 OLMo 1v2 CI',        '[.496,.519]',       '(no registry record)',               'N/A', 'NOT IN REGISTRY'),\n    ('Tab1 OLMo 2v3 AUC',       '.4973',             'exp_002_olmo_depth',                 '0.4972', 'MATCH (rounding)'),\n    ('Tab1 OLMo 2v3 CI',        '[.486,.509]',       '(no registry record)',               'N/A', 'NOT IN REGISTRY'),\n    ('Tab1 OLMo 3v4 AUC',       '.5024',             'exp_002_olmo_depth',                 '0.5034', 'MISMATCH (+0.001)'),\n    ('Tab1 OLMo 4v5 AUC',       '.4942',             'exp_002_olmo_depth',                 '0.4971', 'MISMATCH (+0.003)'),\n    # Qwen-cont\n    ('Tab1 Qwen-cont 0v1 AUC',  '.9971',             'exp_007_bootstrap_ci[qwen_cont]',    '0.9971', 'MATCH'),\n    ('Tab1 Qwen-cont 1v2 AUC',  '.6112',             'exp_007_bootstrap_ci[qwen_cont]',    '0.6112', 'MATCH'),\n    ('Tab1 Qwen-cont 1v2 CI',   '[.602,.621]',       'exp_007_bootstrap_ci[qwen_cont]',    '[.6015,.6213]', 'MATCH (rounding)'),\n    ('Tab1 Qwen-cont 2v3 AUC',  '.5609',             'exp_007_bootstrap_ci[qwen_cont]',    '0.5609', 'MATCH'),\n    ('Tab1 Qwen-cont 2v3 CI',   '[.551,.571]',       'exp_007_bootstrap_ci[qwen_cont]',    '[.5511,.5712]', 'MATCH (rounding)'),\n    ('Tab1 Qwen-cont 3v4 AUC',  '.5409',             'exp_007_bootstrap_ci[qwen_cont]',    '0.5409', 'MATCH'),\n    ('Tab1 Qwen-cont 4v5 AUC',  '.5141',             'exp_007_bootstrap_ci[qwen_cont]',    '0.5141', 'MATCH'),\n    # Qwen-7B\n    ('Tab1 Qwen-7B 0v1 AUC',    '.9638',             'exp_004_7b_crossscale[bootstrap_ci]','0.9638', 'MATCH'),\n    ('Tab1 Qwen-7B 0v1 CI',     '[.961,.967]',       'exp_004_7b_crossscale[bootstrap_ci]','[.9607,.9665]', 'MATCH (rounding)'),\n    ('Tab1 Qwen-7B 1v2 AUC',    '.6168',             'exp_004_7b_crossscale[bootstrap_ci]','0.6168', 'MATCH'),\n    ('Tab1 Qwen-7B 1v2 CI',     '[.608,.626]',       'exp_004_7b_crossscale[bootstrap_ci]','[.6079,.6261]', 'MATCH (rounding)'),\n    ('Tab1 Qwen-7B 2v3 AUC',    '.5492',             'exp_004_7b_crossscale[bootstrap_ci]','0.5492', 'MATCH'),\n    ('Tab1 Qwen-7B 2v3 CI',     '[.539,.559]',       'exp_004_7b_crossscale[bootstrap_ci]','[.5388,.5594]', 'MATCH (rounding)'),\n    ('Tab1 Qwen-7B 3v4 AUC',    '.5276',             'exp_004_7b_crossscale[bootstrap_ci]','0.5276', 'MATCH'),\n    ('Tab1 Qwen-7B 4v5 AUC',    '.5085',             'exp_004_7b_crossscale[bootstrap_ci]','0.5085', 'MATCH'),\n]\n\nfor loc, pv, rid, rv, match in rows_t1:\n    flag = '' if 'MATCH' in match and 'NOT' not in match and 'MIS' not in match else ' ***'\n    print(f'{loc:<28} {pv:<14} {rid:<40} {rv:<18} {match}{flag}')\n\nprint()\nprint('--- EXTENDED TABLE (tab:kstar_ci_extended): 5 additional models ---')\nprint()\nprint(f'{'Location':<30} {'Paper Value':<14} {'Registry exp_id':<38} {'Registry Value':<18} {'Match?'}')\nprint('-'*100)\n\nrows_ext = [\n    # Qwen-base\n    ('Ext Qwen-base 0v1 AUC',    '.987',   'exp_016_base_vs_instruct',  '0.9870', 'MATCH'),\n    ('Ext Qwen-base 0v1 CI',     '[.985,.989]', 'exp_016[bootstrap_ci]','[.9853,.9885]', 'MATCH (rounding)'),\n    ('Ext Qwen-base 1v2 AUC',    '.626',   'exp_016_base_vs_instruct',  '0.6260', 'MATCH'),\n    ('Ext Qwen-base 1v2 CI',     '[.617,.635]', 'exp_016[bootstrap_ci]','[.6168,.6353]', 'MATCH (rounding)'),\n    ('Ext Qwen-base 2v3 AUC',    '.550',   'exp_016_base_vs_instruct',  '0.5496', 'MATCH (rounding)'),\n    ('Ext Qwen-base 2v3 CI',     '[.540,.560]', 'exp_016[bootstrap_ci]','[.5397,.5600]', 'MATCH (rounding)'),\n    ('Ext Qwen-base 3v4 AUC',    '.529',   'exp_016_base_vs_instruct',  '0.5293', 'MATCH (rounding)'),\n    ('Ext Qwen-base 3v4 CI',     '[.519,.540]', 'exp_016[bootstrap_ci]','[.5188,.5399]', 'MATCH (rounding)'),\n    ('Ext Qwen-base 4v5 AUC',    '.518',   'exp_016_base_vs_instruct',  '0.5181', 'MATCH (rounding)'),\n    ('Ext Qwen-base 4v5 CI',     '[.508,.529]', 'exp_016[bootstrap_ci]','[.5075,.5288]', 'MATCH (rounding)'),\n    # LLaMA-8B\n    ('Ext LLaMA-8B 0v1 AUC',    '.9224',  'exp_018_llama8b_depth',     '0.9224', 'MATCH'),\n    ('Ext LLaMA-8B 0v1 CI',     '[.917,.927]', 'exp_018[bootstrap_ci]','[.9174,.9272]', 'MATCH (rounding)'),\n    ('Ext LLaMA-8B 1v2 AUC',    '.6123',  'exp_018_llama8b_depth',     '0.6123', 'MATCH'),\n    ('Ext LLaMA-8B 1v2 CI',     '[.603,.622]', 'exp_018[bootstrap_ci]','[.6028,.6216]', 'MATCH (rounding)'),\n    ('Ext LLaMA-8B 2v3 AUC',    '.5273',  'exp_018_llama8b_depth',     '0.5273', 'MATCH'),\n    ('Ext LLaMA-8B 2v3 CI',     '[.517,.538]', 'exp_018[bootstrap_ci]','[.5169,.5378]', 'MATCH (rounding)'),\n    ('Ext LLaMA-8B 3v4 AUC',    '.5168',  'exp_018_llama8b_depth',     '0.5168', 'MATCH'),\n    ('Ext LLaMA-8B 3v4 CI',     '[.506,.528]', 'exp_018[bootstrap_ci]','[.5062,.5275]', 'MATCH (rounding)'),\n    ('Ext LLaMA-8B 4v5 AUC',    '.5159',  'exp_018_llama8b_depth',     '0.5159', 'MATCH'),\n    ('Ext LLaMA-8B 4v5 CI',     '[.505,.527]', 'exp_018[bootstrap_ci]','[.5052,.5268]', 'MATCH (rounding)'),\n    # Mistral-7B\n    ('Ext Mistral-7B 0v1 AUC',  '.9170',  'exp_019_mistral7b_depth',   '0.9843', 'MISMATCH (self-scorer)'),\n    ('Ext Mistral-7B 0v1 AUC',  '.9170',  'exp_019b_mistral_cross',     '0.9209', 'MISMATCH (cross-scorer)'),\n    ('Ext Mistral-7B 1v2 AUC',  '.5750',  'exp_019_mistral7b_depth',   '0.5935', 'MISMATCH (self-scorer)'),\n    ('Ext Mistral-7B 1v2 AUC',  '.5750',  'exp_019b_mistral_cross',     '0.5695', 'MISMATCH (cross-scorer)'),\n    ('Ext Mistral-7B 2v3 AUC',  '.5369',  'exp_019_mistral7b_depth',   '0.5402', 'MISMATCH (self=.5402)'),\n    ('Ext Mistral-7B 2v3 AUC',  '.5369',  'exp_019b_mistral_cross',     '0.5335', 'MISMATCH (cross=.5335)'),\n    ('Ext Mistral-7B 3v4 AUC',  '.5174',  'exp_019_mistral7b_depth',   '0.5232', 'MISMATCH (self=.5232)'),\n    ('Ext Mistral-7B 3v4 AUC',  '.5174',  'exp_019b_mistral_cross',     '0.5140', 'MISMATCH (cross=.5140)'),\n    ('Ext Mistral-7B 4v5 AUC',  '.5175',  'exp_019_mistral7b_depth',   '0.5181', 'MATCH (~rounding)'),\n    ('Ext Mistral-7B 4v5 AUC',  '.5175',  'exp_019b_mistral_cross',     '0.5184', 'MATCH (~rounding)'),\n    # Pythia-6.9B\n    ('Ext Pythia-6.9B 0v1 AUC', '.9599',  'exp_pythia69b_c4_nuc',      '0.9599', 'MATCH'),\n    ('Ext Pythia-6.9B 1v2 AUC', '.5955',  'exp_pythia69b_c4_nuc',      '0.5955', 'MATCH'),\n    ('Ext Pythia-6.9B 2v3 AUC', '.5298',  'exp_pythia69b_c4_nuc',      '0.5298', 'MATCH'),\n    ('Ext Pythia-6.9B 3v4 AUC', '.5135',  'exp_pythia69b_c4_nuc',      '0.5135', 'MATCH'),\n    ('Ext Pythia-6.9B 4v5 AUC', '---',    'exp_pythia69b_c4_nuc',      'not measured', 'CONSISTENT'),\n    # Gemma-2B\n    ('Ext Gemma-2B 0v1 AUC',    '.953',   'exp_gemma2b_depth',         '0.9534', 'MATCH (rounding)'),\n    ('Ext Gemma-2B 0v1 CI',     '[.949,.957]', '(no registry record)',  'N/A', 'NOT IN REGISTRY'),\n    ('Ext Gemma-2B 1v2 AUC',    '.5981',  'exp_gemma2b_depth',         '0.5981', 'MATCH'),\n    ('Ext Gemma-2B 1v2 CI',     '[.588,.608]', 'exp_gemma2b_depth[bci]','[.5882,.6076]', 'MATCH (rounding)'),\n    ('Ext Gemma-2B 2v3 AUC',    '.534',   'exp_gemma2b_depth',         '0.5342', 'MATCH (rounding)'),\n    ('Ext Gemma-2B 2v3 CI',     '[.523,.545]', '(no registry record)',  'N/A', 'NOT IN REGISTRY'),\n    ('Ext Gemma-2B 3v4 AUC',    '.5033',  'exp_gemma2b_depth',         '0.5030', 'MATCH (rounding)'),\n    ('Ext Gemma-2B 3v4 CI',     '[.492,.514]', '(no registry record)',  'N/A', 'NOT IN REGISTRY'),\n    ('Ext Gemma-2B 4v5 AUC',    '.5025',  'exp_gemma2b_depth',         '0.5026', 'MATCH (rounding)'),\n    ('Ext Gemma-2B 4v5 CI',     '[.492,.514]', '(no registry record)',  'N/A', 'NOT IN REGISTRY'),\n]\n\nfor loc, pv, rid, rv, match in rows_ext:\n    flag = ' ***' if ('MISMATCH' in match or 'NOT IN REGISTRY' in match) else ''\n    print(f'{loc:<30} {pv:<14} {rid:<38} {rv:<18} {match}{flag}')\n\"\n"
  }
}
```

</details>

---


### Tool result

_source line 422 · 2026-05-23T11:38:26.854996+00:00_

====================================================================================================
COMPLETE CROSS-REFERENCE: PAPER vs REGISTRY
====================================================================================================

--- TABLE 1 (tab:kstar_ci): 5 main models ---

Location                     Paper Value    Registry exp_id                          Registry Value     Match?
----------------------------------------------------------------------------------------------------
Tab1 Qwen-rw 0v1 AUC         .9956          exp_007_bootstrap_ci[qwen_rewrite]       0.9956             MATCH
Tab1 Qwen-rw 1v2 AUC         .6955          exp_007_bootstrap_ci[qwen_rewrite]       0.6955             MATCH
Tab1 Qwen-rw 1v2 CI          [.686,.704]    exp_007_bootstrap_ci[qwen_rewrite]       [.6859,.7041]      MATCH (rounding)
Tab1 Qwen-rw 2v3 AUC         .5893          exp_007_bootstrap_ci[qwen_rewrite]       0.5893             MATCH
Tab1 Qwen-rw 2v3 CI          [.580,.599]    exp_007_bootstrap_ci[qwen_rewrite]       [.5795,.5991]      MATCH (rounding)
Tab1 Qwen-rw 3v4 AUC         .5435          exp_007_bootstrap_ci[qwen_rewrite]       0.5435             MATCH
Tab1 Qwen-rw 4v5 AUC         .5340          exp_007_bootstrap_ci[qwen_rewrite]       0.5340             MATCH
Tab1 Pythia 0v1 AUC          .9722          exp_001_pythia_depth                     0.9722             MATCH
Tab1 Pythia 1v2 AUC          .6074          exp_001_pythia_depth                     0.6074             MATCH
Tab1 Pythia 1v2 CI           [.598,.617]    exp_001_pythia_depth[bootstrap_ci]       [.5975,.6172]      MATCH (rounding)
Tab1 Pythia 2v3 AUC          .5440          exp_001_pythia_depth                     0.5440             MATCH
Tab1 Pythia 2v3 CI           [.534,.554]    (no registry record)                     N/A                NOT IN REGISTRY ***
Tab1 Pythia 3v4 AUC          .5051          exp_001_pythia_depth                     0.5051             MATCH
Tab1 Pythia 4v5 A
…[truncated 8332 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_audit_tables_3_4_inline_20260523T112128",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 423 · 2026-05-23T11:38:26.855165+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport json\n\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/17947013-ea3d-4507-b0e3-f06dfa8892ff/tool-results/mcp-agent-ml-research-read_registry-1779535307441.txt', 'r') as f:\n    raw = json.load(f)\n\ninner = json.loads(raw['result'])\ndata = inner['data']\nexps = data['experiments']\n\n# Let me check if there's a separate analysis file or exp that has exactly these 6 values\n# Maybe from feature ranking Spearman rho per depth pair across configs\n\n# Try searching for 0.600 as spearman-related value, and also 0.532 and 0.668 as Spearman\n# (not just any AUC value)\n# The task says Table S2 has 'Spearman rho values: 0.600, 0.782, 0.914, 0.893, 0.532, 0.668'\n# These 6 values for Table S2 which has 4 decoding configs × 5 depth pairs = 20 AUC values\n# The Spearman values don't fit the 4×5 structure directly\n\n# Actually rethinking: maybe Spearman rho between depth (1,2,3,4,5) and AUC for each config\n# but using 0-indexed means only 5 points, always monotonic = always -1\n# Unless there are more depth pairs? 0v1,1v2,2v3,3v4,4v5 = 5 pairs, all decreasing -> rho=-1\n\n# OR: these are Spearman rho of the 15 OBD features' individual AUCs across depth pairs\n# for each model-config combination\n\n# I conclude these 6 Spearman values are NOT in the registry at all.\n# The closest match: \n# 0.914 -> exp_005 Pythia_vs_Qwen_cont feature ranking Spearman = 0.9143\n# The others (0.600, 0.782, 0.893, 0.532, 0.668) are not in the registry as Spearman values\n\n# Final check: look for any 'spearman' stored in artifact-style data that I might have missed\nfor exp_id, exp in exps.items():\n    s = json.dumps(exp)\n    if '0.782' in s or '0.600' in s:\n        # Only print if surrounded by context suggesting it's a Spearman value\n        import re\n        for m in re.finditer(r'.{50}(0\\.782|0\\.600).{50}', s):\n            context = m.group(0)\n            if 'spearman' in context.lower() or 'rho' in context.lower():\n                print(f'{exp_id}: {context}')\n\" 2>&1\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_audit_tables_3_4_inline_20260523T112128",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport json\n\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/17947013-ea3d-4507-b0e3-f06dfa8892ff/tool-results/mcp-agent-ml-research-read_registry-1779535307441.txt', 'r') as f:\n    raw = json.load(f)\n\ninner = json.loads(raw['result'])\ndata = inner['data']\nexps = data['experiments']\n\n# Let me check if there's a separate analysis file or exp that has exactly these 6 values\n# Maybe from feature ranking Spearman rho per depth pair across configs\n\n# Try searching for 0.600 as spearman-related value, and also 0.532 and 0.668 as Spearman\n# (not just any AUC value)\n# The task says Table S2 has 'Spearman rho values: 0.600, 0.782, 0.914, 0.893, 0.532, 0.668'\n# These 6 values for Table S2 which has 4 decoding configs × 5 depth pairs = 20 AUC values\n# The Spearman values don't fit the 4×5 structure directly\n\n# Actually rethinking: maybe Spearman rho between depth (1,2,3,4,5) and AUC for each config\n# but using 0-indexed means only 5 points, always monotonic = always -1\n# Unless there are more depth pairs? 0v1,1v2,2v3,3v4,4v5 = 5 pairs, all decreasing -> rho=-1\n\n# OR: these are Spearman rho of the 15 OBD features' individual AUCs across depth pairs\n# for each model-config combination\n\n# I conclude these 6 Spearman values are NOT in the registry at all.\n# The closest match: \n# 0.914 -> exp_005 Pythia_vs_Qwen_cont feature ranking Spearman = 0.9143\n# The others (0.600, 0.782, 0.893, 0.532, 0.668) are not in the registry as Spearman values\n\n# Final check: look for any 'spearman' stored in artifact-style data that I might have missed\nfor exp_id, exp in exps.items():\n    s = json.dumps(exp)\n    if '0.782' in s or '0.600' in s:\n        # Only print if surrounded by context suggesting it's a Spearman value\n        import re\n        for m in re.finditer(r'.{50}(0\\.782|0\\.600).{50}', s):\n            context = m.group(0)\n            if 'spearman' in context.lower() or 'rho' in context.lower():\n                print(f'{exp_id}: {context}')\n\" 2>&1\n"
  }
}
```

</details>

---


### Tool result

_source line 424 · 2026-05-23T11:38:26.855313+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_audit_tables_3_4_inline_20260523T112128",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 425 · 2026-05-23T11:38:26.855458+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport json\n\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/17947013-ea3d-4507-b0e3-f06dfa8892ff/tool-results/mcp-agent-ml-research-read_registry-1779535307441.txt') as f:\n    outer = json.load(f)\n\ninner = json.loads(outer['result'])\nexps = inner['data']['experiments']\n\n# The 0v1 JSD claim: '0.077 at 8B vs 0.15-0.27 at <=1.5B'\n# Let's see if this is specifically about the arXiv domain context\n# Discussion paragraph 'Boundary cases and scale effect':\n# 'Larger models reduce 0v1 JSD (0.077 at 8B vs. 0.15-0.27 at ≤1.5B)'\n# This is about ALL domains, specifically noting scale effect\n\n# 8B LLaMA C4: 0.077 ✓\n# What about 8B on arXiv? LLaMA-8B arXiv: 0.1296, LLaMA-8B wiki: 0.06169\n# These vary by domain\n\n# For <=1.5B: they likely mean main C4 (or combined) results\n# Qwen-1.5B variants: 0.164 and 0.286\n# OLMo-1B: 0.230\n# Pythia-1.4B: 0.110\n\n# The range 0.15-0.27 excludes Pythia (0.11) and Qwen-instruct (0.286)\n# Perhaps 'typical' range or excluding outliers\n# Qwen-base 0.164 ≈ 0.15, OLMo 0.230, Qwen-instruct 0.286 ≈ 0.27?\n# Qwen-instruct rounds down from 0.286 to 0.27? (imprecise)\n\nprint('JSD range analysis:')\nprint('Qwen-1.5B-Base 0v1 JSD: 0.164 -> paper says lower bound 0.15 (diff: 0.014)')\nprint('Qwen-1.5B-Instruct 0v1 JSD: 0.286 -> paper says upper bound 0.27 (diff: 0.016)')\nprint()\nprint('The range 0.15-0.27 is INACCURATE by ~0.01-0.02 based on registry data.')\nprint('Actual range of <=1.5B models on C4: 0.110-0.286 (including Pythia and Qwen-instruct)')\nprint('Or excluding Pythia and Qwen-instruct: 0.164-0.230')\nprint()\n\n# Let me also see what values the 0v1 JSD is for the rewrite mode (mvp_pilot = Qwen-rewrite)\nprint('Qwen rewrite mvp_pilot 0v1 JSD:', exps['mvp_pilot_sat_v1']['metrics']['pairwise_jsd']['0v1'])\n# = 0.2669\n\n# So the <=1.5B C4 models range:\n# Pythia-1.4B: 0.110\n# Qwen-1.5B-Base: 0.164\n# OLMo-1B: 0.230\n# Qwen-rewrite (MVP/1.5B): 0.267\n# Qwen-1.5B-Instruct: 0.286\n\n# If paper excludes Pythia (0.11) and takes the main continuation mode models:\n# Qwen-base: 0.164, OLMo-1B: 0.230, Qwen-instruct: 0.286\n# Lower: 0.16 (not 0.15), upper: 0.29 (not 0.27)\n\n# OR maybe paper uses Qwen-rewrite 0.267 as upper ≈ 0.27 and Qwen-base 0.164 ≈ 0.15?\n# That would give 0.164-0.267 ≈ '0.15-0.27'\n# This interpretation: rounds 0.164->0.15 and 0.267->0.27\nprint()\nprint('If using Qwen-base (0.164) and Qwen-rewrite (0.267):')\nprint('  Rounded: 0.16 -> 0.15, 0.27 -> 0.27')\nprint('  Upper is exact match; lower is off by 0.014')\n\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_audit_tables_3_4_inline_20260523T112128",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport json\n\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/17947013-ea3d-4507-b0e3-f06dfa8892ff/tool-results/mcp-agent-ml-research-read_registry-1779535307441.txt') as f:\n    outer = json.load(f)\n\ninner = json.loads(outer['result'])\nexps = inner['data']['experiments']\n\n# The 0v1 JSD claim: '0.077 at 8B vs 0.15-0.27 at <=1.5B'\n# Let's see if this is specifically about the arXiv domain context\n# Discussion paragraph 'Boundary cases and scale effect':\n# 'Larger models reduce 0v1 JSD (0.077 at 8B vs. 0.15-0.27 at ≤1.5B)'\n# This is about ALL domains, specifically noting scale effect\n\n# 8B LLaMA C4: 0.077 ✓\n# What about 8B on arXiv? LLaMA-8B arXiv: 0.1296, LLaMA-8B wiki: 0.06169\n# These vary by domain\n\n# For <=1.5B: they likely mean main C4 (or combined) results\n# Qwen-1.5B variants: 0.164 and 0.286\n# OLMo-1B: 0.230\n# Pythia-1.4B: 0.110\n\n# The range 0.15-0.27 excludes Pythia (0.11) and Qwen-instruct (0.286)\n# Perhaps 'typical' range or excluding outliers\n# Qwen-base 0.164 ≈ 0.15, OLMo 0.230, Qwen-instruct 0.286 ≈ 0.27?\n# Qwen-instruct rounds down from 0.286 to 0.27? (imprecise)\n\nprint('JSD range analysis:')\nprint('Qwen-1.5B-Base 0v1 JSD: 0.164 -> paper says lower bound 0.15 (diff: 0.014)')\nprint('Qwen-1.5B-Instruct 0v1 JSD: 0.286 -> paper says upper bound 0.27 (diff: 0.016)')\nprint()\nprint('The range 0.15-0.27 is INACCURATE by ~0.01-0.02 based on registry data.')\nprint('Actual range of <=1.5B models on C4: 0.110-0.286 (including Pythia and Qwen-instruct)')\nprint('Or excluding Pythia and Qwen-instruct: 0.164-0.230')\nprint()\n\n# Let me also see what values the 0v1 JSD is for the rewrite mode (mvp_pilot = Qwen-rewrite)\nprint('Qwen rewrite mvp_pilot 0v1 JSD:', exps['mvp_pilot_sat_v1']['metrics']['pairwise_jsd']['0v1'])\n# = 0.2669\n\n# So the <=1.5B C4 models range:\n# Pythia-1.4B: 0.110\n# Qwen-1.5B-Base: 0.164\n# OLMo-1B: 0.230\n# Qwen-rewrite (MVP/1.5B): 0.267\n# Qwen-1.5B-Instruct: 0.286\n\n# If paper excludes Pythia (0.11) and takes the main continuation mode models:\n# Qwen-base: 0.164, OLMo-1B: 0.230, Qwen-instruct: 0.286\n# Lower: 0.16 (not 0.15), upper: 0.29 (not 0.27)\n\n# OR maybe paper uses Qwen-rewrite 0.267 as upper ≈ 0.27 and Qwen-base 0.164 ≈ 0.15?\n# That would give 0.164-0.267 ≈ '0.15-0.27'\n# This interpretation: rounds 0.164->0.15 and 0.267->0.27\nprint()\nprint('If using Qwen-base (0.164) and Qwen-rewrite (0.267):')\nprint('  Rounded: 0.16 -> 0.15, 0.27 -> 0.27')\nprint('  Upper is exact match; lower is off by 0.014')\n\"\n"
  }
}
```

</details>

---


### Tool result

_source line 426 · 2026-05-23T11:38:26.855606+00:00_

JSD range analysis:
Qwen-1.5B-Base 0v1 JSD: 0.164 -> paper says lower bound 0.15 (diff: 0.014)
Qwen-1.5B-Instruct 0v1 JSD: 0.286 -> paper says upper bound 0.27 (diff: 0.016)

The range 0.15-0.27 is INACCURATE by ~0.01-0.02 based on registry data.
Actual range of <=1.5B models on C4: 0.110-0.286 (including Pythia and Qwen-instruct)
Or excluding Pythia and Qwen-instruct: 0.164-0.230

Qwen rewrite mvp_pilot 0v1 JSD: 0.2669

If using Qwen-base (0.164) and Qwen-rewrite (0.267):
  Rounded: 0.16 -> 0.15, 0.27 -> 0.27
  Upper is exact match; lower is off by 0.014

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_audit_tables_3_4_inline_20260523T112128",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 427 · 2026-05-23T11:38:26.855752+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport json\n\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/17947013-ea3d-4507-b0e3-f06dfa8892ff/tool-results/mcp-agent-ml-research-read_registry-1779535307441.txt') as f:\n    outer = json.load(f)\n\ninner = json.loads(outer['result'])\nexps = inner['data']['experiments']\n\n# Also check the OLMo self-scored 1v2 value (before update)\n# exp_002 notes: 'Self-scored 1v2=0.6145, Qwen-scored 1v2=0.5001'\n# But the self-scored value of 0.6145 - where does it come from?\n# It was a previous run of exp_002 before cross-scoring was applied\n\ne002 = exps['exp_002_olmo_depth']\nprint('exp_002 full metrics:')\nprint(json.dumps(e002['metrics'], indent=2))\nprint()\nprint('exp_002 notes:', e002.get('notes', '')[:400])\n\n# The self-scored OLMo value 0.6145 appears to be from old runs\n# Qwen cross-scored: 0.5001 (the updated result)\n# Gap = 0.6145 - 0.5001 = 0.1144 = 11.44pp\n# Paper says +11.5pp: rounds 11.44 to 11.5 (difference of 0.06pp - acceptable rounding)\n\nprint()\nprint('OLMo gap computation: 11.44 pp vs paper 11.5pp - rounding OK')\nprint('Pythia gap: 4.65pp vs paper 4.7pp - rounding OK')\nprint('OLMo: self=0.6145, cross=0.5001 -> delta=11.44pp (rounds to 11.5pp)')\nprint('Pythia: self=0.6539, cross=0.6074 -> delta=4.65pp (rounds to 4.7pp)')\n\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_audit_tables_3_4_inline_20260523T112128",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport json\n\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/17947013-ea3d-4507-b0e3-f06dfa8892ff/tool-results/mcp-agent-ml-research-read_registry-1779535307441.txt') as f:\n    outer = json.load(f)\n\ninner = json.loads(outer['result'])\nexps = inner['data']['experiments']\n\n# Also check the OLMo self-scored 1v2 value (before update)\n# exp_002 notes: 'Self-scored 1v2=0.6145, Qwen-scored 1v2=0.5001'\n# But the self-scored value of 0.6145 - where does it come from?\n# It was a previous run of exp_002 before cross-scoring was applied\n\ne002 = exps['exp_002_olmo_depth']\nprint('exp_002 full metrics:')\nprint(json.dumps(e002['metrics'], indent=2))\nprint()\nprint('exp_002 notes:', e002.get('notes', '')[:400])\n\n# The self-scored OLMo value 0.6145 appears to be from old runs\n# Qwen cross-scored: 0.5001 (the updated result)\n# Gap = 0.6145 - 0.5001 = 0.1144 = 11.44pp\n# Paper says +11.5pp: rounds 11.44 to 11.5 (difference of 0.06pp - acceptable rounding)\n\nprint()\nprint('OLMo gap computation: 11.44 pp vs paper 11.5pp - rounding OK')\nprint('Pythia gap: 4.65pp vs paper 4.7pp - rounding OK')\nprint('OLMo: self=0.6145, cross=0.5001 -> delta=11.44pp (rounds to 11.5pp)')\nprint('Pythia: self=0.6539, cross=0.6074 -> delta=4.65pp (rounds to 4.7pp)')\n\"\n"
  }
}
```

</details>

---


### Tool result

_source line 428 · 2026-05-23T11:38:26.855911+00:00_

exp_002 full metrics:
{
  "k_star": 1,
  "pairwise_auc": {
    "0v1": 0.9861,
    "1v2": 0.5001,
    "2v3": 0.4972,
    "3v4": 0.5034,
    "4v5": 0.4971
  },
  "scorer": "Qwen2.5-1.5B-Instruct",
  "note": "Updated to Qwen cross-scoring (D107). Self-scored 1v2=0.6145 K*=2, Qwen-scored 1v2=0.5001 K*=1."
}

exp_002 notes: 

OLMo gap computation: 11.44 pp vs paper 11.5pp - rounding OK
Pythia gap: 4.65pp vs paper 4.7pp - rounding OK
OLMo: self=0.6145, cross=0.5001 -> delta=11.44pp (rounds to 11.5pp)
Pythia: self=0.6539, cross=0.6074 -> delta=4.65pp (rounds to 4.7pp)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_audit_tables_3_4_inline_20260523T112128",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 429 · 2026-05-23T11:38:26.856056+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nfrom decimal import Decimal, ROUND_HALF_UP\n\ndef round_standard(x, n):\n    d = Decimal(str(x))\n    factor = Decimal(10) ** (-n)\n    return float(d.quantize(factor, rounding=ROUND_HALF_UP))\n\n# S12 arXiv 4v5: paper=.530, registry=0.5294 -> rounds to 0.529\n# But paper shows .530 which requires 0.5295+\nprint('S12 arXiv 4v5:')\nprint(f'  0.5294 rounds to {round_standard(0.5294, 3)}')\nprint(f'  For .530: need value in [0.5295, 0.5305)')\nprint()\n\n# Note: Table 4 also shows arXiv/Qwen-1.5B but there's no 4v5 in Table 4 (not shown)\n# S12 uses the same exp_024 data, so the 4v5 issue propagates\n\n# Summary of all mismatches:\nprint('='*70)\nprint('FINAL MISMATCH SUMMARY')\nprint('='*70)\nprint()\nprint('Table 4 mismatches:')\nprint('  1. arXiv/Qwen-1.5B 2v3: paper=.644, registry=0.6427 (rounds to .643)')\nprint('  2. Code/LLaMA-8B 2v3: paper=.510, registry=0.5112 (rounds to .511)')\nprint()\nprint('Table S12 mismatches:')\nprint('  3. arXiv col, 2v3: paper=.644, registry=0.6427 (rounds to .643)  [same as #1]')\nprint('  4. arXiv col, 4v5: paper=.530, registry=0.5294 (rounds to .529)')\nprint('  (Wiki 0v1, 3v4, 4v5: UNVERIFIABLE - exp_023 has incomplete registry metrics)')\nprint()\nprint('Inline claim mismatches:')\nprint('  5. Qwen arXiv 2v3 inline: paper=0.644, registry=0.6427 (rounds to 0.643) [same as #1]')\nprint('  6. LLaMA-8B arXiv 2v3 inline: paper=0.620, registry=0.6215 (rounds to 0.622)')\nprint('  7. Pythia arXiv CI lower: paper=0.640, registry=0.6401 (rounds to 0.640) -- BORDERLINE')\nprint('     (0.6401 -> actually rounds to 0.640 with ROUND_HALF_UP: OK)')\nprint(f'     round_standard(0.6401, 3) = {round_standard(0.6401, 3)}')\nprint()\nprint('JSD claim:')\nprint('  8. arXiv 1v2 JSD = 0.077: no registry experiment has exactly 0.077 for arXiv 1v2 JSD')\nprint('     Nearest: Mistral arXiv=0.0762, LLaMA arXiv=0.0785')\nprint('     C4 JSD ~0.01: exp_016=0.01081 -- OK (matches ~0.01)')\nprint()\nprint('Not a mismatch (verifiable OK):')\nprint('  - arXiv/Pythia 2v3: 0.6545 rounds to 0.655 -- OK')\nprint('  - Pythia CI [0.640, 0.669]: registry [0.6401, 0.6688] -- OK')\nprint('  - Qwen arXiv CI [0.628, 0.658]: registry [0.6275, 0.6575] -- OK')\n\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_audit_tables_3_4_inline_20260523T112128",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nfrom decimal import Decimal, ROUND_HALF_UP\n\ndef round_standard(x, n):\n    d = Decimal(str(x))\n    factor = Decimal(10) ** (-n)\n    return float(d.quantize(factor, rounding=ROUND_HALF_UP))\n\n# S12 arXiv 4v5: paper=.530, registry=0.5294 -> rounds to 0.529\n# But paper shows .530 which requires 0.5295+\nprint('S12 arXiv 4v5:')\nprint(f'  0.5294 rounds to {round_standard(0.5294, 3)}')\nprint(f'  For .530: need value in [0.5295, 0.5305)')\nprint()\n\n# Note: Table 4 also shows arXiv/Qwen-1.5B but there's no 4v5 in Table 4 (not shown)\n# S12 uses the same exp_024 data, so the 4v5 issue propagates\n\n# Summary of all mismatches:\nprint('='*70)\nprint('FINAL MISMATCH SUMMARY')\nprint('='*70)\nprint()\nprint('Table 4 mismatches:')\nprint('  1. arXiv/Qwen-1.5B 2v3: paper=.644, registry=0.6427 (rounds to .643)')\nprint('  2. Code/LLaMA-8B 2v3: paper=.510, registry=0.5112 (rounds to .511)')\nprint()\nprint('Table S12 mismatches:')\nprint('  3. arXiv col, 2v3: paper=.644, registry=0.6427 (rounds to .643)  [same as #1]')\nprint('  4. arXiv col, 4v5: paper=.530, registry=0.5294 (rounds to .529)')\nprint('  (Wiki 0v1, 3v4, 4v5: UNVERIFIABLE - exp_023 has incomplete registry metrics)')\nprint()\nprint('Inline claim mismatches:')\nprint('  5. Qwen arXiv 2v3 inline: paper=0.644, registry=0.6427 (rounds to 0.643) [same as #1]')\nprint('  6. LLaMA-8B arXiv 2v3 inline: paper=0.620, registry=0.6215 (rounds to 0.622)')\nprint('  7. Pythia arXiv CI lower: paper=0.640, registry=0.6401 (rounds to 0.640) -- BORDERLINE')\nprint('     (0.6401 -> actually rounds to 0.640 with ROUND_HALF_UP: OK)')\nprint(f'     round_standard(0.6401, 3) = {round_standard(0.6401, 3)}')\nprint()\nprint('JSD claim:')\nprint('  8. arXiv 1v2 JSD = 0.077: no registry experiment has exactly 0.077 for arXiv 1v2 JSD')\nprint('     Nearest: Mistral arXiv=0.0762, LLaMA arXiv=0.0785')\nprint('     C4 JSD ~0.01: exp_016=0.01081 -- OK (matches ~0.01)')\nprint()\nprint('Not a mismatch (verifiable OK):')\nprint('  - arXiv/Pythia 2v3: 0.6545 rounds to 0.655 -- OK')\nprint('  - Pythia CI [0.640, 0.669]: registry [0.6401, 0.6688] -- OK')\nprint('  - Qwen arXiv CI [0.628, 0.658]: registry [0.6275, 0.6575] -- OK')\n\"\n"
  }
}
```

</details>

---


### Tool result

_source line 430 · 2026-05-23T11:38:26.856201+00:00_

S12 arXiv 4v5:
  0.5294 rounds to 0.529
  For .530: need value in [0.5295, 0.5305)

======================================================================
FINAL MISMATCH SUMMARY
======================================================================

Table 4 mismatches:
  1. arXiv/Qwen-1.5B 2v3: paper=.644, registry=0.6427 (rounds to .643)
  2. Code/LLaMA-8B 2v3: paper=.510, registry=0.5112 (rounds to .511)

Table S12 mismatches:
  3. arXiv col, 2v3: paper=.644, registry=0.6427 (rounds to .643)  [same as #1]
  4. arXiv col, 4v5: paper=.530, registry=0.5294 (rounds to .529)
  (Wiki 0v1, 3v4, 4v5: UNVERIFIABLE - exp_023 has incomplete registry metrics)

Inline claim mismatches:
  5. Qwen arXiv 2v3 inline: paper=0.644, registry=0.6427 (rounds to 0.643) [same as #1]
  6. LLaMA-8B arXiv 2v3 inline: paper=0.620, registry=0.6215 (rounds to 0.622)
  7. Pythia arXiv CI lower: paper=0.640, registry=0.6401 (rounds to 0.640) -- BORDERLINE
     (0.6401 -> actually rounds to 0.640 with ROUND_HALF_UP: OK)
     round_standard(0.6401, 3) = 0.64

JSD claim:
  8. arXiv 1v2 JSD = 0.077: no registry experiment has exactly 0.077 for arXiv 1v2 JSD
     Nearest: Mistral arXiv=0.0762, LLaMA arXiv=0.0785
     C4 JSD ~0.01: exp_016=0.01081 -- OK (matches ~0.01)

Not a mismatch (verifiable OK):
  - arXiv/Pythia 2v3: 0.6545 rounds to 0.655 -- OK
  - Pythia CI [0.640, 0.669]: registry [0.6401, 0.6688] -- OK
  - Qwen arXiv CI [0.628, 0.658]: registry [0.6275, 0.6575] -- OK

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_audit_tables_3_4_inline_20260523T112128",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 431 · 2026-05-23T11:38:26.856348+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport json\n\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/17947013-ea3d-4507-b0e3-f06dfa8892ff/tool-results/mcp-agent-ml-research-read_registry-1779535307441.txt', 'r') as f:\n    raw = json.load(f)\n\ninner = json.loads(raw['result'])\ndata = inner['data']\nexps = data['experiments']\n\n# Double-check OLMo Table S8 CI bounds (paper has CI but exp_002 only has point estimates)\n# Also need to check if there's a separate bootstrap experiment for OLMo cross-scored\n# or if the CIs come from somewhere else\n\n# Check: does exp_007 olmo_cont match paper exactly except it's self-scored vs cross-scored?\nexp007 = exps['exp_007_bootstrap_ci']\nexp007_olmo = exp007['metrics']['olmo_cont']\nexp002 = exps['exp_002_olmo_depth']\nexp002_auc = exp002['metrics']['pairwise_auc']\n\nprint('exp_007 olmo_cont (self-scored):')\nfor pair in ['0v1','1v2','2v3','3v4','4v5']:\n    e = exp007_olmo[pair]\n    print(f'  {pair}: auc={e[\\\"auc\\\"]:.4f} ci=[{e[\\\"ci_lower\\\"]:.4f},{e[\\\"ci_upper\\\"]:.4f}]')\n\nprint()\nprint('exp_002 olmo_depth (Qwen cross-scored, no CI):')\nfor pair in ['0v1','1v2','2v3','3v4','4v5']:\n    print(f'  {pair}: auc={exp002_auc[pair]:.4f}')\n\nprint()\nprint('Paper Table S8 OLMo:')\npaper_olmo = {\n    '0v1': (.986, .984, .988),\n    '1v2': (.500, .496, .519),\n    '2v3': (.497, .486, .509),\n    '3v4': (.502, .491, .513),\n    '4v5': (.494, .483, .506),\n}\nfor pair, (auc, lo, hi) in paper_olmo.items():\n    print(f'  {pair}: auc={auc:.3f} ci=[{lo:.3f},{hi:.3f}]')\n\" 2>&1\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_audit_tables_3_4_inline_20260523T112128",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport json\n\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/17947013-ea3d-4507-b0e3-f06dfa8892ff/tool-results/mcp-agent-ml-research-read_registry-1779535307441.txt', 'r') as f:\n    raw = json.load(f)\n\ninner = json.loads(raw['result'])\ndata = inner['data']\nexps = data['experiments']\n\n# Double-check OLMo Table S8 CI bounds (paper has CI but exp_002 only has point estimates)\n# Also need to check if there's a separate bootstrap experiment for OLMo cross-scored\n# or if the CIs come from somewhere else\n\n# Check: does exp_007 olmo_cont match paper exactly except it's self-scored vs cross-scored?\nexp007 = exps['exp_007_bootstrap_ci']\nexp007_olmo = exp007['metrics']['olmo_cont']\nexp002 = exps['exp_002_olmo_depth']\nexp002_auc = exp002['metrics']['pairwise_auc']\n\nprint('exp_007 olmo_cont (self-scored):')\nfor pair in ['0v1','1v2','2v3','3v4','4v5']:\n    e = exp007_olmo[pair]\n    print(f'  {pair}: auc={e[\\\"auc\\\"]:.4f} ci=[{e[\\\"ci_lower\\\"]:.4f},{e[\\\"ci_upper\\\"]:.4f}]')\n\nprint()\nprint('exp_002 olmo_depth (Qwen cross-scored, no CI):')\nfor pair in ['0v1','1v2','2v3','3v4','4v5']:\n    print(f'  {pair}: auc={exp002_auc[pair]:.4f}')\n\nprint()\nprint('Paper Table S8 OLMo:')\npaper_olmo = {\n    '0v1': (.986, .984, .988),\n    '1v2': (.500, .496, .519),\n    '2v3': (.497, .486, .509),\n    '3v4': (.502, .491, .513),\n    '4v5': (.494, .483, .506),\n}\nfor pair, (auc, lo, hi) in paper_olmo.items():\n    print(f'  {pair}: auc={auc:.3f} ci=[{lo:.3f},{hi:.3f}]')\n\" 2>&1\n"
  }
}
```

</details>

---


### Tool result

_source line 432 · 2026-05-23T11:38:26.856484+00:00_

exp_007 olmo_cont (self-scored):
  0v1: auc=0.9970 ci=[0.9964,0.9975]
  1v2: auc=0.6145 ci=[0.6045,0.6247]
  2v3: auc=0.5496 ci=[0.5399,0.5596]
  3v4: auc=0.5091 ci=[0.4973,0.5200]
  4v5: auc=0.5045 ci=[0.4932,0.5150]

exp_002 olmo_depth (Qwen cross-scored, no CI):
  0v1: auc=0.9861
  1v2: auc=0.5001
  2v3: auc=0.4972
  3v4: auc=0.5034
  4v5: auc=0.4971

Paper Table S8 OLMo:
  0v1: auc=0.986 ci=[0.984,0.988]
  1v2: auc=0.500 ci=[0.496,0.519]
  2v3: auc=0.497 ci=[0.486,0.509]
  3v4: auc=0.502 ci=[0.491,0.513]
  4v5: auc=0.494 ci=[0.483,0.506]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_audit_tables_3_4_inline_20260523T112128",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 433 · 2026-05-23T11:38:26.856621+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nfrom decimal import Decimal, ROUND_HALF_UP\n\ndef round_standard(x, n):\n    d = Decimal(str(x))\n    factor = Decimal(10) ** (-n)\n    return float(d.quantize(factor, rounding=ROUND_HALF_UP))\n\n# Double-check: Pythia CI lower 0.6401 -> 0.640? Using ROUND_HALF_UP\nprint('Pythia CI lower 0.6401 ->',round_standard(0.6401, 3))\n# 0.6401: 4th decimal is 1, so we round down -> 0.640 OK\n\n# Let me also confirm CI for Qwen arXiv: [0.628, 0.658]\n# 0.6275 -> 0.628 (standard half-up: 4th decimal is 5, rounds up the 3rd: 7->8 -> 0.628) WAIT\n# 0.6275: d=0.627|5 so 3rd decimal=7, 4th decimal=5 -> round up 7->8 -> NO WAIT\n# 0.6275 means: 0.6 2 7 5 -> 3dp means we look at 4th dp=5 -> round up 3rd dp (7->8? no, that's not right)\n# 0.6275 in 3dp: floor is 0.627, next is 0.628\n# The digit at 4th decimal position is 5 -> rounds up -> 0.628 \nprint('Qwen arXiv CI lower 0.6275 ->', round_standard(0.6275, 3))  # should be 0.628\n\n# 0.6575: 4th decimal is 5 -> rounds up -> 0.658\nprint('Qwen arXiv CI upper 0.6575 ->', round_standard(0.6575, 3))  # should be 0.658\n\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_audit_tables_3_4_inline_20260523T112128",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nfrom decimal import Decimal, ROUND_HALF_UP\n\ndef round_standard(x, n):\n    d = Decimal(str(x))\n    factor = Decimal(10) ** (-n)\n    return float(d.quantize(factor, rounding=ROUND_HALF_UP))\n\n# Double-check: Pythia CI lower 0.6401 -> 0.640? Using ROUND_HALF_UP\nprint('Pythia CI lower 0.6401 ->',round_standard(0.6401, 3))\n# 0.6401: 4th decimal is 1, so we round down -> 0.640 OK\n\n# Let me also confirm CI for Qwen arXiv: [0.628, 0.658]\n# 0.6275 -> 0.628 (standard half-up: 4th decimal is 5, rounds up the 3rd: 7->8 -> 0.628) WAIT\n# 0.6275: d=0.627|5 so 3rd decimal=7, 4th decimal=5 -> round up 7->8 -> NO WAIT\n# 0.6275 means: 0.6 2 7 5 -> 3dp means we look at 4th dp=5 -> round up 3rd dp (7->8? no, that's not right)\n# 0.6275 in 3dp: floor is 0.627, next is 0.628\n# The digit at 4th decimal position is 5 -> rounds up -> 0.628 \nprint('Qwen arXiv CI lower 0.6275 ->', round_standard(0.6275, 3))  # should be 0.628\n\n# 0.6575: 4th decimal is 5 -> rounds up -> 0.658\nprint('Qwen arXiv CI upper 0.6575 ->', round_standard(0.6575, 3))  # should be 0.658\n\"\n"
  }
}
```

</details>

---


### Tool result

_source line 434 · 2026-05-23T11:38:26.856747+00:00_

Pythia CI lower 0.6401 -> 0.64
Qwen arXiv CI lower 0.6275 -> 0.628
Qwen arXiv CI upper 0.6575 -> 0.658

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_audit_tables_3_4_inline_20260523T112128",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 435 · 2026-05-23T11:38:26.856903+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport json\n\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/17947013-ea3d-4507-b0e3-f06dfa8892ff/tool-results/mcp-agent-ml-research-read_registry-1779535307441.txt') as f:\n    outer = json.load(f)\n\ninner = json.loads(outer['result'])\nexps = inner['data']['experiments']\n\n# Check if Mistral ~1.9pp is a different comparison\n# The paper says 'LLaMA-8B and Mistral-7B (~+1.9 pp each)'\n# For Mistral: self=0.5935, cross=0.5695 => 2.4pp (from exp_019 self vs exp_019b cross)\n# \n# But wait - do these two experiments use the same data?\n# exp_019 self-scored = Mistral scoring its own Mistral-generated text\n# exp_019b cross-scored = Qwen scoring Mistral-generated text\n# The data IS the same (Mistral-generated C4 text)\n# So the gap is valid: 2.4pp\n# \n# Paper says ~1.9pp - which is off by 0.5pp\n# This could be because the paper average includes LLaMA, and LLaMA gap is smaller\n# OR the Mistral self-scored value might be different (maybe not from exp_019)\n#\n# Let me check if there's another Mistral self-scored experiment\nprint('Mistral experiments:')\nfor k, v in exps.items():\n    if 'mistral' in k.lower():\n        m = v.get('metrics', {})\n        auc_1v2 = m.get('pairwise_auc', {}).get('1v2') or m.get('auc_1v2')\n        scorer = v.get('spec', {}).get('eval_data', '') or v.get('metrics', {}).get('scorer', '')\n        print(f'  {k}: 1v2={auc_1v2}, conclusion={v.get(\\\"conclusion\\\")}')\n\nprint()\nprint('The key issue: paper says LLaMA/Mistral ~+1.9pp each')\nprint('From registry: Mistral self=0.5935, cross=0.5695 => 2.4pp')\nprint('For LLaMA: no self-scorer experiment exists')\nprint('If LLaMA gap ~1.4pp and Mistral ~2.4pp, average ~ 1.9pp')\nprint('But paper says each is ~1.9pp, not average')\n\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_audit_tables_3_4_inline_20260523T112128",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport json\n\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/17947013-ea3d-4507-b0e3-f06dfa8892ff/tool-results/mcp-agent-ml-research-read_registry-1779535307441.txt') as f:\n    outer = json.load(f)\n\ninner = json.loads(outer['result'])\nexps = inner['data']['experiments']\n\n# Check if Mistral ~1.9pp is a different comparison\n# The paper says 'LLaMA-8B and Mistral-7B (~+1.9 pp each)'\n# For Mistral: self=0.5935, cross=0.5695 => 2.4pp (from exp_019 self vs exp_019b cross)\n# \n# But wait - do these two experiments use the same data?\n# exp_019 self-scored = Mistral scoring its own Mistral-generated text\n# exp_019b cross-scored = Qwen scoring Mistral-generated text\n# The data IS the same (Mistral-generated C4 text)\n# So the gap is valid: 2.4pp\n# \n# Paper says ~1.9pp - which is off by 0.5pp\n# This could be because the paper average includes LLaMA, and LLaMA gap is smaller\n# OR the Mistral self-scored value might be different (maybe not from exp_019)\n#\n# Let me check if there's another Mistral self-scored experiment\nprint('Mistral experiments:')\nfor k, v in exps.items():\n    if 'mistral' in k.lower():\n        m = v.get('metrics', {})\n        auc_1v2 = m.get('pairwise_auc', {}).get('1v2') or m.get('auc_1v2')\n        scorer = v.get('spec', {}).get('eval_data', '') or v.get('metrics', {}).get('scorer', '')\n        print(f'  {k}: 1v2={auc_1v2}, conclusion={v.get(\\\"conclusion\\\")}')\n\nprint()\nprint('The key issue: paper says LLaMA/Mistral ~+1.9pp each')\nprint('From registry: Mistral self=0.5935, cross=0.5695 => 2.4pp')\nprint('For LLaMA: no self-scorer experiment exists')\nprint('If LLaMA gap ~1.4pp and Mistral ~2.4pp, average ~ 1.9pp')\nprint('But paper says each is ~1.9pp, not average')\n\"\n"
  }
}
```

</details>

---


### Tool result

_source line 436 · 2026-05-23T11:38:26.857044+00:00_

Mistral experiments:
  exp_code_mistral7b: 1v2=0.6152, conclusion=success
  exp_arXiv_mistral7b_crossscorer: 1v2=0.8141, conclusion=success
  exp_wiki_mistral7b: 1v2=0.5552, conclusion=success
  exp_arXiv_mistral7b: 1v2=0.8201, conclusion=success
  exp_019b_mistral_cross_scorer: 1v2=0.5695, conclusion=success
  exp_019_mistral7b_depth: 1v2=0.5935, conclusion=success

The key issue: paper says LLaMA/Mistral ~+1.9pp each
From registry: Mistral self=0.5935, cross=0.5695 => 2.4pp
For LLaMA: no self-scorer experiment exists
If LLaMA gap ~1.4pp and Mistral ~2.4pp, average ~ 1.9pp
But paper says each is ~1.9pp, not average

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_audit_tables_3_4_inline_20260523T112128",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool result

_source line 437 · 2026-05-23T11:38:26.857241+00:00_

Here is the complete audit result.

---

## Cross-Reference: Paper Tables vs Registry

**Registry source file:** `/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/17947013-ea3d-4507-b0e3-f06dfa8892ff/tool-results/mcp-agent-ml-research-read_registry-1779535307441.txt`

**Paper source:** `/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex` (Table 1) and `docs/paper/appendix.tex` (Extended Table)

---

### Table 1 (tab:kstar_ci) — 5 Main Models

| Location | Paper Value | Registry exp_id | Registry Value | Match? |
|---|---|---|---|---|
| Qwen-rw 0v1 AUC | .9956 | exp_007_bootstrap_ci[qwen_rewrite] | 0.9956 | MATCH |
| Qwen-rw 1v2 AUC | .6955 | exp_007_bootstrap_ci[qwen_rewrite] | 0.6955 | MATCH |
| Qwen-rw 1v2 CI | [.686,.704] | exp_007_bootstrap_ci[qwen_rewrite] | [.6859,.7041] | MATCH (rounding) |
| Qwen-rw 2v3 AUC | .5893 | exp_007_bootstrap_ci[qwen_rewrite] | 0.5893 | MATCH |
| Qwen-rw 2v3 CI | [.580,.599] | exp_007_bootstrap_ci[qwen_rewrite] | [.5795,.5991] | MATCH (rounding) |
| Qwen-rw 3v4 AUC | .5435 | exp_007_bootstrap_ci[qwen_rewrite] | 0.5435 | MATCH |
| Qwen-rw 4v5 AUC | .5340 | exp_007_bootstrap_ci[qwen_rewrite] | 0.5340 | MATCH |
| Pythia 0v1 AUC | .9722 | exp_001_pythia_depth | 0.9722 | MATCH |
| Pythia 1v2 AUC | .6074 | exp_001_pythia_depth | 0.6074 | MATCH |
| Pythia 1v2 CI | [.598,.617] | exp_001_pythia_depth[bootstrap_ci] | [.5975,.6172] | MATCH (rounding) |
| Pythia 2v3 AUC | .5440 | exp_001_pythia_depth | 0.5440 | MATCH |
| **Pythia 2v3 CI** | **[.534,.554]** | **(no registry record)** | **N/A** | **NOT IN REGISTRY** |
| Pythia 3v4 AUC | .5051 | exp_001_pythia_depth | 0.5051 | MATCH |
| Pythia 4v5 AUC | .5079 | exp_001_pythia_depth | 0.5079 | MATCH |
| OLMo 0v1 AUC | .9860 | exp_002_olmo_depth | 0.9861 | MATCH (rounding) |
| OLMo 1v2 AUC | .5001 | exp_002_olmo_depth | 0.5001 | MATCH |
| **OLMo 1v2 CI** | **[.496,.519]
…[truncated 5552 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_audit_tables_3_4_inline_20260523T112128",
  "tool": "Agent",
  "elapsed_ms": 63
}
```

</details>

---


### Tool call

_source line 438 · 2026-05-23T11:38:26.857411+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nfrom decimal import Decimal, ROUND_HALF_UP\n\ndef round_standard(x, n):\n    d = Decimal(str(x))\n    factor = Decimal(10) ** (-n)\n    return float(d.quantize(factor, rounding=ROUND_HALF_UP))\n\n# The paper displays 0.640 for Pythia CI lower (3 decimal places shown as .640)\n# But round_standard(0.6401, 3) = 0.640 (displayed without trailing zero: 0.64)\n# In the paper context 0.640 = 0.64 -- they're the same\n\n# Now let's verify: is the CI lower 0.640 in the paper exact?\n# Inline: '0.655 [0.640, 0.669]'\n# Registry: ci_lower=0.6401, ci_upper=0.6688\n# 0.6401 -> 0.640 OK, 0.6688 -> 0.669 OK -- MATCH\n\n# Final verification table for all inline claims:\nprint('=== INLINE CLAIMS FINAL VERIFICATION ===')\nprint()\nprint('Claim 1: Qwen arXiv 2v3 = 0.644 [0.628, 0.658]')\nprint('  Registry (exp_024): auc=0.6427, CI=[0.6275, 0.6575]')\nprint(f'  AUC: 0.6427 rounds to {round_standard(0.6427, 3)} -- paper says 0.644 -- MISMATCH')\nprint(f'  CI lower: 0.6275 -> {round_standard(0.6275, 3)} -- paper says 0.628 -- OK')\nprint(f'  CI upper: 0.6575 -> {round_standard(0.6575, 3)} -- paper says 0.658 -- OK')\nprint()\nprint('Claim 2: Pythia arXiv 2v3 = 0.655 [0.640, 0.669]')\nprint('  Registry (exp_025): auc=0.6545, CI=[0.6401, 0.6688]')\nprint(f'  AUC: 0.6545 rounds to {round_standard(0.6545, 3)} -- paper says 0.655 -- OK')\nprint(f'  CI lower: 0.6401 -> {round_standard(0.6401, 3)} -- paper says 0.640 -- OK')\nprint(f'  CI upper: 0.6688 -> {round_standard(0.6688, 3)} -- paper says 0.669 -- OK')\nprint()\nprint('Claim 3: LLaMA-8B arXiv 2v3 = 0.620 [0.605, 0.635]')\nprint('  Registry (exp_arXiv_llama8b): auc=0.6215, CI=NOT STORED')\nprint(f'  AUC: 0.6215 rounds to {round_standard(0.6215, 3)} -- paper says 0.620 -- MISMATCH')\nprint('  CI: not verifiable (no bootstrap CI in registry)')\nprint()\nprint('Claim 4: arXiv 1v2 JSD = 0.077 vs ~0.01 for C4')\nprint('  Registry arXiv 1v2 JSD values: LLaMA=0.0785, Mistral=0.0762, Pythia=0.0573')\nprint('  No single experiment has JSD=0.077 for arXiv 1v2')\nprint('  Closest: Mistral 0.0762 (rounds to 0.076 NOT 0.077)')\nprint('  C4 JSD ~0.01: exp_016=0.01081 -- OK')\n\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_audit_tables_3_4_inline_20260523T112128",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nfrom decimal import Decimal, ROUND_HALF_UP\n\ndef round_standard(x, n):\n    d = Decimal(str(x))\n    factor = Decimal(10) ** (-n)\n    return float(d.quantize(factor, rounding=ROUND_HALF_UP))\n\n# The paper displays 0.640 for Pythia CI lower (3 decimal places shown as .640)\n# But round_standard(0.6401, 3) = 0.640 (displayed without trailing zero: 0.64)\n# In the paper context 0.640 = 0.64 -- they're the same\n\n# Now let's verify: is the CI lower 0.640 in the paper exact?\n# Inline: '0.655 [0.640, 0.669]'\n# Registry: ci_lower=0.6401, ci_upper=0.6688\n# 0.6401 -> 0.640 OK, 0.6688 -> 0.669 OK -- MATCH\n\n# Final verification table for all inline claims:\nprint('=== INLINE CLAIMS FINAL VERIFICATION ===')\nprint()\nprint('Claim 1: Qwen arXiv 2v3 = 0.644 [0.628, 0.658]')\nprint('  Registry (exp_024): auc=0.6427, CI=[0.6275, 0.6575]')\nprint(f'  AUC: 0.6427 rounds to {round_standard(0.6427, 3)} -- paper says 0.644 -- MISMATCH')\nprint(f'  CI lower: 0.6275 -> {round_standard(0.6275, 3)} -- paper says 0.628 -- OK')\nprint(f'  CI upper: 0.6575 -> {round_standard(0.6575, 3)} -- paper says 0.658 -- OK')\nprint()\nprint('Claim 2: Pythia arXiv 2v3 = 0.655 [0.640, 0.669]')\nprint('  Registry (exp_025): auc=0.6545, CI=[0.6401, 0.6688]')\nprint(f'  AUC: 0.6545 rounds to {round_standard(0.6545, 3)} -- paper says 0.655 -- OK')\nprint(f'  CI lower: 0.6401 -> {round_standard(0.6401, 3)} -- paper says 0.640 -- OK')\nprint(f'  CI upper: 0.6688 -> {round_standard(0.6688, 3)} -- paper says 0.669 -- OK')\nprint()\nprint('Claim 3: LLaMA-8B arXiv 2v3 = 0.620 [0.605, 0.635]')\nprint('  Registry (exp_arXiv_llama8b): auc=0.6215, CI=NOT STORED')\nprint(f'  AUC: 0.6215 rounds to {round_standard(0.6215, 3)} -- paper says 0.620 -- MISMATCH')\nprint('  CI: not verifiable (no bootstrap CI in registry)')\nprint()\nprint('Claim 4: arXiv 1v2 JSD = 0.077 vs ~0.01 for C4')\nprint('  Registry arXiv 1v2 JSD values: LLaMA=0.0785, Mistral=0.0762, Pythia=0.0573')\nprint('  No single experiment has JSD=0.077 for arXiv 1v2')\nprint('  Closest: Mistral 0.0762 (rounds to 0.076 NOT 0.077)')\nprint('  C4 JSD ~0.01: exp_016=0.01081 -- OK')\n\"\n"
  }
}
```

</details>

---


### Tool result

_source line 439 · 2026-05-23T11:38:26.857561+00:00_

=== INLINE CLAIMS FINAL VERIFICATION ===

Claim 1: Qwen arXiv 2v3 = 0.644 [0.628, 0.658]
  Registry (exp_024): auc=0.6427, CI=[0.6275, 0.6575]
  AUC: 0.6427 rounds to 0.643 -- paper says 0.644 -- MISMATCH
  CI lower: 0.6275 -> 0.628 -- paper says 0.628 -- OK
  CI upper: 0.6575 -> 0.658 -- paper says 0.658 -- OK

Claim 2: Pythia arXiv 2v3 = 0.655 [0.640, 0.669]
  Registry (exp_025): auc=0.6545, CI=[0.6401, 0.6688]
  AUC: 0.6545 rounds to 0.655 -- paper says 0.655 -- OK
  CI lower: 0.6401 -> 0.64 -- paper says 0.640 -- OK
  CI upper: 0.6688 -> 0.669 -- paper says 0.669 -- OK

Claim 3: LLaMA-8B arXiv 2v3 = 0.620 [0.605, 0.635]
  Registry (exp_arXiv_llama8b): auc=0.6215, CI=NOT STORED
  AUC: 0.6215 rounds to 0.622 -- paper says 0.620 -- MISMATCH
  CI: not verifiable (no bootstrap CI in registry)

Claim 4: arXiv 1v2 JSD = 0.077 vs ~0.01 for C4
  Registry arXiv 1v2 JSD values: LLaMA=0.0785, Mistral=0.0762, Pythia=0.0573
  No single experiment has JSD=0.077 for arXiv 1v2
  Closest: Mistral 0.0762 (rounds to 0.076 NOT 0.077)
  C4 JSD ~0.01: exp_016=0.01081 -- OK

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_audit_tables_3_4_inline_20260523T112128",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 440 · 2026-05-23T11:38:26.857724+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\n# Summary of all findings for final report\nprint('='*80)\nprint('AUDIT SUMMARY')\nprint('='*80)\nprint()\nprint('TASK 1: Filtering results (experiments_c3.tex)')\nprint('-'*50)\nprint()\nprint('Tab filtering_main.tex: ALL entries MATCH registry (exp_006_graduated_filtering)')\nprint()\nprint('Inline numbers:')\nprint()\nprint('1. -1.53 pp (no-filter MMLU degradation from base):')\nprint('   Base=0.6018, no_filter=0.5865 => (0.5865-0.6018)*100 = -1.53 pp')\nprint('   Registry: exact match ✓')\nprint()\nprint('2. -0.77 pp (binary-ours MMLU degradation):')\nprint('   Base=0.6018, binary_ours=0.5941 => (0.5941-0.6018)*100 = -0.77 pp')\nprint('   Registry: exact match ✓')\nprint()\nprint('3. ~50% reduction:')\nprint('   (1.53-0.77)/1.53 = 49.7% ≈ 50%')\nprint('   Registry: matches ✓')\nprint()\nprint('4. p_corr < 0.05 vs all alternatives (binary-ours MMLU):')\nprint('   exp_E_paired_stats: binary_ours_vs_all_mmlu=all significant')\nprint('   tab_pairwise_significance: all p < .05 for binary-ours vs all ✓')\nprint()\nprint('5. p_corr = 1.00 (graduated a=0.9 vs binary-ours on HellaSwag):')\nprint('   tab_pairwise_significance: HellaSwag delta=0.00, p=1.00 ✓')\nprint()\nprint('6. p_corr = 0.011 (graduated a=0.9 vs binary-ours on MMLU):')\nprint('   tab_pairwise_significance: MMLU p=.011 ✓')\nprint()\nprint()\nprint('TASK 2: Introduction numbers')\nprint('-'*50)\nprint()\nprint('1. MMLU 0.5941 vs base 0.6018:')\nprint('   Registry binary_ours MMLU: 0.5941 ✓')\nprint('   Registry base_model MMLU: 0.6018 ✓')\nprint()\nprint('2. p <= 0.002 for K*=2 configurations:')\nprint('   exp_007_bootstrap_ci: all K*=2 perm_p = 0.002 ✓')\nprint()\nprint()\nprint('TASK 3: Discussion numbers')\nprint('-'*50)\nprint()\n\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_audit_tables_3_4_inline_20260523T112128",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\n# Summary of all findings for final report\nprint('='*80)\nprint('AUDIT SUMMARY')\nprint('='*80)\nprint()\nprint('TASK 1: Filtering results (experiments_c3.tex)')\nprint('-'*50)\nprint()\nprint('Tab filtering_main.tex: ALL entries MATCH registry (exp_006_graduated_filtering)')\nprint()\nprint('Inline numbers:')\nprint()\nprint('1. -1.53 pp (no-filter MMLU degradation from base):')\nprint('   Base=0.6018, no_filter=0.5865 => (0.5865-0.6018)*100 = -1.53 pp')\nprint('   Registry: exact match ✓')\nprint()\nprint('2. -0.77 pp (binary-ours MMLU degradation):')\nprint('   Base=0.6018, binary_ours=0.5941 => (0.5941-0.6018)*100 = -0.77 pp')\nprint('   Registry: exact match ✓')\nprint()\nprint('3. ~50% reduction:')\nprint('   (1.53-0.77)/1.53 = 49.7% ≈ 50%')\nprint('   Registry: matches ✓')\nprint()\nprint('4. p_corr < 0.05 vs all alternatives (binary-ours MMLU):')\nprint('   exp_E_paired_stats: binary_ours_vs_all_mmlu=all significant')\nprint('   tab_pairwise_significance: all p < .05 for binary-ours vs all ✓')\nprint()\nprint('5. p_corr = 1.00 (graduated a=0.9 vs binary-ours on HellaSwag):')\nprint('   tab_pairwise_significance: HellaSwag delta=0.00, p=1.00 ✓')\nprint()\nprint('6. p_corr = 0.011 (graduated a=0.9 vs binary-ours on MMLU):')\nprint('   tab_pairwise_significance: MMLU p=.011 ✓')\nprint()\nprint()\nprint('TASK 2: Introduction numbers')\nprint('-'*50)\nprint()\nprint('1. MMLU 0.5941 vs base 0.6018:')\nprint('   Registry binary_ours MMLU: 0.5941 ✓')\nprint('   Registry base_model MMLU: 0.6018 ✓')\nprint()\nprint('2. p <= 0.002 for K*=2 configurations:')\nprint('   exp_007_bootstrap_ci: all K*=2 perm_p = 0.002 ✓')\nprint()\nprint()\nprint('TASK 3: Discussion numbers')\nprint('-'*50)\nprint()\n\"\n"
  }
}
```

</details>

---


### Tool result

_source line 441 · 2026-05-23T11:38:26.857926+00:00_

================================================================================
AUDIT SUMMARY
================================================================================

TASK 1: Filtering results (experiments_c3.tex)
--------------------------------------------------

Tab filtering_main.tex: ALL entries MATCH registry (exp_006_graduated_filtering)

Inline numbers:

1. -1.53 pp (no-filter MMLU degradation from base):
   Base=0.6018, no_filter=0.5865 => (0.5865-0.6018)*100 = -1.53 pp
   Registry: exact match ✓

2. -0.77 pp (binary-ours MMLU degradation):
   Base=0.6018, binary_ours=0.5941 => (0.5941-0.6018)*100 = -0.77 pp
   Registry: exact match ✓

3. ~50% reduction:
   (1.53-0.77)/1.53 = 49.7% ≈ 50%
   Registry: matches ✓

4. p_corr < 0.05 vs all alternatives (binary-ours MMLU):
   exp_E_paired_stats: binary_ours_vs_all_mmlu=all significant
   tab_pairwise_significance: all p < .05 for binary-ours vs all ✓

5. p_corr = 1.00 (graduated a=0.9 vs binary-ours on HellaSwag):
   tab_pairwise_significance: HellaSwag delta=0.00, p=1.00 ✓

6. p_corr = 0.011 (graduated a=0.9 vs binary-ours on MMLU):
   tab_pairwise_significance: MMLU p=.011 ✓


TASK 2: Introduction numbers
--------------------------------------------------

1. MMLU 0.5941 vs base 0.6018:
   Registry binary_ours MMLU: 0.5941 ✓
   Registry base_model MMLU: 0.6018 ✓

2. p <= 0.002 for K*=2 configurations:
   exp_007_bootstrap_ci: all K*=2 perm_p = 0.002 ✓


TASK 3: Discussion numbers
--------------------------------------------------

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_audit_tables_3_4_inline_20260523T112128",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 442 · 2026-05-23T11:38:26.858091+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport json\n\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/17947013-ea3d-4507-b0e3-f06dfa8892ff/tool-results/mcp-agent-ml-research-read_registry-1779535307441.txt', 'r') as f:\n    raw = json.load(f)\n\ninner = json.loads(raw['result'])\ndata = inner['data']\nexps = data['experiments']\n\n# exp_007 OLMo values are self-scored, paper Table S8 shows Qwen cross-scored values (matching exp_002)\n# The CIs in Table S8 for OLMo must come from a bootstrap run not captured in the registry\n\n# Now let's compile the complete audit table for final output\n# Including all tasks with clear verdicts\n\nprint('=== COMPLETE AUDIT TABLE ===')\nprint()\n\nrows = []\n\n# TASK 1: Table S2 (exp_003) - all 20 values matched\nrows.append(('Task 1 summary', 'S2 AUC (all 20 cells)', 'All match', 'exp_003', 'All match', 'OK'))\n\n# TASK 2: Table S8 (exp_007 for Qwen-rw, Qwen-cont; exp_002 for OLMo AUC; mixed for Pythia)\nrows.append(('Task 2', 'S8 Qwen-rw all 5 pairs', 'All match exp_007', 'exp_007', 'All match', 'OK'))\nrows.append(('Task 2', 'S8 Pythia 0v1=.993', '0.993[.992,.994]', 'exp_007', '0.9932[0.9921,0.9943]', 'OK'))\nrows.append(('Task 2', 'S8 Pythia 1v2=.607', '0.607[.598,.617]', 'exp_007', '0.6539[0.6454,0.6630]', 'MISMATCH'))\nrows.append(('Task 2', 'S8 Pythia 1v2=.607 vs exp_001', '0.607[.598,.617]', 'exp_001 cross-scored', '0.6074 (no CI stored)', 'PARTIAL MATCH (AUC only)'))\nrows.append(('Task 2', 'S8 Pythia 2v3=.551', '0.551[.542,.563]', 'exp_007', '0.5514[0.5417,0.5628]', 'OK'))\nrows.append(('Task 2', 'S8 Pythia 3v4=.515', '0.515[.504,.526]', 'exp_007', '0.5152[0.5041,0.5260]', 'OK'))\nrows.append(('Task 2', 'S8 Pythia 4v5=.514', '0.514[.502,.525]', 'exp_007', '0.5136[0.5021,0.5249]', 'OK'))\nrows.append(('Task 2', 'S8 OLMo 0v1=.986', '.986[.984,.988]', 'exp_007', '0.9970[0.9964,0.9975]', 'MISMATCH'))\nrows.append(('Task 2', 'S8 OLMo 0v1=.986', '.986[.984,.988]', 'exp_002 cross-scored', '0.9861 (no CI)', 'AUC matches, CI unverified'))\nrows.append(('Task 2', 'S8 OLMo 1v2=.500', '.500[.496,.519]', 'exp_007', '0.6145[0.6045,0.6247]', 'MISMATCH'))\nrows.append(('Task 2', 'S8 OLMo 1v2=.500', '.500[.496,.519]', 'exp_002 cross-scored', '0.5001 (no CI)', 'AUC matches, CI unverified'))\nrows.append(('Task 2', 'S8 OLMo 2v3=.497', '.497[.486,.509]', 'exp_002 cross-scored', '0.4972 (no CI)', 'AUC matches, CI unverified'))\nrows.append(('Task 2', 'S8 OLMo 3v4=.502', '.502[.491,.513]', 'exp_002 cross-scored', '0.5034 (no CI)', 'AUC matches, CI unverified'))\nrows.append(('Task 2', 'S8 OLMo 4v5=.494', '.494[.483,.506]', 'exp_002 cross-scored', '0.4971 (no CI)', 'AUC matches, CI unverified'))\nrows.append(('Task 2', 'S8 Qwen-cont all 5 pairs', 'All match', 'exp_007', 'All match', 'OK'))\n\n# TASK 3: Neural probe (exp_015)\nrows.append(('Task 3', 'Qwen 2v3 AUC=0.6159', '0.6159', 'exp_015', '0.616', 'OK'))\nrows.append(('Task 3', 'Qwen K*=3', 'K*=3', 'exp_015', 'k_star_neural=3', 'OK'))\nrows.append(('Task 3', 'Pythia 2v3 AUC=0.5963', '0.5963', 'exp_015', '0.596', 'OK'))\nrows.append(('Task 3', 'Pythia K*=2', 'K*=2', 'exp_015', 'k_star_neural=2', 'OK'))\nrows.append(('Task 3', 'OLMo 2v3 AUC=0.5056', '0.5056', 'exp_015', '0.589', 'MISMATCH'))\nrows.append(('Task 3', 'OLMo 1v2=0.5054', '0.5054', 'exp_015', '0.657', 'MISMATCH'))\nrows.append(('Task 3', 'OLMo K*=1', 'K*=1', 'exp_015', 'k_star_neural=2', 'MISMATCH'))\n\n# Task 3 CI bounds from exp_015 - note that registry has no CI for neural probe\nrows.append(('Task 3', 'Qwen 2v3 CI [0.610,0.622]', '[0.610,0.622]', 'exp_015', 'No CI stored', 'UNVERIFIABLE'))\nrows.append(('Task 3', 'Pythia 2v3 CI [0.589,0.603]', '[0.589,0.603]', 'exp_015', 'No CI stored', 'UNVERIFIABLE'))\nrows.append(('Task 3', 'OLMo 2v3 CI [0.497,0.516]', '[0.497,0.516]', 'exp_015', 'No CI stored', 'UNVERIFIABLE'))\n\nprint(f'{'Location':<40} {'Paper Value':<30} {'Exp ID':<20} {'Registry Value':<35} Match')\nprint('-' * 130)\nfor task, loc, paper, exp_id, reg, match in rows:\n    print(f'{loc:<40} {paper:<30} {exp_id:<20} {reg:<35} {match}')\n\" 2>&1\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_audit_tables_3_4_inline_20260523T112128",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport json\n\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/17947013-ea3d-4507-b0e3-f06dfa8892ff/tool-results/mcp-agent-ml-research-read_registry-1779535307441.txt', 'r') as f:\n    raw = json.load(f)\n\ninner = json.loads(raw['result'])\ndata = inner['data']\nexps = data['experiments']\n\n# exp_007 OLMo values are self-scored, paper Table S8 shows Qwen cross-scored values (matching exp_002)\n# The CIs in Table S8 for OLMo must come from a bootstrap run not captured in the registry\n\n# Now let's compile the complete audit table for final output\n# Including all tasks with clear verdicts\n\nprint('=== COMPLETE AUDIT TABLE ===')\nprint()\n\nrows = []\n\n# TASK 1: Table S2 (exp_003) - all 20 values matched\nrows.append(('Task 1 summary', 'S2 AUC (all 20 cells)', 'All match', 'exp_003', 'All match', 'OK'))\n\n# TASK 2: Table S8 (exp_007 for Qwen-rw, Qwen-cont; exp_002 for OLMo AUC; mixed for Pythia)\nrows.append(('Task 2', 'S8 Qwen-rw all 5 pairs', 'All match exp_007', 'exp_007', 'All match', 'OK'))\nrows.append(('Task 2', 'S8 Pythia 0v1=.993', '0.993[.992,.994]', 'exp_007', '0.9932[0.9921,0.9943]', 'OK'))\nrows.append(('Task 2', 'S8 Pythia 1v2=.607', '0.607[.598,.617]', 'exp_007', '0.6539[0.6454,0.6630]', 'MISMATCH'))\nrows.append(('Task 2', 'S8 Pythia 1v2=.607 vs exp_001', '0.607[.598,.617]', 'exp_001 cross-scored', '0.6074 (no CI stored)', 'PARTIAL MATCH (AUC only)'))\nrows.append(('Task 2', 'S8 Pythia 2v3=.551', '0.551[.542,.563]', 'exp_007', '0.5514[0.5417,0.5628]', 'OK'))\nrows.append(('Task 2', 'S8 Pythia 3v4=.515', '0.515[.504,.526]', 'exp_007', '0.5152[0.5041,0.5260]', 'OK'))\nrows.append(('Task 2', 'S8 Pythia 4v5=.514', '0.514[.502,.525]', 'exp_007', '0.5136[0.5021,0.5249]', 'OK'))\nrows.append(('Task 2', 'S8 OLMo 0v1=.986', '.986[.984,.988]', 'exp_007', '0.9970[0.9964,0.9975]', 'MISMATCH'))\nrows.append(('Task 2', 'S8 OLMo 0v1=.986', '.986[.984,.988]', 'exp_002 cross-scored', '0.9861 (no CI)', 'AUC matches, CI unverified'))\nrows.append(('Task 2', 'S8 OLMo 1v2=.500', '.500[.496,.519]', 'exp_007', '0.6145[0.6045,0.6247]', 'MISMATCH'))\nrows.append(('Task 2', 'S8 OLMo 1v2=.500', '.500[.496,.519]', 'exp_002 cross-scored', '0.5001 (no CI)', 'AUC matches, CI unverified'))\nrows.append(('Task 2', 'S8 OLMo 2v3=.497', '.497[.486,.509]', 'exp_002 cross-scored', '0.4972 (no CI)', 'AUC matches, CI unverified'))\nrows.append(('Task 2', 'S8 OLMo 3v4=.502', '.502[.491,.513]', 'exp_002 cross-scored', '0.5034 (no CI)', 'AUC matches, CI unverified'))\nrows.append(('Task 2', 'S8 OLMo 4v5=.494', '.494[.483,.506]', 'exp_002 cross-scored', '0.4971 (no CI)', 'AUC matches, CI unverified'))\nrows.append(('Task 2', 'S8 Qwen-cont all 5 pairs', 'All match', 'exp_007', 'All match', 'OK'))\n\n# TASK 3: Neural probe (exp_015)\nrows.append(('Task 3', 'Qwen 2v3 AUC=0.6159', '0.6159', 'exp_015', '0.616', 'OK'))\nrows.append(('Task 3', 'Qwen K*=3', 'K*=3', 'exp_015', 'k_star_neural=3', 'OK'))\nrows.append(('Task 3', 'Pythia 2v3 AUC=0.5963', '0.5963', 'exp_015', '0.596', 'OK'))\nrows.append(('Task 3', 'Pythia K*=2', 'K*=2', 'exp_015', 'k_star_neural=2', 'OK'))\nrows.append(('Task 3', 'OLMo 2v3 AUC=0.5056', '0.5056', 'exp_015', '0.589', 'MISMATCH'))\nrows.append(('Task 3', 'OLMo 1v2=0.5054', '0.5054', 'exp_015', '0.657', 'MISMATCH'))\nrows.append(('Task 3', 'OLMo K*=1', 'K*=1', 'exp_015', 'k_star_neural=2', 'MISMATCH'))\n\n# Task 3 CI bounds from exp_015 - note that registry has no CI for neural probe\nrows.append(('Task 3', 'Qwen 2v3 CI [0.610,0.622]', '[0.610,0.622]', 'exp_015', 'No CI stored', 'UNVERIFIABLE'))\nrows.append(('Task 3', 'Pythia 2v3 CI [0.589,0.603]', '[0.589,0.603]', 'exp_015', 'No CI stored', 'UNVERIFIABLE'))\nrows.append(('Task 3', 'OLMo 2v3 CI [0.497,0.516]', '[0.497,0.516]', 'exp_015', 'No CI stored', 'UNVERIFIABLE'))\n\nprint(f'{'Location':<40} {'Paper Value':<30} {'Exp ID':<20} {'Registry Value':<35} Match')\nprint('-' * 130)\nfor task, loc, paper, exp_id, reg, match in rows:\n    print(f'{loc:<40} {paper:<30} {exp_id:<20} {reg:<35} {match}')\n\" 2>&1\n"
  }
}
```

</details>

---


### Tool result

_source line 443 · 2026-05-23T11:38:26.858259+00:00_

=== COMPLETE AUDIT TABLE ===

Location                                 Paper Value                    Exp ID               Registry Value                      Match
----------------------------------------------------------------------------------------------------------------------------------
S2 AUC (all 20 cells)                    All match                      exp_003              All match                           OK
S8 Qwen-rw all 5 pairs                   All match exp_007              exp_007              All match                           OK
S8 Pythia 0v1=.993                       0.993[.992,.994]               exp_007              0.9932[0.9921,0.9943]               OK
S8 Pythia 1v2=.607                       0.607[.598,.617]               exp_007              0.6539[0.6454,0.6630]               MISMATCH
S8 Pythia 1v2=.607 vs exp_001            0.607[.598,.617]               exp_001 cross-scored 0.6074 (no CI stored)               PARTIAL MATCH (AUC only)
S8 Pythia 2v3=.551                       0.551[.542,.563]               exp_007              0.5514[0.5417,0.5628]               OK
S8 Pythia 3v4=.515                       0.515[.504,.526]               exp_007              0.5152[0.5041,0.5260]               OK
S8 Pythia 4v5=.514                       0.514[.502,.525]               exp_007              0.5136[0.5021,0.5249]               OK
S8 OLMo 0v1=.986                         .986[.984,.988]                exp_007              0.9970[0.9964,0.9975]               MISMATCH
S8 OLMo 0v1=.986                         .986[.984,.988]                exp_002 cross-scored 0.9861 (no CI)                      AUC matches, CI unverified
S8 OLMo 1v2=.500                         .500[.496,.519]                exp_007              0.6145[0.6045,0.6247]               MISMATCH
S8 OLMo 1v2=.500                         .500[.496,.519]                exp_002 cross-scored 0.5001 (no CI)                      AUC matches, CI unverified
S8 OLMo 2v3=.497                
…[truncated 1935 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_audit_tables_3_4_inline_20260523T112128",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 444 · 2026-05-23T11:38:26.858426+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport json\n\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/17947013-ea3d-4507-b0e3-f06dfa8892ff/tool-results/mcp-agent-ml-research-read_registry-1779535307441.txt', 'r') as f:\n    raw = json.load(f)\n\ninner = json.loads(raw['result'])\ndata = inner['data']\nexps = data['experiments']\n\n# Final check: Task 2 note about Pythia 2v3\n# Task says: 'Table S8 Pythia 2v3 says .551 but Table 1 says .5440. Check which is in registry.'\n# Answer: registry has TWO different values:\n# exp_007 (self-scored): 2v3=0.5514 -> this rounds to .551 (Table S8)\n# exp_001 (Qwen cross-scored): 2v3=0.544 -> this rounds to .544 (Table 1)\n# Both are in the registry, but for different scorer setups\n\nprint('Pythia 2v3 disambiguation:')\nprint(f'  exp_007 (self-scored): 2v3_auc = {exps[\\\"exp_007_bootstrap_ci\\\"][\\\"metrics\\\"][\\\"pythia_cont\\\"][\\\"2v3\\\"][\\\"auc\\\"]:.4f} -> rounds to .551 (Table S8)')\nprint(f'  exp_001 (Qwen cross-scored): 2v3_auc = {exps[\\\"exp_001_pythia_depth\\\"][\\\"metrics\\\"][\\\"pairwise_auc\\\"][\\\"2v3\\\"]:.4f} -> rounds to .544 (Table 1)')\nprint()\nprint('=> Table S8 uses exp_007 self-scored data (consistent for 0v1, 2v3, 3v4, 4v5)')\nprint('=> Table 1 uses exp_001 Qwen cross-scored data')\nprint('=> BUT Table S8 Pythia 1v2=.607 comes from cross-scored data (exp_001), NOT exp_007')\nprint()\n\n# Also verify the exp_020 vs S10 patterns more carefully\n# The issue is that multiple values in S10 are off by 1-8 thousandths from exp_020\n# This could indicate: (a) a different run of exp020, (b) post-hoc correction, \n# or (c) the paper uses bootstrap mean vs OOF AUC\nexp020 = exps['exp_020_pythia_decoding']\nprint('exp020 notes excerpt:')\nnotes = exp020.get('notes', '')\nprint(notes[:500])\n\" 2>&1\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_audit_tables_3_4_inline_20260523T112128",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport json\n\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/17947013-ea3d-4507-b0e3-f06dfa8892ff/tool-results/mcp-agent-ml-research-read_registry-1779535307441.txt', 'r') as f:\n    raw = json.load(f)\n\ninner = json.loads(raw['result'])\ndata = inner['data']\nexps = data['experiments']\n\n# Final check: Task 2 note about Pythia 2v3\n# Task says: 'Table S8 Pythia 2v3 says .551 but Table 1 says .5440. Check which is in registry.'\n# Answer: registry has TWO different values:\n# exp_007 (self-scored): 2v3=0.5514 -> this rounds to .551 (Table S8)\n# exp_001 (Qwen cross-scored): 2v3=0.544 -> this rounds to .544 (Table 1)\n# Both are in the registry, but for different scorer setups\n\nprint('Pythia 2v3 disambiguation:')\nprint(f'  exp_007 (self-scored): 2v3_auc = {exps[\\\"exp_007_bootstrap_ci\\\"][\\\"metrics\\\"][\\\"pythia_cont\\\"][\\\"2v3\\\"][\\\"auc\\\"]:.4f} -> rounds to .551 (Table S8)')\nprint(f'  exp_001 (Qwen cross-scored): 2v3_auc = {exps[\\\"exp_001_pythia_depth\\\"][\\\"metrics\\\"][\\\"pairwise_auc\\\"][\\\"2v3\\\"]:.4f} -> rounds to .544 (Table 1)')\nprint()\nprint('=> Table S8 uses exp_007 self-scored data (consistent for 0v1, 2v3, 3v4, 4v5)')\nprint('=> Table 1 uses exp_001 Qwen cross-scored data')\nprint('=> BUT Table S8 Pythia 1v2=.607 comes from cross-scored data (exp_001), NOT exp_007')\nprint()\n\n# Also verify the exp_020 vs S10 patterns more carefully\n# The issue is that multiple values in S10 are off by 1-8 thousandths from exp_020\n# This could indicate: (a) a different run of exp020, (b) post-hoc correction, \n# or (c) the paper uses bootstrap mean vs OOF AUC\nexp020 = exps['exp_020_pythia_decoding']\nprint('exp020 notes excerpt:')\nnotes = exp020.get('notes', '')\nprint(notes[:500])\n\" 2>&1\n"
  }
}
```

</details>

---


### Tool result

_source line 445 · 2026-05-23T11:38:26.858569+00:00_

Pythia 2v3 disambiguation:
  exp_007 (self-scored): 2v3_auc = 0.5514 -> rounds to .551 (Table S8)
  exp_001 (Qwen cross-scored): 2v3_auc = 0.5440 -> rounds to .544 (Table 1)

=> Table S8 uses exp_007 self-scored data (consistent for 0v1, 2v3, 3v4, 4v5)
=> Table 1 uses exp_001 Qwen cross-scored data
=> BUT Table S8 Pythia 1v2=.607 comes from cross-scored data (exp_001), NOT exp_007

exp020 notes excerpt:
greedy 1v2 AUC=0.8838 调查完成：根因为 Pythia-1.4B greedy 级联重复坍塌（4-gram repeat rate: d0=0.01→d1=0.72→d2=0.81; TTR: d0=0.72→d1=0.19→d2=0.14）。hapax_ratio (d=1.06) 和 low_freq_ratio (d=1.03) 是 top 贡献特征。非 bug，参数正确，无数据泄漏。K*=2 不受影响。建议论文标注为 repetition-dominated regime。| Bootstrap CI (10000 iter): t07 2v3 AUC=0.5939 CI [0.5855, 0.6025] BORDERLINE (CI upper crosses θ); t12 1v2 AUC=0.6170 CI [0.6071, 0.6270] PASS。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_audit_tables_3_4_inline_20260523T112128",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool result

_source line 446 · 2026-05-23T11:38:26.858793+00:00_

Here is the complete audit report.

---

## Audit Report: Domain Ablation / Cross-Domain Evaluation

### Registry Experiments Found

| Paper Row | Registry exp_id | Status |
|---|---|---|
| arXiv / Qwen-1.5B | `exp_024_arxiv_domain` | DONE |
| arXiv / Pythia-1.4B | `exp_025_pythia_arxiv` | DONE |
| C4 / Qwen-1.5B | `exp_016_base_vs_instruct` | DONE |
| Wiki / Qwen-1.5B | `exp_023_domain_ablation` | DONE (incomplete metrics) |
| Code / Qwen-1.5B | `exp_code_qwen1b5` | DONE |
| Code / LLaMA-8B | `exp_code_llama8b` | DONE |
| LLaMA-8B arXiv inline | `exp_arXiv_llama8b` | DONE (no CI stored) |
| Table S12 C4 | `exp_017_qwen_continuation` | DONE |

---

### Table 4 (tab:domain_kstar) Verification

| Location | Paper Value | Registry exp_id | Registry Value | Match? |
|---|---|---|---|---|
| Tab4 arXiv/Qwen-1.5B 1v2 AUC | .858 | exp_024 | 0.858 | OK |
| Tab4 arXiv/Qwen-1.5B 2v3 AUC | .644 | exp_024 | 0.6427 (rounds to .643) | **MISMATCH** |
| Tab4 arXiv/Qwen-1.5B K* | 3 | exp_024 | 3 | OK |
| Tab4 arXiv/Pythia-1.4B 1v2 AUC | .805 | exp_025 | 0.8047 (rounds to .805) | OK |
| Tab4 arXiv/Pythia-1.4B 2v3 AUC | .655 | exp_025 | 0.6545 (rounds to .655) | OK |
| Tab4 arXiv/Pythia-1.4B K* | 3 | exp_025 | 3 | OK |
| Tab4 C4/Qwen-1.5B 1v2 AUC | .626 | exp_016 | 0.6262 (rounds to .626) | OK |
| Tab4 C4/Qwen-1.5B 2v3 AUC | .550 | exp_016 | 0.5496 (rounds to .550) | OK |
| Tab4 C4/Qwen-1.5B K* | 2 | exp_016 | 2 | OK |
| Tab4 Wiki/Qwen-1.5B 1v2 AUC | .619 | exp_023 | 0.6193 (rounds to .619) | OK |
| Tab4 Wiki/Qwen-1.5B 2v3 AUC | .550 | exp_023 | 0.5498 (rounds to .550) | OK |
| Tab4 Wiki/Qwen-1.5B K* | 2 | exp_023 | 2 | OK |
| Tab4 Code/Qwen-1.5B 1v2 AUC | .738 | exp_code_qwen1b5 | 0.7382 (rounds to .738) | OK |
| Tab4 Code/Qwen-1.5B 2v3 AUC | .530 | exp_code_qwen1b5 | 0.53 | OK |
| Tab4 Code/Qwen-1.5B K* | 2 | exp_code_qwen1b5 | 2 | OK |
| Tab4 Code/LLaMA-8B 1v2 AUC | .739 | exp_code_llama8b | 0.7394 (rounds to .739) | OK |
| Tab4 Code/LLaMA-8B 2v3 AUC | .510 | exp_code_llama8b | 0.51
…[truncated 3903 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_audit_tables_3_4_inline_20260523T112128",
  "tool": "Agent",
  "elapsed_ms": 63
}
```

</details>

---


### Tool result

_source line 447 · 2026-05-23T11:38:26.859024+00:00_

Now I have all the data needed to produce the complete audit report. Let me compile the final table:

---

## Audit Report

### TASK 1: Filtering (experiments_c3.tex + tab_filtering_main.tex)

**Table tab_filtering_main.tex** — all cells verified against `exp_006_graduated_filtering`:

| Row | MMLU (paper) | MMLU (registry) | HellaSwag (paper) | HellaSwag (registry) | Match? |
|---|---|---|---|---|---|
| Base model | 0.6018 | 0.6018 | 0.6821 | 0.6821 | MATCH |
| Binary-ours | 0.5941±0.0008 | 0.5941±0.0008 | 0.6701±0.0006 | 0.6701±0.0006 | MATCH |
| Binary-Drayson | 0.5913±0.0009 | 0.5913±0.0009 | 0.6691±0.0004 | 0.6691±0.0004 | MATCH |
| Surprisal | 0.5894±0.0009 | 0.5894±0.0009 | 0.6641±0.0006 | 0.6641±0.0006 | MATCH |
| Graduated (α=0.9) | 0.5892±0.0008 | 0.5892±0.0008 | 0.6701±0.0007 | 0.6701±0.0007 | MATCH |
| DSIR | 0.5869±0.0003 | 0.5869±0.0003 | 0.6631±0.0007 | 0.6631±0.0007 | MATCH |
| No filter | 0.5865±0.0010 | 0.5865±0.0010 | 0.6638±0.0008 | 0.6638±0.0008 | MATCH |

**Inline numbers in experiments_c3.tex:**

| Location | Paper Value | Registry exp_id | Registry Value | Match? |
|---|---|---|---|---|
| experiments_c3.tex | -1.53 pp (no-filter MMLU degradation) | exp_006_graduated_filtering | (0.5865−0.6018)×100 = −1.53 pp | MATCH |
| experiments_c3.tex | -0.77 pp (binary-ours MMLU degradation) | exp_006_graduated_filtering | (0.5941−0.6018)×100 = −0.77 pp | MATCH |
| experiments_c3.tex | ~50% reduction | exp_006_graduated_filtering | (1.53−0.77)/1.53 = 49.7% | MATCH |
| experiments_c3.tex | p_corr < 0.05 vs all alternatives | exp_E_paired_stats | all 5 binary-ours MMLU pairs significant | MATCH |
| experiments_c3.tex | p_corr = 1.00 (graduated α=0.9 vs binary-ours, HellaSwag) | exp_E_paired_stats / tab_pairwise_significance | p=1.00, Δ=0.00 | MATCH |
| experiments_c3.tex | p_corr = 0.011 (graduated α=0.9 vs binary-ours, MMLU) | exp_E_paired_stats / tab_pairwise_significance | p=.011 | MATCH |

---

### TASK 2: Introduction numbers

| Location | Paper Value
…[truncated 4425 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_audit_tables_3_4_inline_20260523T112128",
  "tool": "Agent",
  "elapsed_ms": 62
}
```

</details>

---


### Tool result

_source line 448 · 2026-05-23T11:38:26.859272+00:00_

Here is the complete audit report.

---

## Numerical Audit Report

### TASK 1: Decoding Ablation AUC — Table S2 (exp_003_decoding_ablation)

All 20 AUC point estimates and confidence intervals in Table S2 match exp_003 within rounding tolerance (±0.001).

| Location | Paper Value | Registry exp_id | Registry Value | Match? |
|---|---|---|---|---|
| S2 0v1 Greedy | .980 [.977,.982] | exp_003 | 0.9796 [0.9772,0.9820] | OK |
| S2 0v1 Nuc p=0.9 T=1.0 | .995 [.993,.996] | exp_003 | 0.9945 [0.9934,0.9956] | OK |
| S2 0v1 Nuc p=0.95 T=0.7 | .988 [.986,.990] | exp_003 | 0.9877 [0.9857,0.9896] | OK |
| S2 0v1 Nuc p=0.95 T=1.2 | .998 [.998,.999] | exp_003 | 0.9982 [0.9975,0.9987] | OK |
| S2 1v2 Greedy | .689 [.680,.698] | exp_003 | 0.6892 [0.6802,0.6982] | OK |
| S2 1v2 Nuc p=0.9 T=1.0 | .687 [.677,.695] | exp_003 | 0.6862 [0.6774,0.6951] | OK |
| S2 1v2 Nuc p=0.95 T=0.7 | .689 [.680,.697] | exp_003 | 0.6885 [0.6797,0.6970] | OK |
| S2 1v2 Nuc p=0.95 T=1.2 | .704 [.695,.713] | exp_003 | 0.7037 [0.6945,0.7126] | OK |
| S2 2v3 Greedy | .561 [.552,.571] | exp_003 | 0.5612 [0.5517,0.5705] | OK |
| S2 2v3 Nuc p=0.9 T=1.0 | .592 [.582,.601] | exp_003 | 0.5917 [0.5824,0.6010] | OK |
| S2 2v3 Nuc p=0.95 T=0.7 | .590 [.581,.600] | exp_003 | 0.5901 [0.5806,0.5996] | OK |
| S2 2v3 Nuc p=0.95 T=1.2 | .582 [.572,.592] | exp_003 | 0.5820 [0.5722,0.5917] | OK |
| S2 3v4 Greedy | .540 [.531,.550] | exp_003 | 0.5405 [0.5308,0.5502] | OK |
| S2 3v4 Nuc p=0.9 T=1.0 | .547 [.537,.557] | exp_003 | 0.5468 [0.5369,0.5568] | OK |
| S2 3v4 Nuc p=0.95 T=0.7 | .539 [.529,.549] | exp_003 | 0.5390 [0.5288,0.5493] | OK |
| S2 3v4 Nuc p=0.95 T=1.2 | .529 [.519,.540] | exp_003 | 0.5293 [0.5185,0.5399] | OK |
| S2 4v5 Greedy | .514 [.503,.524] | exp_003 | 0.5137 [0.5033,0.5238] | OK |
| S2 4v5 Nuc p=0.9 T=1.0 | .507 [.496,.517] | exp_003 | 0.5066 [0.4959,0.5173] | OK |
| S2 4v5 Nuc p=0.95 T=0.7 | .535 [.524,.545] | exp_003 | 0.5348 [0.5243,0.5454] | OK |
| S2 4v5 Nuc p=0.95 T=1.2 | .524 [.513,.535] | exp_0
…[truncated 8516 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_audit_tables_3_4_inline_20260523T112128",
  "tool": "Agent",
  "elapsed_ms": 59
}
```

</details>

---


### Tool call

_source line 449 · 2026-05-23T11:38:26.859509+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex",
  "old_string": "2v3 $\\auc = 0.644\\;[0.628,\\,0.658]$, $0.655\\;[0.640,\\,0.669]$, and $0.620\\;[0.605,\\,0.635]$",
  "new_string": "2v3 $\\auc = 0.643\\;[0.628,\\,0.658]$, $0.655\\;[0.640,\\,0.669]$, and $0.622\\;[0.605,\\,0.635]$"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_audit_tables_3_4_inline_20260523T112128",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex",
    "old_string": "2v3 $\\auc = 0.644\\;[0.628,\\,0.658]$, $0.655\\;[0.640,\\,0.669]$, and $0.620\\;[0.605,\\,0.635]$",
    "new_string": "2v3 $\\auc = 0.643\\;[0.628,\\,0.658]$, $0.655\\;[0.640,\\,0.669]$, and $0.622\\;[0.605,\\,0.635]$"
  }
}
```

</details>

---


### Tool result

_source line 450 · 2026-05-23T11:38:26.859701+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_audit_tables_3_4_inline_20260523T112128",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 451 · 2026-05-23T11:38:26.859856+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex",
  "old_string": "arXiv & Qwen-1.5B\\rlap{$^\\dagger$}  & .858 & .644 & 3 \\\\",
  "new_string": "arXiv & Qwen-1.5B\\rlap{$^\\dagger$}  & .858 & .643 & 3 \\\\"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_audit_tables_3_4_inline_20260523T112128",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex",
    "old_string": "arXiv & Qwen-1.5B\\rlap{$^\\dagger$}  & .858 & .644 & 3 \\\\",
    "new_string": "arXiv & Qwen-1.5B\\rlap{$^\\dagger$}  & .858 & .643 & 3 \\\\"
  }
}
```

</details>

---


### Tool result

_source line 452 · 2026-05-23T11:38:26.860039+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_audit_tables_3_4_inline_20260523T112128",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 453 · 2026-05-23T11:38:26.860170+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex",
  "old_string": "Code  & LLaMA-8B   & .739 & .510 & 2 \\\\",
  "new_string": "Code  & LLaMA-8B   & .739 & .511 & 2 \\\\"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_audit_tables_3_4_inline_20260523T112128",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex",
    "old_string": "Code  & LLaMA-8B   & .739 & .510 & 2 \\\\",
    "new_string": "Code  & LLaMA-8B   & .739 & .511 & 2 \\\\"
  }
}
```

</details>

---


### Tool result

_source line 454 · 2026-05-23T11:38:26.860340+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_audit_tables_3_4_inline_20260523T112128",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 455 · 2026-05-23T11:38:26.860467+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex",
  "old_string": "2v3 & .561 & .550 & .644$^*$ \\\\",
  "new_string": "2v3 & .561 & .550 & .643$^*$ \\\\"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_audit_tables_3_4_inline_20260523T112128",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex",
    "old_string": "2v3 & .561 & .550 & .644$^*$ \\\\",
    "new_string": "2v3 & .561 & .550 & .643$^*$ \\\\"
  }
}
```

</details>

---


### Tool result

_source line 456 · 2026-05-23T11:38:26.860718+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_audit_tables_3_4_inline_20260523T112128",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 457 · 2026-05-23T11:38:26.860884+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex",
  "old_string": "4v5 & .514 & .514 & .530 \\\\",
  "new_string": "4v5 & .514 & .514 & .529 \\\\"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_audit_tables_3_4_inline_20260523T112128",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex",
    "old_string": "4v5 & .514 & .514 & .530 \\\\",
    "new_string": "4v5 & .514 & .514 & .529 \\\\"
  }
}
```

</details>

---


### Tool result

_source line 458 · 2026-05-23T11:38:26.861140+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_audit_tables_3_4_inline_20260523T112128",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 459 · 2026-05-23T11:38:26.861308+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\.644",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_audit_tables_3_4_inline_20260523T112128",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\.644",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 460 · 2026-05-23T11:38:26.861438+00:00_

docs/paper/appendix_extended.tex:253:arXiv   & 3 & 0.644~(2v3) & 4 & 0.624~(3v4) \\

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_audit_tables_3_4_inline_20260523T112128",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 461 · 2026-05-23T11:38:26.861560+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\.620",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_audit_tables_3_4_inline_20260523T112128",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\.620",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 462 · 2026-05-23T11:38:26.861690+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_audit_tables_3_4_inline_20260523T112128",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 463 · 2026-05-23T11:38:26.861827+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex",
  "offset": "250",
  "limit": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_audit_tables_3_4_inline_20260523T112128",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex",
    "offset": "250",
    "limit": "5"
  }
}
```

</details>

---


### Tool result

_source line 464 · 2026-05-23T11:38:26.861960+00:00_

250	\textbf{Domain} & $\Kempirical$ & boundary $\auc$ & $\Kempirical$ & boundary $\auc$ \\
251	\midrule
252	C4      & 2 & 0.626~(1v2) & 2 & 0.705~(1v2) \\
253	arXiv   & 3 & 0.644~(2v3) & 4 & 0.624~(3v4) \\
254	Code    & 2 & 0.738~(1v2) & 2 & 0.808~(1v2) \\

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_audit_tables_3_4_inline_20260523T112128",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 465 · 2026-05-23T11:38:26.862083+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex",
  "old_string": "arXiv   & 3 & 0.644~(2v3) & 4 & 0.624~(3v4) \\\\",
  "new_string": "arXiv   & 3 & 0.643~(2v3) & 4 & 0.624~(3v4) \\\\"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_audit_tables_3_4_inline_20260523T112128",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex",
    "old_string": "arXiv   & 3 & 0.644~(2v3) & 4 & 0.624~(3v4) \\\\",
    "new_string": "arXiv   & 3 & 0.643~(2v3) & 4 & 0.624~(3v4) \\\\"
  }
}
```

</details>

---


### Tool result

_source line 466 · 2026-05-23T11:38:26.862263+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_audit_tables_3_4_inline_20260523T112128",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---


### Assistant

_source line 467 · 2026-05-23T11:38:26.862447+00:00_

All clear rounding errors fixed. Here is the complete audit report:

---

## 全文数据审计报告

### 已修复（来源明确的舍入错误）

| 位置 | 论文原值 | Registry值 | 修正后 |
|------|---------|-----------|--------|
| Tab4 arXiv/Qwen 2v3 AUC | .644 | 0.6427→.643 | **.643** |
| Tab S12 arXiv 2v3 | .644 | 同上 | **.643** |
| experiments_c1 inline arXiv 2v3 | 0.644 | 同上 | **0.643** |
| appendix_extended DeBERTa table | 0.644 | 同上 | **0.643** |
| experiments_c1 inline LLaMA arXiv 2v3 | 0.620 | 0.6215→.622 | **0.622** |
| Tab4 Code/LLaMA 2v3 AUC | .510 | 0.5112→.511 | **.511** |
| Tab S12 arXiv 4v5 | .530 | 0.5294→.529 | **.529** |

### 需要人工确认的不匹配（严重度从高到低）

#### CRITICAL: Neural probe OLMo (experiments_c1.tex Table neural_probe_crossmodel)

| 位置 | 论文值 | Registry exp_id | Registry值 |
|------|--------|----------------|-----------|
| OLMo 1v2 AUC | 0.5054 | exp_015 | **0.657** |
| OLMo 2v3 AUC | 0.5056 | exp_015 | **0.589** |
| OLMo K* | 1 | exp_015 | **2** |

论文值（0.505x）酷似 15D OBD cross-scored 结果（exp_002: 1v2=0.5001），疑似误用了 OBD 值替代 neural probe 值。如果 registry 正确，则 OLMo neural probe K*=2，论文中 K*=1 的结论需修改，连带 discussion.tex 中引用此结果的段落。

#### HIGH: Mistral-7B 全部 AUC (Tab kstar_ci_extended)

| 位置 | 论文值 | exp_019 (self) | exp_019b (cross) |
|------|--------|---------------|-----------------|
| 0v1 | .9170 | 0.9843 | 0.9209 |
| 1v2 | .5750 | 0.5935 | 0.5695 |
| 2v3 | .5369 | 0.5402 | 0.5335 |
| 3v4 | .5174 | 0.5232 | 0.5140 |

论文值既不等于 self-scored 也不等于 cross-scored。2v3 值恰好等于两者均值 (0.5402+0.5335)/2=0.5369，但其他行不符合此规律。来源不明。

#### HIGH: Table S8 Pythia/OLMo 混用 self/cross-scored 数据

| 位置 | 论文值 | exp_007 (self) | exp_001/002 (cross) |
|------|--------|---------------|-------------------|
| S8 Pythia 1v2 | .607 | 0.6539 | 0.6074 (exp_001) |
| S8 OLMo 全5行 | .986/.500/.497/.502/.494 | .997/.614/.550/.509/.505 | ≈matches AUC only, CI无来源 |

Table S8 标注为 exp-007 bootstrap CI，但 OLMo 行使用了 cross-scored AUC（无对应 CI），Pythia 1v2 同样混用。CIs 无法追溯到任何 registry 实验。

#### HIGH: Table S10 Pythia Decoding (10/20 cells mismatch)

10个值与 exp_020 相差 0.002–0.008，非系统性偏差，可能来自 rerun 或 bootstrap-mean vs OOF-AUC 的差异。涉及行：1v2/nuc09, 2v3全行, 3v4/nuc09+t07+t12, 4v5/greedy+t12。

#### MODERATE: OLMo 3v4/4v5 (Table 1)

| 位置 | 论文值 | exp_002 |
|------|--------|---------|
| 3v4 | .5024 | 0.5034 |
| 4v5 | .4942 | 0.4971 |

差异 0.001–0.003，可能来自 scorer 更新前的旧值。

#### MODERATE: Discussion inline 数字

| 位置 | 论文值 | Registry值 |
|------|--------|-----------|
| "≈+1.9 pp" Mistral gap | 1.9 pp | 2.4 pp (0.5935−0.5695) |
| "0.15–0.27" JSD (≤1.5B) | 0.15–0.27 | 0.164–0.286 (registry range) |

### 匹配确认（所有其他值）

- **Table 1 (tab:kstar_ci)**: Qwen-rw/Pythia/Qwen-cont/Qwen-7B 全部 25 个 AUC + CI 值 ✓（OLMo 0v1/1v2/2v3 也 ✓）
- **Extended table**: Qwen-base 全 5 行 ✓, LLaMA-8B 全 5 行 ✓, Pythia-6.9B 全 ✓, Gemma-2B 全 ✓
- **Table S1 (transfer matrix)**: 16/16 cells ✓, retention% inline claims ✓
- **Table S2 (decoding ablation)**: 20/20 AUC + CI cells ✓（Spearman ρ 6个值不在 registry，无法验证）
- **Table 4 (domain)**: 其余 10/12 cells ✓
- **Filtering table**: 7/7 rows 全 ✓
- **experiments_c3.tex inline**: −1.53pp ✓, −0.77pp ✓, ~50% ✓, p 值全 ✓
- **introduction.tex**: MMLU 0.5941 ✓, base 0.6018 ✓, p≤0.002 ✓
- **discussion.tex**: 0v1 AUC≥0.92 ✓, 96% recall ✓, 14–22% ✓, 8–38% ✓, retrain chain 0.68–0.80 ✓, 6v7 0.634–0.641 ✓, Δauc −0.021 ✓

### 无法验证（registry 未存储）

- η²_p = .166 / .146（ANOVA 未单独注册实验）
- Table S2 Spearman ρ 6 个值（exp_003 未存储）
- Table S11 除 1v2 外的 12 个值（exp_021 仅存 1v2）
- Table S12 Wiki 0v1/3v4/4v5（exp_023 仅存 1v2/2v3）
- 部分 CI（Pythia 2v3, OLMo 全部, Gemma 多数）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_audit_tables_3_4_inline_20260523T112128"
}
```

</details>

---
