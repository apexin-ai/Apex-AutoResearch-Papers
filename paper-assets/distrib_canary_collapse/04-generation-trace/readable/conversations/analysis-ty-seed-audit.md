# analysis ty seed audit

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 97
- **Recorded user turns:** 0
- **Tool calls:** 48
- **Original source:** `logs/chats/worker_analysis_ty_seed_audit_20260515T235823.jsonl`
- **Structured JSON:** [`dd3bc0fa8337f383342a.json`](../../sessions/dd/dd3bc0fa8337f383342a.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

97 recorded events

### Tool call

_source line 1 · 2026-05-16T00:06:21.088559+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__detect_image,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__read_project_file",
  "max_results": "6"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_ty_seed_audit_20260515T235823",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__detect_image,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__read_project_file",
    "max_results": "6"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-16T00:06:21.088838+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_ty_seed_audit_20260515T235823",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-16T00:06:21.089010+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "ls /root/autodl-tmp/distrib_canary_collapse/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_ty_seed_audit_20260515T235823",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "ls /root/autodl-tmp/distrib_canary_collapse/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-16T00:06:21.089153+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"__pycache__\\nalpha_sweep_queue.md\\nanalysis\\nanalyze_alpha_sweep.py\\nanalyze_extended.py\\nanalyze_mvp.py\\nbootstrap_ty_validation.py\\nconsensus_framework.py\\ncross_alpha_analysis.py\\ncross_alpha_analysis_v4.py\\ncross_alpha_v3_analysis.py\\ndata\\ndebug_ty.py\\ndetrending_utils.py\\ndmax_sensitivity.py\\nextract_drift.py\\ngen_dose_response.py\\niterative_train.py\\niterative_train.py.bak.mvp\\niterative_train.py.bak.v2\\nleadlag_gpt2m_s42.py\\nlogs\\nmethod_ablation.py\\nmethod_ablation_phase2.py\\nmetrics.py\\npermutation_granger.py\\npooled_panel_analysis.py\\nprepare_c4.py\\nprepare_c4_v2.py\\nprepare_c4_v3.py\\nprepare_c4_v4.py\\nprepare_data.py\\nresults\\nresume_plan006_s42.py\\nrun_mvp.sh\\nrun_verify.sh\\nwindow_sensitivity.py\\nwindow_sensitivity_report.md\\nwindow_sensitivity_v2.py\\nwindow_sensitivity_v3.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.94}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_ty_seed_audit_20260515T235823",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-16T00:06:21.089312+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "find /root/autodl-tmp/distrib_canary_collapse/ -name \"*.py\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_ty_seed_audit_20260515T235823",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "find /root/autodl-tmp/distrib_canary_collapse/ -name \"*.py\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-16T00:06:21.089453+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "find /root/autodl-tmp/distrib_canary_collapse/ -name \"*.csv\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_ty_seed_audit_20260515T235823",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "find /root/autodl-tmp/distrib_canary_collapse/ -name \"*.csv\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-16T00:06:21.089596+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/distrib_canary_collapse/metrics.py\\n/root/autodl-tmp/distrib_canary_collapse/iterative_train.py\\n/root/autodl-tmp/distrib_canary_collapse/prepare_data.py\\n/root/autodl-tmp/distrib_canary_collapse/analyze_mvp.py\\n/root/autodl-tmp/distrib_canary_collapse/method_ablation.py\\n/root/autodl-tmp/distrib_canary_collapse/dmax_sensitivity.py\\n/root/autodl-tmp/distrib_canary_collapse/analyze_alpha_sweep.py\\n/root/autodl-tmp/distrib_canary_collapse/bootstrap_ty_validation.py\\n/root/autodl-tmp/distrib_canary_collapse/detrending_utils.py\\n/root/autodl-tmp/distrib_canary_collapse/analysis/detrending_utils.py\\n/root/autodl-tmp/distrib_canary_collapse/permutation_granger.py\\n/root/autodl-tmp/distrib_canary_collapse/analyze_extended.py\\n/root/autodl-tmp/distrib_canary_collapse/pooled_panel_analysis.py\\n/root/autodl-tmp/distrib_canary_collapse/extract_drift.py\\n/root/autodl-tmp/distrib_canary_collapse/gen_dose_response.py\\n/root/autodl-tmp/distrib_canary_collapse/cross_alpha_analysis.py\\n/root/autodl-tmp/distrib_canary_collapse/cross_alpha_v3_analysis.py\\n/root/autodl-tmp/distrib_canary_collapse/prepare_c4.py\\n/root/autodl-tmp/distrib_canary_collapse/consensus_framework.py\\n/root/autodl-tmp/distrib_canary_collapse/prepare_c4_v2.py\\n/root/autodl-tmp/distrib_canary_collapse/prepare_c4_v3.py\\n/root/autodl-tmp/distrib_canary_collapse/prepare_c4_v4.py\\n/root/autodl-tmp/distrib_canary_collapse/method_ablation_phase2.py\\n/root/autodl-tmp/distrib_canary_collapse/cross_alpha_analysis_v4.py\\n/root/autodl-tmp/distrib_canary_collapse/resume_plan006_s42.py\\n/root/autodl-tmp/distrib_canary_collapse/leadlag_gpt2m_s42.py\\n/root/autodl-tmp/distrib_canary_collapse/window_sensitivity.py\\n/root/autodl-tmp/distrib_canary_collapse/debug_ty.py\\n/root/autodl-tmp/distrib_canary_collapse/window_sensitivity_v2.py\\n/root/autodl-tmp/distrib_canary_collapse/window_sensitivity_v3.py\\n\", \"stderr\": \"\", \"return
…[truncated 73 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_ty_seed_audit_20260515T235823",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-16T00:06:21.089748+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/distrib_canary_collapse/results/mvp/analysis/lead_time_table.csv\\n/root/autodl-tmp/distrib_canary_collapse/results/mvp/analysis_maxlag5_backup/lead_time_table.csv\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep_analysis/phase_diagram.csv\\n/root/autodl-tmp/distrib_canary_collapse/results/dose_response_drift.csv\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.53}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_ty_seed_audit_20260515T235823",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-16T00:06:21.089900+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "find /root/autodl-tmp/distrib_canary_collapse/data/ -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_ty_seed_audit_20260515T235823",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "find /root/autodl-tmp/distrib_canary_collapse/data/ -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-16T00:06:21.090105+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/distrib_canary_collapse/data/wikitext103/train/data-00000-of-00001.arrow\\n/root/autodl-tmp/distrib_canary_collapse/data/wikitext103/train/state.json\\n/root/autodl-tmp/distrib_canary_collapse/data/wikitext103/train/dataset_info.json\\n/root/autodl-tmp/distrib_canary_collapse/data/wikitext103/eval/data-00000-of-00001.arrow\\n/root/autodl-tmp/distrib_canary_collapse/data/wikitext103/eval/state.json\\n/root/autodl-tmp/distrib_canary_collapse/data/wikitext103/eval/dataset_info.json\\n/root/autodl-tmp/distrib_canary_collapse/data/wikitext103/prompts/data-00000-of-00001.arrow\\n/root/autodl-tmp/distrib_canary_collapse/data/wikitext103/prompts/state.json\\n/root/autodl-tmp/distrib_canary_collapse/data/wikitext103/prompts/dataset_info.json\\n/root/autodl-tmp/distrib_canary_collapse/data/wikitext103_5k/train/data-00000-of-00001.arrow\\n/root/autodl-tmp/distrib_canary_collapse/data/wikitext103_5k/train/state.json\\n/root/autodl-tmp/distrib_canary_collapse/data/wikitext103_5k/train/dataset_info.json\\n/root/autodl-tmp/distrib_canary_collapse/data/wikitext103_5k/train/cache-cb0a0578d0ae1a3e.arrow\\n/root/autodl-tmp/distrib_canary_collapse/data/wikitext103_5k/train/cache-10c2114ed504cc42.arrow\\n/root/autodl-tmp/distrib_canary_collapse/data/wikitext103_5k/train/cache-7ce5032117e7914e.arrow\\n/root/autodl-tmp/distrib_canary_collapse/data/wikitext103_5k/train/cache-c3d22c02024b88f7.arrow\\n/root/autodl-tmp/distrib_canary_collapse/data/wikitext103_5k/train/cache-4cec26b0fa3200a9.arrow\\n/root/autodl-tmp/distrib_canary_collapse/data/wikitext103_5k/train/cache-971cbd2cd05dbbaf.arrow\\n/root/autodl-tmp/distrib_canary_collapse/data/wikitext103_5k/train/cache-466741fe9c35a7a6.arrow\\n/root/autodl-tmp/distrib_canary_collapse/data/wikitext103_5k/train/cache-5bf92e2b98cbcdd1.arrow\\n/root/autodl-tmp/distrib_canary_collapse/data/wikitext103_5k/train/cache-06aaa7da75c7ea23.arrow\\n/root/autodl-tmp/distrib_canary_collap
…[truncated 6377 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_ty_seed_audit_20260515T235823",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-16T00:06:21.090269+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "find /root/autodl-tmp/distrib_canary_collapse/results/ -type f -name \"*.json\" -o -name \"*.csv\" -o -name \"*.md\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_ty_seed_audit_20260515T235823",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "find /root/autodl-tmp/distrib_canary_collapse/results/ -type f -name \"*.json\" -o -name \"*.csv\" -o -name \"*.md\"",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-16T00:06:21.090400+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "head -80 /root/autodl-tmp/distrib_canary_collapse/method_ablation.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_ty_seed_audit_20260515T235823",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "head -80 /root/autodl-tmp/distrib_canary_collapse/method_ablation.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-16T00:06:21.090585+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/distrib_canary_collapse/results/mvp/rep_42_v1_partial/config.json\\n/root/autodl-tmp/distrib_canary_collapse/results/mvp/rep_42_v1_partial/gen_0/synthetic_data/state.json\\n/root/autodl-tmp/distrib_canary_collapse/results/mvp/rep_42_v1_partial/gen_0/synthetic_data/dataset_info.json\\n/root/autodl-tmp/distrib_canary_collapse/results/mvp/rep_43_v1_partial/config.json\\n/root/autodl-tmp/distrib_canary_collapse/results/mvp/rep_43_v1_partial/gen_0/synthetic_data/state.json\\n/root/autodl-tmp/distrib_canary_collapse/results/mvp/rep_43_v1_partial/gen_0/synthetic_data/dataset_info.json\\n/root/autodl-tmp/distrib_canary_collapse/results/mvp/rep_42/config.json\\n/root/autodl-tmp/distrib_canary_collapse/results/mvp/rep_42/gen_0/synthetic_data/state.json\\n/root/autodl-tmp/distrib_canary_collapse/results/mvp/rep_42/gen_0/synthetic_data/dataset_info.json\\n/root/autodl-tmp/distrib_canary_collapse/results/mvp/rep_42/gen_0/metrics.json\\n/root/autodl-tmp/distrib_canary_collapse/results/mvp/rep_42/gen_1/synthetic_data/state.json\\n/root/autodl-tmp/distrib_canary_collapse/results/mvp/rep_42/gen_1/synthetic_data/dataset_info.json\\n/root/autodl-tmp/distrib_canary_collapse/results/mvp/rep_42/gen_1/checkpoint/config.json\\n/root/autodl-tmp/distrib_canary_collapse/results/mvp/rep_42/gen_1/checkpoint/generation_config.json\\n/root/autodl-tmp/distrib_canary_collapse/results/mvp/rep_42/gen_1/checkpoint/tokenizer_config.json\\n/root/autodl-tmp/distrib_canary_collapse/results/mvp/rep_42/gen_1/checkpoint/special_tokens_map.json\\n/root/autodl-tmp/distrib_canary_collapse/results/mvp/rep_42/gen_1/checkpoint/tokenizer.json\\n/root/autodl-tmp/distrib_canary_collapse/results/mvp/rep_42/gen_1/metrics.json\\n/root/autodl-tmp/distrib_canary_collapse/results/mvp/rep_42/gen_2/synthetic_data/state.json\\n/root/autodl-tmp/distrib_canary_collapse/results/mvp/rep_42/gen_2/synthetic_data/dataset_info.json\\n/root/autodl-tmp/distrib_can
…[truncated 6365 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_ty_seed_audit_20260515T235823",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-16T00:06:21.090810+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Method ablation: compare four lead-lag estimation methods.\\n\\nCompares naive vs robust approaches to detect canary->downstream lead-lag,\\nquantifying the spurious regression rate when non-stationary series are\\ncorrelated without proper detrending.\\n\\nInput:  results/mvp/rep_{seed}/all_metrics.json (seeds 42-45)\\nOutput: results/mvp/analysis/method_ablation.json\\n        (with BH FDR correction and effect sizes)\\n\\nMethods:\\n  1. Naive Pearson lag-correlation (raw levels)\\n  2. Differenced cross-correlation (first-differenced series)\\n  3. Threshold-based lead time (2-sigma onset detection)\\n  4. Toda-Yamamoto augmented-lag Granger causality\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport json\\nimport os\\nimport warnings\\nfrom itertools import product\\n\\nimport numpy as np\\nfrom scipy import stats\\nfrom statsmodels.stats.multitest import multipletests\\nfrom statsmodels.tsa.stattools import adfuller\\nfrom permutation_granger import permutation_granger_test\\n\\nwarnings.filterwarnings(\\\"ignore\\\")\\n\\nCANARY = [\\\"token_entropy\\\", \\\"self_bleu\\\", \\\"ece\\\", \\\"effective_rank\\\"]\\nDOWNSTREAM = [\\\"perplexity\\\", \\\"distinct_1\\\", \\\"distinct_2\\\", \\\"distinct_3\\\"]\\n\\n# Sign conventions: \\\"higher is worse\\\" kept as-is; \\\"lower is worse\\\" negated\\n# so that degradation = positive direction in all analyses.\\nHIGHER_IS_WORSE = {\\\"self_bleu\\\", \\\"ece\\\", \\\"perplexity\\\"}\\nLOWER_IS_WORSE = {\\\"token_entropy\\\", \\\"effective_rank\\\",\\n                   \\\"distinct_1\\\", \\\"distinct_2\\\", \\\"distinct_3\\\"}\\n\\nALPHA = 0.05\\n\\n\\ndef load_metrics(data_dir, seeds):\\n    \\\"\\\"\\\"Load all_metrics.json for each seed.\\\"\\\"\\\"\\n    data = {}\\n    for s in seeds:\\n        path = os.path.join(data_dir, f\\\"rep_{s}\\\", \\\"all_metrics.json\\\")\\n        with open(path) as f:\\n            data[s] = json.load(f)\\n    return 
…[truncated 1260 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_ty_seed_audit_20260515T235823",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-16T00:06:21.091004+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "ls /root/autodl-tmp/distrib_canary_collapse/results/mvp/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_ty_seed_audit_20260515T235823",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "ls /root/autodl-tmp/distrib_canary_collapse/results/mvp/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-16T00:06:21.091138+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"analysis\\nanalysis_dryrun\\nanalysis_maxlag5_backup\\nrep_42\\nrep_42_v1_partial\\nrep_43\\nrep_43_v1_partial\\nrep_44\\nrep_45\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_ty_seed_audit_20260515T235823",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-16T00:06:21.091271+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "python3 -c \"import json; d=json.load(open('/root/autodl-tmp/distrib_canary_collapse/results/mvp/rep_42/all_metrics.json')); print(len(d)); print(json.dumps(d[0], indent=2)); print('---'); print(json.dumps(d[-1], indent=2))\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_ty_seed_audit_20260515T235823",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "python3 -c \"import json; d=json.load(open('/root/autodl-tmp/distrib_canary_collapse/results/mvp/rep_42/all_metrics.json')); print(len(d)); print(json.dumps(d[0], indent=2)); print('---'); print(json.dumps(d[-1], indent=2))\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-16T00:06:21.091400+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_ty_seed_audit_20260515T235823",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-16T00:06:21.091513+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "python3 -c \"import json; d=json.load(open('/root/autodl-tmp/distrib_canary_collapse/results/mvp/rep_42/all_metrics.json')); print([m['generation'] for m in sorted(d, key=lambda x: x['generation'])])\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_ty_seed_audit_20260515T235823",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "python3 -c \"import json; d=json.load(open('/root/autodl-tmp/distrib_canary_collapse/results/mvp/rep_42/all_metrics.json')); print([m['generation'] for m in sorted(d, key=lambda x: x['generation'])])\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-16T00:06:21.091635+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_ty_seed_audit_20260515T235823",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-16T00:06:21.091777+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "cat /root/autodl-tmp/distrib_canary_collapse/results/mvp/rep_42/all_metrics.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_ty_seed_audit_20260515T235823",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "cat /root/autodl-tmp/distrib_canary_collapse/results/mvp/rep_42/all_metrics.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-16T00:06:21.091962+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"[\\n  {\\n    \\\"token_entropy\\\": 3.2341948700181407,\\n    \\\"self_bleu\\\": 0.010194395218435404,\\n    \\\"distinct_1\\\": 0.0982156685333268,\\n    \\\"distinct_2\\\": 0.5178027030111348,\\n    \\\"distinct_3\\\": 0.8127277321747353,\\n    \\\"ece\\\": 0.010804557477709054,\\n    \\\"effective_rank\\\": 46.612774691899155,\\n    \\\"perplexity\\\": 26.948958972544652,\\n    \\\"mauve\\\": 0.03406737671684175,\\n    \\\"generation\\\": 0\\n  },\\n  {\\n    \\\"token_entropy\\\": 1.9084596230213162,\\n    \\\"self_bleu\\\": 0.01031278388147428,\\n    \\\"distinct_1\\\": 0.09752517633628247,\\n    \\\"distinct_2\\\": 0.5140825545933428,\\n    \\\"distinct_3\\\": 0.8103854590526204,\\n    \\\"ece\\\": 0.20417187361498956,\\n    \\\"effective_rank\\\": 79.56989240852776,\\n    \\\"perplexity\\\": 55.948464930758895,\\n    \\\"mauve\\\": 0.03232946507236373,\\n    \\\"generation\\\": 1\\n  },\\n  {\\n    \\\"token_entropy\\\": 1.4804942099201883,\\n    \\\"self_bleu\\\": 0.011490308317431907,\\n    \\\"distinct_1\\\": 0.081484375,\\n    \\\"distinct_2\\\": 0.42797209353198074,\\n    \\\"distinct_3\\\": 0.7098782793481148,\\n    \\\"ece\\\": 0.32288266580453445,\\n    \\\"effective_rank\\\": 95.37208001881726,\\n    \\\"perplexity\\\": 160.41778977682145,\\n    \\\"mauve\\\": 0.030902052851972305,\\n    \\\"generation\\\": 2\\n  },\\n  {\\n    \\\"token_entropy\\\": 1.3802752536019032,\\n    \\\"self_bleu\\\": 0.011848694755297396,\\n    \\\"distinct_1\\\": 0.0758359375,\\n    \\\"distinct_2\\\": 0.38982335799498435,\\n    \\\"distinct_3\\\": 0.6548852325817591,\\n    \\\"ece\\\": 0.35848641042192086,\\n    \\\"effective_rank\\\": 89.96337953045757,\\n    \\\"perplexity\\\": 281.6068229762598,\\n    \\\"mauve\\\": 0.03579527110360478,\\n    \\\"generation\\\": 3\\n  },\\n  {\\n    \\\"token_entropy\\\": 1.3307051448147535,\\n    \\\"self_bleu\\\": 0.012522986760915155,\\n    \\\"distinct_1\\\": 0.0731484375,\\
…[truncated 3073 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_ty_seed_audit_20260515T235823",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-16T00:06:21.092109+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "cat /root/autodl-tmp/distrib_canary_collapse/window_sensitivity.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_ty_seed_audit_20260515T235823",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "cat /root/autodl-tmp/distrib_canary_collapse/window_sensitivity.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-16T00:06:21.092362+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"Observation Window Sensitivity Analysis for Pythia-410M alpha=1.0\\\"\\\"\\\"\\n\\nimport json\\nimport numpy as np\\nfrom scipy import stats\\nfrom statsmodels.tsa.api import VAR\\nfrom statsmodels.stats.multitest import multipletests\\nimport warnings\\nwarnings.filterwarnings('ignore')\\n\\n# ── Config ──\\nSEEDS = [42, 43, 44, 45]\\nWINDOWS = [5, 6, 7, 8, 9, 10]\\nBASE = \\\"/root/autodl-tmp/distrib_canary_collapse/results/mvp\\\"\\nPAIRS = [\\n    (\\\"token_entropy\\\", \\\"distinct_1\\\", \\\"entropy→d1\\\"),\\n    (\\\"token_entropy\\\", \\\"distinct_2\\\", \\\"entropy→d2\\\"),\\n    (\\\"token_entropy\\\", \\\"distinct_3\\\", \\\"entropy→d3\\\"),\\n    (\\\"ece\\\", \\\"distinct_1\\\", \\\"ECE→d1\\\"),\\n    (\\\"ece\\\", \\\"distinct_2\\\", \\\"ECE→d2\\\"),\\n    (\\\"ece\\\", \\\"distinct_3\\\", \\\"ECE→d3\\\"),\\n]\\nN_PERM = 5000\\nFDR_Q = 0.05\\nTHRESHOLD_PCT = 0.10\\n\\n# ── Load data ──\\ndef load_seed(seed):\\n    with open(f\\\"{BASE}/rep_{seed}/all_metrics.json\\\") as f:\\n        return json.load(f)\\n\\nall_data = {s: load_seed(s) for s in SEEDS}\\n\\n# ── Method implementations ──\\n\\ndef naive_xcorr(x, y, max_lag=5):\\n    \\\"\\\"\\\"Pearson cross-correlation at lags 0..max_lag, returns min p-value across lags.\\\"\\\"\\\"\\n    n = len(x)\\n    pvals = []\\n    for lag in range(min(max_lag + 1, n - 2)):\\n        if lag == 0:\\n            r, p = stats.pearsonr(x, y)\\n        else:\\n            r, p = stats.pearsonr(x[:-lag], y[lag:])\\n        if not np.isnan(p):\\n            pvals.append(p)\\n    return pvals\\n\\ndef diff_xcorr(x, y, max_lag=5):\\n    \\\"\\\"\\\"First-differenced cross-correlation.\\\"\\\"\\\"\\n    dx = np.diff(x)\\n    dy = np.diff(y)\\n    n = len(dx)\\n    pvals = []\\n    for lag in range(min(max_lag + 1, n - 2)):\\n        if lag == 0:\\n            r, p = stats.pearsonr(dx, dy)\\n        else:\\n            if len(dx[
…[truncated 7148 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_ty_seed_audit_20260515T235823",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-16T00:06:21.092530+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "cat /root/autodl-tmp/distrib_canary_collapse/debug_ty.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_ty_seed_audit_20260515T235823",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "cat /root/autodl-tmp/distrib_canary_collapse/debug_ty.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-16T00:06:21.092677+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"import numpy as np\\nimport pandas as pd\\nfrom statsmodels.tsa.api import VAR\\nimport json, warnings\\nwarnings.filterwarnings('ignore')\\n\\nwith open(\\\"/root/autodl-tmp/distrib_canary_collapse/results/mvp/rep_42/all_metrics.json\\\") as f:\\n    metrics = json.load(f)\\n\\nx = np.array([m['token_entropy'] for m in metrics[:10]])\\ny = np.array([m['distinct_1'] for m in metrics[:10]])\\n\\ndata = pd.DataFrame({'cause': x, 'effect': y})\\nprint(\\\"Data shape:\\\", data.shape)\\nprint(data)\\n\\nfor p in [1, 2, 3]:\\n    try:\\n        model = VAR(data)\\n        result = model.fit(p)\\n        print(f\\\"\\\\nVAR({p}) fitted, AIC={result.aic:.4f}\\\")\\n        print(\\\"Params shape:\\\", result.params.shape)\\n        print(\\\"Params:\\\\n\\\", result.params)\\n        \\n        # Try different test_causality calls\\n        try:\\n            tr = result.test_causality('effect', ['cause'], kind='wald')\\n            print(f\\\"test_causality('effect', ['cause']): stat={tr.test_statistic:.4f}, p={tr.pvalue:.6f}\\\")\\n        except Exception as e:\\n            print(f\\\"test_causality failed: {e}\\\")\\n        \\n        try:\\n            tr2 = result.test_causality(1, [0], kind='wald')\\n            print(f\\\"test_causality(1, [0]): stat={tr2.test_statistic:.4f}, p={tr2.pvalue:.6f}\\\")\\n        except Exception as e2:\\n            print(f\\\"test_causality(1,[0]) failed: {e2}\\\")\\n            \\n    except Exception as e:\\n        print(f\\\"VAR({p}) failed: {e}\\\")\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_ty_seed_audit_20260515T235823",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-16T00:06:21.092849+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "grep -n \"toda_yamamoto\\|metrics\\[:1\\|T\\+1\\|T \\+1\\|window\\|slice\\|extract\\|gen_\" /root/autodl-tmp/distrib_canary_collapse/method_ablation.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_ty_seed_audit_20260515T235823",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "grep -n \"toda_yamamoto\\|metrics\\[:1\\|T\\+1\\|T \\+1\\|window\\|slice\\|extract\\|gen_\" /root/autodl-tmp/distrib_canary_collapse/method_ablation.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-16T00:06:21.092976+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_ty_seed_audit_20260515T235823",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-16T00:06:21.093095+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "grep -n \"toda_yamamoto\\|metrics\\[\\|data\\[:1\\|T\\+1\\|\\.T\\b\\|n_obs\\|slice\\|extract\\|gen_\" /root/autodl-tmp/distrib_canary_collapse/window_sensitivity.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_ty_seed_audit_20260515T235823",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "grep -n \"toda_yamamoto\\|metrics\\[\\|data\\[:1\\|T\\+1\\|\\.T\\b\\|n_obs\\|slice\\|extract\\|gen_\" /root/autodl-tmp/distrib_canary_collapse/window_sensitivity.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-16T00:06:21.093213+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_ty_seed_audit_20260515T235823",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-16T00:06:21.093362+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "grep -n \"toda_yamamoto\\|T+1\\|n_obs\\|extract\\|sorted\" /root/autodl-tmp/distrib_canary_collapse/method_ablation.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_ty_seed_audit_20260515T235823",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "grep -n \"toda_yamamoto\\|T+1\\|n_obs\\|extract\\|sorted\" /root/autodl-tmp/distrib_canary_collapse/method_ablation.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-16T00:06:21.093481+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_ty_seed_audit_20260515T235823",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-16T00:06:21.093605+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "grep -n \"toda_yamamoto\\|T+1\\|n_obs\\|extract\\|sorted\\|metrics\\[\" /root/autodl-tmp/distrib_canary_collapse/window_sensitivity.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_ty_seed_audit_20260515T235823",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "grep -n \"toda_yamamoto\\|T+1\\|n_obs\\|extract\\|sorted\\|metrics\\[\" /root/autodl-tmp/distrib_canary_collapse/window_sensitivity.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-16T00:06:21.093721+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_ty_seed_audit_20260515T235823",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-16T00:06:21.093846+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "grep -n -e \"toda_yamamoto\" -e \"extract\" -e \"sorted\" -e \"n_obs\" /root/autodl-tmp/distrib_canary_collapse/method_ablation.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_ty_seed_audit_20260515T235823",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "grep -n -e \"toda_yamamoto\" -e \"extract\" -e \"sorted\" -e \"n_obs\" /root/autodl-tmp/distrib_canary_collapse/method_ablation.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-16T00:06:21.094007+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"54:def extract(metrics_list, name):\\n55:    \\\"\\\"\\\"Extract a single metric as numpy array, sorted by generation.\\\"\\\"\\\"\\n56:    return np.array([m[name] for m in sorted(metrics_list,\\n193:def toda_yamamoto(c, d, cn, dn):\\n210:            \\\"method\\\": \\\"toda_yamamoto\\\", \\\"p\\\": p, \\\"d_max\\\": d_max, \\\"k\\\": k,\\n232:            \\\"method\\\": \\\"toda_yamamoto\\\", \\\"p\\\": p, \\\"d_max\\\": d_max, \\\"k\\\": k,\\n255:            \\\"method\\\": \\\"toda_yamamoto\\\", \\\"p\\\": p, \\\"d_max\\\": d_max, \\\"k\\\": k,\\n262:        \\\"method\\\": \\\"toda_yamamoto\\\",\\n316:            ty = sr[\\\"toda_yamamoto\\\"]\\n341:    for method in [\\\"naive_pearson\\\", \\\"differenced_xcorr\\\", \\\"toda_yamamoto\\\", \\\"permutation_granger\\\"]:\\n361:            for m in [\\\"naive_pearson\\\", \\\"differenced_xcorr\\\", \\\"toda_yamamoto\\\"]:\\n391:METHODS = [\\\"naive_pearson\\\", \\\"differenced_xcorr\\\", \\\"threshold_onset\\\", \\\"toda_yamamoto\\\", \\\"permutation_granger\\\"]\\n396:    \\\"toda_yamamoto\\\": toda_yamamoto,\\n419:            c_arr = extract(data[seed], cn)\\n420:            d_arr = extract(data[seed], dn)\\n441:        ty_sig     = summary[\\\"toda_yamamoto\\\"][\\\"verdict\\\"] == \\\"SIGNIFICANT\\\"\\n446:                   \\\"threshold_onset\\\": thresh_sig, \\\"toda_yamamoto\\\": ty_sig,\\n478:    n_ty     = sum(1 for r in all_pairs if r[\\\"summary\\\"][\\\"toda_yamamoto\\\"][\\\"verdict\\\"] == \\\"SIGNIFICANT\\\")\\n502:                \\\"toda_yamamoto: augmented-lag Granger causality (Wald F-test)\\\",\\n558:    for _m in [\\\"naive_pearson\\\", \\\"differenced_xcorr\\\", \\\"toda_yamamoto\\\", \\\"permutation_granger\\\"]:\\n599:    for _m in [\\\"naive_pearson\\\", \\\"differenced_xcorr\\\", \\\"toda_yamamoto\\\", \\\"permutation_granger\\\"]:\\n677:                ty = s[\\\"toda_yamamoto\\\"]\\n\", \"stderr\": \"\", \"return_code\": 0}, \"err
…[truncated 56 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_ty_seed_audit_20260515T235823",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-16T00:06:21.094147+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "grep -n -e \"toda_yamamoto\" -e \"T+1\" -e \"sorted\" -e \"extract\" -e \"n_obs\" -e \"metrics\" /root/autodl-tmp/distrib_canary_collapse/window_sensitivity.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_ty_seed_audit_20260515T235823",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "grep -n -e \"toda_yamamoto\" -e \"T+1\" -e \"sorted\" -e \"extract\" -e \"n_obs\" -e \"metrics\" /root/autodl-tmp/distrib_canary_collapse/window_sensitivity.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-16T00:06:21.094301+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"30:    with open(f\\\"{BASE}/rep_{seed}/all_metrics.json\\\") as f:\\n104:def toda_yamamoto(x, y, maxlag=2):\\n151:def toda_yamamoto_v2(x, y, maxlag=2):\\n193:        metrics = all_data[seed][:T]  # gen_0 to gen_{T-1}\\n196:            x = np.array([m[x_key] for m in metrics])\\n197:            y = np.array([m[y_key] for m in metrics])\\n228:            p_ty = toda_yamamoto_v2(x, y)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_ty_seed_audit_20260515T235823",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-16T00:06:21.094458+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "sed -n '104,190p' /root/autodl-tmp/distrib_canary_collapse/window_sensitivity.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_ty_seed_audit_20260515T235823",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "sed -n '104,190p' /root/autodl-tmp/distrib_canary_collapse/window_sensitivity.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-16T00:06:21.094576+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: 'sed' is not in the read-only allowlist. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_ty_seed_audit_20260515T235823",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-16T00:06:21.094685+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "sed -n '193,240p' /root/autodl-tmp/distrib_canary_collapse/method_ablation.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_ty_seed_audit_20260515T235823",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "sed -n '193,240p' /root/autodl-tmp/distrib_canary_collapse/method_ablation.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-16T00:06:21.094826+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: 'sed' is not in the read-only allowlist. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_ty_seed_audit_20260515T235823",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-16T00:06:21.094938+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "cat /root/autodl-tmp/distrib_canary_collapse/results/mvp/rep_43/all_metrics.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_ty_seed_audit_20260515T235823",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "cat /root/autodl-tmp/distrib_canary_collapse/results/mvp/rep_43/all_metrics.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-16T00:06:21.095118+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"[\\n  {\\n    \\\"token_entropy\\\": 3.2341948700181407,\\n    \\\"self_bleu\\\": 0.010826090501434389,\\n    \\\"distinct_1\\\": 0.09833431219002871,\\n    \\\"distinct_2\\\": 0.5131779657560506,\\n    \\\"distinct_3\\\": 0.8056693041846806,\\n    \\\"ece\\\": 0.010804557477709054,\\n    \\\"effective_rank\\\": 46.612774691899155,\\n    \\\"perplexity\\\": 26.948958972544652,\\n    \\\"mauve\\\": 0.03350582133330568,\\n    \\\"generation\\\": 0\\n  },\\n  {\\n    \\\"token_entropy\\\": 1.9091676850858001,\\n    \\\"self_bleu\\\": 0.010964385056351856,\\n    \\\"distinct_1\\\": 0.09963439966763606,\\n    \\\"distinct_2\\\": 0.5176943722008492,\\n    \\\"distinct_3\\\": 0.8097101738292286,\\n    \\\"ece\\\": 0.2047232364754478,\\n    \\\"effective_rank\\\": 78.44949353495862,\\n    \\\"perplexity\\\": 55.45443987331369,\\n    \\\"mauve\\\": 0.029947808319125253,\\n    \\\"generation\\\": 1\\n  },\\n  {\\n    \\\"token_entropy\\\": 1.4656595424390364,\\n    \\\"self_bleu\\\": 0.01167633497255247,\\n    \\\"distinct_1\\\": 0.08178125,\\n    \\\"distinct_2\\\": 0.42847990999929686,\\n    \\\"distinct_3\\\": 0.7063860372818326,\\n    \\\"ece\\\": 0.32151683081221566,\\n    \\\"effective_rank\\\": 94.30570627135812,\\n    \\\"perplexity\\\": 158.7070438020113,\\n    \\\"mauve\\\": 0.03443139669928502,\\n    \\\"generation\\\": 2\\n  },\\n  {\\n    \\\"token_entropy\\\": 1.3254262710650406,\\n    \\\"self_bleu\\\": 0.012155088186284052,\\n    \\\"distinct_1\\\": 0.076546875,\\n    \\\"distinct_2\\\": 0.3851592590567114,\\n    \\\"distinct_3\\\": 0.6405334458350912,\\n    \\\"ece\\\": 0.361099150868516,\\n    \\\"effective_rank\\\": 99.28918987011264,\\n    \\\"perplexity\\\": 279.71671416824785,\\n    \\\"mauve\\\": 0.03324061204122193,\\n    \\\"generation\\\": 3\\n  },\\n  {\\n    \\\"token_entropy\\\": 1.279669450498936,\\n    \\\"self_bleu\\\": 0.01172099795687604,\\n    \\\"distinct_1\\\": 0.074,\\n    \\\"distin
…[truncated 3058 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_ty_seed_audit_20260515T235823",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-16T00:06:21.095311+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "cat /root/autodl-tmp/distrib_canary_collapse/results/mvp/rep_44/all_metrics.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_ty_seed_audit_20260515T235823",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "cat /root/autodl-tmp/distrib_canary_collapse/results/mvp/rep_44/all_metrics.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-16T00:06:21.095513+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"[\\n  {\\n    \\\"token_entropy\\\": 3.2341948700181407,\\n    \\\"self_bleu\\\": 0.011024683423681741,\\n    \\\"distinct_1\\\": 0.09808801064406446,\\n    \\\"distinct_2\\\": 0.5132353786640604,\\n    \\\"distinct_3\\\": 0.8057672722494169,\\n    \\\"ece\\\": 0.010804557477709054,\\n    \\\"effective_rank\\\": 46.612774691899155,\\n    \\\"perplexity\\\": 26.948958972544652,\\n    \\\"mauve\\\": 0.02953861796475695,\\n    \\\"generation\\\": 0\\n  },\\n  {\\n    \\\"token_entropy\\\": 1.8893646159023845,\\n    \\\"self_bleu\\\": 0.010031830626628888,\\n    \\\"distinct_1\\\": 0.0976259850341037,\\n    \\\"distinct_2\\\": 0.5126441348597349,\\n    \\\"distinct_3\\\": 0.8040991341489662,\\n    \\\"ece\\\": 0.20947405654493584,\\n    \\\"effective_rank\\\": 78.64317578127446,\\n    \\\"perplexity\\\": 56.365283599559646,\\n    \\\"mauve\\\": 0.03189722578287753,\\n    \\\"generation\\\": 1\\n  },\\n  {\\n    \\\"token_entropy\\\": 1.5357174457488199,\\n    \\\"self_bleu\\\": 0.011327896283488638,\\n    \\\"distinct_1\\\": 0.0813359375,\\n    \\\"distinct_2\\\": 0.429456480128751,\\n    \\\"distinct_3\\\": 0.7129720776887138,\\n    \\\"ece\\\": 0.3174814347563344,\\n    \\\"effective_rank\\\": 74.5236039799353,\\n    \\\"perplexity\\\": 161.75839394784464,\\n    \\\"mauve\\\": 0.03254977898818445,\\n    \\\"generation\\\": 2\\n  },\\n  {\\n    \\\"token_entropy\\\": 1.34933725274223,\\n    \\\"self_bleu\\\": 0.012207081513261346,\\n    \\\"distinct_1\\\": 0.07571875,\\n    \\\"distinct_2\\\": 0.3870498988273346,\\n    \\\"distinct_3\\\": 0.6474163658807169,\\n    \\\"ece\\\": 0.36143363341891466,\\n    \\\"effective_rank\\\": 83.53133488420403,\\n    \\\"perplexity\\\": 281.7541286096598,\\n    \\\"mauve\\\": 0.03404886425384626,\\n    \\\"generation\\\": 3\\n  },\\n  {\\n    \\\"token_entropy\\\": 1.2902888727921988,\\n    \\\"self_bleu\\\": 0.012673474841930984,\\n    \\\"distinct_1\\\": 0.07384375,\\n    \\\"d
…[truncated 3066 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_ty_seed_audit_20260515T235823",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-16T00:06:21.095671+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "cat /root/autodl-tmp/distrib_canary_collapse/results/mvp/rep_45/all_metrics.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_ty_seed_audit_20260515T235823",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "cat /root/autodl-tmp/distrib_canary_collapse/results/mvp/rep_45/all_metrics.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-16T00:06:21.095862+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"[\\n  {\\n    \\\"token_entropy\\\": 3.2341948700181407,\\n    \\\"self_bleu\\\": 0.010086378095600196,\\n    \\\"distinct_1\\\": 0.09857404984654373,\\n    \\\"distinct_2\\\": 0.5146298917157621,\\n    \\\"distinct_3\\\": 0.8083616525824687,\\n    \\\"ece\\\": 0.010804557477709054,\\n    \\\"effective_rank\\\": 46.612774691899155,\\n    \\\"perplexity\\\": 26.948958972544652,\\n    \\\"mauve\\\": 0.03305519373060749,\\n    \\\"generation\\\": 0\\n  },\\n  {\\n    \\\"token_entropy\\\": 1.8999594054507678,\\n    \\\"self_bleu\\\": 0.010006842730058394,\\n    \\\"distinct_1\\\": 0.09901316331405789,\\n    \\\"distinct_2\\\": 0.5199140011697159,\\n    \\\"distinct_3\\\": 0.816987380144321,\\n    \\\"ece\\\": 0.20864186080006125,\\n    \\\"effective_rank\\\": 78.8806956405284,\\n    \\\"perplexity\\\": 56.15400418972092,\\n    \\\"mauve\\\": 0.030817809717514348,\\n    \\\"generation\\\": 1\\n  },\\n  {\\n    \\\"token_entropy\\\": 1.554124562829477,\\n    \\\"self_bleu\\\": 0.010884596954784274,\\n    \\\"distinct_1\\\": 0.0817578125,\\n    \\\"distinct_2\\\": 0.43087836623723624,\\n    \\\"distinct_3\\\": 0.7109407959499368,\\n    \\\"ece\\\": 0.31792345033625224,\\n    \\\"effective_rank\\\": 74.38677348444702,\\n    \\\"perplexity\\\": 169.32642422086198,\\n    \\\"mauve\\\": 0.03128062353546652,\\n    \\\"generation\\\": 2\\n  },\\n  {\\n    \\\"token_entropy\\\": 1.4132002819281364,\\n    \\\"self_bleu\\\": 0.011810202868349284,\\n    \\\"distinct_1\\\": 0.075609375,\\n    \\\"distinct_2\\\": 0.3862530176017,\\n    \\\"distinct_3\\\": 0.6460882201284395,\\n    \\\"ece\\\": 0.35672111702986187,\\n    \\\"effective_rank\\\": 83.81549748633424,\\n    \\\"perplexity\\\": 285.5874645275131,\\n    \\\"mauve\\\": 0.03324193432432916,\\n    \\\"generation\\\": 3\\n  },\\n  {\\n    \\\"token_entropy\\\": 1.3632528999895621,\\n    \\\"self_bleu\\\": 0.012584758986444757,\\n    \\\"distinct_1\\\": 0.0732890625,\\n    \
…[truncated 3072 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_ty_seed_audit_20260515T235823",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-16T00:06:21.096012+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "tail -n +193 /root/autodl-tmp/distrib_canary_collapse/method_ablation.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_ty_seed_audit_20260515T235823",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "tail -n +193 /root/autodl-tmp/distrib_canary_collapse/method_ablation.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-16T00:06:21.096272+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"def toda_yamamoto(c, d, cn, dn):\\n    \\\"\\\"\\\"Toda-Yamamoto Granger causality: canary → downstream direction.\\\"\\\"\\\"\\n    x, y = orient(c, cn), orient(d, dn)\\n    n = len(x)\\n\\n    dc, dd = _adf_order(x), _adf_order(y)\\n    d_max = max(dc, dd)\\n\\n    # With T=10, only p=1 is feasible regardless of AIC\\n    p = 1\\n    k = p + d_max                       # total lags in augmented VAR\\n    T_eff = n - k                        # effective sample after lagging\\n    n_params = 1 + 2 * k                 # intercept + k lags × 2 variables\\n    df_resid = T_eff - n_params\\n\\n    if df_resid < 1:\\n        return {\\n            \\\"method\\\": \\\"toda_yamamoto\\\", \\\"p\\\": p, \\\"d_max\\\": d_max, \\\"k\\\": k,\\n            \\\"wald_F\\\": None, \\\"p_value\\\": None, \\\"significant\\\": False,\\n            \\\"note\\\": f\\\"no residual df (T_eff={T_eff}, params={n_params})\\\",\\n            \\\"d_canary\\\": dc, \\\"d_downstream\\\": dd,\\n        }\\n\\n    # OLS for the downstream equation:\\n    #   y_t = c0 + Σ_{l=1}^{k} a_l·x_{t-l} + Σ_{l=1}^{k} b_l·y_{t-l} + ε\\n    Y = y[k:]\\n    X_cols = [np.ones(T_eff)]\\n    for l in range(1, k + 1):\\n        X_cols.append(x[k - l : n - l])   # canary  lag l\\n        X_cols.append(y[k - l : n - l])   # downstream lag l\\n    X = np.column_stack(X_cols)\\n\\n    try:\\n        beta = np.linalg.lstsq(X, Y, rcond=None)[0]\\n        resid = Y - X @ beta\\n        sigma2 = np.sum(resid ** 2) / df_resid\\n        XtX_inv = np.linalg.inv(X.T @ X)\\n    except Exception:\\n        return {\\n            \\\"method\\\": \\\"toda_yamamoto\\\", \\\"p\\\": p, \\\"d_max\\\": d_max, \\\"k\\\": k,\\n            \\\"wald_F\\\": None, \\\"p_value\\\": None, \\\"significant\\\": False,\\n            \\\"note\\\": \\\"OLS failed (singular design matrix)\\\",\\n            \\\"d_canary\\\": dc, \\\"d_downstream\\\": dd,\\n        }\\n\\n    # Wald test on firs
…[truncated 7535 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_ty_seed_audit_20260515T235823",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-16T00:06:21.096469+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "grep -n \"_adf_order\" /root/autodl-tmp/distrib_canary_collapse/method_ablation.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_ty_seed_audit_20260515T235823",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "grep -n \"_adf_order\" /root/autodl-tmp/distrib_canary_collapse/method_ablation.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-16T00:06:21.096595+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"177:def _adf_order(series, max_d=2):\\n198:    dc, dd = _adf_order(x), _adf_order(y)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_ty_seed_audit_20260515T235823",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-16T00:06:21.096711+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "head -192 /root/autodl-tmp/distrib_canary_collapse/method_ablation.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_ty_seed_audit_20260515T235823",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "head -192 /root/autodl-tmp/distrib_canary_collapse/method_ablation.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-16T00:06:21.096926+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Method ablation: compare four lead-lag estimation methods.\\n\\nCompares naive vs robust approaches to detect canary->downstream lead-lag,\\nquantifying the spurious regression rate when non-stationary series are\\ncorrelated without proper detrending.\\n\\nInput:  results/mvp/rep_{seed}/all_metrics.json (seeds 42-45)\\nOutput: results/mvp/analysis/method_ablation.json\\n        (with BH FDR correction and effect sizes)\\n\\nMethods:\\n  1. Naive Pearson lag-correlation (raw levels)\\n  2. Differenced cross-correlation (first-differenced series)\\n  3. Threshold-based lead time (2-sigma onset detection)\\n  4. Toda-Yamamoto augmented-lag Granger causality\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport json\\nimport os\\nimport warnings\\nfrom itertools import product\\n\\nimport numpy as np\\nfrom scipy import stats\\nfrom statsmodels.stats.multitest import multipletests\\nfrom statsmodels.tsa.stattools import adfuller\\nfrom permutation_granger import permutation_granger_test\\n\\nwarnings.filterwarnings(\\\"ignore\\\")\\n\\nCANARY = [\\\"token_entropy\\\", \\\"self_bleu\\\", \\\"ece\\\", \\\"effective_rank\\\"]\\nDOWNSTREAM = [\\\"perplexity\\\", \\\"distinct_1\\\", \\\"distinct_2\\\", \\\"distinct_3\\\"]\\n\\n# Sign conventions: \\\"higher is worse\\\" kept as-is; \\\"lower is worse\\\" negated\\n# so that degradation = positive direction in all analyses.\\nHIGHER_IS_WORSE = {\\\"self_bleu\\\", \\\"ece\\\", \\\"perplexity\\\"}\\nLOWER_IS_WORSE = {\\\"token_entropy\\\", \\\"effective_rank\\\",\\n                   \\\"distinct_1\\\", \\\"distinct_2\\\", \\\"distinct_3\\\"}\\n\\nALPHA = 0.05\\n\\n\\ndef load_metrics(data_dir, seeds):\\n    \\\"\\\"\\\"Load all_metrics.json for each seed.\\\"\\\"\\\"\\n    data = {}\\n    for s in seeds:\\n        path = os.path.join(data_dir, f\\\"rep_{s}\\\", \\\"all_metrics.json\\\")\\n        with open(path) as f:\\n            data[s] = json.load(f)\\n    return 
…[truncated 5496 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_ty_seed_audit_20260515T235823",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-16T00:06:21.097107+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "tail -n +104 /root/autodl-tmp/distrib_canary_collapse/window_sensitivity.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_ty_seed_audit_20260515T235823",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "tail -n +104 /root/autodl-tmp/distrib_canary_collapse/window_sensitivity.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-16T00:06:21.097352+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"def toda_yamamoto(x, y, maxlag=2):\\n    \\\"\\\"\\\"Toda-Yamamoto test: VAR(p+d) with Wald test on first p lags.\\\"\\\"\\\"\\n    data = np.column_stack([x, y])\\n    n = len(x)\\n    \\n    # Determine integration order d (use 1 as default for short series)\\n    d = 1\\n    \\n    # Select optimal lag p (AIC on VAR)\\n    best_p = 1\\n    best_aic = np.inf\\n    for p in range(1, min(maxlag + 1, n // 3)):\\n        try:\\n            model = VAR(data)\\n            result = model.fit(p)\\n            if result.aic < best_aic:\\n                best_aic = result.aic\\n                best_p = p\\n        except:\\n            continue\\n    \\n    # Fit VAR(p+d)\\n    p_d = best_p + d\\n    if p_d >= n - 1:\\n        return 1.0  # not enough observations\\n    \\n    try:\\n        model = VAR(data)\\n        result = model.fit(p_d)\\n        # Wald test: x does not Granger-cause y\\n        # Test coefficients of x in y equation for first p lags\\n        # result.params shape: (p_d*2+1, 2), equation for y is column 1\\n        # Params order: const, L1.x, L1.y, L2.x, L2.y, ...\\n        \\n        # Use built-in test\\n        test_result = result.test_causality('y1', 'y2', kind='wald')\\n        return test_result.pvalue\\n    except Exception:\\n        # Fallback: manual Wald\\n        try:\\n            model = VAR(data)\\n            result = model.fit(p_d)\\n            test_result = result.test_causality(0, 1, kind='wald')\\n            return test_result.pvalue\\n        except:\\n            return 1.0\\n\\ndef toda_yamamoto_v2(x, y, maxlag=2):\\n    \\\"\\\"\\\"Toda-Yamamoto with proper column naming.\\\"\\\"\\\"\\n    import pandas as pd\\n    data = pd.DataFrame({'cause': x, 'effect': y})\\n    n = len(x)\\n    d = 1\\n    \\n    best_p = 1\\n    best_aic = np.inf\\n    for p in range(1, min(maxlag + 1, max(2, n // 3))):\\n        try:\\n            model = VAR(data)\\n            result = mode
…[truncated 6936 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_ty_seed_audit_20260515T235823",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-16T00:06:21.097591+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-19828",
  "command": "cat > /root/autodl-tmp/distrib_canary_collapse/ty_audit.py << 'PYEOF'\n\"\"\"TY Toda-Yamamoto Full Seed Audit\nRuns TY on all 4 seeds × 6 pairs with both 11-point and 10-point data.\nImplements two TY variants:\n  A) method_ablation style (hand OLS, F-test, ADF for d_max, p=1 fixed)\n  B) statsmodels VAR test_causality (Wald chi2, d=1 hardcoded, AIC for p)\n\"\"\"\n\nimport json, warnings\nimport numpy as np\nimport pandas as pd\nfrom scipy import stats\nfrom statsmodels.tsa.api import VAR\nfrom statsmodels.tsa.stattools import adfuller\n\nwarnings.filterwarnings('ignore')\n\nSEEDS = [42, 43, 44, 45]\nBASE = \"/root/autodl-tmp/distrib_canary_collapse/results/mvp\"\nPAIRS = [\n    (\"token_entropy\", \"distinct_1\", \"TE→d1\"),\n    (\"token_entropy\", \"distinct_2\", \"TE→d2\"),\n    (\"token_entropy\", \"distinct_3\", \"TE→d3\"),\n    (\"ece\", \"distinct_1\", \"ECE→d1\"),\n    (\"ece\", \"distinct_2\", \"ECE→d2\"),\n    (\"ece\", \"distinct_3\", \"ECE→d3\"),\n]\nALPHA = 0.05\n\n# --- Load data ---\nall_data = {}\nfor s in SEEDS:\n    with open(f\"{BASE}/rep_{s}/all_metrics.json\") as f:\n        raw = json.load(f)\n    all_data[s] = sorted(raw, key=lambda x: x[\"generation\"])\n\nprint(f\"Seeds: {SEEDS}\")\nfor s in SEEDS:\n    gens = [m['generation'] for m in all_data[s]]\n    print(f\"  seed {s}: {len(all_data[s])} points, generations {gens}\")\n\n# --- ADF integration order ---\ndef adf_order(series, max_d=2):\n    for d in range(max_d + 1):\n        s = series.copy()\n        for _ in range(d):\n            s = np.diff(s)\n        if len(s) < 5:\n            return d\n        try:\n            if adfuller(s, maxlag=1, autolag=None)[1] < 0.05:\n                return d\n        except:\n            pass\n    return max_d\n\n# --- TY Method A: method_ablation style (hand OLS, F-test) ---\ndef ty_method_a(x, y):\n    n = len(x)\n    dc, dd = adf_order(x), adf_order(y)\n    d_max = max(dc, dd)\n    p = 1\n    k = p + d_max\n    T_eff = n - k\n    n_params = 1 + 2 * k\n    df_resid = T_eff - n_params\n\n    if df_resid < 1:\n        return {\"F\": None, \"p\": None, \"sig\": False, \"d_max\": d_max, \"p_lag\": p, \"k\": k,\n                \"df_resid\": df_resid, \"dc\": dc, \"dd\": dd, \"note\": f\"no df (T_eff={T_eff}, params={n_params})\"}\n\n    Y = y[k:]\n    X_cols = [np.ones(T_eff)]\n    for l in range(1, k + 1):\n        X_cols.append(x[k - l : n - l])\n        X_cols.append(y[k - l : n - l])\n    X = np.column_stack(X_cols)\n\n    try:\n        beta = np.linalg.lstsq(X, Y, rcond=None)[0]\n        resid = Y - X @ beta\n        sigma2 = np.sum(resid ** 2) / df_resid\n        XtX_inv = np.linalg.inv(X.T @ X)\n    except:\n        return {\"F\": None, \"p\": None, \"sig\": False, \"d_max\": d_max, \"p_lag\": p, \"k\": k,\n                \"df_resid\": df_resid, \"dc\": dc, \"dd\": dd, \"note\": \"OLS failed\"}\n\n    test_idx = [2 * (l - 1) + 1 for l in range(1, p + 1)]\n    R = np.zeros((p, n_params))\n    for i, idx in enumerate(test_idx):\n        R[i, idx] = 1.0\n\n    Rb = R @ beta\n    try:\n        cov_Rb = sigma2 * (R @ XtX_inv @ R.T)\n        W = float(Rb @ np.linalg.inv(cov_Rb) @ Rb)\n        F = W / p\n        pval = float(1.0 - stats.f.cdf(F, p, df_resid))\n    except:\n        return {\"F\": None, \"p\": None, \"sig\": False, \"d_max\": d_max, \"p_lag\": p, \"k\": k,\n                \"df_resid\": df_resid, \"dc\": dc, \"dd\": dd, \"note\": \"Wald failed\"}\n\n    return {\"F\": round(F, 4), \"p\": round(pval, 6), \"sig\": pval < ALPHA,\n            \"d_max\": d_max, \"p_lag\": p, \"k\": k, \"df_resid\": df_resid, \"dc\": dc, \"dd\": dd, \"note\": \"\"}\n\n# --- TY Method B: statsmodels VAR (Wald chi2, AIC lag, d=1 fixed) ---\ndef ty_method_b(x, y, maxlag=2):\n    data = pd.DataFrame({'cause': x, 'effect': y})\n    n = len(x)\n    d = 1\n    best_p = 1\n    best_aic = np.inf\n    for p_try in range(1, min(maxlag + 1, max(2, n // 3))):\n        try:\n            model = VAR(data)\n            result = model.fit(p_try)\n            if result.aic < best_aic:\n                best_aic = result.aic\n                best_p = p_try\n        except:\n            continue\n    p_d = best_p + d\n    if p_d >= n - 2:\n        return {\"chi2\": None, \"p\": None, \"sig\": False, \"p_lag\": best_p, \"d\": d, \"note\": \"not enough obs\"}\n    try:\n        model = VAR(data)\n        result = model.fit(p_d)\n        test_result = result.test_causality('effect', ['cause'], kind='wald')\n        pval = float(test_result.pvalue)\n        chi2_val = float(test_result.test_statistic)\n        return {\"chi2\": round(chi2_val, 4), \"p\": round(pval, 6), \"sig\": pval < ALPHA,\n                \"p_lag\": best_p, \"d\": d, \"note\": \"\"}\n    except Exception as e:\n        return {\"chi2\": None, \"p\": None, \"sig\": False, \"p_lag\": best_p, \"d\": d, \"note\": str(e)[:50]}\n\n# --- Run both methods for both 11-point and 10-point data ---\nresults = {}\nfor n_points, label in [(11, \"11pt\"), (10, \"10pt\")]:\n    results[label] = {}\n    for seed in SEEDS:\n        results[label][seed] = {}\n        metrics = all_data[seed][:n_points]\n        for x_key, y_key, pair_name in PAIRS:\n            x = np.array([m[x_key] for m in metrics])\n            y = np.array([m[y_key] for m in metrics])\n            \n            res_a = ty_method_a(x, y)\n            res_b = ty_method_b(x, y)\n            results[label][seed][pair_name] = {\"method_a\": res_a, \"method_b\": res_b}\n\n# --- Print results ---\nprint(\"\\n\" + \"=\"*100)\nprint(\"TODA-YAMAMOTO AUDIT: 11-point (gen_0-gen_10) vs 10-point (gen_0-gen_9)\")\nprint(\"=\"*100)\n\nfor label in [\"11pt\", \"10pt\"]:\n    print(f\"\\n{'─'*100}\")\n    print(f\"  {label.upper()} DATA\")\n    print(f\"{'─'*100}\")\n    \n    # Method A table\n    print(f\"\\n  Method A (hand OLS, F-test, ADF d_max, p=1 fixed):\")\n    print(f\"  {'Pair':<10} {'s42':>20} {'s43':>20} {'s44':>20} {'s45':>20}\")\n    print(f\"  {'':10} {'F / p-val':>20} {'F / p-val':>20} {'F / p-val':>20} {'F / p-val':>20}\")\n    for _, _, pn in PAIRS:\n        cells = [f\"  {pn:<10}\"]\n        for seed in SEEDS:\n            r = results[label][seed][pn][\"method_a\"]\n            if r[\"F\"] is not None:\n                sig_mark = \"*\" if r[\"sig\"] else \" \"\n                cells.append(f\"{r['F']:6.2f} / {r['p']:.4f}{sig_mark}\")\n            else:\n                cells.append(f\"{'N/A':>20}\")\n        print(\" \".join(cells))\n    \n    # Method A detail\n    print(f\"\\n  Method A details (d_max, k, df_resid):\")\n    for _, _, pn in PAIRS:\n        for seed in SEEDS:\n            r = results[label][seed][pn][\"method_a\"]\n            print(f\"    {pn} s{seed}: dc={r['dc']}, dd={r['dd']}, d_max={r['d_max']}, k={r['k']}, df_resid={r['df_resid']} {r['note']}\")\n    \n    # Method B table\n    print(f\"\\n  Method B (statsmodels VAR, Wald chi2, d=1, AIC lag):\")\n    print(f\"  {'Pair':<10} {'s42':>20} {'s43':>20} {'s44':>20} {'s45':>20}\")\n    print(f\"  {'':10} {'chi2 / p-val':>20} {'chi2 / p-val':>20} {'chi2 / p-val':>20} {'chi2 / p-val':>20}\")\n    for _, _, pn in PAIRS:\n        cells = [f\"  {pn:<10}\"]\n        for seed in SEEDS:\n            r = results[label][seed][pn][\"method_b\"]\n            if r[\"chi2\"] is not None:\n                sig_mark = \"*\" if r[\"sig\"] else \" \"\n                cells.append(f\"{r['chi2']:6.2f} / {r['p']:.4f}{sig_mark}\")\n            else:\n                cells.append(f\"{'N/A':>20}\")\n        print(\" \".join(cells))\n\n# --- Significance summary ---\nprint(f\"\\n{'='*100}\")\nprint(\"SIGNIFICANCE SUMMARY (p < 0.05)\")\nprint(f\"{'='*100}\")\nprint(f\"\\n  {'Pair':<10} {'Method':<12} {'11pt sig_seeds':>16} {'10pt sig_seeds':>16} {'FLIP?':>8}\")\nfor _, _, pn in PAIRS:\n    for method_key, method_name in [(\"method_a\", \"OLS-F\"), (\"method_b\", \"VAR-chi2\")]:\n        sig_11 = sum(1 for s in SEEDS if results[\"11pt\"][s][pn][method_key][\"sig\"])\n        sig_10 = sum(1 for s in SEEDS if results[\"10pt\"][s][pn][method_key][\"sig\"])\n        flip = \"YES\" if sig_11 != sig_10 else \"\"\n        print(f\"  {pn:<10} {method_name:<12} {sig_11:>10}/4       {sig_10:>10}/4       {flip:>8}\")\n\n# --- FNR calculation ---\nprint(f\"\\n{'='*100}\")\nprint(\"FNR CALCULATION (using Method A = method_ablation implementation, 11pt)\")\nprint(f\"{'='*100}\")\nprint(\"\\nPer-pair sig_seeds count (p < 0.05):\")\nfnr_miss = 0\nfnr_total = len(PAIRS)\nfor _, _, pn in PAIRS:\n    sig_count = sum(1 for s in SEEDS if results[\"11pt\"][s][pn][\"method_a\"][\"sig\"])\n    status = \"DETECTED (≥3)\" if sig_count >= 3 else \"MISSED (<3)\"\n    if sig_count < 3:\n        fnr_miss += 1\n    print(f\"  {pn:<10}: {sig_count}/4 sig seeds → {status}\")\n\nfnr = fnr_miss / fnr_total\nprint(f\"\\nFNR = {fnr_miss}/{fnr_total} = {fnr:.1%}\")\nprint(f\"(Paper claims FNR=33.3% = 2/6)\")\n\n# --- Save JSON ---\noutput = {\"results\": {}, \"summary\": {}}\nfor label in [\"11pt\", \"10pt\"]:\n    output[\"results\"][label] = {}\n    for seed in SEEDS:\n        output[\"results\"][label][str(seed)] = {}\n        for _, _, pn in PAIRS:\n            output[\"results\"][label][str(seed)][pn] = results[label][seed][pn]\n\nwith open(\"/root/autodl-tmp/distrib_canary_collapse/ty_audit_results.json\", \"w\") as f:\n    json.dump(output, f, indent=2, default=str)\nprint(\"\\nResults saved to ty_audit_results.json\")\nPYEOF\necho \"Script written\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_ty_seed_audit_20260515T235823",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-19828",
    "command": "cat > /root/autodl-tmp/distrib_canary_collapse/ty_audit.py << 'PYEOF'\n\"\"\"TY Toda-Yamamoto Full Seed Audit\nRuns TY on all 4 seeds × 6 pairs with both 11-point and 10-point data.\nImplements two TY variants:\n  A) method_ablation style (hand OLS, F-test, ADF for d_max, p=1 fixed)\n  B) statsmodels VAR test_causality (Wald chi2, d=1 hardcoded, AIC for p)\n\"\"\"\n\nimport json, warnings\nimport numpy as np\nimport pandas as pd\nfrom scipy import stats\nfrom statsmodels.tsa.api import VAR\nfrom statsmodels.tsa.stattools import adfuller\n\nwarnings.filterwarnings('ignore')\n\nSEEDS = [42, 43, 44, 45]\nBASE = \"/root/autodl-tmp/distrib_canary_collapse/results/mvp\"\nPAIRS = [\n    (\"token_entropy\", \"distinct_1\", \"TE→d1\"),\n    (\"token_entropy\", \"distinct_2\", \"TE→d2\"),\n    (\"token_entropy\", \"distinct_3\", \"TE→d3\"),\n    (\"ece\", \"distinct_1\", \"ECE→d1\"),\n    (\"ece\", \"distinct_2\", \"ECE→d2\"),\n    (\"ece\", \"distinct_3\", \"ECE→d3\"),\n]\nALPHA = 0.05\n\n# --- Load data ---\nall_data = {}\nfor s in SEEDS:\n    with open(f\"{BASE}/rep_{s}/all_metrics.json\") as f:\n        raw = json.load(f)\n    all_data[s] = sorted(raw, key=lambda x: x[\"generation\"])\n\nprint(f\"Seeds: {SEEDS}\")\nfor s in SEEDS:\n    gens = [m['generation'] for m in all_data[s]]\n    print(f\"  seed {s}: {len(all_data[s])} points, generations {gens}\")\n\n# --- ADF integration order ---\ndef adf_order(series, max_d=2):\n    for d in range(max_d + 1):\n        s = series.copy()\n        for _ in range(d):\n            s = np.diff(s)\n        if len(s) < 5:\n            return d\n        try:\n            if adfuller(s, maxlag=1, autolag=None)[1] < 0.05:\n                return d\n        except:\n            pass\n    return max_d\n\n# --- TY Method A: method_ablation style (hand OLS, F-test) ---\ndef ty_method_a(x, y):\n    n = len(x)\n    dc, dd = adf_order(x), adf_order(y)\n    d_max = max(dc, dd)\n    p = 1\n    k = p + d_max\n    T_eff = n - k\n    n_params = 1 + 2 * k\n    df_resid = T_eff - n_params\n\n    if df_resid < 1:\n        return {\"F\": None, \"p\": None, \"sig\": False, \"d_max\": d_max, \"p_lag\": p, \"k\": k,\n                \"df_resid\": df_resid, \"dc\": dc, \"dd\": dd, \"note\": f\"no df (T_eff={T_eff}, params={n_params})\"}\n\n    Y = y[k:]\n    X_cols = [np.ones(T_eff)]\n    for l in range(1, k + 1):\n        X_cols.append(x[k - l : n - l])\n        X_cols.append(y[k - l : n - l])\n    X = np.column_stack(X_cols)\n\n    try:\n        beta = np.linalg.lstsq(X, Y, rcond=None)[0]\n        resid = Y - X @ beta\n        sigma2 = np.sum(resid ** 2) / df_resid\n        XtX_inv = np.linalg.inv(X.T @ X)\n    except:\n        return {\"F\": None, \"p\": None, \"sig\": False, \"d_max\": d_max, \"p_lag\": p, \"k\": k,\n                \"df_resid\": df_resid, \"dc\": dc, \"dd\": dd, \"note\": \"OLS failed\"}\n\n    test_idx = [2 * (l - 1) + 1 for l in range(1, p + 1)]\n    R = np.zeros((p, n_params))\n    for i, idx in enumerate(test_idx):\n        R[i, idx] = 1.0\n\n    Rb = R @ beta\n    try:\n        cov_Rb = sigma2 * (R @ XtX_inv @ R.T)\n        W = float(Rb @ np.linalg.inv(cov_Rb) @ Rb)\n        F = W / p\n        pval = float(1.0 - stats.f.cdf(F, p, df_resid))\n    except:\n        return {\"F\": None, \"p\": None, \"sig\": False, \"d_max\": d_max, \"p_lag\": p, \"k\": k,\n                \"df_resid\": df_resid, \"dc\": dc, \"dd\": dd, \"note\": \"Wald failed\"}\n\n    return {\"F\": round(F, 4), \"p\": round(pval, 6), \"sig\": pval < ALPHA,\n            \"d_max\": d_max, \"p_lag\": p, \"k\": k, \"df_resid\": df_resid, \"dc\": dc, \"dd\": dd, \"note\": \"\"}\n\n# --- TY Method B: statsmodels VAR (Wald chi2, AIC lag, d=1 fixed) ---\ndef ty_method_b(x, y, maxlag=2):\n    data = pd.DataFrame({'cause': x, 'effect': y})\n    n = len(x)\n    d = 1\n    best_p = 1\n    best_aic = np.inf\n    for p_try in range(1, min(maxlag + 1, max(2, n // 3))):\n        try:\n            model = VAR(data)\n            result = model.fit(p_try)\n            if result.aic < best_aic:\n                best_aic = result.aic\n                best_p = p_try\n        except:\n            continue\n    p_d = best_p + d\n    if p_d >= n - 2:\n        return {\"chi2\": None, \"p\": None, \"sig\": False, \"p_lag\": best_p, \"d\": d, \"note\": \"not enough obs\"}\n    try:\n        model = VAR(data)\n        result = model.fit(p_d)\n        test_result = result.test_causality('effect', ['cause'], kind='wald')\n        pval = float(test_result.pvalue)\n        chi2_val = float(test_result.test_statistic)\n        return {\"chi2\": round(chi2_val, 4), \"p\": round(pval, 6), \"sig\": pval < ALPHA,\n                \"p_lag\": best_p, \"d\": d, \"note\": \"\"}\n    except Exception as e:\n        return {\"chi2\": None, \"p\": None, \"sig\": False, \"p_lag\": best_p, \"d\": d, \"note\": str(e)[:50]}\n\n# --- Run both methods for both 11-point and 10-point data ---\nresults = {}\nfor n_points, label in [(11, \"11pt\"), (10, \"10pt\")]:\n    results[label] = {}\n    for seed in SEEDS:\n        results[label][seed] = {}\n        metrics = all_data[seed][:n_points]\n        for x_key, y_key, pair_name in PAIRS:\n            x = np.array([m[x_key] for m in metrics])\n            y = np.array([m[y_key] for m in metrics])\n            \n            res_a = ty_method_a(x, y)\n            res_b = ty_method_b(x, y)\n            results[label][seed][pair_name] = {\"method_a\": res_a, \"method_b\": res_b}\n\n# --- Print results ---\nprint(\"\\n\" + \"=\"*100)\nprint(\"TODA-YAMAMOTO AUDIT: 11-point (gen_0-gen_10) vs 10-point (gen_0-gen_9)\")\nprint(\"=\"*100)\n\nfor label in [\"11pt\", \"10pt\"]:\n    print(f\"\\n{'─'*100}\")\n    print(f\"  {label.upper()} DATA\")\n    print(f\"{'─'*100}\")\n    \n    # Method A table\n    print(f\"\\n  Method A (hand OLS, F-test, ADF d_max, p=1 fixed):\")\n    print(f\"  {'Pair':<10} {'s42':>20} {'s43':>20} {'s44':>20} {'s45':>20}\")\n    print(f\"  {'':10} {'F / p-val':>20} {'F / p-val':>20} {'F / p-val':>20} {'F / p-val':>20}\")\n    for _, _, pn in PAIRS:\n        cells = [f\"  {pn:<10}\"]\n        for seed in SEEDS:\n            r = results[label][seed][pn][\"method_a\"]\n            if r[\"F\"] is not None:\n                sig_mark = \"*\" if r[\"sig\"] else \" \"\n                cells.append(f\"{r['F']:6.2f} / {r['p']:.4f}{sig_mark}\")\n            else:\n                cells.append(f\"{'N/A':>20}\")\n        print(\" \".join(cells))\n    \n    # Method A detail\n    print(f\"\\n  Method A details (d_max, k, df_resid):\")\n    for _, _, pn in PAIRS:\n        for seed in SEEDS:\n            r = results[label][seed][pn][\"method_a\"]\n            print(f\"    {pn} s{seed}: dc={r['dc']}, dd={r['dd']}, d_max={r['d_max']}, k={r['k']}, df_resid={r['df_resid']} {r['note']}\")\n    \n    # Method B table\n    print(f\"\\n  Method B (statsmodels VAR, Wald chi2, d=1, AIC lag):\")\n    print(f\"  {'Pair':<10} {'s42':>20} {'s43':>20} {'s44':>20} {'s45':>20}\")\n    print(f\"  {'':10} {'chi2 / p-val':>20} {'chi2 / p-val':>20} {'chi2 / p-val':>20} {'chi2 / p-val':>20}\")\n    for _, _, pn in PAIRS:\n        cells = [f\"  {pn:<10}\"]\n        for seed in SEEDS:\n            r = results[label][seed][pn][\"method_b\"]\n            if r[\"chi2\"] is not None:\n                sig_mark = \"*\" if r[\"sig\"] else \" \"\n                cells.append(f\"{r['chi2']:6.2f} / {r['p']:.4f}{sig_mark}\")\n            else:\n                cells.append(f\"{'N/A':>20}\")\n        print(\" \".join(cells))\n\n# --- Significance summary ---\nprint(f\"\\n{'='*100}\")\nprint(\"SIGNIFICANCE SUMMARY (p < 0.05)\")\nprint(f\"{'='*100}\")\nprint(f\"\\n  {'Pair':<10} {'Method':<12} {'11pt sig_seeds':>16} {'10pt sig_seeds':>16} {'FLIP?':>8}\")\nfor _, _, pn in PAIRS:\n    for method_key, method_name in [(\"method_a\", \"OLS-F\"), (\"method_b\", \"VAR-chi2\")]:\n        sig_11 = sum(1 for s in SEEDS if results[\"11pt\"][s][pn][method_key][\"sig\"])\n        sig_10 = sum(1 for s in SEEDS if results[\"10pt\"][s][pn][method_key][\"sig\"])\n        flip = \"YES\" if sig_11 != sig_10 else \"\"\n        print(f\"  {pn:<10} {method_name:<12} {sig_11:>10}/4       {sig_10:>10}/4       {flip:>8}\")\n\n# --- FNR calculation ---\nprint(f\"\\n{'='*100}\")\nprint(\"FNR CALCULATION (using Method A = method_ablation implementation, 11pt)\")\nprint(f\"{'='*100}\")\nprint(\"\\nPer-pair sig_seeds count (p < 0.05):\")\nfnr_miss = 0\nfnr_total = len(PAIRS)\nfor _, _, pn in PAIRS:\n    sig_count = sum(1 for s in SEEDS if results[\"11pt\"][s][pn][\"method_a\"][\"sig\"])\n    status = \"DETECTED (≥3)\" if sig_count >= 3 else \"MISSED (<3)\"\n    if sig_count < 3:\n        fnr_miss += 1\n    print(f\"  {pn:<10}: {sig_count}/4 sig seeds → {status}\")\n\nfnr = fnr_miss / fnr_total\nprint(f\"\\nFNR = {fnr_miss}/{fnr_total} = {fnr:.1%}\")\nprint(f\"(Paper claims FNR=33.3% = 2/6)\")\n\n# --- Save JSON ---\noutput = {\"results\": {}, \"summary\": {}}\nfor label in [\"11pt\", \"10pt\"]:\n    output[\"results\"][label] = {}\n    for seed in SEEDS:\n        output[\"results\"][label][str(seed)] = {}\n        for _, _, pn in PAIRS:\n            output[\"results\"][label][str(seed)][pn] = results[label][seed][pn]\n\nwith open(\"/root/autodl-tmp/distrib_canary_collapse/ty_audit_results.json\", \"w\") as f:\n    json.dump(output, f, indent=2, default=str)\nprint(\"\\nResults saved to ty_audit_results.json\")\nPYEOF\necho \"Script written\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-16T00:06:21.097825+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Script written\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_ty_seed_audit_20260515T235823",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-16T00:06:21.097952+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-19828",
  "command": "cd /root/autodl-tmp/distrib_canary_collapse && python3 ty_audit.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_ty_seed_audit_20260515T235823",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-19828",
    "command": "cd /root/autodl-tmp/distrib_canary_collapse && python3 ty_audit.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-16T00:06:21.098073+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Encountered a bad command exit code!\\n\\nCommand: 'cd /root/autodl-tmp/distrib_canary_collapse && python3 ty_audit.py'\\n\\nExit code: 127\\n\\nStdout:\\n\\n\\n\\nStderr:\\n\\nbash: line 1: python3: command not found\\n\\n\", \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_ty_seed_audit_20260515T235823",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-16T00:06:21.098201+00:00_

called mcp__agent-ml-research__detect_image

<details open><summary>🔧 Tool call — mcp__agent-ml-research__detect_image</summary>

```json
{
  "server": "westd-19828",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_ty_seed_audit_20260515T235823",
  "tool": "mcp__agent-ml-research__detect_image",
  "tool_args": {
    "server": "westd-19828",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-16T00:06:21.098360+00:00_

{"result":"{\n  \"detected\": false,\n  \"status\": \"unknown\",\n  \"skip_base_setup\": false,\n  \"message\": \"No image marker file found. Use traditional env-setup flow.\"\n}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_ty_seed_audit_20260515T235823",
  "tool": "mcp__agent-ml-research__detect_image",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-16T00:06:21.098478+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "ls /root/miniconda3/bin/python3",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_ty_seed_audit_20260515T235823",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "ls /root/miniconda3/bin/python3",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-16T00:06:21.098594+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/miniconda3/bin/python3\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_ty_seed_audit_20260515T235823",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-16T00:06:21.098712+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "find /usr -name \"python3\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_ty_seed_audit_20260515T235823",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "find /usr -name \"python3\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 66 · 2026-05-16T00:06:21.098829+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "find /root -name \"python3\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_ty_seed_audit_20260515T235823",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "find /root -name \"python3\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 67 · 2026-05-16T00:06:21.098940+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.48}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_ty_seed_audit_20260515T235823",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-16T00:06:21.099049+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.77}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_ty_seed_audit_20260515T235823",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-16T00:06:21.099168+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-19828",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/distrib_canary_collapse && python ty_audit.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_ty_seed_audit_20260515T235823",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-19828",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/distrib_canary_collapse && python ty_audit.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-16T00:06:21.099367+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Seeds: [42, 43, 44, 45]\\n  seed 42: 11 points, generations [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\\n  seed 43: 11 points, generations [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\\n  seed 44: 11 points, generations [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\\n  seed 45: 11 points, generations [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\\n\\n====================================================================================================\\nTODA-YAMAMOTO AUDIT: 11-point (gen_0-gen_10) vs 10-point (gen_0-gen_9)\\n====================================================================================================\\n\\n────────────────────────────────────────────────────────────────────────────────────────────────────\\n  11PT DATA\\n─────────────────────────────────────���──────────────────────────────────────────────────────────────\\n\\n  Method A (hand OLS, F-test, ADF d_max, p=1 fixed):\\n  Pair                        s42                  s43                  s44                  s45\\n                        F / p-val            F / p-val            F / p-val            F / p-val\\n  TE→d1      311.67 / 0.0000* 199.49 / 0.0000* 501.08 / 0.0000* 388.44 / 0.0000*\\n  TE→d2      115.44 / 0.0000* 113.93 / 0.0000* 549.55 / 0.0000* 187.36 / 0.0000*\\n  TE→d3      101.37 / 0.0000* 110.55 / 0.0000* 232.19 / 0.0000* 138.65 / 0.0000*\\n  ECE→d1     785.93 / 0.0000* 3369.54 / 0.0000*   2.74 / 0.1729   11.47 / 0.0276*\\n  ECE→d2     124.17 / 0.0000* 201.93 / 0.0000*   1.00 / 0.3734    0.32 / 0.5995 \\n  ECE→d3      74.03 / 0.0001* 113.35 / 0.0000*   2.01 / 0.2294    0.38 / 0.5725 \\n\\n  Method A details (d_max, k, df_resid):\\n    TE→d1 s42: dc=0, dd=0, d_max=0, k=1, df_resid=7 \\n    TE→d1 s43: dc=0, dd=0, d_max=0, k=1, df_resid=7 \\n    TE→d1 s44: dc=0, dd=0, d_max=0, k=1, df_resid=7 \\n    TE→d1 s45: dc=0, dd=0, d_max=0, k=1, df_resid=7 \\n    TE→d2 s42: dc=0, dd=0, d_max=0, k=1, df_resid=7 \\n    TE→d2 s43: dc=0, dd=0, d_max=0, k=1, df_resid=7
…[truncated 6480 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_ty_seed_audit_20260515T235823",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 71 · 2026-05-16T00:06:21.099549+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "cat /root/autodl-tmp/distrib_canary_collapse/ty_audit_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_ty_seed_audit_20260515T235823",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "cat /root/autodl-tmp/distrib_canary_collapse/ty_audit_results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-16T00:06:21.099893+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"results\\\": {\\n    \\\"11pt\\\": {\\n      \\\"42\\\": {\\n        \\\"TE\\\\u2192d1\\\": {\\n          \\\"method_a\\\": {\\n            \\\"F\\\": 311.6695,\\n            \\\"p\\\": 0.0,\\n            \\\"sig\\\": true,\\n            \\\"d_max\\\": 0,\\n            \\\"p_lag\\\": 1,\\n            \\\"k\\\": 1,\\n            \\\"df_resid\\\": 7,\\n            \\\"dc\\\": 0,\\n            \\\"dd\\\": 0,\\n            \\\"note\\\": \\\"\\\"\\n          },\\n          \\\"method_b\\\": {\\n            \\\"chi2\\\": 1.5675,\\n            \\\"p\\\": 0.666775,\\n            \\\"sig\\\": false,\\n            \\\"p_lag\\\": 2,\\n            \\\"d\\\": 1,\\n            \\\"note\\\": \\\"\\\"\\n          }\\n        },\\n        \\\"TE\\\\u2192d2\\\": {\\n          \\\"method_a\\\": {\\n            \\\"F\\\": 115.4437,\\n            \\\"p\\\": 1.3e-05,\\n            \\\"sig\\\": true,\\n            \\\"d_max\\\": 0,\\n            \\\"p_lag\\\": 1,\\n            \\\"k\\\": 1,\\n            \\\"df_resid\\\": 7,\\n            \\\"dc\\\": 0,\\n            \\\"dd\\\": 0,\\n            \\\"note\\\": \\\"\\\"\\n          },\\n          \\\"method_b\\\": {\\n            \\\"chi2\\\": 1.215,\\n            \\\"p\\\": 0.749403,\\n            \\\"sig\\\": false,\\n            \\\"p_lag\\\": 2,\\n            \\\"d\\\": 1,\\n            \\\"note\\\": \\\"\\\"\\n          }\\n        },\\n        \\\"TE\\\\u2192d3\\\": {\\n          \\\"method_a\\\": {\\n            \\\"F\\\": 101.3651,\\n            \\\"p\\\": 2e-05,\\n            \\\"sig\\\": true,\\n            \\\"d_max\\\": 0,\\n            \\\"p_lag\\\": 1,\\n            \\\"k\\\": 1,\\n            \\\"df_resid\\\": 7,\\n            \\\"dc\\\": 0,\\n            \\\"dd\\\": 0,\\n            \\\"note\\\": \\\"\\\"\\n          },\\n          \\\"method_b\\\": {\\n            \\\"chi2\\\": 1.4119,\\n            \\\"p\\\": 0.702739,\\n            \\\"sig\\\": false,\\n   
…[truncated 9053 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_ty_seed_audit_20260515T235823",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 73 · 2026-05-16T00:06:21.100086+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "cat /root/autodl-tmp/distrib_canary_collapse/window_sensitivity_report.md",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_ty_seed_audit_20260515T235823",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "cat /root/autodl-tmp/distrib_canary_collapse/window_sensitivity_report.md",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 74 · 2026-05-16T00:06:21.100290+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"# Observation Window Sensitivity Analysis\\n## Pythia-410M, α=1.0, 4 seeds (42–45)\\n\\n**Goal**: Test robustness of 5-method consensus to observation window length T.\\nFor each T, we use generations 0 to T−1 (T data points).\\n6 forward pairs: entropy→{d1,d2,d3}, ECE→{d1,d2,d3}.\\n\\n## Table 1: Consensus Stability by Window Length\\n\\nCell = pairs (of 6) where ≥3/4 seeds show significance.\\n\\n| T | Robust pairs | Naive xcorr | Diff xcorr | Threshold | Perm Granger | TY |\\n|:---:|:---:|:---:|:---:|:---:|:---:|:---:|\\n| 5 | **0/6** | 6/6 | 6/6 | 6/6 | 0/6 | 0/6 |\\n| 6 | **6/6** | 6/6 | 6/6 | 6/6 | 6/6 | 0/6 |\\n| 7 | **6/6** | 6/6 | 6/6 | 6/6 | 6/6 | 0/6 |\\n| 8 | **6/6** | 6/6 | 6/6 | 6/6 | 6/6 | 0/6 |\\n| 9 | **6/6** | 6/6 | 6/6 | 6/6 | 6/6 | 0/6 |\\n| 10 | **6/6** | 6/6 | 6/6 | 6/6 | 6/6 | 1/6 |\\n\\n**TY feasibility note**: Toda-Yamamoto requires VAR(p+d) estimation. With d=1 and optimal p≥1, the augmented model needs p+d+1 parameters per equation × 2 equations. For T≤7, this often leaves insufficient residual df, producing infeasible fits. This is intrinsic to the method, not the data.\\n\\n- T=5: 0/24 feasible TY tests\\n- T=6: 0/24 feasible TY tests\\n- T=7: 0/24 feasible TY tests\\n- T=8: 0/24 feasible TY tests\\n- T=9: 24/24 feasible TY tests\\n- T=10: 24/24 feasible TY tests\\n\\n## Table 2: Method Sensitivity to T\\n\\nSmallest T where each method's conclusion matches T=10 and stays stable.\\n\\n| Method | Stable from T= | Pairs stable ≤T=5 | Pairs stable ≤T=6 | Notes |\\n|---|:---:|:---:|:---:|---|\\n| Naive xcorr | 5 | 6/6 | 6/6 | All stable |\\n| Diff xcorr | 5 | 6/6 | 6/6 | All stable |\\n| Threshold | 5 | 6/6 | 6/6 | All stable |\\n| Perm Granger | 6 | 0/6 | 6/6 | All stable |\\n| Toda-Yamamoto | 5 | 5/6 | 5/6 | Unstable: ECE→d3 |\\n\\n## Table 3: Per-pair Significance Matrix\\n\\nMethods with ≥3/4 seed consensus. **Bold** = robust (≥4/5 methods).\\n\\n| Pair | T=5 | T=6 | T=7 | T=8 | T=9
…[truncated 5776 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_ty_seed_audit_20260515T235823",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 75 · 2026-05-16T00:06:21.100517+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-19828",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 -c \"\nimport json\nwith open('/root/autodl-tmp/distrib_canary_collapse/ty_audit_results.json') as f:\n    data = json.load(f)\n\nfor label in ['11pt', '10pt']:\n    print(f'\\\\n=== {label} Method A ===')\n    print(f'{\\\"Pair\\\":<10} {\\\"s42\\\":>20} {\\\"s43\\\":>20} {\\\"s44\\\":>20} {\\\"s45\\\":>20}')\n    for pn in ['TE→d1', 'TE→d2', 'TE→d3', 'ECE→d1', 'ECE→d2', 'ECE→d3']:\n        cells = [f'{pn:<10}']\n        for s in ['42','43','44','45']:\n            r = data['results'][label][s][pn]['method_a']\n            if r['F'] is not None:\n                sig = '*' if r['sig'] else ' '\n                cells.append(f\\\"F={r['F']:7.2f} p={r['p']:.4f}{sig}\\\")\n            else:\n                cells.append('N/A')\n        print(' '.join(cells))\n    print(f'\\\\n=== {label} Method B ===')\n    print(f'{\\\"Pair\\\":<10} {\\\"s42\\\":>20} {\\\"s43\\\":>20} {\\\"s44\\\":>20} {\\\"s45\\\":>20}')\n    for pn in ['TE→d1', 'TE→d2', 'TE→d3', 'ECE→d1', 'ECE→d2', 'ECE→d3']:\n        cells = [f'{pn:<10}']\n        for s in ['42','43','44','45']:\n            r = data['results'][label][s][pn]['method_b']\n            if r['chi2'] is not None:\n                import math\n                if math.isnan(r['chi2']):\n                    cells.append('NaN')\n                else:\n                    sig = '*' if r['sig'] else ' '\n                    cells.append(f\\\"X2={r['chi2']:7.2f} p={r['p']:.4f}{sig}\\\")\n            else:\n                cells.append('N/A')\n        print(' '.join(cells))\n\"\n",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_ty_seed_audit_20260515T235823",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-19828",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 -c \"\nimport json\nwith open('/root/autodl-tmp/distrib_canary_collapse/ty_audit_results.json') as f:\n    data = json.load(f)\n\nfor label in ['11pt', '10pt']:\n    print(f'\\\\n=== {label} Method A ===')\n    print(f'{\\\"Pair\\\":<10} {\\\"s42\\\":>20} {\\\"s43\\\":>20} {\\\"s44\\\":>20} {\\\"s45\\\":>20}')\n    for pn in ['TE→d1', 'TE→d2', 'TE→d3', 'ECE→d1', 'ECE→d2', 'ECE→d3']:\n        cells = [f'{pn:<10}']\n        for s in ['42','43','44','45']:\n            r = data['results'][label][s][pn]['method_a']\n            if r['F'] is not None:\n                sig = '*' if r['sig'] else ' '\n                cells.append(f\\\"F={r['F']:7.2f} p={r['p']:.4f}{sig}\\\")\n            else:\n                cells.append('N/A')\n        print(' '.join(cells))\n    print(f'\\\\n=== {label} Method B ===')\n    print(f'{\\\"Pair\\\":<10} {\\\"s42\\\":>20} {\\\"s43\\\":>20} {\\\"s44\\\":>20} {\\\"s45\\\":>20}')\n    for pn in ['TE→d1', 'TE→d2', 'TE→d3', 'ECE→d1', 'ECE→d2', 'ECE→d3']:\n        cells = [f'{pn:<10}']\n        for s in ['42','43','44','45']:\n            r = data['results'][label][s][pn]['method_b']\n            if r['chi2'] is not None:\n                import math\n                if math.isnan(r['chi2']):\n                    cells.append('NaN')\n                else:\n                    sig = '*' if r['sig'] else ' '\n                    cells.append(f\\\"X2={r['chi2']:7.2f} p={r['p']:.4f}{sig}\\\")\n            else:\n                cells.append('N/A')\n        print(' '.join(cells))\n\"\n",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 76 · 2026-05-16T00:06:21.100703+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\n=== 11pt Method A ===\\nPair                        s42                  s43                  s44                  s45\\nTE→d1      F= 311.67 p=0.0000* F= 199.49 p=0.0000* F= 501.08 p=0.0000* F= 388.44 p=0.0000*\\nTE→d2      F= 115.44 p=0.0000* F= 113.93 p=0.0000* F= 549.55 p=0.0000* F= 187.36 p=0.0000*\\nTE→d3      F= 101.37 p=0.0000* F= 110.55 p=0.0000* F= 232.19 p=0.0000* F= 138.65 p=0.0000*\\nECE→d1     F= 785.93 p=0.0000* F=3369.54 p=0.0000* F=   2.74 p=0.1729  F=  11.47 p=0.0276*\\nECE→d2     F= 124.17 p=0.0000* F= 201.93 p=0.0000* F=   1.00 p=0.3734  F=   0.32 p=0.5995 \\nECE→d3     F=  74.03 p=0.0001* F= 113.35 p=0.0000* F=   2.01 p=0.2294  F=   0.38 p=0.5725 \\n\\n=== 11pt Method B ===\\nPair                        s42                  s43                  s44                  s45\\nTE→d1      X2=   1.57 p=0.6668  X2=   5.17 p=0.1596  X2=   7.61 p=0.0548  X2=   2.68 p=0.2613 \\nTE→d2      X2=   1.22 p=0.7494  X2=   6.76 p=0.0799  X2=   2.10 p=0.5525  X2=   1.41 p=0.7041 \\nTE→d3      X2=   1.41 p=0.7027  X2=   1.46 p=0.6923  X2=   0.98 p=0.8069  X2=   0.49 p=0.9212 \\nECE→d1     X2= 123.33 p=0.0000* X2=   3.42 p=0.3311  X2=   9.78 p=0.0205* X2=  35.75 p=0.0000*\\nECE→d2     X2=  35.86 p=0.0000* X2=   1.93 p=0.5867  X2=   9.99 p=0.0186* X2=  18.81 p=0.0003*\\nECE→d3     X2= 433.91 p=0.0000* X2=   5.37 p=0.1469  X2=   1.20 p=0.7532  X2=  26.35 p=0.0000*\\n\\n=== 10pt Method A ===\\nPair                        s42                  s43                  s44                  s45\\nTE→d1      F= 272.80 p=0.0000* F= 208.96 p=0.0000* F= 483.31 p=0.0000* F= 486.70 p=0.0000*\\nTE→d2      F= 101.61 p=0.0001* F= 116.14 p=0.0000* F= 489.48 p=0.0000* F= 198.85 p=0.0000*\\nTE→d3      F=  86.80 p=0.0001* F= 111.49 p=0.0000* F= 200.69 p=0.0000* F= 138.40 p=0.0000*\\nECE→d1     F=1110.61 p=0.0000* F=2991.05 p=0.0000* F=   3.20 p=0.1714  F=   7.78 p=0.0685 \\nECE→d2     F= 106.12 p=0.0000* F= 186.19 p=0.0000* F=   5.16
…[truncated 545 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_ty_seed_audit_20260515T235823",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 77 · 2026-05-16T00:06:21.100900+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "head -60 /root/autodl-tmp/distrib_canary_collapse/method_ablation_phase2.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_ty_seed_audit_20260515T235823",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "head -60 /root/autodl-tmp/distrib_canary_collapse/method_ablation_phase2.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 78 · 2026-05-16T00:06:21.101063+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Method Ablation Phase 2: Pooled Panel Analysis across alpha regimes.\\n\\nExtends Phase 1 (alpha=1.0, 4 seeds, 16 pairs) to all completed alpha levels.\\nCore evidence for Claim 3: method sensitivity compounded by regime dependence.\\n\\nInput:\\n  - results/alpha_sweep/a{NNN}_s42/all_metrics.json (alpha=0.00,0.25,0.50)\\n  - results/mvp/rep_{42..45}/all_metrics.json (alpha=1.00)\\n\\nOutput:\\n  - results/method_ablation_phase2_panel.json\\n  - results/method_ablation_phase2_report.md\\n\\\"\\\"\\\"\\n\\nimport json\\nimport os\\nimport re\\nimport sys\\nimport warnings\\nfrom collections import defaultdict\\nfrom datetime import datetime\\nfrom itertools import product\\n\\nimport numpy as np\\nfrom scipy import stats\\nfrom statsmodels.stats.multitest import multipletests\\n\\nfrom method_ablation import (\\n    naive_pearson, diff_xcorr, threshold_lead, toda_yamamoto,\\n    extract, orient, ALPHA,\\n)\\nfrom permutation_granger import permutation_granger_test\\n\\nwarnings.filterwarnings(\\\"ignore\\\")\\n\\nCANARY = [\\\"token_entropy\\\", \\\"ece\\\"]\\nDOWNSTREAM = [\\\"distinct_1\\\", \\\"distinct_2\\\", \\\"distinct_3\\\", \\\"perplexity\\\"]\\nMETHOD_NAMES = [\\\"naive\\\", \\\"differenced\\\", \\\"threshold\\\", \\\"permutation_granger\\\", \\\"TY\\\"]\\nN_PERM = 1000\\n\\n\\ndef load_all_data(base_dir):\\n    data = []\\n\\n    sweep_dir = os.path.join(base_dir, \\\"results\\\", \\\"alpha_sweep\\\")\\n    pat = re.compile(r\\\"^a(\\\\d{3})_s(\\\\d+)$\\\")\\n    if os.path.isdir(sweep_dir):\\n        for name in sorted(os.listdir(sweep_dir)):\\n            m = pat.match(name)\\n            if not m:\\n                continue\\n            path = os.path.join(sweep_dir, name, \\\"all_metrics.json\\\")\\n            if not os.path.isfile(path):\\n                continue\\n            alpha = int(m.group(1)) / 100.0\\n            seed = int(m.group(2))\\n            with open(path) as f:\\
…[truncated 256 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_ty_seed_audit_20260515T235823",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 79 · 2026-05-16T00:06:21.101207+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "grep -n \"toda_yamamoto\" /root/autodl-tmp/distrib_canary_collapse/method_ablation_phase2.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_ty_seed_audit_20260515T235823",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "grep -n \"toda_yamamoto\" /root/autodl-tmp/distrib_canary_collapse/method_ablation_phase2.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 80 · 2026-05-16T00:06:21.101349+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"29:    naive_pearson, diff_xcorr, threshold_lead, toda_yamamoto,\\n114:    r = toda_yamamoto(c, d, cn, dn)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_ty_seed_audit_20260515T235823",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 81 · 2026-05-16T00:06:21.101508+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "cat /root/autodl-tmp/distrib_canary_collapse/results/mvp/analysis/method_ablation.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_ty_seed_audit_20260515T235823",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "cat /root/autodl-tmp/distrib_canary_collapse/results/mvp/analysis/method_ablation.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 82 · 2026-05-16T00:06:21.101833+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"meta\\\": {\\n    \\\"seeds\\\": [\\n      42,\\n      43,\\n      44,\\n      45\\n    ],\\n    \\\"alpha\\\": 0.05,\\n    \\\"canary_metrics\\\": [\\n      \\\"token_entropy\\\",\\n      \\\"self_bleu\\\",\\n      \\\"ece\\\",\\n      \\\"effective_rank\\\"\\n    ],\\n    \\\"downstream_metrics\\\": [\\n      \\\"perplexity\\\",\\n      \\\"distinct_1\\\",\\n      \\\"distinct_2\\\",\\n      \\\"distinct_3\\\"\\n    ],\\n    \\\"methods\\\": [\\n      \\\"naive_pearson: raw-level Pearson lag-correlation\\\",\\n      \\\"differenced_xcorr: first-differenced cross-correlation\\\",\\n      \\\"threshold_onset: 2-sigma signal-onset lead time\\\",\\n      \\\"toda_yamamoto: augmented-lag Granger causality (Wald F-test)\\\",\\n      \\\"permutation_granger: differenced + shuffle permutation Granger (F-test)\\\"\\n    ]\\n  },\\n  \\\"summary\\\": {\\n    \\\"total_pairs\\\": 16,\\n    \\\"naive_significant\\\": 16,\\n    \\\"differenced_significant\\\": 14,\\n    \\\"threshold_significant\\\": 9,\\n    \\\"ty_significant\\\": 4,\\n    \\\"perm_granger_significant\\\": 6,\\n    \\\"spurious_count\\\": 12,\\n    \\\"spurious_rate\\\": 0.75,\\n    \\\"spurious_pairs\\\": [\\n      {\\n        \\\"canary\\\": \\\"token_entropy\\\",\\n        \\\"downstream\\\": \\\"perplexity\\\"\\n      },\\n      {\\n        \\\"canary\\\": \\\"self_bleu\\\",\\n        \\\"downstream\\\": \\\"perplexity\\\"\\n      },\\n      {\\n        \\\"canary\\\": \\\"self_bleu\\\",\\n        \\\"downstream\\\": \\\"distinct_1\\\"\\n      },\\n      {\\n        \\\"canary\\\": \\\"self_bleu\\\",\\n        \\\"downstream\\\": \\\"distinct_2\\\"\\n      },\\n      {\\n        \\\"canary\\\": \\\"self_bleu\\\",\\n        \\\"downstream\\\": \\\"distinct_3\\\"\\n      },\\n      {\\n        \\\"canary\\\": \\\"ece\\\",\\n        \\\"downstream\\\": \\\"perplexity\\\"\\n      },\\n      {\\n        \\\"canary\\\": \\\"ece\\\",\\n        \\
…[truncated 8595 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_ty_seed_audit_20260515T235823",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 83 · 2026-05-16T00:06:21.102064+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:TodoWrite",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_ty_seed_audit_20260515T235823",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:TodoWrite",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 84 · 2026-05-16T00:06:21.102187+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_ty_seed_audit_20260515T235823",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 85 · 2026-05-16T00:06:21.102320+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'SSH to server, find data and scripts', 'status': 'completed', 'activeForm': 'Exploring server data and scripts'}, {'content': 'Run TY audit with 11pt and 10pt data', 'status': 'completed', 'activeForm': 'Running TY audit'}, {'content': 'Identify off-by-one bug and implementation differences', 'status': 'completed', 'activeForm': 'Analyzing script bugs'}, {'content': 'Write comprehensive audit report', 'status': 'in_progress', 'activeForm': 'Writing audit report'}, {'content': 'Register artifact', 'status': 'pending', 'activeForm': 'Registering artifact'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_ty_seed_audit_20260515T235823",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'SSH to server, find data and scripts', 'status': 'completed', 'activeForm': 'Exploring server data and scripts'}, {'content': 'Run TY audit with 11pt and 10pt data', 'status': 'completed', 'activeForm': 'Running TY audit'}, {'content': 'Identify off-by-one bug and implementation differences', 'status': 'completed', 'activeForm': 'Analyzing script bugs'}, {'content': 'Write comprehensive audit report', 'status': 'in_progress', 'activeForm': 'Writing audit report'}, {'content': 'Register artifact', 'status': 'pending', 'activeForm': 'Registering artifact'}]"
  }
}
```

</details>

---

### Tool result

_source line 86 · 2026-05-16T00:06:21.102451+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_ty_seed_audit_20260515T235823",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 87 · 2026-05-16T00:06:21.102569+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/ty_seed_audit",
  "description": "Create audit report directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_ty_seed_audit_20260515T235823",
  "tool": "Bash",
  "tool_args": {
    "command": "mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/ty_seed_audit",
    "description": "Create audit report directory"
  }
}
```

</details>

---

### Tool result

_source line 88 · 2026-05-16T00:06:21.102677+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_ty_seed_audit_20260515T235823",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 89 · 2026-05-16T00:06:21.102840+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

````json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/ty_seed_audit/ty_audit_report.md",
  "content": "# Toda-Yamamoto Full Seed Audit Report\n\n**Date**: 2026-05-16\n**Data**: Pythia-410M, α=1.0, seeds 42/43/44/45, gen_0–gen_10 (11 data points)\n\n---\n\n## 1. Executive Summary\n\n| Finding | Status |\n|---------|--------|\n| Off-by-one bug in `window_sensitivity.py` | **CONFIRMED** |\n| Two incompatible TY implementations across scripts | **CONFIRMED** |\n| Paper FNR=33.3% (2/6) | **CORRECT** |\n| Paper ECE→d1 sig_seeds=3/4 | **CORRECT** |\n| Window sensitivity TY results (all TE p>0.3) | **WRONG** (caused by both bugs) |\n\n---\n\n## 2. Bug #1: Off-by-One in window_sensitivity.py\n\n**Location**: `window_sensitivity.py` line 193\n\n```python\nmetrics = all_data[seed][:T]  # gen_0 to gen_{T-1}\n```\n\nWhen T=10, this takes `[:10]` = 10 data points (gen_0 to gen_9). The paper convention \"T=10 generations\" means gen_0 through gen_10 = **11 data points**.\n\nMeanwhile, `method_ablation.py` uses `extract(data[seed], cn)` which extracts the full list — all 11 data points.\n\n**Impact**: For Method A (OLS-F), ECE→d1 flips from 3/4 sig (11pt) to 2/4 sig (10pt). See Section 4 for details.\n\n---\n\n## 3. Bug #2: Two Incompatible TY Implementations\n\n| Parameter | Method A (`method_ablation.py`) | Method B (`window_sensitivity.py`) |\n|-----------|-------------------------------|-----------------------------------|\n| d_max | ADF test per series (`_adf_order`) | Hardcoded d=1 |\n| Lag order p | Fixed p=1 | AIC-selected (typically p=2) |\n| Test statistic | F-test (hand-coded OLS + Wald) | χ² (statsmodels `test_causality`) |\n| Total lags k | p + d_max (varies 1–3) | p + 1 (typically 3) |\n\n**Root cause of TE→d discrepancy**: ADF correctly identifies token_entropy and distinct_* as I(0) at α=1.0 (the series plateau after ~4 generations). With d_max=0, Method A fits VAR(1) with df_resid=7, yielding massive F statistics (100–500). Method B hardcodes d=1, forces VAR(3), exhausts degrees of freedom → all TE pairs non-significant.\n\n**Paper uses Method A** (confirmed: `method_ablation_phase2.py` imports `toda_yamamoto` from `method_ablation.py`).\n\n---\n\n## 4. Complete P-Value Tables\n\n### 4a. 11-Point Data (gen_0 to gen_10) — Method A (paper implementation)\n\n| Pair | s42 | s43 | s44 | s45 | sig_seeds |\n|------|-----|-----|-----|-----|-----------|\n| TE→d1 | F=311.67, **p<.0001*** | F=199.49, **p<.0001*** | F=501.08, **p<.0001*** | F=388.44, **p<.0001*** | **4/4** |\n| TE→d2 | F=115.44, **p<.0001*** | F=113.93, **p<.0001*** | F=549.55, **p<.0001*** | F=187.36, **p<.0001*** | **4/4** |\n| TE→d3 | F=101.37, **p<.0001*** | F=110.55, **p<.0001*** | F=232.19, **p<.0001*** | F=138.65, **p<.0001*** | **4/4** |\n| ECE→d1 | F=785.93, **p<.0001*** | F=3369.54, **p<.0001*** | F=2.74, p=.1729 | F=11.47, **p=.0276*** | **3/4** |\n| ECE→d2 | F=124.17, **p<.0001*** | F=201.93, **p<.0001*** | F=1.00, p=.3734 | F=0.32, p=.5995 | **2/4** |\n| ECE→d3 | F=74.03, **p=.0001*** | F=113.35, **p<.0001*** | F=2.01, p=.2294 | F=0.38, p=.5725 | **2/4** |\n\nADF-derived parameters:\n- TE pairs (all seeds): dc=0, dd=0, d_max=0, k=1, **df_resid=7**\n- ECE pairs s42/s43: dc=0, dd=0, d_max=0, k=1, **df_resid=7**\n- ECE pairs s44/s45: dc=1, dd=0, d_max=1, k=2, **df_resid=4**\n\n### 4b. 10-Point Data (gen_0 to gen_9) — Method A\n\n| Pair | s42 | s43 | s44 | s45 | sig_seeds |\n|------|-----|-----|-----|-----|-----------|\n| TE→d1 | F=272.80, **p<.0001*** | F=208.96, **p<.0001*** | F=483.31, **p<.0001*** | F=486.70, **p<.0001*** | **4/4** |\n| TE→d2 | F=101.61, **p=.0001*** | F=116.14, **p<.0001*** | F=489.48, **p<.0001*** | F=198.85, **p<.0001*** | **4/4** |\n| TE→d3 | F=86.80, **p=.0001*** | F=111.49, **p<.0001*** | F=200.69, **p<.0001*** | F=138.40, **p<.0001*** | **4/4** |\n| ECE→d1 | F=1110.61, **p<.0001*** | F=2991.05, **p<.0001*** | F=3.20, p=.1714 | F=7.78, p=.0685 | **2/4** |\n| ECE→d2 | F=106.12, **p<.0001*** | F=186.19, **p<.0001*** | F=5.16, p=.1079 | F=0.25, p=.6527 | **2/4** |\n| ECE→d3 | F=62.91, **p=.0002*** | F=105.46, **p=.0001*** | F=0.03, p=.8736 | F=0.28, p=.6345 | **2/4** |\n\n10pt ECE pairs s44/s45: dc=1, dd=0, d_max=1, k=2, **df_resid=3** (vs 4 with 11pt)\n\n### 4c. 11-Point Data — Method B (window_sensitivity implementation)\n\n| Pair | s42 | s43 | s44 | s45 | sig_seeds |\n|------|-----|-----|-----|-----|-----------|\n| TE→d1 | χ²=1.57, p=.667 | χ²=5.17, p=.160 | χ²=7.61, p=.055 | χ²=2.68, p=.261 | **0/4** |\n| TE→d2 | χ²=1.22, p=.749 | χ²=6.76, p=.080 | χ²=2.10, p=.553 | χ²=1.41, p=.704 | **0/4** |\n| TE→d3 | χ²=1.41, p=.703 | χ²=1.46, p=.692 | χ²=0.98, p=.807 | χ²=0.49, p=.921 | **0/4** |\n| ECE→d1 | χ²=123.33, **p<.0001*** | χ²=3.42, p=.331 | χ²=9.78, **p=.021*** | χ²=35.75, **p<.0001*** | **3/4** |\n| ECE→d2 | χ²=35.86, **p<.0001*** | χ²=1.93, p=.587 | χ²=9.99, **p=.019*** | χ²=18.81, **p=.0003*** | **3/4** |\n| ECE→d3 | χ²=433.91, **p<.0001*** | χ²=5.37, p=.147 | χ²=1.20, p=.753 | χ²=26.35, **p<.0001*** | **2/4** |\n\n### 4d. 10-Point Data — Method B\n\n| Pair | s42 | s43 | s44 | s45 | sig_seeds |\n|------|-----|-----|-----|-----|-----------|\n| TE→d1–d3 | NaN | NaN | NaN | NaN | **0/4** |\n| ECE→d1 | NaN | NaN | NaN | χ²=8.32, **p=.016*** | **1/4** |\n| ECE→d2–d3 | NaN | NaN | NaN | NaN | **0/4** |\n\nMethod B with 10 points: VAR(3) on 10 observations → near-singular, statsmodels returns NaN for most fits.\n\n---\n\n## 5. 11-Point vs 10-Point Conclusion Differences\n\n### Method A (paper implementation)\n\n| Pair | 11pt sig_seeds | 10pt sig_seeds | Flipped? |\n|------|---------------|---------------|----------|\n| TE→d1 | 4/4 | 4/4 | No |\n| TE→d2 | 4/4 | 4/4 | No |\n| TE→d3 | 4/4 | 4/4 | No |\n| ECE→d1 | **3/4** | **2/4** | **YES** |\n| ECE→d2 | 2/4 | 2/4 | No |\n| ECE→d3 | 2/4 | 2/4 | No |\n\n**ECE→d1 flip mechanism**: Seed 45 goes from p=0.0276 (11pt, sig) to p=0.0685 (10pt, marginal ns). Adding gen_10 increases df_resid from 3 to 4 AND provides one more observation point, just enough to push this marginal case over the threshold.\n\n### Method B (window_sensitivity implementation)\n\n| Pair | 11pt sig_seeds | 10pt sig_seeds | Flipped? |\n|------|---------------|---------------|----------|\n| TE→d1–d3 | 0/4 | 0/4 | No |\n| ECE→d1 | **3/4** | **1/4** | **YES** |\n| ECE→d2 | **3/4** | **0/4** | **YES** |\n| ECE→d3 | 2/4 | 0/4 | **YES** |\n\nMethod B is far more sensitive to the one-point difference because VAR(3) on 10 points has essentially zero residual df.\n\n---\n\n## 6. Why Window Sensitivity Report Shows TE p>0.3\n\nThe window sensitivity report (T=10, 10 data points) used Method B:\n- TE→d1 s42: p=0.980, s43: p=0.885, s44: p=0.995, s45: p=0.983\n\nThis is caused by **Bug #2**, not Bug #1. Even with 11 points, Method B gives p=0.667, 0.160, 0.055, 0.261 for TE→d1 — all non-significant.\n\nThe hardcoded d=1 + AIC lag selection (p=2) creates a VAR(3) model that consumes all degrees of freedom testing TE→d_i, while the data is actually I(0) and needs only VAR(1).\n\n---\n\n## 7. ECE→d1: ablation vs paper\n\n| Source | ECE→d1 sig_seeds | Implementation |\n|--------|------------------|----------------|\n| method_ablation.json (robust_pairs) | ≥3/4 → SIGNIFICANT | Method A, 11pt |\n| This audit, Method A, 11pt | 3/4 (s42✓ s43✓ s44✗ s45✓) | Confirmed |\n| Paper method.tex | 3/4 | Matches Method A |\n\n**Answer**: Paper is correct (3/4 sig). If an earlier ablation draft said 2/4, it was either using 10-point data or a different run.\n\n---\n\n## 8. FNR Recalculation\n\nUsing Method A (paper implementation), 11-point data, threshold ≥3/4 seeds:\n\n| Pair | sig_seeds | Status |\n|------|-----------|--------|\n| TE→d1 | 4/4 | DETECTED |\n| TE→d2 | 4/4 | DETECTED |\n| TE→d3 | 4/4 | DETECTED |\n| ECE→d1 | 3/4 | DETECTED |\n| ECE→d2 | 2/4 | MISSED |\n| ECE→d3 | 2/4 | MISSED |\n\n**FNR = 2/6 = 33.3%** — Paper's claim is correct.\n\nECE→d2 and ECE→d3 miss because seeds 44 and 45 have ECE classified as I(1) by ADF, triggering d_max=1, k=2, df_resid=4, which severely limits power. Seeds 42 and 43 have ECE classified as I(0), giving df_resid=7 and strong significance.\n\n---\n\n## 9. Root Cause: ECE Stationarity is Seed-Dependent\n\nThe split in ECE pair results (s42/s43 sig, s44/s45 ns) traces to ADF stationarity classification:\n\n| Seed | ECE at gen_5–10 range | ADF classification | d_max | df_resid |\n|------|----------------------|-------------------|-------|----------|\n| 42 | 0.390–0.417 (flat) | I(0) | 0 | 7 |\n| 43 | 0.394–0.420 (flat) | I(0) | 0 | 7 |\n| 44 | 0.393–0.424 (slight upward) | I(1) | 1 | 4 |\n| 45 | 0.386–0.417 (slight upward) | I(1) | 1 | 4 |\n\nSeeds 44/45 have a marginally detectable upward trend in ECE's late plateau, causing ADF to classify ECE as I(1). This adds an augmentation lag, cutting df_resid from 7 to 4 and destroying power.\n\nThis is a genuine statistical limitation, not a bug. The FNR reflects real power constraints with T=10.\n\n---\n\n## 10. Summary of Bugs and Corrections Needed\n\n### Must fix:\n1. **`window_sensitivity.py` line 193**: Change `all_data[seed][:T]` to `all_data[seed][:T+1]` to use T+1 data points for \"T generations\"\n2. **`window_sensitivity.py` TY implementation**: The `toda_yamamoto_v2` function is fundamentally different from the paper's TY. The report should either:\n   - (a) Use the same `toda_yamamoto` from `method_ablation.py`, OR\n   - (b) Clearly label the results as using a different TY variant\n\n### No fix needed:\n- Paper FNR=33.3% is correct\n- Paper ECE→d1 sig_seeds=3/4 is correct\n- Method A implementation is sound\n\n### Constraint C001 status:\nThe audit confirms that TY results at α=1.0 are consistent across seeds for TE pairs (4/4) but seed-dependent for ECE pairs (due to ADF classification). This is within-α behavior and does NOT address the cross-α non-monotonicity flagged in C001. The constraint remains in effect.\n"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "worker_analysis_ty_seed_audit_20260515T235823",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/ty_seed_audit/ty_audit_report.md",
    "content": "# Toda-Yamamoto Full Seed Audit Report\n\n**Date**: 2026-05-16\n**Data**: Pythia-410M, α=1.0, seeds 42/43/44/45, gen_0–gen_10 (11 data points)\n\n---\n\n## 1. Executive Summary\n\n| Finding | Status |\n|---------|--------|\n| Off-by-one bug in `window_sensitivity.py` | **CONFIRMED** |\n| Two incompatible TY implementations across scripts | **CONFIRMED** |\n| Paper FNR=33.3% (2/6) | **CORRECT** |\n| Paper ECE→d1 sig_seeds=3/4 | **CORRECT** |\n| Window sensitivity TY results (all TE p>0.3) | **WRONG** (caused by both bugs) |\n\n---\n\n## 2. Bug #1: Off-by-One in window_sensitivity.py\n\n**Location**: `window_sensitivity.py` line 193\n\n```python\nmetrics = all_data[seed][:T]  # gen_0 to gen_{T-1}\n```\n\nWhen T=10, this takes `[:10]` = 10 data points (gen_0 to gen_9). The paper convention \"T=10 generations\" means gen_0 through gen_10 = **11 data points**.\n\nMeanwhile, `method_ablation.py` uses `extract(data[seed], cn)` which extracts the full list — all 11 data points.\n\n**Impact**: For Method A (OLS-F), ECE→d1 flips from 3/4 sig (11pt) to 2/4 sig (10pt). See Section 4 for details.\n\n---\n\n## 3. Bug #2: Two Incompatible TY Implementations\n\n| Parameter | Method A (`method_ablation.py`) | Method B (`window_sensitivity.py`) |\n|-----------|-------------------------------|-----------------------------------|\n| d_max | ADF test per series (`_adf_order`) | Hardcoded d=1 |\n| Lag order p | Fixed p=1 | AIC-selected (typically p=2) |\n| Test statistic | F-test (hand-coded OLS + Wald) | χ² (statsmodels `test_causality`) |\n| Total lags k | p + d_max (varies 1–3) | p + 1 (typically 3) |\n\n**Root cause of TE→d discrepancy**: ADF correctly identifies token_entropy and distinct_* as I(0) at α=1.0 (the series plateau after ~4 generations). With d_max=0, Method A fits VAR(1) with df_resid=7, yielding massive F statistics (100–500). Method B hardcodes d=1, forces VAR(3), exhausts degrees of freedom → all TE pairs non-significant.\n\n**Paper uses Method A** (confirmed: `method_ablation_phase2.py` imports `toda_yamamoto` from `method_ablation.py`).\n\n---\n\n## 4. Complete P-Value Tables\n\n### 4a. 11-Point Data (gen_0 to gen_10) — Method A (paper implementation)\n\n| Pair | s42 | s43 | s44 | s45 | sig_seeds |\n|------|-----|-----|-----|-----|-----------|\n| TE→d1 | F=311.67, **p<.0001*** | F=199.49, **p<.0001*** | F=501.08, **p<.0001*** | F=388.44, **p<.0001*** | **4/4** |\n| TE→d2 | F=115.44, **p<.0001*** | F=113.93, **p<.0001*** | F=549.55, **p<.0001*** | F=187.36, **p<.0001*** | **4/4** |\n| TE→d3 | F=101.37, **p<.0001*** | F=110.55, **p<.0001*** | F=232.19, **p<.0001*** | F=138.65, **p<.0001*** | **4/4** |\n| ECE→d1 | F=785.93, **p<.0001*** | F=3369.54, **p<.0001*** | F=2.74, p=.1729 | F=11.47, **p=.0276*** | **3/4** |\n| ECE→d2 | F=124.17, **p<.0001*** | F=201.93, **p<.0001*** | F=1.00, p=.3734 | F=0.32, p=.5995 | **2/4** |\n| ECE→d3 | F=74.03, **p=.0001*** | F=113.35, **p<.0001*** | F=2.01, p=.2294 | F=0.38, p=.5725 | **2/4** |\n\nADF-derived parameters:\n- TE pairs (all seeds): dc=0, dd=0, d_max=0, k=1, **df_resid=7**\n- ECE pairs s42/s43: dc=0, dd=0, d_max=0, k=1, **df_resid=7**\n- ECE pairs s44/s45: dc=1, dd=0, d_max=1, k=2, **df_resid=4**\n\n### 4b. 10-Point Data (gen_0 to gen_9) — Method A\n\n| Pair | s42 | s43 | s44 | s45 | sig_seeds |\n|------|-----|-----|-----|-----|-----------|\n| TE→d1 | F=272.80, **p<.0001*** | F=208.96, **p<.0001*** | F=483.31, **p<.0001*** | F=486.70, **p<.0001*** | **4/4** |\n| TE→d2 | F=101.61, **p=.0001*** | F=116.14, **p<.0001*** | F=489.48, **p<.0001*** | F=198.85, **p<.0001*** | **4/4** |\n| TE→d3 | F=86.80, **p=.0001*** | F=111.49, **p<.0001*** | F=200.69, **p<.0001*** | F=138.40, **p<.0001*** | **4/4** |\n| ECE→d1 | F=1110.61, **p<.0001*** | F=2991.05, **p<.0001*** | F=3.20, p=.1714 | F=7.78, p=.0685 | **2/4** |\n| ECE→d2 | F=106.12, **p<.0001*** | F=186.19, **p<.0001*** | F=5.16, p=.1079 | F=0.25, p=.6527 | **2/4** |\n| ECE→d3 | F=62.91, **p=.0002*** | F=105.46, **p=.0001*** | F=0.03, p=.8736 | F=0.28, p=.6345 | **2/4** |\n\n10pt ECE pairs s44/s45: dc=1, dd=0, d_max=1, k=2, **df_resid=3** (vs 4 with 11pt)\n\n### 4c. 11-Point Data — Method B (window_sensitivity implementation)\n\n| Pair | s42 | s43 | s44 | s45 | sig_seeds |\n|------|-----|-----|-----|-----|-----------|\n| TE→d1 | χ²=1.57, p=.667 | χ²=5.17, p=.160 | χ²=7.61, p=.055 | χ²=2.68, p=.261 | **0/4** |\n| TE→d2 | χ²=1.22, p=.749 | χ²=6.76, p=.080 | χ²=2.10, p=.553 | χ²=1.41, p=.704 | **0/4** |\n| TE→d3 | χ²=1.41, p=.703 | χ²=1.46, p=.692 | χ²=0.98, p=.807 | χ²=0.49, p=.921 | **0/4** |\n| ECE→d1 | χ²=123.33, **p<.0001*** | χ²=3.42, p=.331 | χ²=9.78, **p=.021*** | χ²=35.75, **p<.0001*** | **3/4** |\n| ECE→d2 | χ²=35.86, **p<.0001*** | χ²=1.93, p=.587 | χ²=9.99, **p=.019*** | χ²=18.81, **p=.0003*** | **3/4** |\n| ECE→d3 | χ²=433.91, **p<.0001*** | χ²=5.37, p=.147 | χ²=1.20, p=.753 | χ²=26.35, **p<.0001*** | **2/4** |\n\n### 4d. 10-Point Data — Method B\n\n| Pair | s42 | s43 | s44 | s45 | sig_seeds |\n|------|-----|-----|-----|-----|-----------|\n| TE→d1–d3 | NaN | NaN | NaN | NaN | **0/4** |\n| ECE→d1 | NaN | NaN | NaN | χ²=8.32, **p=.016*** | **1/4** |\n| ECE→d2–d3 | NaN | NaN | NaN | NaN | **0/4** |\n\nMethod B with 10 points: VAR(3) on 10 observations → near-singular, statsmodels returns NaN for most fits.\n\n---\n\n## 5. 11-Point vs 10-Point Conclusion Differences\n\n### Method A (paper implementation)\n\n| Pair | 11pt sig_seeds | 10pt sig_seeds | Flipped? |\n|------|---------------|---------------|----------|\n| TE→d1 | 4/4 | 4/4 | No |\n| TE→d2 | 4/4 | 4/4 | No |\n| TE→d3 | 4/4 | 4/4 | No |\n| ECE→d1 | **3/4** | **2/4** | **YES** |\n| ECE→d2 | 2/4 | 2/4 | No |\n| ECE→d3 | 2/4 | 2/4 | No |\n\n**ECE→d1 flip mechanism**: Seed 45 goes from p=0.0276 (11pt, sig) to p=0.0685 (10pt, marginal ns). Adding gen_10 increases df_resid from 3 to 4 AND provides one more observation point, just enough to push this marginal case over the threshold.\n\n### Method B (window_sensitivity implementation)\n\n| Pair | 11pt sig_seeds | 10pt sig_seeds | Flipped? |\n|------|---------------|---------------|----------|\n| TE→d1–d3 | 0/4 | 0/4 | No |\n| ECE→d1 | **3/4** | **1/4** | **YES** |\n| ECE→d2 | **3/4** | **0/4** | **YES** |\n| ECE→d3 | 2/4 | 0/4 | **YES** |\n\nMethod B is far more sensitive to the one-point difference because VAR(3) on 10 points has essentially zero residual df.\n\n---\n\n## 6. Why Window Sensitivity Report Shows TE p>0.3\n\nThe window sensitivity report (T=10, 10 data points) used Method B:\n- TE→d1 s42: p=0.980, s43: p=0.885, s44: p=0.995, s45: p=0.983\n\nThis is caused by **Bug #2**, not Bug #1. Even with 11 points, Method B gives p=0.667, 0.160, 0.055, 0.261 for TE→d1 — all non-significant.\n\nThe hardcoded d=1 + AIC lag selection (p=2) creates a VAR(3) model that consumes all degrees of freedom testing TE→d_i, while the data is actually I(0) and needs only VAR(1).\n\n---\n\n## 7. ECE→d1: ablation vs paper\n\n| Source | ECE→d1 sig_seeds | Implementation |\n|--------|------------------|----------------|\n| method_ablation.json (robust_pairs) | ≥3/4 → SIGNIFICANT | Method A, 11pt |\n| This audit, Method A, 11pt | 3/4 (s42✓ s43✓ s44✗ s45✓) | Confirmed |\n| Paper method.tex | 3/4 | Matches Method A |\n\n**Answer**: Paper is correct (3/4 sig). If an earlier ablation draft said 2/4, it was either using 10-point data or a different run.\n\n---\n\n## 8. FNR Recalculation\n\nUsing Method A (paper implementation), 11-point data, threshold ≥3/4 seeds:\n\n| Pair | sig_seeds | Status |\n|------|-----------|--------|\n| TE→d1 | 4/4 | DETECTED |\n| TE→d2 | 4/4 | DETECTED |\n| TE→d3 | 4/4 | DETECTED |\n| ECE→d1 | 3/4 | DETECTED |\n| ECE→d2 | 2/4 | MISSED |\n| ECE→d3 | 2/4 | MISSED |\n\n**FNR = 2/6 = 33.3%** — Paper's claim is correct.\n\nECE→d2 and ECE→d3 miss because seeds 44 and 45 have ECE classified as I(1) by ADF, triggering d_max=1, k=2, df_resid=4, which severely limits power. Seeds 42 and 43 have ECE classified as I(0), giving df_resid=7 and strong significance.\n\n---\n\n## 9. Root Cause: ECE Stationarity is Seed-Dependent\n\nThe split in ECE pair results (s42/s43 sig, s44/s45 ns) traces to ADF stationarity classification:\n\n| Seed | ECE at gen_5–10 range | ADF classification | d_max | df_resid |\n|------|----------------------|-------------------|-------|----------|\n| 42 | 0.390–0.417 (flat) | I(0) | 0 | 7 |\n| 43 | 0.394–0.420 (flat) | I(0) | 0 | 7 |\n| 44 | 0.393–0.424 (slight upward) | I(1) | 1 | 4 |\n| 45 | 0.386–0.417 (slight upward) | I(1) | 1 | 4 |\n\nSeeds 44/45 have a marginally detectable upward trend in ECE's late plateau, causing ADF to classify ECE as I(1). This adds an augmentation lag, cutting df_resid from 7 to 4 and destroying power.\n\nThis is a genuine statistical limitation, not a bug. The FNR reflects real power constraints with T=10.\n\n---\n\n## 10. Summary of Bugs and Corrections Needed\n\n### Must fix:\n1. **`window_sensitivity.py` line 193**: Change `all_data[seed][:T]` to `all_data[seed][:T+1]` to use T+1 data points for \"T generations\"\n2. **`window_sensitivity.py` TY implementation**: The `toda_yamamoto_v2` function is fundamentally different from the paper's TY. The report should either:\n   - (a) Use the same `toda_yamamoto` from `method_ablation.py`, OR\n   - (b) Clearly label the results as using a different TY variant\n\n### No fix needed:\n- Paper FNR=33.3% is correct\n- Paper ECE→d1 sig_seeds=3/4 is correct\n- Method A implementation is sound\n\n### Constraint C001 status:\nThe audit confirms that TY results at α=1.0 are consistent across seeds for TE pairs (4/4) but seed-dependent for ECE pairs (due to ADF classification). This is within-α behavior and does NOT address the cross-α non-monotonicity flagged in C001. The constraint remains in effect.\n"
  }
}
````

</details>

---

### Tool result

_source line 90 · 2026-05-16T00:06:21.103082+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/ty_seed_audit/ty_audit_report.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_ty_seed_audit_20260515T235823",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 91 · 2026-05-16T00:06:21.103216+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'SSH to server, find data and scripts', 'status': 'completed', 'activeForm': 'Exploring server data and scripts'}, {'content': 'Run TY audit with 11pt and 10pt data', 'status': 'completed', 'activeForm': 'Running TY audit'}, {'content': 'Identify off-by-one bug and implementation differences', 'status': 'completed', 'activeForm': 'Analyzing script bugs'}, {'content': 'Write comprehensive audit report', 'status': 'completed', 'activeForm': 'Writing audit report'}, {'content': 'Register artifact', 'status': 'in_progress', 'activeForm': 'Registering artifact'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_ty_seed_audit_20260515T235823",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'SSH to server, find data and scripts', 'status': 'completed', 'activeForm': 'Exploring server data and scripts'}, {'content': 'Run TY audit with 11pt and 10pt data', 'status': 'completed', 'activeForm': 'Running TY audit'}, {'content': 'Identify off-by-one bug and implementation differences', 'status': 'completed', 'activeForm': 'Analyzing script bugs'}, {'content': 'Write comprehensive audit report', 'status': 'completed', 'activeForm': 'Writing audit report'}, {'content': 'Register artifact', 'status': 'in_progress', 'activeForm': 'Registering artifact'}]"
  }
}
```

</details>

---

### Tool result

_source line 92 · 2026-05-16T00:06:21.103374+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_ty_seed_audit_20260515T235823",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 93 · 2026-05-16T00:06:21.103498+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "TY Seed Audit Report",
  "type": "report",
  "description": "Toda-Yamamoto full seed audit: off-by-one bug confirmed, two incompatible TY implementations identified, paper FNR=33.3% verified correct, complete p-value tables for 11pt and 10pt data",
  "project": "distrib_canary_collapse",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/ty_seed_audit/ty_audit_report.md",
  "tags": "['ty', 'audit', 'fnr', 'bug', 'granger-causality']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_ty_seed_audit_20260515T235823",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "TY Seed Audit Report",
    "type": "report",
    "description": "Toda-Yamamoto full seed audit: off-by-one bug confirmed, two incompatible TY implementations identified, paper FNR=33.3% verified correct, complete p-value tables for 11pt and 10pt data",
    "project": "distrib_canary_collapse",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/ty_seed_audit/ty_audit_report.md",
    "tags": "['ty', 'audit', 'fnr', 'bug', 'granger-causality']"
  }
}
```

</details>

---

### Tool result

_source line 94 · 2026-05-16T00:06:21.103638+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260516_33a86e\", \"name\": \"TY Seed Audit Report\", \"type\": \"report\", \"description\": \"Toda-Yamamoto full seed audit: off-by-one bug confirmed, two incompatible TY implementations identified, paper FNR=33.3% verified correct, complete p-value tables for 11pt and 10pt data\", \"path\": \"projects/distrib_canary_collapse/artifacts/_project/report/ty_audit_report.md\", \"url\": null, \"project\": \"distrib_canary_collapse\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-16T00:06:04.999494+00:00\", \"tags\": [\"ty\", \"audit\", \"fnr\", \"bug\", \"granger-causality\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_ty_seed_audit_20260515T235823",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 95 · 2026-05-16T00:06:21.103762+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'SSH to server, find data and scripts', 'status': 'completed', 'activeForm': 'Exploring server data and scripts'}, {'content': 'Run TY audit with 11pt and 10pt data', 'status': 'completed', 'activeForm': 'Running TY audit'}, {'content': 'Identify off-by-one bug and implementation differences', 'status': 'completed', 'activeForm': 'Analyzing script bugs'}, {'content': 'Write comprehensive audit report', 'status': 'completed', 'activeForm': 'Writing audit report'}, {'content': 'Register artifact', 'status': 'completed', 'activeForm': 'Registering artifact'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_ty_seed_audit_20260515T235823",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'SSH to server, find data and scripts', 'status': 'completed', 'activeForm': 'Exploring server data and scripts'}, {'content': 'Run TY audit with 11pt and 10pt data', 'status': 'completed', 'activeForm': 'Running TY audit'}, {'content': 'Identify off-by-one bug and implementation differences', 'status': 'completed', 'activeForm': 'Analyzing script bugs'}, {'content': 'Write comprehensive audit report', 'status': 'completed', 'activeForm': 'Writing audit report'}, {'content': 'Register artifact', 'status': 'completed', 'activeForm': 'Registering artifact'}]"
  }
}
```

</details>

---

### Tool result

_source line 96 · 2026-05-16T00:06:21.103904+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_ty_seed_audit_20260515T235823",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 97 · 2026-05-16T00:06:21.104050+00:00_

审计完成。核心发现：

**两个 bug 导致三份报告互相矛盾：**

1. **Off-by-one**（`window_sensitivity.py:193`）：`[:T]` 在 T=10 时只取 10 个点，少了 gen_10。ECE→d1 因此从 3/4 sig 掉到 2/4 sig（seed 45 从 p=0.028 变为 p=0.069）。

2. **两套不兼容的 TY 实现**：
   - `method_ablation.py`（论文用的）：ADF 测 d_max、固定 p=1、F-test → TE 系列被正确判为 I(0)，d_max=0，df_resid=7，F 值 100–500，全部显著
   - `window_sensitivity.py`：硬编码 d=1、AIC 选 p=2、chi² → VAR(3) 吃光自由度，TE 全部 p>0.3

**关键结论：**
- **Paper FNR=33.3% (2/6) 正确** — ECE→d2 和 ECE→d3 各 2/4 sig，被 TY miss
- **Paper ECE→d1 sig_seeds=3/4 正确** — s42✓ s43✓ s44✗ s45✓
- **Window sensitivity 报告的 TE p>0.3 是错的** — 用了错误的 TY 实现（Bug #2），不是 off-by-one 导致的
- ECE pairs 中 s44/s45 不显著的根因：ADF 将这两个 seed 的 ECE 判为 I(1)，d_max=1 导致 df_resid 只有 4，power 不足

报告已写入 `artifacts/ty_seed_audit/ty_audit_report.md` 并注册。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_ty_seed_audit_20260515T235823"
}
```

</details>

---
