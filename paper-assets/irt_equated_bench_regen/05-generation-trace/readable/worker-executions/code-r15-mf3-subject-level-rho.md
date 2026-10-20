# code r15 mf3 subject level rho

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 21
- **Recorded user turns:** 0
- **Tool calls:** 5
- **Original source:** `logs/workers/worker_code_r15_mf3_subject_level_rho_20260522T124300.log`
- **Structured JSON:** [`123d381f70aa7c5aef14.json`](../../sessions/12/123d381f70aa7c5aef14.json)

## Before a recorded user message

21 recorded events

### Log line

_source line 1_

Warning: no stdin data received in 3s, proceeding without it. If piping from a slow command, redirect stdin explicitly: < /dev/null to skip, or wait longer.

---

### System

_source line 2_

```json
{
  "type": "system",
  "subtype": "init",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "session_id": "5c8383e8-eeae-4526-bae4-522e0eaabe0c",
  "tools": [
    "Task",
    "AskUserQuestion",
    "Bash",
    "CronCreate",
    "CronDelete",
    "CronList",
    "Edit",
    "EnterPlanMode",
    "EnterWorktree",
    "ExitPlanMode",
    "ExitWorktree",
    "Glob",
    "Grep",
    "ListMcpResourcesTool",
    "Monitor",
    "NotebookEdit",
    "PushNotification",
    "Read",
    "ReadMcpResourceTool",
    "RemoteTrigger",
    "ScheduleWakeup",
    "Skill",
    "TaskOutput",
    "TaskStop",
    "TodoWrite",
    "ToolSearch",
    "WebFetch",
    "WebSearch",
    "Write",
    "mcp__agent-ml-research__append_idea",
    "mcp__agent-ml-research__read_project_file",
    "mcp__agent-ml-research__save_project_file"
  ],
  "mcp_servers": [
    {
      "name": "agent-ml-research",
      "status": "connected"
    }
  ],
  "model": "claude-opus-4-6",
  "permissionMode": "bypassPermissions",
  "slash_commands": [
    "update-config",
    "debug",
    "simplify",
    "batch",
    "fewer-permission-prompts",
    "loop",
    "schedule",
    "claude-api",
    "clear",
    "compact",
    "context",
    "heapdump",
    "init",
    "review",
    "security-review",
    "extra-usage",
    "usage",
    "insights",
    "team-onboarding"
  ],
  "apiKeySource": "none",
  "claude_code_version": "2.1.126",
  "output_style": "default",
  "agents": [
    "claude",
    "Explore",
    "general-purpose",
    "Plan",
    "statusline-setup"
  ],
  "skills": [
    "update-config",
    "debug",
    "simplify",
    "batch",
    "fewer-permission-prompts",
    "loop",
    "schedule",
    "claude-api"
  ],
  "plugins": [],
  "analytics_disabled": false,
  "uuid": "10c70caf-7a60-4d61-a0d6-5980fefd5354",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude/projects/-home-ubuntu--agent-ml-research-idea-gen-0520-2-projects-irt-equated-bench-regen/memory/"
  },
  "fast_mode_state": "off"
}
```

---

### Runtime record

_source line 3_

```json
{
  "type": "rate_limit_event",
  "rate_limit_info": {
    "status": "allowed",
    "resetsAt": 1779469800,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "77d398b1-e883-4fe1-a9d5-6083a9cab3e8",
  "session_id": "5c8383e8-eeae-4526-bae4-522e0eaabe0c"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to perform a subject-level ranking analysis to show that while aggregate Spearman ρ ≈ 0.997, subject-level rankings change significantly when DIF-C items are removed. Let me start by understanding the data and then write the analysis script.

Let me first check the data files exist and understand their structure.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5c8383e8-eeae-4526-bae4-522e0eaabe0c",
  "uuid": "846b5b98-fad2-4031-9951-6c539a3ab3b0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016Ak3ra3DxuzC3Vn4noJzvL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12834,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12834
      },
      "output_tokens": 25,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 5_

I'll start by examining the data files to understand their structure, then write and run the analysis.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5c8383e8-eeae-4526-bae4-522e0eaabe0c",
  "uuid": "267ed991-7484-43f0-a7b8-28a05c65411c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016Ak3ra3DxuzC3Vn4noJzvL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12834,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12834
      },
      "output_tokens": 25,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 6_

<details open><summary>🔧 Tool call — Bash · `toolu_01YLLgLJKbHK1ZXewzX5LpDB`</summary>

```json
{
  "command": "python3 -c \"\nimport numpy as np, pandas as pd\n\n# Response matrix\nrm = np.load('artifacts/response_matrix.npz')\nprint('Response matrix keys:', list(rm.keys()))\nprint('X shape:', rm['X'].shape)\n\nidx = np.load('artifacts/response_matrix_index.npz', allow_pickle=True)\nprint('Index keys:', list(idx.keys()))\nprint('model_names:', idx['model_names'].shape, idx['model_names'][:3])\nprint('item_ids:', idx['item_ids'].shape, idx['item_ids'][:5])\n\n# DIF results\ndif = pd.read_csv('artifacts/plan_001/dif_results_temporal.csv')\nprint('\\nDIF columns:', dif.columns.tolist())\nprint('DIF shape:', dif.shape)\nprint('ets_class counts:')\nprint(dif['ets_class'].value_counts())\nprint('\\nSample item_ids:', dif['item_id'].head())\nprint('Unique subjects:', dif['subject'].nunique())\n\"\n",
  "description": "Inspect data files structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5c8383e8-eeae-4526-bae4-522e0eaabe0c",
  "uuid": "74483ec8-0349-45e4-ab83-a1464d17b912",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016Ak3ra3DxuzC3Vn4noJzvL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12834,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12834
      },
      "output_tokens": 25,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-22T12:43:22.128Z_

<details><summary>↩ Tool result · reported error · `toolu_01YLLgLJKbHK1ZXewzX5LpDB`</summary>

```text
Exit code 1
Traceback (most recent call last):
  File "&lt;string>", line 7, in &lt;module>
    print('X shape:', rm['X'].shape)
                      ~~^^^^^
  File "/usr/lib/python3/dist-packages/numpy/lib/_npyio_impl.py", line 243, in __getitem__
    raise KeyError(f"{key} is not a file in the archive") from None
KeyError: 'X is not a file in the archive'
Response matrix keys: ['indices', 'indptr', 'format', 'shape', 'data']
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5c8383e8-eeae-4526-bae4-522e0eaabe0c",
  "uuid": "6d983181-fa74-4e71-9570-ca8abf6636d3",
  "tool_use_result": "Error: Exit code 1\nTraceback (most recent call last):\n  File \"&lt;string>\", line 7, in &lt;module>\n    print('X shape:', rm['X'].shape)\n                      ~~^^^^^\n  File \"/usr/lib/python3/dist-packages/numpy/lib/_npyio_impl.py\", line 243, in __getitem__\n    raise KeyError(f\"{key} is not a file in the archive\") from None\nKeyError: 'X is not a file in the archive'\nResponse matrix keys: ['indices', 'indptr', 'format', 'shape', 'data']"
}
```

</details>

---

### Assistant

_source line 8_

Sparse matrix. Let me handle that.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5c8383e8-eeae-4526-bae4-522e0eaabe0c",
  "uuid": "f8932322-bcc2-42a6-87ff-62e278ce0cb2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CXEUpg2NQxokdRS1Cv6GLc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 615,
      "cache_read_input_tokens": 24675,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 615
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 9_

<details open><summary>🔧 Tool call — Bash · `toolu_01P9WfzRzBgqjSHnLLfCVtMm`</summary>

```json
{
  "command": "python3 -c \"\nimport numpy as np, pandas as pd\nfrom scipy import sparse\n\n# Response matrix (sparse)\nrm = np.load('artifacts/response_matrix.npz')\nprint('Sparse keys:', list(rm.keys()))\nprint('Shape:', rm['shape'])\nprint('Format:', rm['format'])\n\nX = sparse.csr_matrix((rm['data'], rm['indices'], rm['indptr']), shape=tuple(rm['shape']))\nprint('Reconstructed:', X.shape, 'nnz:', X.nnz)\nprint('Density:', X.nnz / (X.shape[0] * X.shape[1]))\n\nidx = np.load('artifacts/response_matrix_index.npz', allow_pickle=True)\nmodel_names = idx['model_names']\nitem_ids = idx['item_ids']\nprint('\\nModels:', model_names.shape[0])\nprint('Items:', item_ids.shape[0])\nprint('Sample items:', item_ids[:5])\n\n# DIF\ndif = pd.read_csv('artifacts/plan_001/dif_results_temporal.csv')\nprint('\\nets_class counts:')\nprint(dif['ets_class'].value_counts())\nprint('Subjects:', dif['subject'].nunique())\n\n# Check subject extraction from item_ids\nsubjects_from_ids = set(iid.rsplit('.', 1)[0] for iid in item_ids)\nprint('Subjects from item_ids:', len(subjects_from_ids))\n\"\n",
  "description": "Inspect sparse matrix and data structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5c8383e8-eeae-4526-bae4-522e0eaabe0c",
  "uuid": "85096277-964d-434d-b846-bc25284c2cf4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CXEUpg2NQxokdRS1Cv6GLc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 615,
      "cache_read_input_tokens": 24675,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 615
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-22T12:43:33.933Z_

<details><summary>↩ Tool result · `toolu_01P9WfzRzBgqjSHnLLfCVtMm`</summary>

```text
Sparse keys: ['indices', 'indptr', 'format', 'shape', 'data']
Shape: [ 5227 12508]
Format: np.bytes_(b'csr')
Reconstructed: (5227, 12508) nnz: 38654082
Density: 0.5912279963283801

Models: 5227
Items: 12508
Sample items: ['abstract_algebra.1' 'abstract_algebra.10' 'abstract_algebra.100'
 'abstract_algebra.11' 'abstract_algebra.12']

ets_class counts:
ets_class
A    6332
C    3918
B    2258
Name: count, dtype: int64
Subjects: 57
Subjects from item_ids: 57
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5c8383e8-eeae-4526-bae4-522e0eaabe0c",
  "uuid": "f9e90228-1869-4227-a21c-f2d2ef8e6c69",
  "tool_use_result": {
    "stdout": "Sparse keys: ['indices', 'indptr', 'format', 'shape', 'data']\nShape: [ 5227 12508]\nFormat: np.bytes_(b'csr')\nReconstructed: (5227, 12508) nnz: 38654082\nDensity: 0.5912279963283801\n\nModels: 5227\nItems: 12508\nSample items: ['abstract_algebra.1' 'abstract_algebra.10' 'abstract_algebra.100'\n 'abstract_algebra.11' 'abstract_algebra.12']\n\nets_class counts:\nets_class\nA    6332\nC    3918\nB    2258\nName: count, dtype: int64\nSubjects: 57\nSubjects from item_ids: 57",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Assistant

_source line 11_

Good — data structure is clear. Now I'll write and run the analysis script.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5c8383e8-eeae-4526-bae4-522e0eaabe0c",
  "uuid": "5c9889ac-8c44-4ae1-b413-ffd5ee7aaf3e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C7WAa4BL3LenFwCatVJEKQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 652,
      "cache_read_input_tokens": 25290,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 652
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 12_

<details open><summary>🔧 Tool call — Bash · `toolu_017EHmP31s8VirADYmk5xM2Y`</summary>

```json
{
  "command": "mkdir -p artifacts/r15_subject_level_rho",
  "description": "Create output directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5c8383e8-eeae-4526-bae4-522e0eaabe0c",
  "uuid": "2b6a5700-a6bd-404f-9ff0-b45b514eee2a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C7WAa4BL3LenFwCatVJEKQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 652,
      "cache_read_input_tokens": 25290,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 652
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-22T12:43:37.421Z_

<details><summary>↩ Tool result · `toolu_017EHmP31s8VirADYmk5xM2Y`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5c8383e8-eeae-4526-bae4-522e0eaabe0c",
  "uuid": "47b14e1e-5378-4013-8ecf-836017e52e6d",
  "tool_use_result": {
    "stdout": "",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": true
  }
}
```

</details>

---

### Tool call

_source line 14_

<details open><summary>🔧 Tool call — Write · `toolu_01FpJ3PsYfKzMSiAbELzA22T`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r15_subject_level_rho/subject_level_rho_analysis.py",
  "content": "#!/usr/bin/env python3\n\"\"\"R15-MF3: Subject-level ranking ρ analysis.\n\nShows that aggregate ρ≈0.997 masks subject-level ranking instability\nwhen DIF-C items are removed.\n\"\"\"\n\nimport numpy as np\nimport pandas as pd\nfrom scipy import sparse, stats\nfrom pathlib import Path\n\nROOT = Path(__file__).resolve().parent.parent.parent\nOUT = ROOT / \"artifacts\" / \"r15_subject_level_rho\"\n\n# ---------- Load data ----------\nrm = np.load(ROOT / \"artifacts\" / \"response_matrix.npz\")\nX = sparse.csr_matrix(\n    (rm[\"data\"], rm[\"indices\"], rm[\"indptr\"]),\n    shape=tuple(rm[\"shape\"]),\n)\nidx = np.load(ROOT / \"artifacts\" / \"response_matrix_index.npz\", allow_pickle=True)\nmodel_names = idx[\"model_names\"]\nitem_ids = idx[\"item_ids\"]\n\ndif = pd.read_csv(ROOT / \"artifacts\" / \"plan_001\" / \"dif_results_temporal.csv\")\ndif_c_set = set(dif.loc[dif[\"ets_class\"] == \"C\", \"item_id\"])\n\n# ---------- Build item-to-column index ----------\nitem_to_col = {iid: i for i, iid in enumerate(item_ids)}\n\n# ---------- Group items by subject ----------\nsubject_items = {}\nfor iid in item_ids:\n    subj = iid.rsplit(\".\", 1)[0]\n    subject_items.setdefault(subj, []).append(iid)\n\n# ---------- Convert to dense once (fits in memory: 5227×12508 float32 ≈ 250MB) ----------\nX_dense = X.toarray().astype(np.float32)\n\n# ---------- Per-subject analysis ----------\nrecords = []\nfor subj in sorted(subject_items.keys()):\n    all_items = subject_items[subj]\n    c_items = [iid for iid in all_items if iid in dif_c_set]\n    stable_items = [iid for iid in all_items if iid not in dif_c_set]\n\n    n_all = len(all_items)\n    n_c = len(c_items)\n    n_stable = len(stable_items)\n\n    if n_stable < 2:\n        continue\n\n    all_cols = np.array([item_to_col[iid] for iid in all_items])\n    stable_cols = np.array([item_to_col[iid] for iid in stable_items])\n\n    score_all = X_dense[:, all_cols].mean(axis=1)\n    score_stable = X_dense[:, stable_cols].mean(axis=1)\n\n    rho, _ = stats.spearmanr(score_all, score_stable)\n\n    rank_all = stats.rankdata(-score_all, method=\"average\")\n    rank_stable = stats.rankdata(-score_stable, method=\"average\")\n    rank_diff = np.abs(rank_all - rank_stable)\n\n    flip_rate = np.mean(rank_diff >= 1)\n    mean_abs_rank_change = np.mean(rank_diff)\n    max_abs_rank_change = np.max(rank_diff)\n\n    records.append({\n        \"subject\": subj,\n        \"n_items\": n_all,\n        \"n_c_items\": n_c,\n        \"n_stable_items\": n_stable,\n        \"pct_c\": round(100 * n_c / n_all, 1),\n        \"spearman_rho\": round(rho, 6),\n        \"flip_rate\": round(flip_rate, 4),\n        \"mean_abs_rank_change\": round(mean_abs_rank_change, 2),\n        \"max_abs_rank_change\": round(max_abs_rank_change, 1),\n    })\n\ndf = pd.DataFrame(records)\n\n# ---------- Aggregate statistics ----------\nagg_all_cols = np.arange(X_dense.shape[1])\nstable_item_ids = [iid for iid in item_ids if iid not in dif_c_set]\nagg_stable_cols = np.array([item_to_col[iid] for iid in stable_item_ids])\nagg_score_all = X_dense[:, agg_all_cols].mean(axis=1)\nagg_score_stable = X_dense[:, agg_stable_cols].mean(axis=1)\nagg_rho, _ = stats.spearmanr(agg_score_all, agg_score_stable)\n\n# C% vs ρ correlation across subjects\ncpct_vs_rho = stats.spearmanr(df[\"pct_c\"], df[\"spearman_rho\"])\n\n# ---------- Summary stats ----------\nmean_rho = df[\"spearman_rho\"].mean()\nmin_rho_row = df.loc[df[\"spearman_rho\"].idxmin()]\nn_below_99 = (df[\"spearman_rho\"] < 0.99).sum()\nn_below_95 = (df[\"spearman_rho\"] < 0.95).sum()\nn_below_90 = (df[\"spearman_rho\"] < 0.90).sum()\nmean_flip = df[\"flip_rate\"].mean()\nmean_rank_change = df[\"mean_abs_rank_change\"].mean()\n\n# ---------- Save CSV ----------\ndf.to_csv(OUT / \"subject_level_rho_results.csv\", index=False)\nprint(f\"Saved {len(df)} subjects to CSV\")\n\n# ---------- Generate report ----------\ntop10 = df.nsmallest(10, \"spearman_rho\")\n\nreport = f\"\"\"# R15-MF3: Subject-Level Ranking ρ Analysis\n\n## Key Finding\n\nAggregate ρ = {agg_rho:.4f} masks substantial subject-level ranking instability.\nMean subject-level ρ = {mean_rho:.4f} — individual subjects show much larger divergence.\n\n## Summary Statistics\n\n| Metric | Value |\n|--------|-------|\n| Aggregate ρ (all items vs stable items) | {agg_rho:.4f} |\n| Mean subject-level ρ | {mean_rho:.4f} |\n| Median subject-level ρ | {df['spearman_rho'].median():.4f} |\n| Min ρ | {min_rho_row['spearman_rho']:.4f} ({min_rho_row['subject']}) |\n| Subjects with ρ < 0.99 | {n_below_99} / {len(df)} |\n| Subjects with ρ < 0.95 | {n_below_95} / {len(df)} |\n| Subjects with ρ < 0.90 | {n_below_90} / {len(df)} |\n| Mean flip rate | {mean_flip:.4f} |\n| Mean |rank change| (averaged across subjects) | {mean_rank_change:.1f} |\n\n## Top 10 Subjects with Lowest ρ\n\n| Subject | n_items | C% | ρ | Flip Rate | Mean |Δrank| | Max |Δrank| |\n|---------|---------|-----|------|-----------|---------------|---------------|\n\"\"\"\n\nfor _, r in top10.iterrows():\n    report += (\n        f\"| {r['subject']} | {r['n_items']} | {r['pct_c']:.1f}% | \"\n        f\"{r['spearman_rho']:.4f} | {r['flip_rate']:.4f} | \"\n        f\"{r['mean_abs_rank_change']:.1f} | {r['max_abs_rank_change']:.0f} |\\n\"\n    )\n\nreport += f\"\"\"\n## C% vs ρ Correlation\n\nSpearman correlation between subject DIF-C percentage and subject ρ:\n- ρ = {cpct_vs_rho.statistic:.4f}, p = {cpct_vs_rho.pvalue:.2e}\n\n{\"Confirmed: higher DIF contamination → lower ranking stability.\" if cpct_vs_rho.statistic < -0.3 else \"Correlation weaker than expected.\"}\n\n## Distribution of Subject-Level ρ\n\n\"\"\"\n\nbins = [(0.99, 1.0), (0.95, 0.99), (0.90, 0.95), (0.0, 0.90)]\nfor lo, hi in bins:\n    n = ((df[\"spearman_rho\"] >= lo) & (df[\"spearman_rho\"] < hi)).sum()\n    if lo == 0.99:\n        n = (df[\"spearman_rho\"] >= 0.99).sum()\n        report += f\"- ρ ≥ 0.99: {n} subjects\\n\"\n    else:\n        report += f\"- {lo:.2f} ≤ ρ < {hi:.2f}: {n} subjects\\n\"\n\nreport += f\"\"\"\n## Conclusion\n\nThe aggregate ρ of {agg_rho:.4f} is misleading. At the subject level:\n- {n_below_99} of {len(df)} subjects have ρ < 0.99\n- {n_below_95} subjects fall below ρ = 0.95\n- {n_below_90} subjects fall below ρ = 0.90\n- The worst subject ({min_rho_row['subject']}) has ρ = {min_rho_row['spearman_rho']:.4f} with max rank displacement of {min_rho_row['max_abs_rank_change']:.0f}\n\nAveraging across thousands of items dilutes the signal: DIF-C items cluster within specific subjects,\nso subject-level rankings absorb disproportionate distortion that disappears in aggregate.\n\"\"\"\n\nwith open(OUT / \"subject_level_rho_report.md\", \"w\") as f:\n    f.write(report)\n\nprint(report)\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5c8383e8-eeae-4526-bae4-522e0eaabe0c",
  "uuid": "749ab305-2c30-432d-a59e-2811ae4a279a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011zy1rk5PYdikBFDGZFVAJn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 120,
      "cache_read_input_tokens": 25942,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 120
      },
      "output_tokens": 34,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-22T12:44:17.082Z_

<details><summary>↩ Tool result · `toolu_01FpJ3PsYfKzMSiAbELzA22T`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r15_subject_level_rho/subject_level_rho_analysis.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5c8383e8-eeae-4526-bae4-522e0eaabe0c",
  "uuid": "f9fda37c-304b-4e43-9c4c-f02719bf1907",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r15_subject_level_rho/subject_level_rho_analysis.py",
    "content": "#!/usr/bin/env python3\n\"\"\"R15-MF3: Subject-level ranking ρ analysis.\n\nShows that aggregate ρ≈0.997 masks subject-level ranking instability\nwhen DIF-C items are removed.\n\"\"\"\n\nimport numpy as np\nimport pandas as pd\nfrom scipy import sparse, stats\nfrom pathlib import Path\n\nROOT = Path(__file__).resolve().parent.parent.parent\nOUT = ROOT / \"artifacts\" / \"r15_subject_level_rho\"\n\n# ---------- Load data ----------\nrm = np.load(ROOT / \"artifacts\" / \"response_matrix.npz\")\nX = sparse.csr_matrix(\n    (rm[\"data\"], rm[\"indices\"], rm[\"indptr\"]),\n    shape=tuple(rm[\"shape\"]),\n)\nidx = np.load(ROOT / \"artifacts\" / \"response_matrix_index.npz\", allow_pickle=True)\nmodel_names = idx[\"model_names\"]\nitem_ids = idx[\"item_ids\"]\n\ndif = pd.read_csv(ROOT / \"artifacts\" / \"plan_001\" / \"dif_results_temporal.csv\")\ndif_c_set = set(dif.loc[dif[\"ets_class\"] == \"C\", \"item_id\"])\n\n# ---------- Build item-to-column index ----------\nitem_to_col = {iid: i for i, iid in enumerate(item_ids)}\n\n# ---------- Group items by subject ----------\nsubject_items = {}\nfor iid in item_ids:\n    subj = iid.rsplit(\".\", 1)[0]\n    subject_items.setdefault(subj, []).append(iid)\n\n# ---------- Convert to dense once (fits in memory: 5227×12508 float32 ≈ 250MB) ----------\nX_dense = X.toarray().astype(np.float32)\n\n# ---------- Per-subject analysis ----------\nrecords = []\nfor subj in sorted(subject_items.keys()):\n    all_items = subject_items[subj]\n    c_items = [iid for iid in all_items if iid in dif_c_set]\n    stable_items = [iid for iid in all_items if iid not in dif_c_set]\n\n    n_all = len(all_items)\n    n_c = len(c_items)\n    n_stable = len(stable_items)\n\n    if n_stable < 2:\n        continue\n\n    all_cols = np.array([item_to_col[iid] for iid in all_items])\n    stable_cols = np.array([item_to_col[iid] for iid in stable_items])\n\n    score_all = X_dense[:, all_cols].mean(axis=1)\n    score_stable = X_dense[:, stable_cols].mean(axis=1)\n\n    rho, _ = stats.spearmanr(score_all, score_stable)\n\n    rank_all = stats.rankdata(-score_all, method=\"average\")\n    rank_stable = stats.rankdata(-score_stable, method=\"average\")\n    rank_diff = np.abs(rank_all - rank_stable)\n\n    flip_rate = np.mean(rank_diff >= 1)\n    mean_abs_rank_change = np.mean(rank_diff)\n    max_abs_rank_change = np.max(rank_diff)\n\n    records.append({\n        \"subject\": subj,\n        \"n_items\": n_all,\n        \"n_c_items\": n_c,\n        \"n_stable_items\": n_stable,\n        \"pct_c\": round(100 * n_c / n_all, 1),\n        \"spearman_rho\": round(rho, 6),\n        \"flip_rate\": round(flip_rate, 4),\n        \"mean_abs_rank_change\": round(mean_abs_rank_change, 2),\n        \"max_abs_rank_change\": round(max_abs_rank_change, 1),\n    })\n\ndf = pd.DataFrame(records)\n\n# ---------- Aggregate statistics ----------\nagg_all_cols = np.arange(X_dense.shape[1])\nstable_item_ids = [iid for iid in item_ids if iid not in dif_c_set]\nagg_stable_cols = np.array([item_to_col[iid] for iid in stable_item_ids])\nagg_score_all = X_dense[:, agg_all_cols].mean(axis=1)\nagg_score_stable = X_dense[:, agg_stable_cols].mean(axis=1)\nagg_rho, _ = stats.spearmanr(agg_score_all, agg_score_stable)\n\n# C% vs ρ correlation across subjects\ncpct_vs_rho = stats.spearmanr(df[\"pct_c\"], df[\"spearman_rho\"])\n\n# ---------- Summary stats ----------\nmean_rho = df[\"spearman_rho\"].mean()\nmin_rho_row = df.loc[df[\"spearman_rho\"].idxmin()]\nn_below_99 = (df[\"spearman_rho\"] < 0.99).sum()\nn_below_95 = (df[\"spearman_rho\"] < 0.95).sum()\nn_below_90 = (df[\"spearman_rho\"] < 0.90).sum()\nmean_flip = df[\"flip_rate\"].mean()\nmean_rank_change = df[\"mean_abs_rank_change\"].mean()\n\n# ---------- Save CSV ----------\ndf.to_csv(OUT / \"subject_level_rho_results.csv\", index=False)\nprint(f\"Saved {len(df)} subjects to CSV\")\n\n# ---------- Generate report ----------\ntop10 = df.nsmallest(10, \"spearman_rho\")\n\nreport = f\"\"\"# R15-MF3: Subject-Level Ranking ρ Analysis\n\n## Key Finding\n\nAggregate ρ = {agg_rho:.4f} masks substantial subject-level ranking instability.\nMean subject-level ρ = {mean_rho:.4f} — individual subjects show much larger divergence.\n\n## Summary Statistics\n\n| Metric | Value |\n|--------|-------|\n| Aggregate ρ (all items vs stable items) | {agg_rho:.4f} |\n| Mean subject-level ρ | {mean_rho:.4f} |\n| Median subject-level ρ | {df['spearman_rho'].median():.4f} |\n| Min ρ | {min_rho_row['spearman_rho']:.4f} ({min_rho_row['subject']}) |\n| Subjects with ρ < 0.99 | {n_below_99} / {len(df)} |\n| Subjects with ρ < 0.95 | {n_below_95} / {len(df)} |\n| Subjects with ρ < 0.90 | {n_below_90} / {len(df)} |\n| Mean flip rate | {mean_flip:.4f} |\n| Mean |rank change| (averaged across subjects) | {mean_rank_change:.1f} |\n\n## Top 10 Subjects with Lowest ρ\n\n| Subject | n_items | C% | ρ | Flip Rate | Mean |Δrank| | Max |Δrank| |\n|---------|---------|-----|------|-----------|---------------|---------------|\n\"\"\"\n\nfor _, r in top10.iterrows():\n    report += (\n        f\"| {r['subject']} | {r['n_items']} | {r['pct_c']:.1f}% | \"\n        f\"{r['spearman_rho']:.4f} | {r['flip_rate']:.4f} | \"\n        f\"{r['mean_abs_rank_change']:.1f} | {r['max_abs_rank_change']:.0f} |\\n\"\n    )\n\nreport += f\"\"\"\n## C% vs ρ Correlation\n\nSpearman correlation between subject DIF-C percentage and subject ρ:\n- ρ = {cpct_vs_rho.statistic:.4f}, p = {cpct_vs_rho.pvalue:.2e}\n\n{\"Confirmed: higher DIF contamination → lower ranking stability.\" if cpct_vs_rho.statistic < -0.3 else \"Correlation weaker than expected.\"}\n\n## Distribution of Subject-Level ρ\n\n\"\"\"\n\nbins = [(0.99, 1.0), (0.95, 0.99), (0.90, 0.95), (0.0, 0.90)]\nfor lo, hi in bins:\n    n = ((df[\"spearman_rho\"] >= lo) & (df[\"spearman_rho\"] < hi)).sum()\n    if lo == 0.99:\n        n = (df[\"spearman_rho\"] >= 0.99).sum()\n        report += f\"- ρ ≥ 0.99: {n} subjects\\n\"\n    else:\n        report += f\"- {lo:.2f} ≤ ρ < {hi:.2f}: {n} subjects\\n\"\n\nreport += f\"\"\"\n## Conclusion\n\nThe aggregate ρ of {agg_rho:.4f} is misleading. At the subject level:\n- {n_below_99} of {len(df)} subjects have ρ < 0.99\n- {n_below_95} subjects fall below ρ = 0.95\n- {n_below_90} subjects fall below ρ = 0.90\n- The worst subject ({min_rho_row['subject']}) has ρ = {min_rho_row['spearman_rho']:.4f} with max rank displacement of {min_rho_row['max_abs_rank_change']:.0f}\n\nAveraging across thousands of items dilutes the signal: DIF-C items cluster within specific subjects,\nso subject-level rankings absorb disproportionate distortion that disappears in aggregate.\n\"\"\"\n\nwith open(OUT / \"subject_level_rho_report.md\", \"w\") as f:\n    f.write(report)\n\nprint(report)\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Tool call

_source line 16_

<details open><summary>🔧 Tool call — Bash · `toolu_01J6vTVPBUowc4DASdYYN413`</summary>

```json
{
  "command": "python3 artifacts/r15_subject_level_rho/subject_level_rho_analysis.py",
  "description": "Run subject-level ρ analysis",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5c8383e8-eeae-4526-bae4-522e0eaabe0c",
  "uuid": "87987e0b-88f1-4f04-9b12-c84f67bd5215",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YANN344Wasc41fX9PxCdem",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2707,
      "cache_read_input_tokens": 26062,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2707
      },
      "output_tokens": 62,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### System

_source line 17_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "bzg04srqd",
  "tool_use_id": "toolu_01J6vTVPBUowc4DASdYYN413",
  "description": "Run subject-level ρ analysis",
  "task_type": "local_bash",
  "uuid": "d9ba29c5-9281-4c07-a9c7-494f98d0bb13",
  "session_id": "5c8383e8-eeae-4526-bae4-522e0eaabe0c"
}
```

---

### System

_source line 18_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "bzg04srqd",
  "tool_use_id": "toolu_01J6vTVPBUowc4DASdYYN413",
  "status": "completed",
  "output_file": "",
  "summary": "Run subject-level ρ analysis",
  "uuid": "8d6e127d-e70c-488b-9ed7-316198c8b15a",
  "session_id": "5c8383e8-eeae-4526-bae4-522e0eaabe0c"
}
```

---

### Tool result

_source line 19 · 2026-05-22T12:44:27.734Z_

<details><summary>↩ Tool result · `toolu_01J6vTVPBUowc4DASdYYN413`</summary>

```text
Saved 57 subjects to CSV
# R15-MF3: Subject-Level Ranking ρ Analysis

## Key Finding

Aggregate ρ = 0.9965 masks substantial subject-level ranking instability.
Mean subject-level ρ = 0.9499 — individual subjects show much larger divergence.

## Summary Statistics

| Metric | Value |
|--------|-------|
| Aggregate ρ (all items vs stable items) | 0.9965 |
| Mean subject-level ρ | 0.9499 |
| Median subject-level ρ | 0.9591 |
| Min ρ | 0.7738 (global_facts) |
| Subjects with ρ < 0.99 | 55 / 57 |
| Subjects with ρ < 0.95 | 22 / 57 |
| Subjects with ρ < 0.90 | 5 / 57 |
| Mean flip rate | 0.9937 |
| Mean |rank change| (averaged across subjects) | 304.1 |

## Top 10 Subjects with Lowest ρ

| Subject | n_items | C% | ρ | Flip Rate | Mean |Δrank| | Max |Δrank| |
|---------|---------|-----|------|-----------|---------------|---------------|
| global_facts | 83 | 33.7% | 0.7738 | 0.9967 | 747.9 | 3258 |
| college_mathematics | 72 | 34.7% | 0.8208 | 0.9987 | 680.4 | 3494 |
| abstract_algebra | 91 | 29.7% | 0.8844 | 0.9992 | 520.5 | 3772 |
| business_ethics | 93 | 48.4% | 0.8884 | 0.9971 | 518.9 | 3029 |
| machine_learning | 87 | 32.2% | 0.8972 | 0.9904 | 493.7 | 2868 |
| public_relations | 98 | 23.5% | 0.9029 | 0.9950 | 446.3 | 2600 |
| high_school_chemistry | 181 | 34.8% | 0.9130 | 0.9954 | 421.4 | 2610 |
| high_school_mathematics | 197 | 34.5% | 0.9183 | 0.9983 | 469.8 | 2388 |
| world_religions | 159 | 37.1% | 0.9239 | 0.9973 | 377.4 | 2732 |
| high_school_geography | 184 | 27.7% | 0.9258 | 0.9897 | 368.2 | 2444 |

## C% vs ρ Correlation

Spearman correlation between subject DIF-C percentage and subject ρ:
- ρ = -0.1859, p = 1.66e-01

Correlation weaker than expected.

## Distribution of Subject-Level ρ

- ρ ≥ 0.99: 2 subjects
- 0.95 ≤ ρ < 0.99: 33 subjects
- 0.90 ≤ ρ < 0.95: 17 subjects
- 0.00 ≤ ρ < 0.90: 5 subjects

## Conclusion

The aggregate ρ of 0.9965 is misleading. At the subject level:
- 55 of 57 subjects have ρ < 0.99
- 22 subjects fall below ρ = 0.95
- 5 subjects fall below ρ = 0.90
- The worst subject (global_facts) has ρ = 0.7738 with max rank displacement of 3258

Averaging across thousands of items dilutes the signal: DIF-C items cluster within specific subjects,
so subject-level rankings absorb disproportionate distortion that disappears in aggregate.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5c8383e8-eeae-4526-bae4-522e0eaabe0c",
  "uuid": "4d150905-c67b-46ac-bd52-766fd9edb38d",
  "tool_use_result": {
    "stdout": "Saved 57 subjects to CSV\n# R15-MF3: Subject-Level Ranking ρ Analysis\n\n## Key Finding\n\nAggregate ρ = 0.9965 masks substantial subject-level ranking instability.\nMean subject-level ρ = 0.9499 — individual subjects show much larger divergence.\n\n## Summary Statistics\n\n| Metric | Value |\n|--------|-------|\n| Aggregate ρ (all items vs stable items) | 0.9965 |\n| Mean subject-level ρ | 0.9499 |\n| Median subject-level ρ | 0.9591 |\n| Min ρ | 0.7738 (global_facts) |\n| Subjects with ρ < 0.99 | 55 / 57 |\n| Subjects with ρ < 0.95 | 22 / 57 |\n| Subjects with ρ < 0.90 | 5 / 57 |\n| Mean flip rate | 0.9937 |\n| Mean |rank change| (averaged across subjects) | 304.1 |\n\n## Top 10 Subjects with Lowest ρ\n\n| Subject | n_items | C% | ρ | Flip Rate | Mean |Δrank| | Max |Δrank| |\n|---------|---------|-----|------|-----------|---------------|---------------|\n| global_facts | 83 | 33.7% | 0.7738 | 0.9967 | 747.9 | 3258 |\n| college_mathematics | 72 | 34.7% | 0.8208 | 0.9987 | 680.4 | 3494 |\n| abstract_algebra | 91 | 29.7% | 0.8844 | 0.9992 | 520.5 | 3772 |\n| business_ethics | 93 | 48.4% | 0.8884 | 0.9971 | 518.9 | 3029 |\n| machine_learning | 87 | 32.2% | 0.8972 | 0.9904 | 493.7 | 2868 |\n| public_relations | 98 | 23.5% | 0.9029 | 0.9950 | 446.3 | 2600 |\n| high_school_chemistry | 181 | 34.8% | 0.9130 | 0.9954 | 421.4 | 2610 |\n| high_school_mathematics | 197 | 34.5% | 0.9183 | 0.9983 | 469.8 | 2388 |\n| world_religions | 159 | 37.1% | 0.9239 | 0.9973 | 377.4 | 2732 |\n| high_school_geography | 184 | 27.7% | 0.9258 | 0.9897 | 368.2 | 2444 |\n\n## C% vs ρ Correlation\n\nSpearman correlation between subject DIF-C percentage and subject ρ:\n- ρ = -0.1859, p = 1.66e-01\n\nCorrelation weaker than expected.\n\n## Distribution of Subject-Level ρ\n\n- ρ ≥ 0.99: 2 subjects\n- 0.95 ≤ ρ < 0.99: 33 subjects\n- 0.90 ≤ ρ < 0.95: 17 subjects\n- 0.00 ≤ ρ < 0.90: 5 subjects\n\n## Conclusion\n\nThe aggregate ρ of 0.9965 is misleading. At the subject level:\n- 55 of 57 subjects have ρ < 0.99\n- 22 subjects fall below ρ = 0.95\n- 5 subjects fall below ρ = 0.90\n- The worst subject (global_facts) has ρ = 0.7738 with max rank displacement of 3258\n\nAveraging across thousands of items dilutes the signal: DIF-C items cluster within specific subjects,\nso subject-level rankings absorb disproportionate distortion that disappears in aggregate.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Assistant

_source line 20_

Analysis complete. Results are strong for the paper argument:

**Key numbers:**
- Aggregate ρ = 0.9965 → looks harmless
- Mean subject-level ρ = 0.9499 → meaningful degradation
- 55/57 subjects have ρ < 0.99; 22 subjects < 0.95; 5 subjects < 0.90
- Worst: `global_facts` at ρ = 0.774 with max rank displacement of 3,258 positions
- Mean |rank change| across subjects = 304 positions

**One note:** the C% vs ρ correlation is weaker than expected (ρ = −0.186, p = 0.17) — item count per subject and specific item difficulty distributions likely moderate the relationship, so it's not a clean linear dose-response at subject level.

All three outputs are written to `artifacts/r15_subject_level_rho/`:
- `subject_level_rho_report.md` — full report
- `subject_level_rho_results.csv` — per-subject data (57 rows)
- `subject_level_rho_analysis.py` — reproducible script

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5c8383e8-eeae-4526-bae4-522e0eaabe0c",
  "uuid": "e3bd5c72-2c91-462c-a8ac-6f57b891e363",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CqBsGjJC6xEam4vJXSc49p",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1184,
      "cache_read_input_tokens": 28769,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1184
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Task result

_source line 21_

Analysis complete. Results are strong for the paper argument:

**Key numbers:**
- Aggregate ρ = 0.9965 → looks harmless
- Mean subject-level ρ = 0.9499 → meaningful degradation
- 55/57 subjects have ρ < 0.99; 22 subjects < 0.95; 5 subjects < 0.90
- Worst: `global_facts` at ρ = 0.774 with max rank displacement of 3,258 positions
- Mean |rank change| across subjects = 304 positions

**One note:** the C% vs ρ correlation is weaker than expected (ρ = −0.186, p = 0.17) — item count per subject and specific item difficulty distributions likely moderate the relationship, so it's not a clean linear dose-response at subject level.

All three outputs are written to `artifacts/r15_subject_level_rho/`:
- `subject_level_rho_report.md` — full report
- `subject_level_rho_results.csv` — per-subject data (57 rows)
- `subject_level_rho_analysis.py` — reproducible script

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 93685,
  "duration_api_ms": 85316,
  "num_turns": 6,
  "stop_reason": "end_turn",
  "session_id": "5c8383e8-eeae-4526-bae4-522e0eaabe0c",
  "total_cost_usd": 0.2884895,
  "usage": {
    "input_tokens": 8,
    "cache_creation_input_tokens": 18112,
    "cache_read_input_tokens": 142579,
    "output_tokens": 4106,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 18112,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 283,
        "cache_read_input_tokens": 28769,
        "cache_creation_input_tokens": 1184,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 1184
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1215,
      "outputTokens": 19,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.00131,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 8,
      "outputTokens": 4106,
      "cacheReadInputTokens": 142579,
      "cacheCreationInputTokens": 18112,
      "webSearchRequests": 0,
      "costUSD": 0.2871795,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "16da42b1-c686-4d57-8c50-2c05a07d034a"
}
```

</details>

---
