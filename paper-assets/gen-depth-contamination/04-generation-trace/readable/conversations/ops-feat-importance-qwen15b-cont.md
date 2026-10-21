# ops feat importance qwen15b cont

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 53
- **Recorded user turns:** 0
- **Tool calls:** 26
- **Original source:** `logs/chats/worker_ops_feat_importance_qwen15b_cont_20260521T073611.jsonl`
- **Structured JSON:** [`1152ab3683a095f986d5.json`](../../sessions/11/1152ab3683a095f986d5.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

53 recorded events

### Tool call

_source line 1 · 2026-05-21T07:40:20.599352+00:00_

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
  "session": "worker_ops_feat_importance_qwen15b_cont_20260521T073611",
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

_source line 2 · 2026-05-21T07:40:20.599764+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_feat_importance_qwen15b_cont_20260521T073611",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-21T07:40:20.599992+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "find /root/autodl-tmp/gen-depth-contamination/results/ -path \"*cont*\" -type f -name \"*.csv\" -o -path \"*cont*\" -type f -name \"*.json\" -o -path \"*continuation*\" -type f -name \"*.csv\" -o -path \"*continuation*\" -type f -name \"*.json\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_feat_importance_qwen15b_cont_20260521T073611",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "find /root/autodl-tmp/gen-depth-contamination/results/ -path \"*cont*\" -type f -name \"*.csv\" -o -path \"*cont*\" -type f -name \"*.json\" -o -path \"*continuation*\" -type f -name \"*.csv\" -o -path \"*continuation*\" -type f -name \"*.json\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-21T07:40:20.600261+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/gen-depth-contamination/results/exp_018_llama8b/pairwise_auc.json\\n/root/autodl-tmp/gen-depth-contamination/results/exp_018_llama8b/jsd.json\\n/root/autodl-tmp/gen-depth-contamination/results/exp_018_llama8b/ordinal_results.json\\n/root/autodl-tmp/gen-depth-contamination/results/exp_018_llama8b/feature_importance.json\\n/root/autodl-tmp/gen-depth-contamination/results/exp_021_length_128/pairwise_auc.json\\n/root/autodl-tmp/gen-depth-contamination/results/exp_021_length_128/jsd.json\\n/root/autodl-tmp/gen-depth-contamination/results/exp_021_length_128/ordinal_results.json\\n/root/autodl-tmp/gen-depth-contamination/results/exp_021_length_128/feature_importance.json\\n/root/autodl-tmp/gen-depth-contamination/results/exp_021_length_256/pairwise_auc.json\\n/root/autodl-tmp/gen-depth-contamination/results/exp_021_length_256/jsd.json\\n/root/autodl-tmp/gen-depth-contamination/results/exp_021_length_256/ordinal_results.json\\n/root/autodl-tmp/gen-depth-contamination/results/exp_021_length_256/feature_importance.json\\n/root/autodl-tmp/gen-depth-contamination/results/exp_021_length_512/pairwise_auc.json\\n/root/autodl-tmp/gen-depth-contamination/results/exp_021_length_512/jsd.json\\n/root/autodl-tmp/gen-depth-contamination/results/exp_021_length_512/ordinal_results.json\\n/root/autodl-tmp/gen-depth-contamination/results/exp_021_length_512/feature_importance.json\\n/root/autodl-tmp/gen-depth-contamination/results/exp_023_wiki/pairwise_auc.json\\n/root/autodl-tmp/gen-depth-contamination/results/exp_023_wiki/jsd.json\\n/root/autodl-tmp/gen-depth-contamination/results/exp_023_wiki/ordinal_results.json\\n/root/autodl-tmp/gen-depth-contamination/results/exp_023_wiki/feature_importance.json\\n/root/autodl-tmp/gen-depth-contamination/results/exp_024_arxiv/pairwise_auc.json\\n/root/autodl-tmp/gen-depth-contamination/results/exp_024_arxiv/jsd.json\\n/root/autodl-tmp/gen-depth-contamination/results/exp_024_arxiv/
…[truncated 6364 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_feat_importance_qwen15b_cont_20260521T073611",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-21T07:40:20.600438+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "ls /root/autodl-tmp/gen-depth-contamination/results/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_feat_importance_qwen15b_cont_20260521T073611",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "ls /root/autodl-tmp/gen-depth-contamination/results/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-21T07:40:20.600607+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"analysis_pythia_retrain_depth7\\nbootstrap_stability\\nc4_power_curve\\nc4_subsample_control.json\\ncontamination_sweep\\ncross_scorer_f1\\ndata_consistency_snapshot_corrected.json\\ndeberta_cross_transfer\\nexp_008_retrain_chain\\nexp_009_dose_response\\nexp_014_naturalistic\\nexp_014_naturalistic.log\\nexp_018_llama8b\\nexp_021_length_128\\nexp_021_length_256\\nexp_021_length_512\\nexp_023_wiki\\nexp_024_arxiv\\nexp_025_pythia_arxiv\\nexp_025_pythia_filtering\\nexp_026_arxiv_filtering\\nexp_027_latex_ablation\\nexp_028_power_curve\\nexp_028_power_curve.log\\nexp_14b_c4\\nexp_7b_cross_transfer\\nexp_7b_scorer_ablation\\nexp_7b_scorer_arxiv\\nexp_7b_scorer_arxiv.log\\nexp_arXiv_llama8b\\nexp_arXiv_llama8b_crossscorer\\nexp_arXiv_mistral7b\\nexp_arXiv_mistral7b_crossscorer\\nexp_arXiv_olmo\\nexp_arXiv_qwen1b5_crossscorer\\nexp_arXiv_qwen7b\\nexp_arXiv_qwen7b_crossscorer\\nexp_bootstrap_10k\\nexp_bootstrap_10k_log.txt\\nexp_changepoint_kstar\\nexp_code_llama8b\\nexp_code_mistral7b\\nexp_code_mistral7b.log\\nexp_code_multi_source\\nexp_code_multi_source.log\\nexp_code_pythia1b4\\nexp_code_qwen1b5\\nexp_code_qwen1b5_pythia_scorer\\nexp_code_qwen7b\\nexp_contamination_rate_sweep\\nexp_deberta_arxiv\\nexp_deberta_arxiv_qwen1b5\\nexp_deberta_c4_1b5\\nexp_deberta_code_qwen1b5\\nexp_deberta_filtering_comparison\\nexp_deberta_upperbound\\nexp_deberta_upperbound.log\\nexp_expanded_downstream_eval\\nexp_gemma2b_depth\\nexp_multi_source_arxiv\\nexp_multi_source_detection\\nexp_multi_source_detection_v2\\nexp_multi_source_unified_scorer\\nexp_olmo_retrain_chain\\nexp_pythia69b_c4\\nexp_pythia_retrain_depth7\\nexp_qwen_retrain_chain\\nexp_qwen_retrain_chain_ext\\nexp_wiki_llama8b\\nexp_wiki_mistral7b\\nexp_wiki_multi_source\\nexp_wiki_multi_source.log\\nexp_wiki_olmo\\nexp_wiki_olmo_v2\\nexp_wiki_pythia\\nexp_wiki_pythia_v2\\nexp_wiki_qwen7b\\nexp_wiki_scorer_confound\\nexp_wiki_scorer_confound_1b5\\nf1_optimal_threshold\\nfe
…[truncated 280 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_feat_importance_qwen15b_cont_20260521T073611",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-21T07:40:20.600769+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "head -100 /root/autodl-tmp/gen-depth-contamination/scripts/feature_importance_analysis.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_feat_importance_qwen15b_cont_20260521T073611",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "head -100 /root/autodl-tmp/gen-depth-contamination/scripts/feature_importance_analysis.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-21T07:40:20.601098+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nPermutation Importance Analysis for 15D OBD Features\\nAnalyzes feature contributions to K*=2 boundary (0v1 vs 1v2 classification)\\n\\\"\\\"\\\"\\n\\nimport csv\\nimport json\\nimport os\\nimport sys\\nfrom pathlib import Path\\n\\nimport numpy as np\\nimport matplotlib\\nmatplotlib.use(\\\"Agg\\\")\\nimport matplotlib.pyplot as plt\\nfrom sklearn.inspection import permutation_importance\\nfrom sklearn.metrics import roc_auc_score\\nfrom sklearn.model_selection import GroupKFold\\nimport lightgbm as lgb\\n\\nos.environ[\\\"CUDA_VISIBLE_DEVICES\\\"] = \\\"1\\\"\\nos.environ[\\\"OMP_NUM_THREADS\\\"] = \\\"4\\\"\\n\\nDATA_PATH = Path(\\\"/root/autodl-tmp/gen-depth-contamination/data/exp_018_llama8b/features.csv\\\")\\nOUT_DIR = Path(\\\"/root/autodl-tmp/gen-depth-contamination/results/feature_importance\\\")\\nART_DIR = Path(\\\"/root/autodl-tmp/gen-depth-contamination/artifacts\\\")\\nOUT_DIR.mkdir(parents=True, exist_ok=True)\\nART_DIR.mkdir(parents=True, exist_ok=True)\\n\\nALL_FEATURES = [\\n    \\\"surp_mean\\\", \\\"surp_std\\\", \\\"surp_skew\\\", \\\"surp_kurt\\\",\\n    \\\"surp_d1_mean\\\", \\\"surp_d1_std\\\", \\\"surp_d1_skew\\\",\\n    \\\"surp_d2_mean\\\", \\\"surp_d2_std\\\",\\n    \\\"ttr\\\", \\\"hapax_ratio\\\", \\\"self_bleu\\\",\\n    \\\"freq_kurtosis\\\", \\\"freq_entropy\\\", \\\"low_freq_ratio\\\",\\n]\\n\\nFEATURE_GROUPS = {\\n    \\\"surp_mean\\\": \\\"surprisal_base\\\", \\\"surp_std\\\": \\\"surprisal_base\\\",\\n    \\\"surp_skew\\\": \\\"surprisal_base\\\", \\\"surp_kurt\\\": \\\"surprisal_base\\\",\\n    \\\"surp_d1_mean\\\": \\\"surprisal_deriv\\\", \\\"surp_d1_std\\\": \\\"surprisal_deriv\\\",\\n    \\\"surp_d1_skew\\\": \\\"surprisal_deriv\\\",\\n    \\\"surp_d2_mean\\\": \\\"surprisal_deriv\\\", \\\"surp_d2_std\\\": \\\"surprisal_deriv\\\",\\n    \\\"ttr\\\": \\\"lexical_diversity\\\", \\\"hapax_ratio\\\": \\\"lexical_diversity\\\",\\n    \\\"self_bleu\\\": \\\"le
…[truncated 2164 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_feat_importance_qwen15b_cont_20260521T073611",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-21T07:40:20.601364+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "find /root/autodl-tmp/gen-depth-contamination/data/ -name \"features.csv\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_feat_importance_qwen15b_cont_20260521T073611",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "find /root/autodl-tmp/gen-depth-contamination/data/ -name \"features.csv\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-21T07:40:20.601547+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/gen-depth-contamination/data/exp_018_llama8b/features.csv\\n/root/autodl-tmp/gen-depth-contamination/data/exp_021_length_128/features.csv\\n/root/autodl-tmp/gen-depth-contamination/data/exp_021_length_256/features.csv\\n/root/autodl-tmp/gen-depth-contamination/data/exp_021_length_512/features.csv\\n/root/autodl-tmp/gen-depth-contamination/data/exp_023_wiki/features.csv\\n/root/autodl-tmp/gen-depth-contamination/data/exp_024_arxiv/features.csv\\n/root/autodl-tmp/gen-depth-contamination/data/exp_025_pythia_arxiv/features.csv\\n/root/autodl-tmp/gen-depth-contamination/data/exp_008_retrain_chain/features.csv\\n/root/autodl-tmp/gen-depth-contamination/data/exp_arXiv_olmo/features.csv\\n/root/autodl-tmp/gen-depth-contamination/data/exp_arXiv_llama8b/features.csv\\n/root/autodl-tmp/gen-depth-contamination/data/exp_wiki_pythia/features.csv\\n/root/autodl-tmp/gen-depth-contamination/data/exp_wiki_olmo/features.csv\\n/root/autodl-tmp/gen-depth-contamination/data/exp_arXiv_qwen7b/features.csv\\n/root/autodl-tmp/gen-depth-contamination/data/exp_wiki_llama8b/features.csv\\n/root/autodl-tmp/gen-depth-contamination/data/exp_arXiv_mistral7b/features.csv\\n/root/autodl-tmp/gen-depth-contamination/data/exp_wiki_mistral7b/features.csv\\n/root/autodl-tmp/gen-depth-contamination/data/exp_wiki_qwen7b/features.csv\\n/root/autodl-tmp/gen-depth-contamination/data/exp_wiki_scorer_confound/features.csv\\n/root/autodl-tmp/gen-depth-contamination/data/exp_wiki_scorer_confound_1b5/features.csv\\n/root/autodl-tmp/gen-depth-contamination/data/exp_arXiv_qwen7b_crossscorer/features.csv\\n/root/autodl-tmp/gen-depth-contamination/data/exp_arXiv_qwen1b5_crossscorer/features.csv\\n/root/autodl-tmp/gen-depth-contamination/data/exp_arXiv_llama8b_crossscorer/features.csv\\n/root/autodl-tmp/gen-depth-contamination/data/exp_arXiv_mistral7b_crossscorer/features.csv\\n/root/autodl-tmp/gen-depth-contamination/data/exp_027_latex_ablation/fe
…[truncated 1735 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_feat_importance_qwen15b_cont_20260521T073611",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-21T07:40:20.601711+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "ls /root/autodl-tmp/gen-depth-contamination/data/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_feat_importance_qwen15b_cont_20260521T073611",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "ls /root/autodl-tmp/gen-depth-contamination/data/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-21T07:40:20.601923+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"code_python_seed\\ncontamination_sweep\\nexp_008_retrain_chain\\nexp_009_dose_response\\nexp_018_llama8b\\nexp_021_length_128\\nexp_021_length_256\\nexp_021_length_512\\nexp_023_wiki\\nexp_024_arxiv\\nexp_025_pythia_arxiv\\nexp_027_latex_ablation\\nexp_7b_scorer_ablation\\nexp_7b_scorer_arxiv\\nexp_arXiv_llama8b\\nexp_arXiv_llama8b_crossscorer\\nexp_arXiv_mistral7b\\nexp_arXiv_mistral7b_crossscorer\\nexp_arXiv_olmo\\nexp_arXiv_qwen1b5_crossscorer\\nexp_arXiv_qwen7b\\nexp_arXiv_qwen7b_crossscorer\\nexp_code_llama8b\\nexp_code_mistral7b\\nexp_code_pythia1b4\\nexp_code_qwen1b5\\nexp_code_qwen1b5_pythia_scorer\\nexp_code_qwen7b\\nexp_gemma2b_depth\\nexp_pythia69b_c4\\nexp_qwen_retrain_chain\\nexp_wiki_llama8b\\nexp_wiki_mistral7b\\nexp_wiki_olmo\\nexp_wiki_pythia\\nexp_wiki_qwen7b\\nexp_wiki_scorer_confound\\nexp_wiki_scorer_confound_1b5\\nolmo_c4_cont\\nolmo_retrain_chain\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_feat_importance_qwen15b_cont_20260521T073611",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-21T07:40:20.602073+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "ls /root/autodl-tmp/gen-depth-contamination/results/feature_importance/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_feat_importance_qwen15b_cont_20260521T073611",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "ls /root/autodl-tmp/gen-depth-contamination/results/feature_importance/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-21T07:40:20.602204+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"importance_results.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_feat_importance_qwen15b_cont_20260521T073611",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-21T07:40:20.602328+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "ls /root/autodl-tmp/gen-depth-contamination/results/feature_importance_pythia/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_feat_importance_qwen15b_cont_20260521T073611",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "ls /root/autodl-tmp/gen-depth-contamination/results/feature_importance_pythia/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-21T07:40:20.602453+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"importance_results.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.65}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_feat_importance_qwen15b_cont_20260521T073611",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-21T07:40:20.602601+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "head -5 /root/autodl-tmp/gen-depth-contamination/data/exp_qwen_retrain_chain/features.csv",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_feat_importance_qwen15b_cont_20260521T073611",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "head -5 /root/autodl-tmp/gen-depth-contamination/data/exp_qwen_retrain_chain/features.csv",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-21T07:40:20.602911+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"doc_id,depth,surp_mean,surp_std,surp_skew,surp_kurt,surp_d1_mean,surp_d1_std,surp_d1_skew,surp_d2_mean,surp_d2_std,ttr,hapax_ratio,self_bleu,freq_kurtosis,freq_entropy,low_freq_ratio\\r\\n0,0,3.3487279415130615,3.6196162700653076,1.1923067569732666,0.17527055740356445,-0.040933798998594284,3.126880645751953,-0.21806024014949799,-0.0027106928173452616,5.435549259185791,0.6411290322580645,0.7547169811320755,0.00033532936225085853,32.84599954971851,6.72451758445088,0.9230769230769231\\r\\n1,0,4.266286373138428,3.886166572570801,0.8370857238769531,-0.6568143367767334,-0.0288324486464262,3.6146955490112305,-0.14190223813056946,0.0035798929166048765,6.296764850616455,0.6058091286307054,0.7534246575342466,0.0,10.486046852634258,6.765095558557913,0.9029850746268657\\r\\n2,0,2.1282870769500732,2.5061192512512207,1.8054604530334473,3.6829376220703125,-0.0006367414607666433,3.3885278701782227,0.3021502196788788,0.009285538457334042,5.748108386993408,0.5054151624548736,0.6428571428571429,0.00039135879877985407,18.761368123720054,6.436231801840419,0.9107142857142857\\r\\n3,0,5.816761493682861,4.460556507110596,0.2375178039073944,-1.3557852506637573,-0.0396154448390007,3.5022640228271484,-0.48342210054397583,-0.0014357452746480703,5.938627243041992,0.7547169811320755,0.76875,0.0,17.307093333053935,6.904835421176308,0.9548872180451128\\r\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_feat_importance_qwen15b_cont_20260521T073611",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-21T07:40:20.603107+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "wc -l /root/autodl-tmp/gen-depth-contamination/data/exp_qwen_retrain_chain/features.csv",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_feat_importance_qwen15b_cont_20260521T073611",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "wc -l /root/autodl-tmp/gen-depth-contamination/data/exp_qwen_retrain_chain/features.csv",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-21T07:40:20.603246+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"40001 /root/autodl-tmp/gen-depth-contamination/data/exp_qwen_retrain_chain/features.csv\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_feat_importance_qwen15b_cont_20260521T073611",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-21T07:40:20.603370+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "head -5 /root/autodl-tmp/gen-depth-contamination/data/exp_008_retrain_chain/features.csv",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_feat_importance_qwen15b_cont_20260521T073611",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "head -5 /root/autodl-tmp/gen-depth-contamination/data/exp_008_retrain_chain/features.csv",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-21T07:40:20.603572+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"doc_id,depth,surp_mean,surp_std,surp_skew,surp_kurt,surp_d1_mean,surp_d1_std,surp_d1_skew,surp_d2_mean,surp_d2_std,ttr,hapax_ratio,self_bleu,freq_kurtosis,freq_entropy,low_freq_ratio\\r\\n0,0,3.3487279415130615,3.6196162700653076,1.1923067569732666,0.17527055740356445,-0.040933798998594284,3.126880645751953,-0.21806024014949799,-0.0027106928173452616,5.435549259185791,0.6411290322580645,0.7547169811320755,0.00033532936225085853,32.84599954971851,6.72451758445088,0.9230769230769231\\r\\n1,0,4.266286373138428,3.886166572570801,0.8370857238769531,-0.6568143367767334,-0.0288324486464262,3.6146955490112305,-0.14190223813056946,0.0035798929166048765,6.296764850616455,0.6058091286307054,0.7534246575342466,0.0,10.486046852634258,6.765095558557913,0.9029850746268657\\r\\n2,0,2.1282870769500732,2.5061192512512207,1.8054604530334473,3.6829376220703125,-0.0006367414607666433,3.3885278701782227,0.3021502196788788,0.009285538457334042,5.748108386993408,0.5054151624548736,0.6428571428571429,0.00039135879877985407,18.761368123720054,6.436231801840419,0.9107142857142857\\r\\n3,0,5.816761493682861,4.460556507110596,0.2375178039073944,-1.3557852506637573,-0.0396154448390007,3.5022640228271484,-0.48342210054397583,-0.0014357452746480703,5.938627243041992,0.7547169811320755,0.76875,0.0,17.307093333053935,6.904835421176308,0.9548872180451128\\r\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_feat_importance_qwen15b_cont_20260521T073611",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-21T07:40:20.603796+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "ls /root/autodl-tmp/gen-depth-contamination/results/exp_qwen_retrain_chain/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_feat_importance_qwen15b_cont_20260521T073611",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "ls /root/autodl-tmp/gen-depth-contamination/results/exp_qwen_retrain_chain/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-21T07:40:20.603999+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"bootstrap_ci.json\\njsd.json\\npairwise_auc.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_feat_importance_qwen15b_cont_20260521T073611",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-21T07:40:20.604186+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "grep -l \"qwen\" /root/autodl-tmp/gen-depth-contamination/results/exp_qwen_retrain_chain/*.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_feat_importance_qwen15b_cont_20260521T073611",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "grep -l \"qwen\" /root/autodl-tmp/gen-depth-contamination/results/exp_qwen_retrain_chain/*.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-21T07:40:20.604376+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.37}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_feat_importance_qwen15b_cont_20260521T073611",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-21T07:40:20.604597+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "python3 -c \"import csv; f=open('/root/autodl-tmp/gen-depth-contamination/data/exp_qwen_retrain_chain/features.csv'); rows=list(csv.DictReader(f)); depths=set(r['depth'] for r in rows); print('depths:', sorted(depths)); print('count:', len(rows)); print('per_depth:', {d: sum(1 for r in rows if r['depth']==d) for d in sorted(depths)})\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_feat_importance_qwen15b_cont_20260521T073611",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "python3 -c \"import csv; f=open('/root/autodl-tmp/gen-depth-contamination/data/exp_qwen_retrain_chain/features.csv'); rows=list(csv.DictReader(f)); depths=set(r['depth'] for r in rows); print('depths:', sorted(depths)); print('count:', len(rows)); print('per_depth:', {d: sum(1 for r in rows if r['depth']==d) for d in sorted(depths)})\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-21T07:40:20.604809+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_feat_importance_qwen15b_cont_20260521T073611",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-21T07:40:20.604997+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "ls /root/autodl-tmp/gen-depth-contamination/results/exp_qwen_retrain_chain_ext/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_feat_importance_qwen15b_cont_20260521T073611",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "ls /root/autodl-tmp/gen-depth-contamination/results/exp_qwen_retrain_chain_ext/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-21T07:40:20.605183+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"jsd.json\\npairwise_auc.json\\npairwise_auc_t_dist.json\\nsummary.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_feat_importance_qwen15b_cont_20260521T073611",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-21T07:40:20.605360+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "grep -rn \"qwen.*cont\\|cont.*qwen\\|continuation.*qwen\\|qwen.*continuation\\|retrain_chain\" /root/autodl-tmp/gen-depth-contamination/configs/ 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_feat_importance_qwen15b_cont_20260521T073611",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "grep -rn \"qwen.*cont\\|cont.*qwen\\|continuation.*qwen\\|qwen.*continuation\\|retrain_chain\" /root/autodl-tmp/gen-depth-contamination/configs/ 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-21T07:40:20.605552+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_feat_importance_qwen15b_cont_20260521T073611",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-21T07:40:20.605741+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "find /root/autodl-tmp/gen-depth-contamination/ -name \"*.py\" -path \"*retrain*\" -o -name \"*.py\" -path \"*cont*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_feat_importance_qwen15b_cont_20260521T073611",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "find /root/autodl-tmp/gen-depth-contamination/ -name \"*.py\" -path \"*retrain*\" -o -name \"*.py\" -path \"*cont*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-21T07:40:20.606057+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/gen-depth-contamination/scripts/run_pipeline.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/exp016_bootstrap_ci.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/download_wiki_seed.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/download_arxiv_seed.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/draw_kstar_theta.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/transfer_heatmap.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/plot_auc_decay_ci.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/plot_filtering_strategies.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/exp019_bootstrap_ci.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/exp018_bootstrap_ci.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/borderline_bootstrap_ci.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/exp024_bootstrap_ci.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/exp025_bootstrap_ci.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/exp008_retrain_chain.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/exp009_dose_response.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/exp026_feature_stability.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/exp027_retrain_bootstrap.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/exp026_feature_stability_v2.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/collect_exp009_v3.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/exp_14d_ablation_detail.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/semantic_ablation.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/semantic_ablation_multi_model.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/run_fi_pythia.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/score_14b_confound.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/crossscorer_bootstrap_ci.py\\n/root/autodl-tmp/gen-depth-contamination/scripts/retrain_chain_bootstrap
…[truncated 5431 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_feat_importance_qwen15b_cont_20260521T073611",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-21T07:40:20.606325+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-22115",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 -c \"\nimport csv\nf=open('/root/autodl-tmp/gen-depth-contamination/data/exp_qwen_retrain_chain/features.csv')\nrows=list(csv.DictReader(f))\ndepths=set(r['depth'] for r in rows)\nprint('depths:', sorted(depths))\nprint('count:', len(rows))\nfor d in sorted(depths):\n    print(f'  depth {d}: {sum(1 for r in rows if r[\\\"depth\\\"]==d)} samples')\n\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_feat_importance_qwen15b_cont_20260521T073611",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 -c \"\nimport csv\nf=open('/root/autodl-tmp/gen-depth-contamination/data/exp_qwen_retrain_chain/features.csv')\nrows=list(csv.DictReader(f))\ndepths=set(r['depth'] for r in rows)\nprint('depths:', sorted(depths))\nprint('count:', len(rows))\nfor d in sorted(depths):\n    print(f'  depth {d}: {sum(1 for r in rows if r[\\\"depth\\\"]==d)} samples')\n\"",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-21T07:40:20.606535+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "cat /root/autodl-tmp/gen-depth-contamination/scripts/feature_importance_pythia.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_feat_importance_qwen15b_cont_20260521T073611",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "cat /root/autodl-tmp/gen-depth-contamination/scripts/feature_importance_pythia.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-21T07:40:20.606739+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"depths: ['0', '1', '2', '3', '4', '5', '6', '7']\\ncount: 40000\\n  depth 0: 5000 samples\\n  depth 1: 5000 samples\\n  depth 2: 5000 samples\\n  depth 3: 5000 samples\\n  depth 4: 5000 samples\\n  depth 5: 5000 samples\\n  depth 6: 5000 samples\\n  depth 7: 5000 samples\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.78}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_feat_importance_qwen15b_cont_20260521T073611",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-21T07:40:20.607217+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nPermutation Importance Analysis for 15D OBD Features\\nAnalyzes feature contributions to K*=2 boundary (0v1 vs 1v2 classification)\\n\\\"\\\"\\\"\\n\\nimport csv\\nimport json\\nimport os\\nimport sys\\nfrom pathlib import Path\\n\\nimport numpy as np\\nimport matplotlib\\nmatplotlib.use(\\\"Agg\\\")\\nimport matplotlib.pyplot as plt\\nfrom sklearn.inspection import permutation_importance\\nfrom sklearn.metrics import roc_auc_score\\nfrom sklearn.model_selection import GroupKFold\\nimport lightgbm as lgb\\n\\nos.environ[\\\"CUDA_VISIBLE_DEVICES\\\"] = \\\"1\\\"\\nos.environ[\\\"OMP_NUM_THREADS\\\"] = \\\"4\\\"\\n\\nDATA_PATH = Path(\\\"/root/autodl-tmp/gen-depth-contamination/data/exp_wiki_pythia/features.csv\\\")\\nOUT_DIR = Path(\\\"/root/autodl-tmp/gen-depth-contamination/results/feature_importance_pythia\\\")\\nART_DIR = Path(\\\"/root/autodl-tmp/gen-depth-contamination/artifacts\\\")\\nOUT_DIR.mkdir(parents=True, exist_ok=True)\\nART_DIR.mkdir(parents=True, exist_ok=True)\\n\\nALL_FEATURES = [\\n    \\\"surp_mean\\\", \\\"surp_std\\\", \\\"surp_skew\\\", \\\"surp_kurt\\\",\\n    \\\"surp_d1_mean\\\", \\\"surp_d1_std\\\", \\\"surp_d1_skew\\\",\\n    \\\"surp_d2_mean\\\", \\\"surp_d2_std\\\",\\n    \\\"ttr\\\", \\\"hapax_ratio\\\", \\\"self_bleu\\\",\\n    \\\"freq_kurtosis\\\", \\\"freq_entropy\\\", \\\"low_freq_ratio\\\",\\n]\\n\\nFEATURE_GROUPS = {\\n    \\\"surp_mean\\\": \\\"surprisal_base\\\", \\\"surp_std\\\": \\\"surprisal_base\\\",\\n    \\\"surp_skew\\\": \\\"surprisal_base\\\", \\\"surp_kurt\\\": \\\"surprisal_base\\\",\\n    \\\"surp_d1_mean\\\": \\\"surprisal_deriv\\\", \\\"surp_d1_std\\\": \\\"surprisal_deriv\\\",\\n    \\\"surp_d1_skew\\\": \\\"surprisal_deriv\\\",\\n    \\\"surp_d2_mean\\\": \\\"surprisal_deriv\\\", \\\"surp_d2_std\\\": \\\"surprisal_deriv\\\",\\n    \\\"ttr\\\": \\\"lexical_diversity\\\", \\\"hapax_ratio\\\": \\\"lexical_diversity\\\",\\n    \\\"self_bleu\\\":
…[truncated 7577 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_feat_importance_qwen15b_cont_20260521T073611",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-21T07:40:20.607504+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "head -60 /root/autodl-tmp/gen-depth-contamination/scripts/exp_qwen_retrain_chain.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_feat_importance_qwen15b_cont_20260521T073611",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "head -60 /root/autodl-tmp/gen-depth-contamination/scripts/exp_qwen_retrain_chain.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-21T07:40:20.607735+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"# exp_qwen_retrain_chain: Qwen2.5-1.5B retrain-chain ecological validity experiment\\n# Each generation: LoRA fine-tune Qwen2.5-1.5B on depth_d texts, merge weights, generate depth_{d+1}\\n# Independent LoRA per generation (no accumulation)\\n# Hypothesis: retrain-chain K* <= prompt-chain K*=2, confirming prompt-chain as upper bound\\n#\\n# Input:  C4 depth-0 seed data (5000 docs, copied from exp_008)\\n# Output: data/exp_qwen_retrain_chain/depth_{0..4}.jsonl, features.csv\\n#         results/exp_qwen_retrain_chain/{pairwise_auc,jsd,bootstrap_ci,permutation_test,summary}.json\\n#\\n# Deps: torch, transformers, peft, datasets, scipy, lightgbm, sklearn, tqdm, numpy\\n\\nimport argparse\\nimport csv\\nimport gc\\nimport json\\nimport logging\\nimport math\\nimport os\\nimport shutil\\nimport sys\\nfrom collections import Counter\\nfrom pathlib import Path\\n\\nimport numpy as np\\nimport torch\\nfrom scipy import stats\\nfrom tqdm import tqdm\\n\\nos.environ.setdefault(\\\"HF_HOME\\\", \\\"/root/autodl-tmp/.hf_cache\\\")\\n\\nlogging.basicConfig(\\n    level=logging.INFO,\\n    format=\\\"%(asctime)s [%(levelname)s] %(message)s\\\",\\n    datefmt=\\\"%H:%M:%S\\\",\\n    handlers=[logging.StreamHandler(sys.stdout)],\\n)\\nlog = logging.getLogger(__name__)\\n\\n# ---------------------------------------------------------------------------\\n# Config\\n# ---------------------------------------------------------------------------\\n\\nQWEN_MODEL_PATH = \\\"/root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-1___5B\\\"\\nSCORER_PATH = \\\"/root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-1___5B\\\"\\nSEED_DATA = \\\"/root/autodl-tmp/gen-depth-contamination/data/exp_008_retrain_chain/depth_0.jsonl\\\"\\n\\nLORA_RANK = 16\\nLORA_ALPHA = 32\\nLORA_TARGET_MODULES = [\\\"q_proj\\\", \\\"k_proj\\\", \\\"v_proj\\\"]\\nTRAIN_LR = 2e-4\\nTRAIN_BATCH_SIZE = 4\\nGRADIENT_ACCUMULATION = 4\\nTRAIN_EPOCHS = 1\\n\\nGEN_TOP_P = 0.95\\nGEN_TEMPERATURE = 
…[truncated 177 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_feat_importance_qwen15b_cont_20260521T073611",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-21T07:40:20.607961+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "grep -n \"mode\\|continuation\\|retrain\\|base_model\\|from_scratch\\|resume\\|init_from\" /root/autodl-tmp/gen-depth-contamination/scripts/exp_qwen_retrain_chain.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_feat_importance_qwen15b_cont_20260521T073611",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "grep -n \"mode\\|continuation\\|retrain\\|base_model\\|from_scratch\\|resume\\|init_from\" /root/autodl-tmp/gen-depth-contamination/scripts/exp_qwen_retrain_chain.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-21T07:40:20.608106+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_feat_importance_qwen15b_cont_20260521T073611",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-21T07:40:20.608266+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "head -15 /root/autodl-tmp/gen-depth-contamination/scripts/exp_qwen_retrain_chain_ext.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_feat_importance_qwen15b_cont_20260521T073611",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "head -15 /root/autodl-tmp/gen-depth-contamination/scripts/exp_qwen_retrain_chain_ext.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-21T07:40:20.608406+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"# exp_qwen_retrain_chain_ext: Qwen2.5-1.5B retrain-chain depth extension (depth 5-7)\\n#\\n# Continues from the depth 0-4 data produced by exp_qwen_retrain_chain.\\n# Each generation: fresh LoRA fine-tune on depth_d texts -> merge -> generate depth_{d+1}\\n#\\n# Input:  depth_0..4.jsonl from exp_qwen_retrain_chain (same data_dir, auto-skipped)\\n# Output: depth_5..7.jsonl + features.csv + pairwise_auc.json + jsd.json (5-fold CV)\\n# Deps:   torch, transformers, peft, lightgbm, sklearn, scipy, tqdm, numpy\\n# Note:   No bootstrap (GroupKFold data leakage risk). Uses 5-fold GroupKFold CV only.\\n\\nimport argparse\\nimport csv\\nimport gc\\nimport json\\nimport logging\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_feat_importance_qwen15b_cont_20260521T073611",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-21T07:40:20.608542+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "head -5 /root/autodl-tmp/gen-depth-contamination/data/olmo_c4_cont/features.csv",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_feat_importance_qwen15b_cont_20260521T073611",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "head -5 /root/autodl-tmp/gen-depth-contamination/data/olmo_c4_cont/features.csv",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-21T07:40:20.608678+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"doc_id,depth,surp_mean,surp_std,surp_skew,surp_kurt,surp_d1_mean,surp_d1_std,surp_d1_skew,surp_d2_mean,surp_d2_std,ttr,hapax_ratio,self_bleu,freq_kurtosis,freq_entropy,low_freq_ratio\\r\\n0,0,2.2366733229719102,2.6309698081253545,2.4947952043223904,11.026745440612762,0.054473039215686275,3.585056463563804,0.7932031002828096,0.10320779000680277,5.9089578463249195,0.7182320441988951,0.8153846153846154,0.0002512986673621978,32.84599954971851,6.72451758445088,0.9230769230769231\\r\\n1,0,2.8951686285436153,2.734662704660925,1.739820970563017,5.500353452414261,0.06456035539215686,3.535911297358869,-0.09900527752489154,0.04200756643700788,6.018237932370326,0.694300518134715,0.8059701492537313,0.0,10.486046852634258,6.765095558557913,0.9029850746268657\\r\\n2,0,2.312308022286743,2.5664093938226165,1.7929683115354151,4.235766905295773,0.03324142156862745,3.546873752226389,0.10310985690319172,0.06163109005905512,5.971711839361135,0.64,0.7410714285714286,0.0,18.761368123720054,6.436231801840419,0.9107142857142857\\r\\n3,0,3.382187480657873,2.8112848978000766,0.9117053411206052,0.27178055620656716,-0.009544516509433961,3.785036960643812,-0.1006007917499593,0.029153398992890996,6.434801391298092,0.7823529411764706,0.8045112781954887,0.0,17.307093333053935,6.904835421176308,0.9548872180451128\\r\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_feat_importance_qwen15b_cont_20260521T073611",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-21T07:40:20.608981+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "head -15 /root/autodl-tmp/gen-depth-contamination/scripts/olmo_c4_bootstrap_ci.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_feat_importance_qwen15b_cont_20260521T073611",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "head -15 /root/autodl-tmp/gen-depth-contamination/scripts/olmo_c4_bootstrap_ci.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-21T07:40:20.609250+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"import csv\\nimport json\\nimport time\\nfrom pathlib import Path\\n\\nimport numpy as np\\nimport lightgbm as lgb\\nfrom sklearn.model_selection import GroupKFold\\nfrom sklearn.metrics import roc_auc_score\\n\\nFEAT_COLS = [\\n    \\\"surp_mean\\\", \\\"surp_std\\\", \\\"surp_skew\\\", \\\"surp_kurt\\\",\\n    \\\"surp_d1_mean\\\", \\\"surp_d1_std\\\", \\\"surp_d1_skew\\\",\\n    \\\"surp_d2_mean\\\", \\\"surp_d2_std\\\",\\n    \\\"ttr\\\", \\\"hapax_ratio\\\", \\\"self_bleu\\\",\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_feat_importance_qwen15b_cont_20260521T073611",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-21T07:40:20.609604+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-22115",
  "command": "cat > /root/autodl-tmp/gen-depth-contamination/scripts/feature_importance_qwen_cont.py << 'PYEOF'\n\"\"\"\nPermutation Importance Analysis for 15D OBD Features\nQwen-1.5B continuation mode (retrain chain) on C4\n\"\"\"\n\nimport csv\nimport json\nimport os\nimport sys\nfrom pathlib import Path\n\nimport numpy as np\nimport matplotlib\nmatplotlib.use(\"Agg\")\nimport matplotlib.pyplot as plt\nfrom sklearn.inspection import permutation_importance\nfrom sklearn.metrics import roc_auc_score\nfrom sklearn.model_selection import GroupKFold\nimport lightgbm as lgb\n\nos.environ[\"CUDA_VISIBLE_DEVICES\"] = \"3\"\nos.environ[\"OMP_NUM_THREADS\"] = \"4\"\n\nDATA_PATH = Path(\"/root/autodl-tmp/gen-depth-contamination/data/exp_qwen_retrain_chain/features.csv\")\nOUT_DIR = Path(\"/root/autodl-tmp/gen-depth-contamination/results/feature_importance_qwen_cont\")\nART_DIR = Path(\"/root/autodl-tmp/gen-depth-contamination/artifacts\")\nOUT_DIR.mkdir(parents=True, exist_ok=True)\nART_DIR.mkdir(parents=True, exist_ok=True)\n\nALL_FEATURES = [\n    \"surp_mean\", \"surp_std\", \"surp_skew\", \"surp_kurt\",\n    \"surp_d1_mean\", \"surp_d1_std\", \"surp_d1_skew\",\n    \"surp_d2_mean\", \"surp_d2_std\",\n    \"ttr\", \"hapax_ratio\", \"self_bleu\",\n    \"freq_kurtosis\", \"freq_entropy\", \"low_freq_ratio\",\n]\n\nFEATURE_GROUPS = {\n    \"surp_mean\": \"surprisal_base\", \"surp_std\": \"surprisal_base\",\n    \"surp_skew\": \"surprisal_base\", \"surp_kurt\": \"surprisal_base\",\n    \"surp_d1_mean\": \"surprisal_deriv\", \"surp_d1_std\": \"surprisal_deriv\",\n    \"surp_d1_skew\": \"surprisal_deriv\",\n    \"surp_d2_mean\": \"surprisal_deriv\", \"surp_d2_std\": \"surprisal_deriv\",\n    \"ttr\": \"lexical_diversity\", \"hapax_ratio\": \"lexical_diversity\",\n    \"self_bleu\": \"lexical_diversity\",\n    \"freq_kurtosis\": \"freq_distribution\", \"freq_entropy\": \"freq_distribution\",\n    \"low_freq_ratio\": \"freq_distribution\",\n}\n\nDISPLAY_NAMES = {\n    \"surp_mean\": \"Mean Surprisal\",\n    \"surp_std\": \"Surprisal Std\",\n    \"surp_skew\": \"Surprisal Skew\",\n    \"surp_kurt\": \"Surprisal Kurtosis\",\n    \"surp_d1_mean\": \"Δ¹ Surprisal Mean\",\n    \"surp_d1_std\": \"Δ¹ Surprisal Std\",\n    \"surp_d1_skew\": \"Δ¹ Surprisal Skew\",\n    \"surp_d2_mean\": \"Δ² Surprisal Mean\",\n    \"surp_d2_std\": \"Δ² Surprisal Std\",\n    \"ttr\": \"TTR\",\n    \"hapax_ratio\": \"Hapax Ratio\",\n    \"self_bleu\": \"Self-BLEU\",\n    \"freq_kurtosis\": \"Freq Kurtosis\",\n    \"freq_entropy\": \"Freq Entropy\",\n    \"low_freq_ratio\": \"Low-Freq Ratio\",\n}\n\nLGB_PARAMS = dict(\n    n_estimators=200, max_depth=6, learning_rate=0.05,\n    num_leaves=31, verbose=-1, n_jobs=4,\n)\n\nN_REPEATS = 10\nN_FOLDS = 5\n\n\ndef load_data():\n    with open(DATA_PATH) as f:\n        rows = list(csv.DictReader(f))\n    doc_ids = np.array([int(r[\"doc_id\"]) for r in rows])\n    depths = np.array([int(r[\"depth\"]) for r in rows])\n    feat_dict = {}\n    for col in ALL_FEATURES:\n        vals = []\n        for r in rows:\n            v = r[col]\n            vals.append(float(v) if v != \"\" and v != \"nan\" else np.nan)\n        feat_dict[col] = np.array(vals)\n    return doc_ids, depths, feat_dict\n\n\ndef get_pair_data(doc_ids, depths, feat_dict, d_low, d_high):\n    mask = (depths == d_low) | (depths == d_high)\n    ids = doc_ids[mask]\n    y = (depths[mask] == d_high).astype(int)\n    X = np.column_stack([feat_dict[col][mask] for col in ALL_FEATURES])\n    nan_mask = np.isnan(X).any(axis=1)\n    if nan_mask.any():\n        valid = ~nan_mask\n        X, y, ids = X[valid], y[valid], ids[valid]\n    return ids, X, y\n\n\ndef compute_permutation_importance(X, y, groups):\n    gkf = GroupKFold(n_splits=N_FOLDS)\n    all_importances = []\n    fold_aucs = []\n\n    for train_idx, test_idx in gkf.split(X, y, groups):\n        X_train, X_test = X[train_idx], X[test_idx]\n        y_train, y_test = y[train_idx], y[test_idx]\n\n        model = lgb.LGBMClassifier(**LGB_PARAMS)\n        model.fit(X_train, y_train)\n\n        baseline_auc = roc_auc_score(y_test, model.predict_proba(X_test)[:, 1])\n        fold_aucs.append(baseline_auc)\n\n        result = permutation_importance(\n            model, X_test, y_test,\n            n_repeats=N_REPEATS,\n            scoring=\"roc_auc\",\n            random_state=42,\n        )\n        all_importances.append(result.importances_mean)\n\n    mean_importance = np.mean(all_importances, axis=0)\n    std_importance = np.std(all_importances, axis=0)\n    mean_auc = np.mean(fold_aucs)\n\n    return mean_importance, std_importance, mean_auc\n\n\nGROUP_COLORS = {\n    \"surprisal_base\": \"#2196F3\",\n    \"surprisal_deriv\": \"#4CAF50\",\n    \"lexical_diversity\": \"#FF9800\",\n    \"freq_distribution\": \"#9C27B0\",\n}\n\nGROUP_LABELS = {\n    \"surprisal_base\": \"Surprisal (base)\",\n    \"surprisal_deriv\": \"Surprisal (derivatives)\",\n    \"lexical_diversity\": \"Lexical diversity\",\n    \"freq_distribution\": \"Frequency distribution\",\n}\n\n\ndef make_barplot(res_0v1, res_1v2, save_path):\n    mean_01 = res_0v1[\"mean\"]\n    std_01 = res_0v1[\"std\"]\n    mean_12 = res_1v2[\"mean\"]\n    std_12 = res_1v2[\"std\"]\n\n    order_01 = np.argsort(mean_01)[::-1]\n\n    fig, axes = plt.subplots(1, 2, figsize=(14, 5), sharey=True)\n\n    for ax, mean_vals, std_vals, title in [\n        (axes[0], mean_01, std_01, \"0 vs 1 (human vs gen-1)\"),\n        (axes[1], mean_12, std_12, \"1 vs 2 (K* boundary)\"),\n    ]:\n        display = [DISPLAY_NAMES[ALL_FEATURES[i]] for i in order_01]\n        vals = mean_vals[order_01]\n        errs = std_vals[order_01]\n        colors = [GROUP_COLORS[FEATURE_GROUPS[ALL_FEATURES[i]]] for i in order_01]\n\n        bars = ax.barh(range(len(display)), vals, xerr=errs, color=colors, alpha=0.85, edgecolor=\"white\", linewidth=0.5)\n        ax.set_yticks(range(len(display)))\n        ax.set_yticklabels(display, fontsize=9)\n        ax.set_xlabel(\"Permutation Importance (ΔAUC)\", fontsize=10)\n        ax.set_title(title, fontsize=11, fontweight=\"bold\")\n        ax.invert_yaxis()\n        ax.axvline(x=0, color=\"gray\", linewidth=0.5, linestyle=\"--\")\n\n    from matplotlib.patches import Patch\n    legend_elements = [Patch(facecolor=c, label=GROUP_LABELS[g]) for g, c in GROUP_COLORS.items()]\n    fig.legend(handles=legend_elements, loc=\"lower center\", ncol=4, fontsize=8, bbox_to_anchor=(0.5, -0.02))\n\n    fig.suptitle(\"Qwen-1.5B Continuation Mode (C4) — Permutation Feature Importance\", fontsize=12, fontweight=\"bold\")\n    plt.tight_layout(rect=[0, 0.04, 1, 0.96])\n    fig.savefig(save_path, bbox_inches=\"tight\", dpi=150)\n    plt.close()\n    print(f\"Saved: {save_path}\")\n\n\ndef make_latex_table(res_0v1, res_1v2, save_path):\n    mean_01 = res_0v1[\"mean\"]\n    std_01 = res_0v1[\"std\"]\n    mean_12 = res_1v2[\"mean\"]\n    std_12 = res_1v2[\"std\"]\n\n    order_01 = np.argsort(mean_01)[::-1]\n\n    lines = [\n        r\"\\begin{tabular}{llrr}\",\n        r\"\\toprule\",\n        r\"Group & Feature & 0\\,vs\\,1 & 1\\,vs\\,2 \\\\\",\n        r\"\\midrule\",\n    ]\n\n    prev_group = None\n    for i in order_01:\n        feat = ALL_FEATURES[i]\n        group = FEATURE_GROUPS[feat]\n        group_label = GROUP_LABELS[group] if group != prev_group else \"\"\n        prev_group = group\n\n        val_01 = f\"{mean_01[i]:.4f} \\\\pm {std_01[i]:.4f}\"\n        val_12 = f\"{mean_12[i]:.4f} \\\\pm {std_12[i]:.4f}\"\n\n        lines.append(f\"  {group_label} & {DISPLAY_NAMES[feat]} & ${val_01}$ & ${val_12}$ \\\\\\\\\")\n\n    lines.append(r\"\\bottomrule\")\n    lines.append(r\"\\end{tabular}\")\n\n    with open(save_path, \"w\") as f:\n        f.write(\"\\n\".join(lines))\n    print(f\"Saved: {save_path}\")\n\n\ndef main():\n    print(f\"Loading data from {DATA_PATH}\")\n    doc_ids, depths, feat_dict = load_data()\n    print(f\"Loaded {len(doc_ids)} samples, depths: {sorted(set(depths))}\")\n\n    # 0 vs 1\n    print(\"\\n=== 0 vs 1 (human vs first generation) ===\")\n    ids_01, X_01, y_01 = get_pair_data(doc_ids, depths, feat_dict, 0, 1)\n    print(f\"  Samples: {len(y_01)} (class 0: {(y_01==0).sum()}, class 1: {(y_01==1).sum()})\")\n    mean_01, std_01, auc_01 = compute_permutation_importance(X_01, y_01, ids_01)\n    print(f\"  Baseline AUC: {auc_01:.4f}\")\n    print(\"  Top-5 features:\")\n    top5_01 = np.argsort(mean_01)[::-1][:5]\n    for rank, i in enumerate(top5_01, 1):\n        print(f\"    {rank}. {ALL_FEATURES[i]:20s} {mean_01[i]:.4f} ± {std_01[i]:.4f}\")\n\n    # 1 vs 2\n    print(\"\\n=== 1 vs 2 (K* boundary) ===\")\n    ids_12, X_12, y_12 = get_pair_data(doc_ids, depths, feat_dict, 1, 2)\n    print(f\"  Samples: {len(y_12)} (class 0: {(y_12==0).sum()}, class 1: {(y_12==1).sum()})\")\n    mean_12, std_12, auc_12 = compute_permutation_importance(X_12, y_12, ids_12)\n    print(f\"  Baseline AUC: {auc_12:.4f}\")\n    print(\"  Top-5 features:\")\n    top5_12 = np.argsort(mean_12)[::-1][:5]\n    for rank, i in enumerate(top5_12, 1):\n        print(f\"    {rank}. {ALL_FEATURES[i]:20s} {mean_12[i]:.4f} ± {std_12[i]:.4f}\")\n\n    # 2 vs 3\n    print(\"\\n=== 2 vs 3 (post-boundary, expected indistinguishable) ===\")\n    ids_23, X_23, y_23 = get_pair_data(doc_ids, depths, feat_dict, 2, 3)\n    print(f\"  Samples: {len(y_23)} (class 0: {(y_23==0).sum()}, class 1: {(y_23==1).sum()})\")\n    mean_23, std_23, auc_23 = compute_permutation_importance(X_23, y_23, ids_23)\n    print(f\"  Baseline AUC: {auc_23:.4f}\")\n    print(\"  Top-5 features:\")\n    top5_23 = np.argsort(mean_23)[::-1][:5]\n    for rank, i in enumerate(top5_23, 1):\n        print(f\"    {rank}. {ALL_FEATURES[i]:20s} {mean_23[i]:.4f} ± {std_23[i]:.4f}\")\n\n    # Save results\n    results = {\n        \"data_path\": str(DATA_PATH),\n        \"model\": \"Qwen-1.5B-cont\",\n        \"domain\": \"C4\",\n        \"mode\": \"continuation (retrain chain)\",\n        \"n_repeats\": N_REPEATS,\n        \"n_folds\": N_FOLDS,\n        \"lgb_params\": LGB_PARAMS,\n        \"features\": ALL_FEATURES,\n        \"0v1\": {\n            \"baseline_auc\": round(auc_01, 4),\n            \"importance\": {ALL_FEATURES[i]: {\"mean\": round(float(mean_01[i]), 6), \"std\": round(float(std_01[i]), 6)} for i in range(len(ALL_FEATURES))},\n            \"ranking\": [ALL_FEATURES[i] for i in np.argsort(mean_01)[::-1]],\n        },\n        \"1v2\": {\n            \"baseline_auc\": round(auc_12, 4),\n            \"importance\": {ALL_FEATURES[i]: {\"mean\": round(float(mean_12[i]), 6), \"std\": round(float(std_12[i]), 6)} for i in range(len(ALL_FEATURES))},\n            \"ranking\": [ALL_FEATURES[i] for i in np.argsort(mean_12)[::-1]],\n        },\n        \"2v3\": {\n            \"baseline_auc\": round(auc_23, 4),\n            \"importance\": {ALL_FEATURES[i]: {\"mean\": round(float(mean_23[i]), 6), \"std\": round(float(std_23[i]), 6)} for i in range(len(ALL_FEATURES))},\n            \"ranking\": [ALL_FEATURES[i] for i in np.argsort(mean_23)[::-1]],\n        },\n    }\n\n    results_path = OUT_DIR / \"importance_results.json\"\n    with open(results_path, \"w\") as f:\n        json.dump(results, f, indent=2)\n    print(f\"\\nSaved: {results_path}\")\n\n    # Visualizations\n    res_0v1 = {\"mean\": mean_01, \"std\": std_01}\n    res_1v2 = {\"mean\": mean_12, \"std\": std_12}\n\n    pdf_path = ART_DIR / \"feature_importance_qwen_1.5b_cont.pdf\"\n    make_barplot(res_0v1, res_1v2, pdf_path)\n\n    tex_path = ART_DIR / \"feature_importance_qwen_1.5b_cont.tex\"\n    make_latex_table(res_0v1, res_1v2, tex_path)\n\n    # Summary\n    print(\"\\n\" + \"=\"*60)\n    print(\"KEY FINDINGS\")\n    print(\"=\"*60)\n    print(f\"\\n1. 0v1 classification AUC: {auc_01:.4f}\")\n    print(f\"   1v2 classification AUC: {auc_12:.4f}\")\n    print(f\"   2v3 classification AUC: {auc_23:.4f}\")\n\n    surp_mean_idx = ALL_FEATURES.index(\"surp_mean\")\n    print(f\"\\n2. Mean Surprisal contribution to 0v1: {mean_01[surp_mean_idx]:.4f} \"\n          f\"({mean_01[surp_mean_idx]/mean_01.sum()*100:.1f}% of total positive importance)\")\n\n    print(f\"\\n3. Top feature for 1v2 boundary: {ALL_FEATURES[np.argmax(mean_12)]} \"\n          f\"(importance: {mean_12.max():.4f})\")\n\n    print(f\"\\n4. Importance concentration (Gini-like):\")\n    for name, imp in [(\"0v1\", mean_01), (\"1v2\", mean_12), (\"2v3\", mean_23)]:\n        pos_imp = np.maximum(imp, 0)\n        if pos_imp.sum() > 0:\n            normed = pos_imp / pos_imp.sum()\n            gini = 1 - (normed**2).sum()\n            print(f\"   {name}: entropy={gini:.3f} (higher=more distributed)\")\n\n\nif __name__ == \"__main__\":\n    main()\nPYEOF\necho \"Script created successfully\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_feat_importance_qwen15b_cont_20260521T073611",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "cat > /root/autodl-tmp/gen-depth-contamination/scripts/feature_importance_qwen_cont.py << 'PYEOF'\n\"\"\"\nPermutation Importance Analysis for 15D OBD Features\nQwen-1.5B continuation mode (retrain chain) on C4\n\"\"\"\n\nimport csv\nimport json\nimport os\nimport sys\nfrom pathlib import Path\n\nimport numpy as np\nimport matplotlib\nmatplotlib.use(\"Agg\")\nimport matplotlib.pyplot as plt\nfrom sklearn.inspection import permutation_importance\nfrom sklearn.metrics import roc_auc_score\nfrom sklearn.model_selection import GroupKFold\nimport lightgbm as lgb\n\nos.environ[\"CUDA_VISIBLE_DEVICES\"] = \"3\"\nos.environ[\"OMP_NUM_THREADS\"] = \"4\"\n\nDATA_PATH = Path(\"/root/autodl-tmp/gen-depth-contamination/data/exp_qwen_retrain_chain/features.csv\")\nOUT_DIR = Path(\"/root/autodl-tmp/gen-depth-contamination/results/feature_importance_qwen_cont\")\nART_DIR = Path(\"/root/autodl-tmp/gen-depth-contamination/artifacts\")\nOUT_DIR.mkdir(parents=True, exist_ok=True)\nART_DIR.mkdir(parents=True, exist_ok=True)\n\nALL_FEATURES = [\n    \"surp_mean\", \"surp_std\", \"surp_skew\", \"surp_kurt\",\n    \"surp_d1_mean\", \"surp_d1_std\", \"surp_d1_skew\",\n    \"surp_d2_mean\", \"surp_d2_std\",\n    \"ttr\", \"hapax_ratio\", \"self_bleu\",\n    \"freq_kurtosis\", \"freq_entropy\", \"low_freq_ratio\",\n]\n\nFEATURE_GROUPS = {\n    \"surp_mean\": \"surprisal_base\", \"surp_std\": \"surprisal_base\",\n    \"surp_skew\": \"surprisal_base\", \"surp_kurt\": \"surprisal_base\",\n    \"surp_d1_mean\": \"surprisal_deriv\", \"surp_d1_std\": \"surprisal_deriv\",\n    \"surp_d1_skew\": \"surprisal_deriv\",\n    \"surp_d2_mean\": \"surprisal_deriv\", \"surp_d2_std\": \"surprisal_deriv\",\n    \"ttr\": \"lexical_diversity\", \"hapax_ratio\": \"lexical_diversity\",\n    \"self_bleu\": \"lexical_diversity\",\n    \"freq_kurtosis\": \"freq_distribution\", \"freq_entropy\": \"freq_distribution\",\n    \"low_freq_ratio\": \"freq_distribution\",\n}\n\nDISPLAY_NAMES = {\n    \"surp_mean\": \"Mean Surprisal\",\n    \"surp_std\": \"Surprisal Std\",\n    \"surp_skew\": \"Surprisal Skew\",\n    \"surp_kurt\": \"Surprisal Kurtosis\",\n    \"surp_d1_mean\": \"Δ¹ Surprisal Mean\",\n    \"surp_d1_std\": \"Δ¹ Surprisal Std\",\n    \"surp_d1_skew\": \"Δ¹ Surprisal Skew\",\n    \"surp_d2_mean\": \"Δ² Surprisal Mean\",\n    \"surp_d2_std\": \"Δ² Surprisal Std\",\n    \"ttr\": \"TTR\",\n    \"hapax_ratio\": \"Hapax Ratio\",\n    \"self_bleu\": \"Self-BLEU\",\n    \"freq_kurtosis\": \"Freq Kurtosis\",\n    \"freq_entropy\": \"Freq Entropy\",\n    \"low_freq_ratio\": \"Low-Freq Ratio\",\n}\n\nLGB_PARAMS = dict(\n    n_estimators=200, max_depth=6, learning_rate=0.05,\n    num_leaves=31, verbose=-1, n_jobs=4,\n)\n\nN_REPEATS = 10\nN_FOLDS = 5\n\n\ndef load_data():\n    with open(DATA_PATH) as f:\n        rows = list(csv.DictReader(f))\n    doc_ids = np.array([int(r[\"doc_id\"]) for r in rows])\n    depths = np.array([int(r[\"depth\"]) for r in rows])\n    feat_dict = {}\n    for col in ALL_FEATURES:\n        vals = []\n        for r in rows:\n            v = r[col]\n            vals.append(float(v) if v != \"\" and v != \"nan\" else np.nan)\n        feat_dict[col] = np.array(vals)\n    return doc_ids, depths, feat_dict\n\n\ndef get_pair_data(doc_ids, depths, feat_dict, d_low, d_high):\n    mask = (depths == d_low) | (depths == d_high)\n    ids = doc_ids[mask]\n    y = (depths[mask] == d_high).astype(int)\n    X = np.column_stack([feat_dict[col][mask] for col in ALL_FEATURES])\n    nan_mask = np.isnan(X).any(axis=1)\n    if nan_mask.any():\n        valid = ~nan_mask\n        X, y, ids = X[valid], y[valid], ids[valid]\n    return ids, X, y\n\n\ndef compute_permutation_importance(X, y, groups):\n    gkf = GroupKFold(n_splits=N_FOLDS)\n    all_importances = []\n    fold_aucs = []\n\n    for train_idx, test_idx in gkf.split(X, y, groups):\n        X_train, X_test = X[train_idx], X[test_idx]\n        y_train, y_test = y[train_idx], y[test_idx]\n\n        model = lgb.LGBMClassifier(**LGB_PARAMS)\n        model.fit(X_train, y_train)\n\n        baseline_auc = roc_auc_score(y_test, model.predict_proba(X_test)[:, 1])\n        fold_aucs.append(baseline_auc)\n\n        result = permutation_importance(\n            model, X_test, y_test,\n            n_repeats=N_REPEATS,\n            scoring=\"roc_auc\",\n            random_state=42,\n        )\n        all_importances.append(result.importances_mean)\n\n    mean_importance = np.mean(all_importances, axis=0)\n    std_importance = np.std(all_importances, axis=0)\n    mean_auc = np.mean(fold_aucs)\n\n    return mean_importance, std_importance, mean_auc\n\n\nGROUP_COLORS = {\n    \"surprisal_base\": \"#2196F3\",\n    \"surprisal_deriv\": \"#4CAF50\",\n    \"lexical_diversity\": \"#FF9800\",\n    \"freq_distribution\": \"#9C27B0\",\n}\n\nGROUP_LABELS = {\n    \"surprisal_base\": \"Surprisal (base)\",\n    \"surprisal_deriv\": \"Surprisal (derivatives)\",\n    \"lexical_diversity\": \"Lexical diversity\",\n    \"freq_distribution\": \"Frequency distribution\",\n}\n\n\ndef make_barplot(res_0v1, res_1v2, save_path):\n    mean_01 = res_0v1[\"mean\"]\n    std_01 = res_0v1[\"std\"]\n    mean_12 = res_1v2[\"mean\"]\n    std_12 = res_1v2[\"std\"]\n\n    order_01 = np.argsort(mean_01)[::-1]\n\n    fig, axes = plt.subplots(1, 2, figsize=(14, 5), sharey=True)\n\n    for ax, mean_vals, std_vals, title in [\n        (axes[0], mean_01, std_01, \"0 vs 1 (human vs gen-1)\"),\n        (axes[1], mean_12, std_12, \"1 vs 2 (K* boundary)\"),\n    ]:\n        display = [DISPLAY_NAMES[ALL_FEATURES[i]] for i in order_01]\n        vals = mean_vals[order_01]\n        errs = std_vals[order_01]\n        colors = [GROUP_COLORS[FEATURE_GROUPS[ALL_FEATURES[i]]] for i in order_01]\n\n        bars = ax.barh(range(len(display)), vals, xerr=errs, color=colors, alpha=0.85, edgecolor=\"white\", linewidth=0.5)\n        ax.set_yticks(range(len(display)))\n        ax.set_yticklabels(display, fontsize=9)\n        ax.set_xlabel(\"Permutation Importance (ΔAUC)\", fontsize=10)\n        ax.set_title(title, fontsize=11, fontweight=\"bold\")\n        ax.invert_yaxis()\n        ax.axvline(x=0, color=\"gray\", linewidth=0.5, linestyle=\"--\")\n\n    from matplotlib.patches import Patch\n    legend_elements = [Patch(facecolor=c, label=GROUP_LABELS[g]) for g, c in GROUP_COLORS.items()]\n    fig.legend(handles=legend_elements, loc=\"lower center\", ncol=4, fontsize=8, bbox_to_anchor=(0.5, -0.02))\n\n    fig.suptitle(\"Qwen-1.5B Continuation Mode (C4) — Permutation Feature Importance\", fontsize=12, fontweight=\"bold\")\n    plt.tight_layout(rect=[0, 0.04, 1, 0.96])\n    fig.savefig(save_path, bbox_inches=\"tight\", dpi=150)\n    plt.close()\n    print(f\"Saved: {save_path}\")\n\n\ndef make_latex_table(res_0v1, res_1v2, save_path):\n    mean_01 = res_0v1[\"mean\"]\n    std_01 = res_0v1[\"std\"]\n    mean_12 = res_1v2[\"mean\"]\n    std_12 = res_1v2[\"std\"]\n\n    order_01 = np.argsort(mean_01)[::-1]\n\n    lines = [\n        r\"\\begin{tabular}{llrr}\",\n        r\"\\toprule\",\n        r\"Group & Feature & 0\\,vs\\,1 & 1\\,vs\\,2 \\\\\",\n        r\"\\midrule\",\n    ]\n\n    prev_group = None\n    for i in order_01:\n        feat = ALL_FEATURES[i]\n        group = FEATURE_GROUPS[feat]\n        group_label = GROUP_LABELS[group] if group != prev_group else \"\"\n        prev_group = group\n\n        val_01 = f\"{mean_01[i]:.4f} \\\\pm {std_01[i]:.4f}\"\n        val_12 = f\"{mean_12[i]:.4f} \\\\pm {std_12[i]:.4f}\"\n\n        lines.append(f\"  {group_label} & {DISPLAY_NAMES[feat]} & ${val_01}$ & ${val_12}$ \\\\\\\\\")\n\n    lines.append(r\"\\bottomrule\")\n    lines.append(r\"\\end{tabular}\")\n\n    with open(save_path, \"w\") as f:\n        f.write(\"\\n\".join(lines))\n    print(f\"Saved: {save_path}\")\n\n\ndef main():\n    print(f\"Loading data from {DATA_PATH}\")\n    doc_ids, depths, feat_dict = load_data()\n    print(f\"Loaded {len(doc_ids)} samples, depths: {sorted(set(depths))}\")\n\n    # 0 vs 1\n    print(\"\\n=== 0 vs 1 (human vs first generation) ===\")\n    ids_01, X_01, y_01 = get_pair_data(doc_ids, depths, feat_dict, 0, 1)\n    print(f\"  Samples: {len(y_01)} (class 0: {(y_01==0).sum()}, class 1: {(y_01==1).sum()})\")\n    mean_01, std_01, auc_01 = compute_permutation_importance(X_01, y_01, ids_01)\n    print(f\"  Baseline AUC: {auc_01:.4f}\")\n    print(\"  Top-5 features:\")\n    top5_01 = np.argsort(mean_01)[::-1][:5]\n    for rank, i in enumerate(top5_01, 1):\n        print(f\"    {rank}. {ALL_FEATURES[i]:20s} {mean_01[i]:.4f} ± {std_01[i]:.4f}\")\n\n    # 1 vs 2\n    print(\"\\n=== 1 vs 2 (K* boundary) ===\")\n    ids_12, X_12, y_12 = get_pair_data(doc_ids, depths, feat_dict, 1, 2)\n    print(f\"  Samples: {len(y_12)} (class 0: {(y_12==0).sum()}, class 1: {(y_12==1).sum()})\")\n    mean_12, std_12, auc_12 = compute_permutation_importance(X_12, y_12, ids_12)\n    print(f\"  Baseline AUC: {auc_12:.4f}\")\n    print(\"  Top-5 features:\")\n    top5_12 = np.argsort(mean_12)[::-1][:5]\n    for rank, i in enumerate(top5_12, 1):\n        print(f\"    {rank}. {ALL_FEATURES[i]:20s} {mean_12[i]:.4f} ± {std_12[i]:.4f}\")\n\n    # 2 vs 3\n    print(\"\\n=== 2 vs 3 (post-boundary, expected indistinguishable) ===\")\n    ids_23, X_23, y_23 = get_pair_data(doc_ids, depths, feat_dict, 2, 3)\n    print(f\"  Samples: {len(y_23)} (class 0: {(y_23==0).sum()}, class 1: {(y_23==1).sum()})\")\n    mean_23, std_23, auc_23 = compute_permutation_importance(X_23, y_23, ids_23)\n    print(f\"  Baseline AUC: {auc_23:.4f}\")\n    print(\"  Top-5 features:\")\n    top5_23 = np.argsort(mean_23)[::-1][:5]\n    for rank, i in enumerate(top5_23, 1):\n        print(f\"    {rank}. {ALL_FEATURES[i]:20s} {mean_23[i]:.4f} ± {std_23[i]:.4f}\")\n\n    # Save results\n    results = {\n        \"data_path\": str(DATA_PATH),\n        \"model\": \"Qwen-1.5B-cont\",\n        \"domain\": \"C4\",\n        \"mode\": \"continuation (retrain chain)\",\n        \"n_repeats\": N_REPEATS,\n        \"n_folds\": N_FOLDS,\n        \"lgb_params\": LGB_PARAMS,\n        \"features\": ALL_FEATURES,\n        \"0v1\": {\n            \"baseline_auc\": round(auc_01, 4),\n            \"importance\": {ALL_FEATURES[i]: {\"mean\": round(float(mean_01[i]), 6), \"std\": round(float(std_01[i]), 6)} for i in range(len(ALL_FEATURES))},\n            \"ranking\": [ALL_FEATURES[i] for i in np.argsort(mean_01)[::-1]],\n        },\n        \"1v2\": {\n            \"baseline_auc\": round(auc_12, 4),\n            \"importance\": {ALL_FEATURES[i]: {\"mean\": round(float(mean_12[i]), 6), \"std\": round(float(std_12[i]), 6)} for i in range(len(ALL_FEATURES))},\n            \"ranking\": [ALL_FEATURES[i] for i in np.argsort(mean_12)[::-1]],\n        },\n        \"2v3\": {\n            \"baseline_auc\": round(auc_23, 4),\n            \"importance\": {ALL_FEATURES[i]: {\"mean\": round(float(mean_23[i]), 6), \"std\": round(float(std_23[i]), 6)} for i in range(len(ALL_FEATURES))},\n            \"ranking\": [ALL_FEATURES[i] for i in np.argsort(mean_23)[::-1]],\n        },\n    }\n\n    results_path = OUT_DIR / \"importance_results.json\"\n    with open(results_path, \"w\") as f:\n        json.dump(results, f, indent=2)\n    print(f\"\\nSaved: {results_path}\")\n\n    # Visualizations\n    res_0v1 = {\"mean\": mean_01, \"std\": std_01}\n    res_1v2 = {\"mean\": mean_12, \"std\": std_12}\n\n    pdf_path = ART_DIR / \"feature_importance_qwen_1.5b_cont.pdf\"\n    make_barplot(res_0v1, res_1v2, pdf_path)\n\n    tex_path = ART_DIR / \"feature_importance_qwen_1.5b_cont.tex\"\n    make_latex_table(res_0v1, res_1v2, tex_path)\n\n    # Summary\n    print(\"\\n\" + \"=\"*60)\n    print(\"KEY FINDINGS\")\n    print(\"=\"*60)\n    print(f\"\\n1. 0v1 classification AUC: {auc_01:.4f}\")\n    print(f\"   1v2 classification AUC: {auc_12:.4f}\")\n    print(f\"   2v3 classification AUC: {auc_23:.4f}\")\n\n    surp_mean_idx = ALL_FEATURES.index(\"surp_mean\")\n    print(f\"\\n2. Mean Surprisal contribution to 0v1: {mean_01[surp_mean_idx]:.4f} \"\n          f\"({mean_01[surp_mean_idx]/mean_01.sum()*100:.1f}% of total positive importance)\")\n\n    print(f\"\\n3. Top feature for 1v2 boundary: {ALL_FEATURES[np.argmax(mean_12)]} \"\n          f\"(importance: {mean_12.max():.4f})\")\n\n    print(f\"\\n4. Importance concentration (Gini-like):\")\n    for name, imp in [(\"0v1\", mean_01), (\"1v2\", mean_12), (\"2v3\", mean_23)]:\n        pos_imp = np.maximum(imp, 0)\n        if pos_imp.sum() > 0:\n            normed = pos_imp / pos_imp.sum()\n            gini = 1 - (normed**2).sum()\n            print(f\"   {name}: entropy={gini:.3f} (higher=more distributed)\")\n\n\nif __name__ == \"__main__\":\n    main()\nPYEOF\necho \"Script created successfully\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-21T07:40:20.610209+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Script created successfully\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.55}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_feat_importance_qwen15b_cont_20260521T073611",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-21T07:40:20.610384+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-22115",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/gen-depth-contamination && CUDA_VISIBLE_DEVICES=3 python scripts/feature_importance_qwen_cont.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_feat_importance_qwen15b_cont_20260521T073611",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/gen-depth-contamination && CUDA_VISIBLE_DEVICES=3 python scripts/feature_importance_qwen_cont.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-21T07:40:20.610648+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Loading data from /root/autodl-tmp/gen-depth-contamination/data/exp_qwen_retrain_chain/features.csv\\nLoaded 40000 samples, depths: [np.int64(0), np.int64(1), np.int64(2), np.int64(3), np.int64(4), np.int64(5), np.int64(6), np.int64(7)]\\n\\n=== 0 vs 1 (human vs first generation) ===\\n  Samples: 8149 (class 0: 3598, class 1: 4551)\\n  Baseline AUC: 0.9945\\n  Top-5 features:\\n    1. surp_d1_std          0.1939 ± 0.0144\\n    2. surp_std             0.0562 ± 0.0059\\n    3. surp_mean            0.0108 ± 0.0019\\n    4. surp_skew            0.0038 ± 0.0011\\n    5. surp_kurt            0.0038 ± 0.0006\\n\\n=== 1 vs 2 (K* boundary) ===\\n  Samples: 9388 (class 0: 4551, class 1: 4837)\\n  Baseline AUC: 0.9025\\n  Top-5 features:\\n    1. surp_skew            0.0915 ± 0.0110\\n    2. surp_std             0.0841 ± 0.0051\\n    3. surp_d1_std          0.0234 ± 0.0050\\n    4. surp_mean            0.0220 ± 0.0035\\n    5. self_bleu            0.0159 ± 0.0012\\n\\n=== 2 vs 3 (post-boundary, expected indistinguishable) ===\\n  Samples: 9771 (class 0: 4837, class 1: 4934)\\n  Baseline AUC: 0.8099\\n  Top-5 features:\\n    1. surp_skew            0.0637 ± 0.0084\\n    2. surp_mean            0.0468 ± 0.0018\\n    3. surp_std             0.0440 ± 0.0052\\n    4. low_freq_ratio       0.0300 ± 0.0019\\n    5. hapax_ratio          0.0155 ± 0.0031\\n\\nSaved: /root/autodl-tmp/gen-depth-contamination/results/feature_importance_qwen_cont/importance_results.json\\nSaved: /root/autodl-tmp/gen-depth-contamination/artifacts/feature_importance_qwen_1.5b_cont.pdf\\nSaved: /root/autodl-tmp/gen-depth-contamination/artifacts/feature_importance_qwen_1.5b_cont.tex\\n\\n============================================================\\nKEY FINDINGS\\n============================================================\\n\\n1. 0v1 classification AUC: 0.9945\\n   1v2 classification AUC: 0.9025\\n   2v3 classification AUC: 0.8099\\n\\n2. Mean Surprisal c
…[truncated 8642 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_feat_importance_qwen15b_cont_20260521T073611",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 53 · 2026-05-21T07:40:20.610884+00:00_

完成。结果如下：

```
MODEL: Qwen-1.5B-cont
DOMAIN: C4
DATA: data/exp_qwen_retrain_chain/features.csv (40K samples, depths 0-7)

0v1_BASELINE_AUC: 0.9945
0v1_TOP3: surp_d1_std (0.1939), surp_std (0.0562), surp_mean (0.0108)

1v2_BASELINE_AUC: 0.9025
1v2_TOP3: surp_skew (0.0915), surp_std (0.0841), surp_d1_std (0.0234)

2v3_BASELINE_AUC: 0.8099
2v3_TOP3: surp_skew (0.0637), surp_mean (0.0468), surp_std (0.0440)
```

输出文件：
- `results/feature_importance_qwen_cont/importance_results.json`
- `artifacts/feature_importance_qwen_1.5b_cont.pdf`
- `artifacts/feature_importance_qwen_1.5b_cont.tex`

注意：2v3 AUC 仍为 0.81，说明 continuation mode 下 depth 2 和 3 仍有较强可区分性（不像 prompt chain 那样在 K*=2 后趋于不可区分）。importance 分布从 0v1 的高度集中（surp_d1_std 独大，entropy=0.451）到 2v3 逐步分散（entropy=0.824）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_ops_feat_importance_qwen15b_cont_20260521T073611"
}
```

</details>

---
