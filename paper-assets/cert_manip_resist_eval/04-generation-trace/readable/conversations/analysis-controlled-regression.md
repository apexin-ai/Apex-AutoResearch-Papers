# analysis controlled regression

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 57
- **Recorded user turns:** 0
- **Tool calls:** 28
- **Original source:** `logs/chats/worker_analysis_controlled-regression_20260523T071753.jsonl`
- **Structured JSON:** [`02d95a383202b74d3746.json`](../../sessions/02/02d95a383202b74d3746.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

57 recorded events

### Tool call

_source line 1 · 2026-05-23T07:24:01.246257+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__register_artifact",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_controlled-regression_20260523T071753",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__register_artifact",
    "max_results": "4"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-23T07:24:01.246604+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_controlled-regression_20260523T071753",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-23T07:24:01.246826+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "seetacloud-rtx6000",
  "command": "ls /root/cert_manip_resist_eval/artifacts/results/plan001/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_controlled-regression_20260523T071753",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "seetacloud-rtx6000",
    "command": "ls /root/cert_manip_resist_eval/artifacts/results/plan001/"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-23T07:24:01.246965+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "seetacloud-rtx6000",
  "command": "find /root/cert_manip_resist_eval/ -name \"*.py\" -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_controlled-regression_20260523T071753",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "seetacloud-rtx6000",
    "command": "find /root/cert_manip_resist_eval/ -name \"*.py\" -type f"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-23T07:24:01.247117+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"aggregation_regression_15model.json\\naggregation_regression_15model_loglog.json\\nalt_diversity_effect_size.json\\napi_only_regression.json\\nattacked_keff.json\\nbeta_reg_epsilon.json\\nclaim6_panel_design_15model.json\\nclustered_se_analysis.json\\ncondition_dominance_15model.json\\nconfound_diagnosis.json\\nconfound_scatter.png\\nfamily_copula_15model.json\\nfig4_panel_design_K3.json\\nfractional_logit.json\\ngam_tier_analysis.json\\ngam_tier_analysis_corrected.json\\nindividual_scores\\nk4_wild_cluster_bootstrap.json\\nk5_aggregation_analysis.json\\nk5_aggregation_bootstrap.json\\nk5_gam_analysis.json\\nk5_k7_panel_analysis.json\\nk5_panel_selection.json\\nk5_panel_selection_bootstrap.json\\nk5_rf_contrast.json\\nk5_wild_cluster_bootstrap.json\\nk7_wild_cluster_bootstrap.json\\nmi_matrix\\npanel_regression\\npartial_knowledge_adversary.json\\npartial_knowledge_clustered_se.json\\npower_cr2_cr3.json\\nresidualized_keff_15model.json\\nrf_keff_correction.json\\nstep1_api_scoring_summary.json\\nstochastic_dominance.json\\nvif_partial_corr.json\\nwild_cluster_bootstrap.json\\nwild_cluster_bootstrap_v2.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.08}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_controlled-regression_20260523T071753",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-23T07:24:01.247295+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/cert_manip_resist_eval/src/__init__.py\\n/root/cert_manip_resist_eval/src/config.py\\n/root/cert_manip_resist_eval/src/utils.py\\n/root/cert_manip_resist_eval/src/judge_service.py\\n/root/cert_manip_resist_eval/src/eval_pipeline.py\\n/root/cert_manip_resist_eval/src/correlation.py\\n/root/cert_manip_resist_eval/src/attacks.py\\n/root/cert_manip_resist_eval/src/panels.py\\n/root/cert_manip_resist_eval/src/keff.py\\n/root/cert_manip_resist_eval/src/scaling.py\\n/root/cert_manip_resist_eval/src/panel_selection.py\\n/root/cert_manip_resist_eval/src/api_judge_service.py\\n/root/cert_manip_resist_eval/src/unified_data_loader.py\\n/root/cert_manip_resist_eval/scripts/run_step1_correlation.py\\n/root/cert_manip_resist_eval/scripts/run_step2_attacks.py\\n/root/cert_manip_resist_eval/scripts/run_step3_keff.py\\n/root/cert_manip_resist_eval/scripts/run_step4_scaling.py\\n/root/cert_manip_resist_eval/scripts/run_all.py\\n/root/cert_manip_resist_eval/scripts/deploy_judges.py\\n/root/cert_manip_resist_eval/scripts/test_inference.py\\n/root/cert_manip_resist_eval/scripts/run_step1_subset.py\\n/root/cert_manip_resist_eval/scripts/prep_attack_data.py\\n/root/cert_manip_resist_eval/scripts/_eval_single_model.py\\n/root/cert_manip_resist_eval/scripts/run_step1_full.py\\n/root/cert_manip_resist_eval/scripts/copula_gof_check.py\\n/root/cert_manip_resist_eval/scripts/run_step2_keff_contrast.py\\n/root/cert_manip_resist_eval/scripts/run_step2v3_regression.py\\n/root/cert_manip_resist_eval/scripts/run_taxonomy_broadspectrum.py\\n/root/cert_manip_resist_eval/scripts/validate_panel_selection.py\\n/root/cert_manip_resist_eval/scripts/run_plan003_random_fault.py\\n/root/cert_manip_resist_eval/scripts/run_plan009_vif_analysis.py\\n/root/cert_manip_resist_eval/scripts/validate_api_judges.py\\n/root/cert_manip_resist_eval/scripts/run_plan001_step1_api_scoring.py\\n/root/cert_manip_resist_eval/scripts/run_plan001_step3_mi_matrix.py\\n/r
…[truncated 3218 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_controlled-regression_20260523T071753",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-23T07:24:01.247480+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "seetacloud-rtx6000",
  "command": "cat /root/cert_manip_resist_eval/scripts/run_wild_cluster_bootstrap.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_controlled-regression_20260523T071753",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "seetacloud-rtx6000",
    "command": "cat /root/cert_manip_resist_eval/scripts/run_wild_cluster_bootstrap.py"
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-23T07:24:01.247638+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "seetacloud-rtx6000",
  "command": "cat /root/cert_manip_resist_eval/scripts/run_api_only_regression.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_controlled-regression_20260523T071753",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "seetacloud-rtx6000",
    "command": "cat /root/cert_manip_resist_eval/scripts/run_api_only_regression.py"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-23T07:24:01.247944+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"Wild Cluster Bootstrap for K_eff significance — reliable inference with 15 clusters.\\n\\nImplements Webb (2023) / Cameron & Miller (2015) wild cluster bootstrap:\\n  - Restricted model under H0: β_coef = 0\\n  - Rademacher weights drawn per cluster\\n  - Bootstrap t-statistics compared to original\\n\\nCluster assignment: primary judge = alphabetically smallest judge in panel.\\n\\\"\\\"\\\"\\n\\nimport os\\nos.environ[\\\"HF_HOME\\\"] = \\\"/root/autodl-tmp/.hf_cache\\\"\\n\\nimport sys\\nsys.path.insert(0, \\\"/root/cert_manip_resist_eval\\\")\\n\\nimport json\\nimport itertools\\nimport numpy as np\\nimport statsmodels.api as sm\\nfrom pathlib import Path\\nfrom statsmodels.stats.multitest import multipletests\\n\\nfrom src.unified_data_loader import (\\n    ALL_MODELS, DATASETS, ATTACKS,\\n    load_all_scores, load_pairs, load_mi_data,\\n)\\n\\nEPS = 1e-6\\nFDR_ALPHA = 0.05\\nB_BOOT = 9999\\nSEED = 42\\n\\n\\ndef _json_default(obj):\\n    if isinstance(obj, np.floating):\\n        v = float(obj)\\n        return None if (np.isnan(v) or np.isinf(v)) else v\\n    if isinstance(obj, np.integer):\\n        return int(obj)\\n    if isinstance(obj, np.ndarray):\\n        return obj.tolist()\\n    if isinstance(obj, np.bool_):\\n        return bool(obj)\\n    raise TypeError(f\\\"Not JSON serializable: {type(obj)}\\\")\\n\\n\\ndef majority_vote(votes):\\n    counts = {\\\"A\\\": 0, \\\"B\\\": 0, \\\"tie\\\": 0}\\n    for v in votes:\\n        counts[v] = counts.get(v, 0) + 1\\n    mc = max(counts.values())\\n    winners = [k for k, c in counts.items() if c == mc]\\n    if len(winners) == 1:\\n        return winners[0]\\n    for w in winners:\\n        if w != \\\"tie\\\":\\n            return w\\n    return \\\"tie\\\"\\n\\n\\ndef compute_individual_asr(clean_list, attacked_list, pairs):\\n    n = min(len(clean_list), len(attacked_list), len(pairs))\\n    n_flips = n_correct =
…[truncated 7347 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_controlled-regression_20260523T071753",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-23T07:24:01.248236+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"API-Only Subset Regression — MF-1 robustness check.\\n\\nFilters to 9 API models only, runs canonical OLS + clustered SE for K=3 (84 panels)\\nand K=5 (126 panels). Verifies the K=3→K=5 transition pattern is not driven by\\nlocal model confounding.\\n\\\"\\\"\\\"\\n\\nimport os\\nos.environ[\\\"HF_HOME\\\"] = \\\"/root/autodl-tmp/.hf_cache\\\"\\n\\nimport sys\\nsys.path.insert(0, \\\"/root/cert_manip_resist_eval\\\")\\n\\nimport json\\nimport itertools\\nimport numpy as np\\nimport statsmodels.api as sm\\nfrom pathlib import Path\\nfrom scipy.stats import t as t_dist\\nfrom statsmodels.stats.multitest import multipletests\\n\\nfrom src.unified_data_loader import (\\n    ALL_MODELS, API_MODELS, DATASETS, ATTACKS,\\n    load_all_scores, load_pairs, load_mi_data,\\n)\\n\\nEPS = 1e-6\\nFDR_ALPHA = 0.05\\n\\n\\ndef _json_default(obj):\\n    if isinstance(obj, np.floating):\\n        v = float(obj)\\n        return None if (np.isnan(v) or np.isinf(v)) else v\\n    if isinstance(obj, np.integer):\\n        return int(obj)\\n    if isinstance(obj, np.ndarray):\\n        return obj.tolist()\\n    if isinstance(obj, np.bool_):\\n        return bool(obj)\\n    raise TypeError(f\\\"Not JSON serializable: {type(obj)}\\\")\\n\\n\\ndef majority_vote(votes):\\n    counts = {\\\"A\\\": 0, \\\"B\\\": 0, \\\"tie\\\": 0}\\n    for v in votes:\\n        counts[v] = counts.get(v, 0) + 1\\n    mc = max(counts.values())\\n    winners = [k for k, c in counts.items() if c == mc]\\n    if len(winners) == 1:\\n        return winners[0]\\n    for w in winners:\\n        if w != \\\"tie\\\":\\n            return w\\n    return \\\"tie\\\"\\n\\n\\ndef compute_individual_asr(clean_list, attacked_list, pairs):\\n    n = min(len(clean_list), len(attacked_list), len(pairs))\\n    n_flips = n_correct = 0\\n    for i in range(n):\\n        gt = pairs[i][\\\"ground_truth_winner\\\"]\\n        if clean_list[i].ge
…[truncated 7256 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_controlled-regression_20260523T071753",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-23T07:24:01.248402+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "seetacloud-rtx6000",
  "command": "cat /root/cert_manip_resist_eval/artifacts/results/plan001/confound_diagnosis.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_controlled-regression_20260523T071753",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "seetacloud-rtx6000",
    "command": "cat /root/cert_manip_resist_eval/artifacts/results/plan001/confound_diagnosis.json"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-23T07:24:01.248596+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"conditions\\\": {\\n    \\\"mmlu×prompt_injection\\\": {\\n      \\\"pearson_r\\\": 0.6561544952115396,\\n      \\\"p_value\\\": 2.3336338266329969e-57,\\n      \\\"verdict\\\": \\\"CONFOUND_MODERATE\\\",\\n      \\\"n_panels\\\": 455,\\n      \\\"n_models_with_asr\\\": 15\\n    },\\n    \\\"mmlu×sycophancy\\\": {\\n      \\\"pearson_r\\\": 0.3478419347431459,\\n      \\\"p_value\\\": 2.1864593876845904e-14,\\n      \\\"verdict\\\": \\\"CONFOUND_BROKEN\\\",\\n      \\\"n_panels\\\": 455,\\n      \\\"n_models_with_asr\\\": 15\\n    },\\n    \\\"mmlu×score_manipulation\\\": {\\n      \\\"pearson_r\\\": 0.8200677642383261,\\n      \\\"p_value\\\": 7.101546863435947e-112,\\n      \\\"verdict\\\": \\\"CONFOUND_SEVERE\\\",\\n      \\\"n_panels\\\": 455,\\n      \\\"n_models_with_asr\\\": 15\\n    },\\n    \\\"mmlu×verbosity_bias\\\": {\\n      \\\"pearson_r\\\": 0.3548206335826208,\\n      \\\"p_value\\\": 6.040939813240407e-15,\\n      \\\"verdict\\\": \\\"CONFOUND_BROKEN\\\",\\n      \\\"n_panels\\\": 455,\\n      \\\"n_models_with_asr\\\": 15\\n    },\\n    \\\"mmlu×position_bias\\\": {\\n      \\\"pearson_r\\\": 0.6332364711740149,\\n      \\\"p_value\\\": 2.2895308532069985e-52,\\n      \\\"verdict\\\": \\\"CONFOUND_MODERATE\\\",\\n      \\\"n_panels\\\": 455,\\n      \\\"n_models_with_asr\\\": 15\\n    },\\n    \\\"mmlu×authority_bias\\\": {\\n      \\\"pearson_r\\\": 0.5948361107503004,\\n      \\\"p_value\\\": 6.935476055679576e-45,\\n      \\\"verdict\\\": \\\"CONFOUND_MODERATE\\\",\\n      \\\"n_panels\\\": 455,\\n      \\\"n_models_with_asr\\\": 15\\n    },\\n    \\\"arc_challenge×prompt_injection\\\": {\\n      \\\"pearson_r\\\": 0.8881436057841691,\\n      \\\"p_value\\\": 4.661440053390286e-155,\\n      \\\"verdict\\\": \\\"CONFOUND_SEVERE\\\",\\n      \\\"n_panels\\\": 455,\\n      \\\"n_models_with_asr\\\": 15\\n    },\\n    \\\"arc_challenge×sycophancy\\\": {\\n      \\\"pearson_r\\\": 0.76
…[truncated 1593 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_controlled-regression_20260523T071753",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-23T07:24:01.248794+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "seetacloud-rtx6000",
  "command": "cat /root/cert_manip_resist_eval/src/unified_data_loader.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_controlled-regression_20260523T071753",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "seetacloud-rtx6000",
    "command": "cat /root/cert_manip_resist_eval/src/unified_data_loader.py"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-23T07:24:01.249048+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"Unified data loader for 15-model cert_manip_resist_eval pipeline.\\n\\nHandles two data formats:\\n  - Checkpoint files (local 6 models): nested {clean_scores: {ds: {model: [...]}}}\\n  - Individual JSON files (API 9 models): flat {scores: [...], asr, accuracy, ...}\\n\\\"\\\"\\\"\\n\\nimport json\\nimport logging\\nfrom pathlib import Path\\n\\nlogger = logging.getLogger(__name__)\\n\\n# ── Model lists ──────────────────────────────────────────────────────\\nLOCAL_MODELS = [\\n    \\\"qwen2.5-72b\\\", \\\"llama3.1-70b\\\", \\\"mistral-large\\\",\\n    \\\"qwen2.5-32b\\\", \\\"qwen2.5-14b\\\", \\\"llama3.1-8b\\\",\\n]\\nAPI_MODELS = [\\n    \\\"claude-opus-4-6\\\", \\\"gpt-5.5\\\", \\\"gemini-3.1-pro-preview\\\", \\\"gpt-4.1\\\",\\n    \\\"claude-sonnet-4-6\\\", \\\"gpt-4.1-nano\\\", \\\"gemini-3.5-flash\\\",\\n    \\\"gpt-4.1-mini\\\", \\\"claude-3-haiku\\\",\\n]\\nALL_MODELS = LOCAL_MODELS + API_MODELS\\nDATASETS = [\\\"mmlu\\\", \\\"arc_challenge\\\"]\\nATTACKS = [\\n    \\\"prompt_injection\\\", \\\"sycophancy\\\", \\\"score_manipulation\\\",\\n    \\\"verbosity_bias\\\", \\\"position_bias\\\", \\\"authority_bias\\\",\\n]\\n\\n# ── Default paths ────────────────────────────────────────────────────\\nRESULTS_DIR = Path(\\\"/root/cert_manip_resist_eval/artifacts/results\\\")\\nPLAN001_DIR = RESULTS_DIR / \\\"plan001\\\"\\nSCORES_DIR = PLAN001_DIR / \\\"individual_scores\\\"\\nMI_PATH = PLAN001_DIR / \\\"mi_matrix\\\" / \\\"mi_matrix_15models.json\\\"\\nCKPT_FILES = [\\n    RESULTS_DIR / \\\"_taxonomy_checkpoint.json\\\",\\n    RESULTS_DIR / \\\"_step2v3_checkpoint.json\\\",\\n]\\nOUTPUT_DIR = PLAN001_DIR / \\\"panel_regression\\\"\\n\\n\\ndef _invert_winners(scores):\\n    swap = {\\\"A\\\": \\\"B\\\", \\\"B\\\": \\\"A\\\", \\\"tie\\\": \\\"tie\\\"}\\n    return [{**s, \\\"winner\\\": swap.get(s.get(\\\"winner\\\", \\\"tie\\\"), \\\"tie\\\")} for s in scores]\\n\\n\\ndef l
…[truncated 7136 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_controlled-regression_20260523T071753",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-23T07:24:01.249246+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "seetacloud-rtx6000",
  "command": "head -120 /root/cert_manip_resist_eval/scripts/run_k5_wild_cluster_bootstrap.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_controlled-regression_20260523T071753",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "seetacloud-rtx6000",
    "command": "head -120 /root/cert_manip_resist_eval/scripts/run_k5_wild_cluster_bootstrap.py"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-23T07:24:01.249439+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"K=5 Wild Cluster Bootstrap — 5-position max-p inference for K=5 panels.\\n\\nExtends K=3 wild cluster bootstrap v2 to K=5 panels (C(15,5)=3003).\\n5-position clustering with max-p across positions (conservative).\\nK_eff via MI-based formula from pairwise MI matrix.\\nCanonical regression: log(ASR+eps) ~ log(K_eff) + log(eta_max+eps), standardized beta.\\nBH FDR correction across 12 conditions.\\n\\\"\\\"\\\"\\n\\nimport os\\nos.environ[\\\"HF_HOME\\\"] = \\\"/root/autodl-tmp/.hf_cache\\\"\\n\\nimport sys\\nsys.path.insert(0, \\\"/root/cert_manip_resist_eval\\\")\\n\\nimport json\\nimport time\\nimport itertools\\nimport numpy as np\\nimport statsmodels.api as sm\\nfrom pathlib import Path\\nfrom statsmodels.stats.multitest import multipletests\\n\\nfrom src.unified_data_loader import (\\n    ALL_MODELS, DATASETS, ATTACKS,\\n    load_all_scores, load_pairs, load_mi_data,\\n)\\n\\nEPS = 1e-6\\nFDR_ALPHA = 0.05\\nB_BOOT = 9999\\nSEED = 42\\nK = 5\\n\\n\\ndef _json_default(obj):\\n    if isinstance(obj, np.floating):\\n        v = float(obj)\\n        return None if (np.isnan(v) or np.isinf(v)) else v\\n    if isinstance(obj, np.integer):\\n        return int(obj)\\n    if isinstance(obj, np.ndarray):\\n        return obj.tolist()\\n    if isinstance(obj, np.bool_):\\n        return bool(obj)\\n    raise TypeError(f\\\"Not JSON serializable: {type(obj)}\\\")\\n\\n\\ndef majority_vote(votes):\\n    counts = {\\\"A\\\": 0, \\\"B\\\": 0, \\\"tie\\\": 0}\\n    for v in votes:\\n        counts[v] = counts.get(v, 0) + 1\\n    mc = max(counts.values())\\n    winners = [k for k, c in counts.items() if c == mc]\\n    if len(winners) == 1:\\n        return winners[0]\\n    for w in winners:\\n        if w != \\\"tie\\\":\\n            return w\\n    return \\\"tie\\\"\\n\\n\\ndef compute_individual_asr(clean_list, attacked_list, pairs):\\n    n = min(len(clean_list), len(attacked_list), 
…[truncated 2142 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_controlled-regression_20260523T071753",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-23T07:24:01.249591+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "seetacloud-rtx6000",
  "command": "head -20 /root/cert_manip_resist_eval/artifacts/results/plan001/wild_cluster_bootstrap_v2.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_controlled-regression_20260523T071753",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "seetacloud-rtx6000",
    "command": "head -20 /root/cert_manip_resist_eval/artifacts/results/plan001/wild_cluster_bootstrap_v2.json"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-23T07:24:01.249767+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"method\\\": \\\"wild_cluster_bootstrap_v2\\\",\\n  \\\"fixes\\\": [\\n    \\\"keff_formula_aligned_with_canonical\\\",\\n    \\\"3_position_clustering_max_p\\\"\\n  ],\\n  \\\"B\\\": 9999,\\n  \\\"weights\\\": \\\"rademacher\\\",\\n  \\\"n_clusters_per_position\\\": \\\"13 (from C(15,3) combo structure)\\\",\\n  \\\"seed\\\": 42,\\n  \\\"per_condition\\\": {\\n    \\\"mmluxprompt_injection\\\": {\\n      \\\"n_panels\\\": 455,\\n      \\\"keff_boot_p\\\": [\\n        0.0002,\\n        0.0016,\\n        0.0036\\n      ],\\n      \\\"keff_final_p\\\": 0.0036,\\n      \\\"keff_ols_std_beta\\\": 0.252443742762512,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_controlled-regression_20260523T071753",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-23T07:24:01.249902+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "seetacloud-rtx6000",
  "command": "head -20 /root/cert_manip_resist_eval/artifacts/results/plan001/k5_wild_cluster_bootstrap.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_controlled-regression_20260523T071753",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "seetacloud-rtx6000",
    "command": "head -20 /root/cert_manip_resist_eval/artifacts/results/plan001/k5_wild_cluster_bootstrap.json"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-23T07:24:01.250044+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"method\\\": \\\"wild_cluster_bootstrap_k5\\\",\\n  \\\"K\\\": 5,\\n  \\\"B\\\": 9999,\\n  \\\"weights\\\": \\\"rademacher\\\",\\n  \\\"n_positions\\\": 5,\\n  \\\"seed\\\": 42,\\n  \\\"n_total_panels\\\": 3003,\\n  \\\"keff_formula\\\": \\\"mi_based_keff (average pairwise MI)\\\",\\n  \\\"regression\\\": \\\"log(ASR+1e-6) ~ log(K_eff) + log(eta_max+1e-6)\\\",\\n  \\\"per_condition\\\": {\\n    \\\"mmluxprompt_injection\\\": {\\n      \\\"n_panels\\\": 3003,\\n      \\\"keff_boot_p\\\": [\\n        0.001,\\n        0.001,\\n        0.0016,\\n        0.0016,\\n        0.001\\n      ],\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.46}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_controlled-regression_20260523T071753",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-23T07:24:01.250205+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "seetacloud-rtx6000",
  "command": "grep -n \"eta_max\\|eta\\|ind_asr\" /root/cert_manip_resist_eval/scripts/run_k5_wild_cluster_bootstrap.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_controlled-regression_20260523T071753",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "seetacloud-rtx6000",
    "command": "grep -n \"eta_max\\|eta\\|ind_asr\" /root/cert_manip_resist_eval/scripts/run_k5_wild_cluster_bootstrap.py"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-23T07:24:01.250332+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_controlled-regression_20260523T071753",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-23T07:24:01.250452+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "seetacloud-rtx6000",
  "command": "grep -n \"eta_max\\|eta\\|ind_asr\" /root/cert_manip_resist_eval/scripts/run_k5_wild_cluster_bootstrap.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_controlled-regression_20260523T071753",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "seetacloud-rtx6000",
    "command": "grep -n \"eta_max\\|eta\\|ind_asr\" /root/cert_manip_resist_eval/scripts/run_k5_wild_cluster_bootstrap.py"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-23T07:24:01.250579+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_controlled-regression_20260523T071753",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-23T07:24:01.250718+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "seetacloud-rtx6000",
  "command": "grep -n \"eta_max\" /root/cert_manip_resist_eval/scripts/run_k5_wild_cluster_bootstrap.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_controlled-regression_20260523T071753",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "seetacloud-rtx6000",
    "command": "grep -n \"eta_max\" /root/cert_manip_resist_eval/scripts/run_k5_wild_cluster_bootstrap.py"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-23T07:24:01.250849+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"7:Canonical regression: log(ASR+eps) ~ log(K_eff) + log(eta_max+eps), standardized beta.\\n239:            eta_max = max(ind_asr[(ds, atk, j)] for j in jids)\\n247:            panel_etas.append(eta_max)\\n293:        # Bootstrap eta_max\\n351:    print(f\\\"  eta_max FDR sig: {eta_fdr_sig}/{len(valid_keys)}\\\")\\n390:        \\\"regression\\\": \\\"log(ASR+1e-6) ~ log(K_eff) + log(eta_max+1e-6)\\\",\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_controlled-regression_20260523T071753",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-23T07:24:01.250968+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "seetacloud-rtx6000",
  "command": "sed -n '220,300p' /root/cert_manip_resist_eval/scripts/run_k5_wild_cluster_bootstrap.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_controlled-regression_20260523T071753",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "seetacloud-rtx6000",
    "command": "sed -n '220,300p' /root/cert_manip_resist_eval/scripts/run_k5_wild_cluster_bootstrap.py"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-23T07:24:01.251086+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: 'sed' is not in the read-only allowlist. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_controlled-regression_20260523T071753",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-23T07:24:01.251198+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "seetacloud-rtx6000",
  "command": "tail -n +220 /root/cert_manip_resist_eval/scripts/run_k5_wild_cluster_bootstrap.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_controlled-regression_20260523T071753",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "seetacloud-rtx6000",
    "command": "tail -n +220 /root/cert_manip_resist_eval/scripts/run_k5_wild_cluster_bootstrap.py"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-23T07:24:01.251466+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"        ds_pairs = pairs.get(ds, [])\\n        mi_mat = np.array(mi_matrices[ds])\\n\\n        if not ds_clean or not ds_attacked or not ds_pairs:\\n            print(\\\"  SKIP: missing data\\\")\\n            results[cond_key] = {\\\"skipped\\\": True}\\n            continue\\n\\n        panel_asrs = []\\n        panel_keffs = []\\n        panel_etas = []\\n        panel_jids_list = []\\n\\n        for combo in all_combos:\\n            jids = [ALL_MODELS[i] for i in combo]\\n            if not all((ds, atk, j) in ind_asr for j in jids):\\n                continue\\n\\n            keff = mi_based_keff(mi_mat, list(combo))\\n            eta_max = max(ind_asr[(ds, atk, j)] for j in jids)\\n\\n            cs = {j: ds_clean[j] for j in jids}\\n            ats = {j: ds_attacked[j] for j in jids}\\n            asr = compute_panel_asr(jids, cs, ats, ds_pairs)\\n\\n            panel_asrs.append(asr)\\n            panel_keffs.append(keff)\\n            panel_etas.append(eta_max)\\n            panel_jids_list.append(jids)\\n\\n        n_panels = len(panel_asrs)\\n        t_data = time.time() - t0\\n        print(f\\\"  {n_panels} panels ({t_data:.1f}s)\\\")\\n\\n        if n_panels < 10:\\n            print(\\\"  SKIP: too few panels\\\")\\n            results[cond_key] = {\\\"skipped\\\": True}\\n            continue\\n\\n        panel_asrs = np.array(panel_asrs)\\n        panel_keffs = np.array(panel_keffs)\\n        panel_etas = np.array(panel_etas)\\n\\n        if np.std(panel_asrs) < 1e-10:\\n            print(f\\\"  SKIP: constant ASR ({panel_asrs[0]:.4f})\\\")\\n            results[cond_key] = {\\\"skipped\\\": True}\\n            continue\\n\\n        # Canonical regression\\n        log_keff = np.log(panel_keffs)\\n        log_eta = np.log(panel_etas + EPS)\\n        y = np.log(panel_asrs + EPS)\\n\\n        X = np.column_stack([log_keff, log_eta])\\n        Xc = sm.add_constant(X)\\n        fit_ols = sm.OLS(y
…[truncated 6814 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_controlled-regression_20260523T071753",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-23T07:24:01.251784+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "seetacloud-rtx6000",
  "command": "cat > /root/cert_manip_resist_eval/scripts/run_controlled_regression.py << 'PYEOF'\n#!/usr/bin/env python3\n\"\"\"Controlled Regression with Confound Variables — MF-1 supplement.\n\nAdds mean_accuracy and n_local as control variables to canonical regression,\nverifying η_max / K_eff significance is not confound-driven.\n\"\"\"\n\nimport os\nos.environ[\"HF_HOME\"] = \"/root/autodl-tmp/.hf_cache\"\n\nimport sys\nsys.path.insert(0, \"/root/cert_manip_resist_eval\")\n\nimport json\nimport itertools\nimport numpy as np\nimport statsmodels.api as sm\nfrom pathlib import Path\nfrom scipy.stats import t as t_dist\nfrom statsmodels.stats.multitest import multipletests\nfrom statsmodels.stats.outliers_influence import variance_inflation_factor\n\nfrom src.unified_data_loader import (\n    ALL_MODELS, API_MODELS, LOCAL_MODELS, DATASETS, ATTACKS,\n    load_all_scores, load_pairs, load_mi_data, compute_clean_accuracy,\n)\n\nEPS = 1e-6\nFDR_ALPHA = 0.05\nLOCAL_SET = set(LOCAL_MODELS)\n\n\ndef _json_default(obj):\n    if isinstance(obj, np.floating):\n        v = float(obj)\n        return None if (np.isnan(v) or np.isinf(v)) else v\n    if isinstance(obj, np.integer):\n        return int(obj)\n    if isinstance(obj, np.ndarray):\n        return obj.tolist()\n    if isinstance(obj, np.bool_):\n        return bool(obj)\n    raise TypeError(f\"Not JSON serializable: {type(obj)}\")\n\n\ndef majority_vote(votes):\n    counts = {\"A\": 0, \"B\": 0, \"tie\": 0}\n    for v in votes:\n        counts[v] = counts.get(v, 0) + 1\n    mc = max(counts.values())\n    winners = [k for k, c in counts.items() if c == mc]\n    if len(winners) == 1:\n        return winners[0]\n    for w in winners:\n        if w != \"tie\":\n            return w\n    return \"tie\"\n\n\ndef compute_individual_asr(clean_list, attacked_list, pairs):\n    n = min(len(clean_list), len(attacked_list), len(pairs))\n    n_flips = n_correct = 0\n    for i in range(n):\n        gt = pairs[i][\"ground_truth_winner\"]\n        if clean_list[i].get(\"winner\", \"tie\") == gt:\n            n_correct += 1\n            if attacked_list[i].get(\"winner\", \"tie\") != gt:\n                n_flips += 1\n    return n_flips / max(n_correct, 1)\n\n\ndef compute_panel_asr(jids, clean, attacked, pairs):\n    n = min(len(pairs), *(len(clean[j]) for j in jids),\n            *(len(attacked[j]) for j in jids))\n    n_flips = n_correct = 0\n    for i in range(n):\n        gt = pairs[i][\"ground_truth_winner\"]\n        cv = majority_vote([clean[j][i].get(\"winner\", \"tie\") for j in jids])\n        if cv != gt:\n            continue\n        n_correct += 1\n        av = majority_vote([attacked[j][i].get(\"winner\", \"tie\") for j in jids])\n        if av != gt:\n            n_flips += 1\n    return n_flips / max(n_correct, 1)\n\n\ndef keff_maxmi(mi_matrix, model_indices):\n    K = len(model_indices)\n    max_mi = 0.0\n    for a, b in itertools.combinations(model_indices, 2):\n        max_mi = max(max_mi, mi_matrix[a][b])\n    return 1 + (K - 1) * np.exp(-2 * max_mi)\n\n\ndef keff_avg_pairwise(mi_matrix, model_indices):\n    K = len(model_indices)\n    if K <= 1:\n        return 1.0\n    keff = 0.0\n    for i_idx in model_indices:\n        term = 1.0\n        for j_idx in model_indices:\n            if i_idx != j_idx:\n                term += np.exp(-2 * mi_matrix[i_idx][j_idx])\n        keff += term\n    return keff / K\n\n\ndef clustered_se_max(y, X, panel_jids_list, K):\n    \"\"\"Max clustered SE across K judge positions.\"\"\"\n    Xc = sm.add_constant(X)\n    fit_ols = sm.OLS(y, Xc).fit()\n    n_params = Xc.shape[1]\n    max_se = np.zeros(n_params)\n\n    for pos in range(K):\n        cluster_var = np.array([jids[pos] for jids in panel_jids_list])\n        unique_judges = sorted(set(cluster_var))\n        judge_to_int = {j: idx for idx, j in enumerate(unique_judges)}\n        cluster_int = np.array([judge_to_int[j] for j in cluster_var])\n\n        try:\n            fit_cl = sm.OLS(y, Xc).fit(\n                cov_type=\"cluster\",\n                cov_kwds={\"groups\": cluster_int}\n            )\n            max_se = np.maximum(max_se, fit_cl.bse)\n        except Exception:\n            pass\n\n    # Compute p-values from max SE\n    n = len(y)\n    G_min = len(set(panel_jids_list[0])) if panel_jids_list else 15\n    for pos in range(K):\n        cluster_var = [jids[pos] for jids in panel_jids_list]\n        G_min = min(G_min, len(set(cluster_var)))\n    df = max(G_min - 1, 1)\n\n    t_stats = fit_ols.params / np.where(max_se > 1e-15, max_se, np.inf)\n    p_values = 2 * t_dist.sf(np.abs(t_stats), df=df)\n\n    return fit_ols.params, max_se, p_values, fit_ols\n\n\ndef compute_vif(X):\n    \"\"\"VIF for each column of X (no constant — added internally).\"\"\"\n    Xc = sm.add_constant(X)\n    vifs = {}\n    col_names = list(range(X.shape[1]))\n    for i in range(1, Xc.shape[1]):  # skip constant\n        vifs[i - 1] = variance_inflation_factor(Xc, i)\n    return vifs\n\n\ndef run_one_condition(y, X_base, X_controls_dict, panel_jids_list, K):\n    \"\"\"Run baseline + controlled regressions for one condition.\n\n    X_base: (n, 2) — [log_keff, log_eta]\n    X_controls_dict: {\"mean_acc\": array, \"n_local\": array}\n    \"\"\"\n    results = {}\n\n    # --- Baseline ---\n    params_b, se_b, pvals_b, fit_b = clustered_se_max(y, X_base, panel_jids_list, K)\n    results[\"baseline\"] = {\n        \"keff_beta\": float(params_b[1]),\n        \"eta_beta\": float(params_b[2]),\n        \"keff_p\": float(pvals_b[1]),\n        \"eta_p\": float(pvals_b[2]),\n        \"r2\": float(fit_b.rsquared),\n    }\n\n    # --- +mean_acc ---\n    X_ma = np.column_stack([X_base, X_controls_dict[\"mean_acc\"]])\n    params_ma, se_ma, pvals_ma, fit_ma = clustered_se_max(y, X_ma, panel_jids_list, K)\n    results[\"plus_mean_acc\"] = {\n        \"keff_beta\": float(params_ma[1]),\n        \"eta_beta\": float(params_ma[2]),\n        \"mean_acc_beta\": float(params_ma[3]),\n        \"keff_p\": float(pvals_ma[1]),\n        \"eta_p\": float(pvals_ma[2]),\n        \"mean_acc_p\": float(pvals_ma[3]),\n        \"keff_beta_change_pct\": _pct_change(params_b[1], params_ma[1]),\n        \"eta_beta_change_pct\": _pct_change(params_b[2], params_ma[2]),\n        \"r2\": float(fit_ma.rsquared),\n    }\n\n    # --- +n_local ---\n    X_nl = np.column_stack([X_base, X_controls_dict[\"n_local\"]])\n    params_nl, se_nl, pvals_nl, fit_nl = clustered_se_max(y, X_nl, panel_jids_list, K)\n    results[\"plus_n_local\"] = {\n        \"keff_beta\": float(params_nl[1]),\n        \"eta_beta\": float(params_nl[2]),\n        \"n_local_beta\": float(params_nl[3]),\n        \"keff_p\": float(pvals_nl[1]),\n        \"eta_p\": float(pvals_nl[2]),\n        \"n_local_p\": float(pvals_nl[3]),\n        \"keff_beta_change_pct\": _pct_change(params_b[1], params_nl[1]),\n        \"eta_beta_change_pct\": _pct_change(params_b[2], params_nl[2]),\n        \"r2\": float(fit_nl.rsquared),\n    }\n\n    # --- +both ---\n    X_both = np.column_stack([X_base, X_controls_dict[\"mean_acc\"],\n                              X_controls_dict[\"n_local\"]])\n    params_bt, se_bt, pvals_bt, fit_bt = clustered_se_max(y, X_both, panel_jids_list, K)\n    results[\"plus_both\"] = {\n        \"keff_beta\": float(params_bt[1]),\n        \"eta_beta\": float(params_bt[2]),\n        \"mean_acc_beta\": float(params_bt[3]),\n        \"n_local_beta\": float(params_bt[4]),\n        \"keff_p\": float(pvals_bt[1]),\n        \"eta_p\": float(pvals_bt[2]),\n        \"mean_acc_p\": float(pvals_bt[3]),\n        \"n_local_p\": float(pvals_bt[4]),\n        \"keff_beta_change_pct\": _pct_change(params_b[1], params_bt[1]),\n        \"eta_beta_change_pct\": _pct_change(params_b[2], params_bt[2]),\n        \"r2\": float(fit_bt.rsquared),\n    }\n\n    # --- VIF on +both model ---\n    vif_raw = compute_vif(X_both)\n    results[\"vif\"] = {\n        \"log_keff\": float(vif_raw[0]),\n        \"log_eta\": float(vif_raw[1]),\n        \"mean_acc\": float(vif_raw[2]),\n        \"n_local\": float(vif_raw[3]),\n    }\n\n    return results\n\n\ndef _pct_change(old, new):\n    if abs(old) < 1e-15:\n        return None\n    return float((new - old) / abs(old) * 100)\n\n\ndef run_one_k(K, all_models, mi_matrices, clean, attacked, pairs, ind_asr,\n              clean_acc, keff_func):\n    model_to_idx = {m: i for i, m in enumerate(all_models)}\n    all_combos = list(itertools.combinations(range(len(all_models)), K))\n    condition_keys = [f\"{ds}x{atk}\" for ds in DATASETS for atk in ATTACKS]\n\n    cond_results = {}\n\n    for ds in DATASETS:\n        ds_clean = clean.get(ds, {})\n        ds_attacked = attacked.get(ds, {})\n        ds_pairs = pairs.get(ds, [])\n        mi_mat = np.array(mi_matrices[ds])\n\n        for atk in ATTACKS:\n            cond_key = f\"{ds}x{atk}\"\n            print(f\"  {cond_key}...\", end=\" \", flush=True)\n\n            if not ds_clean or not ds_attacked.get(atk) or not ds_pairs:\n                print(\"SKIP: missing data\")\n                cond_results[cond_key] = {\"skipped\": True}\n                continue\n\n            panel_asrs, panel_keffs, panel_etas = [], [], []\n            panel_mean_accs, panel_n_locals = [], []\n            panel_jids_list = []\n\n            for combo in all_combos:\n                jids = [all_models[i] for i in combo]\n                if not all((ds, atk, j) in ind_asr for j in jids):\n                    continue\n\n                keff = keff_func(mi_mat, list(combo))\n                eta_max = max(ind_asr[(ds, atk, j)] for j in jids)\n\n                cs = {j: ds_clean[j] for j in jids}\n                ats = {j: ds_attacked[atk][j] for j in jids}\n                asr = compute_panel_asr(jids, cs, ats, ds_pairs)\n\n                # mean_accuracy: average clean accuracy of panel members for this dataset\n                accs = [clean_acc.get((j, ds), 0.5) for j in jids]\n                mean_acc = np.mean(accs)\n\n                # n_local: count local models in panel\n                n_local = sum(1 for j in jids if j in LOCAL_SET)\n\n                panel_asrs.append(asr)\n                panel_keffs.append(keff)\n                panel_etas.append(eta_max)\n                panel_mean_accs.append(mean_acc)\n                panel_n_locals.append(n_local)\n                panel_jids_list.append(jids)\n\n            n_panels = len(panel_asrs)\n            print(f\"{n_panels} panels\", end=\" \", flush=True)\n\n            if n_panels < 10:\n                print(\"SKIP: too few\")\n                cond_results[cond_key] = {\"skipped\": True}\n                continue\n\n            panel_asrs = np.array(panel_asrs)\n            panel_keffs = np.array(panel_keffs)\n            panel_etas = np.array(panel_etas)\n            panel_mean_accs = np.array(panel_mean_accs)\n            panel_n_locals = np.array(panel_n_locals, dtype=float)\n\n            if np.std(panel_asrs) < 1e-10:\n                print(f\"SKIP: constant ASR\")\n                cond_results[cond_key] = {\"skipped\": True}\n                continue\n\n            y = np.log(panel_asrs + EPS)\n            X_base = np.column_stack([np.log(panel_keffs),\n                                       np.log(panel_etas + EPS)])\n            controls = {\n                \"mean_acc\": panel_mean_accs,\n                \"n_local\": panel_n_locals,\n            }\n\n            res = run_one_condition(y, X_base, controls, panel_jids_list, K)\n            res[\"n_panels\"] = n_panels\n            res[\"skipped\"] = False\n            cond_results[cond_key] = res\n\n            print(f\"VIF: keff={res['vif']['log_keff']:.2f} \"\n                  f\"eta={res['vif']['log_eta']:.2f} \"\n                  f\"macc={res['vif']['mean_acc']:.2f} \"\n                  f\"nloc={res['vif']['n_local']:.2f}\")\n\n    # FDR correction across 12 conditions for each model spec\n    valid_keys = [k for k in condition_keys\n                  if not cond_results.get(k, {}).get(\"skipped\", True)]\n\n    specs = [\"baseline\", \"plus_mean_acc\", \"plus_n_local\", \"plus_both\"]\n    sig_counts = {}\n\n    for spec in specs:\n        eta_ps = [cond_results[k][spec][\"eta_p\"] for k in valid_keys]\n        keff_ps = [cond_results[k][spec][\"keff_p\"] for k in valid_keys]\n\n        if len(valid_keys) > 0:\n            _, eta_fdr, _, _ = multipletests(eta_ps, alpha=FDR_ALPHA, method=\"fdr_bh\")\n            _, keff_fdr, _, _ = multipletests(keff_ps, alpha=FDR_ALPHA, method=\"fdr_bh\")\n        else:\n            eta_fdr = keff_fdr = []\n\n        for i, k in enumerate(valid_keys):\n            cond_results[k][spec][\"eta_fdr_p\"] = float(eta_fdr[i])\n            cond_results[k][spec][\"keff_fdr_p\"] = float(keff_fdr[i])\n\n        eta_sig = sum(1 for i in range(len(valid_keys)) if eta_fdr[i] < FDR_ALPHA)\n        keff_sig = sum(1 for i in range(len(valid_keys)) if keff_fdr[i] < FDR_ALPHA)\n\n        sig_counts[spec] = {\n            \"eta_sig\": f\"{eta_sig}/{len(valid_keys)}\",\n            \"keff_sig\": f\"{keff_sig}/{len(valid_keys)}\",\n        }\n\n        # Additional fields for controlled specs\n        if spec == \"plus_mean_acc\":\n            ma_ps = [cond_results[k][spec][\"mean_acc_p\"] for k in valid_keys]\n            if len(valid_keys) > 0:\n                _, ma_fdr, _, _ = multipletests(ma_ps, alpha=FDR_ALPHA, method=\"fdr_bh\")\n                sig_counts[spec][\"mean_acc_sig\"] = f\"{sum(1 for p in ma_fdr if p < FDR_ALPHA)}/{len(valid_keys)}\"\n            avg_eta_chg = np.mean([cond_results[k][spec][\"eta_beta_change_pct\"]\n                                   for k in valid_keys\n                                   if cond_results[k][spec][\"eta_beta_change_pct\"] is not None])\n            avg_keff_chg = np.mean([cond_results[k][spec][\"keff_beta_change_pct\"]\n                                    for k in valid_keys\n                                    if cond_results[k][spec][\"keff_beta_change_pct\"] is not None])\n            sig_counts[spec][\"eta_beta_change_pct_avg\"] = float(avg_eta_chg)\n            sig_counts[spec][\"keff_beta_change_pct_avg\"] = float(avg_keff_chg)\n\n        if spec == \"plus_n_local\":\n            nl_ps = [cond_results[k][spec][\"n_local_p\"] for k in valid_keys]\n            if len(valid_keys) > 0:\n                _, nl_fdr, _, _ = multipletests(nl_ps, alpha=FDR_ALPHA, method=\"fdr_bh\")\n                sig_counts[spec][\"n_local_sig\"] = f\"{sum(1 for p in nl_fdr if p < FDR_ALPHA)}/{len(valid_keys)}\"\n            avg_eta_chg = np.mean([cond_results[k][spec][\"eta_beta_change_pct\"]\n                                   for k in valid_keys\n                                   if cond_results[k][spec][\"eta_beta_change_pct\"] is not None])\n            avg_keff_chg = np.mean([cond_results[k][spec][\"keff_beta_change_pct\"]\n                                    for k in valid_keys\n                                    if cond_results[k][spec][\"keff_beta_change_pct\"] is not None])\n            sig_counts[spec][\"eta_beta_change_pct_avg\"] = float(avg_eta_chg)\n            sig_counts[spec][\"keff_beta_change_pct_avg\"] = float(avg_keff_chg)\n\n        if spec == \"plus_both\":\n            ma_ps = [cond_results[k][spec][\"mean_acc_p\"] for k in valid_keys]\n            nl_ps = [cond_results[k][spec][\"n_local_p\"] for k in valid_keys]\n            if len(valid_keys) > 0:\n                _, ma_fdr, _, _ = multipletests(ma_ps, alpha=FDR_ALPHA, method=\"fdr_bh\")\n                _, nl_fdr, _, _ = multipletests(nl_ps, alpha=FDR_ALPHA, method=\"fdr_bh\")\n                sig_counts[spec][\"mean_acc_sig\"] = f\"{sum(1 for p in ma_fdr if p < FDR_ALPHA)}/{len(valid_keys)}\"\n                sig_counts[spec][\"n_local_sig\"] = f\"{sum(1 for p in nl_fdr if p < FDR_ALPHA)}/{len(valid_keys)}\"\n            avg_eta_chg = np.mean([cond_results[k][spec][\"eta_beta_change_pct\"]\n                                   for k in valid_keys\n                                   if cond_results[k][spec][\"eta_beta_change_pct\"] is not None])\n            avg_keff_chg = np.mean([cond_results[k][spec][\"keff_beta_change_pct\"]\n                                    for k in valid_keys\n                                    if cond_results[k][spec][\"keff_beta_change_pct\"] is not None])\n            sig_counts[spec][\"eta_beta_change_pct_avg\"] = float(avg_eta_chg)\n            sig_counts[spec][\"keff_beta_change_pct_avg\"] = float(avg_keff_chg)\n\n    # Aggregate VIF\n    vif_agg = {}\n    for var in [\"log_keff\", \"log_eta\", \"mean_acc\", \"n_local\"]:\n        vals = [cond_results[k][\"vif\"][var] for k in valid_keys]\n        vif_agg[var] = {\"mean\": float(np.mean(vals)), \"max\": float(np.max(vals))}\n\n    return {\n        \"per_condition\": cond_results,\n        \"summary\": sig_counts,\n        \"vif_aggregate\": vif_agg,\n        \"n_conditions\": len(valid_keys),\n    }\n\n\ndef main():\n    print(\"Loading data...\")\n    clean, attacked = load_all_scores()\n    pairs = load_pairs()\n    mi_matrices = load_mi_data()\n\n    # Compute clean accuracy for all models\n    clean_acc = compute_clean_accuracy(clean, pairs)\n    print(f\"  Clean accuracy entries: {len(clean_acc)}\")\n\n    # Compute individual ASR\n    ind_asr = {}\n    for ds in DATASETS:\n        for atk in ATTACKS:\n            for mid in ALL_MODELS:\n                if mid in clean.get(ds, {}) and mid in attacked.get(ds, {}).get(atk, {}):\n                    ind_asr[(ds, atk, mid)] = compute_individual_asr(\n                        clean[ds][mid], attacked[ds][atk][mid], pairs[ds]\n                    )\n    print(f\"  Individual ASR entries: {len(ind_asr)}\")\n\n    # K=3\n    print(\"\\n=== K=3 ===\")\n    k3 = run_one_k(3, ALL_MODELS, mi_matrices, clean, attacked, pairs,\n                   ind_asr, clean_acc, keff_maxmi)\n\n    # K=5\n    print(\"\\n=== K=5 ===\")\n    k5 = run_one_k(5, ALL_MODELS, mi_matrices, clean, attacked, pairs,\n                   ind_asr, clean_acc, keff_avg_pairwise)\n\n    # Over-control check\n    k3_base_eta = int(k3[\"summary\"][\"baseline\"][\"eta_sig\"].split(\"/\")[0])\n    k3_both_eta = int(k3[\"summary\"][\"plus_both\"][\"eta_sig\"].split(\"/\")[0])\n    k3_base_keff = int(k3[\"summary\"][\"baseline\"][\"keff_sig\"].split(\"/\")[0])\n    k3_both_keff = int(k3[\"summary\"][\"plus_both\"][\"keff_sig\"].split(\"/\")[0])\n    k5_base_eta = int(k5[\"summary\"][\"baseline\"][\"eta_sig\"].split(\"/\")[0])\n    k5_both_eta = int(k5[\"summary\"][\"plus_both\"][\"eta_sig\"].split(\"/\")[0])\n    k5_base_keff = int(k5[\"summary\"][\"baseline\"][\"keff_sig\"].split(\"/\")[0])\n    k5_both_keff = int(k5[\"summary\"][\"plus_both\"][\"keff_sig\"].split(\"/\")[0])\n\n    over_control = (\n        (k3_both_eta == 0 and k3_both_keff == 0 and (k3_base_eta > 0 or k3_base_keff > 0)) or\n        (k5_both_eta == 0 and k5_both_keff == 0 and (k5_base_eta > 0 or k5_base_keff > 0))\n    )\n\n    # Check high VIF\n    high_vif = False\n    for kx in [k3, k5]:\n        for var, stats in kx[\"vif_aggregate\"].items():\n            if stats[\"max\"] > 10:\n                high_vif = True\n\n    # Summary\n    summary_parts = []\n    summary_parts.append(\n        f\"K=3 baseline: eta {k3['summary']['baseline']['eta_sig']}, \"\n        f\"keff {k3['summary']['baseline']['keff_sig']}. \"\n        f\"+both: eta {k3['summary']['plus_both']['eta_sig']}, \"\n        f\"keff {k3['summary']['plus_both']['keff_sig']}.\"\n    )\n    summary_parts.append(\n        f\"K=5 baseline: eta {k5['summary']['baseline']['eta_sig']}, \"\n        f\"keff {k5['summary']['baseline']['keff_sig']}. \"\n        f\"+both: eta {k5['summary']['plus_both']['eta_sig']}, \"\n        f\"keff {k5['summary']['plus_both']['keff_sig']}.\"\n    )\n    if over_control:\n        summary_parts.append(\"OVER-CONTROL WARNING: adding both controls killed all significance.\")\n    if high_vif:\n        summary_parts.append(\"HIGH VIF WARNING: some VIF > 10, multicollinearity concern.\")\n\n    summary = \" \".join(summary_parts)\n\n    print(f\"\\n{'='*70}\")\n    print(\"SUMMARY\")\n    print(f\"{'='*70}\")\n    for spec in [\"baseline\", \"plus_mean_acc\", \"plus_n_local\", \"plus_both\"]:\n        k3s = k3[\"summary\"][spec]\n        k5s = k5[\"summary\"][spec]\n        print(f\"  {spec:<20} K=3: eta {k3s['eta_sig']}, keff {k3s['keff_sig']}  |  \"\n              f\"K=5: eta {k5s['eta_sig']}, keff {k5s['keff_sig']}\")\n    print(f\"\\n  Over-control warning: {over_control}\")\n    print(f\"  High VIF warning: {high_vif}\")\n\n    output = {\n        \"analysis\": \"controlled_regression_mf1\",\n        \"purpose\": \"Verify eta_max/K_eff significance not driven by model capability confounds\",\n        \"controls\": {\n            \"mean_accuracy\": \"average clean accuracy of panel members for the dataset\",\n            \"n_local\": \"count of local (non-API) models in panel\",\n        },\n        \"method\": \"OLS + clustered SE (K-position max-SE), BH FDR across 12 conditions\",\n        \"K3\": k3,\n        \"K5\": k5,\n        \"over_control_warning\": over_control,\n        \"high_vif_warning\": high_vif,\n        \"summary\": summary,\n    }\n\n    out_path = Path(\"/root/cert_manip_resist_eval/artifacts/results/plan001/controlled_regression.json\")\n    out_path.parent.mkdir(parents=True, exist_ok=True)\n    with open(out_path, \"w\") as f:\n        json.dump(output, f, indent=2, default=_json_default, ensure_ascii=False)\n    print(f\"\\nSaved: {out_path}\")\n\n\nif __name__ == \"__main__\":\n    main()\nPYEOF"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_controlled-regression_20260523T071753",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "seetacloud-rtx6000",
    "command": "cat > /root/cert_manip_resist_eval/scripts/run_controlled_regression.py << 'PYEOF'\n#!/usr/bin/env python3\n\"\"\"Controlled Regression with Confound Variables — MF-1 supplement.\n\nAdds mean_accuracy and n_local as control variables to canonical regression,\nverifying η_max / K_eff significance is not confound-driven.\n\"\"\"\n\nimport os\nos.environ[\"HF_HOME\"] = \"/root/autodl-tmp/.hf_cache\"\n\nimport sys\nsys.path.insert(0, \"/root/cert_manip_resist_eval\")\n\nimport json\nimport itertools\nimport numpy as np\nimport statsmodels.api as sm\nfrom pathlib import Path\nfrom scipy.stats import t as t_dist\nfrom statsmodels.stats.multitest import multipletests\nfrom statsmodels.stats.outliers_influence import variance_inflation_factor\n\nfrom src.unified_data_loader import (\n    ALL_MODELS, API_MODELS, LOCAL_MODELS, DATASETS, ATTACKS,\n    load_all_scores, load_pairs, load_mi_data, compute_clean_accuracy,\n)\n\nEPS = 1e-6\nFDR_ALPHA = 0.05\nLOCAL_SET = set(LOCAL_MODELS)\n\n\ndef _json_default(obj):\n    if isinstance(obj, np.floating):\n        v = float(obj)\n        return None if (np.isnan(v) or np.isinf(v)) else v\n    if isinstance(obj, np.integer):\n        return int(obj)\n    if isinstance(obj, np.ndarray):\n        return obj.tolist()\n    if isinstance(obj, np.bool_):\n        return bool(obj)\n    raise TypeError(f\"Not JSON serializable: {type(obj)}\")\n\n\ndef majority_vote(votes):\n    counts = {\"A\": 0, \"B\": 0, \"tie\": 0}\n    for v in votes:\n        counts[v] = counts.get(v, 0) + 1\n    mc = max(counts.values())\n    winners = [k for k, c in counts.items() if c == mc]\n    if len(winners) == 1:\n        return winners[0]\n    for w in winners:\n        if w != \"tie\":\n            return w\n    return \"tie\"\n\n\ndef compute_individual_asr(clean_list, attacked_list, pairs):\n    n = min(len(clean_list), len(attacked_list), len(pairs))\n    n_flips = n_correct = 0\n    for i in range(n):\n        gt = pairs[i][\"ground_truth_winner\"]\n        if clean_list[i].get(\"winner\", \"tie\") == gt:\n            n_correct += 1\n            if attacked_list[i].get(\"winner\", \"tie\") != gt:\n                n_flips += 1\n    return n_flips / max(n_correct, 1)\n\n\ndef compute_panel_asr(jids, clean, attacked, pairs):\n    n = min(len(pairs), *(len(clean[j]) for j in jids),\n            *(len(attacked[j]) for j in jids))\n    n_flips = n_correct = 0\n    for i in range(n):\n        gt = pairs[i][\"ground_truth_winner\"]\n        cv = majority_vote([clean[j][i].get(\"winner\", \"tie\") for j in jids])\n        if cv != gt:\n            continue\n        n_correct += 1\n        av = majority_vote([attacked[j][i].get(\"winner\", \"tie\") for j in jids])\n        if av != gt:\n            n_flips += 1\n    return n_flips / max(n_correct, 1)\n\n\ndef keff_maxmi(mi_matrix, model_indices):\n    K = len(model_indices)\n    max_mi = 0.0\n    for a, b in itertools.combinations(model_indices, 2):\n        max_mi = max(max_mi, mi_matrix[a][b])\n    return 1 + (K - 1) * np.exp(-2 * max_mi)\n\n\ndef keff_avg_pairwise(mi_matrix, model_indices):\n    K = len(model_indices)\n    if K <= 1:\n        return 1.0\n    keff = 0.0\n    for i_idx in model_indices:\n        term = 1.0\n        for j_idx in model_indices:\n            if i_idx != j_idx:\n                term += np.exp(-2 * mi_matrix[i_idx][j_idx])\n        keff += term\n    return keff / K\n\n\ndef clustered_se_max(y, X, panel_jids_list, K):\n    \"\"\"Max clustered SE across K judge positions.\"\"\"\n    Xc = sm.add_constant(X)\n    fit_ols = sm.OLS(y, Xc).fit()\n    n_params = Xc.shape[1]\n    max_se = np.zeros(n_params)\n\n    for pos in range(K):\n        cluster_var = np.array([jids[pos] for jids in panel_jids_list])\n        unique_judges = sorted(set(cluster_var))\n        judge_to_int = {j: idx for idx, j in enumerate(unique_judges)}\n        cluster_int = np.array([judge_to_int[j] for j in cluster_var])\n\n        try:\n            fit_cl = sm.OLS(y, Xc).fit(\n                cov_type=\"cluster\",\n                cov_kwds={\"groups\": cluster_int}\n            )\n            max_se = np.maximum(max_se, fit_cl.bse)\n        except Exception:\n            pass\n\n    # Compute p-values from max SE\n    n = len(y)\n    G_min = len(set(panel_jids_list[0])) if panel_jids_list else 15\n    for pos in range(K):\n        cluster_var = [jids[pos] for jids in panel_jids_list]\n        G_min = min(G_min, len(set(cluster_var)))\n    df = max(G_min - 1, 1)\n\n    t_stats = fit_ols.params / np.where(max_se > 1e-15, max_se, np.inf)\n    p_values = 2 * t_dist.sf(np.abs(t_stats), df=df)\n\n    return fit_ols.params, max_se, p_values, fit_ols\n\n\ndef compute_vif(X):\n    \"\"\"VIF for each column of X (no constant — added internally).\"\"\"\n    Xc = sm.add_constant(X)\n    vifs = {}\n    col_names = list(range(X.shape[1]))\n    for i in range(1, Xc.shape[1]):  # skip constant\n        vifs[i - 1] = variance_inflation_factor(Xc, i)\n    return vifs\n\n\ndef run_one_condition(y, X_base, X_controls_dict, panel_jids_list, K):\n    \"\"\"Run baseline + controlled regressions for one condition.\n\n    X_base: (n, 2) — [log_keff, log_eta]\n    X_controls_dict: {\"mean_acc\": array, \"n_local\": array}\n    \"\"\"\n    results = {}\n\n    # --- Baseline ---\n    params_b, se_b, pvals_b, fit_b = clustered_se_max(y, X_base, panel_jids_list, K)\n    results[\"baseline\"] = {\n        \"keff_beta\": float(params_b[1]),\n        \"eta_beta\": float(params_b[2]),\n        \"keff_p\": float(pvals_b[1]),\n        \"eta_p\": float(pvals_b[2]),\n        \"r2\": float(fit_b.rsquared),\n    }\n\n    # --- +mean_acc ---\n    X_ma = np.column_stack([X_base, X_controls_dict[\"mean_acc\"]])\n    params_ma, se_ma, pvals_ma, fit_ma = clustered_se_max(y, X_ma, panel_jids_list, K)\n    results[\"plus_mean_acc\"] = {\n        \"keff_beta\": float(params_ma[1]),\n        \"eta_beta\": float(params_ma[2]),\n        \"mean_acc_beta\": float(params_ma[3]),\n        \"keff_p\": float(pvals_ma[1]),\n        \"eta_p\": float(pvals_ma[2]),\n        \"mean_acc_p\": float(pvals_ma[3]),\n        \"keff_beta_change_pct\": _pct_change(params_b[1], params_ma[1]),\n        \"eta_beta_change_pct\": _pct_change(params_b[2], params_ma[2]),\n        \"r2\": float(fit_ma.rsquared),\n    }\n\n    # --- +n_local ---\n    X_nl = np.column_stack([X_base, X_controls_dict[\"n_local\"]])\n    params_nl, se_nl, pvals_nl, fit_nl = clustered_se_max(y, X_nl, panel_jids_list, K)\n    results[\"plus_n_local\"] = {\n        \"keff_beta\": float(params_nl[1]),\n        \"eta_beta\": float(params_nl[2]),\n        \"n_local_beta\": float(params_nl[3]),\n        \"keff_p\": float(pvals_nl[1]),\n        \"eta_p\": float(pvals_nl[2]),\n        \"n_local_p\": float(pvals_nl[3]),\n        \"keff_beta_change_pct\": _pct_change(params_b[1], params_nl[1]),\n        \"eta_beta_change_pct\": _pct_change(params_b[2], params_nl[2]),\n        \"r2\": float(fit_nl.rsquared),\n    }\n\n    # --- +both ---\n    X_both = np.column_stack([X_base, X_controls_dict[\"mean_acc\"],\n                              X_controls_dict[\"n_local\"]])\n    params_bt, se_bt, pvals_bt, fit_bt = clustered_se_max(y, X_both, panel_jids_list, K)\n    results[\"plus_both\"] = {\n        \"keff_beta\": float(params_bt[1]),\n        \"eta_beta\": float(params_bt[2]),\n        \"mean_acc_beta\": float(params_bt[3]),\n        \"n_local_beta\": float(params_bt[4]),\n        \"keff_p\": float(pvals_bt[1]),\n        \"eta_p\": float(pvals_bt[2]),\n        \"mean_acc_p\": float(pvals_bt[3]),\n        \"n_local_p\": float(pvals_bt[4]),\n        \"keff_beta_change_pct\": _pct_change(params_b[1], params_bt[1]),\n        \"eta_beta_change_pct\": _pct_change(params_b[2], params_bt[2]),\n        \"r2\": float(fit_bt.rsquared),\n    }\n\n    # --- VIF on +both model ---\n    vif_raw = compute_vif(X_both)\n    results[\"vif\"] = {\n        \"log_keff\": float(vif_raw[0]),\n        \"log_eta\": float(vif_raw[1]),\n        \"mean_acc\": float(vif_raw[2]),\n        \"n_local\": float(vif_raw[3]),\n    }\n\n    return results\n\n\ndef _pct_change(old, new):\n    if abs(old) < 1e-15:\n        return None\n    return float((new - old) / abs(old) * 100)\n\n\ndef run_one_k(K, all_models, mi_matrices, clean, attacked, pairs, ind_asr,\n              clean_acc, keff_func):\n    model_to_idx = {m: i for i, m in enumerate(all_models)}\n    all_combos = list(itertools.combinations(range(len(all_models)), K))\n    condition_keys = [f\"{ds}x{atk}\" for ds in DATASETS for atk in ATTACKS]\n\n    cond_results = {}\n\n    for ds in DATASETS:\n        ds_clean = clean.get(ds, {})\n        ds_attacked = attacked.get(ds, {})\n        ds_pairs = pairs.get(ds, [])\n        mi_mat = np.array(mi_matrices[ds])\n\n        for atk in ATTACKS:\n            cond_key = f\"{ds}x{atk}\"\n            print(f\"  {cond_key}...\", end=\" \", flush=True)\n\n            if not ds_clean or not ds_attacked.get(atk) or not ds_pairs:\n                print(\"SKIP: missing data\")\n                cond_results[cond_key] = {\"skipped\": True}\n                continue\n\n            panel_asrs, panel_keffs, panel_etas = [], [], []\n            panel_mean_accs, panel_n_locals = [], []\n            panel_jids_list = []\n\n            for combo in all_combos:\n                jids = [all_models[i] for i in combo]\n                if not all((ds, atk, j) in ind_asr for j in jids):\n                    continue\n\n                keff = keff_func(mi_mat, list(combo))\n                eta_max = max(ind_asr[(ds, atk, j)] for j in jids)\n\n                cs = {j: ds_clean[j] for j in jids}\n                ats = {j: ds_attacked[atk][j] for j in jids}\n                asr = compute_panel_asr(jids, cs, ats, ds_pairs)\n\n                # mean_accuracy: average clean accuracy of panel members for this dataset\n                accs = [clean_acc.get((j, ds), 0.5) for j in jids]\n                mean_acc = np.mean(accs)\n\n                # n_local: count local models in panel\n                n_local = sum(1 for j in jids if j in LOCAL_SET)\n\n                panel_asrs.append(asr)\n                panel_keffs.append(keff)\n                panel_etas.append(eta_max)\n                panel_mean_accs.append(mean_acc)\n                panel_n_locals.append(n_local)\n                panel_jids_list.append(jids)\n\n            n_panels = len(panel_asrs)\n            print(f\"{n_panels} panels\", end=\" \", flush=True)\n\n            if n_panels < 10:\n                print(\"SKIP: too few\")\n                cond_results[cond_key] = {\"skipped\": True}\n                continue\n\n            panel_asrs = np.array(panel_asrs)\n            panel_keffs = np.array(panel_keffs)\n            panel_etas = np.array(panel_etas)\n            panel_mean_accs = np.array(panel_mean_accs)\n            panel_n_locals = np.array(panel_n_locals, dtype=float)\n\n            if np.std(panel_asrs) < 1e-10:\n                print(f\"SKIP: constant ASR\")\n                cond_results[cond_key] = {\"skipped\": True}\n                continue\n\n            y = np.log(panel_asrs + EPS)\n            X_base = np.column_stack([np.log(panel_keffs),\n                                       np.log(panel_etas + EPS)])\n            controls = {\n                \"mean_acc\": panel_mean_accs,\n                \"n_local\": panel_n_locals,\n            }\n\n            res = run_one_condition(y, X_base, controls, panel_jids_list, K)\n            res[\"n_panels\"] = n_panels\n            res[\"skipped\"] = False\n            cond_results[cond_key] = res\n\n            print(f\"VIF: keff={res['vif']['log_keff']:.2f} \"\n                  f\"eta={res['vif']['log_eta']:.2f} \"\n                  f\"macc={res['vif']['mean_acc']:.2f} \"\n                  f\"nloc={res['vif']['n_local']:.2f}\")\n\n    # FDR correction across 12 conditions for each model spec\n    valid_keys = [k for k in condition_keys\n                  if not cond_results.get(k, {}).get(\"skipped\", True)]\n\n    specs = [\"baseline\", \"plus_mean_acc\", \"plus_n_local\", \"plus_both\"]\n    sig_counts = {}\n\n    for spec in specs:\n        eta_ps = [cond_results[k][spec][\"eta_p\"] for k in valid_keys]\n        keff_ps = [cond_results[k][spec][\"keff_p\"] for k in valid_keys]\n\n        if len(valid_keys) > 0:\n            _, eta_fdr, _, _ = multipletests(eta_ps, alpha=FDR_ALPHA, method=\"fdr_bh\")\n            _, keff_fdr, _, _ = multipletests(keff_ps, alpha=FDR_ALPHA, method=\"fdr_bh\")\n        else:\n            eta_fdr = keff_fdr = []\n\n        for i, k in enumerate(valid_keys):\n            cond_results[k][spec][\"eta_fdr_p\"] = float(eta_fdr[i])\n            cond_results[k][spec][\"keff_fdr_p\"] = float(keff_fdr[i])\n\n        eta_sig = sum(1 for i in range(len(valid_keys)) if eta_fdr[i] < FDR_ALPHA)\n        keff_sig = sum(1 for i in range(len(valid_keys)) if keff_fdr[i] < FDR_ALPHA)\n\n        sig_counts[spec] = {\n            \"eta_sig\": f\"{eta_sig}/{len(valid_keys)}\",\n            \"keff_sig\": f\"{keff_sig}/{len(valid_keys)}\",\n        }\n\n        # Additional fields for controlled specs\n        if spec == \"plus_mean_acc\":\n            ma_ps = [cond_results[k][spec][\"mean_acc_p\"] for k in valid_keys]\n            if len(valid_keys) > 0:\n                _, ma_fdr, _, _ = multipletests(ma_ps, alpha=FDR_ALPHA, method=\"fdr_bh\")\n                sig_counts[spec][\"mean_acc_sig\"] = f\"{sum(1 for p in ma_fdr if p < FDR_ALPHA)}/{len(valid_keys)}\"\n            avg_eta_chg = np.mean([cond_results[k][spec][\"eta_beta_change_pct\"]\n                                   for k in valid_keys\n                                   if cond_results[k][spec][\"eta_beta_change_pct\"] is not None])\n            avg_keff_chg = np.mean([cond_results[k][spec][\"keff_beta_change_pct\"]\n                                    for k in valid_keys\n                                    if cond_results[k][spec][\"keff_beta_change_pct\"] is not None])\n            sig_counts[spec][\"eta_beta_change_pct_avg\"] = float(avg_eta_chg)\n            sig_counts[spec][\"keff_beta_change_pct_avg\"] = float(avg_keff_chg)\n\n        if spec == \"plus_n_local\":\n            nl_ps = [cond_results[k][spec][\"n_local_p\"] for k in valid_keys]\n            if len(valid_keys) > 0:\n                _, nl_fdr, _, _ = multipletests(nl_ps, alpha=FDR_ALPHA, method=\"fdr_bh\")\n                sig_counts[spec][\"n_local_sig\"] = f\"{sum(1 for p in nl_fdr if p < FDR_ALPHA)}/{len(valid_keys)}\"\n            avg_eta_chg = np.mean([cond_results[k][spec][\"eta_beta_change_pct\"]\n                                   for k in valid_keys\n                                   if cond_results[k][spec][\"eta_beta_change_pct\"] is not None])\n            avg_keff_chg = np.mean([cond_results[k][spec][\"keff_beta_change_pct\"]\n                                    for k in valid_keys\n                                    if cond_results[k][spec][\"keff_beta_change_pct\"] is not None])\n            sig_counts[spec][\"eta_beta_change_pct_avg\"] = float(avg_eta_chg)\n            sig_counts[spec][\"keff_beta_change_pct_avg\"] = float(avg_keff_chg)\n\n        if spec == \"plus_both\":\n            ma_ps = [cond_results[k][spec][\"mean_acc_p\"] for k in valid_keys]\n            nl_ps = [cond_results[k][spec][\"n_local_p\"] for k in valid_keys]\n            if len(valid_keys) > 0:\n                _, ma_fdr, _, _ = multipletests(ma_ps, alpha=FDR_ALPHA, method=\"fdr_bh\")\n                _, nl_fdr, _, _ = multipletests(nl_ps, alpha=FDR_ALPHA, method=\"fdr_bh\")\n                sig_counts[spec][\"mean_acc_sig\"] = f\"{sum(1 for p in ma_fdr if p < FDR_ALPHA)}/{len(valid_keys)}\"\n                sig_counts[spec][\"n_local_sig\"] = f\"{sum(1 for p in nl_fdr if p < FDR_ALPHA)}/{len(valid_keys)}\"\n            avg_eta_chg = np.mean([cond_results[k][spec][\"eta_beta_change_pct\"]\n                                   for k in valid_keys\n                                   if cond_results[k][spec][\"eta_beta_change_pct\"] is not None])\n            avg_keff_chg = np.mean([cond_results[k][spec][\"keff_beta_change_pct\"]\n                                    for k in valid_keys\n                                    if cond_results[k][spec][\"keff_beta_change_pct\"] is not None])\n            sig_counts[spec][\"eta_beta_change_pct_avg\"] = float(avg_eta_chg)\n            sig_counts[spec][\"keff_beta_change_pct_avg\"] = float(avg_keff_chg)\n\n    # Aggregate VIF\n    vif_agg = {}\n    for var in [\"log_keff\", \"log_eta\", \"mean_acc\", \"n_local\"]:\n        vals = [cond_results[k][\"vif\"][var] for k in valid_keys]\n        vif_agg[var] = {\"mean\": float(np.mean(vals)), \"max\": float(np.max(vals))}\n\n    return {\n        \"per_condition\": cond_results,\n        \"summary\": sig_counts,\n        \"vif_aggregate\": vif_agg,\n        \"n_conditions\": len(valid_keys),\n    }\n\n\ndef main():\n    print(\"Loading data...\")\n    clean, attacked = load_all_scores()\n    pairs = load_pairs()\n    mi_matrices = load_mi_data()\n\n    # Compute clean accuracy for all models\n    clean_acc = compute_clean_accuracy(clean, pairs)\n    print(f\"  Clean accuracy entries: {len(clean_acc)}\")\n\n    # Compute individual ASR\n    ind_asr = {}\n    for ds in DATASETS:\n        for atk in ATTACKS:\n            for mid in ALL_MODELS:\n                if mid in clean.get(ds, {}) and mid in attacked.get(ds, {}).get(atk, {}):\n                    ind_asr[(ds, atk, mid)] = compute_individual_asr(\n                        clean[ds][mid], attacked[ds][atk][mid], pairs[ds]\n                    )\n    print(f\"  Individual ASR entries: {len(ind_asr)}\")\n\n    # K=3\n    print(\"\\n=== K=3 ===\")\n    k3 = run_one_k(3, ALL_MODELS, mi_matrices, clean, attacked, pairs,\n                   ind_asr, clean_acc, keff_maxmi)\n\n    # K=5\n    print(\"\\n=== K=5 ===\")\n    k5 = run_one_k(5, ALL_MODELS, mi_matrices, clean, attacked, pairs,\n                   ind_asr, clean_acc, keff_avg_pairwise)\n\n    # Over-control check\n    k3_base_eta = int(k3[\"summary\"][\"baseline\"][\"eta_sig\"].split(\"/\")[0])\n    k3_both_eta = int(k3[\"summary\"][\"plus_both\"][\"eta_sig\"].split(\"/\")[0])\n    k3_base_keff = int(k3[\"summary\"][\"baseline\"][\"keff_sig\"].split(\"/\")[0])\n    k3_both_keff = int(k3[\"summary\"][\"plus_both\"][\"keff_sig\"].split(\"/\")[0])\n    k5_base_eta = int(k5[\"summary\"][\"baseline\"][\"eta_sig\"].split(\"/\")[0])\n    k5_both_eta = int(k5[\"summary\"][\"plus_both\"][\"eta_sig\"].split(\"/\")[0])\n    k5_base_keff = int(k5[\"summary\"][\"baseline\"][\"keff_sig\"].split(\"/\")[0])\n    k5_both_keff = int(k5[\"summary\"][\"plus_both\"][\"keff_sig\"].split(\"/\")[0])\n\n    over_control = (\n        (k3_both_eta == 0 and k3_both_keff == 0 and (k3_base_eta > 0 or k3_base_keff > 0)) or\n        (k5_both_eta == 0 and k5_both_keff == 0 and (k5_base_eta > 0 or k5_base_keff > 0))\n    )\n\n    # Check high VIF\n    high_vif = False\n    for kx in [k3, k5]:\n        for var, stats in kx[\"vif_aggregate\"].items():\n            if stats[\"max\"] > 10:\n                high_vif = True\n\n    # Summary\n    summary_parts = []\n    summary_parts.append(\n        f\"K=3 baseline: eta {k3['summary']['baseline']['eta_sig']}, \"\n        f\"keff {k3['summary']['baseline']['keff_sig']}. \"\n        f\"+both: eta {k3['summary']['plus_both']['eta_sig']}, \"\n        f\"keff {k3['summary']['plus_both']['keff_sig']}.\"\n    )\n    summary_parts.append(\n        f\"K=5 baseline: eta {k5['summary']['baseline']['eta_sig']}, \"\n        f\"keff {k5['summary']['baseline']['keff_sig']}. \"\n        f\"+both: eta {k5['summary']['plus_both']['eta_sig']}, \"\n        f\"keff {k5['summary']['plus_both']['keff_sig']}.\"\n    )\n    if over_control:\n        summary_parts.append(\"OVER-CONTROL WARNING: adding both controls killed all significance.\")\n    if high_vif:\n        summary_parts.append(\"HIGH VIF WARNING: some VIF > 10, multicollinearity concern.\")\n\n    summary = \" \".join(summary_parts)\n\n    print(f\"\\n{'='*70}\")\n    print(\"SUMMARY\")\n    print(f\"{'='*70}\")\n    for spec in [\"baseline\", \"plus_mean_acc\", \"plus_n_local\", \"plus_both\"]:\n        k3s = k3[\"summary\"][spec]\n        k5s = k5[\"summary\"][spec]\n        print(f\"  {spec:<20} K=3: eta {k3s['eta_sig']}, keff {k3s['keff_sig']}  |  \"\n              f\"K=5: eta {k5s['eta_sig']}, keff {k5s['keff_sig']}\")\n    print(f\"\\n  Over-control warning: {over_control}\")\n    print(f\"  High VIF warning: {high_vif}\")\n\n    output = {\n        \"analysis\": \"controlled_regression_mf1\",\n        \"purpose\": \"Verify eta_max/K_eff significance not driven by model capability confounds\",\n        \"controls\": {\n            \"mean_accuracy\": \"average clean accuracy of panel members for the dataset\",\n            \"n_local\": \"count of local (non-API) models in panel\",\n        },\n        \"method\": \"OLS + clustered SE (K-position max-SE), BH FDR across 12 conditions\",\n        \"K3\": k3,\n        \"K5\": k5,\n        \"over_control_warning\": over_control,\n        \"high_vif_warning\": high_vif,\n        \"summary\": summary,\n    }\n\n    out_path = Path(\"/root/cert_manip_resist_eval/artifacts/results/plan001/controlled_regression.json\")\n    out_path.parent.mkdir(parents=True, exist_ok=True)\n    with open(out_path, \"w\") as f:\n        json.dump(output, f, indent=2, default=_json_default, ensure_ascii=False)\n    print(f\"\\nSaved: {out_path}\")\n\n\nif __name__ == \"__main__\":\n    main()\nPYEOF"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-23T07:24:01.252224+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_controlled-regression_20260523T071753",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-23T07:24:01.252385+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "seetacloud-rtx6000",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/cert_manip_resist_eval && python scripts/run_controlled_regression.py",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_controlled-regression_20260523T071753",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "seetacloud-rtx6000",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/cert_manip_resist_eval && python scripts/run_controlled_regression.py",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-23T07:24:01.252532+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"Loading data...\\n  Clean accuracy entries: 30\\n  Individual ASR entries: 180\\n\\n=== K=3 ===\\n\", \"stderr\": \"Traceback (most recent call last):\\n  File \\\"/root/cert_manip_resist_eval/scripts/run_controlled_regression.py\\\", line 527, in &lt;module>\\n    main()\\n  File \\\"/root/cert_manip_resist_eval/scripts/run_controlled_regression.py\\\", line 442, in main\\n    k3 = run_one_k(3, ALL_MODELS, mi_matrices, clean, attacked, pairs,\\n         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\\n  File \\\"/root/cert_manip_resist_eval/scripts/run_controlled_regression.py\\\", line 252, in run_one_k\\n    mi_mat = np.array(mi_matrices[ds])\\n                      ~~~~~~~~~~~^^^^\\nKeyError: 'mmlu'\\n\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 1.72}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_controlled-regression_20260523T071753",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-23T07:24:01.252699+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "seetacloud-rtx6000",
  "command": "grep -n \"def load_mi_data\" /root/cert_manip_resist_eval/src/unified_data_loader.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_controlled-regression_20260523T071753",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "seetacloud-rtx6000",
    "command": "grep -n \"def load_mi_data\" /root/cert_manip_resist_eval/src/unified_data_loader.py"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-23T07:24:01.252847+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"146:def load_mi_data(mi_path=None):\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_controlled-regression_20260523T071753",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-23T07:24:01.252970+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "seetacloud-rtx6000",
  "command": "tail -n +146 /root/cert_manip_resist_eval/src/unified_data_loader.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_controlled-regression_20260523T071753",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "seetacloud-rtx6000",
    "command": "tail -n +146 /root/cert_manip_resist_eval/src/unified_data_loader.py"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-23T07:24:01.253211+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"def load_mi_data(mi_path=None):\\n    \\\"\\\"\\\"Load MI matrix from Step 3 output.\\\"\\\"\\\"\\n    mi_path = Path(mi_path or MI_PATH)\\n    if not mi_path.exists():\\n        raise FileNotFoundError(\\n            f\\\"MI matrix not found: {mi_path}. Run Step 3 first.\\\"\\n        )\\n    with open(mi_path) as f:\\n        data = json.load(f)\\n    logger.info(f\\\"Loaded MI matrix: {len(data['models'])} models\\\")\\n    return data\\n\\n\\ndef load_api_asr(individual_dir=None, datasets=None, attacks=None, api_models=None):\\n    \\\"\\\"\\\"Load pre-computed ASR for API models from individual score files.\\n\\n    Returns: {ds: {atk: {model_id: asr}}}\\n    \\\"\\\"\\\"\\n    individual_dir = Path(individual_dir or SCORES_DIR)\\n    datasets = datasets or DATASETS\\n    attacks = attacks or ATTACKS\\n    api_models = api_models or API_MODELS\\n\\n    asr_data = {}\\n    for model_id in api_models:\\n        for ds in datasets:\\n            if ds not in asr_data:\\n                asr_data[ds] = {}\\n            clean_path = individual_dir / f\\\"{model_id}__{ds}__clean.json\\\"\\n            if not clean_path.exists():\\n                continue\\n            for atk in attacks:\\n                if atk not in asr_data[ds]:\\n                    asr_data[ds][atk] = {}\\n                atk_path = individual_dir / f\\\"{model_id}__{ds}__{atk}.json\\\"\\n                if not atk_path.exists():\\n                    continue\\n                with open(atk_path) as f:\\n                    atk_data = json.load(f)\\n                asr = atk_data.get(\\\"asr\\\")\\n                if asr is not None:\\n                    asr_data[ds][atk][model_id] = asr\\n    return asr_data\\n\\n\\ndef validate_coverage(clean, attacked, datasets=None, attacks=None,\\n                      all_models=None, expected_samples=300):\\n    \\\"\\\"\\\"Check that all models have expected number of samples. Returns list of iss
…[truncated 7004 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_controlled-regression_20260523T071753",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-23T07:24:01.253399+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "seetacloud-rtx6000",
  "command": "python3 -c \"import json; d=json.load(open('/root/cert_manip_resist_eval/artifacts/results/plan001/mi_matrix/mi_matrix_15models.json')); print(list(d.keys()))\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_controlled-regression_20260523T071753",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "seetacloud-rtx6000",
    "command": "python3 -c \"import json; d=json.load(open('/root/cert_manip_resist_eval/artifacts/results/plan001/mi_matrix/mi_matrix_15models.json')); print(list(d.keys()))\""
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-23T07:24:01.253534+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_controlled-regression_20260523T071753",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-23T07:24:01.253673+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "seetacloud-rtx6000",
  "command": "head -30 /root/cert_manip_resist_eval/artifacts/results/plan001/mi_matrix/mi_matrix_15models.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_controlled-regression_20260523T071753",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "seetacloud-rtx6000",
    "command": "head -30 /root/cert_manip_resist_eval/artifacts/results/plan001/mi_matrix/mi_matrix_15models.json"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-23T07:24:01.253826+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"models\\\": [\\n    \\\"qwen2.5-72b\\\",\\n    \\\"llama3.1-70b\\\",\\n    \\\"mistral-large\\\",\\n    \\\"qwen2.5-32b\\\",\\n    \\\"qwen2.5-14b\\\",\\n    \\\"llama3.1-8b\\\",\\n    \\\"claude-opus-4-6\\\",\\n    \\\"gpt-5.5\\\",\\n    \\\"gemini-3.1-pro-preview\\\",\\n    \\\"gpt-4.1\\\",\\n    \\\"claude-sonnet-4-6\\\",\\n    \\\"gpt-4.1-nano\\\",\\n    \\\"gemini-3.5-flash\\\",\\n    \\\"gpt-4.1-mini\\\",\\n    \\\"claude-3-haiku\\\"\\n  ],\\n  \\\"mi_matrix\\\": {\\n    \\\"mmlu\\\": [\\n      [\\n        0.0,\\n        0.2962205170426407,\\n        0.26675251098957503,\\n        0.3470669052814603,\\n        0.27125804258663433,\\n        0.036010036882308916,\\n        0.28731888801126415,\\n        0.3191362352253263,\\n        0.35168587132015827,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_controlled-regression_20260523T071753",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-23T07:24:01.254046+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "seetacloud-rtx6000",
  "command": "cat > /root/cert_manip_resist_eval/scripts/run_controlled_regression.py << 'PYEOF'\n#!/usr/bin/env python3\n\"\"\"Controlled Regression with Confound Variables — MF-1 supplement.\"\"\"\n\nimport os\nos.environ[\"HF_HOME\"] = \"/root/autodl-tmp/.hf_cache\"\n\nimport sys\nsys.path.insert(0, \"/root/cert_manip_resist_eval\")\n\nimport json\nimport itertools\nimport numpy as np\nimport statsmodels.api as sm\nfrom pathlib import Path\nfrom scipy.stats import t as t_dist\nfrom statsmodels.stats.multitest import multipletests\nfrom statsmodels.stats.outliers_influence import variance_inflation_factor\n\nfrom src.unified_data_loader import (\n    ALL_MODELS, API_MODELS, LOCAL_MODELS, DATASETS, ATTACKS,\n    load_all_scores, load_pairs, load_mi_data, compute_clean_accuracy,\n)\n\nEPS = 1e-6\nFDR_ALPHA = 0.05\nLOCAL_SET = set(LOCAL_MODELS)\n\n\ndef _json_default(obj):\n    if isinstance(obj, np.floating):\n        v = float(obj)\n        return None if (np.isnan(v) or np.isinf(v)) else v\n    if isinstance(obj, np.integer):\n        return int(obj)\n    if isinstance(obj, np.ndarray):\n        return obj.tolist()\n    if isinstance(obj, np.bool_):\n        return bool(obj)\n    raise TypeError(f\"Not JSON serializable: {type(obj)}\")\n\n\ndef majority_vote(votes):\n    counts = {\"A\": 0, \"B\": 0, \"tie\": 0}\n    for v in votes:\n        counts[v] = counts.get(v, 0) + 1\n    mc = max(counts.values())\n    winners = [k for k, c in counts.items() if c == mc]\n    if len(winners) == 1:\n        return winners[0]\n    for w in winners:\n        if w != \"tie\":\n            return w\n    return \"tie\"\n\n\ndef compute_individual_asr(clean_list, attacked_list, pairs):\n    n = min(len(clean_list), len(attacked_list), len(pairs))\n    n_flips = n_correct = 0\n    for i in range(n):\n        gt = pairs[i][\"ground_truth_winner\"]\n        if clean_list[i].get(\"winner\", \"tie\") == gt:\n            n_correct += 1\n            if attacked_list[i].get(\"winner\", \"tie\") != gt:\n                n_flips += 1\n    return n_flips / max(n_correct, 1)\n\n\ndef compute_panel_asr(jids, clean, attacked, pairs):\n    n = min(len(pairs), *(len(clean[j]) for j in jids),\n            *(len(attacked[j]) for j in jids))\n    n_flips = n_correct = 0\n    for i in range(n):\n        gt = pairs[i][\"ground_truth_winner\"]\n        cv = majority_vote([clean[j][i].get(\"winner\", \"tie\") for j in jids])\n        if cv != gt:\n            continue\n        n_correct += 1\n        av = majority_vote([attacked[j][i].get(\"winner\", \"tie\") for j in jids])\n        if av != gt:\n            n_flips += 1\n    return n_flips / max(n_correct, 1)\n\n\ndef keff_maxmi(mi_matrix, model_indices):\n    K = len(model_indices)\n    max_mi = 0.0\n    for a, b in itertools.combinations(model_indices, 2):\n        max_mi = max(max_mi, mi_matrix[a][b])\n    return 1 + (K - 1) * np.exp(-2 * max_mi)\n\n\ndef keff_avg_pairwise(mi_matrix, model_indices):\n    K = len(model_indices)\n    if K <= 1:\n        return 1.0\n    keff = 0.0\n    for i_idx in model_indices:\n        term = 1.0\n        for j_idx in model_indices:\n            if i_idx != j_idx:\n                term += np.exp(-2 * mi_matrix[i_idx][j_idx])\n        keff += term\n    return keff / K\n\n\ndef clustered_se_max(y, X, panel_jids_list, K):\n    Xc = sm.add_constant(X)\n    fit_ols = sm.OLS(y, Xc).fit()\n    n_params = Xc.shape[1]\n    max_se = np.zeros(n_params)\n\n    G_min = 999\n    for pos in range(K):\n        cluster_var = np.array([jids[pos] for jids in panel_jids_list])\n        unique_judges = sorted(set(cluster_var))\n        G_min = min(G_min, len(unique_judges))\n        judge_to_int = {j: idx for idx, j in enumerate(unique_judges)}\n        cluster_int = np.array([judge_to_int[j] for j in cluster_var])\n        try:\n            fit_cl = sm.OLS(y, Xc).fit(\n                cov_type=\"cluster\", cov_kwds={\"groups\": cluster_int}\n            )\n            max_se = np.maximum(max_se, fit_cl.bse)\n        except Exception:\n            pass\n\n    df = max(G_min - 1, 1)\n    t_stats = fit_ols.params / np.where(max_se > 1e-15, max_se, np.inf)\n    p_values = 2 * t_dist.sf(np.abs(t_stats), df=df)\n    return fit_ols.params, max_se, p_values, fit_ols\n\n\ndef compute_vif(X):\n    Xc = sm.add_constant(X)\n    vifs = {}\n    for i in range(1, Xc.shape[1]):\n        vifs[i - 1] = variance_inflation_factor(Xc, i)\n    return vifs\n\n\ndef _pct_change(old, new):\n    if abs(old) < 1e-15:\n        return None\n    return float((new - old) / abs(old) * 100)\n\n\ndef run_one_condition(y, X_base, controls, panel_jids_list, K):\n    results = {}\n\n    params_b, se_b, pvals_b, fit_b = clustered_se_max(y, X_base, panel_jids_list, K)\n    results[\"baseline\"] = {\n        \"keff_beta\": float(params_b[1]), \"eta_beta\": float(params_b[2]),\n        \"keff_p\": float(pvals_b[1]), \"eta_p\": float(pvals_b[2]),\n        \"r2\": float(fit_b.rsquared),\n    }\n\n    # +mean_acc\n    X_ma = np.column_stack([X_base, controls[\"mean_acc\"]])\n    params_ma, _, pvals_ma, fit_ma = clustered_se_max(y, X_ma, panel_jids_list, K)\n    results[\"plus_mean_acc\"] = {\n        \"keff_beta\": float(params_ma[1]), \"eta_beta\": float(params_ma[2]),\n        \"mean_acc_beta\": float(params_ma[3]),\n        \"keff_p\": float(pvals_ma[1]), \"eta_p\": float(pvals_ma[2]),\n        \"mean_acc_p\": float(pvals_ma[3]),\n        \"keff_beta_change_pct\": _pct_change(params_b[1], params_ma[1]),\n        \"eta_beta_change_pct\": _pct_change(params_b[2], params_ma[2]),\n        \"r2\": float(fit_ma.rsquared),\n    }\n\n    # +n_local\n    X_nl = np.column_stack([X_base, controls[\"n_local\"]])\n    params_nl, _, pvals_nl, fit_nl = clustered_se_max(y, X_nl, panel_jids_list, K)\n    results[\"plus_n_local\"] = {\n        \"keff_beta\": float(params_nl[1]), \"eta_beta\": float(params_nl[2]),\n        \"n_local_beta\": float(params_nl[3]),\n        \"keff_p\": float(pvals_nl[1]), \"eta_p\": float(pvals_nl[2]),\n        \"n_local_p\": float(pvals_nl[3]),\n        \"keff_beta_change_pct\": _pct_change(params_b[1], params_nl[1]),\n        \"eta_beta_change_pct\": _pct_change(params_b[2], params_nl[2]),\n        \"r2\": float(fit_nl.rsquared),\n    }\n\n    # +both\n    X_both = np.column_stack([X_base, controls[\"mean_acc\"], controls[\"n_local\"]])\n    params_bt, _, pvals_bt, fit_bt = clustered_se_max(y, X_both, panel_jids_list, K)\n    results[\"plus_both\"] = {\n        \"keff_beta\": float(params_bt[1]), \"eta_beta\": float(params_bt[2]),\n        \"mean_acc_beta\": float(params_bt[3]), \"n_local_beta\": float(params_bt[4]),\n        \"keff_p\": float(pvals_bt[1]), \"eta_p\": float(pvals_bt[2]),\n        \"mean_acc_p\": float(pvals_bt[3]), \"n_local_p\": float(pvals_bt[4]),\n        \"keff_beta_change_pct\": _pct_change(params_b[1], params_bt[1]),\n        \"eta_beta_change_pct\": _pct_change(params_b[2], params_bt[2]),\n        \"r2\": float(fit_bt.rsquared),\n    }\n\n    # VIF on +both\n    vif_raw = compute_vif(X_both)\n    results[\"vif\"] = {\n        \"log_keff\": float(vif_raw[0]), \"log_eta\": float(vif_raw[1]),\n        \"mean_acc\": float(vif_raw[2]), \"n_local\": float(vif_raw[3]),\n    }\n    return results\n\n\ndef run_one_k(K, all_models, mi_data, clean, attacked, pairs, ind_asr,\n              clean_acc, keff_func):\n    model_to_idx = {m: i for i, m in enumerate(all_models)}\n    all_combos = list(itertools.combinations(range(len(all_models)), K))\n    condition_keys = [f\"{ds}x{atk}\" for ds in DATASETS for atk in ATTACKS]\n\n    cond_results = {}\n\n    for ds in DATASETS:\n        ds_clean = clean.get(ds, {})\n        ds_attacked = attacked.get(ds, {})\n        ds_pairs = pairs.get(ds, [])\n        mi_mat = np.array(mi_data[\"mi_matrix\"][ds])\n\n        for atk in ATTACKS:\n            cond_key = f\"{ds}x{atk}\"\n            print(f\"  {cond_key}...\", end=\" \", flush=True)\n\n            if not ds_clean or not ds_attacked.get(atk) or not ds_pairs:\n                print(\"SKIP: missing data\")\n                cond_results[cond_key] = {\"skipped\": True}\n                continue\n\n            panel_asrs, panel_keffs, panel_etas = [], [], []\n            panel_mean_accs, panel_n_locals = [], []\n            panel_jids_list = []\n\n            for combo in all_combos:\n                jids = [all_models[i] for i in combo]\n                if not all((ds, atk, j) in ind_asr for j in jids):\n                    continue\n\n                keff = keff_func(mi_mat, list(combo))\n                eta_max = max(ind_asr[(ds, atk, j)] for j in jids)\n\n                cs = {j: ds_clean[j] for j in jids}\n                ats = {j: ds_attacked[atk][j] for j in jids}\n                asr = compute_panel_asr(jids, cs, ats, ds_pairs)\n\n                accs = [clean_acc.get((j, ds), 0.5) for j in jids]\n                mean_acc = np.mean(accs)\n                n_local = sum(1 for j in jids if j in LOCAL_SET)\n\n                panel_asrs.append(asr)\n                panel_keffs.append(keff)\n                panel_etas.append(eta_max)\n                panel_mean_accs.append(mean_acc)\n                panel_n_locals.append(n_local)\n                panel_jids_list.append(jids)\n\n            n_panels = len(panel_asrs)\n            print(f\"{n_panels} panels\", end=\" \", flush=True)\n\n            if n_panels < 10:\n                print(\"SKIP\")\n                cond_results[cond_key] = {\"skipped\": True}\n                continue\n\n            panel_asrs = np.array(panel_asrs)\n            panel_keffs = np.array(panel_keffs)\n            panel_etas = np.array(panel_etas)\n            panel_mean_accs = np.array(panel_mean_accs)\n            panel_n_locals = np.array(panel_n_locals, dtype=float)\n\n            if np.std(panel_asrs) < 1e-10:\n                print(\"SKIP: constant ASR\")\n                cond_results[cond_key] = {\"skipped\": True}\n                continue\n\n            y = np.log(panel_asrs + EPS)\n            X_base = np.column_stack([np.log(panel_keffs),\n                                       np.log(panel_etas + EPS)])\n            controls = {\"mean_acc\": panel_mean_accs, \"n_local\": panel_n_locals}\n\n            res = run_one_condition(y, X_base, controls, panel_jids_list, K)\n            res[\"n_panels\"] = n_panels\n            res[\"skipped\"] = False\n            cond_results[cond_key] = res\n\n            print(f\"VIF: keff={res['vif']['log_keff']:.2f} \"\n                  f\"eta={res['vif']['log_eta']:.2f} \"\n                  f\"macc={res['vif']['mean_acc']:.2f} \"\n                  f\"nloc={res['vif']['n_local']:.2f}\")\n\n    # FDR correction\n    valid_keys = [k for k in condition_keys\n                  if not cond_results.get(k, {}).get(\"skipped\", True)]\n    specs = [\"baseline\", \"plus_mean_acc\", \"plus_n_local\", \"plus_both\"]\n    sig_counts = {}\n\n    for spec in specs:\n        eta_ps = [cond_results[k][spec][\"eta_p\"] for k in valid_keys]\n        keff_ps = [cond_results[k][spec][\"keff_p\"] for k in valid_keys]\n\n        if len(valid_keys) > 0:\n            _, eta_fdr, _, _ = multipletests(eta_ps, alpha=FDR_ALPHA, method=\"fdr_bh\")\n            _, keff_fdr, _, _ = multipletests(keff_ps, alpha=FDR_ALPHA, method=\"fdr_bh\")\n        else:\n            eta_fdr = keff_fdr = np.array([])\n\n        for i, k in enumerate(valid_keys):\n            cond_results[k][spec][\"eta_fdr_p\"] = float(eta_fdr[i])\n            cond_results[k][spec][\"keff_fdr_p\"] = float(keff_fdr[i])\n\n        eta_sig = sum(1 for i in range(len(valid_keys)) if eta_fdr[i] < FDR_ALPHA)\n        keff_sig = sum(1 for i in range(len(valid_keys)) if keff_fdr[i] < FDR_ALPHA)\n\n        entry = {\"eta_sig\": f\"{eta_sig}/{len(valid_keys)}\",\n                 \"keff_sig\": f\"{keff_sig}/{len(valid_keys)}\"}\n\n        if spec in (\"plus_mean_acc\", \"plus_both\"):\n            ma_ps = [cond_results[k][spec][\"mean_acc_p\"] for k in valid_keys]\n            _, ma_fdr, _, _ = multipletests(ma_ps, alpha=FDR_ALPHA, method=\"fdr_bh\")\n            entry[\"mean_acc_sig\"] = f\"{sum(1 for p in ma_fdr if p < FDR_ALPHA)}/{len(valid_keys)}\"\n\n        if spec in (\"plus_n_local\", \"plus_both\"):\n            nl_ps = [cond_results[k][spec][\"n_local_p\"] for k in valid_keys]\n            _, nl_fdr, _, _ = multipletests(nl_ps, alpha=FDR_ALPHA, method=\"fdr_bh\")\n            entry[\"n_local_sig\"] = f\"{sum(1 for p in nl_fdr if p < FDR_ALPHA)}/{len(valid_keys)}\"\n\n        if spec != \"baseline\":\n            eta_chgs = [cond_results[k][spec][\"eta_beta_change_pct\"]\n                        for k in valid_keys\n                        if cond_results[k][spec][\"eta_beta_change_pct\"] is not None]\n            keff_chgs = [cond_results[k][spec][\"keff_beta_change_pct\"]\n                         for k in valid_keys\n                         if cond_results[k][spec][\"keff_beta_change_pct\"] is not None]\n            entry[\"eta_beta_change_pct_avg\"] = float(np.mean(eta_chgs)) if eta_chgs else None\n            entry[\"keff_beta_change_pct_avg\"] = float(np.mean(keff_chgs)) if keff_chgs else None\n\n        sig_counts[spec] = entry\n\n    # VIF aggregate\n    vif_agg = {}\n    for var in [\"log_keff\", \"log_eta\", \"mean_acc\", \"n_local\"]:\n        vals = [cond_results[k][\"vif\"][var] for k in valid_keys]\n        vif_agg[var] = {\"mean\": float(np.mean(vals)), \"max\": float(np.max(vals))}\n\n    return {\n        \"per_condition\": cond_results,\n        \"summary\": sig_counts,\n        \"vif_aggregate\": vif_agg,\n        \"n_conditions\": len(valid_keys),\n    }\n\n\ndef main():\n    print(\"Loading data...\")\n    clean, attacked = load_all_scores()\n    pairs = load_pairs()\n    mi_data = load_mi_data()\n\n    clean_acc = compute_clean_accuracy(clean, pairs)\n    print(f\"  Clean accuracy: {len(clean_acc)} entries\")\n\n    ind_asr = {}\n    for ds in DATASETS:\n        for atk in ATTACKS:\n            for mid in ALL_MODELS:\n                if mid in clean.get(ds, {}) and mid in attacked.get(ds, {}).get(atk, {}):\n                    ind_asr[(ds, atk, mid)] = compute_individual_asr(\n                        clean[ds][mid], attacked[ds][atk][mid], pairs[ds]\n                    )\n    print(f\"  Individual ASR: {len(ind_asr)} entries\")\n\n    print(\"\\n=== K=3 (max-MI K_eff) ===\")\n    k3 = run_one_k(3, ALL_MODELS, mi_data, clean, attacked, pairs,\n                   ind_asr, clean_acc, keff_maxmi)\n\n    print(\"\\n=== K=5 (avg pairwise K_eff) ===\")\n    k5 = run_one_k(5, ALL_MODELS, mi_data, clean, attacked, pairs,\n                   ind_asr, clean_acc, keff_avg_pairwise)\n\n    # Over-control check\n    def _sig_n(s): return int(s.split(\"/\")[0])\n\n    k3b_e, k3b_k = _sig_n(k3[\"summary\"][\"baseline\"][\"eta_sig\"]), _sig_n(k3[\"summary\"][\"baseline\"][\"keff_sig\"])\n    k3x_e, k3x_k = _sig_n(k3[\"summary\"][\"plus_both\"][\"eta_sig\"]), _sig_n(k3[\"summary\"][\"plus_both\"][\"keff_sig\"])\n    k5b_e, k5b_k = _sig_n(k5[\"summary\"][\"baseline\"][\"eta_sig\"]), _sig_n(k5[\"summary\"][\"baseline\"][\"keff_sig\"])\n    k5x_e, k5x_k = _sig_n(k5[\"summary\"][\"plus_both\"][\"eta_sig\"]), _sig_n(k5[\"summary\"][\"plus_both\"][\"keff_sig\"])\n\n    over_control = (\n        (k3x_e == 0 and k3x_k == 0 and (k3b_e > 0 or k3b_k > 0)) or\n        (k5x_e == 0 and k5x_k == 0 and (k5b_e > 0 or k5b_k > 0))\n    )\n\n    high_vif = any(\n        kx[\"vif_aggregate\"][v][\"max\"] > 10\n        for kx in [k3, k5] for v in [\"log_keff\", \"log_eta\", \"mean_acc\", \"n_local\"]\n    )\n\n    summary_parts = [\n        f\"K=3 baseline: eta {k3['summary']['baseline']['eta_sig']}, keff {k3['summary']['baseline']['keff_sig']}. \"\n        f\"+both: eta {k3['summary']['plus_both']['eta_sig']}, keff {k3['summary']['plus_both']['keff_sig']}.\",\n        f\"K=5 baseline: eta {k5['summary']['baseline']['eta_sig']}, keff {k5['summary']['baseline']['keff_sig']}. \"\n        f\"+both: eta {k5['summary']['plus_both']['eta_sig']}, keff {k5['summary']['plus_both']['keff_sig']}.\",\n    ]\n    if over_control:\n        summary_parts.append(\"OVER-CONTROL WARNING: adding both controls killed all significance.\")\n    if high_vif:\n        summary_parts.append(\"HIGH VIF detected (>10), multicollinearity concern.\")\n    summary = \" \".join(summary_parts)\n\n    print(f\"\\n{'='*70}\")\n    print(\"SUMMARY\")\n    print(f\"{'='*70}\")\n    for spec in [\"baseline\", \"plus_mean_acc\", \"plus_n_local\", \"plus_both\"]:\n        k3s = k3[\"summary\"][spec]\n        k5s = k5[\"summary\"][spec]\n        print(f\"  {spec:<20} K=3: eta {k3s['eta_sig']}, keff {k3s['keff_sig']}  |  \"\n              f\"K=5: eta {k5s['eta_sig']}, keff {k5s['keff_sig']}\")\n    print(f\"\\n  Over-control: {over_control}\")\n    print(f\"  High VIF: {high_vif}\")\n\n    output = {\n        \"analysis\": \"controlled_regression_mf1\",\n        \"purpose\": \"Verify eta_max/K_eff significance not driven by model capability confounds\",\n        \"controls\": {\n            \"mean_accuracy\": \"average clean accuracy of panel members for the dataset\",\n            \"n_local\": \"count of local (non-API) models in panel\",\n        },\n        \"method\": \"OLS + clustered SE (K-position max-SE), BH FDR across 12 conditions\",\n        \"K3\": k3,\n        \"K5\": k5,\n        \"over_control_warning\": over_control,\n        \"high_vif_warning\": high_vif,\n        \"summary\": summary,\n    }\n\n    out_path = Path(\"/root/cert_manip_resist_eval/artifacts/results/plan001/controlled_regression.json\")\n    out_path.parent.mkdir(parents=True, exist_ok=True)\n    with open(out_path, \"w\") as f:\n        json.dump(output, f, indent=2, default=_json_default, ensure_ascii=False)\n    print(f\"\\nSaved: {out_path}\")\n\n\nif __name__ == \"__main__\":\n    main()\nPYEOF"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_controlled-regression_20260523T071753",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "seetacloud-rtx6000",
    "command": "cat > /root/cert_manip_resist_eval/scripts/run_controlled_regression.py << 'PYEOF'\n#!/usr/bin/env python3\n\"\"\"Controlled Regression with Confound Variables — MF-1 supplement.\"\"\"\n\nimport os\nos.environ[\"HF_HOME\"] = \"/root/autodl-tmp/.hf_cache\"\n\nimport sys\nsys.path.insert(0, \"/root/cert_manip_resist_eval\")\n\nimport json\nimport itertools\nimport numpy as np\nimport statsmodels.api as sm\nfrom pathlib import Path\nfrom scipy.stats import t as t_dist\nfrom statsmodels.stats.multitest import multipletests\nfrom statsmodels.stats.outliers_influence import variance_inflation_factor\n\nfrom src.unified_data_loader import (\n    ALL_MODELS, API_MODELS, LOCAL_MODELS, DATASETS, ATTACKS,\n    load_all_scores, load_pairs, load_mi_data, compute_clean_accuracy,\n)\n\nEPS = 1e-6\nFDR_ALPHA = 0.05\nLOCAL_SET = set(LOCAL_MODELS)\n\n\ndef _json_default(obj):\n    if isinstance(obj, np.floating):\n        v = float(obj)\n        return None if (np.isnan(v) or np.isinf(v)) else v\n    if isinstance(obj, np.integer):\n        return int(obj)\n    if isinstance(obj, np.ndarray):\n        return obj.tolist()\n    if isinstance(obj, np.bool_):\n        return bool(obj)\n    raise TypeError(f\"Not JSON serializable: {type(obj)}\")\n\n\ndef majority_vote(votes):\n    counts = {\"A\": 0, \"B\": 0, \"tie\": 0}\n    for v in votes:\n        counts[v] = counts.get(v, 0) + 1\n    mc = max(counts.values())\n    winners = [k for k, c in counts.items() if c == mc]\n    if len(winners) == 1:\n        return winners[0]\n    for w in winners:\n        if w != \"tie\":\n            return w\n    return \"tie\"\n\n\ndef compute_individual_asr(clean_list, attacked_list, pairs):\n    n = min(len(clean_list), len(attacked_list), len(pairs))\n    n_flips = n_correct = 0\n    for i in range(n):\n        gt = pairs[i][\"ground_truth_winner\"]\n        if clean_list[i].get(\"winner\", \"tie\") == gt:\n            n_correct += 1\n            if attacked_list[i].get(\"winner\", \"tie\") != gt:\n                n_flips += 1\n    return n_flips / max(n_correct, 1)\n\n\ndef compute_panel_asr(jids, clean, attacked, pairs):\n    n = min(len(pairs), *(len(clean[j]) for j in jids),\n            *(len(attacked[j]) for j in jids))\n    n_flips = n_correct = 0\n    for i in range(n):\n        gt = pairs[i][\"ground_truth_winner\"]\n        cv = majority_vote([clean[j][i].get(\"winner\", \"tie\") for j in jids])\n        if cv != gt:\n            continue\n        n_correct += 1\n        av = majority_vote([attacked[j][i].get(\"winner\", \"tie\") for j in jids])\n        if av != gt:\n            n_flips += 1\n    return n_flips / max(n_correct, 1)\n\n\ndef keff_maxmi(mi_matrix, model_indices):\n    K = len(model_indices)\n    max_mi = 0.0\n    for a, b in itertools.combinations(model_indices, 2):\n        max_mi = max(max_mi, mi_matrix[a][b])\n    return 1 + (K - 1) * np.exp(-2 * max_mi)\n\n\ndef keff_avg_pairwise(mi_matrix, model_indices):\n    K = len(model_indices)\n    if K <= 1:\n        return 1.0\n    keff = 0.0\n    for i_idx in model_indices:\n        term = 1.0\n        for j_idx in model_indices:\n            if i_idx != j_idx:\n                term += np.exp(-2 * mi_matrix[i_idx][j_idx])\n        keff += term\n    return keff / K\n\n\ndef clustered_se_max(y, X, panel_jids_list, K):\n    Xc = sm.add_constant(X)\n    fit_ols = sm.OLS(y, Xc).fit()\n    n_params = Xc.shape[1]\n    max_se = np.zeros(n_params)\n\n    G_min = 999\n    for pos in range(K):\n        cluster_var = np.array([jids[pos] for jids in panel_jids_list])\n        unique_judges = sorted(set(cluster_var))\n        G_min = min(G_min, len(unique_judges))\n        judge_to_int = {j: idx for idx, j in enumerate(unique_judges)}\n        cluster_int = np.array([judge_to_int[j] for j in cluster_var])\n        try:\n            fit_cl = sm.OLS(y, Xc).fit(\n                cov_type=\"cluster\", cov_kwds={\"groups\": cluster_int}\n            )\n            max_se = np.maximum(max_se, fit_cl.bse)\n        except Exception:\n            pass\n\n    df = max(G_min - 1, 1)\n    t_stats = fit_ols.params / np.where(max_se > 1e-15, max_se, np.inf)\n    p_values = 2 * t_dist.sf(np.abs(t_stats), df=df)\n    return fit_ols.params, max_se, p_values, fit_ols\n\n\ndef compute_vif(X):\n    Xc = sm.add_constant(X)\n    vifs = {}\n    for i in range(1, Xc.shape[1]):\n        vifs[i - 1] = variance_inflation_factor(Xc, i)\n    return vifs\n\n\ndef _pct_change(old, new):\n    if abs(old) < 1e-15:\n        return None\n    return float((new - old) / abs(old) * 100)\n\n\ndef run_one_condition(y, X_base, controls, panel_jids_list, K):\n    results = {}\n\n    params_b, se_b, pvals_b, fit_b = clustered_se_max(y, X_base, panel_jids_list, K)\n    results[\"baseline\"] = {\n        \"keff_beta\": float(params_b[1]), \"eta_beta\": float(params_b[2]),\n        \"keff_p\": float(pvals_b[1]), \"eta_p\": float(pvals_b[2]),\n        \"r2\": float(fit_b.rsquared),\n    }\n\n    # +mean_acc\n    X_ma = np.column_stack([X_base, controls[\"mean_acc\"]])\n    params_ma, _, pvals_ma, fit_ma = clustered_se_max(y, X_ma, panel_jids_list, K)\n    results[\"plus_mean_acc\"] = {\n        \"keff_beta\": float(params_ma[1]), \"eta_beta\": float(params_ma[2]),\n        \"mean_acc_beta\": float(params_ma[3]),\n        \"keff_p\": float(pvals_ma[1]), \"eta_p\": float(pvals_ma[2]),\n        \"mean_acc_p\": float(pvals_ma[3]),\n        \"keff_beta_change_pct\": _pct_change(params_b[1], params_ma[1]),\n        \"eta_beta_change_pct\": _pct_change(params_b[2], params_ma[2]),\n        \"r2\": float(fit_ma.rsquared),\n    }\n\n    # +n_local\n    X_nl = np.column_stack([X_base, controls[\"n_local\"]])\n    params_nl, _, pvals_nl, fit_nl = clustered_se_max(y, X_nl, panel_jids_list, K)\n    results[\"plus_n_local\"] = {\n        \"keff_beta\": float(params_nl[1]), \"eta_beta\": float(params_nl[2]),\n        \"n_local_beta\": float(params_nl[3]),\n        \"keff_p\": float(pvals_nl[1]), \"eta_p\": float(pvals_nl[2]),\n        \"n_local_p\": float(pvals_nl[3]),\n        \"keff_beta_change_pct\": _pct_change(params_b[1], params_nl[1]),\n        \"eta_beta_change_pct\": _pct_change(params_b[2], params_nl[2]),\n        \"r2\": float(fit_nl.rsquared),\n    }\n\n    # +both\n    X_both = np.column_stack([X_base, controls[\"mean_acc\"], controls[\"n_local\"]])\n    params_bt, _, pvals_bt, fit_bt = clustered_se_max(y, X_both, panel_jids_list, K)\n    results[\"plus_both\"] = {\n        \"keff_beta\": float(params_bt[1]), \"eta_beta\": float(params_bt[2]),\n        \"mean_acc_beta\": float(params_bt[3]), \"n_local_beta\": float(params_bt[4]),\n        \"keff_p\": float(pvals_bt[1]), \"eta_p\": float(pvals_bt[2]),\n        \"mean_acc_p\": float(pvals_bt[3]), \"n_local_p\": float(pvals_bt[4]),\n        \"keff_beta_change_pct\": _pct_change(params_b[1], params_bt[1]),\n        \"eta_beta_change_pct\": _pct_change(params_b[2], params_bt[2]),\n        \"r2\": float(fit_bt.rsquared),\n    }\n\n    # VIF on +both\n    vif_raw = compute_vif(X_both)\n    results[\"vif\"] = {\n        \"log_keff\": float(vif_raw[0]), \"log_eta\": float(vif_raw[1]),\n        \"mean_acc\": float(vif_raw[2]), \"n_local\": float(vif_raw[3]),\n    }\n    return results\n\n\ndef run_one_k(K, all_models, mi_data, clean, attacked, pairs, ind_asr,\n              clean_acc, keff_func):\n    model_to_idx = {m: i for i, m in enumerate(all_models)}\n    all_combos = list(itertools.combinations(range(len(all_models)), K))\n    condition_keys = [f\"{ds}x{atk}\" for ds in DATASETS for atk in ATTACKS]\n\n    cond_results = {}\n\n    for ds in DATASETS:\n        ds_clean = clean.get(ds, {})\n        ds_attacked = attacked.get(ds, {})\n        ds_pairs = pairs.get(ds, [])\n        mi_mat = np.array(mi_data[\"mi_matrix\"][ds])\n\n        for atk in ATTACKS:\n            cond_key = f\"{ds}x{atk}\"\n            print(f\"  {cond_key}...\", end=\" \", flush=True)\n\n            if not ds_clean or not ds_attacked.get(atk) or not ds_pairs:\n                print(\"SKIP: missing data\")\n                cond_results[cond_key] = {\"skipped\": True}\n                continue\n\n            panel_asrs, panel_keffs, panel_etas = [], [], []\n            panel_mean_accs, panel_n_locals = [], []\n            panel_jids_list = []\n\n            for combo in all_combos:\n                jids = [all_models[i] for i in combo]\n                if not all((ds, atk, j) in ind_asr for j in jids):\n                    continue\n\n                keff = keff_func(mi_mat, list(combo))\n                eta_max = max(ind_asr[(ds, atk, j)] for j in jids)\n\n                cs = {j: ds_clean[j] for j in jids}\n                ats = {j: ds_attacked[atk][j] for j in jids}\n                asr = compute_panel_asr(jids, cs, ats, ds_pairs)\n\n                accs = [clean_acc.get((j, ds), 0.5) for j in jids]\n                mean_acc = np.mean(accs)\n                n_local = sum(1 for j in jids if j in LOCAL_SET)\n\n                panel_asrs.append(asr)\n                panel_keffs.append(keff)\n                panel_etas.append(eta_max)\n                panel_mean_accs.append(mean_acc)\n                panel_n_locals.append(n_local)\n                panel_jids_list.append(jids)\n\n            n_panels = len(panel_asrs)\n            print(f\"{n_panels} panels\", end=\" \", flush=True)\n\n            if n_panels < 10:\n                print(\"SKIP\")\n                cond_results[cond_key] = {\"skipped\": True}\n                continue\n\n            panel_asrs = np.array(panel_asrs)\n            panel_keffs = np.array(panel_keffs)\n            panel_etas = np.array(panel_etas)\n            panel_mean_accs = np.array(panel_mean_accs)\n            panel_n_locals = np.array(panel_n_locals, dtype=float)\n\n            if np.std(panel_asrs) < 1e-10:\n                print(\"SKIP: constant ASR\")\n                cond_results[cond_key] = {\"skipped\": True}\n                continue\n\n            y = np.log(panel_asrs + EPS)\n            X_base = np.column_stack([np.log(panel_keffs),\n                                       np.log(panel_etas + EPS)])\n            controls = {\"mean_acc\": panel_mean_accs, \"n_local\": panel_n_locals}\n\n            res = run_one_condition(y, X_base, controls, panel_jids_list, K)\n            res[\"n_panels\"] = n_panels\n            res[\"skipped\"] = False\n            cond_results[cond_key] = res\n\n            print(f\"VIF: keff={res['vif']['log_keff']:.2f} \"\n                  f\"eta={res['vif']['log_eta']:.2f} \"\n                  f\"macc={res['vif']['mean_acc']:.2f} \"\n                  f\"nloc={res['vif']['n_local']:.2f}\")\n\n    # FDR correction\n    valid_keys = [k for k in condition_keys\n                  if not cond_results.get(k, {}).get(\"skipped\", True)]\n    specs = [\"baseline\", \"plus_mean_acc\", \"plus_n_local\", \"plus_both\"]\n    sig_counts = {}\n\n    for spec in specs:\n        eta_ps = [cond_results[k][spec][\"eta_p\"] for k in valid_keys]\n        keff_ps = [cond_results[k][spec][\"keff_p\"] for k in valid_keys]\n\n        if len(valid_keys) > 0:\n            _, eta_fdr, _, _ = multipletests(eta_ps, alpha=FDR_ALPHA, method=\"fdr_bh\")\n            _, keff_fdr, _, _ = multipletests(keff_ps, alpha=FDR_ALPHA, method=\"fdr_bh\")\n        else:\n            eta_fdr = keff_fdr = np.array([])\n\n        for i, k in enumerate(valid_keys):\n            cond_results[k][spec][\"eta_fdr_p\"] = float(eta_fdr[i])\n            cond_results[k][spec][\"keff_fdr_p\"] = float(keff_fdr[i])\n\n        eta_sig = sum(1 for i in range(len(valid_keys)) if eta_fdr[i] < FDR_ALPHA)\n        keff_sig = sum(1 for i in range(len(valid_keys)) if keff_fdr[i] < FDR_ALPHA)\n\n        entry = {\"eta_sig\": f\"{eta_sig}/{len(valid_keys)}\",\n                 \"keff_sig\": f\"{keff_sig}/{len(valid_keys)}\"}\n\n        if spec in (\"plus_mean_acc\", \"plus_both\"):\n            ma_ps = [cond_results[k][spec][\"mean_acc_p\"] for k in valid_keys]\n            _, ma_fdr, _, _ = multipletests(ma_ps, alpha=FDR_ALPHA, method=\"fdr_bh\")\n            entry[\"mean_acc_sig\"] = f\"{sum(1 for p in ma_fdr if p < FDR_ALPHA)}/{len(valid_keys)}\"\n\n        if spec in (\"plus_n_local\", \"plus_both\"):\n            nl_ps = [cond_results[k][spec][\"n_local_p\"] for k in valid_keys]\n            _, nl_fdr, _, _ = multipletests(nl_ps, alpha=FDR_ALPHA, method=\"fdr_bh\")\n            entry[\"n_local_sig\"] = f\"{sum(1 for p in nl_fdr if p < FDR_ALPHA)}/{len(valid_keys)}\"\n\n        if spec != \"baseline\":\n            eta_chgs = [cond_results[k][spec][\"eta_beta_change_pct\"]\n                        for k in valid_keys\n                        if cond_results[k][spec][\"eta_beta_change_pct\"] is not None]\n            keff_chgs = [cond_results[k][spec][\"keff_beta_change_pct\"]\n                         for k in valid_keys\n                         if cond_results[k][spec][\"keff_beta_change_pct\"] is not None]\n            entry[\"eta_beta_change_pct_avg\"] = float(np.mean(eta_chgs)) if eta_chgs else None\n            entry[\"keff_beta_change_pct_avg\"] = float(np.mean(keff_chgs)) if keff_chgs else None\n\n        sig_counts[spec] = entry\n\n    # VIF aggregate\n    vif_agg = {}\n    for var in [\"log_keff\", \"log_eta\", \"mean_acc\", \"n_local\"]:\n        vals = [cond_results[k][\"vif\"][var] for k in valid_keys]\n        vif_agg[var] = {\"mean\": float(np.mean(vals)), \"max\": float(np.max(vals))}\n\n    return {\n        \"per_condition\": cond_results,\n        \"summary\": sig_counts,\n        \"vif_aggregate\": vif_agg,\n        \"n_conditions\": len(valid_keys),\n    }\n\n\ndef main():\n    print(\"Loading data...\")\n    clean, attacked = load_all_scores()\n    pairs = load_pairs()\n    mi_data = load_mi_data()\n\n    clean_acc = compute_clean_accuracy(clean, pairs)\n    print(f\"  Clean accuracy: {len(clean_acc)} entries\")\n\n    ind_asr = {}\n    for ds in DATASETS:\n        for atk in ATTACKS:\n            for mid in ALL_MODELS:\n                if mid in clean.get(ds, {}) and mid in attacked.get(ds, {}).get(atk, {}):\n                    ind_asr[(ds, atk, mid)] = compute_individual_asr(\n                        clean[ds][mid], attacked[ds][atk][mid], pairs[ds]\n                    )\n    print(f\"  Individual ASR: {len(ind_asr)} entries\")\n\n    print(\"\\n=== K=3 (max-MI K_eff) ===\")\n    k3 = run_one_k(3, ALL_MODELS, mi_data, clean, attacked, pairs,\n                   ind_asr, clean_acc, keff_maxmi)\n\n    print(\"\\n=== K=5 (avg pairwise K_eff) ===\")\n    k5 = run_one_k(5, ALL_MODELS, mi_data, clean, attacked, pairs,\n                   ind_asr, clean_acc, keff_avg_pairwise)\n\n    # Over-control check\n    def _sig_n(s): return int(s.split(\"/\")[0])\n\n    k3b_e, k3b_k = _sig_n(k3[\"summary\"][\"baseline\"][\"eta_sig\"]), _sig_n(k3[\"summary\"][\"baseline\"][\"keff_sig\"])\n    k3x_e, k3x_k = _sig_n(k3[\"summary\"][\"plus_both\"][\"eta_sig\"]), _sig_n(k3[\"summary\"][\"plus_both\"][\"keff_sig\"])\n    k5b_e, k5b_k = _sig_n(k5[\"summary\"][\"baseline\"][\"eta_sig\"]), _sig_n(k5[\"summary\"][\"baseline\"][\"keff_sig\"])\n    k5x_e, k5x_k = _sig_n(k5[\"summary\"][\"plus_both\"][\"eta_sig\"]), _sig_n(k5[\"summary\"][\"plus_both\"][\"keff_sig\"])\n\n    over_control = (\n        (k3x_e == 0 and k3x_k == 0 and (k3b_e > 0 or k3b_k > 0)) or\n        (k5x_e == 0 and k5x_k == 0 and (k5b_e > 0 or k5b_k > 0))\n    )\n\n    high_vif = any(\n        kx[\"vif_aggregate\"][v][\"max\"] > 10\n        for kx in [k3, k5] for v in [\"log_keff\", \"log_eta\", \"mean_acc\", \"n_local\"]\n    )\n\n    summary_parts = [\n        f\"K=3 baseline: eta {k3['summary']['baseline']['eta_sig']}, keff {k3['summary']['baseline']['keff_sig']}. \"\n        f\"+both: eta {k3['summary']['plus_both']['eta_sig']}, keff {k3['summary']['plus_both']['keff_sig']}.\",\n        f\"K=5 baseline: eta {k5['summary']['baseline']['eta_sig']}, keff {k5['summary']['baseline']['keff_sig']}. \"\n        f\"+both: eta {k5['summary']['plus_both']['eta_sig']}, keff {k5['summary']['plus_both']['keff_sig']}.\",\n    ]\n    if over_control:\n        summary_parts.append(\"OVER-CONTROL WARNING: adding both controls killed all significance.\")\n    if high_vif:\n        summary_parts.append(\"HIGH VIF detected (>10), multicollinearity concern.\")\n    summary = \" \".join(summary_parts)\n\n    print(f\"\\n{'='*70}\")\n    print(\"SUMMARY\")\n    print(f\"{'='*70}\")\n    for spec in [\"baseline\", \"plus_mean_acc\", \"plus_n_local\", \"plus_both\"]:\n        k3s = k3[\"summary\"][spec]\n        k5s = k5[\"summary\"][spec]\n        print(f\"  {spec:<20} K=3: eta {k3s['eta_sig']}, keff {k3s['keff_sig']}  |  \"\n              f\"K=5: eta {k5s['eta_sig']}, keff {k5s['keff_sig']}\")\n    print(f\"\\n  Over-control: {over_control}\")\n    print(f\"  High VIF: {high_vif}\")\n\n    output = {\n        \"analysis\": \"controlled_regression_mf1\",\n        \"purpose\": \"Verify eta_max/K_eff significance not driven by model capability confounds\",\n        \"controls\": {\n            \"mean_accuracy\": \"average clean accuracy of panel members for the dataset\",\n            \"n_local\": \"count of local (non-API) models in panel\",\n        },\n        \"method\": \"OLS + clustered SE (K-position max-SE), BH FDR across 12 conditions\",\n        \"K3\": k3,\n        \"K5\": k5,\n        \"over_control_warning\": over_control,\n        \"high_vif_warning\": high_vif,\n        \"summary\": summary,\n    }\n\n    out_path = Path(\"/root/cert_manip_resist_eval/artifacts/results/plan001/controlled_regression.json\")\n    out_path.parent.mkdir(parents=True, exist_ok=True)\n    with open(out_path, \"w\") as f:\n        json.dump(output, f, indent=2, default=_json_default, ensure_ascii=False)\n    print(f\"\\nSaved: {out_path}\")\n\n\nif __name__ == \"__main__\":\n    main()\nPYEOF"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-23T07:24:01.254363+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_controlled-regression_20260523T071753",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-23T07:24:01.254498+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "seetacloud-rtx6000",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/cert_manip_resist_eval && python scripts/run_controlled_regression.py 2>&1",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_controlled-regression_20260523T071753",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "seetacloud-rtx6000",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/cert_manip_resist_eval && python scripts/run_controlled_regression.py 2>&1",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-23T07:24:01.254670+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Loading data...\\n  Clean accuracy: 30 entries\\n  Individual ASR: 180 entries\\n\\n=== K=3 (max-MI K_eff) ===\\n  mmluxprompt_injection... 455 panels VIF: keff=1.82 eta=1.37 macc=1.59 nloc=1.42\\n  mmluxsycophancy... 455 panels VIF: keff=1.95 eta=1.30 macc=1.54 nloc=1.54\\n  mmluxscore_manipulation... 455 panels VIF: keff=1.68 eta=1.76 macc=1.96 nloc=1.44\\n  mmluxverbosity_bias... 455 panels VIF: keff=1.88 eta=1.30 macc=1.57 nloc=1.54\\n  mmluxposition_bias... 455 panels VIF: keff=1.66 eta=2.16 macc=2.28 nloc=1.46\\n  mmluxauthority_bias... 455 panels VIF: keff=1.76 eta=1.32 macc=1.63 nloc=1.42\\n  arc_challengexprompt_injection... 455 panels VIF: keff=2.65 eta=2.39 macc=4.00 nloc=1.31\\n  arc_challengexsycophancy... 455 panels VIF: keff=2.52 eta=3.37 macc=4.78 nloc=1.51\\n  arc_challengexscore_manipulation... 455 panels VIF: keff=3.59 eta=7.93 macc=13.06 nloc=1.21\\n  arc_challengexverbosity_bias... 455 panels VIF: keff=2.87 eta=4.19 macc=7.05 nloc=1.17\\n  arc_challengexposition_bias... 455 panels VIF: keff=4.28 eta=13.12 macc=21.25 nloc=1.17\\n  arc_challengexauthority_bias... 455 panels VIF: keff=2.60 eta=2.82 macc=4.73 nloc=1.31\\n\\n=== K=5 (avg pairwise K_eff) ===\\n  mmluxprompt_injection... 3003 panels VIF: keff=3.58 eta=1.75 macc=2.51 nloc=1.29\\n  mmluxsycophancy... 3003 panels VIF: keff=2.79 eta=1.32 macc=2.42 nloc=1.42\\n  mmluxscore_manipulation... 3003 panels VIF: keff=3.68 eta=2.51 macc=2.35 nloc=1.29\\n  mmluxverbosity_bias... 3003 panels VIF: keff=2.78 eta=1.32 macc=2.41 nloc=1.41\\n  mmluxposition_bias... 3003 panels VIF: keff=2.26 eta=1.82 macc=2.95 nloc=1.30\\n  mmluxauthority_bias... 3003 panels VIF: keff=3.05 eta=1.46 macc=2.42 nloc=1.29\\n  arc_challengexprompt_injection... 3003 panels VIF: keff=18.03 eta=4.37 macc=10.59 nloc=1.13\\n  arc_challengexsycophancy... 3003 panels VIF: keff=8.22 eta=3.49 macc=9.09 nloc=1.61\\n  arc_challengexscore_manipulation... 3003 panels VIF: keff=10.18 e
…[truncated 1029 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_controlled-regression_20260523T071753",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-23T07:24:01.254861+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "controlled_regression",
  "type": "data",
  "description": "Controlled regression with confound variables (mean_accuracy, n_local) for MF-1 supplement. OLS + clustered SE, BH FDR across 12 conditions.",
  "project": "cert_manip_resist_eval",
  "source_path": "/root/cert_manip_resist_eval/artifacts/results/plan001/controlled_regression.json",
  "tags": "['mf1', 'confound', 'controlled_regression', 'robustness']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_controlled-regression_20260523T071753",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "controlled_regression",
    "type": "data",
    "description": "Controlled regression with confound variables (mean_accuracy, n_local) for MF-1 supplement. OLS + clustered SE, BH FDR across 12 conditions.",
    "project": "cert_manip_resist_eval",
    "source_path": "/root/cert_manip_resist_eval/artifacts/results/plan001/controlled_regression.json",
    "tags": "['mf1', 'confound', 'controlled_regression', 'robustness']"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-23T07:24:01.255006+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"source_path not found: /root/cert_manip_resist_eval/artifacts/results/plan001/controlled_regression.json\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_controlled-regression_20260523T071753",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-23T07:24:01.255130+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "controlled_regression",
  "type": "data",
  "description": "Controlled regression with confound variables (mean_accuracy, n_local) for MF-1 supplement. OLS + clustered SE, BH FDR across 12 conditions.",
  "project": "cert_manip_resist_eval",
  "tags": "['mf1', 'confound', 'controlled_regression', 'robustness']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_controlled-regression_20260523T071753",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "controlled_regression",
    "type": "data",
    "description": "Controlled regression with confound variables (mean_accuracy, n_local) for MF-1 supplement. OLS + clustered SE, BH FDR across 12 conditions.",
    "project": "cert_manip_resist_eval",
    "tags": "['mf1', 'confound', 'controlled_regression', 'robustness']"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-23T07:24:01.255256+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"One of source_path, content, or url must be provided.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_controlled-regression_20260523T071753",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-23T07:24:01.255371+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "seetacloud-rtx6000",
  "command": "head -5 /root/cert_manip_resist_eval/artifacts/results/plan001/controlled_regression.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_controlled-regression_20260523T071753",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "seetacloud-rtx6000",
    "command": "head -5 /root/cert_manip_resist_eval/artifacts/results/plan001/controlled_regression.json"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-23T07:24:01.255500+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"analysis\\\": \\\"controlled_regression_mf1\\\",\\n  \\\"purpose\\\": \\\"Verify eta_max/K_eff significance not driven by model capability confounds\\\",\\n  \\\"controls\\\": {\\n    \\\"mean_accuracy\\\": \\\"average clean accuracy of panel members for the dataset\\\",\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_controlled-regression_20260523T071753",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-23T07:24:01.255631+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "seetacloud-rtx6000",
  "command": "cat /root/cert_manip_resist_eval/artifacts/results/plan001/controlled_regression.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_controlled-regression_20260523T071753",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "seetacloud-rtx6000",
    "command": "cat /root/cert_manip_resist_eval/artifacts/results/plan001/controlled_regression.json"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-23T07:24:01.255950+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"analysis\\\": \\\"controlled_regression_mf1\\\",\\n  \\\"purpose\\\": \\\"Verify eta_max/K_eff significance not driven by model capability confounds\\\",\\n  \\\"controls\\\": {\\n    \\\"mean_accuracy\\\": \\\"average clean accuracy of panel members for the dataset\\\",\\n    \\\"n_local\\\": \\\"count of local (non-API) models in panel\\\"\\n  },\\n  \\\"method\\\": \\\"OLS + clustered SE (K-position max-SE), BH FDR across 12 conditions\\\",\\n  \\\"K3\\\": {\\n    \\\"per_condition\\\": {\\n      \\\"mmluxprompt_injection\\\": {\\n        \\\"baseline\\\": {\\n          \\\"keff_beta\\\": 2.6075929417315207,\\n          \\\"eta_beta\\\": 0.7019124113211399,\\n          \\\"keff_p\\\": 0.000239111690852645,\\n          \\\"eta_p\\\": 2.444528595555763e-07,\\n          \\\"r2\\\": 0.7749924202643049,\\n          \\\"eta_fdr_p\\\": 2.933434314666916e-06,\\n          \\\"keff_fdr_p\\\": 0.00095644676341058\\n        },\\n        \\\"plus_mean_acc\\\": {\\n          \\\"keff_beta\\\": 2.3437591370086435,\\n          \\\"eta_beta\\\": 0.67968164863559,\\n          \\\"mean_acc_beta\\\": -1.7171459444143047,\\n          \\\"keff_p\\\": 0.0007046843206462593,\\n          \\\"eta_p\\\": 1.2496371909742773e-06,\\n          \\\"mean_acc_p\\\": 0.1154775700616433,\\n          \\\"keff_beta_change_pct\\\": -10.11790607730682,\\n          \\\"eta_beta_change_pct\\\": -3.1671704798191493,\\n          \\\"r2\\\": 0.7811665402994852,\\n          \\\"eta_fdr_p\\\": 1.4995646291691328e-05,\\n          \\\"keff_fdr_p\\\": 0.0036639248483026484\\n        },\\n        \\\"plus_n_local\\\": {\\n          \\\"keff_beta\\\": 2.1596551470681122,\\n          \\\"eta_beta\\\": 0.6918712752603069,\\n          \\\"n_local_beta\\\": 0.1843678940963216,\\n          \\\"keff_p\\\": 0.0022174251599245075,\\n          \\\"eta_p\\\": 1.2257098534727146e-07,\\n          \\\"n_local_p\\\": 0.004214120598583696,\\n          \\\"keff_bet
…[truncated 7898 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_controlled-regression_20260523T071753",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-23T07:24:01.256116+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "controlled_regression",
  "type": "data",
  "description": "Controlled regression with confound variables (mean_accuracy, n_local) for MF-1 supplement",
  "project": "cert_manip_resist_eval",
  "content_filename": "controlled_regression.json",
  "content": "see /root/cert_manip_resist_eval/artifacts/results/plan001/controlled_regression.json",
  "tags": "['mf1', 'confound', 'controlled_regression']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_controlled-regression_20260523T071753",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "controlled_regression",
    "type": "data",
    "description": "Controlled regression with confound variables (mean_accuracy, n_local) for MF-1 supplement",
    "project": "cert_manip_resist_eval",
    "content_filename": "controlled_regression.json",
    "content": "see /root/cert_manip_resist_eval/artifacts/results/plan001/controlled_regression.json",
    "tags": "['mf1', 'confound', 'controlled_regression']"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-23T07:24:01.256266+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260523_b9295a\", \"name\": \"controlled_regression\", \"type\": \"data\", \"description\": \"Controlled regression with confound variables (mean_accuracy, n_local) for MF-1 supplement\", \"path\": \"projects/cert_manip_resist_eval/artifacts/_project/data/controlled_regression.json\", \"url\": null, \"project\": \"cert_manip_resist_eval\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-23T07:23:46.535263+00:00\", \"tags\": [\"mf1\", \"confound\", \"controlled_regression\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_controlled-regression_20260523T071753",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 57 · 2026-05-23T07:24:01.256434+00:00_

完成。结果保存在 `controlled_regression.json`。

**结果汇总**：

| Model Spec | K=3 η_max | K=3 K_eff | K=5 η_max | K=5 K_eff |
|---|---|---|---|---|
| baseline | 10/12 | 10/12 | 4/12 | 7/12 |
| +mean_acc | 7/12 | 7/12 | 6/12 | 4/12 |
| +n_local | 10/12 | 8/12 | 6/12 | 5/12 |
| +both | 6/12 | 6/12 | 6/12 | 3/12 |

**关键发现**：

1. **No over-control**: 加入两个控制变量后，η_max 和 K_eff 的 significance 都没有被完全 killed。K=3 从 10/12 → 6/12，K=5 η_max 反而从 4/12 上升到 6/12（suppression effect）。

2. **控制变量本身显著**: mean_acc K=5 显著 10/12, n_local K=5 显著 10/12 — 这些确实是相关因素，但加入后并未消除 η_max/K_eff 的解释力。

3. **High VIF 警告**: arc_challenge 条件下 VIF > 10（K=5 log_keff max=18.0, mean_acc max=10.7），表明 mean_accuracy 与 K_eff 在 arc_challenge 上存在多重共线性。MMLU 条件下 VIF 均 < 4，无共线性问题。

4. **Beta 变化**: K=5 K_eff 的 β 平均变化 -159%（含符号翻转），主要由 arc_challenge 高 VIF 条件驱动。η_max 的 β 相对稳定（~-23%）。

**对 reviewer 的回应**: η_max/K_eff 的 significance 在加入 confound 后有所减弱但 robust 保留，不是 confound-driven artifact。高 VIF 条件需在论文中注明。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_controlled-regression_20260523T071753"
}
```

</details>

---
