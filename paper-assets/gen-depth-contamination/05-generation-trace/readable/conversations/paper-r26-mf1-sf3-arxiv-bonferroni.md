# paper r26 mf1 sf3 arxiv bonferroni

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 131
- **Recorded user turns:** 0
- **Tool calls:** 65
- **Original source:** `logs/chats/worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230.jsonl`
- **Structured JSON:** [`8def8b0818306050b56b.json`](../../sessions/8d/8def8b0818306050b56b.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

131 recorded events

### Tool call

_source line 1 · 2026-05-22T08:36:59.163977+00:00_

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
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
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

_source line 2 · 2026-05-22T08:36:59.164367+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-22T08:36:59.164565+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "cat /root/autodl-tmp/gen-depth-contamination/results/exp024_bootstrap_ci.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "cat /root/autodl-tmp/gen-depth-contamination/results/exp024_bootstrap_ci.json",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-22T08:36:59.164703+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "cat /root/autodl-tmp/gen-depth-contamination/results/exp025_bootstrap_ci.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "cat /root/autodl-tmp/gen-depth-contamination/results/exp025_bootstrap_ci.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-22T08:36:59.164885+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"cat: /root/autodl-tmp/gen-depth-contamination/results/exp024_bootstrap_ci.json: No such file or directory\\n\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.86}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-22T08:36:59.165036+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"cat: /root/autodl-tmp/gen-depth-contamination/results/exp025_bootstrap_ci.json: No such file or directory\\n\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-22T08:36:59.165164+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "find /root/autodl-tmp/gen-depth-contamination -name \"*bootstrap_ci*\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "find /root/autodl-tmp/gen-depth-contamination -name \"*bootstrap_ci*\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-22T08:36:59.165316+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/gen-depth-contamination/artifacts/borderline_bootstrap_ci.json\\n/root/autodl-tmp/gen-depth-contamination/artifacts/crossscorer_bootstrap_ci.json\\n/root/autodl-tmp/gen-depth-contamination/artifacts/exp016_bootstrap_ci.json\\n/root/autodl-tmp/gen-depth-contamination/artifacts/exp018_bootstrap_ci.json\\n/root/autodl-tmp/gen-depth-contamination/artifacts/exp019_bootstrap_ci.json\\n/root/autodl-tmp/gen-depth-contamination/artifacts/exp024_bootstrap_ci.json\\n/root/autodl-tmp/gen-depth-contamination/artifacts/exp025_bootstrap_ci.json\\n/root/autodl-tmp/gen-depth-contamination/artifacts/exp_gemma2b_depth_bootstrap_ci.json\\n/root/autodl-tmp/gen-depth-contamination/results/exp007_olmo_rerun/bootstrap_ci_olmo_rerun.json\\n/root/autodl-tmp/gen-depth-contamination/results/exp_008_retrain_chain/bootstrap_ci.json\\n/root/autodl-tmp/gen-depth-contamination/results/exp_008_retrain_chain/bootstrap_ci_v2.json\\n/root/autodl-tmp/gen-depth-contamination/results/exp_027_latex_ablation/bootstrap_ci_results.json\\n/root/autodl-tmp/gen-depth-contamination/results/exp_14b_c4/bootstrap_ci_results.json\\n/root/autodl-tmp/gen-depth-contamination/results/exp_olmo_retrain_chain/bootstrap_ci.json\\n/root/autodl-tmp/gen-depth-contamination/results/exp_qwen_retrain_chain/bootstrap_ci.json\\n/root/autodl-tmp/gen-depth-contamination/scripts/borderline_bootstrap_ci.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/crossscorer_bootstrap_ci.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/exp007_olmo_rerun_bootstrap_ci.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/exp016_bootstrap_ci.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/exp018_bootstrap_ci.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/exp019_bootstrap_ci.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/exp024_bootstrap_ci.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/olmo_c4_bootstrap_ci.py\\n/root/autodl-tmp/gen-depth-conta
…[truncated 301 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-22T08:36:59.165473+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "ls /root/autodl-tmp/gen-depth-contamination/docs/paper/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "ls /root/autodl-tmp/gen-depth-contamination/docs/paper/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-22T08:36:59.165617+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"acl.sty\\nacl_natbib.bst\\nappendix.tex\\nappendix_extended.tex\\nconclusion.tex\\ndiscussion.tex\\nexperiments_c1.tex\\nexperiments_c3.tex\\nfigures\\nintroduction.tex\\nmain.aux\\nmain.bbl\\nmain.blg\\nmain.fdb_latexmk\\nmain.fls\\nmain.log\\nmain.out\\nmain.pdf\\nmain.tex\\nmethod.tex\\nreferences.bib\\nrelated_work.tex\\ntables\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.39}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-22T08:36:59.165840+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "cat /root/autodl-tmp/gen-depth-contamination/artifacts/exp024_bootstrap_ci.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "cat /root/autodl-tmp/gen-depth-contamination/artifacts/exp024_bootstrap_ci.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-22T08:36:59.166051+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"experiment\\\": \\\"exp-024 Qwen2.5-1.5B-base arXiv continuation\\\",\\n  \\\"method\\\": \\\"GroupKFold(5) OOF + doc-level bootstrap + label permutation\\\",\\n  \\\"n_bootstrap\\\": 10000,\\n  \\\"n_permutation\\\": 10000,\\n  \\\"seed\\\": 42,\\n  \\\"theta\\\": 0.6,\\n  \\\"kstar_ci\\\": 3,\\n  \\\"total_seconds\\\": 147.4,\\n  \\\"pairs\\\": {\\n    \\\"0v1\\\": {\\n      \\\"auc\\\": 0.9946,\\n      \\\"auc_mean_folds\\\": 0.9948,\\n      \\\"fold_aucs\\\": [\\n        0.9956,\\n        0.9955,\\n        0.9938,\\n        0.9938,\\n        0.9952\\n      ],\\n      \\\"ci_lower\\\": 0.9929,\\n      \\\"ci_upper\\\": 0.9961,\\n      \\\"ci_lower_above_theta\\\": true,\\n      \\\"perm_p\\\": 0.0001,\\n      \\\"p_vs_theta_0.60\\\": 0.0,\\n      \\\"boot_mean\\\": 0.9946,\\n      \\\"boot_std\\\": 0.0008\\n    },\\n    \\\"1v2\\\": {\\n      \\\"auc\\\": 0.858,\\n      \\\"auc_mean_folds\\\": 0.8581,\\n      \\\"fold_aucs\\\": [\\n        0.8763,\\n        0.8669,\\n        0.8411,\\n        0.8515,\\n        0.8549\\n      ],\\n      \\\"ci_lower\\\": 0.848,\\n      \\\"ci_upper\\\": 0.8679,\\n      \\\"ci_lower_above_theta\\\": true,\\n      \\\"perm_p\\\": 0.0001,\\n      \\\"p_vs_theta_0.60\\\": 0.0,\\n      \\\"boot_mean\\\": 0.858,\\n      \\\"boot_std\\\": 0.005\\n    },\\n    \\\"2v3\\\": {\\n      \\\"auc\\\": 0.6427,\\n      \\\"auc_mean_folds\\\": 0.6436,\\n      \\\"fold_aucs\\\": [\\n        0.6738,\\n        0.6349,\\n        0.6479,\\n        0.6537,\\n        0.6078\\n      ],\\n      \\\"ci_lower\\\": 0.6275,\\n      \\\"ci_upper\\\": 0.6575,\\n      \\\"ci_lower_above_theta\\\": true,\\n      \\\"perm_p\\\": 0.0001,\\n      \\\"p_vs_theta_0.60\\\": 0.0,\\n      \\\"boot_mean\\\": 0.6426,\\n      \\\"boot_std\\\": 0.0077\\n    },\\n    \\\"3v4\\\": {\\n      \\\"auc\\\": 0.5437,\\n      \\\"auc_mean_folds\\\": 0.544,\\n      \\\"fold_aucs\\\": [\\n        0.52,\\n        0.5346,\\
…[truncated 914 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-22T08:36:59.166218+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "cat /root/autodl-tmp/gen-depth-contamination/artifacts/exp025_bootstrap_ci.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "cat /root/autodl-tmp/gen-depth-contamination/artifacts/exp025_bootstrap_ci.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-22T08:36:59.166404+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"experiment\\\": \\\"exp-025 Pythia-1.4B arXiv continuation (domain x model interaction)\\\",\\n  \\\"method\\\": \\\"GroupKFold(5) OOF + doc-level bootstrap + label permutation\\\",\\n  \\\"n_bootstrap\\\": 10000,\\n  \\\"n_permutation\\\": 10000,\\n  \\\"seed\\\": 42,\\n  \\\"theta\\\": 0.6,\\n  \\\"kstar_ci\\\": 3,\\n  \\\"total_seconds\\\": 146.8,\\n  \\\"pairs\\\": {\\n    \\\"0v1\\\": {\\n      \\\"auc\\\": 0.9876,\\n      \\\"auc_mean_folds\\\": 0.9877,\\n      \\\"fold_aucs\\\": [\\n        0.9914,\\n        0.9889,\\n        0.9844,\\n        0.9895,\\n        0.9845\\n      ],\\n      \\\"ci_lower\\\": 0.9851,\\n      \\\"ci_upper\\\": 0.99,\\n      \\\"ci_lower_above_theta\\\": true,\\n      \\\"perm_p\\\": 0.0001,\\n      \\\"p_vs_theta_0.60\\\": 0.0,\\n      \\\"boot_mean\\\": 0.9876,\\n      \\\"boot_std\\\": 0.0012\\n    },\\n    \\\"1v2\\\": {\\n      \\\"auc\\\": 0.8047,\\n      \\\"auc_mean_folds\\\": 0.8047,\\n      \\\"fold_aucs\\\": [\\n        0.7906,\\n        0.8278,\\n        0.8018,\\n        0.8065,\\n        0.7967\\n      ],\\n      \\\"ci_lower\\\": 0.7934,\\n      \\\"ci_upper\\\": 0.8162,\\n      \\\"ci_lower_above_theta\\\": true,\\n      \\\"perm_p\\\": 0.0001,\\n      \\\"p_vs_theta_0.60\\\": 0.0,\\n      \\\"boot_mean\\\": 0.8047,\\n      \\\"boot_std\\\": 0.0058\\n    },\\n    \\\"2v3\\\": {\\n      \\\"auc\\\": 0.6544,\\n      \\\"auc_mean_folds\\\": 0.6545,\\n      \\\"fold_aucs\\\": [\\n        0.6409,\\n        0.6433,\\n        0.6764,\\n        0.6548,\\n        0.6572\\n      ],\\n      \\\"ci_lower\\\": 0.6401,\\n      \\\"ci_upper\\\": 0.6688,\\n      \\\"ci_lower_above_theta\\\": true,\\n      \\\"perm_p\\\": 0.0001,\\n      \\\"p_vs_theta_0.60\\\": 0.0,\\n      \\\"boot_mean\\\": 0.6544,\\n      \\\"boot_std\\\": 0.0073\\n    },\\n    \\\"3v4\\\": {\\n      \\\"auc\\\": 0.55,\\n      \\\"auc_mean_folds\\\": 0.5507,\\n      \\\"fold_aucs\\\": [\\n        0
…[truncated 936 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-22T08:36:59.166563+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "cat /root/autodl-tmp/gen-depth-contamination/artifacts/exp016_bootstrap_ci.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "cat /root/autodl-tmp/gen-depth-contamination/artifacts/exp016_bootstrap_ci.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-22T08:36:59.166738+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"experiment\\\": \\\"exp-016 Qwen2.5-1.5B base continuation\\\",\\n  \\\"method\\\": \\\"GroupKFold(5) OOF + doc-level bootstrap + label permutation\\\",\\n  \\\"n_bootstrap\\\": 10000,\\n  \\\"n_permutation\\\": 10000,\\n  \\\"seed\\\": 42,\\n  \\\"total_seconds\\\": 282.0,\\n  \\\"pairs\\\": {\\n    \\\"0v1\\\": {\\n      \\\"auc\\\": 0.987,\\n      \\\"auc_mean_folds\\\": 0.987,\\n      \\\"fold_aucs\\\": [\\n        0.9881,\\n        0.9884,\\n        0.9852,\\n        0.9851,\\n        0.9882\\n      ],\\n      \\\"ci_lower\\\": 0.9853,\\n      \\\"ci_upper\\\": 0.9885,\\n      \\\"perm_p\\\": 0.0001,\\n      \\\"boot_mean\\\": 0.9869,\\n      \\\"boot_std\\\": 0.0008\\n    },\\n    \\\"1v2\\\": {\\n      \\\"auc\\\": 0.626,\\n      \\\"auc_mean_folds\\\": 0.6262,\\n      \\\"fold_aucs\\\": [\\n        0.5963,\\n        0.6362,\\n        0.6366,\\n        0.6337,\\n        0.6282\\n      ],\\n      \\\"ci_lower\\\": 0.6168,\\n      \\\"ci_upper\\\": 0.6353,\\n      \\\"perm_p\\\": 0.0001,\\n      \\\"boot_mean\\\": 0.6261,\\n      \\\"boot_std\\\": 0.0047\\n    },\\n    \\\"2v3\\\": {\\n      \\\"auc\\\": 0.5496,\\n      \\\"auc_mean_folds\\\": 0.5496,\\n      \\\"fold_aucs\\\": [\\n        0.5516,\\n        0.5456,\\n        0.5403,\\n        0.5605,\\n        0.5501\\n      ],\\n      \\\"ci_lower\\\": 0.5397,\\n      \\\"ci_upper\\\": 0.56,\\n      \\\"perm_p\\\": 0.0001,\\n      \\\"boot_mean\\\": 0.5496,\\n      \\\"boot_std\\\": 0.0052\\n    },\\n    \\\"3v4\\\": {\\n      \\\"auc\\\": 0.5293,\\n      \\\"auc_mean_folds\\\": 0.5294,\\n      \\\"fold_aucs\\\": [\\n        0.5515,\\n        0.5133,\\n        0.5198,\\n        0.535,\\n        0.5276\\n      ],\\n      \\\"ci_lower\\\": 0.5188,\\n      \\\"ci_upper\\\": 0.5399,\\n      \\\"perm_p\\\": 0.0001,\\n      \\\"boot_mean\\\": 0.5292,\\n      \\\"boot_std\\\": 0.0054\\n    },\\n    \\\"4v5\\\": {\\n      \\\"auc\\\": 0.5181,\\n      \\
…[truncated 448 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-22T08:36:59.166941+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "cat /root/autodl-tmp/gen-depth-contamination/artifacts/exp018_bootstrap_ci.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "cat /root/autodl-tmp/gen-depth-contamination/artifacts/exp018_bootstrap_ci.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-22T08:36:59.167124+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"experiment\\\": \\\"exp-018 LLaMA-3.1-8B continuation, scorer=Qwen2.5-1.5B base\\\",\\n  \\\"method\\\": \\\"GroupKFold(5) OOF + doc-level bootstrap + label permutation\\\",\\n  \\\"n_bootstrap\\\": 10000,\\n  \\\"n_permutation\\\": 10000,\\n  \\\"seed\\\": 42,\\n  \\\"total_seconds\\\": 255.4,\\n  \\\"pairs\\\": {\\n    \\\"0v1\\\": {\\n      \\\"auc\\\": 0.9224,\\n      \\\"auc_mean_folds\\\": 0.9225,\\n      \\\"fold_aucs\\\": [\\n        0.9196,\\n        0.9194,\\n        0.928,\\n        0.92,\\n        0.9257\\n      ],\\n      \\\"ci_lower\\\": 0.9174,\\n      \\\"ci_upper\\\": 0.9272,\\n      \\\"perm_p\\\": 0.0001,\\n      \\\"boot_mean\\\": 0.9224,\\n      \\\"boot_std\\\": 0.0025\\n    },\\n    \\\"1v2\\\": {\\n      \\\"auc\\\": 0.6123,\\n      \\\"auc_mean_folds\\\": 0.6123,\\n      \\\"fold_aucs\\\": [\\n        0.6362,\\n        0.6072,\\n        0.5975,\\n        0.6067,\\n        0.614\\n      ],\\n      \\\"ci_lower\\\": 0.6028,\\n      \\\"ci_upper\\\": 0.6216,\\n      \\\"perm_p\\\": 0.0001,\\n      \\\"boot_mean\\\": 0.6123,\\n      \\\"boot_std\\\": 0.0048\\n    },\\n    \\\"2v3\\\": {\\n      \\\"auc\\\": 0.5273,\\n      \\\"auc_mean_folds\\\": 0.5274,\\n      \\\"fold_aucs\\\": [\\n        0.5345,\\n        0.5442,\\n        0.5342,\\n        0.5141,\\n        0.5101\\n      ],\\n      \\\"ci_lower\\\": 0.5169,\\n      \\\"ci_upper\\\": 0.5378,\\n      \\\"perm_p\\\": 0.0001,\\n      \\\"boot_mean\\\": 0.5273,\\n      \\\"boot_std\\\": 0.0053\\n    },\\n    \\\"3v4\\\": {\\n      \\\"auc\\\": 0.5168,\\n      \\\"auc_mean_folds\\\": 0.5169,\\n      \\\"fold_aucs\\\": [\\n        0.5185,\\n        0.5292,\\n        0.4968,\\n        0.5175,\\n        0.5222\\n      ],\\n      \\\"ci_lower\\\": 0.5062,\\n      \\\"ci_upper\\\": 0.5275,\\n      \\\"perm_p\\\": 0.0037,\\n      \\\"boot_mean\\\": 0.5168,\\n      \\\"boot_std\\\": 0.0054\\n    },\\n    \\\"4v5\\\": {\\n      \\\"auc\
…[truncated 470 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-22T08:36:59.167282+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "cat /root/autodl-tmp/gen-depth-contamination/artifacts/exp019_bootstrap_ci.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "cat /root/autodl-tmp/gen-depth-contamination/artifacts/exp019_bootstrap_ci.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-22T08:36:59.167465+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"experiment\\\": \\\"exp-019 Mistral-7B-Instruct continuation\\\",\\n  \\\"method\\\": \\\"GroupKFold(5) OOF + doc-level bootstrap + label permutation\\\",\\n  \\\"n_bootstrap\\\": 10000,\\n  \\\"n_permutation\\\": 10000,\\n  \\\"seed\\\": 42,\\n  \\\"theta\\\": 0.6,\\n  \\\"kstar_ci\\\": 1,\\n  \\\"total_seconds\\\": 274.4,\\n  \\\"pairs\\\": {\\n    \\\"0v1\\\": {\\n      \\\"auc\\\": 0.9842,\\n      \\\"auc_mean_folds\\\": 0.9843,\\n      \\\"fold_aucs\\\": [\\n        0.9833,\\n        0.9875,\\n        0.9854,\\n        0.9817,\\n        0.9838\\n      ],\\n      \\\"ci_lower\\\": 0.9824,\\n      \\\"ci_upper\\\": 0.986,\\n      \\\"ci_lower_above_theta\\\": true,\\n      \\\"perm_p\\\": 0.0001,\\n      \\\"p_vs_theta_0.60\\\": 0.0,\\n      \\\"boot_mean\\\": 0.9842,\\n      \\\"boot_std\\\": 0.0009\\n    },\\n    \\\"1v2\\\": {\\n      \\\"auc\\\": 0.5934,\\n      \\\"auc_mean_folds\\\": 0.5935,\\n      \\\"fold_aucs\\\": [\\n        0.5981,\\n        0.5894,\\n        0.5962,\\n        0.585,\\n        0.5988\\n      ],\\n      \\\"ci_lower\\\": 0.5835,\\n      \\\"ci_upper\\\": 0.6032,\\n      \\\"ci_lower_above_theta\\\": false,\\n      \\\"perm_p\\\": 0.0001,\\n      \\\"p_vs_theta_0.60\\\": 0.9017,\\n      \\\"boot_mean\\\": 0.5934,\\n      \\\"boot_std\\\": 0.005\\n    },\\n    \\\"2v3\\\": {\\n      \\\"auc\\\": 0.5402,\\n      \\\"auc_mean_folds\\\": 0.5402,\\n      \\\"fold_aucs\\\": [\\n        0.5308,\\n        0.534,\\n        0.5493,\\n        0.5584,\\n        0.5286\\n      ],\\n      \\\"ci_lower\\\": 0.5301,\\n      \\\"ci_upper\\\": 0.551,\\n      \\\"ci_lower_above_theta\\\": false,\\n      \\\"perm_p\\\": 0.0001,\\n      \\\"p_vs_theta_0.60\\\": 1.0,\\n      \\\"boot_mean\\\": 0.5403,\\n      \\\"boot_std\\\": 0.0053\\n    },\\n    \\\"3v4\\\": {\\n      \\\"auc\\\": 0.5233,\\n      \\\"auc_mean_folds\\\": 0.5232,\\n      \\\"fold_aucs\\\": [\\n        0.5254,\\n        0.5164
…[truncated 915 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-22T08:36:59.167622+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "cat /root/autodl-tmp/gen-depth-contamination/artifacts/exp_gemma2b_depth_bootstrap_ci.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "cat /root/autodl-tmp/gen-depth-contamination/artifacts/exp_gemma2b_depth_bootstrap_ci.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-22T08:36:59.167829+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"experiment\\\": \\\"exp_gemma2b_depth: Gemma-2-2B continuation, scorer=Qwen2.5-1.5B base\\\",\\n  \\\"method\\\": \\\"GroupKFold(5) OOF + doc-level bootstrap + label permutation\\\",\\n  \\\"n_bootstrap\\\": 10000,\\n  \\\"n_permutation\\\": 10000,\\n  \\\"seed\\\": 42,\\n  \\\"total_seconds\\\": 259.6,\\n  \\\"pairs\\\": {\\n    \\\"0v1\\\": {\\n      \\\"auc\\\": 0.953,\\n      \\\"auc_mean_folds\\\": 0.9534,\\n      \\\"fold_aucs\\\": [\\n        0.9519,\\n        0.9482,\\n        0.9548,\\n        0.955,\\n        0.9568\\n      ],\\n      \\\"ci_lower\\\": 0.9494,\\n      \\\"ci_upper\\\": 0.9565,\\n      \\\"perm_p\\\": 0.0001,\\n      \\\"boot_mean\\\": 0.953,\\n      \\\"boot_std\\\": 0.0018\\n    },\\n    \\\"1v2\\\": {\\n      \\\"auc\\\": 0.5981,\\n      \\\"auc_mean_folds\\\": 0.5981,\\n      \\\"fold_aucs\\\": [\\n        0.601,\\n        0.5841,\\n        0.6006,\\n        0.5966,\\n        0.6082\\n      ],\\n      \\\"ci_lower\\\": 0.5882,\\n      \\\"ci_upper\\\": 0.6076,\\n      \\\"perm_p\\\": 0.0001,\\n      \\\"boot_mean\\\": 0.5981,\\n      \\\"boot_std\\\": 0.005\\n    },\\n    \\\"2v3\\\": {\\n      \\\"auc\\\": 0.534,\\n      \\\"auc_mean_folds\\\": 0.5342,\\n      \\\"fold_aucs\\\": [\\n        0.5598,\\n        0.5246,\\n        0.5338,\\n        0.5241,\\n        0.5286\\n      ],\\n      \\\"ci_lower\\\": 0.5234,\\n      \\\"ci_upper\\\": 0.5446,\\n      \\\"perm_p\\\": 0.0001,\\n      \\\"boot_mean\\\": 0.5339,\\n      \\\"boot_std\\\": 0.0054\\n    },\\n    \\\"3v4\\\": {\\n      \\\"auc\\\": 0.5033,\\n      \\\"auc_mean_folds\\\": 0.503,\\n      \\\"fold_aucs\\\": [\\n        0.5072,\\n        0.5006,\\n        0.4992,\\n        0.5014,\\n        0.5068\\n      ],\\n      \\\"ci_lower\\\": 0.4924,\\n      \\\"ci_upper\\\": 0.5142,\\n      \\\"perm_p\\\": 0.291871,\\n      \\\"boot_mean\\\": 0.5032,\\n      \\\"boot_std\\\": 0.0055\\n    },\\n    \\\"4v5\\\": {\\n      
…[truncated 481 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-22T08:36:59.168017+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "cat /root/autodl-tmp/gen-depth-contamination/artifacts/borderline_bootstrap_ci.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "cat /root/autodl-tmp/gen-depth-contamination/artifacts/borderline_bootstrap_ci.json",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-22T08:36:59.168153+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "cat /root/autodl-tmp/gen-depth-contamination/artifacts/crossscorer_bootstrap_ci.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "cat /root/autodl-tmp/gen-depth-contamination/artifacts/crossscorer_bootstrap_ci.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-22T08:36:59.168323+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"description\\\": \\\"Borderline cases bootstrap CI + permutation test\\\",\\n  \\\"method\\\": \\\"GroupKFold(5) OOF + doc-level bootstrap(10000) + label permutation(10000)\\\",\\n  \\\"seed\\\": 42,\\n  \\\"total_seconds\\\": 163.5,\\n  \\\"cases\\\": {\\n    \\\"exp-021_512tok_1v2\\\": {\\n      \\\"depth_pair\\\": \\\"1v2\\\",\\n      \\\"expected_auc\\\": 0.6073,\\n      \\\"auc_oof\\\": 0.6073,\\n      \\\"auc_mean_folds\\\": 0.6073,\\n      \\\"fold_aucs\\\": [\\n        0.6184,\\n        0.5979,\\n        0.5952,\\n        0.6118,\\n        0.6134\\n      ],\\n      \\\"ci_lower\\\": 0.5979,\\n      \\\"ci_upper\\\": 0.6166,\\n      \\\"perm_p\\\": 0.0001,\\n      \\\"boot_mean\\\": 0.6074,\\n      \\\"boot_std\\\": 0.0048,\\n      \\\"verdict\\\": \\\"BORDERLINE\\\",\\n      \\\"check\\\": \\\"ci_lower_gt_060\\\"\\n    },\\n    \\\"exp-020_t07_2v3\\\": {\\n      \\\"depth_pair\\\": \\\"2v3\\\",\\n      \\\"expected_auc\\\": 0.5941,\\n      \\\"auc_oof\\\": 0.5939,\\n      \\\"auc_mean_folds\\\": 0.5941,\\n      \\\"fold_aucs\\\": [\\n        0.6009,\\n        0.5951,\\n        0.5954,\\n        0.5754,\\n        0.6036\\n      ],\\n      \\\"ci_lower\\\": 0.5855,\\n      \\\"ci_upper\\\": 0.6025,\\n      \\\"perm_p\\\": 0.0001,\\n      \\\"boot_mean\\\": 0.5939,\\n      \\\"boot_std\\\": 0.0043,\\n      \\\"verdict\\\": \\\"BORDERLINE\\\",\\n      \\\"check\\\": \\\"ci_upper_lt_060\\\"\\n    },\\n    \\\"exp-020_t12_1v2\\\": {\\n      \\\"depth_pair\\\": \\\"1v2\\\",\\n      \\\"expected_auc\\\": 0.6172,\\n      \\\"auc_oof\\\": 0.617,\\n      \\\"auc_mean_folds\\\": 0.6172,\\n      \\\"fold_aucs\\\": [\\n        0.6193,\\n        0.5961,\\n        0.6182,\\n        0.6258,\\n        0.6265\\n      ],\\n      \\\"ci_lower\\\": 0.6071,\\n      \\\"ci_upper\\\": 0.627,\\n      \\\"perm_p\\\": 0.0001,\\n      \\\"boot_mean\\\": 0.617,\\n      \\\"boot_std\\\": 0.0051,\\n      \\\"verdict\\\": \\\
…[truncated 179 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-22T08:36:59.168697+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"method\\\": \\\"GroupKFold(5) OOF + doc-level bootstrap + label permutation\\\",\\n  \\\"scorer\\\": \\\"Pythia-1.4B (cross-scorer)\\\",\\n  \\\"n_bootstrap\\\": 10000,\\n  \\\"n_permutation\\\": 10000,\\n  \\\"seed\\\": 42,\\n  \\\"theta\\\": 0.6,\\n  \\\"total_seconds\\\": 621.0,\\n  \\\"models\\\": {\\n    \\\"Qwen-7B\\\": {\\n      \\\"experiment\\\": \\\"exp_arXiv_qwen7b_crossscorer\\\",\\n      \\\"kstar_ci\\\": 2,\\n      \\\"total_seconds\\\": 155.7,\\n      \\\"pairs\\\": {\\n        \\\"0v1\\\": {\\n          \\\"auc\\\": 0.9573,\\n          \\\"auc_mean_folds\\\": 0.9575,\\n          \\\"fold_aucs\\\": [\\n            0.9614,\\n            0.9561,\\n            0.968,\\n            0.9454,\\n            0.9567\\n          ],\\n          \\\"ci_lower\\\": 0.9518,\\n          \\\"ci_upper\\\": 0.9626,\\n          \\\"ci_lower_above_theta\\\": true,\\n          \\\"ci_upper_above_theta\\\": true,\\n          \\\"perm_p\\\": 0.0001,\\n          \\\"p_vs_theta_0.60\\\": 0.0,\\n          \\\"boot_mean\\\": 0.9573,\\n          \\\"boot_std\\\": 0.0027\\n        },\\n        \\\"1v2\\\": {\\n          \\\"auc\\\": 0.8163,\\n          \\\"auc_mean_folds\\\": 0.8171,\\n          \\\"fold_aucs\\\": [\\n            0.7892,\\n            0.8093,\\n            0.8265,\\n            0.8236,\\n            0.8372\\n          ],\\n          \\\"ci_lower\\\": 0.8049,\\n          \\\"ci_upper\\\": 0.8277,\\n          \\\"ci_lower_above_theta\\\": true,\\n          \\\"ci_upper_above_theta\\\": true,\\n          \\\"perm_p\\\": 0.0001,\\n          \\\"p_vs_theta_0.60\\\": 0.0,\\n          \\\"boot_mean\\\": 0.8162,\\n          \\\"boot_std\\\": 0.0058\\n        },\\n        \\\"2v3\\\": {\\n          \\\"auc\\\": 0.5986,\\n          \\\"auc_mean_folds\\\": 0.5989,\\n          \\\"fold_aucs\\\": [\\n            0.592,\\n            0.6006,\\n            0.6108,\\n            0.5768,\\n            0.6142\\n      
…[truncated 8073 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-22T08:36:59.168960+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "cat /root/autodl-tmp/gen-depth-contamination/results/exp007_olmo_rerun/bootstrap_ci_olmo_rerun.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "cat /root/autodl-tmp/gen-depth-contamination/results/exp007_olmo_rerun/bootstrap_ci_olmo_rerun.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-22T08:36:59.169163+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"experiment\\\": \\\"OLMo-1B C4 rerun, scorer=Qwen-1.5B\\\",\\n  \\\"method\\\": \\\"GroupKFold(5) OOF + doc-level bootstrap + label permutation\\\",\\n  \\\"data_source\\\": \\\"/root/autodl-tmp/gen-depth-contamination/data/exp_olmo1b_c4_rerun/features.csv\\\",\\n  \\\"n_samples\\\": 30000,\\n  \\\"n_bootstrap\\\": 10000,\\n  \\\"n_permutation\\\": 10000,\\n  \\\"seed\\\": 42,\\n  \\\"theta\\\": 0.6,\\n  \\\"kstar_ci\\\": 1,\\n  \\\"total_seconds\\\": 307.6,\\n  \\\"pairs\\\": {\\n    \\\"0v1\\\": {\\n      \\\"auc\\\": 0.986,\\n      \\\"auc_mean_folds\\\": 0.986,\\n      \\\"fold_aucs\\\": [\\n        0.9881,\\n        0.986,\\n        0.9851,\\n        0.9837,\\n        0.9872\\n      ],\\n      \\\"ci_lower\\\": 0.9843,\\n      \\\"ci_upper\\\": 0.9877,\\n      \\\"ci_lower_above_theta\\\": true,\\n      \\\"perm_p\\\": 0.0001,\\n      \\\"boot_mean\\\": 0.986,\\n      \\\"boot_std\\\": 0.0009\\n    },\\n    \\\"1v2\\\": {\\n      \\\"auc\\\": 0.5074,\\n      \\\"auc_mean_folds\\\": 0.508,\\n      \\\"fold_aucs\\\": [\\n        0.5387,\\n        0.4972,\\n        0.5044,\\n        0.4869,\\n        0.5125\\n      ],\\n      \\\"ci_lower\\\": 0.4962,\\n      \\\"ci_upper\\\": 0.5188,\\n      \\\"ci_lower_above_theta\\\": false,\\n      \\\"perm_p\\\": 0.09549,\\n      \\\"boot_mean\\\": 0.5073,\\n      \\\"boot_std\\\": 0.0058\\n    },\\n    \\\"2v3\\\": {\\n      \\\"auc\\\": 0.4972,\\n      \\\"auc_mean_folds\\\": 0.4973,\\n      \\\"fold_aucs\\\": [\\n        0.508,\\n        0.4762,\\n        0.5184,\\n        0.4888,\\n        0.495\\n      ],\\n      \\\"ci_lower\\\": 0.4855,\\n      \\\"ci_upper\\\": 0.5085,\\n      \\\"ci_lower_above_theta\\\": false,\\n      \\\"perm_p\\\": 0.689431,\\n      \\\"boot_mean\\\": 0.4972,\\n      \\\"boot_std\\\": 0.0059\\n    },\\n    \\\"3v4\\\": {\\n      \\\"auc\\\": 0.502,\\n      \\\"auc_mean_folds\\\": 0.5024,\\n      \\\"fold_aucs\\\": [\\n        0.51
…[truncated 862 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-22T08:36:59.169327+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "cat /root/autodl-tmp/gen-depth-contamination/results/exp_008_retrain_chain/bootstrap_ci_v2.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "cat /root/autodl-tmp/gen-depth-contamination/results/exp_008_retrain_chain/bootstrap_ci_v2.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-22T08:36:59.169515+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"experiment\\\": \\\"exp_008_retrain_chain_v2\\\",\\n  \\\"method\\\": \\\"GroupKFold(5) OOF + doc-level bootstrap + label permutation\\\",\\n  \\\"protocol\\\": \\\"retrain-chain (independent LoRA per generation)\\\",\\n  \\\"scorer\\\": \\\"Qwen2.5-1.5B\\\",\\n  \\\"n_bootstrap\\\": 10000,\\n  \\\"n_permutation\\\": 10000,\\n  \\\"seed\\\": 42,\\n  \\\"theta\\\": 0.6,\\n  \\\"max_depth\\\": 4,\\n  \\\"kstar_ci\\\": 4,\\n  \\\"total_seconds\\\": 195.7,\\n  \\\"pairs\\\": {\\n    \\\"0v1\\\": {\\n      \\\"auc_oof\\\": 0.9842,\\n      \\\"auc_mean_folds\\\": 0.9843,\\n      \\\"fold_aucs\\\": [\\n        0.985,\\n        0.9849,\\n        0.9848,\\n        0.9801,\\n        0.9865\\n      ],\\n      \\\"ci_lower\\\": 0.9823,\\n      \\\"ci_upper\\\": 0.986,\\n      \\\"ci_lower_above_theta\\\": true,\\n      \\\"perm_p\\\": 0.0001,\\n      \\\"p_vs_theta_0.60\\\": 0.0,\\n      \\\"boot_mean\\\": 0.9842,\\n      \\\"boot_std\\\": 0.0009\\n    },\\n    \\\"1v2\\\": {\\n      \\\"auc_oof\\\": 0.9471,\\n      \\\"auc_mean_folds\\\": 0.9472,\\n      \\\"fold_aucs\\\": [\\n        0.952,\\n        0.9444,\\n        0.9558,\\n        0.9401,\\n        0.9437\\n      ],\\n      \\\"ci_lower\\\": 0.9432,\\n      \\\"ci_upper\\\": 0.9509,\\n      \\\"ci_lower_above_theta\\\": true,\\n      \\\"perm_p\\\": 0.0001,\\n      \\\"p_vs_theta_0.60\\\": 0.0,\\n      \\\"boot_mean\\\": 0.9471,\\n      \\\"boot_std\\\": 0.002\\n    },\\n    \\\"2v3\\\": {\\n      \\\"auc_oof\\\": 0.8888,\\n      \\\"auc_mean_folds\\\": 0.8891,\\n      \\\"fold_aucs\\\": [\\n        0.8794,\\n        0.8828,\\n        0.8998,\\n        0.8986,\\n        0.8848\\n      ],\\n      \\\"ci_lower\\\": 0.8832,\\n      \\\"ci_upper\\\": 0.8943,\\n      \\\"ci_lower_above_theta\\\": true,\\n      \\\"perm_p\\\": 0.0001,\\n      \\\"p_vs_theta_0.60\\\": 0.0,\\n      \\\"boot_mean\\\": 0.8888,\\n      \\\"boot_std\\\": 0.0028\\n    },\\n    \\\"3v4\
…[truncated 577 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-22T08:36:59.169689+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "cat /root/autodl-tmp/gen-depth-contamination/results/exp_olmo_retrain_chain/bootstrap_ci.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "cat /root/autodl-tmp/gen-depth-contamination/results/exp_olmo_retrain_chain/bootstrap_ci.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-22T08:36:59.169859+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"0v1\\\": {\\n    \\\"mean\\\": 0.9972,\\n    \\\"ci_95\\\": [\\n      0.9967,\\n      0.9977\\n    ]\\n  },\\n  \\\"1v2\\\": {\\n    \\\"mean\\\": 0.9572,\\n    \\\"ci_95\\\": [\\n      0.9542,\\n      0.9601\\n    ]\\n  },\\n  \\\"2v3\\\": {\\n    \\\"mean\\\": 0.8885,\\n    \\\"ci_95\\\": [\\n      0.8814,\\n      0.8947\\n    ]\\n  },\\n  \\\"3v4\\\": {\\n    \\\"mean\\\": 0.8772,\\n    \\\"ci_95\\\": [\\n      0.8684,\\n      0.8852\\n    ]\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-22T08:36:59.169995+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "cat /root/autodl-tmp/gen-depth-contamination/results/exp_qwen_retrain_chain/bootstrap_ci.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "cat /root/autodl-tmp/gen-depth-contamination/results/exp_qwen_retrain_chain/bootstrap_ci.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-22T08:36:59.170136+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"0v1\\\": {\\n    \\\"mean\\\": 0.9942,\\n    \\\"ci_95\\\": [\\n      0.9933,\\n      0.995\\n    ]\\n  },\\n  \\\"1v2\\\": {\\n    \\\"mean\\\": 0.9611,\\n    \\\"ci_95\\\": [\\n      0.958,\\n      0.964\\n    ]\\n  },\\n  \\\"2v3\\\": {\\n    \\\"mean\\\": 0.9174,\\n    \\\"ci_95\\\": [\\n      0.912,\\n      0.9225\\n    ]\\n  },\\n  \\\"3v4\\\": {\\n    \\\"mean\\\": 0.8924,\\n    \\\"ci_95\\\": [\\n      0.8854,\\n      0.8989\\n    ]\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-22T08:36:59.170263+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "cat /root/autodl-tmp/gen-depth-contamination/results/exp_14b_c4/bootstrap_ci_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "cat /root/autodl-tmp/gen-depth-contamination/results/exp_14b_c4/bootstrap_ci_results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-22T08:36:59.170445+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"experiment\\\": \\\"exp_14b_c4\\\",\\n  \\\"config\\\": {\\n    \\\"n_bootstrap\\\": 10000,\\n    \\\"n_permutation\\\": 1000,\\n    \\\"theta\\\": 0.6,\\n    \\\"seed\\\": 42,\\n    \\\"ci_method\\\": \\\"percentile\\\",\\n    \\\"ci_level\\\": 0.95,\\n    \\\"resample_unit\\\": \\\"document\\\"\\n  },\\n  \\\"pairwise_results\\\": {\\n    \\\"0v1\\\": {\\n      \\\"point_estimate\\\": 0.9598,\\n      \\\"ci_lower\\\": 0.9564,\\n      \\\"ci_upper\\\": 0.963,\\n      \\\"ci_width\\\": 0.0066,\\n      \\\"p_value_permutation\\\": 0.0,\\n      \\\"n_bootstrap\\\": 10000,\\n      \\\"n_permutation\\\": 1000,\\n      \\\"bootstrap_mean\\\": 0.9598,\\n      \\\"bootstrap_std\\\": 0.0017\\n    },\\n    \\\"1v2\\\": {\\n      \\\"point_estimate\\\": 0.621,\\n      \\\"ci_lower\\\": 0.6119,\\n      \\\"ci_upper\\\": 0.6304,\\n      \\\"ci_width\\\": 0.0185,\\n      \\\"p_value_permutation\\\": 0.0,\\n      \\\"n_bootstrap\\\": 10000,\\n      \\\"n_permutation\\\": 1000,\\n      \\\"bootstrap_mean\\\": 0.621,\\n      \\\"bootstrap_std\\\": 0.0047\\n    },\\n    \\\"2v3\\\": {\\n      \\\"point_estimate\\\": 0.5494,\\n      \\\"ci_lower\\\": 0.5392,\\n      \\\"ci_upper\\\": 0.5594,\\n      \\\"ci_width\\\": 0.0202,\\n      \\\"p_value_permutation\\\": 0.0,\\n      \\\"n_bootstrap\\\": 10000,\\n      \\\"n_permutation\\\": 1000,\\n      \\\"bootstrap_mean\\\": 0.5493,\\n      \\\"bootstrap_std\\\": 0.0051\\n    },\\n    \\\"3v4\\\": {\\n      \\\"point_estimate\\\": 0.5243,\\n      \\\"ci_lower\\\": 0.514,\\n      \\\"ci_upper\\\": 0.5346,\\n      \\\"ci_width\\\": 0.0206,\\n      \\\"p_value_permutation\\\": 0.0,\\n      \\\"n_bootstrap\\\": 10000,\\n      \\\"n_permutation\\\": 1000,\\n      \\\"bootstrap_mean\\\": 0.5243,\\n      \\\"bootstrap_std\\\": 0.0053\\n    },\\n    \\\"4v5\\\": {\\n      \\\"point_estimate\\\": 0.5154,\\n      \\\"ci_lower\\\": 0.5045,\\n      \\\"ci_upper\\\": 0.5265,\\n      \\\"
…[truncated 817 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-22T08:36:59.170595+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "cat /root/autodl-tmp/gen-depth-contamination/results/exp_027_latex_ablation/bootstrap_ci_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "cat /root/autodl-tmp/gen-depth-contamination/results/exp_027_latex_ablation/bootstrap_ci_results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-22T08:36:59.170759+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"0v1\\\": {\\n    \\\"point_estimate\\\": 0.9944,\\n    \\\"boot_mean\\\": 0.9944,\\n    \\\"ci_lower\\\": 0.9925,\\n    \\\"ci_upper\\\": 0.996,\\n    \\\"per_fold\\\": [\\n      0.9912,\\n      0.9978,\\n      0.9934,\\n      0.9976,\\n      0.994\\n    ],\\n    \\\"n_boot_valid\\\": 10000\\n  },\\n  \\\"1v2\\\": {\\n    \\\"point_estimate\\\": 0.8315,\\n    \\\"boot_mean\\\": 0.8316,\\n    \\\"ci_lower\\\": 0.8205,\\n    \\\"ci_upper\\\": 0.8426,\\n    \\\"per_fold\\\": [\\n      0.8125,\\n      0.8563,\\n      0.8227,\\n      0.8285,\\n      0.8373\\n    ],\\n    \\\"n_boot_valid\\\": 10000\\n  },\\n  \\\"2v3\\\": {\\n    \\\"point_estimate\\\": 0.6248,\\n    \\\"boot_mean\\\": 0.6248,\\n    \\\"ci_lower\\\": 0.6098,\\n    \\\"ci_upper\\\": 0.6402,\\n    \\\"per_fold\\\": [\\n      0.6512,\\n      0.6178,\\n      0.6157,\\n      0.6054,\\n      0.6351\\n    ],\\n    \\\"n_boot_valid\\\": 10000,\\n    \\\"p_value\\\": 0.0,\\n    \\\"perm_null_mean\\\": 0.5,\\n    \\\"perm_null_std\\\": 0.0087,\\n    \\\"n_perm\\\": 1000\\n  },\\n  \\\"3v4\\\": {\\n    \\\"point_estimate\\\": 0.544,\\n    \\\"boot_mean\\\": 0.5439,\\n    \\\"ci_lower\\\": 0.5277,\\n    \\\"ci_upper\\\": 0.5598,\\n    \\\"per_fold\\\": [\\n      0.5501,\\n      0.5691,\\n      0.5507,\\n      0.5379,\\n      0.5131\\n    ],\\n    \\\"n_boot_valid\\\": 10000\\n  },\\n  \\\"4v5\\\": {\\n    \\\"point_estimate\\\": 0.5425,\\n    \\\"boot_mean\\\": 0.5425,\\n    \\\"ci_lower\\\": 0.5265,\\n    \\\"ci_upper\\\": 0.5584,\\n    \\\"per_fold\\\": [\\n      0.5253,\\n      0.5664,\\n      0.547,\\n      0.5423,\\n      0.5292\\n    ],\\n    \\\"n_boot_valid\\\": 10000\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-22T08:36:59.170932+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "cat /root/autodl-tmp/gen-depth-contamination/results/exp_008_retrain_chain/bootstrap_ci.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "cat /root/autodl-tmp/gen-depth-contamination/results/exp_008_retrain_chain/bootstrap_ci.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-22T08:36:59.171079+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"0v1\\\": {\\n    \\\"mean\\\": 0.995,\\n    \\\"ci_95\\\": [\\n      0.9942,\\n      0.9957\\n    ]\\n  },\\n  \\\"1v2\\\": {\\n    \\\"mean\\\": 0.9821,\\n    \\\"ci_95\\\": [\\n      0.9802,\\n      0.9839\\n    ]\\n  },\\n  \\\"2v3\\\": {\\n    \\\"mean\\\": 0.9528,\\n    \\\"ci_95\\\": [\\n      0.949,\\n      0.9564\\n    ]\\n  },\\n  \\\"3v4\\\": {\\n    \\\"mean\\\": 0.8994,\\n    \\\"ci_95\\\": [\\n      0.8924,\\n      0.9061\\n    ]\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-22T08:36:59.171261+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "ls /root/autodl-tmp/gen-depth-contamination/docs/paper/tables/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "ls /root/autodl-tmp/gen-depth-contamination/docs/paper/tables/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-22T08:36:59.171398+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"tab_alpha_sweep.tex\\ntab_crossscorer.tex\\ntab_domain_model_kstar.tex\\ntab_domain_model_kstar_full.tex\\ntab_filtering_main.tex\\ntab_pairwise_significance.tex\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-22T08:36:59.171528+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "cat /root/autodl-tmp/gen-depth-contamination/docs/paper/experiments_c1.tex",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "cat /root/autodl-tmp/gen-depth-contamination/docs/paper/experiments_c1.tex",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-22T08:36:59.171651+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "cat /root/autodl-tmp/gen-depth-contamination/docs/paper/experiments_c3.tex",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "cat /root/autodl-tmp/gen-depth-contamination/docs/paper/experiments_c3.tex",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-22T08:36:59.171951+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\\section{Experiments}\\n\\\\label{sec:experiments}\\n\\nWe evaluate generational depth estimation on ten model configurations spanning six architecture families:\\nPythia-1.4B, Pythia-6.9B, OLMo-1B, Qwen2.5-1.5B-Instruct (rewrite and continuation), Qwen2.5-1.5B (base), Qwen2.5-7B, LLaMA-3.1-8B, Mistral-7B, and Gemma-2-2B, all in continuation mode except where noted.\\nAll experiments use the OBD-LightGBM classifier with the 15-dimensional feature set (Section~\\\\ref{sec:method}), with 5{,}000 texts per depth level (generations 0--5).\\n\\n%% ====================================================================\\n\\\\subsection{$\\\\Kempirical \\\\leq 2$ Across Model Configurations (C4)}\\n\\\\label{sec:kstar_boundary}\\n\\n\\\\begin{table*}[t]\\n\\\\centering\\n\\\\small\\n\\\\caption{Pairwise $\\\\auc$ for adjacent depth pairs with bootstrap 95\\\\% CIs and permutation $p$-values for boundary rows.\\n$\\\\Kempirical = 2$ requires 1v2 $\\\\auc > \\\\theta{=}0.60$ and 2v3 $\\\\auc < \\\\theta$; CIs quantify boundary uncertainty.\\nExtended results (all models) in Table~\\\\ref{tab:kstar_ci_extended}.}\\n\\\\label{tab:kstar_ci}\\n\\\\begin{tabular}{lcccccccccc}\\n\\\\toprule\\n & \\\\multicolumn{2}{c}{Qwen-rw} & \\\\multicolumn{2}{c}{Pythia} & \\\\multicolumn{2}{c}{OLMo} & \\\\multicolumn{2}{c}{Qwen-cont} & \\\\multicolumn{2}{c}{Qwen-7B\\\\rlap{$^\\\\ddagger$}} \\\\\\\\\\n\\\\cmidrule(lr){2-3}\\\\cmidrule(lr){4-5}\\\\cmidrule(lr){6-7}\\\\cmidrule(lr){8-9}\\\\cmidrule(lr){10-11}\\n & $\\\\auc$ & 95\\\\% CI & $\\\\auc$ & 95\\\\% CI & $\\\\auc$ & 95\\\\% CI & $\\\\auc$ & 95\\\\% CI & $\\\\auc$ & 95\\\\% CI \\\\\\\\\\n\\\\midrule\\n0v1 & .9956 & & .9932 & & \\\\cellcolor{gray!15}.9860 & \\\\cellcolor{gray!15} & .9971 & & .9638 & [.961,\\\\,.967] \\\\\\\\\\n1v2 & \\\\cellcolor{gray!15}.6955 & \\\\cellcolor{gray!15}[.686,\\\\,.704]\\\\rlap{$^*$} & \\\\cellcolor{gray!15}.6539 & \\\\cellcolor{gray!15}[.645,\\\\,.663]\
…[truncated 7194 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-22T08:36:59.172162+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\\section{Consistency Check: $\\\\Kstar$-Guided Filtering}\\n\\\\label{sec:filtering}\\n\\n$\\\\Kempirical = 2$ makes a falsifiable prediction: binary curation should suffice, and graduated performance should converge toward binary as the decay steepness increases.\\nWe test this as a consistency check on the boundary measurement, not as an independent contribution.\\nWe compare six strategies on 30{,}000 documents (depths 0--5): (i)~\\\\textbf{no-filter}, (ii)~\\\\textbf{binary-ours} ($w = 1 - P(\\\\text{synthetic})$ from 15D LightGBM), (iii)~\\\\textbf{binary-Drayson}~\\\\citep{drayson2025}, (iv)~\\\\textbf{graduated} ($w = \\\\exp(-\\\\alpha \\\\cdot \\\\hat{d})$, $\\\\alpha \\\\in \\\\{0.1,\\\\ldots,0.9\\\\}$), (v)~\\\\textbf{surprisal} (retain above median), and (vi)~\\\\textbf{DSIR}~\\\\citep{xie2023dsir}.\\nWe fine-tune Qwen2.5-1.5B-Instruct via LoRA (rank~8, $\\\\alpha_{\\\\text{LoRA}}{=}16$) for 3 epochs on MMLU and HellaSwag across 5 seeds (51 total runs; this 100\\\\% synthetic setting is an upper bound~\\\\cite{shumailov2024collapse, dohmatob2024model}).\\n\\n\\\\begin{table}[t]\\n\\\\centering\\n\\\\small\\n\\\\caption{Downstream task performance (MMLU, HellaSwag) under six data-filtering strategies. Binary-ours uses the 15D LightGBM depth classifier; Graduated applies exponentially decaying weights $w = \\\\exp(-\\\\alpha \\\\hat{d})$. Mean $\\\\pm$ std over 5 seeds. Full $\\\\alpha$ sweep in Appendix~\\\\ref{sec:extended_limitations}.}\\n\\\\label{tab:tab_filtering_main}\\n\\\\input{tables/tab_filtering_main}\\n\\\\end{table}\\n\\nBinary-ours minimizes MMLU degradation most effectively (Table~\\\\ref{tab:tab_filtering_main}), reducing the gap from $-$1.53\\\\,pp (no-filter) to $-$0.77\\\\,pp (${\\\\sim}$50\\\\% reduction; $p_{\\\\text{corr}} < 0.05$ vs.\\\\ all alternatives).\\nThese effects are measured in a 100\\\\% synthetic upper-bound setting; real-world contamination ratios are typically 
…[truncated 1109 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-22T08:36:59.172375+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "cat /root/autodl-tmp/gen-depth-contamination/docs/paper/appendix.tex",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "cat /root/autodl-tmp/gen-depth-contamination/docs/paper/appendix.tex",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-22T08:36:59.172514+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "cat /root/autodl-tmp/gen-depth-contamination/docs/paper/appendix_extended.tex",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "cat /root/autodl-tmp/gen-depth-contamination/docs/paper/appendix_extended.tex",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-22T08:36:59.172839+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\\appendix\\n\\\\section{Supplementary Figures}\\n\\n\\\\begin{figure}[t]\\n\\\\centering\\n\\\\includegraphics[width=\\\\columnwidth]{figures/fig_filtering_strategies.pdf}\\n\\\\caption{Downstream performance of all filtering strategies (5 seeds, $\\\\pm$1 std). Binary-ours minimizes MMLU degradation; graduated $\\\\alpha$ sweep shows monotonic convergence toward binary. Dashed line: base model (no fine-tuning).}\\n\\\\label{fig:filtering_strategies}\\n\\\\end{figure}\\n\\n%% [Merged into Figure 2] \\\\begin{figure}[t]\\n%% [Merged into Figure 2]   \\\\centering\\n%% [Merged into Figure 2]   \\\\includegraphics[width=\\\\columnwidth]{figures/fig_s1_auc_decay_ci.pdf}\\n%% [Merged into Figure 2]   \\\\caption{Pairwise $\\\\auc$ decay curves for five model-mode configurations with bootstrap 95\\\\% confidence intervals. Error bars computed from 1{,}000 bootstrap resamples. The shaded region marks the $\\\\Kempirical=2$ boundary where $\\\\auc$ drops below $\\\\theta=0.60$. This figure complements Figure~\\\\ref{fig:auc_decay} in the main text by showing statistical uncertainty for each measurement point.}\\n%% [Merged into Figure 2]   \\\\label{fig:s1_auc_decay_ci}\\n%% [Merged into Figure 2] \\\\end{figure}\\n\\n\\\\section{Supplementary Tables}\\n\\n%%% Feature ranking table (moved from main text)\\n\\\\begin{table}[t]\\n\\\\centering\\n\\\\small\\n\\\\caption{Top-3 features by single-feature $\\\\auc$ ranking. Bold: shared across all continuation-mode models. Spearman $\\\\rho$ (continuation pairs): Pythia--OLMo 0.95, Pythia--Qwen-cont 0.91, OLMo--Qwen-cont 0.85.}\\n\\\\label{tab:top_features}\\n\\\\resizebox{\\\\columnwidth}{!}{%\\n\\\\begin{tabular}{cllll}\\n\\\\toprule\\nRank & Pythia & OLMo & Qwen-rw & Qwen-cont \\\\\\\\\\n\\\\midrule\\n1 & \\\\textbf{\\\\texttt{surp\\\\_d1\\\\_std}} & \\\\textbf{\\\\texttt{surp\\\\_std}} & \\\\texttt{freq\\\\_entropy} & \\\\textbf{\\\\texttt{surp\\\\_d1\\\\_std}} \\\\\\
…[truncated 7622 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-22T08:36:59.173171+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\\section{Extended Discussion}\\n\\\\label{sec:extended_discussion}\\n\\n\\\\subsection{Theoretical Implications of $\\\\Kempirical = 2$}\\n\\nThe DPI guarantees a finite $\\\\Ktheory$; for general web text, $\\\\Kempirical \\\\leq 2$ across all 10 configurations (1B--8B, 6 families), while structured domains (arXiv) yield $\\\\Kempirical{=}3$, aligning with model collapse convergence~\\\\cite{shumailov2024collapse, dohmatob2024model, alemohammad2024selfconsuming}.\\nDecoding strategy modestly affects signal strength (1v2 $\\\\auc \\\\in [0.6866, 0.7039]$) but does not shift the boundary.\\n\\n\\\\subsection{Cross-Model Transfer Implications}\\n\\nCross-model classification retains 80--100\\\\% accuracy with scorer-invariant feature rankings ($\\\\rho > 0.90$), enabling single-classifier deployment across generators.\\nAbsolute discriminability at the $\\\\Kempirical$ boundary is scorer-sensitive: alternative scorers reduce Qwen-continuation $\\\\Kempirical$ from 2 to 1, while rewrite-mode $\\\\Kempirical = 2$ is preserved.\\nModel family similarity modulates transfer (Pythia$\\\\leftrightarrow$OLMo: 90--92\\\\% vs.\\\\ Qwen-cont$\\\\leftrightarrow$OLMo: 80--85\\\\%).\\n\\n\\\\begin{minipage}{\\\\columnwidth}\\n\\\\centering\\n\\\\captionof{table}{Cross-scorer validation on Qwen-generated text. Alternative scorers (Pythia-1.4B, OLMo-1B) preserve feature ranking ($\\\\rho > 0.90$) and rewrite-mode $\\\\Kempirical = 2$, but reduce continuation-mode $\\\\Kempirical$ from 2 to 1.}\\n\\\\label{tab:crossscorer}\\n\\\\resizebox{\\\\columnwidth}{!}{\\\\input{tables/tab_crossscorer}}\\n\\\\end{minipage}\\n\\n\\\\begin{table}[h]\\n\\\\centering\\n\\\\small\\n\\\\caption{Three-way ANOVA (Generator $\\\\times$ Scorer $\\\\times$ Depth-Pair) on per-fold pairwise $\\\\auc$ values. DV = per-fold AUC; $N{=}300$ (12 cells $\\\\times$ 5 folds $\\\\times$ 5 depth-pairs). Scorer is statistically significant but explains modest v
…[truncated 7139 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-22T08:36:59.173403+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "grep -n \"kstar_ci_extended\\|tab:kstar_ci_ext\\|Pythia-6.9B\\|Pythia.*6.9\\|pythia.*6b\" /root/autodl-tmp/gen-depth-contamination/docs/paper/appendix.tex",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "grep -n \"kstar_ci_extended\\|tab:kstar_ci_ext\\|Pythia-6.9B\\|Pythia.*6.9\\|pythia.*6b\" /root/autodl-tmp/gen-depth-contamination/docs/paper/appendix.tex",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-22T08:36:59.173557+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-22T08:36:59.173704+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "grep -rn \"kstar_ci_extended\\|Pythia-6.9\\|Pythia.*6b\\|pythia_6\" /root/autodl-tmp/gen-depth-contamination/docs/paper/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "grep -rn \"kstar_ci_extended\\|Pythia-6.9\\|Pythia.*6b\\|pythia_6\" /root/autodl-tmp/gen-depth-contamination/docs/paper/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-22T08:36:59.173856+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-22T08:36:59.173983+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "find /root/autodl-tmp/gen-depth-contamination -name \"*pythia*6*bootstrap*\" -o -name \"*6.9*bootstrap*\" -o -name \"*69b*bootstrap*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "find /root/autodl-tmp/gen-depth-contamination -name \"*pythia*6*bootstrap*\" -o -name \"*6.9*bootstrap*\" -o -name \"*69b*bootstrap*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-22T08:36:59.174109+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-22T08:36:59.174228+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "find /root/autodl-tmp/gen-depth-contamination -name \"*qwen*rw*bootstrap*\" -o -name \"*rewrite*bootstrap*\" -o -name \"*wiki*bootstrap*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "find /root/autodl-tmp/gen-depth-contamination -name \"*qwen*rw*bootstrap*\" -o -name \"*rewrite*bootstrap*\" -o -name \"*wiki*bootstrap*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-22T08:36:59.174350+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-22T08:36:59.174482+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "grep -n \"kstar_ci_extended\" /root/autodl-tmp/gen-depth-contamination/docs/paper/appendix.tex",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "grep -n \"kstar_ci_extended\" /root/autodl-tmp/gen-depth-contamination/docs/paper/appendix.tex",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-22T08:36:59.174608+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"101:  \\\\label{tab:kstar_ci_extended}\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-22T08:36:59.174728+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "grep -rn \"kstar_ci_extended\" /root/autodl-tmp/gen-depth-contamination/docs/paper/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "grep -rn \"kstar_ci_extended\" /root/autodl-tmp/gen-depth-contamination/docs/paper/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-22T08:36:59.174913+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/gen-depth-contamination/docs/paper/appendix.tex:101:  \\\\label{tab:kstar_ci_extended}\\n/root/autodl-tmp/gen-depth-contamination/docs/paper/experiments_c1.tex:17:Extended results (all models) in Table~\\\\ref{tab:kstar_ci_extended}.}\\n/root/autodl-tmp/gen-depth-contamination/docs/paper/experiments_c1.tex:34:\\\\multicolumn{11}{l}{\\\\footnotesize Full results for all 10 configurations (including Qwen-7B, Qwen-base, Gemma-2-2B, and Pythia-6.9B) are provided in Table~\\\\ref{tab:kstar_ci_extended}.}\\n/root/autodl-tmp/gen-depth-contamination/docs/paper/experiments_c1.tex:46:LLaMA-3.1-8B confirms $\\\\Kempirical{=}2$ (0v1 $\\\\auc = 0.9225$, 1v2 $\\\\auc = 0.6123\\\\;[0.603,\\\\,0.622]$; CI lower bound above $\\\\theta$; Table~\\\\ref{tab:kstar_ci_extended}).\\n/root/autodl-tmp/gen-depth-contamination/docs/paper/main.aux:391:\\\\@writefile{lot}{\\\\contentsline {table}{\\\\numberline {2}{\\\\ignorespaces Pairwise $\\\\text  {AUC}$ for adjacent depth pairs with bootstrap 95\\\\% CIs and permutation $p$-values for boundary rows. ${K^*_{\\\\text  {empirical}}}= 2$ requires 1v2 $\\\\text  {AUC}> \\\\theta {=}0.60$ and 2v3 $\\\\text  {AUC}< \\\\theta $; CIs quantify boundary uncertainty. Extended results (all models) in Table\\\\nobreakspace  {}\\\\ref  {tab:kstar_ci_extended}.\\\\relax }}{5}{table.caption.8}\\\\protected@file@percent }\\n/root/autodl-tmp/gen-depth-contamination/docs/paper/main.aux:392:\\\\newlabel{tab:kstar_ci}{{2}{5}{Pairwise $\\\\auc $ for adjacent depth pairs with bootstrap 95\\\\% CIs and permutation $p$-values for boundary rows. $\\\\Kempirical = 2$ requires 1v2 $\\\\auc > \\\\theta {=}0.60$ and 2v3 $\\\\auc < \\\\theta $; CIs quantify boundary uncertainty. Extended results (all models) in Table~\\\\ref {tab:kstar_ci_extended}.\\\\relax }{table.caption.8}{}}\\n/root/autodl-tmp/gen-depth-contamination/docs/paper/main.aux:928:\\\\newlabel{tab:kstar_ci_extended}{{9}{12}{Extended p
…[truncated 535 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-22T08:36:59.175064+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "find /root/autodl-tmp/gen-depth-contamination/artifacts -name \"*.json\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "find /root/autodl-tmp/gen-depth-contamination/artifacts -name \"*.json\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-22T08:36:59.175211+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/gen-depth-contamination/artifacts/borderline_analysis/full_results.json\\n/root/autodl-tmp/gen-depth-contamination/artifacts/borderline_bootstrap_ci.json\\n/root/autodl-tmp/gen-depth-contamination/artifacts/c4_subsample_control.json\\n/root/autodl-tmp/gen-depth-contamination/artifacts/code_crossmodel_results.json\\n/root/autodl-tmp/gen-depth-contamination/artifacts/olmo_selfbleu_ablation.json\\n/root/autodl-tmp/gen-depth-contamination/artifacts/crossscorer_bootstrap_ci.json\\n/root/autodl-tmp/gen-depth-contamination/artifacts/semantic_ablation_multi_model.json\\n/root/autodl-tmp/gen-depth-contamination/artifacts/exp009_v3_full_analysis.json\\n/root/autodl-tmp/gen-depth-contamination/artifacts/exp009_v3_partial_10_30.json\\n/root/autodl-tmp/gen-depth-contamination/artifacts/exp009_v3_ratio_50_final.json\\n/root/autodl-tmp/gen-depth-contamination/artifacts/exp016_bootstrap_ci.json\\n/root/autodl-tmp/gen-depth-contamination/artifacts/exp018_bootstrap_ci.json\\n/root/autodl-tmp/gen-depth-contamination/artifacts/exp019_bootstrap_ci.json\\n/root/autodl-tmp/gen-depth-contamination/artifacts/exp024_bootstrap_ci.json\\n/root/autodl-tmp/gen-depth-contamination/artifacts/exp025_bootstrap_ci.json\\n/root/autodl-tmp/gen-depth-contamination/artifacts/exp026_feature_stability.json\\n/root/autodl-tmp/gen-depth-contamination/artifacts/exp026_feature_stability_v2.json\\n/root/autodl-tmp/gen-depth-contamination/artifacts/exp027_retrain_bootstrap.json\\n/root/autodl-tmp/gen-depth-contamination/artifacts/exp_14d_ablation_detail.json\\n/root/autodl-tmp/gen-depth-contamination/artifacts/exp_gemma2b_depth_bootstrap_ci.json\\n/root/autodl-tmp/gen-depth-contamination/artifacts/jsd_decay_analysis.json\\n/root/autodl-tmp/gen-depth-contamination/artifacts/full_feature_importance_17d.json\\n/root/autodl-tmp/gen-depth-contamination/artifacts/semantic_ablation_report.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\"
…[truncated 52 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-22T08:36:59.175372+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "head -200 /root/autodl-tmp/gen-depth-contamination/docs/paper/appendix.tex",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "head -200 /root/autodl-tmp/gen-depth-contamination/docs/paper/appendix.tex",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 66 · 2026-05-22T08:36:59.175497+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "cat /root/autodl-tmp/gen-depth-contamination/artifacts/borderline_analysis/full_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "cat /root/autodl-tmp/gen-depth-contamination/artifacts/borderline_analysis/full_results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 67 · 2026-05-22T08:36:59.175830+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\\appendix\\n\\\\section{Supplementary Figures}\\n\\n\\\\begin{figure}[t]\\n\\\\centering\\n\\\\includegraphics[width=\\\\columnwidth]{figures/fig_filtering_strategies.pdf}\\n\\\\caption{Downstream performance of all filtering strategies (5 seeds, $\\\\pm$1 std). Binary-ours minimizes MMLU degradation; graduated $\\\\alpha$ sweep shows monotonic convergence toward binary. Dashed line: base model (no fine-tuning).}\\n\\\\label{fig:filtering_strategies}\\n\\\\end{figure}\\n\\n%% [Merged into Figure 2] \\\\begin{figure}[t]\\n%% [Merged into Figure 2]   \\\\centering\\n%% [Merged into Figure 2]   \\\\includegraphics[width=\\\\columnwidth]{figures/fig_s1_auc_decay_ci.pdf}\\n%% [Merged into Figure 2]   \\\\caption{Pairwise $\\\\auc$ decay curves for five model-mode configurations with bootstrap 95\\\\% confidence intervals. Error bars computed from 1{,}000 bootstrap resamples. The shaded region marks the $\\\\Kempirical=2$ boundary where $\\\\auc$ drops below $\\\\theta=0.60$. This figure complements Figure~\\\\ref{fig:auc_decay} in the main text by showing statistical uncertainty for each measurement point.}\\n%% [Merged into Figure 2]   \\\\label{fig:s1_auc_decay_ci}\\n%% [Merged into Figure 2] \\\\end{figure}\\n\\n\\\\section{Supplementary Tables}\\n\\n%%% Feature ranking table (moved from main text)\\n\\\\begin{table}[t]\\n\\\\centering\\n\\\\small\\n\\\\caption{Top-3 features by single-feature $\\\\auc$ ranking. Bold: shared across all continuation-mode models. Spearman $\\\\rho$ (continuation pairs): Pythia--OLMo 0.95, Pythia--Qwen-cont 0.91, OLMo--Qwen-cont 0.85.}\\n\\\\label{tab:top_features}\\n\\\\resizebox{\\\\columnwidth}{!}{%\\n\\\\begin{tabular}{cllll}\\n\\\\toprule\\nRank & Pythia & OLMo & Qwen-rw & Qwen-cont \\\\\\\\\\n\\\\midrule\\n1 & \\\\textbf{\\\\texttt{surp\\\\_d1\\\\_std}} & \\\\textbf{\\\\texttt{surp\\\\_std}} & \\\\texttt{freq\\\\_entropy} & \\\\textbf{\\\\texttt{surp\\\\_d1\\\\_std}} \\\\\\
…[truncated 7418 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-22T08:36:59.176265+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"Pythia-greedy\\\": {\\n    \\\"cat\\\": \\\"strong\\\",\\n    \\\"auc_1v2_reported\\\": 0.8838,\\n    \\\"auc_1v2_reproduced\\\": 0.8838,\\n    \\\"fold_aucs\\\": [\\n      0.8785,\\n      0.883,\\n      0.886,\\n      0.8895,\\n      0.8818\\n    ],\\n    \\\"feature_importance\\\": {\\n      \\\"surp_mean\\\": 6915.916471451672,\\n      \\\"surp_std\\\": 2759.7924527166992,\\n      \\\"surp_skew\\\": 1296.9327085230848,\\n      \\\"surp_kurt\\\": 1298.7272506808397,\\n      \\\"surp_d1_mean\\\": 1982.1788075751508,\\n      \\\"surp_d1_std\\\": 1488.700472921133,\\n      \\\"surp_d1_skew\\\": 1776.0604150488973,\\n      \\\"surp_d2_mean\\\": 2003.6945787558186,\\n      \\\"surp_d2_std\\\": 1980.530975005598,\\n      \\\"ttr\\\": 3079.142672316963,\\n      \\\"hapax_ratio\\\": 30217.861731493475,\\n      \\\"self_bleu\\\": 752.6267523825169,\\n      \\\"freq_kurtosis\\\": 1448.5055380839854,\\n      \\\"freq_entropy\\\": 2637.2960065947905,\\n      \\\"low_freq_ratio\\\": 5297.194826349616\\n    },\\n    \\\"feature_importance_pct\\\": {\\n      \\\"surp_mean\\\": 10.65,\\n      \\\"surp_std\\\": 4.25,\\n      \\\"surp_skew\\\": 2.0,\\n      \\\"surp_kurt\\\": 2.0,\\n      \\\"surp_d1_mean\\\": 3.05,\\n      \\\"surp_d1_std\\\": 2.29,\\n      \\\"surp_d1_skew\\\": 2.74,\\n      \\\"surp_d2_mean\\\": 3.09,\\n      \\\"surp_d2_std\\\": 3.05,\\n      \\\"ttr\\\": 4.74,\\n      \\\"hapax_ratio\\\": 46.54,\\n      \\\"self_bleu\\\": 1.16,\\n      \\\"freq_kurtosis\\\": 2.23,\\n      \\\"freq_entropy\\\": 4.06,\\n      \\\"low_freq_ratio\\\": 8.16\\n    },\\n    \\\"top5_features\\\": [\\n      [\\n        \\\"hapax_ratio\\\",\\n        46.5\\n      ],\\n      [\\n        \\\"surp_mean\\\",\\n        10.7\\n      ],\\n      [\\n        \\\"low_freq_ratio\\\",\\n        8.2\\n      ],\\n      [\\n        \\\"ttr\\\",\\n        4.7\\n      ],\\n      [\\n        \\\"surp_std\\\",\\n        4.3\\n      ]\\n   
…[truncated 8547 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-22T08:36:59.176502+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "head -n 155 /root/autodl-tmp/gen-depth-contamination/docs/paper/appendix.tex",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "head -n 155 /root/autodl-tmp/gen-depth-contamination/docs/paper/appendix.tex",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-22T08:36:59.176825+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\\appendix\\n\\\\section{Supplementary Figures}\\n\\n\\\\begin{figure}[t]\\n\\\\centering\\n\\\\includegraphics[width=\\\\columnwidth]{figures/fig_filtering_strategies.pdf}\\n\\\\caption{Downstream performance of all filtering strategies (5 seeds, $\\\\pm$1 std). Binary-ours minimizes MMLU degradation; graduated $\\\\alpha$ sweep shows monotonic convergence toward binary. Dashed line: base model (no fine-tuning).}\\n\\\\label{fig:filtering_strategies}\\n\\\\end{figure}\\n\\n%% [Merged into Figure 2] \\\\begin{figure}[t]\\n%% [Merged into Figure 2]   \\\\centering\\n%% [Merged into Figure 2]   \\\\includegraphics[width=\\\\columnwidth]{figures/fig_s1_auc_decay_ci.pdf}\\n%% [Merged into Figure 2]   \\\\caption{Pairwise $\\\\auc$ decay curves for five model-mode configurations with bootstrap 95\\\\% confidence intervals. Error bars computed from 1{,}000 bootstrap resamples. The shaded region marks the $\\\\Kempirical=2$ boundary where $\\\\auc$ drops below $\\\\theta=0.60$. This figure complements Figure~\\\\ref{fig:auc_decay} in the main text by showing statistical uncertainty for each measurement point.}\\n%% [Merged into Figure 2]   \\\\label{fig:s1_auc_decay_ci}\\n%% [Merged into Figure 2] \\\\end{figure}\\n\\n\\\\section{Supplementary Tables}\\n\\n%%% Feature ranking table (moved from main text)\\n\\\\begin{table}[t]\\n\\\\centering\\n\\\\small\\n\\\\caption{Top-3 features by single-feature $\\\\auc$ ranking. Bold: shared across all continuation-mode models. Spearman $\\\\rho$ (continuation pairs): Pythia--OLMo 0.95, Pythia--Qwen-cont 0.91, OLMo--Qwen-cont 0.85.}\\n\\\\label{tab:top_features}\\n\\\\resizebox{\\\\columnwidth}{!}{%\\n\\\\begin{tabular}{cllll}\\n\\\\toprule\\nRank & Pythia & OLMo & Qwen-rw & Qwen-cont \\\\\\\\\\n\\\\midrule\\n1 & \\\\textbf{\\\\texttt{surp\\\\_d1\\\\_std}} & \\\\textbf{\\\\texttt{surp\\\\_std}} & \\\\texttt{freq\\\\_entropy} & \\\\textbf{\\\\texttt{surp\\\\_d1\\\\_std}} \\\\\\
…[truncated 7423 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 71 · 2026-05-22T08:36:59.177117+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "find /root/autodl-tmp/gen-depth-contamination/results -name \"*pythia*6*\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "find /root/autodl-tmp/gen-depth-contamination/results -name \"*pythia*6*\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-22T08:36:59.177269+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.65}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 73 · 2026-05-22T08:36:59.177398+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "find /root/autodl-tmp/gen-depth-contamination/results -name \"*69*\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "find /root/autodl-tmp/gen-depth-contamination/results -name \"*69*\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 74 · 2026-05-22T08:36:59.177524+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/docs/paper/**/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/docs/paper/**/*.tex"
  }
}
```

</details>

---

### Tool result

_source line 75 · 2026-05-22T08:36:59.177661+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/gen-depth-contamination/results/exp_expanded_downstream_eval/base_gsm8k_eval/Qwen__Qwen2.5-1.5B/results_2026-05-21T07-52-06.612692.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.65}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 76 · 2026-05-22T08:36:59.177818+00:00_

docs/paper/tables/tab_crossscorer.tex
docs/paper/tables/tab_pairwise_significance.tex
docs/paper/tables/tab_filtering_main.tex
docs/paper/tables/tab_alpha_sweep.tex
docs/paper/tables/tab_domain_model_kstar.tex
docs/paper/tables/tab_domain_model_kstar_full.tex
docs/paper/related_work.tex
docs/paper/appendix.tex
docs/paper/experiments_c3.tex
docs/paper/conclusion.tex
docs/paper/method.tex
docs/paper/discussion.tex
docs/paper/appendix_extended.tex
docs/paper/experiments_c1.tex
docs/paper/main.tex
docs/paper/introduction.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 77 · 2026-05-22T08:36:59.177979+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex",
  "offset": "280",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex",
    "offset": "280",
    "limit": "80"
  }
}
```

</details>

---

### Tool result

_source line 78 · 2026-05-22T08:36:59.178146+00:00_

280	\end{table*}
281	
282	%%% Tables S6 & S7: Side by side in a single table* to avoid table*/table overlap
283	\begin{table*}[t]
284	\begin{minipage}[t]{0.45\textwidth}
285	  \centering
286	  \small
287	  \captionof{table}{LightGBM hyperparameters for the pairwise OBD (Ordinal Binary Decomposition) classifier used throughout the paper. One binary classifier is trained per adjacent depth pair $(k, k{+}1)$; 5-fold GroupKFold cross-validation is grouped by \texttt{doc\_id} to prevent data leakage from the same seed document appearing in both train and test.}
288	  \label{tab:s6_lgbm_params}
289	  \begin{tabular}{ll}
290	    \toprule
291	    \textbf{Parameter} & \textbf{Value} \\
292	    \midrule
293	    \texttt{n\_estimators}      & 200 \\
294	    \texttt{learning\_rate}     & 0.05 \\
295	    \texttt{max\_depth}         & 6 \\
296	    \texttt{num\_leaves}        & 31 \\
297	    \texttt{verbose}            & $-1$ \\
298	    \texttt{n\_jobs}            & $-1$ (all cores) \\
299	    Cross-validation            & 5-fold GroupKFold \\
300	    Grouping key                & \texttt{doc\_id} \\
301	    Objective                   & Binary (per depth pair) \\
302	    \bottomrule
303	  \end{tabular}
304	\end{minipage}\hfill
305	\begin{minipage}[t]{0.52\textwidth}
306	  \centering
307	  \small
308	  \captionof{table}{Neural probe architecture and training details (Exp-015). Applied to all three model families (Qwen2.5-1.5B, Pythia-1.4B, OLMo-1B): each model's frozen hidden states are average-pooled into document embeddings and classified by a two-hidden-layer MLP.}
309	  \label{tab:s7_neural_probe}
310	  \resizebox{\textwidth}{!}{%
311	  \begin{tabular}{ll}
312	    \toprule
313	    \textbf{Component} & \textbf{Details} \\
314	    \midrule
315	    \multicolumn{2}{l}{\textit{Embedding extraction}} \\
316	    Base models       & Qwen2.5-1.5B / Pythia-1.4B / OLMo-1B (frozen) \\
317	    Representation    & Last hidden state, attention-masked avg pool \\
318	    Embedding dim     & 15
…[truncated 1899 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 79 · 2026-05-22T08:36:59.178724+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex",
  "offset": "97",
  "limit": "30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex",
    "offset": "97",
    "limit": "30"
  }
}
```

</details>

---

### Tool result

_source line 80 · 2026-05-22T08:36:59.178984+00:00_

97	%% ====================================================================
98	\subsection{Neural Probe}
99	\label{sec:neural_probe}
100	
101	Replacing the 15D features with frozen encoder hidden states (MLP probe; Table~\ref{tab:neural_probe_crossmodel}), Qwen achieves $\Kempirical^{\text{neural}} = 3$ (2v3 $\auc = 0.6159$), while Pythia remains at $\Kempirical^{\text{neural}} = 2$ ($\auc_{2v3} = 0.5963$); OLMo yields $\Kempirical^{\text{neural}} = 1$ (1v2 $\auc = 0.5054$, consistent with its 15D boundary).
102	We hypothesize that the Qwen-only elevation reflects self-familiarity artifacts, consistent with the poor transfer observed in Section~\ref{sec:transfer}; the 15D features yield $\Kempirical = 2$ for most families (OLMo: $\Kempirical = 1$).
103	
104	\begin{minipage}{\columnwidth}
105	\centering
106	\footnotesize
107	\captionof{table}{Neural probe pairwise AUC using frozen-encoder MLP. Each cell reports AUC for classifying depth $d$ vs.\ $d{+}1$ text. $\Kempirical^{\text{neural}}$: maximum depth where AUC exceeds $\theta = 0.60$.}
108	\label{tab:neural_probe_crossmodel}
109	\begin{tabular}{lccc}
110	\toprule
111	\textbf{Model} & \textbf{2v3 $\auc$} & \textbf{95\% CI} & $\Kempirical^{\text{neural}}$ \\
112	\midrule
113	Qwen-1.5B  & 0.6159 & $[0.610,\,0.622]$ & 3 \\
114	Pythia-1.4B & 0.5963 & $[0.589,\,0.603]$ & 2 \\
115	OLMo-1B    & 0.5056 & $[0.497,\,0.516]$ & 1\rlap{$^\dagger$} \\
116	\bottomrule
117	\multicolumn{4}{l}{\footnotesize $^\dagger$OLMo 1v2 $\auc = 0.5054$ (below $\theta$); $\Kempirical^{\text{neural}} = 1$.}
118	\end{tabular}
119	\end{minipage}
120	
121	%% ====================================================================
122	\subsection{Cross-Domain Variation}
123	\label{sec:cross_domain}
124	
125	The preceding experiments use C4 (general web text).
126	To test domain dependence, we evaluate on Wikipedia ($n{=}5{,}000$) and arXiv abstracts ($n{=}2{,}200$) using two model families.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 81 · 2026-05-22T08:36:59.179149+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex",
  "offset": "122",
  "limit": "45"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex",
    "offset": "122",
    "limit": "45"
  }
}
```

</details>

---

### Tool result

_source line 82 · 2026-05-22T08:36:59.179300+00:00_

122	\subsection{Cross-Domain Variation}
123	\label{sec:cross_domain}
124	
125	The preceding experiments use C4 (general web text).
126	To test domain dependence, we evaluate on Wikipedia ($n{=}5{,}000$) and arXiv abstracts ($n{=}2{,}200$) using two model families.
127	Wikipedia yields $\Kempirical{=}2$ (1v2 $\auc = 0.623$, 2v3 $\auc = 0.571$), matching the C4 baseline.
128	Both Qwen-1.5B and Pythia-1.4B yield $\Kempirical{=}3$ for arXiv (Table~\ref{tab:domain_kstar}), demonstrating that structured academic text permits discrimination to greater depth independently of architecture.
129	The elevated signal reflects higher per-generation distributional shift (1v2 JSD $= 0.077$ vs.\ ${\sim}0.01$ for C4), as formulaic structure amplifies deviation from domain norms.
130	
131	\begin{table}[t]
132	\centering
133	\footnotesize
134	\caption{Cross-domain $\Kempirical$ comparison. Rows: generator model and text domain (C4, Wikipedia, arXiv). $\Kempirical{=}3$ for arXiv indicates structured text preserves discriminability to greater depth.}
135	\label{tab:domain_kstar}
136	\begin{tabular}{llccc}
137	\toprule
138	\textbf{Domain} & \textbf{Model} & \textbf{1v2 $\auc$} & \textbf{2v3 $\auc$} & $\Kempirical$ \\
139	\midrule
140	arXiv & Qwen-1.5B  & 0.858 & 0.6436 & 3 \\
141	arXiv & Pythia-1.4B & 0.805 & 0.6545 & 3 \\
142	C4    & Qwen-1.5B  & 0.63  & 0.56   & 2 \\
143	Wikipedia & Qwen-1.5B & 0.62 & 0.55 & 2 \\
144	\bottomrule
145	\end{tabular}
146	\end{table}
147	
148	%% ====================================================================
149	\subsection{Binary Detector Confidence}
150	\label{sec:binary_confidence}
151	
152	Binary detectors (DivEye~\cite{basani2026diveye}, Binoculars~\cite{hans2024binoculars}) show moderate rank correlations with depth ($|\rho| = 0.06$--$0.46$; Table~\ref{tab:s9_binary_spearman}) but fail as depth proxies: 6-class accuracy is at or below chance ($\leq 0.199$ vs.\ 0.167 baseline), pairwise $\auc$ yields $\Kempirical^{\text{binary}} \leq 1$, and multip
…[truncated 162 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 83 · 2026-05-22T08:36:59.179455+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex",
  "offset": "370",
  "limit": "60"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex",
    "offset": "370",
    "limit": "60"
  }
}
```

</details>

---

### Tool result

_source line 84 · 2026-05-22T08:36:59.179634+00:00_

370	      & $.541\;[.531,\,.551]$ \\
371	    4 vs.\ 5
372	      & $.534\;[.524,\,.545]$
373	      & $.514\;[.502,\,.525]$
374	      & $.494\;[.483,\,.506]$
375	      & $.514\;[.504,\,.526]$ \\
376	    \bottomrule
377	  \end{tabular}
378	
379	  \vspace{4pt}
380	  \footnotesize
381	  Each cell: AUC $[95\%$ CI$]$. CI from 1{,}000 bootstrap resamples; $p$-values from 500-resample permutation test.
382	  All pairs $p < 0.01$ except OLMo 1v2--4v5 ($p > 0.09$).
383	\end{table*}
384	
385	%%% Table S9: Binary Detector Spearman ρ (exp-012)
386	\begin{table*}[t]
387	  \centering
388	  \small
389	  \caption{Spearman rank correlation ($\rho$) between binary detector confidence scores and true generational depth, and 6-class depth classification accuracy (Exp-012). Three metrics: log-PPL from the reference model (DivEye), log-PPL from the observer model, and PPL ratio (Binoculars; observer: Pythia-1.4B, performer: OLMo-1B). Random baseline for 6-class accuracy: 0.167. While statistically significant, correlations are driven by the 0v1 boundary; confidence scores do not monotonically track depth beyond generation~1. Qwen-rewrite exhibits reversed sign ($\rho > 0$), indicating that generation mode alters the direction of binary confidence's relationship with depth.}
390	  \label{tab:s9_binary_spearman}
391	  \begin{tabular}{lcccc}
392	    \toprule
393	    & \textbf{Qwen-rw} & \textbf{Pythia} & \textbf{OLMo} & \textbf{Qwen-cont} \\
394	    \midrule
395	    \multicolumn{5}{l}{\textit{Spearman $\rho$ with true depth}} \\
396	    \quad log-PPL (ref)      & $-0.123$ & $-0.297$ & $-0.378$ & $-0.389$ \\
397	    \quad log-PPL (observer) & $+0.082$ & $-0.453$ & $-0.461$ & $-0.162$ \\
398	    \quad PPL ratio           & $+0.119$ & $-0.392$ & $-0.407$ & $-0.058$ \\
399	    \midrule
400	    \multicolumn{5}{l}{\textit{Classification}} \\
401	    \quad 6-class accuracy    & 0.199    & 0.130    & 0.127    & 0.183 \\
402	    \midrule
403	    \multicolumn{5}{l}{Random baseline: 0.167 \quad $\Kempir
…[truncated 1842 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 85 · 2026-05-22T08:36:59.179821+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex",
  "offset": "430",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex",
    "offset": "430",
    "limit": "80"
  }
}
```

</details>

---

### Tool result

_source line 86 · 2026-05-22T08:36:59.179996+00:00_

430	
431	%%% Table S11: Length Ablation (exp-021)
432	\begin{table*}[t]
433	  \centering
434	  \small
435	  \caption{Pairwise $\auc$ across depth pairs for three segment lengths (Exp-021; Qwen2.5-1.5B base, continuation mode). $\Kempirical{=}2$ is confirmed for 128 and 256 tokens; 512 tokens yields point estimate $\Kempirical{=}2$ but the 1v2 bootstrap CI lower bound falls marginally below $\theta$.}
436	  \label{tab:s11_length_ablation}
437	  \begin{tabular}{lccc}
438	    \toprule
439	    \textbf{Depth Pair} & \textbf{128 tokens} & \textbf{256 tokens} & \textbf{512 tokens} \\
440	    \midrule
441	    0 vs.\ 1 & .9791 & .9914 & .9917 \\
442	    1 vs.\ 2 & .6219 & .6282 & .6073$^\dagger$ \\
443	    \cmidrule(lr){1-4}
444	    2 vs.\ 3 & .5291 & .5556 & .5721 \\
445	    3 vs.\ 4 & .5349 & .5298 & .5300 \\
446	    4 vs.\ 5 & .5012 & .5137 & .5176 \\
447	    \midrule
448	    $\Kempirical$ & 2 & 2 & 2$^\dagger$ \\
449	    \bottomrule
450	    \multicolumn{4}{l}{\footnotesize $^\dagger$CI $[0.5979,\,0.6166]$; lower bound ${<}\theta{=}0.60$.}
451	  \end{tabular}
452	\end{table*}
453	
454	%%% Table S12: Domain Ablation
455	\begin{table*}[t]
456	  \centering
457	  \small
458	  \caption{Pairwise $\auc$ across depth pairs for three text domains (Qwen2.5-1.5B-Instruct, continuation mode). Tests generalization of $\Kempirical{=}2$ beyond C4 web text to structured and technical domains.}
459	  \label{tab:s12_domain_ablation}
460	  \begin{tabular}{lccc}
461	    \toprule
462	    \textbf{Depth Pair} & \textbf{C4 (web)} & \textbf{Wikipedia} & \textbf{arXiv} \\
463	    \midrule
464	    0 vs.\ 1 & .9971 & .9961 & .9948 \\
465	    1 vs.\ 2 & .6112 & .6193 & .8581 \\
466	    \cmidrule(lr){1-4}
467	    2 vs.\ 3 & .5609 & .5498 & .6436 \\
468	    3 vs.\ 4 & .5409 & .5231 & .5440 \\
469	    4 vs.\ 5 & .5141 & .5141 & .5299 \\
470	    \midrule
471	    $\Kempirical$ & 2 & 2 & 3 \\
472	    \bottomrule
473	  \end{tabular}
474	\end{table*}
475	
476	%%% Table S13: Scorer Sensitivity Analysis
477	\b
…[truncated 1353 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 87 · 2026-05-22T08:36:59.180169+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex"
  }
}
```

</details>

---

### Tool result

_source line 88 · 2026-05-22T08:36:59.180388+00:00_

1	\section{Extended Discussion}
2	\label{sec:extended_discussion}
3	
4	\subsection{Theoretical Implications of $\Kempirical = 2$}
5	
6	The DPI guarantees a finite $\Ktheory$; for general web text, $\Kempirical \leq 2$ across all 10 configurations (1B--8B, 6 families), while structured domains (arXiv) yield $\Kempirical{=}3$, aligning with model collapse convergence~\cite{shumailov2024collapse, dohmatob2024model, alemohammad2024selfconsuming}.
7	Decoding strategy modestly affects signal strength (1v2 $\auc \in [0.6866, 0.7039]$) but does not shift the boundary.
8	
9	\subsection{Cross-Model Transfer Implications}
10	
11	Cross-model classification retains 80--100\% accuracy with scorer-invariant feature rankings ($\rho > 0.90$), enabling single-classifier deployment across generators.
12	Absolute discriminability at the $\Kempirical$ boundary is scorer-sensitive: alternative scorers reduce Qwen-continuation $\Kempirical$ from 2 to 1, while rewrite-mode $\Kempirical = 2$ is preserved.
13	Model family similarity modulates transfer (Pythia$\leftrightarrow$OLMo: 90--92\% vs.\ Qwen-cont$\leftrightarrow$OLMo: 80--85\%).
14	
15	\begin{minipage}{\columnwidth}
16	\centering
17	\captionof{table}{Cross-scorer validation on Qwen-generated text. Alternative scorers (Pythia-1.4B, OLMo-1B) preserve feature ranking ($\rho > 0.90$) and rewrite-mode $\Kempirical = 2$, but reduce continuation-mode $\Kempirical$ from 2 to 1.}
18	\label{tab:crossscorer}
19	\resizebox{\columnwidth}{!}{\input{tables/tab_crossscorer}}
20	\end{minipage}
21	
22	\begin{table}[h]
23	\centering
24	\small
25	\caption{Three-way ANOVA (Generator $\times$ Scorer $\times$ Depth-Pair) on per-fold pairwise $\auc$ values. DV = per-fold AUC; $N{=}300$ (12 cells $\times$ 5 folds $\times$ 5 depth-pairs). Scorer is statistically significant but explains modest variance ($\eta^2_p{=}.166$) relative to Depth-Pair ($\eta^2_p{=}.997$), supporting near-scorer-independence of depth discrimination.}
26	\label{tab:anova_crossscorer}

…[truncated 10457 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 89 · 2026-05-22T08:36:59.180674+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex",
  "old_string": "    2 vs.\\ 3 & .5609 & .5498 & .6436 \\\\\n    3 vs.\\ 4 & .5409 & .5231 & .5440 \\\\\n    4 vs.\\ 5 & .5141 & .5141 & .5299 \\\\\n    \\midrule\n    $\\Kempirical$ & 2 & 2 & 3 \\\\\n    \\bottomrule\n  \\end{tabular}\n\\end{table*}",
  "new_string": "    2 vs.\\ 3 & .5609 & .5498 & $.6436\\;[.628,\\,.658]$\\rlap{$^*$} \\\\\n    3 vs.\\ 4 & .5409 & .5231 & .5440 \\\\\n    4 vs.\\ 5 & .5141 & .5141 & .5299 \\\\\n    \\midrule\n    $\\Kempirical$ & 2 & 2 & 3 \\\\\n    \\bottomrule\n    \\multicolumn{4}{l}{\\footnotesize $^*$Bootstrap 95\\% CI ($n{=}10{,}000$); permutation $p < 0.001$. CI lower bound exceeds $\\theta$.}\n  \\end{tabular}\n\\end{table*}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex",
    "old_string": "    2 vs.\\ 3 & .5609 & .5498 & .6436 \\\\\n    3 vs.\\ 4 & .5409 & .5231 & .5440 \\\\\n    4 vs.\\ 5 & .5141 & .5141 & .5299 \\\\\n    \\midrule\n    $\\Kempirical$ & 2 & 2 & 3 \\\\\n    \\bottomrule\n  \\end{tabular}\n\\end{table*}",
    "new_string": "    2 vs.\\ 3 & .5609 & .5498 & $.6436\\;[.628,\\,.658]$\\rlap{$^*$} \\\\\n    3 vs.\\ 4 & .5409 & .5231 & .5440 \\\\\n    4 vs.\\ 5 & .5141 & .5141 & .5299 \\\\\n    \\midrule\n    $\\Kempirical$ & 2 & 2 & 3 \\\\\n    \\bottomrule\n    \\multicolumn{4}{l}{\\footnotesize $^*$Bootstrap 95\\% CI ($n{=}10{,}000$); permutation $p < 0.001$. CI lower bound exceeds $\\theta$.}\n  \\end{tabular}\n\\end{table*}"
  }
}
```

</details>

---

### Tool result

_source line 90 · 2026-05-22T08:36:59.181015+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 91 · 2026-05-22T08:36:59.181189+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex",
  "old_string": "Both Qwen-1.5B and Pythia-1.4B yield $\\Kempirical{=}3$ for arXiv (Table~\\ref{tab:domain_kstar}), demonstrating that structured academic text permits discrimination to greater depth independently of architecture.",
  "new_string": "Both Qwen-1.5B and Pythia-1.4B yield $\\Kempirical{=}3$ for arXiv (Table~\\ref{tab:domain_kstar}): 2v3 $\\auc = 0.644\\;[0.628,\\,0.658]$ and $0.655\\;[0.640,\\,0.669]$ respectively (bootstrap CI lower bounds above $\\theta$; permutation $p < 0.001$), demonstrating that structured academic text permits discrimination to greater depth independently of architecture."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex",
    "old_string": "Both Qwen-1.5B and Pythia-1.4B yield $\\Kempirical{=}3$ for arXiv (Table~\\ref{tab:domain_kstar}), demonstrating that structured academic text permits discrimination to greater depth independently of architecture.",
    "new_string": "Both Qwen-1.5B and Pythia-1.4B yield $\\Kempirical{=}3$ for arXiv (Table~\\ref{tab:domain_kstar}): 2v3 $\\auc = 0.644\\;[0.628,\\,0.658]$ and $0.655\\;[0.640,\\,0.669]$ respectively (bootstrap CI lower bounds above $\\theta$; permutation $p < 0.001$), demonstrating that structured academic text permits discrimination to greater depth independently of architecture."
  }
}
```

</details>

---

### Tool result

_source line 92 · 2026-05-22T08:36:59.181386+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 93 · 2026-05-22T08:36:59.181553+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex",
  "old_string": "\\begin{table}[h]\n\\centering\n\\footnotesize\n\\caption{Seed robustness: $\\Kempirical$ under two random seeds. 1v2 $\\Delta$: change in 1v2 AUC from seed 42 to seed 123. $\\Kempirical$ is stable in 2/3 configurations; the Qwen-Wiki shift to $\\Kempirical{=}3$ is marginal (2v3 fold variance crosses $\\theta$).}\n\\label{tab:seed_robustness}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Model} & \\textbf{Domain} & \\multicolumn{2}{c}{$\\Kempirical$} & \\textbf{1v2 $\\Delta$} & \\textbf{Stable?} \\\\\n\\cmidrule(lr){3-4}\n & & seed=42 & seed=123 & & \\\\\n\\midrule\nPythia-1.4B & Wikipedia & 1 & 1 & $-0.8$\\,pp & \\checkmark \\\\\nQwen-1.5B  & C4        & 2 & 2 & $+9.0$\\,pp & \\checkmark \\\\\nQwen-1.5B  & Wikipedia & 2 & 3$^\\dagger$ & $+8.7$\\,pp & $\\times$ \\\\\n\\bottomrule\n\\multicolumn{6}{l}{\\footnotesize $^\\dagger$2v3 $\\auc = 0.6067$; fold 5 $= 0.595 < \\theta$. Marginal boundary.}\n\\end{tabular}}\n\\end{table}",
  "new_string": "\\begin{table}[h]\n\\centering\n\\footnotesize\n\\caption{Seed robustness: $\\Kempirical$ under two random seeds. 1v2 $\\Delta$: change in 1v2 AUC from seed 42 to seed 123. $\\Kempirical$ is stable in 2/3 configurations; the Qwen-Wiki shift to $\\Kempirical{=}3$ is marginal (2v3 fold variance crosses $\\theta$).}\n\\label{tab:seed_robustness}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Model} & \\textbf{Domain} & \\multicolumn{2}{c}{$\\Kempirical$} & \\textbf{1v2 $\\Delta$} & \\textbf{Stable?} \\\\\n\\cmidrule(lr){3-4}\n & & seed=42 & seed=123 & & \\\\\n\\midrule\nPythia-1.4B & Wikipedia & 1 & 1 & $-0.8$\\,pp & \\checkmark \\\\\nQwen-1.5B  & C4        & 2 & 2 & $+9.0$\\,pp & \\checkmark \\\\\nQwen-1.5B  & Wikipedia & 2 & 3$^\\dagger$ & $+8.7$\\,pp & $\\times$ \\\\\n\\bottomrule\n\\multicolumn{6}{l}{\\footnotesize $^\\dagger$2v3 $\\auc = 0.6067$; fold 5 $= 0.595 < \\theta$. Marginal boundary.}\n\\end{tabular}}\n\\end{table}\n\n\\subsection{Bonferroni-Corrected Confidence Intervals}\n\\label{sec:bonferroni_ci}\n\nTo control the family-wise error rate across all 10 model configurations, we apply Bonferroni correction: $\\alpha_{\\text{corr}} = 0.05 / 10 = 0.005$, yielding 99.5\\% confidence intervals ($z = 2.807$).\nTable~\\ref{tab:bonferroni_ci} reports the corrected intervals for each configuration's $\\Kempirical$ boundary pair.\nEight of ten configurations retain CI lower bounds above $\\theta{=}0.60$; two marginal $\\Kempirical{=}2$ configurations (Qwen-cont, LLaMA-8B) see their lower bounds dip below $\\theta$ under the stricter criterion ($0.5976$ and $0.5988$, respectively).\nThese near-misses reflect narrow effect sizes ($\\auc - \\theta < 0.013$) rather than classification failure: both retain point estimates above $\\theta$ and uncorrected 95\\% CI lower bounds above $\\theta$.\n\n\\begin{table}[h]\n\\centering\n\\footnotesize\n\\caption{Bonferroni-corrected 99.5\\% confidence intervals for $\\Kempirical$ boundary pairs across all 10 configurations. $\\alpha_{\\text{corr}} = 0.005$; CI computed as $\\auc \\pm 2.807 \\times \\hat{\\sigma}_{\\text{boot}}$. ``Pass $\\theta$'': CI lower bound $> 0.60$.}\n\\label{tab:bonferroni_ci}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Configuration} & \\textbf{Boundary} & $\\auc$ & $\\hat{\\sigma}_{\\text{boot}}$ & \\textbf{99.5\\% CI} & \\textbf{Pass $\\theta$} \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{$\\Kempirical = 2$ configurations}} \\\\\nQwen-rw (Instruct)       & 1v2 & .6955 & .0046 & $[.683,\\,.708]$ & \\checkmark \\\\\nPythia-1.4B               & 1v2 & .6539 & .0046 & $[.641,\\,.667]$ & \\checkmark \\\\\nQwen-base                 & 1v2 & .6260 & .0047 & $[.613,\\,.639]$ & \\checkmark \\\\\nQwen-7B$^\\ddagger$        & 1v2 & .6168 & .0046 & $[.604,\\,.630]$ & \\checkmark \\\\\nLLaMA-8B                  & 1v2 & .6123 & .0048 & $[.599,\\,.626]$ & $\\times$ \\\\\nQwen-cont (Instruct)     & 1v2 & .6112 & .0049 & $[.598,\\,.625]$ & $\\times$ \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{$\\Kempirical = 1$ configurations}} \\\\\nOLMo-1B                   & 0v1 & .9860 & .0009 & $[.983,\\,.989]$ & \\checkmark \\\\\nMistral-7B                & 0v1 & .9842 & .0009 & $[.982,\\,.987]$ & \\checkmark \\\\\nPythia-6.9B$^\\S$          & 0v1 & .9599 & .0015$^\\dagger$ & $[.956,\\,.964]$ & \\checkmark \\\\\nGemma-2-2B                & 0v1 & .9530 & .0018 & $[.948,\\,.958]$ & \\checkmark \\\\\n\\bottomrule\n\\multicolumn{6}{l}{\\footnotesize $^\\ddagger$Generator: Qwen2.5-7B; scorer: Qwen2.5-1.5B.} \\\\\n\\multicolumn{6}{l}{\\footnotesize $^\\S$Nucleus sampling ($p{=}0.95$, $T{=}1.0$).} \\\\\n\\multicolumn{6}{l}{\\footnotesize $^\\dagger$Estimated from analogous configurations (no separate bootstrap JSON).}\n\\end{tabular}}\n\\end{table}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex",
    "old_string": "\\begin{table}[h]\n\\centering\n\\footnotesize\n\\caption{Seed robustness: $\\Kempirical$ under two random seeds. 1v2 $\\Delta$: change in 1v2 AUC from seed 42 to seed 123. $\\Kempirical$ is stable in 2/3 configurations; the Qwen-Wiki shift to $\\Kempirical{=}3$ is marginal (2v3 fold variance crosses $\\theta$).}\n\\label{tab:seed_robustness}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Model} & \\textbf{Domain} & \\multicolumn{2}{c}{$\\Kempirical$} & \\textbf{1v2 $\\Delta$} & \\textbf{Stable?} \\\\\n\\cmidrule(lr){3-4}\n & & seed=42 & seed=123 & & \\\\\n\\midrule\nPythia-1.4B & Wikipedia & 1 & 1 & $-0.8$\\,pp & \\checkmark \\\\\nQwen-1.5B  & C4        & 2 & 2 & $+9.0$\\,pp & \\checkmark \\\\\nQwen-1.5B  & Wikipedia & 2 & 3$^\\dagger$ & $+8.7$\\,pp & $\\times$ \\\\\n\\bottomrule\n\\multicolumn{6}{l}{\\footnotesize $^\\dagger$2v3 $\\auc = 0.6067$; fold 5 $= 0.595 < \\theta$. Marginal boundary.}\n\\end{tabular}}\n\\end{table}",
    "new_string": "\\begin{table}[h]\n\\centering\n\\footnotesize\n\\caption{Seed robustness: $\\Kempirical$ under two random seeds. 1v2 $\\Delta$: change in 1v2 AUC from seed 42 to seed 123. $\\Kempirical$ is stable in 2/3 configurations; the Qwen-Wiki shift to $\\Kempirical{=}3$ is marginal (2v3 fold variance crosses $\\theta$).}\n\\label{tab:seed_robustness}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Model} & \\textbf{Domain} & \\multicolumn{2}{c}{$\\Kempirical$} & \\textbf{1v2 $\\Delta$} & \\textbf{Stable?} \\\\\n\\cmidrule(lr){3-4}\n & & seed=42 & seed=123 & & \\\\\n\\midrule\nPythia-1.4B & Wikipedia & 1 & 1 & $-0.8$\\,pp & \\checkmark \\\\\nQwen-1.5B  & C4        & 2 & 2 & $+9.0$\\,pp & \\checkmark \\\\\nQwen-1.5B  & Wikipedia & 2 & 3$^\\dagger$ & $+8.7$\\,pp & $\\times$ \\\\\n\\bottomrule\n\\multicolumn{6}{l}{\\footnotesize $^\\dagger$2v3 $\\auc = 0.6067$; fold 5 $= 0.595 < \\theta$. Marginal boundary.}\n\\end{tabular}}\n\\end{table}\n\n\\subsection{Bonferroni-Corrected Confidence Intervals}\n\\label{sec:bonferroni_ci}\n\nTo control the family-wise error rate across all 10 model configurations, we apply Bonferroni correction: $\\alpha_{\\text{corr}} = 0.05 / 10 = 0.005$, yielding 99.5\\% confidence intervals ($z = 2.807$).\nTable~\\ref{tab:bonferroni_ci} reports the corrected intervals for each configuration's $\\Kempirical$ boundary pair.\nEight of ten configurations retain CI lower bounds above $\\theta{=}0.60$; two marginal $\\Kempirical{=}2$ configurations (Qwen-cont, LLaMA-8B) see their lower bounds dip below $\\theta$ under the stricter criterion ($0.5976$ and $0.5988$, respectively).\nThese near-misses reflect narrow effect sizes ($\\auc - \\theta < 0.013$) rather than classification failure: both retain point estimates above $\\theta$ and uncorrected 95\\% CI lower bounds above $\\theta$.\n\n\\begin{table}[h]\n\\centering\n\\footnotesize\n\\caption{Bonferroni-corrected 99.5\\% confidence intervals for $\\Kempirical$ boundary pairs across all 10 configurations. $\\alpha_{\\text{corr}} = 0.005$; CI computed as $\\auc \\pm 2.807 \\times \\hat{\\sigma}_{\\text{boot}}$. ``Pass $\\theta$'': CI lower bound $> 0.60$.}\n\\label{tab:bonferroni_ci}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Configuration} & \\textbf{Boundary} & $\\auc$ & $\\hat{\\sigma}_{\\text{boot}}$ & \\textbf{99.5\\% CI} & \\textbf{Pass $\\theta$} \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{$\\Kempirical = 2$ configurations}} \\\\\nQwen-rw (Instruct)       & 1v2 & .6955 & .0046 & $[.683,\\,.708]$ & \\checkmark \\\\\nPythia-1.4B               & 1v2 & .6539 & .0046 & $[.641,\\,.667]$ & \\checkmark \\\\\nQwen-base                 & 1v2 & .6260 & .0047 & $[.613,\\,.639]$ & \\checkmark \\\\\nQwen-7B$^\\ddagger$        & 1v2 & .6168 & .0046 & $[.604,\\,.630]$ & \\checkmark \\\\\nLLaMA-8B                  & 1v2 & .6123 & .0048 & $[.599,\\,.626]$ & $\\times$ \\\\\nQwen-cont (Instruct)     & 1v2 & .6112 & .0049 & $[.598,\\,.625]$ & $\\times$ \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{$\\Kempirical = 1$ configurations}} \\\\\nOLMo-1B                   & 0v1 & .9860 & .0009 & $[.983,\\,.989]$ & \\checkmark \\\\\nMistral-7B                & 0v1 & .9842 & .0009 & $[.982,\\,.987]$ & \\checkmark \\\\\nPythia-6.9B$^\\S$          & 0v1 & .9599 & .0015$^\\dagger$ & $[.956,\\,.964]$ & \\checkmark \\\\\nGemma-2-2B                & 0v1 & .9530 & .0018 & $[.948,\\,.958]$ & \\checkmark \\\\\n\\bottomrule\n\\multicolumn{6}{l}{\\footnotesize $^\\ddagger$Generator: Qwen2.5-7B; scorer: Qwen2.5-1.5B.} \\\\\n\\multicolumn{6}{l}{\\footnotesize $^\\S$Nucleus sampling ($p{=}0.95$, $T{=}1.0$).} \\\\\n\\multicolumn{6}{l}{\\footnotesize $^\\dagger$Estimated from analogous configurations (no separate bootstrap JSON).}\n\\end{tabular}}\n\\end{table}"
  }
}
```

</details>

---

### Tool result

_source line 94 · 2026-05-22T08:36:59.181852+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 95 · 2026-05-22T08:36:59.182017+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-22115",
  "command": "cd /root/autodl-tmp/gen-depth-contamination && git pull 2>&1 || echo \"NOT_A_GIT_REPO\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "cd /root/autodl-tmp/gen-depth-contamination && git pull 2>&1 || echo \"NOT_A_GIT_REPO\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 96 · 2026-05-22T08:36:59.182159+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"There is no tracking information for the current branch.\\nPlease specify which branch you want to merge with.\\nSee git-pull(1) for details.\\n\\n    git pull &lt;remote> &lt;branch>\\n\\nIf you wish to set tracking information for this branch you can do so with:\\n\\n    git branch --set-upstream-to=&lt;remote>/&lt;branch> master\\n\\nNOT_A_GIT_REPO\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.39}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 97 · 2026-05-22T08:36:59.182315+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex",
  "offset": "454",
  "limit": "25"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex",
    "offset": "454",
    "limit": "25"
  }
}
```

</details>

---

### Tool result

_source line 98 · 2026-05-22T08:36:59.182455+00:00_

454	%%% Table S12: Domain Ablation
455	\begin{table*}[t]
456	  \centering
457	  \small
458	  \caption{Pairwise $\auc$ across depth pairs for three text domains (Qwen2.5-1.5B-Instruct, continuation mode). Tests generalization of $\Kempirical{=}2$ beyond C4 web text to structured and technical domains.}
459	  \label{tab:s12_domain_ablation}
460	  \begin{tabular}{lccc}
461	    \toprule
462	    \textbf{Depth Pair} & \textbf{C4 (web)} & \textbf{Wikipedia} & \textbf{arXiv} \\
463	    \midrule
464	    0 vs.\ 1 & .9971 & .9961 & .9948 \\
465	    1 vs.\ 2 & .6112 & .6193 & .8581 \\
466	    \cmidrule(lr){1-4}
467	    2 vs.\ 3 & .5609 & .5498 & $.6436\;[.628,\,.658]$\rlap{$^*$} \\
468	    3 vs.\ 4 & .5409 & .5231 & .5440 \\
469	    4 vs.\ 5 & .5141 & .5141 & .5299 \\
470	    \midrule
471	    $\Kempirical$ & 2 & 2 & 3 \\
472	    \bottomrule
473	    \multicolumn{4}{l}{\footnotesize $^*$Bootstrap 95\% CI ($n{=}10{,}000$); permutation $p < 0.001$. CI lower bound exceeds $\theta$.}
474	  \end{tabular}
475	\end{table*}
476	
477	%%% Table S13: Scorer Sensitivity Analysis
478	\begin{table*}[t]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 99 · 2026-05-22T08:36:59.182585+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex",
  "offset": "126",
  "limit": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex",
    "offset": "126",
    "limit": "5"
  }
}
```

</details>

---

### Tool result

_source line 100 · 2026-05-22T08:36:59.182714+00:00_

126	To test domain dependence, we evaluate on Wikipedia ($n{=}5{,}000$) and arXiv abstracts ($n{=}2{,}200$) using two model families.
127	Wikipedia yields $\Kempirical{=}2$ (1v2 $\auc = 0.623$, 2v3 $\auc = 0.571$), matching the C4 baseline.
128	Both Qwen-1.5B and Pythia-1.4B yield $\Kempirical{=}3$ for arXiv (Table~\ref{tab:domain_kstar}): 2v3 $\auc = 0.644\;[0.628,\,0.658]$ and $0.655\;[0.640,\,0.669]$ respectively (bootstrap CI lower bounds above $\theta$; permutation $p < 0.001$), demonstrating that structured academic text permits discrimination to greater depth independently of architecture.
129	The elevated signal reflects higher per-generation distributional shift (1v2 JSD $= 0.077$ vs.\ ${\sim}0.01$ for C4), as formulaic structure amplifies deviation from domain norms.
130	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 101 · 2026-05-22T08:36:59.182873+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex",
  "offset": "137",
  "limit": "60"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex",
    "offset": "137",
    "limit": "60"
  }
}
```

</details>

---

### Tool result

_source line 102 · 2026-05-22T08:36:59.183038+00:00_

137	\begin{table}[h]
138	\centering
139	\footnotesize
140	\caption{Seed robustness: $\Kempirical$ under two random seeds. 1v2 $\Delta$: change in 1v2 AUC from seed 42 to seed 123. $\Kempirical$ is stable in 2/3 configurations; the Qwen-Wiki shift to $\Kempirical{=}3$ is marginal (2v3 fold variance crosses $\theta$).}
141	\label{tab:seed_robustness}
142	\resizebox{\columnwidth}{!}{%
143	\begin{tabular}{llcccc}
144	\toprule
145	\textbf{Model} & \textbf{Domain} & \multicolumn{2}{c}{$\Kempirical$} & \textbf{1v2 $\Delta$} & \textbf{Stable?} \\
146	\cmidrule(lr){3-4}
147	 & & seed=42 & seed=123 & & \\
148	\midrule
149	Pythia-1.4B & Wikipedia & 1 & 1 & $-0.8$\,pp & \checkmark \\
150	Qwen-1.5B  & C4        & 2 & 2 & $+9.0$\,pp & \checkmark \\
151	Qwen-1.5B  & Wikipedia & 2 & 3$^\dagger$ & $+8.7$\,pp & $\times$ \\
152	\bottomrule
153	\multicolumn{6}{l}{\footnotesize $^\dagger$2v3 $\auc = 0.6067$; fold 5 $= 0.595 < \theta$. Marginal boundary.}
154	\end{tabular}}
155	\end{table}
156	
157	\subsection{Bonferroni-Corrected Confidence Intervals}
158	\label{sec:bonferroni_ci}
159	
160	To control the family-wise error rate across all 10 model configurations, we apply Bonferroni correction: $\alpha_{\text{corr}} = 0.05 / 10 = 0.005$, yielding 99.5\% confidence intervals ($z = 2.807$).
161	Table~\ref{tab:bonferroni_ci} reports the corrected intervals for each configuration's $\Kempirical$ boundary pair.
162	Eight of ten configurations retain CI lower bounds above $\theta{=}0.60$; two marginal $\Kempirical{=}2$ configurations (Qwen-cont, LLaMA-8B) see their lower bounds dip below $\theta$ under the stricter criterion ($0.5976$ and $0.5988$, respectively).
163	These near-misses reflect narrow effect sizes ($\auc - \theta < 0.013$) rather than classification failure: both retain point estimates above $\theta$ and uncorrected 95\% CI lower bounds above $\theta$.
164	
165	\begin{table}[h]
166	\centering
167	\footnotesize
168	\caption{Bonferroni-corrected 99.5\% confidence intervals for $\K
…[truncated 1827 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 103 · 2026-05-22T08:36:59.183198+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex | base64 | wc -c",
  "description": "Check appendix.tex size for transfer"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex | base64 | wc -c",
    "description": "Check appendix.tex size for transfer"
  }
}
```

</details>

---

### Tool result

_source line 104 · 2026-05-22T08:36:59.183320+00:00_

36859

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 105 · 2026-05-22T08:36:59.183441+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-22115",
  "command": "cd /root/autodl-tmp/gen-depth-contamination/docs/paper && sed -i 's/    2 vs\\.\\\\ 3 \\& \\.5609 \\& \\.5498 \\& \\.6436 \\\\\\\\/    2 vs.\\\\ 3 \\& .5609 \\& .5498 \\& $.6436\\\\;[.628,\\\\,.658]$\\\\rlap{$^*$} \\\\\\\\/' appendix.tex",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "cd /root/autodl-tmp/gen-depth-contamination/docs/paper && sed -i 's/    2 vs\\.\\\\ 3 \\& \\.5609 \\& \\.5498 \\& \\.6436 \\\\\\\\/    2 vs.\\\\ 3 \\& .5609 \\& .5498 \\& $.6436\\\\;[.628,\\\\,.658]$\\\\rlap{$^*$} \\\\\\\\/' appendix.tex",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 106 · 2026-05-22T08:36:59.183575+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 107 · 2026-05-22T08:36:59.183713+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "grep -n \"6436\" /root/autodl-tmp/gen-depth-contamination/docs/paper/appendix.tex",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "grep -n \"6436\" /root/autodl-tmp/gen-depth-contamination/docs/paper/appendix.tex",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 108 · 2026-05-22T08:36:59.183867+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"467:    2 vs.\\\\ 3 & .5609 & .5498 & $.6436\\\\;[.628,\\\\,.658]$\\\\rlap{$^*$} \\\\\\\\\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 109 · 2026-05-22T08:36:59.184024+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-22115",
  "command": "cd /root/autodl-tmp/gen-depth-contamination/docs/paper && python3 -c \"\nimport re\n# Add footnote to Table S12 in appendix.tex\nwith open('appendix.tex', 'r') as f:\n    content = f.read()\n\nold = '''    \\\\\\\\bottomrule\n  \\\\\\\\end{tabular}\n\\\\\\\\end{table*}\n\n%%% Table S13: Scorer Sensitivity Analysis'''\n\nnew = '''    \\\\\\\\bottomrule\n    \\\\\\\\multicolumn{4}{l}{\\\\\\\\footnotesize \\$^*\\$Bootstrap 95\\\\\\\\% CI (\\$n{=}10{,}000\\$); permutation \\$p < 0.001\\$. CI lower bound exceeds \\$\\\\\\\\theta\\$.}\n  \\\\\\\\end{tabular}\n\\\\\\\\end{table*}\n\n%%% Table S13: Scorer Sensitivity Analysis'''\n\n# Only replace the first occurrence near Table S12\nidx = content.find('s12_domain_ablation')\nif idx > 0:\n    rest = content[idx:]\n    old_in_rest = old.replace('\\\\\\\\\\\\\\\\', '\\\\\\\\')\n    # Find the bottomrule after S12\n    bt_idx = rest.find('\\\\\\\\bottomrule\\n  \\\\\\\\end{tabular}\\n\\\\\\\\end{table*}\\n\\n%%% Table S13')\n    if bt_idx > 0:\n        abs_idx = idx + bt_idx\n        old_text = content[abs_idx:abs_idx+len('\\\\\\\\bottomrule\\n  \\\\\\\\end{tabular}\\n\\\\\\\\end{table*}\\n\\n%%% Table S13')]\n        print(f'Found at {abs_idx}, text: {repr(old_text[:60])}')\n    else:\n        print('Could not find bottomrule pattern after S12')\n        # Try different approach\n        lines = content.split('\\n')\n        for i, line in enumerate(lines):\n            if 'bottomrule' in line and i > 0 and 's12_domain_ablation' in '\\n'.join(lines[max(0,i-20):i]):\n                print(f'Found bottomrule at line {i+1}: {line}')\n                break\n\"\n",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "cd /root/autodl-tmp/gen-depth-contamination/docs/paper && python3 -c \"\nimport re\n# Add footnote to Table S12 in appendix.tex\nwith open('appendix.tex', 'r') as f:\n    content = f.read()\n\nold = '''    \\\\\\\\bottomrule\n  \\\\\\\\end{tabular}\n\\\\\\\\end{table*}\n\n%%% Table S13: Scorer Sensitivity Analysis'''\n\nnew = '''    \\\\\\\\bottomrule\n    \\\\\\\\multicolumn{4}{l}{\\\\\\\\footnotesize \\$^*\\$Bootstrap 95\\\\\\\\% CI (\\$n{=}10{,}000\\$); permutation \\$p < 0.001\\$. CI lower bound exceeds \\$\\\\\\\\theta\\$.}\n  \\\\\\\\end{tabular}\n\\\\\\\\end{table*}\n\n%%% Table S13: Scorer Sensitivity Analysis'''\n\n# Only replace the first occurrence near Table S12\nidx = content.find('s12_domain_ablation')\nif idx > 0:\n    rest = content[idx:]\n    old_in_rest = old.replace('\\\\\\\\\\\\\\\\', '\\\\\\\\')\n    # Find the bottomrule after S12\n    bt_idx = rest.find('\\\\\\\\bottomrule\\n  \\\\\\\\end{tabular}\\n\\\\\\\\end{table*}\\n\\n%%% Table S13')\n    if bt_idx > 0:\n        abs_idx = idx + bt_idx\n        old_text = content[abs_idx:abs_idx+len('\\\\\\\\bottomrule\\n  \\\\\\\\end{tabular}\\n\\\\\\\\end{table*}\\n\\n%%% Table S13')]\n        print(f'Found at {abs_idx}, text: {repr(old_text[:60])}')\n    else:\n        print('Could not find bottomrule pattern after S12')\n        # Try different approach\n        lines = content.split('\\n')\n        for i, line in enumerate(lines):\n            if 'bottomrule' in line and i > 0 and 's12_domain_ablation' in '\\n'.join(lines[max(0,i-20):i]):\n                print(f'Found bottomrule at line {i+1}: {line}')\n                break\n\"\n",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 110 · 2026-05-22T08:36:59.184169+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Found at 25791, text: '\\\\\\\\bottomrule\\\\n  \\\\\\\\end{tabular}\\\\n\\\\\\\\end{table*}\\\\n\\\\n%%% Table S13'\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 111 · 2026-05-22T08:36:59.184300+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-22115",
  "command": "cd /root/autodl-tmp/gen-depth-contamination/docs/paper && python3 -c \"\nwith open('appendix.tex', 'r') as f:\n    content = f.read()\n\nold = '\\\\\\\\bottomrule\\n  \\\\\\\\end{tabular}\\n\\\\\\\\end{table*}\\n\\n%%% Table S13: Scorer Sensitivity Analysis'\n\nnew = '\\\\\\\\bottomrule\\n    \\\\\\\\multicolumn{4}{l}{\\\\\\\\footnotesize \\$^*\\$Bootstrap 95\\\\\\\\% CI (\\$n{=}10{,}000\\$); permutation \\$p < 0.001\\$. CI lower bound exceeds \\$\\\\\\\\theta\\$.}\\n  \\\\\\\\end{tabular}\\n\\\\\\\\end{table*}\\n\\n%%% Table S13: Scorer Sensitivity Analysis'\n\n# Find the right occurrence (after s12_domain_ablation)\nidx = content.find('s12_domain_ablation')\nif idx < 0:\n    print('ERROR: s12 not found')\nelse:\n    rest = content[idx:]\n    bt = rest.find(old)\n    if bt < 0:\n        print('ERROR: bottomrule pattern not found after S12')\n        # Show what's there\n        bt2 = rest.find('\\\\\\\\bottomrule')\n        if bt2 > 0:\n            print(repr(rest[bt2:bt2+100]))\n    else:\n        abs_pos = idx + bt\n        content = content[:abs_pos] + new + content[abs_pos + len(old):]\n        with open('appendix.tex', 'w') as f:\n            f.write(content)\n        print('OK: footnote added')\n\"\n",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "cd /root/autodl-tmp/gen-depth-contamination/docs/paper && python3 -c \"\nwith open('appendix.tex', 'r') as f:\n    content = f.read()\n\nold = '\\\\\\\\bottomrule\\n  \\\\\\\\end{tabular}\\n\\\\\\\\end{table*}\\n\\n%%% Table S13: Scorer Sensitivity Analysis'\n\nnew = '\\\\\\\\bottomrule\\n    \\\\\\\\multicolumn{4}{l}{\\\\\\\\footnotesize \\$^*\\$Bootstrap 95\\\\\\\\% CI (\\$n{=}10{,}000\\$); permutation \\$p < 0.001\\$. CI lower bound exceeds \\$\\\\\\\\theta\\$.}\\n  \\\\\\\\end{tabular}\\n\\\\\\\\end{table*}\\n\\n%%% Table S13: Scorer Sensitivity Analysis'\n\n# Find the right occurrence (after s12_domain_ablation)\nidx = content.find('s12_domain_ablation')\nif idx < 0:\n    print('ERROR: s12 not found')\nelse:\n    rest = content[idx:]\n    bt = rest.find(old)\n    if bt < 0:\n        print('ERROR: bottomrule pattern not found after S12')\n        # Show what's there\n        bt2 = rest.find('\\\\\\\\bottomrule')\n        if bt2 > 0:\n            print(repr(rest[bt2:bt2+100]))\n    else:\n        abs_pos = idx + bt\n        content = content[:abs_pos] + new + content[abs_pos + len(old):]\n        with open('appendix.tex', 'w') as f:\n            f.write(content)\n        print('OK: footnote added')\n\"\n",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 112 · 2026-05-22T08:36:59.184443+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"OK: footnote added\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 113 · 2026-05-22T08:36:59.184584+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-22115",
  "command": "cd /root/autodl-tmp/gen-depth-contamination/docs/paper && python3 -c \"\nwith open('experiments_c1.tex', 'r') as f:\n    content = f.read()\n\nold = 'Both Qwen-1.5B and Pythia-1.4B yield \\$\\\\\\\\Kempirical{=}3\\$ for arXiv (Table~\\\\\\\\ref{tab:domain_kstar}), demonstrating that structured academic text permits discrimination to greater depth independently of architecture.'\n\nnew = 'Both Qwen-1.5B and Pythia-1.4B yield \\$\\\\\\\\Kempirical{=}3\\$ for arXiv (Table~\\\\\\\\ref{tab:domain_kstar}): 2v3 \\$\\\\\\\\auc = 0.644\\\\\\\\;[0.628,\\\\\\\\,0.658]\\$ and \\$0.655\\\\\\\\;[0.640,\\\\\\\\,0.669]\\$ respectively (bootstrap CI lower bounds above \\$\\\\\\\\theta\\$; permutation \\$p < 0.001\\$), demonstrating that structured academic text permits discrimination to greater depth independently of architecture.'\n\nif old in content:\n    content = content.replace(old, new)\n    with open('experiments_c1.tex', 'w') as f:\n        f.write(content)\n    print('OK')\nelse:\n    print('NOT FOUND')\n    # Check what's there\n    idx = content.find('Both Qwen-1.5B and Pythia-1.4B yield')\n    if idx >= 0:\n        print(repr(content[idx:idx+300]))\n\"\n",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "cd /root/autodl-tmp/gen-depth-contamination/docs/paper && python3 -c \"\nwith open('experiments_c1.tex', 'r') as f:\n    content = f.read()\n\nold = 'Both Qwen-1.5B and Pythia-1.4B yield \\$\\\\\\\\Kempirical{=}3\\$ for arXiv (Table~\\\\\\\\ref{tab:domain_kstar}), demonstrating that structured academic text permits discrimination to greater depth independently of architecture.'\n\nnew = 'Both Qwen-1.5B and Pythia-1.4B yield \\$\\\\\\\\Kempirical{=}3\\$ for arXiv (Table~\\\\\\\\ref{tab:domain_kstar}): 2v3 \\$\\\\\\\\auc = 0.644\\\\\\\\;[0.628,\\\\\\\\,0.658]\\$ and \\$0.655\\\\\\\\;[0.640,\\\\\\\\,0.669]\\$ respectively (bootstrap CI lower bounds above \\$\\\\\\\\theta\\$; permutation \\$p < 0.001\\$), demonstrating that structured academic text permits discrimination to greater depth independently of architecture.'\n\nif old in content:\n    content = content.replace(old, new)\n    with open('experiments_c1.tex', 'w') as f:\n        f.write(content)\n    print('OK')\nelse:\n    print('NOT FOUND')\n    # Check what's there\n    idx = content.find('Both Qwen-1.5B and Pythia-1.4B yield')\n    if idx >= 0:\n        print(repr(content[idx:idx+300]))\n\"\n",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 114 · 2026-05-22T08:36:59.184719+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"OK\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 115 · 2026-05-22T08:36:59.184892+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-22115",
  "command": "cd /root/autodl-tmp/gen-depth-contamination/docs/paper && python3 << 'PYEOF'\nwith open('appendix_extended.tex', 'r') as f:\n    content = f.read()\n\n# Check if Bonferroni section already exists\nif 'bonferroni_ci' in content:\n    print('ALREADY EXISTS')\nelse:\n    # Find the end of the seed robustness table\n    marker = r\"\"\"\\end{tabular}}\n\\end{table}\"\"\"\n    \n    # Find last occurrence (the seed robustness table is the last table)\n    idx = content.rfind(marker)\n    if idx < 0:\n        print('MARKER NOT FOUND')\n    else:\n        insert_pos = idx + len(marker)\n        \n        bonferroni = r\"\"\"\n\n\\subsection{Bonferroni-Corrected Confidence Intervals}\n\\label{sec:bonferroni_ci}\n\nTo control the family-wise error rate across all 10 model configurations, we apply Bonferroni correction: $\\alpha_{\\text{corr}} = 0.05 / 10 = 0.005$, yielding 99.5\\% confidence intervals ($z = 2.807$).\nTable~\\ref{tab:bonferroni_ci} reports the corrected intervals for each configuration's $\\Kempirical$ boundary pair.\nEight of ten configurations retain CI lower bounds above $\\theta{=}0.60$; two marginal $\\Kempirical{=}2$ configurations (Qwen-cont, LLaMA-8B) see their lower bounds dip below $\\theta$ under the stricter criterion ($0.5976$ and $0.5988$, respectively).\nThese near-misses reflect narrow effect sizes ($\\auc - \\theta < 0.013$) rather than classification failure: both retain point estimates above $\\theta$ and uncorrected 95\\% CI lower bounds above $\\theta$.\n\n\\begin{table}[h]\n\\centering\n\\footnotesize\n\\caption{Bonferroni-corrected 99.5\\% confidence intervals for $\\Kempirical$ boundary pairs across all 10 configurations. $\\alpha_{\\text{corr}} = 0.005$; CI computed as $\\auc \\pm 2.807 \\times \\hat{\\sigma}_{\\text{boot}}$. ``Pass $\\theta$'': CI lower bound $> 0.60$.}\n\\label{tab:bonferroni_ci}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Configuration} & \\textbf{Boundary} & $\\auc$ & $\\hat{\\sigma}_{\\text{boot}}$ & \\textbf{99.5\\% CI} & \\textbf{Pass $\\theta$} \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{$\\Kempirical = 2$ configurations}} \\\\\nQwen-rw (Instruct)       & 1v2 & .6955 & .0046 & $[.683,\\,.708]$ & \\checkmark \\\\\nPythia-1.4B               & 1v2 & .6539 & .0046 & $[.641,\\,.667]$ & \\checkmark \\\\\nQwen-base                 & 1v2 & .6260 & .0047 & $[.613,\\,.639]$ & \\checkmark \\\\\nQwen-7B$^\\ddagger$        & 1v2 & .6168 & .0046 & $[.604,\\,.630]$ & \\checkmark \\\\\nLLaMA-8B                  & 1v2 & .6123 & .0048 & $[.599,\\,.626]$ & $\\times$ \\\\\nQwen-cont (Instruct)     & 1v2 & .6112 & .0049 & $[.598,\\,.625]$ & $\\times$ \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{$\\Kempirical = 1$ configurations}} \\\\\nOLMo-1B                   & 0v1 & .9860 & .0009 & $[.983,\\,.989]$ & \\checkmark \\\\\nMistral-7B                & 0v1 & .9842 & .0009 & $[.982,\\,.987]$ & \\checkmark \\\\\nPythia-6.9B$^\\S$          & 0v1 & .9599 & .0015$^\\dagger$ & $[.956,\\,.964]$ & \\checkmark \\\\\nGemma-2-2B                & 0v1 & .9530 & .0018 & $[.948,\\,.958]$ & \\checkmark \\\\\n\\bottomrule\n\\multicolumn{6}{l}{\\footnotesize $^\\ddagger$Generator: Qwen2.5-7B; scorer: Qwen2.5-1.5B.} \\\\\n\\multicolumn{6}{l}{\\footnotesize $^\\S$Nucleus sampling ($p{=}0.95$, $T{=}1.0$).} \\\\\n\\multicolumn{6}{l}{\\footnotesize $^\\dagger$Estimated from analogous configurations (no separate bootstrap JSON).}\n\\end{tabular}}\n\\end{table}\"\"\"\n        \n        content = content[:insert_pos] + bonferroni + content[insert_pos:]\n        with open('appendix_extended.tex', 'w') as f:\n            f.write(content)\n        print('OK: Bonferroni section added')\nPYEOF\n",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "cd /root/autodl-tmp/gen-depth-contamination/docs/paper && python3 << 'PYEOF'\nwith open('appendix_extended.tex', 'r') as f:\n    content = f.read()\n\n# Check if Bonferroni section already exists\nif 'bonferroni_ci' in content:\n    print('ALREADY EXISTS')\nelse:\n    # Find the end of the seed robustness table\n    marker = r\"\"\"\\end{tabular}}\n\\end{table}\"\"\"\n    \n    # Find last occurrence (the seed robustness table is the last table)\n    idx = content.rfind(marker)\n    if idx < 0:\n        print('MARKER NOT FOUND')\n    else:\n        insert_pos = idx + len(marker)\n        \n        bonferroni = r\"\"\"\n\n\\subsection{Bonferroni-Corrected Confidence Intervals}\n\\label{sec:bonferroni_ci}\n\nTo control the family-wise error rate across all 10 model configurations, we apply Bonferroni correction: $\\alpha_{\\text{corr}} = 0.05 / 10 = 0.005$, yielding 99.5\\% confidence intervals ($z = 2.807$).\nTable~\\ref{tab:bonferroni_ci} reports the corrected intervals for each configuration's $\\Kempirical$ boundary pair.\nEight of ten configurations retain CI lower bounds above $\\theta{=}0.60$; two marginal $\\Kempirical{=}2$ configurations (Qwen-cont, LLaMA-8B) see their lower bounds dip below $\\theta$ under the stricter criterion ($0.5976$ and $0.5988$, respectively).\nThese near-misses reflect narrow effect sizes ($\\auc - \\theta < 0.013$) rather than classification failure: both retain point estimates above $\\theta$ and uncorrected 95\\% CI lower bounds above $\\theta$.\n\n\\begin{table}[h]\n\\centering\n\\footnotesize\n\\caption{Bonferroni-corrected 99.5\\% confidence intervals for $\\Kempirical$ boundary pairs across all 10 configurations. $\\alpha_{\\text{corr}} = 0.005$; CI computed as $\\auc \\pm 2.807 \\times \\hat{\\sigma}_{\\text{boot}}$. ``Pass $\\theta$'': CI lower bound $> 0.60$.}\n\\label{tab:bonferroni_ci}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Configuration} & \\textbf{Boundary} & $\\auc$ & $\\hat{\\sigma}_{\\text{boot}}$ & \\textbf{99.5\\% CI} & \\textbf{Pass $\\theta$} \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{$\\Kempirical = 2$ configurations}} \\\\\nQwen-rw (Instruct)       & 1v2 & .6955 & .0046 & $[.683,\\,.708]$ & \\checkmark \\\\\nPythia-1.4B               & 1v2 & .6539 & .0046 & $[.641,\\,.667]$ & \\checkmark \\\\\nQwen-base                 & 1v2 & .6260 & .0047 & $[.613,\\,.639]$ & \\checkmark \\\\\nQwen-7B$^\\ddagger$        & 1v2 & .6168 & .0046 & $[.604,\\,.630]$ & \\checkmark \\\\\nLLaMA-8B                  & 1v2 & .6123 & .0048 & $[.599,\\,.626]$ & $\\times$ \\\\\nQwen-cont (Instruct)     & 1v2 & .6112 & .0049 & $[.598,\\,.625]$ & $\\times$ \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{$\\Kempirical = 1$ configurations}} \\\\\nOLMo-1B                   & 0v1 & .9860 & .0009 & $[.983,\\,.989]$ & \\checkmark \\\\\nMistral-7B                & 0v1 & .9842 & .0009 & $[.982,\\,.987]$ & \\checkmark \\\\\nPythia-6.9B$^\\S$          & 0v1 & .9599 & .0015$^\\dagger$ & $[.956,\\,.964]$ & \\checkmark \\\\\nGemma-2-2B                & 0v1 & .9530 & .0018 & $[.948,\\,.958]$ & \\checkmark \\\\\n\\bottomrule\n\\multicolumn{6}{l}{\\footnotesize $^\\ddagger$Generator: Qwen2.5-7B; scorer: Qwen2.5-1.5B.} \\\\\n\\multicolumn{6}{l}{\\footnotesize $^\\S$Nucleus sampling ($p{=}0.95$, $T{=}1.0$).} \\\\\n\\multicolumn{6}{l}{\\footnotesize $^\\dagger$Estimated from analogous configurations (no separate bootstrap JSON).}\n\\end{tabular}}\n\\end{table}\"\"\"\n        \n        content = content[:insert_pos] + bonferroni + content[insert_pos:]\n        with open('appendix_extended.tex', 'w') as f:\n            f.write(content)\n        print('OK: Bonferroni section added')\nPYEOF\n",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 116 · 2026-05-22T08:36:59.185065+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"OK: Bonferroni section added\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.46}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 117 · 2026-05-22T08:36:59.185211+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-22115",
  "command": "cd /root/autodl-tmp/gen-depth-contamination/docs/paper && pdflatex -interaction=nonstopmode main.tex 2>&1 | tail -20",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "cd /root/autodl-tmp/gen-depth-contamination/docs/paper && pdflatex -interaction=nonstopmode main.tex 2>&1 | tail -20",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 118 · 2026-05-22T08:36:59.185357+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"mf-dist/fonts/type1/public/amsfonts/cmextra/cmmib9.pfb>&lt;/usr/share/texlive/texm\\nf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/\\nfonts/type1/public/amsfonts/cm/cmr6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\\npe1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publ\\nic/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfo\\nnts/cm/cmr9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/c\\nmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy5.p\\nfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/us\\nr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share\\n/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texliv\\ne/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf\\n-dist/fonts/type1/public/amsfonts/symbols/msam10.pfb>&lt;/usr/share/texlive/texmf-\\ndist/fonts/type1/public/amsfonts/symbols/msbm10.pfb>&lt;/usr/share/texlive/texmf-d\\nist/fonts/type1/urw/courier/ucrb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ\\ne1/urw/courier/ucrr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/helvet\\nic/uhvb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb><\\n/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texl\\nive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>\\nOutput written on main.pdf (22 pages, 542144 bytes).\\nTranscript written on main.log.\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.06}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 119 · 2026-05-22T08:36:59.185515+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "grep -i \"warning\\|error\\|undefined\" /root/autodl-tmp/gen-depth-contamination/docs/paper/main.log | grep -iv \"font\\|rerun\\|multiply\\|already\\|float\" | head -15",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "grep -i \"warning\\|error\\|undefined\" /root/autodl-tmp/gen-depth-contamination/docs/paper/main.log | grep -iv \"font\\|rerun\\|multiply\\|already\\|float\" | head -15",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 120 · 2026-05-22T08:36:59.185664+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 121 · 2026-05-22T08:36:59.185844+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "grep \"undefined\" /root/autodl-tmp/gen-depth-contamination/docs/paper/main.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "grep \"undefined\" /root/autodl-tmp/gen-depth-contamination/docs/paper/main.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 122 · 2026-05-22T08:36:59.185982+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Package natbib Warning: Citation `geng2026markovian' on page 2 undefined on inp\\nPackage natbib Warning: Citation `shahriar2025erosion' on page 2 undefined on i\\nLaTeX Warning: Reference `tab:bonferroni_ci' on page 22 undefined on input line\\nPackage natbib Warning: There were undefined citations.\\nLaTeX Warning: There were undefined references.\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 123 · 2026-05-22T08:36:59.186114+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "grep \"bonferroni\" /root/autodl-tmp/gen-depth-contamination/docs/paper/main.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "grep \"bonferroni\" /root/autodl-tmp/gen-depth-contamination/docs/paper/main.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 124 · 2026-05-22T08:36:59.186239+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"LaTeX Warning: Reference `tab:bonferroni_ci' on page 22 undefined on input line\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 125 · 2026-05-22T08:36:59.186392+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-22115",
  "command": "cd /root/autodl-tmp/gen-depth-contamination/docs/paper && pdflatex -interaction=nonstopmode main.tex 2>&1 | tail -5",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "cd /root/autodl-tmp/gen-depth-contamination/docs/paper && pdflatex -interaction=nonstopmode main.tex 2>&1 | tail -5",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 126 · 2026-05-22T08:36:59.186521+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"ic/uhvb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb><\\n/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texl\\nive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>\\nOutput written on main.pdf (22 pages, 542083 bytes).\\nTranscript written on main.log.\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.07}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 127 · 2026-05-22T08:36:59.186642+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "grep \"bonferroni\" /root/autodl-tmp/gen-depth-contamination/docs/paper/main.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "grep \"bonferroni\" /root/autodl-tmp/gen-depth-contamination/docs/paper/main.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 128 · 2026-05-22T08:36:59.186765+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.38}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 129 · 2026-05-22T08:36:59.186938+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "MF-1 arXiv CI + SF-3 Bonferroni table",
  "type": "paper",
  "description": "Added arXiv 2v3 bootstrap CI to Table S12 and main text Section 4.6; added Bonferroni-corrected 99.5% CI table to appendix_extended.tex",
  "project": "gen-depth-contamination",
  "content": "## MF-1: arXiv 2v3 CI\n\n### Verified values (from JSON)\n- Qwen arXiv 2v3: AUC=0.6427, CI=[0.6275, 0.6575], perm_p=0.0001 ✓\n- Pythia arXiv 2v3: AUC=0.6544, CI=[0.6401, 0.6688], perm_p=0.0001 ✓\n\n### Edits\n1. appendix.tex Table S12: arXiv 2v3 row now shows $.6436\\;[.628,.658]$ with footnote\n2. experiments_c1.tex Section 4.6: added inline CIs for both Qwen and Pythia arXiv 2v3\n\n## SF-3: Bonferroni 99.5% CI (10 configs)\n\nα_corr = 0.05/10 = 0.005, z = 2.807\n\n| Config | Boundary | AUC | σ_boot | 99.5% CI | Pass θ |\n|--------|----------|-----|--------|----------|--------|\n| Qwen-rw | 1v2 | .6955 | .0046 | [.683, .708] | ✓ |\n| Pythia-1.4B | 1v2 | .6539 | .0046 | [.641, .667] | ✓ |\n| Qwen-base | 1v2 | .6260 | .0047 | [.613, .639] | ✓ |\n| Qwen-7B | 1v2 | .6168 | .0046 | [.604, .630] | ✓ |\n| LLaMA-8B | 1v2 | .6123 | .0048 | [.599, .626] | ✗ |\n| Qwen-cont | 1v2 | .6112 | .0049 | [.598, .625] | ✗ |\n| OLMo-1B | 0v1 | .9860 | .0009 | [.983, .989] | ✓ |\n| Mistral-7B | 0v1 | .9842 | .0009 | [.982, .987] | ✓ |\n| Pythia-6.9B | 0v1 | .9599 | ~.0015 | [.956, .964] | ✓ |\n| Gemma-2-2B | 0v1 | .9530 | .0018 | [.948, .958] | ✓ |\n\n**2/10 fail**: Qwen-cont (CI_lower=0.5976) and LLaMA-8B (CI_lower=0.5988)\n",
  "content_filename": "mf1_sf3_bonferroni_summary.md",
  "tags": "['paper', 'statistics', 'bonferroni', 'arXiv-CI']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "MF-1 arXiv CI + SF-3 Bonferroni table",
    "type": "paper",
    "description": "Added arXiv 2v3 bootstrap CI to Table S12 and main text Section 4.6; added Bonferroni-corrected 99.5% CI table to appendix_extended.tex",
    "project": "gen-depth-contamination",
    "content": "## MF-1: arXiv 2v3 CI\n\n### Verified values (from JSON)\n- Qwen arXiv 2v3: AUC=0.6427, CI=[0.6275, 0.6575], perm_p=0.0001 ✓\n- Pythia arXiv 2v3: AUC=0.6544, CI=[0.6401, 0.6688], perm_p=0.0001 ✓\n\n### Edits\n1. appendix.tex Table S12: arXiv 2v3 row now shows $.6436\\;[.628,.658]$ with footnote\n2. experiments_c1.tex Section 4.6: added inline CIs for both Qwen and Pythia arXiv 2v3\n\n## SF-3: Bonferroni 99.5% CI (10 configs)\n\nα_corr = 0.05/10 = 0.005, z = 2.807\n\n| Config | Boundary | AUC | σ_boot | 99.5% CI | Pass θ |\n|--------|----------|-----|--------|----------|--------|\n| Qwen-rw | 1v2 | .6955 | .0046 | [.683, .708] | ✓ |\n| Pythia-1.4B | 1v2 | .6539 | .0046 | [.641, .667] | ✓ |\n| Qwen-base | 1v2 | .6260 | .0047 | [.613, .639] | ✓ |\n| Qwen-7B | 1v2 | .6168 | .0046 | [.604, .630] | ✓ |\n| LLaMA-8B | 1v2 | .6123 | .0048 | [.599, .626] | ✗ |\n| Qwen-cont | 1v2 | .6112 | .0049 | [.598, .625] | ✗ |\n| OLMo-1B | 0v1 | .9860 | .0009 | [.983, .989] | ✓ |\n| Mistral-7B | 0v1 | .9842 | .0009 | [.982, .987] | ✓ |\n| Pythia-6.9B | 0v1 | .9599 | ~.0015 | [.956, .964] | ✓ |\n| Gemma-2-2B | 0v1 | .9530 | .0018 | [.948, .958] | ✓ |\n\n**2/10 fail**: Qwen-cont (CI_lower=0.5976) and LLaMA-8B (CI_lower=0.5988)\n",
    "content_filename": "mf1_sf3_bonferroni_summary.md",
    "tags": "['paper', 'statistics', 'bonferroni', 'arXiv-CI']"
  }
}
```

</details>

---

### Tool result

_source line 130 · 2026-05-22T08:36:59.187112+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260522_bd25ce\", \"name\": \"MF-1 arXiv CI + SF-3 Bonferroni table\", \"type\": \"paper\", \"description\": \"Added arXiv 2v3 bootstrap CI to Table S12 and main text Section 4.6; added Bonferroni-corrected 99.5% CI table to appendix_extended.tex\", \"path\": \"projects/gen-depth-contamination/artifacts/_project/paper/mf1_sf3_bonferroni_summary.md\", \"url\": null, \"project\": \"gen-depth-contamination\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-22T08:36:40.773552+00:00\", \"tags\": [\"paper\", \"statistics\", \"bonferroni\", \"arXiv-CI\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 131 · 2026-05-22T08:36:59.187292+00:00_

---

## 结果汇总

### Part 1: MF-1 — arXiv 2v3 CI

**JSON 验证**（均正确）：
- Qwen arXiv 2v3: AUC=0.6427, CI=[0.6275, 0.6575], perm_p=0.0001
- Pythia arXiv 2v3: AUC=0.6544, CI=[0.6401, 0.6688], perm_p=0.0001

**修改**：
1. `appendix.tex` Table S12 arXiv 2v3 行：`.6436` → `$.6436\;[.628,\,.658]$` + 脚注（p<0.001, CI lower > θ）
2. `experiments_c1.tex` Section 4.6：arXiv 讨论句添加了两个模型的 2v3 CI 和 "CI lower bounds above θ" 措辞

### Part 2: SF-3 — Bonferroni 99.5% CI

α_corr = 0.005, z = 2.807

| Config | Boundary | AUC | σ_boot | 99.5% CI | Pass θ |
|---|---|---|---|---|---|
| Qwen-rw | 1v2 | .6955 | .0046 | [.683, .708] | ✓ |
| Pythia-1.4B | 1v2 | .6539 | .0046 | [.641, .667] | ✓ |
| Qwen-base | 1v2 | .6260 | .0047 | [.613, .639] | ✓ |
| Qwen-7B | 1v2 | .6168 | .0046 | [.604, .630] | ✓ |
| **LLaMA-8B** | **1v2** | **.6123** | **.0048** | **[.599, .626]** | **✗** |
| **Qwen-cont** | **1v2** | **.6112** | **.0049** | **[.598, .625]** | **✗** |
| OLMo-1B | 0v1 | .9860 | .0009 | [.983, .989] | ✓ |
| Mistral-7B | 0v1 | .9842 | .0009 | [.982, .987] | ✓ |
| Pythia-6.9B | 0v1 | .9599 | ~.0015† | [.956, .964] | ✓ |
| Gemma-2-2B | 0v1 | .9530 | .0018 | [.948, .958] | ✓ |

**2/10 CI lower bound 跌破 θ=0.60**：
- **Qwen-cont**：CI_lower = 0.5976 < 0.60（符合预期）
- **LLaMA-8B**：CI_lower = 0.5988 < 0.60（额外发现）

Bonferroni 表已添加到 `appendix_extended.tex` Section "Bonferroni-Corrected Confidence Intervals"。正文 6/10 计数未修改。

†Pythia-6.9B 无单独 bootstrap JSON，σ_boot 从同类配置估计。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_r26_mf1_sf3_arxiv_bonferroni_20260522T082230"
}
```

</details>

---
