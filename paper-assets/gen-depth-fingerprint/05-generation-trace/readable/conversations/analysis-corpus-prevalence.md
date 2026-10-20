# analysis corpus prevalence

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 55
- **Recorded user turns:** 0
- **Tool calls:** 27
- **Original source:** `logs/chats/worker_analysis_corpus-prevalence_20260517T231957.jsonl`
- **Structured JSON:** [`ac60fcfcf464b65bb9e4.json`](../../sessions/ac/ac60fcfcf464b65bb9e4.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

55 recorded events

### Tool call

_source line 1 · 2026-05-17T23:31:25.639853+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "head -150 /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/eval_8gen_logo.py",
  "description": "Read eval_8gen_logo.py to understand data loading and model training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_corpus-prevalence_20260517T231957",
  "tool": "Bash",
  "tool_args": {
    "command": "head -150 /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/eval_8gen_logo.py",
    "description": "Read eval_8gen_logo.py to understand data loading and model training"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-17T23:31:25.640160+00:00_

Exit code 1
head: cannot open '/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/eval_8gen_logo.py' for reading: No such file or directory

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_corpus-prevalence_20260517T231957",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-17T23:31:25.640313+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/results/ 2>/dev/null; ls /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/logs/ 2>/dev/null; ls /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/*.py 2>/dev/null",
  "description": "List existing files in the project"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_corpus-prevalence_20260517T231957",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/results/ 2>/dev/null; ls /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/logs/ 2>/dev/null; ls /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/*.py 2>/dev/null",
    "description": "List existing files in the project"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-17T23:31:25.640487+00:00_

&lt;tool_use_error>Cancelled: parallel tool call Bash(head -150 /home/ubuntu/.agent-ml-researc…) errored&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_corpus-prevalence_20260517T231957",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-17T23:31:25.640671+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_corpus-prevalence_20260517T231957",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-17T23:31:25.640806+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_corpus-prevalence_20260517T231957",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-17T23:31:25.640933+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "head -200 /root/gen-depth-fingerprint/eval_8gen_logo.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_corpus-prevalence_20260517T231957",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "head -200 /root/gen-depth-fingerprint/eval_8gen_logo.py",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-17T23:31:25.641048+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "ls /root/gen-depth-fingerprint/*.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_corpus-prevalence_20260517T231957",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "ls /root/gen-depth-fingerprint/*.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-17T23:31:25.641274+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\neval_8gen_logo.py — 8-generator LOGO cross-validation.\\n\\n6 original generators (from features_all_models.csv):\\n  pythia-2.8b, pythia-1b, olmo-2-1b, qwen3-0.6b, qwen3-1.7b, qwen3-8b\\n\\n2 new generators (from JSONL):\\n  llama-3.2-3b, mistral-7b-v0.3\\n\\nTasks:\\n  - 3-class LOGO: gen-0 / gen-1 / gen-2+\\n  - Binary LOGO: gen-1 vs gen-2+ (exclude gen-0)\\n  - Bootstrap 95% CI (n=1000)\\n  - Comparison vs 6-gen baseline\\n\\\"\\\"\\\"\\n\\nimport json\\nimport os\\nimport numpy as np\\nimport pandas as pd\\nfrom xgboost import XGBClassifier\\nfrom sklearn.metrics import f1_score\\n\\nSEED = 42\\nFEATURES = [\\\"entropy_mean\\\", \\\"entropy_std\\\", \\\"entropy_min\\\", \\\"entropy_max\\\",\\n            \\\"tail_decay\\\", \\\"ttr\\\", \\\"hapax_ratio\\\"]\\n\\nXGB_PARAMS = dict(n_estimators=200, max_depth=6, learning_rate=0.1,\\n                  random_state=SEED, eval_metric=\\\"mlogloss\\\",\\n                  use_label_encoder=False)\\n\\nCLASS_MAP_3 = {0: 0, 1: 1, 2: 2, 3: 2, 4: 2}\\n\\nROOT = os.path.dirname(os.path.abspath(__file__))\\nDATA_DIR = os.path.join(ROOT, \\\"data\\\")\\nRESULTS_DIR = os.path.join(ROOT, \\\"results\\\")\\n\\n\\ndef load_data():\\n    # 6 original generators from CSV\\n    df_base = pd.read_csv(os.path.join(DATA_DIR, \\\"features_all_models.csv\\\"))\\n\\n    # 2 new generators from JSONL\\n    new_gens = [\\n        (\\\"llama-3.2-3b\\\", os.path.join(DATA_DIR, \\\"llama-3.2-3b\\\", \\\"features_pythia410m.jsonl\\\")),\\n        (\\\"mistral-7b-v0.3\\\", os.path.join(DATA_DIR, \\\"mistral-7b-v0.3\\\", \\\"features_pythia410m.jsonl\\\")),\\n    ]\\n    dfs = [df_base]\\n    for gen_name, path in new_gens:\\n        records = []\\n        with open(path) as f:\\n            for line in f:\\n                rec = json.loads(line)\\n                rec[\\\"model_name\\\"] = gen_name\\n                records.append(rec)\\n        dfs.append(pd.DataFrame(recor
…[truncated 6024 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_corpus-prevalence_20260517T231957",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-17T23:31:25.641465+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/gen-depth-fingerprint/8gen_length_confound.py\\n/root/gen-depth-fingerprint/ablation_analysis.py\\n/root/gen-depth-fingerprint/analyze_7gen_logo.py\\n/root/gen-depth-fingerprint/analyze_instruct.py\\n/root/gen-depth-fingerprint/analyze_prompt_types.py\\n/root/gen-depth-fingerprint/benchmark_efficiency.py\\n/root/gen-depth-fingerprint/bootstrap_ci_plan015.py\\n/root/gen-depth-fingerprint/bootstrap_downstream_ci.py\\n/root/gen-depth-fingerprint/bootstrap_seed_variance.py\\n/root/gen-depth-fingerprint/classify_and_eval.py\\n/root/gen-depth-fingerprint/classify_multi.py\\n/root/gen-depth-fingerprint/compute_binary_baseline.py\\n/root/gen-depth-fingerprint/compute_dataset_stats.py\\n/root/gen-depth-fingerprint/cross_generator_eval.py\\n/root/gen-depth-fingerprint/cross_model_chains.py\\n/root/gen-depth-fingerprint/cross_ref_analysis.py\\n/root/gen-depth-fingerprint/cross_temp_qwen_only.py\\n/root/gen-depth-fingerprint/cross_temp_transfer.py\\n/root/gen-depth-fingerprint/dedup_generations.py\\n/root/gen-depth-fingerprint/detector_baseline.py\\n/root/gen-depth-fingerprint/distributional_tests.py\\n/root/gen-depth-fingerprint/end_to_end_classifier.py\\n/root/gen-depth-fingerprint/end_to_end_classifier_pythia.py\\n/root/gen-depth-fingerprint/end_to_end_classifier_v2.py\\n/root/gen-depth-fingerprint/eval_8gen_baselines.py\\n/root/gen-depth-fingerprint/eval_8gen_baselines_pooled.py\\n/root/gen-depth-fingerprint/eval_8gen_classifier_comparison.py\\n/root/gen-depth-fingerprint/eval_8gen_cross_model_chains.py\\n/root/gen-depth-fingerprint/eval_8gen_finer_depth.py\\n/root/gen-depth-fingerprint/eval_8gen_logo.py\\n/root/gen-depth-fingerprint/eval_8gen_logo_baselines.py\\n/root/gen-depth-fingerprint/eval_8gen_sampling_ablation.py\\n/root/gen-depth-fingerprint/eval_independent_seed.py\\n/root/gen-depth-fingerprint/eval_temp_curve_logo.py\\n/root/gen-depth-fingerprint/extract_confusion_3class.py\\n/root/gen-depth-fingerprin
…[truncated 1638 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_corpus-prevalence_20260517T231957",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-17T23:31:25.641659+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "head -5 /root/gen-depth-fingerprint/data/features_all_models.csv",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_corpus-prevalence_20260517T231957",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "head -5 /root/gen-depth-fingerprint/data/features_all_models.csv",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-17T23:31:25.641806+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"model_name,seed_id,depth,entropy_mean,entropy_std,entropy_min,entropy_max,tail_decay,ttr,hapax_ratio\\npythia-2.8b,0,0,2.7516980171203613,1.744314193725586,0.003396987915039,8.1875,-0.0023380015550609,0.6565656565656566,0.5454545454545454\\npythia-2.8b,0,1,2.616674900054932,1.59860098361969,0.0011329650878906,7.59375,-0.002411389477936,0.5532994923857868,0.4010152284263959\\npythia-2.8b,0,2,2.638378858566284,1.5402252674102783,0.00421142578125,8.03125,-0.0023913172458812,0.3981042654028436,0.2606635071090047\\npythia-2.8b,0,3,0.607209324836731,1.4215928316116333,4.971027374267578e-05,7.37109375,-0.002321573825993,0.088235294117647,0.0147058823529411\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_corpus-prevalence_20260517T231957",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-17T23:31:25.641936+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "ls /root/gen-depth-fingerprint/data/llama-3.2-3b/ /root/gen-depth-fingerprint/data/mistral-7b-v0.3/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_corpus-prevalence_20260517T231957",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "ls /root/gen-depth-fingerprint/data/llama-3.2-3b/ /root/gen-depth-fingerprint/data/mistral-7b-v0.3/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-17T23:31:25.642062+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/gen-depth-fingerprint/data/llama-3.2-3b/:\\nfeatures_olmo2-1b.jsonl\\nfeatures_pythia410m.jsonl\\nfeatures_qwen3-06b.jsonl\\ngenerations_filtered.jsonl\\ngenerations_shard0.jsonl\\n\\n/root/gen-depth-fingerprint/data/mistral-7b-v0.3/:\\nfeatures_olmo2-1b.jsonl\\nfeatures_pythia410m.jsonl\\nfeatures_qwen3-06b.jsonl\\ngenerations_filtered.jsonl\\ngenerations_shard0.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_corpus-prevalence_20260517T231957",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-17T23:31:25.642177+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "ls /root/gen-depth-fingerprint/results/ /root/gen-depth-fingerprint/logs/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_corpus-prevalence_20260517T231957",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "ls /root/gen-depth-fingerprint/results/ /root/gen-depth-fingerprint/logs/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-17T23:31:25.642324+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/gen-depth-fingerprint/logs/:\\nbootstrap_seed_variance.log\\nfeature_importance_stability.log\\ngenerate_chain.log\\nhigh_temp_cuda2.log\\nindep_seed.log\\nllama_rp1.0_resume.log\\nplan012_pythia410m.log\\nplan012_qwen06b.log\\nreview_p1d_6gen_baselines.log\\ntable4_grid.log\\ntc_fix.log\\ntemp_curve_20260518_061706.log\\n\\n/root/gen-depth-fingerprint/results/:\\n8gen_baselines.json\\n8gen_classifier_comparison.json\\n8gen_cross_model_chains.json\\n8gen_feature_ablation.json\\n8gen_finer_depth.json\\n8gen_ldscore_sparse_fixed.json\\n8gen_length_confound.json\\n8gen_lofo_family.json\\n8gen_logo_baselines.json\\n8gen_logo_results.json\\n8gen_logo_results_BUGGY_DO_NOT_USE.json\\n8gen_logo_unfiltered.json\\n8gen_per_gen_spearman.json\\n8gen_pooled_rho.json\\n8gen_sampling_ablation.json\\n8gen_table3_unified.json\\n8gen_table3_v5_unified.json\\n8gen_table3_v6_unified.json\\nREADME.md\\nablation_results.json\\nalt_classifier_results.json\\nbinary_bootstrap_pvalue.json\\nbootstrap_ci_results.json\\nbootstrap_ci_v2_results.json\\nbootstrap_seed_variance.json\\nconfusion_matrix_3class.json\\nconfusion_matrix_results.json\\ncross_model_chains_per_class.json\\ncross_model_chains_results.json\\ncross_temp_transfer.json\\ncross_temp_transfer_qwen_only.json\\ndataset_stats.json\\ndataset_stats_table.tex\\ndegeneration_rates.json\\ndepth_trends.png\\ndistributional_tests.json\\nefficiency_comparison.json\\nfamily_holdout_3class.json\\nfig1_differential_response_v2.pdf\\nfig1_differential_response_v2.png\\nfilter_diagnostic.json\\nfiner_ordinal_results.json\\ngemma_cross_rp_comparison.json\\ngemma_rp11_held_out_logo.json\\nhuman_edit_robustness.json\\nhuman_edit_robustness_old_no_chat_template.json\\ninstruct_length_confound.json\\nlofo_ablation_results.json\\nmulti_classify_results.csv\\nmulti_classify_results.json\\nmulti_domain_results.json\\nmulti_seed_stability.json\\nmvp_results.json\\nn2a_bootstrap_ci.json\\nordi
…[truncated 1206 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_corpus-prevalence_20260517T231957",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-17T23:31:25.642485+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "python3 -c \"\nimport pandas as pd, json, os\nDATA='/root/gen-depth-fingerprint/data'\ndf=pd.read_csv(os.path.join(DATA,'features_all_models.csv'))\nnew_gens=[('llama-3.2-3b',os.path.join(DATA,'llama-3.2-3b','features_pythia410m.jsonl')),('mistral-7b-v0.3',os.path.join(DATA,'mistral-7b-v0.3','features_pythia410m.jsonl'))]\nfor gn,p in new_gens:\n    recs=[]\n    with open(p) as f:\n        for l in f: r=json.loads(l); r['model_name']=gn; recs.append(r)\n    df=pd.concat([df,pd.DataFrame(recs)],ignore_index=True)\nCLASS_MAP={0:0,1:1,2:2,3:2,4:2}\ndf['label']=df['depth'].map(CLASS_MAP)\ndf['binary']=(df['label']>=2).astype(int)\nfor gen in sorted(df['model_name'].unique()):\n    sub=df[df['model_name']==gen]\n    g1=len(sub[sub['label']==1])\n    g2=len(sub[sub['label']>=2])\n    print(f'{gen:20s} total={len(sub):5d}  gen-1={g1:4d}  gen-2+={g2:4d}')\n\"\n",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_corpus-prevalence_20260517T231957",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "python3 -c \"\nimport pandas as pd, json, os\nDATA='/root/gen-depth-fingerprint/data'\ndf=pd.read_csv(os.path.join(DATA,'features_all_models.csv'))\nnew_gens=[('llama-3.2-3b',os.path.join(DATA,'llama-3.2-3b','features_pythia410m.jsonl')),('mistral-7b-v0.3',os.path.join(DATA,'mistral-7b-v0.3','features_pythia410m.jsonl'))]\nfor gn,p in new_gens:\n    recs=[]\n    with open(p) as f:\n        for l in f: r=json.loads(l); r['model_name']=gn; recs.append(r)\n    df=pd.concat([df,pd.DataFrame(recs)],ignore_index=True)\nCLASS_MAP={0:0,1:1,2:2,3:2,4:2}\ndf['label']=df['depth'].map(CLASS_MAP)\ndf['binary']=(df['label']>=2).astype(int)\nfor gen in sorted(df['model_name'].unique()):\n    sub=df[df['model_name']==gen]\n    g1=len(sub[sub['label']==1])\n    g2=len(sub[sub['label']>=2])\n    print(f'{gen:20s} total={len(sub):5d}  gen-1={g1:4d}  gen-2+={g2:4d}')\n\"\n",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-17T23:31:25.642631+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_corpus-prevalence_20260517T231957",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-17T23:31:25.642753+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-5090",
  "command": "cd /root/gen-depth-fingerprint && python3 -c \"\nimport pandas as pd, json, os\nDATA='data'\ndf=pd.read_csv(os.path.join(DATA,'features_all_models.csv'))\nnew_gens=[('llama-3.2-3b',os.path.join(DATA,'llama-3.2-3b','features_pythia410m.jsonl')),('mistral-7b-v0.3',os.path.join(DATA,'mistral-7b-v0.3','features_pythia410m.jsonl'))]\nfor gn,p in new_gens:\n    recs=[]\n    with open(p) as f:\n        for l in f: r=json.loads(l); r['model_name']=gn; recs.append(r)\n    df=pd.concat([df,pd.DataFrame(recs)],ignore_index=True)\nCLASS_MAP={0:0,1:1,2:2,3:2,4:2}\ndf['label']=df['depth'].map(CLASS_MAP)\nfor gen in sorted(df['model_name'].unique()):\n    sub=df[df['model_name']==gen]\n    g1=len(sub[sub['label']==1])\n    g2=len(sub[sub['label']>=2])\n    print(f'{gen:20s} total={len(sub):5d}  gen-1={g1:4d}  gen-2+={g2:4d}')\n\"\n",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_corpus-prevalence_20260517T231957",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cd /root/gen-depth-fingerprint && python3 -c \"\nimport pandas as pd, json, os\nDATA='data'\ndf=pd.read_csv(os.path.join(DATA,'features_all_models.csv'))\nnew_gens=[('llama-3.2-3b',os.path.join(DATA,'llama-3.2-3b','features_pythia410m.jsonl')),('mistral-7b-v0.3',os.path.join(DATA,'mistral-7b-v0.3','features_pythia410m.jsonl'))]\nfor gn,p in new_gens:\n    recs=[]\n    with open(p) as f:\n        for l in f: r=json.loads(l); r['model_name']=gn; recs.append(r)\n    df=pd.concat([df,pd.DataFrame(recs)],ignore_index=True)\nCLASS_MAP={0:0,1:1,2:2,3:2,4:2}\ndf['label']=df['depth'].map(CLASS_MAP)\nfor gen in sorted(df['model_name'].unique()):\n    sub=df[df['model_name']==gen]\n    g1=len(sub[sub['label']==1])\n    g2=len(sub[sub['label']>=2])\n    print(f'{gen:20s} total={len(sub):5d}  gen-1={g1:4d}  gen-2+={g2:4d}')\n\"\n",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-17T23:31:25.642891+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Encountered a bad command exit code!\\n\\nCommand: 'cd /root/gen-depth-fingerprint && python3 -c \\\"\\\\nimport pandas as pd, json, os\\\\nDATA=\\\\'data\\\\'\\\\ndf=pd.read_csv(os.path.join(DATA,\\\\'features_all_models.csv\\\\'))\\\\nnew_gens=[(\\\\'llama-3.2-3b\\\\',os.path.join(DATA,\\\\'llama-3.2-3b\\\\',\\\\'features_pythia410m.jsonl\\\\')),(\\\\'mistral-7b-v0.3\\\\',os.path.join(DATA,\\\\'mistral-7b-v0.3\\\\',\\\\'features_pythia410m.jsonl\\\\'))]\\\\nfor gn,p in new_gens:\\\\n    recs=[]\\\\n    with open(p) as f:\\\\n        for l in f: r=json.loads(l); r[\\\\'model_name\\\\']=gn; recs.append(r)\\\\n    df=pd.concat([df,pd.DataFrame(recs)],ignore_index=True)\\\\nCLASS_MAP={0:0,1:1,2:2,3:2,4:2}\\\\ndf[\\\\'label\\\\']=df[\\\\'depth\\\\'].map(CLASS_MAP)\\\\nfor gen in sorted(df[\\\\'model_name\\\\'].unique()):\\\\n    sub=df[df[\\\\'model_name\\\\']==gen]\\\\n    g1=len(sub[sub[\\\\'label\\\\']==1])\\\\n    g2=len(sub[sub[\\\\'label\\\\']>=2])\\\\n    print(f\\\\'{gen:20s} total={len(sub):5d}  gen-1={g1:4d}  gen-2+={g2:4d}\\\\')\\\\n\\\"\\\\n'\\n\\nExit code: 1\\n\\nStdout:\\n\\n\\n\\nStderr:\\n\\nTraceback (most recent call last):\\n  File \\\"&lt;string>\\\", line 2, in &lt;module>\\nModuleNotFoundError: No module named 'pandas'\\n\\n\", \"metadata\": {\"elapsed_seconds\": 0.31}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_corpus-prevalence_20260517T231957",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-17T23:31:25.643032+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-5090",
  "command": "source /root/miniconda3/bin/activate && cd /root/gen-depth-fingerprint && python3 -c \"\nimport pandas as pd, json, os\nDATA='data'\ndf=pd.read_csv(os.path.join(DATA,'features_all_models.csv'))\nnew_gens=[('llama-3.2-3b',os.path.join(DATA,'llama-3.2-3b','features_pythia410m.jsonl')),('mistral-7b-v0.3',os.path.join(DATA,'mistral-7b-v0.3','features_pythia410m.jsonl'))]\nfor gn,p in new_gens:\n    recs=[]\n    with open(p) as f:\n        for l in f: r=json.loads(l); r['model_name']=gn; recs.append(r)\n    df=pd.concat([df,pd.DataFrame(recs)],ignore_index=True)\nCLASS_MAP={0:0,1:1,2:2,3:2,4:2}\ndf['label']=df['depth'].map(CLASS_MAP)\nfor gen in sorted(df['model_name'].unique()):\n    sub=df[df['model_name']==gen]\n    g1=len(sub[sub['label']==1])\n    g2=len(sub[sub['label']>=2])\n    print(f'{gen:20s} total={len(sub):5d}  gen-1={g1:4d}  gen-2+={g2:4d}')\n\"\n",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_corpus-prevalence_20260517T231957",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-5090",
    "command": "source /root/miniconda3/bin/activate && cd /root/gen-depth-fingerprint && python3 -c \"\nimport pandas as pd, json, os\nDATA='data'\ndf=pd.read_csv(os.path.join(DATA,'features_all_models.csv'))\nnew_gens=[('llama-3.2-3b',os.path.join(DATA,'llama-3.2-3b','features_pythia410m.jsonl')),('mistral-7b-v0.3',os.path.join(DATA,'mistral-7b-v0.3','features_pythia410m.jsonl'))]\nfor gn,p in new_gens:\n    recs=[]\n    with open(p) as f:\n        for l in f: r=json.loads(l); r['model_name']=gn; recs.append(r)\n    df=pd.concat([df,pd.DataFrame(recs)],ignore_index=True)\nCLASS_MAP={0:0,1:1,2:2,3:2,4:2}\ndf['label']=df['depth'].map(CLASS_MAP)\nfor gen in sorted(df['model_name'].unique()):\n    sub=df[df['model_name']==gen]\n    g1=len(sub[sub['label']==1])\n    g2=len(sub[sub['label']>=2])\n    print(f'{gen:20s} total={len(sub):5d}  gen-1={g1:4d}  gen-2+={g2:4d}')\n\"\n",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-17T23:31:25.643247+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"llama-3.2-3b         total= 4680  gen-1= 984  gen-2+=2701\\nmistral-7b-v0.3      total= 4849  gen-1= 994  gen-2+=2859\\nolmo-2-1b            total= 4713  gen-1= 988  gen-2+=2730\\npythia-1b            total= 4555  gen-1= 993  gen-2+=2567\\npythia-2.8b          total= 4609  gen-1= 989  gen-2+=2625\\nqwen3-0.6b           total= 4538  gen-1= 986  gen-2+=2556\\nqwen3-1.7b           total= 4617  gen-1= 983  gen-2+=2638\\nqwen3-8b             total= 4497  gen-1= 979  gen-2+=2523\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.26}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_corpus-prevalence_20260517T231957",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-17T23:31:25.643455+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat > /root/gen-depth-fingerprint/corpus_prevalence_demo.py << 'PYEOF'\n\"\"\"\ncorpus_prevalence_demo.py — Corpus-level depth prevalence estimation.\n\nBuild 5 synthetic corpora with known depth-2+ proportions (0%, 25%, 50%, 75%, 100%),\npredict per-document depth with LOGO-trained XGBoost, compare predicted vs true\ncorpus-level proportions. Report calibration error (MAE).\n\"\"\"\n\nimport json\nimport os\nimport numpy as np\nimport pandas as pd\nfrom xgboost import XGBClassifier\nfrom sklearn.metrics import f1_score\nimport matplotlib\nmatplotlib.use(\"Agg\")\nimport matplotlib.pyplot as plt\n\nSEED = 42\nFEATURES = [\"entropy_mean\", \"entropy_std\", \"entropy_min\", \"entropy_max\",\n            \"tail_decay\", \"ttr\", \"hapax_ratio\"]\n\nXGB_PARAMS = dict(n_estimators=200, max_depth=6, learning_rate=0.1,\n                  random_state=SEED, eval_metric=\"mlogloss\",\n                  use_label_encoder=False)\n\nCLASS_MAP_3 = {0: 0, 1: 1, 2: 2, 3: 2, 4: 2}\n\nROOT = os.path.dirname(os.path.abspath(__file__))\nDATA_DIR = os.path.join(ROOT, \"data\")\nRESULTS_DIR = os.path.join(ROOT, \"results\")\n\nCORPUS_SIZE = 800\nTRUE_PROPORTIONS = [0.0, 0.25, 0.50, 0.75, 1.00]\nN_BOOTSTRAP = 200\n\n\ndef load_data():\n    df_base = pd.read_csv(os.path.join(DATA_DIR, \"features_all_models.csv\"))\n    new_gens = [\n        (\"llama-3.2-3b\", os.path.join(DATA_DIR, \"llama-3.2-3b\", \"features_pythia410m.jsonl\")),\n        (\"mistral-7b-v0.3\", os.path.join(DATA_DIR, \"mistral-7b-v0.3\", \"features_pythia410m.jsonl\")),\n    ]\n    dfs = [df_base]\n    for gen_name, path in new_gens:\n        records = []\n        with open(path) as f:\n            for line in f:\n                rec = json.loads(line)\n                rec[\"model_name\"] = gen_name\n                records.append(rec)\n        dfs.append(pd.DataFrame(records))\n\n    cols = [\"model_name\", \"seed_id\", \"depth\"] + FEATURES\n    df = pd.concat([d[cols] for d in dfs], ignore_index=True)\n    df[\"label\"] = df[\"depth\"].map(CLASS_MAP_3)\n    return df\n\n\ndef downsample(df, label_col, rng):\n    counts = df[label_col].value_counts()\n    min_n = counts.min()\n    parts = []\n    for lbl in sorted(counts.index):\n        sub = df[df[label_col] == lbl]\n        parts.append(sub.sample(n=min_n, random_state=rng, replace=False))\n    return pd.concat(parts, ignore_index=True)\n\n\ndef run_prevalence_estimation(df):\n    generators = sorted(df[\"model_name\"].unique())\n    rng = np.random.RandomState(SEED)\n\n    all_gen_results = {}\n\n    for gen in generators:\n        print(f\"\\n--- Held-out generator: {gen} ---\")\n        test_df = df[df[\"model_name\"] == gen].copy()\n        train_df = df[df[\"model_name\"] != gen].copy()\n\n        # Binary: gen-1 vs gen-2+, exclude gen-0\n        train_bin = train_df[train_df[\"label\"] >= 1].copy()\n        train_bin[\"binary\"] = (train_bin[\"label\"] >= 2).astype(int)\n        test_bin = test_df[test_df[\"label\"] >= 1].copy()\n        test_bin[\"binary\"] = (test_bin[\"label\"] >= 2).astype(int)\n\n        train_ds = downsample(train_bin, \"binary\", rng)\n        clf = XGBClassifier(**XGB_PARAMS)\n        clf.fit(train_ds[FEATURES].values, train_ds[\"binary\"].values)\n\n        # Per-document accuracy on held-out gen\n        y_pred_all = clf.predict(test_bin[FEATURES].values)\n        y_true_all = test_bin[\"binary\"].values\n        doc_f1 = f1_score(y_true_all, y_pred_all, average=\"macro\")\n        print(f\"  Per-document binary F1: {doc_f1:.4f}\")\n\n        gen1_pool = test_bin[test_bin[\"binary\"] == 0]\n        gen2_pool = test_bin[test_bin[\"binary\"] == 1]\n\n        n_gen1 = len(gen1_pool)\n        n_gen2 = len(gen2_pool)\n        print(f\"  Pool sizes: gen-1={n_gen1}, gen-2+={n_gen2}\")\n\n        corpus_results = []\n        for true_prop in TRUE_PROPORTIONS:\n            n_pos = int(round(CORPUS_SIZE * true_prop))\n            n_neg = CORPUS_SIZE - n_pos\n\n            if n_neg > n_gen1 or n_pos > n_gen2:\n                print(f\"  [SKIP] prop={true_prop:.0%}: need {n_neg} gen-1 and {n_pos} gen-2+, have {n_gen1}/{n_gen2}\")\n                continue\n\n            # Bootstrap: resample corpora many times\n            boot_props = []\n            for b in range(N_BOOTSTRAP):\n                brng = np.random.RandomState(SEED + b)\n                sample_neg = gen1_pool.sample(n=n_neg, random_state=brng, replace=True)\n                sample_pos = gen2_pool.sample(n=n_pos, random_state=brng, replace=True)\n                corpus = pd.concat([sample_neg, sample_pos], ignore_index=True)\n\n                preds = clf.predict(corpus[FEATURES].values)\n                pred_prop = float(preds.sum()) / len(preds)\n                boot_props.append(pred_prop)\n\n            boot_arr = np.array(boot_props)\n            pred_mean = float(np.mean(boot_arr))\n            ci_lo = float(np.percentile(boot_arr, 2.5))\n            ci_hi = float(np.percentile(boot_arr, 97.5))\n            error = abs(pred_mean - true_prop)\n\n            corpus_results.append({\n                \"true_prop\": true_prop,\n                \"pred_prop\": round(pred_mean, 4),\n                \"error_pp\": round(error * 100, 2),\n                \"ci_lo\": round(ci_lo, 4),\n                \"ci_hi\": round(ci_hi, 4),\n            })\n            print(f\"  true={true_prop:.0%}  pred={pred_mean:.4f}  |err|={error*100:.2f}pp  \"\n                  f\"95%CI=[{ci_lo:.4f}, {ci_hi:.4f}]\")\n\n        all_gen_results[gen] = {\n            \"doc_f1\": round(doc_f1, 4),\n            \"corpora\": corpus_results,\n        }\n\n    return all_gen_results\n\n\ndef aggregate_results(all_gen_results):\n    # Average across generators for each true_prop\n    prop_errors = {p: [] for p in TRUE_PROPORTIONS}\n    prop_preds = {p: [] for p in TRUE_PROPORTIONS}\n    prop_ci_lo = {p: [] for p in TRUE_PROPORTIONS}\n    prop_ci_hi = {p: [] for p in TRUE_PROPORTIONS}\n\n    for gen, res in all_gen_results.items():\n        for c in res[\"corpora\"]:\n            tp = c[\"true_prop\"]\n            prop_errors[tp].append(c[\"error_pp\"])\n            prop_preds[tp].append(c[\"pred_prop\"])\n            prop_ci_lo[tp].append(c[\"ci_lo\"])\n            prop_ci_hi[tp].append(c[\"ci_hi\"])\n\n    agg = []\n    for tp in TRUE_PROPORTIONS:\n        if not prop_errors[tp]:\n            continue\n        agg.append({\n            \"true_prop\": tp,\n            \"pred_prop_mean\": round(float(np.mean(prop_preds[tp])), 4),\n            \"pred_prop_std\": round(float(np.std(prop_preds[tp])), 4),\n            \"error_pp_mean\": round(float(np.mean(prop_errors[tp])), 2),\n            \"error_pp_std\": round(float(np.std(prop_errors[tp])), 2),\n            \"ci_lo_mean\": round(float(np.mean(prop_ci_lo[tp])), 4),\n            \"ci_hi_mean\": round(float(np.mean(prop_ci_hi[tp])), 4),\n        })\n\n    overall_mae = float(np.mean([a[\"error_pp_mean\"] for a in agg]))\n    return agg, round(overall_mae, 2)\n\n\ndef plot_calibration(agg, all_gen_results, mae, out_path):\n    fig, ax = plt.subplots(figsize=(5, 5))\n\n    # Per-generator points (faded)\n    for gen, res in all_gen_results.items():\n        xs = [c[\"true_prop\"] * 100 for c in res[\"corpora\"]]\n        ys = [c[\"pred_prop\"] * 100 for c in res[\"corpora\"]]\n        ax.scatter(xs, ys, alpha=0.2, s=20, color=\"steelblue\", zorder=2)\n\n    # Averaged points with error bars\n    true_pcts = [a[\"true_prop\"] * 100 for a in agg]\n    pred_pcts = [a[\"pred_prop_mean\"] * 100 for a in agg]\n    ci_lo = [a[\"ci_lo_mean\"] * 100 for a in agg]\n    ci_hi = [a[\"ci_hi_mean\"] * 100 for a in agg]\n    yerr_lo = [p - lo for p, lo in zip(pred_pcts, ci_lo)]\n    yerr_hi = [hi - p for p, hi in zip(pred_pcts, ci_hi)]\n\n    ax.errorbar(true_pcts, pred_pcts, yerr=[yerr_lo, yerr_hi],\n                fmt=\"o\", color=\"darkblue\", capsize=4, capthick=1.5,\n                markersize=8, zorder=3, label=f\"Mean across 8 generators\")\n\n    # Diagonal\n    ax.plot([0, 100], [0, 100], \"k--\", alpha=0.5, linewidth=1, label=\"Perfect calibration\")\n\n    ax.set_xlabel(\"True depth-2+ proportion (%)\", fontsize=12)\n    ax.set_ylabel(\"Predicted depth-2+ proportion (%)\", fontsize=12)\n    ax.set_xlim(-5, 105)\n    ax.set_ylim(-5, 105)\n    ax.set_aspect(\"equal\")\n    ax.legend(loc=\"upper left\", fontsize=10)\n    ax.set_title(f\"Corpus Prevalence Calibration (MAE = {mae:.1f}pp)\", fontsize=13)\n\n    plt.tight_layout()\n    plt.savefig(out_path, dpi=300, bbox_inches=\"tight\")\n    plt.savefig(out_path.replace(\".pdf\", \".png\"), dpi=150, bbox_inches=\"tight\")\n    print(f\"\\nSaved: {out_path}\")\n\n\ndef main():\n    os.makedirs(RESULTS_DIR, exist_ok=True)\n\n    print(\"Loading 8-gen data...\")\n    df = load_data()\n    print(f\"Loaded {len(df)} rows, {df['model_name'].nunique()} generators\")\n\n    all_gen_results = run_prevalence_estimation(df)\n\n    agg, mae = aggregate_results(all_gen_results)\n\n    print(\"\\n\" + \"=\" * 60)\n    print(\"AGGREGATED RESULTS (averaged across 8 held-out generators)\")\n    print(\"=\" * 60)\n    print(f\"{'True %':>8s}  {'Pred %':>8s}  {'|Error|':>8s}  {'95% CI':>20s}\")\n    for a in agg:\n        print(f\"{a['true_prop']*100:7.0f}%  {a['pred_prop_mean']*100:7.1f}%  \"\n              f\"{a['error_pp_mean']:7.2f}pp  \"\n              f\"[{a['ci_lo_mean']*100:.1f}%, {a['ci_hi_mean']*100:.1f}%]\")\n    print(f\"\\nOverall MAE = {mae:.2f}pp\")\n\n    viable = mae < 5.0\n    conclusion = \"viable\" if viable else \"not viable\"\n    print(f\"Conclusion: corpus-level depth auditing is {conclusion} (MAE {'<' if viable else '>='} 5pp)\")\n\n    # Save JSON\n    out = {\n        \"corpus_size\": CORPUS_SIZE,\n        \"n_bootstrap\": N_BOOTSTRAP,\n        \"n_generators\": len(all_gen_results),\n        \"per_generator\": all_gen_results,\n        \"aggregated\": agg,\n        \"overall_mae_pp\": mae,\n        \"conclusion\": conclusion,\n    }\n    json_path = os.path.join(RESULTS_DIR, \"corpus_prevalence_demo.json\")\n    with open(json_path, \"w\") as f:\n        json.dump(out, f, indent=2)\n    print(f\"Saved: {json_path}\")\n\n    # Plot\n    pdf_path = os.path.join(RESULTS_DIR, \"corpus_prevalence_calibration.pdf\")\n    plot_calibration(agg, all_gen_results, mae, pdf_path)\n\n\nif __name__ == \"__main__\":\n    main()\nPYEOF\necho \"Script written.\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_corpus-prevalence_20260517T231957",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat > /root/gen-depth-fingerprint/corpus_prevalence_demo.py << 'PYEOF'\n\"\"\"\ncorpus_prevalence_demo.py — Corpus-level depth prevalence estimation.\n\nBuild 5 synthetic corpora with known depth-2+ proportions (0%, 25%, 50%, 75%, 100%),\npredict per-document depth with LOGO-trained XGBoost, compare predicted vs true\ncorpus-level proportions. Report calibration error (MAE).\n\"\"\"\n\nimport json\nimport os\nimport numpy as np\nimport pandas as pd\nfrom xgboost import XGBClassifier\nfrom sklearn.metrics import f1_score\nimport matplotlib\nmatplotlib.use(\"Agg\")\nimport matplotlib.pyplot as plt\n\nSEED = 42\nFEATURES = [\"entropy_mean\", \"entropy_std\", \"entropy_min\", \"entropy_max\",\n            \"tail_decay\", \"ttr\", \"hapax_ratio\"]\n\nXGB_PARAMS = dict(n_estimators=200, max_depth=6, learning_rate=0.1,\n                  random_state=SEED, eval_metric=\"mlogloss\",\n                  use_label_encoder=False)\n\nCLASS_MAP_3 = {0: 0, 1: 1, 2: 2, 3: 2, 4: 2}\n\nROOT = os.path.dirname(os.path.abspath(__file__))\nDATA_DIR = os.path.join(ROOT, \"data\")\nRESULTS_DIR = os.path.join(ROOT, \"results\")\n\nCORPUS_SIZE = 800\nTRUE_PROPORTIONS = [0.0, 0.25, 0.50, 0.75, 1.00]\nN_BOOTSTRAP = 200\n\n\ndef load_data():\n    df_base = pd.read_csv(os.path.join(DATA_DIR, \"features_all_models.csv\"))\n    new_gens = [\n        (\"llama-3.2-3b\", os.path.join(DATA_DIR, \"llama-3.2-3b\", \"features_pythia410m.jsonl\")),\n        (\"mistral-7b-v0.3\", os.path.join(DATA_DIR, \"mistral-7b-v0.3\", \"features_pythia410m.jsonl\")),\n    ]\n    dfs = [df_base]\n    for gen_name, path in new_gens:\n        records = []\n        with open(path) as f:\n            for line in f:\n                rec = json.loads(line)\n                rec[\"model_name\"] = gen_name\n                records.append(rec)\n        dfs.append(pd.DataFrame(records))\n\n    cols = [\"model_name\", \"seed_id\", \"depth\"] + FEATURES\n    df = pd.concat([d[cols] for d in dfs], ignore_index=True)\n    df[\"label\"] = df[\"depth\"].map(CLASS_MAP_3)\n    return df\n\n\ndef downsample(df, label_col, rng):\n    counts = df[label_col].value_counts()\n    min_n = counts.min()\n    parts = []\n    for lbl in sorted(counts.index):\n        sub = df[df[label_col] == lbl]\n        parts.append(sub.sample(n=min_n, random_state=rng, replace=False))\n    return pd.concat(parts, ignore_index=True)\n\n\ndef run_prevalence_estimation(df):\n    generators = sorted(df[\"model_name\"].unique())\n    rng = np.random.RandomState(SEED)\n\n    all_gen_results = {}\n\n    for gen in generators:\n        print(f\"\\n--- Held-out generator: {gen} ---\")\n        test_df = df[df[\"model_name\"] == gen].copy()\n        train_df = df[df[\"model_name\"] != gen].copy()\n\n        # Binary: gen-1 vs gen-2+, exclude gen-0\n        train_bin = train_df[train_df[\"label\"] >= 1].copy()\n        train_bin[\"binary\"] = (train_bin[\"label\"] >= 2).astype(int)\n        test_bin = test_df[test_df[\"label\"] >= 1].copy()\n        test_bin[\"binary\"] = (test_bin[\"label\"] >= 2).astype(int)\n\n        train_ds = downsample(train_bin, \"binary\", rng)\n        clf = XGBClassifier(**XGB_PARAMS)\n        clf.fit(train_ds[FEATURES].values, train_ds[\"binary\"].values)\n\n        # Per-document accuracy on held-out gen\n        y_pred_all = clf.predict(test_bin[FEATURES].values)\n        y_true_all = test_bin[\"binary\"].values\n        doc_f1 = f1_score(y_true_all, y_pred_all, average=\"macro\")\n        print(f\"  Per-document binary F1: {doc_f1:.4f}\")\n\n        gen1_pool = test_bin[test_bin[\"binary\"] == 0]\n        gen2_pool = test_bin[test_bin[\"binary\"] == 1]\n\n        n_gen1 = len(gen1_pool)\n        n_gen2 = len(gen2_pool)\n        print(f\"  Pool sizes: gen-1={n_gen1}, gen-2+={n_gen2}\")\n\n        corpus_results = []\n        for true_prop in TRUE_PROPORTIONS:\n            n_pos = int(round(CORPUS_SIZE * true_prop))\n            n_neg = CORPUS_SIZE - n_pos\n\n            if n_neg > n_gen1 or n_pos > n_gen2:\n                print(f\"  [SKIP] prop={true_prop:.0%}: need {n_neg} gen-1 and {n_pos} gen-2+, have {n_gen1}/{n_gen2}\")\n                continue\n\n            # Bootstrap: resample corpora many times\n            boot_props = []\n            for b in range(N_BOOTSTRAP):\n                brng = np.random.RandomState(SEED + b)\n                sample_neg = gen1_pool.sample(n=n_neg, random_state=brng, replace=True)\n                sample_pos = gen2_pool.sample(n=n_pos, random_state=brng, replace=True)\n                corpus = pd.concat([sample_neg, sample_pos], ignore_index=True)\n\n                preds = clf.predict(corpus[FEATURES].values)\n                pred_prop = float(preds.sum()) / len(preds)\n                boot_props.append(pred_prop)\n\n            boot_arr = np.array(boot_props)\n            pred_mean = float(np.mean(boot_arr))\n            ci_lo = float(np.percentile(boot_arr, 2.5))\n            ci_hi = float(np.percentile(boot_arr, 97.5))\n            error = abs(pred_mean - true_prop)\n\n            corpus_results.append({\n                \"true_prop\": true_prop,\n                \"pred_prop\": round(pred_mean, 4),\n                \"error_pp\": round(error * 100, 2),\n                \"ci_lo\": round(ci_lo, 4),\n                \"ci_hi\": round(ci_hi, 4),\n            })\n            print(f\"  true={true_prop:.0%}  pred={pred_mean:.4f}  |err|={error*100:.2f}pp  \"\n                  f\"95%CI=[{ci_lo:.4f}, {ci_hi:.4f}]\")\n\n        all_gen_results[gen] = {\n            \"doc_f1\": round(doc_f1, 4),\n            \"corpora\": corpus_results,\n        }\n\n    return all_gen_results\n\n\ndef aggregate_results(all_gen_results):\n    # Average across generators for each true_prop\n    prop_errors = {p: [] for p in TRUE_PROPORTIONS}\n    prop_preds = {p: [] for p in TRUE_PROPORTIONS}\n    prop_ci_lo = {p: [] for p in TRUE_PROPORTIONS}\n    prop_ci_hi = {p: [] for p in TRUE_PROPORTIONS}\n\n    for gen, res in all_gen_results.items():\n        for c in res[\"corpora\"]:\n            tp = c[\"true_prop\"]\n            prop_errors[tp].append(c[\"error_pp\"])\n            prop_preds[tp].append(c[\"pred_prop\"])\n            prop_ci_lo[tp].append(c[\"ci_lo\"])\n            prop_ci_hi[tp].append(c[\"ci_hi\"])\n\n    agg = []\n    for tp in TRUE_PROPORTIONS:\n        if not prop_errors[tp]:\n            continue\n        agg.append({\n            \"true_prop\": tp,\n            \"pred_prop_mean\": round(float(np.mean(prop_preds[tp])), 4),\n            \"pred_prop_std\": round(float(np.std(prop_preds[tp])), 4),\n            \"error_pp_mean\": round(float(np.mean(prop_errors[tp])), 2),\n            \"error_pp_std\": round(float(np.std(prop_errors[tp])), 2),\n            \"ci_lo_mean\": round(float(np.mean(prop_ci_lo[tp])), 4),\n            \"ci_hi_mean\": round(float(np.mean(prop_ci_hi[tp])), 4),\n        })\n\n    overall_mae = float(np.mean([a[\"error_pp_mean\"] for a in agg]))\n    return agg, round(overall_mae, 2)\n\n\ndef plot_calibration(agg, all_gen_results, mae, out_path):\n    fig, ax = plt.subplots(figsize=(5, 5))\n\n    # Per-generator points (faded)\n    for gen, res in all_gen_results.items():\n        xs = [c[\"true_prop\"] * 100 for c in res[\"corpora\"]]\n        ys = [c[\"pred_prop\"] * 100 for c in res[\"corpora\"]]\n        ax.scatter(xs, ys, alpha=0.2, s=20, color=\"steelblue\", zorder=2)\n\n    # Averaged points with error bars\n    true_pcts = [a[\"true_prop\"] * 100 for a in agg]\n    pred_pcts = [a[\"pred_prop_mean\"] * 100 for a in agg]\n    ci_lo = [a[\"ci_lo_mean\"] * 100 for a in agg]\n    ci_hi = [a[\"ci_hi_mean\"] * 100 for a in agg]\n    yerr_lo = [p - lo for p, lo in zip(pred_pcts, ci_lo)]\n    yerr_hi = [hi - p for p, hi in zip(pred_pcts, ci_hi)]\n\n    ax.errorbar(true_pcts, pred_pcts, yerr=[yerr_lo, yerr_hi],\n                fmt=\"o\", color=\"darkblue\", capsize=4, capthick=1.5,\n                markersize=8, zorder=3, label=f\"Mean across 8 generators\")\n\n    # Diagonal\n    ax.plot([0, 100], [0, 100], \"k--\", alpha=0.5, linewidth=1, label=\"Perfect calibration\")\n\n    ax.set_xlabel(\"True depth-2+ proportion (%)\", fontsize=12)\n    ax.set_ylabel(\"Predicted depth-2+ proportion (%)\", fontsize=12)\n    ax.set_xlim(-5, 105)\n    ax.set_ylim(-5, 105)\n    ax.set_aspect(\"equal\")\n    ax.legend(loc=\"upper left\", fontsize=10)\n    ax.set_title(f\"Corpus Prevalence Calibration (MAE = {mae:.1f}pp)\", fontsize=13)\n\n    plt.tight_layout()\n    plt.savefig(out_path, dpi=300, bbox_inches=\"tight\")\n    plt.savefig(out_path.replace(\".pdf\", \".png\"), dpi=150, bbox_inches=\"tight\")\n    print(f\"\\nSaved: {out_path}\")\n\n\ndef main():\n    os.makedirs(RESULTS_DIR, exist_ok=True)\n\n    print(\"Loading 8-gen data...\")\n    df = load_data()\n    print(f\"Loaded {len(df)} rows, {df['model_name'].nunique()} generators\")\n\n    all_gen_results = run_prevalence_estimation(df)\n\n    agg, mae = aggregate_results(all_gen_results)\n\n    print(\"\\n\" + \"=\" * 60)\n    print(\"AGGREGATED RESULTS (averaged across 8 held-out generators)\")\n    print(\"=\" * 60)\n    print(f\"{'True %':>8s}  {'Pred %':>8s}  {'|Error|':>8s}  {'95% CI':>20s}\")\n    for a in agg:\n        print(f\"{a['true_prop']*100:7.0f}%  {a['pred_prop_mean']*100:7.1f}%  \"\n              f\"{a['error_pp_mean']:7.2f}pp  \"\n              f\"[{a['ci_lo_mean']*100:.1f}%, {a['ci_hi_mean']*100:.1f}%]\")\n    print(f\"\\nOverall MAE = {mae:.2f}pp\")\n\n    viable = mae < 5.0\n    conclusion = \"viable\" if viable else \"not viable\"\n    print(f\"Conclusion: corpus-level depth auditing is {conclusion} (MAE {'<' if viable else '>='} 5pp)\")\n\n    # Save JSON\n    out = {\n        \"corpus_size\": CORPUS_SIZE,\n        \"n_bootstrap\": N_BOOTSTRAP,\n        \"n_generators\": len(all_gen_results),\n        \"per_generator\": all_gen_results,\n        \"aggregated\": agg,\n        \"overall_mae_pp\": mae,\n        \"conclusion\": conclusion,\n    }\n    json_path = os.path.join(RESULTS_DIR, \"corpus_prevalence_demo.json\")\n    with open(json_path, \"w\") as f:\n        json.dump(out, f, indent=2)\n    print(f\"Saved: {json_path}\")\n\n    # Plot\n    pdf_path = os.path.join(RESULTS_DIR, \"corpus_prevalence_calibration.pdf\")\n    plot_calibration(agg, all_gen_results, mae, pdf_path)\n\n\nif __name__ == \"__main__\":\n    main()\nPYEOF\necho \"Script written.\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-17T23:31:25.643725+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Script written.\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.32}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_corpus-prevalence_20260517T231957",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-17T23:31:25.643864+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-5090",
  "command": "source /root/miniconda3/bin/activate && cd /root/gen-depth-fingerprint && mkdir -p logs && python corpus_prevalence_demo.py 2>&1 | tee logs/corpus_prevalence_demo.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_corpus-prevalence_20260517T231957",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-5090",
    "command": "source /root/miniconda3/bin/activate && cd /root/gen-depth-fingerprint && mkdir -p logs && python corpus_prevalence_demo.py 2>&1 | tee logs/corpus_prevalence_demo.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-17T23:31:25.644033+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/miniconda3/lib/python3.12/site-packages/xgboost/training.py:200: UserWarning: [07:22:11] WARNING: /__w/xgboost/xgboost/src/learner.cc:782: \\nParameters: { \\\"use_label_encoder\\\" } are not used.\\n\\n  bst.update(dtrain, iteration=i, fobj=obj)\\n/root/miniconda3/lib/python3.12/site-packages/xgboost/training.py:200: UserWarning: [07:22:13] WARNING: /__w/xgboost/xgboost/src/learner.cc:782: \\nParameters: { \\\"use_label_encoder\\\" } are not used.\\n\\n  bst.update(dtrain, iteration=i, fobj=obj)\\n/root/miniconda3/lib/python3.12/site-packages/xgboost/training.py:200: UserWarning: [07:22:15] WARNING: /__w/xgboost/xgboost/src/learner.cc:782: \\nParameters: { \\\"use_label_encoder\\\" } are not used.\\n\\n  bst.update(dtrain, iteration=i, fobj=obj)\\n/root/miniconda3/lib/python3.12/site-packages/xgboost/training.py:200: UserWarning: [07:22:17] WARNING: /__w/xgboost/xgboost/src/learner.cc:782: \\nParameters: { \\\"use_label_encoder\\\" } are not used.\\n\\n  bst.update(dtrain, iteration=i, fobj=obj)\\n/root/miniconda3/lib/python3.12/site-packages/xgboost/training.py:200: UserWarning: [07:22:19] WARNING: /__w/xgboost/xgboost/src/learner.cc:782: \\nParameters: { \\\"use_label_encoder\\\" } are not used.\\n\\n  bst.update(dtrain, iteration=i, fobj=obj)\\n/root/miniconda3/lib/python3.12/site-packages/xgboost/training.py:200: UserWarning: [07:22:21] WARNING: /__w/xgboost/xgboost/src/learner.cc:782: \\nParameters: { \\\"use_label_encoder\\\" } are not used.\\n\\n  bst.update(dtrain, iteration=i, fobj=obj)\\n/root/miniconda3/lib/python3.12/site-packages/xgboost/training.py:200: UserWarning: [07:22:23] WARNING: /__w/xgboost/xgboost/src/learner.cc:782: \\nParameters: { \\\"use_label_encoder\\\" } are not used.\\n\\n  bst.update(dtrain, iteration=i, fobj=obj)\\n/root/miniconda3/lib/python3.12/site-packages/xgboost/training.py:200: UserWarning: [07:22:25] WARNING: /__w/xgboost/xgboost/src/learner.cc:782: \\nParameters:
…[truncated 4524 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_corpus-prevalence_20260517T231957",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-17T23:31:25.644255+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat > /root/gen-depth-fingerprint/corpus_prevalence_demo.py << 'PYEOF'\n\"\"\"\ncorpus_prevalence_demo.py — Corpus-level depth prevalence estimation.\n\nBuild 5 synthetic corpora with known depth-2+ proportions (0%, 25%, 50%, 75%, 100%).\nUse LOGO-trained XGBoost + Adjusted Classify-and-Count (ACC) to estimate corpus-level\ndepth-2+ prevalence. Compare predicted vs true proportions, report calibration MAE.\n\"\"\"\n\nimport json\nimport os\nimport numpy as np\nimport pandas as pd\nfrom xgboost import XGBClassifier\nfrom sklearn.metrics import confusion_matrix\nimport matplotlib\nmatplotlib.use(\"Agg\")\nimport matplotlib.pyplot as plt\n\nSEED = 42\nFEATURES = [\"entropy_mean\", \"entropy_std\", \"entropy_min\", \"entropy_max\",\n            \"tail_decay\", \"ttr\", \"hapax_ratio\"]\n\nXGB_PARAMS = dict(n_estimators=200, max_depth=6, learning_rate=0.1,\n                  random_state=SEED, eval_metric=\"mlogloss\",\n                  use_label_encoder=False)\n\nCLASS_MAP_3 = {0: 0, 1: 1, 2: 2, 3: 2, 4: 2}\n\nROOT = os.path.dirname(os.path.abspath(__file__))\nDATA_DIR = os.path.join(ROOT, \"data\")\nRESULTS_DIR = os.path.join(ROOT, \"results\")\n\nCORPUS_SIZE = 800\nTRUE_PROPORTIONS = [0.0, 0.25, 0.50, 0.75, 1.00]\nN_BOOTSTRAP = 200\n\n\ndef load_data():\n    df_base = pd.read_csv(os.path.join(DATA_DIR, \"features_all_models.csv\"))\n    new_gens = [\n        (\"llama-3.2-3b\", os.path.join(DATA_DIR, \"llama-3.2-3b\", \"features_pythia410m.jsonl\")),\n        (\"mistral-7b-v0.3\", os.path.join(DATA_DIR, \"mistral-7b-v0.3\", \"features_pythia410m.jsonl\")),\n    ]\n    dfs = [df_base]\n    for gen_name, path in new_gens:\n        records = []\n        with open(path) as f:\n            for line in f:\n                rec = json.loads(line)\n                rec[\"model_name\"] = gen_name\n                records.append(rec)\n        dfs.append(pd.DataFrame(records))\n\n    cols = [\"model_name\", \"seed_id\", \"depth\"] + FEATURES\n    df = pd.concat([d[cols] for d in dfs], ignore_index=True)\n    df[\"label\"] = df[\"depth\"].map(CLASS_MAP_3)\n    return df\n\n\ndef downsample(df, label_col, rng):\n    counts = df[label_col].value_counts()\n    min_n = counts.min()\n    parts = []\n    for lbl in sorted(counts.index):\n        sub = df[df[label_col] == lbl]\n        parts.append(sub.sample(n=min_n, random_state=rng, replace=False))\n    return pd.concat(parts, ignore_index=True)\n\n\ndef estimate_tpr_fpr_cv(train_df, features, n_folds=5, seed=42):\n    \"\"\"Estimate TPR and FPR via cross-validation on training data.\"\"\"\n    rng = np.random.RandomState(seed)\n    indices = np.arange(len(train_df))\n    rng.shuffle(indices)\n    folds = np.array_split(indices, n_folds)\n\n    all_y_true, all_y_pred = [], []\n    for i in range(n_folds):\n        val_idx = folds[i]\n        train_idx = np.concatenate([folds[j] for j in range(n_folds) if j != i])\n\n        tr = train_df.iloc[train_idx]\n        va = train_df.iloc[val_idx]\n\n        tr_ds = downsample(tr, \"binary\", rng)\n        clf = XGBClassifier(**XGB_PARAMS)\n        clf.fit(tr_ds[features].values, tr_ds[\"binary\"].values)\n        preds = clf.predict(va[features].values)\n\n        all_y_true.extend(va[\"binary\"].values)\n        all_y_pred.extend(preds)\n\n    all_y_true = np.array(all_y_true)\n    all_y_pred = np.array(all_y_pred)\n    tn, fp, fn, tp = confusion_matrix(all_y_true, all_y_pred).ravel()\n    tpr = tp / (tp + fn)\n    fpr = fp / (fp + tn)\n    return tpr, fpr\n\n\ndef acc_correct(predicted_prevalence, tpr, fpr):\n    \"\"\"Adjusted Classify-and-Count: correct prevalence using TPR/FPR.\"\"\"\n    denom = tpr - fpr\n    if abs(denom) < 1e-6:\n        return predicted_prevalence\n    corrected = (predicted_prevalence - fpr) / denom\n    return np.clip(corrected, 0.0, 1.0)\n\n\ndef run_prevalence_estimation(df):\n    generators = sorted(df[\"model_name\"].unique())\n    rng = np.random.RandomState(SEED)\n\n    all_gen_results = {}\n\n    for gen in generators:\n        print(f\"\\n--- Held-out generator: {gen} ---\")\n        test_df = df[df[\"model_name\"] == gen].copy()\n        train_df = df[df[\"model_name\"] != gen].copy()\n\n        # Binary: gen-1 vs gen-2+, exclude gen-0\n        train_bin = train_df[train_df[\"label\"] >= 1].copy()\n        train_bin[\"binary\"] = (train_bin[\"label\"] >= 2).astype(int)\n        test_bin = test_df[test_df[\"label\"] >= 1].copy()\n        test_bin[\"binary\"] = (test_bin[\"label\"] >= 2).astype(int)\n\n        # Estimate TPR/FPR via CV on training data\n        tpr, fpr = estimate_tpr_fpr_cv(train_bin, FEATURES, n_folds=5, seed=SEED)\n        print(f\"  CV-estimated TPR={tpr:.4f}, FPR={fpr:.4f}\")\n\n        # Train final classifier on all training data\n        train_ds = downsample(train_bin, \"binary\", rng)\n        clf = XGBClassifier(**XGB_PARAMS)\n        clf.fit(train_ds[FEATURES].values, train_ds[\"binary\"].values)\n\n        gen1_pool = test_bin[test_bin[\"binary\"] == 0]\n        gen2_pool = test_bin[test_bin[\"binary\"] == 1]\n        n_gen1 = len(gen1_pool)\n        n_gen2 = len(gen2_pool)\n        print(f\"  Pool sizes: gen-1={n_gen1}, gen-2+={n_gen2}\")\n\n        corpus_results = []\n        for true_prop in TRUE_PROPORTIONS:\n            n_pos = int(round(CORPUS_SIZE * true_prop))\n            n_neg = CORPUS_SIZE - n_pos\n\n            if n_neg > n_gen1 or n_pos > n_gen2:\n                print(f\"  [SKIP] prop={true_prop:.0%}\")\n                continue\n\n            boot_naive = []\n            boot_acc = []\n            for b in range(N_BOOTSTRAP):\n                brng = np.random.RandomState(SEED + b)\n                sample_neg = gen1_pool.sample(n=n_neg, random_state=brng, replace=True)\n                sample_pos = gen2_pool.sample(n=n_pos, random_state=brng, replace=True)\n                corpus = pd.concat([sample_neg, sample_pos], ignore_index=True)\n\n                preds = clf.predict(corpus[FEATURES].values)\n                naive_prop = float(preds.sum()) / len(preds)\n                corrected_prop = float(acc_correct(naive_prop, tpr, fpr))\n\n                boot_naive.append(naive_prop)\n                boot_acc.append(corrected_prop)\n\n            naive_arr = np.array(boot_naive)\n            acc_arr = np.array(boot_acc)\n\n            naive_mean = float(np.mean(naive_arr))\n            acc_mean = float(np.mean(acc_arr))\n            acc_ci_lo = float(np.percentile(acc_arr, 2.5))\n            acc_ci_hi = float(np.percentile(acc_arr, 97.5))\n\n            naive_err = abs(naive_mean - true_prop)\n            acc_err = abs(acc_mean - true_prop)\n\n            corpus_results.append({\n                \"true_prop\": true_prop,\n                \"naive_prop\": round(naive_mean, 4),\n                \"naive_error_pp\": round(naive_err * 100, 2),\n                \"acc_prop\": round(acc_mean, 4),\n                \"acc_error_pp\": round(acc_err * 100, 2),\n                \"acc_ci_lo\": round(acc_ci_lo, 4),\n                \"acc_ci_hi\": round(acc_ci_hi, 4),\n            })\n            print(f\"  true={true_prop:.0%}  naive={naive_mean:.4f} ({naive_err*100:.1f}pp)  \"\n                  f\"ACC={acc_mean:.4f} ({acc_err*100:.1f}pp)  \"\n                  f\"95%CI=[{acc_ci_lo:.4f}, {acc_ci_hi:.4f}]\")\n\n        all_gen_results[gen] = {\n            \"tpr\": round(tpr, 4),\n            \"fpr\": round(fpr, 4),\n            \"corpora\": corpus_results,\n        }\n\n    return all_gen_results\n\n\ndef aggregate_results(all_gen_results):\n    prop_data = {p: {\"naive_err\": [], \"acc_err\": [], \"acc_pred\": [],\n                     \"acc_ci_lo\": [], \"acc_ci_hi\": []} for p in TRUE_PROPORTIONS}\n\n    for gen, res in all_gen_results.items():\n        for c in res[\"corpora\"]:\n            tp = c[\"true_prop\"]\n            prop_data[tp][\"naive_err\"].append(c[\"naive_error_pp\"])\n            prop_data[tp][\"acc_err\"].append(c[\"acc_error_pp\"])\n            prop_data[tp][\"acc_pred\"].append(c[\"acc_prop\"])\n            prop_data[tp][\"acc_ci_lo\"].append(c[\"acc_ci_lo\"])\n            prop_data[tp][\"acc_ci_hi\"].append(c[\"acc_ci_hi\"])\n\n    agg = []\n    for tp in TRUE_PROPORTIONS:\n        d = prop_data[tp]\n        if not d[\"acc_err\"]:\n            continue\n        agg.append({\n            \"true_prop\": tp,\n            \"naive_err_mean\": round(float(np.mean(d[\"naive_err\"])), 2),\n            \"acc_pred_mean\": round(float(np.mean(d[\"acc_pred\"])), 4),\n            \"acc_pred_std\": round(float(np.std(d[\"acc_pred\"])), 4),\n            \"acc_err_mean\": round(float(np.mean(d[\"acc_err\"])), 2),\n            \"acc_err_std\": round(float(np.std(d[\"acc_err\"])), 2),\n            \"acc_ci_lo_mean\": round(float(np.mean(d[\"acc_ci_lo\"])), 4),\n            \"acc_ci_hi_mean\": round(float(np.mean(d[\"acc_ci_hi\"])), 4),\n        })\n\n    naive_mae = float(np.mean([a[\"naive_err_mean\"] for a in agg]))\n    acc_mae = float(np.mean([a[\"acc_err_mean\"] for a in agg]))\n    return agg, round(naive_mae, 2), round(acc_mae, 2)\n\n\ndef plot_calibration(agg, all_gen_results, naive_mae, acc_mae, out_path):\n    fig, axes = plt.subplots(1, 2, figsize=(10, 5))\n\n    for ax, method, title in [\n        (axes[0], \"naive\", f\"Naive Classify & Count\\nMAE = {naive_mae:.1f}pp\"),\n        (axes[1], \"acc\", f\"Adjusted Classify & Count\\nMAE = {acc_mae:.1f}pp\"),\n    ]:\n        # Per-generator points\n        for gen, res in all_gen_results.items():\n            xs = [c[\"true_prop\"] * 100 for c in res[\"corpora\"]]\n            if method == \"naive\":\n                ys = [c[\"naive_prop\"] * 100 for c in res[\"corpora\"]]\n            else:\n                ys = [c[\"acc_prop\"] * 100 for c in res[\"corpora\"]]\n            ax.scatter(xs, ys, alpha=0.25, s=25, color=\"steelblue\", zorder=2)\n\n        # Aggregated points\n        true_pcts = [a[\"true_prop\"] * 100 for a in agg]\n        if method == \"naive\":\n            # compute naive pred from acc results not stored in agg... recompute\n            pred_pcts = []\n            for a in agg:\n                tp = a[\"true_prop\"]\n                naive_preds = []\n                for gen, res in all_gen_results.items():\n                    for c in res[\"corpora\"]:\n                        if c[\"true_prop\"] == tp:\n                            naive_preds.append(c[\"naive_prop\"] * 100)\n                pred_pcts.append(float(np.mean(naive_preds)))\n            ax.plot(true_pcts, pred_pcts, \"o-\", color=\"darkblue\", markersize=8, zorder=3)\n        else:\n            pred_pcts = [a[\"acc_pred_mean\"] * 100 for a in agg]\n            ci_lo = [a[\"acc_ci_lo_mean\"] * 100 for a in agg]\n            ci_hi = [a[\"acc_ci_hi_mean\"] * 100 for a in agg]\n            yerr_lo = [p - lo for p, lo in zip(pred_pcts, ci_lo)]\n            yerr_hi = [hi - p for p, hi in zip(pred_pcts, ci_hi)]\n            ax.errorbar(true_pcts, pred_pcts, yerr=[yerr_lo, yerr_hi],\n                        fmt=\"o-\", color=\"darkblue\", capsize=4, capthick=1.5,\n                        markersize=8, zorder=3)\n\n        ax.plot([0, 100], [0, 100], \"k--\", alpha=0.4, linewidth=1)\n        ax.set_xlabel(\"True depth-2+ proportion (%)\", fontsize=11)\n        ax.set_ylabel(\"Predicted depth-2+ proportion (%)\", fontsize=11)\n        ax.set_xlim(-5, 105)\n        ax.set_ylim(-5, 105)\n        ax.set_aspect(\"equal\")\n        ax.set_title(title, fontsize=12)\n\n    plt.tight_layout()\n    plt.savefig(out_path, dpi=300, bbox_inches=\"tight\")\n    plt.savefig(out_path.replace(\".pdf\", \".png\"), dpi=150, bbox_inches=\"tight\")\n    print(f\"\\nSaved: {out_path}\")\n\n\ndef main():\n    os.makedirs(RESULTS_DIR, exist_ok=True)\n\n    print(\"Loading 8-gen data...\")\n    df = load_data()\n    print(f\"Loaded {len(df)} rows, {df['model_name'].nunique()} generators\")\n\n    all_gen_results = run_prevalence_estimation(df)\n\n    agg, naive_mae, acc_mae = aggregate_results(all_gen_results)\n\n    print(\"\\n\" + \"=\" * 70)\n    print(\"AGGREGATED RESULTS (averaged across 8 held-out generators)\")\n    print(\"=\" * 70)\n    print(f\"{'True %':>8s}  {'Naive':>8s}  {'|Err|':>7s}  {'ACC':>8s}  {'|Err|':>7s}  {'95% CI':>20s}\")\n    for a in agg:\n        # get naive mean from per-gen data\n        tp = a[\"true_prop\"]\n        naive_preds = []\n        for gen, res in all_gen_results.items():\n            for c in res[\"corpora\"]:\n                if c[\"true_prop\"] == tp:\n                    naive_preds.append(c[\"naive_prop\"])\n        naive_mean = float(np.mean(naive_preds))\n        print(f\"{tp*100:7.0f}%  {naive_mean*100:7.1f}%  {a['naive_err_mean']:6.2f}pp  \"\n              f\"{a['acc_pred_mean']*100:7.1f}%  {a['acc_err_mean']:6.2f}pp  \"\n              f\"[{a['acc_ci_lo_mean']*100:.1f}%, {a['acc_ci_hi_mean']*100:.1f}%]\")\n\n    print(f\"\\nNaive MAE  = {naive_mae:.2f}pp\")\n    print(f\"ACC MAE    = {acc_mae:.2f}pp\")\n    viable = acc_mae < 5.0\n    conclusion = \"viable\" if viable else \"not viable\"\n    print(f\"Conclusion: corpus-level depth auditing is {conclusion} (ACC MAE {'<' if viable else '>='} 5pp)\")\n\n    # Save JSON\n    out = {\n        \"corpus_size\": CORPUS_SIZE,\n        \"n_bootstrap\": N_BOOTSTRAP,\n        \"n_generators\": len(all_gen_results),\n        \"per_generator\": all_gen_results,\n        \"aggregated\": agg,\n        \"naive_mae_pp\": naive_mae,\n        \"acc_mae_pp\": acc_mae,\n        \"conclusion\": conclusion,\n    }\n    json_path = os.path.join(RESULTS_DIR, \"corpus_prevalence_demo.json\")\n    with open(json_path, \"w\") as f:\n        json.dump(out, f, indent=2)\n    print(f\"Saved: {json_path}\")\n\n    # Plot\n    pdf_path = os.path.join(RESULTS_DIR, \"corpus_prevalence_calibration.pdf\")\n    plot_calibration(agg, all_gen_results, naive_mae, acc_mae, pdf_path)\n\n\nif __name__ == \"__main__\":\n    main()\nPYEOF\necho \"Updated script written.\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_corpus-prevalence_20260517T231957",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat > /root/gen-depth-fingerprint/corpus_prevalence_demo.py << 'PYEOF'\n\"\"\"\ncorpus_prevalence_demo.py — Corpus-level depth prevalence estimation.\n\nBuild 5 synthetic corpora with known depth-2+ proportions (0%, 25%, 50%, 75%, 100%).\nUse LOGO-trained XGBoost + Adjusted Classify-and-Count (ACC) to estimate corpus-level\ndepth-2+ prevalence. Compare predicted vs true proportions, report calibration MAE.\n\"\"\"\n\nimport json\nimport os\nimport numpy as np\nimport pandas as pd\nfrom xgboost import XGBClassifier\nfrom sklearn.metrics import confusion_matrix\nimport matplotlib\nmatplotlib.use(\"Agg\")\nimport matplotlib.pyplot as plt\n\nSEED = 42\nFEATURES = [\"entropy_mean\", \"entropy_std\", \"entropy_min\", \"entropy_max\",\n            \"tail_decay\", \"ttr\", \"hapax_ratio\"]\n\nXGB_PARAMS = dict(n_estimators=200, max_depth=6, learning_rate=0.1,\n                  random_state=SEED, eval_metric=\"mlogloss\",\n                  use_label_encoder=False)\n\nCLASS_MAP_3 = {0: 0, 1: 1, 2: 2, 3: 2, 4: 2}\n\nROOT = os.path.dirname(os.path.abspath(__file__))\nDATA_DIR = os.path.join(ROOT, \"data\")\nRESULTS_DIR = os.path.join(ROOT, \"results\")\n\nCORPUS_SIZE = 800\nTRUE_PROPORTIONS = [0.0, 0.25, 0.50, 0.75, 1.00]\nN_BOOTSTRAP = 200\n\n\ndef load_data():\n    df_base = pd.read_csv(os.path.join(DATA_DIR, \"features_all_models.csv\"))\n    new_gens = [\n        (\"llama-3.2-3b\", os.path.join(DATA_DIR, \"llama-3.2-3b\", \"features_pythia410m.jsonl\")),\n        (\"mistral-7b-v0.3\", os.path.join(DATA_DIR, \"mistral-7b-v0.3\", \"features_pythia410m.jsonl\")),\n    ]\n    dfs = [df_base]\n    for gen_name, path in new_gens:\n        records = []\n        with open(path) as f:\n            for line in f:\n                rec = json.loads(line)\n                rec[\"model_name\"] = gen_name\n                records.append(rec)\n        dfs.append(pd.DataFrame(records))\n\n    cols = [\"model_name\", \"seed_id\", \"depth\"] + FEATURES\n    df = pd.concat([d[cols] for d in dfs], ignore_index=True)\n    df[\"label\"] = df[\"depth\"].map(CLASS_MAP_3)\n    return df\n\n\ndef downsample(df, label_col, rng):\n    counts = df[label_col].value_counts()\n    min_n = counts.min()\n    parts = []\n    for lbl in sorted(counts.index):\n        sub = df[df[label_col] == lbl]\n        parts.append(sub.sample(n=min_n, random_state=rng, replace=False))\n    return pd.concat(parts, ignore_index=True)\n\n\ndef estimate_tpr_fpr_cv(train_df, features, n_folds=5, seed=42):\n    \"\"\"Estimate TPR and FPR via cross-validation on training data.\"\"\"\n    rng = np.random.RandomState(seed)\n    indices = np.arange(len(train_df))\n    rng.shuffle(indices)\n    folds = np.array_split(indices, n_folds)\n\n    all_y_true, all_y_pred = [], []\n    for i in range(n_folds):\n        val_idx = folds[i]\n        train_idx = np.concatenate([folds[j] for j in range(n_folds) if j != i])\n\n        tr = train_df.iloc[train_idx]\n        va = train_df.iloc[val_idx]\n\n        tr_ds = downsample(tr, \"binary\", rng)\n        clf = XGBClassifier(**XGB_PARAMS)\n        clf.fit(tr_ds[features].values, tr_ds[\"binary\"].values)\n        preds = clf.predict(va[features].values)\n\n        all_y_true.extend(va[\"binary\"].values)\n        all_y_pred.extend(preds)\n\n    all_y_true = np.array(all_y_true)\n    all_y_pred = np.array(all_y_pred)\n    tn, fp, fn, tp = confusion_matrix(all_y_true, all_y_pred).ravel()\n    tpr = tp / (tp + fn)\n    fpr = fp / (fp + tn)\n    return tpr, fpr\n\n\ndef acc_correct(predicted_prevalence, tpr, fpr):\n    \"\"\"Adjusted Classify-and-Count: correct prevalence using TPR/FPR.\"\"\"\n    denom = tpr - fpr\n    if abs(denom) < 1e-6:\n        return predicted_prevalence\n    corrected = (predicted_prevalence - fpr) / denom\n    return np.clip(corrected, 0.0, 1.0)\n\n\ndef run_prevalence_estimation(df):\n    generators = sorted(df[\"model_name\"].unique())\n    rng = np.random.RandomState(SEED)\n\n    all_gen_results = {}\n\n    for gen in generators:\n        print(f\"\\n--- Held-out generator: {gen} ---\")\n        test_df = df[df[\"model_name\"] == gen].copy()\n        train_df = df[df[\"model_name\"] != gen].copy()\n\n        # Binary: gen-1 vs gen-2+, exclude gen-0\n        train_bin = train_df[train_df[\"label\"] >= 1].copy()\n        train_bin[\"binary\"] = (train_bin[\"label\"] >= 2).astype(int)\n        test_bin = test_df[test_df[\"label\"] >= 1].copy()\n        test_bin[\"binary\"] = (test_bin[\"label\"] >= 2).astype(int)\n\n        # Estimate TPR/FPR via CV on training data\n        tpr, fpr = estimate_tpr_fpr_cv(train_bin, FEATURES, n_folds=5, seed=SEED)\n        print(f\"  CV-estimated TPR={tpr:.4f}, FPR={fpr:.4f}\")\n\n        # Train final classifier on all training data\n        train_ds = downsample(train_bin, \"binary\", rng)\n        clf = XGBClassifier(**XGB_PARAMS)\n        clf.fit(train_ds[FEATURES].values, train_ds[\"binary\"].values)\n\n        gen1_pool = test_bin[test_bin[\"binary\"] == 0]\n        gen2_pool = test_bin[test_bin[\"binary\"] == 1]\n        n_gen1 = len(gen1_pool)\n        n_gen2 = len(gen2_pool)\n        print(f\"  Pool sizes: gen-1={n_gen1}, gen-2+={n_gen2}\")\n\n        corpus_results = []\n        for true_prop in TRUE_PROPORTIONS:\n            n_pos = int(round(CORPUS_SIZE * true_prop))\n            n_neg = CORPUS_SIZE - n_pos\n\n            if n_neg > n_gen1 or n_pos > n_gen2:\n                print(f\"  [SKIP] prop={true_prop:.0%}\")\n                continue\n\n            boot_naive = []\n            boot_acc = []\n            for b in range(N_BOOTSTRAP):\n                brng = np.random.RandomState(SEED + b)\n                sample_neg = gen1_pool.sample(n=n_neg, random_state=brng, replace=True)\n                sample_pos = gen2_pool.sample(n=n_pos, random_state=brng, replace=True)\n                corpus = pd.concat([sample_neg, sample_pos], ignore_index=True)\n\n                preds = clf.predict(corpus[FEATURES].values)\n                naive_prop = float(preds.sum()) / len(preds)\n                corrected_prop = float(acc_correct(naive_prop, tpr, fpr))\n\n                boot_naive.append(naive_prop)\n                boot_acc.append(corrected_prop)\n\n            naive_arr = np.array(boot_naive)\n            acc_arr = np.array(boot_acc)\n\n            naive_mean = float(np.mean(naive_arr))\n            acc_mean = float(np.mean(acc_arr))\n            acc_ci_lo = float(np.percentile(acc_arr, 2.5))\n            acc_ci_hi = float(np.percentile(acc_arr, 97.5))\n\n            naive_err = abs(naive_mean - true_prop)\n            acc_err = abs(acc_mean - true_prop)\n\n            corpus_results.append({\n                \"true_prop\": true_prop,\n                \"naive_prop\": round(naive_mean, 4),\n                \"naive_error_pp\": round(naive_err * 100, 2),\n                \"acc_prop\": round(acc_mean, 4),\n                \"acc_error_pp\": round(acc_err * 100, 2),\n                \"acc_ci_lo\": round(acc_ci_lo, 4),\n                \"acc_ci_hi\": round(acc_ci_hi, 4),\n            })\n            print(f\"  true={true_prop:.0%}  naive={naive_mean:.4f} ({naive_err*100:.1f}pp)  \"\n                  f\"ACC={acc_mean:.4f} ({acc_err*100:.1f}pp)  \"\n                  f\"95%CI=[{acc_ci_lo:.4f}, {acc_ci_hi:.4f}]\")\n\n        all_gen_results[gen] = {\n            \"tpr\": round(tpr, 4),\n            \"fpr\": round(fpr, 4),\n            \"corpora\": corpus_results,\n        }\n\n    return all_gen_results\n\n\ndef aggregate_results(all_gen_results):\n    prop_data = {p: {\"naive_err\": [], \"acc_err\": [], \"acc_pred\": [],\n                     \"acc_ci_lo\": [], \"acc_ci_hi\": []} for p in TRUE_PROPORTIONS}\n\n    for gen, res in all_gen_results.items():\n        for c in res[\"corpora\"]:\n            tp = c[\"true_prop\"]\n            prop_data[tp][\"naive_err\"].append(c[\"naive_error_pp\"])\n            prop_data[tp][\"acc_err\"].append(c[\"acc_error_pp\"])\n            prop_data[tp][\"acc_pred\"].append(c[\"acc_prop\"])\n            prop_data[tp][\"acc_ci_lo\"].append(c[\"acc_ci_lo\"])\n            prop_data[tp][\"acc_ci_hi\"].append(c[\"acc_ci_hi\"])\n\n    agg = []\n    for tp in TRUE_PROPORTIONS:\n        d = prop_data[tp]\n        if not d[\"acc_err\"]:\n            continue\n        agg.append({\n            \"true_prop\": tp,\n            \"naive_err_mean\": round(float(np.mean(d[\"naive_err\"])), 2),\n            \"acc_pred_mean\": round(float(np.mean(d[\"acc_pred\"])), 4),\n            \"acc_pred_std\": round(float(np.std(d[\"acc_pred\"])), 4),\n            \"acc_err_mean\": round(float(np.mean(d[\"acc_err\"])), 2),\n            \"acc_err_std\": round(float(np.std(d[\"acc_err\"])), 2),\n            \"acc_ci_lo_mean\": round(float(np.mean(d[\"acc_ci_lo\"])), 4),\n            \"acc_ci_hi_mean\": round(float(np.mean(d[\"acc_ci_hi\"])), 4),\n        })\n\n    naive_mae = float(np.mean([a[\"naive_err_mean\"] for a in agg]))\n    acc_mae = float(np.mean([a[\"acc_err_mean\"] for a in agg]))\n    return agg, round(naive_mae, 2), round(acc_mae, 2)\n\n\ndef plot_calibration(agg, all_gen_results, naive_mae, acc_mae, out_path):\n    fig, axes = plt.subplots(1, 2, figsize=(10, 5))\n\n    for ax, method, title in [\n        (axes[0], \"naive\", f\"Naive Classify & Count\\nMAE = {naive_mae:.1f}pp\"),\n        (axes[1], \"acc\", f\"Adjusted Classify & Count\\nMAE = {acc_mae:.1f}pp\"),\n    ]:\n        # Per-generator points\n        for gen, res in all_gen_results.items():\n            xs = [c[\"true_prop\"] * 100 for c in res[\"corpora\"]]\n            if method == \"naive\":\n                ys = [c[\"naive_prop\"] * 100 for c in res[\"corpora\"]]\n            else:\n                ys = [c[\"acc_prop\"] * 100 for c in res[\"corpora\"]]\n            ax.scatter(xs, ys, alpha=0.25, s=25, color=\"steelblue\", zorder=2)\n\n        # Aggregated points\n        true_pcts = [a[\"true_prop\"] * 100 for a in agg]\n        if method == \"naive\":\n            # compute naive pred from acc results not stored in agg... recompute\n            pred_pcts = []\n            for a in agg:\n                tp = a[\"true_prop\"]\n                naive_preds = []\n                for gen, res in all_gen_results.items():\n                    for c in res[\"corpora\"]:\n                        if c[\"true_prop\"] == tp:\n                            naive_preds.append(c[\"naive_prop\"] * 100)\n                pred_pcts.append(float(np.mean(naive_preds)))\n            ax.plot(true_pcts, pred_pcts, \"o-\", color=\"darkblue\", markersize=8, zorder=3)\n        else:\n            pred_pcts = [a[\"acc_pred_mean\"] * 100 for a in agg]\n            ci_lo = [a[\"acc_ci_lo_mean\"] * 100 for a in agg]\n            ci_hi = [a[\"acc_ci_hi_mean\"] * 100 for a in agg]\n            yerr_lo = [p - lo for p, lo in zip(pred_pcts, ci_lo)]\n            yerr_hi = [hi - p for p, hi in zip(pred_pcts, ci_hi)]\n            ax.errorbar(true_pcts, pred_pcts, yerr=[yerr_lo, yerr_hi],\n                        fmt=\"o-\", color=\"darkblue\", capsize=4, capthick=1.5,\n                        markersize=8, zorder=3)\n\n        ax.plot([0, 100], [0, 100], \"k--\", alpha=0.4, linewidth=1)\n        ax.set_xlabel(\"True depth-2+ proportion (%)\", fontsize=11)\n        ax.set_ylabel(\"Predicted depth-2+ proportion (%)\", fontsize=11)\n        ax.set_xlim(-5, 105)\n        ax.set_ylim(-5, 105)\n        ax.set_aspect(\"equal\")\n        ax.set_title(title, fontsize=12)\n\n    plt.tight_layout()\n    plt.savefig(out_path, dpi=300, bbox_inches=\"tight\")\n    plt.savefig(out_path.replace(\".pdf\", \".png\"), dpi=150, bbox_inches=\"tight\")\n    print(f\"\\nSaved: {out_path}\")\n\n\ndef main():\n    os.makedirs(RESULTS_DIR, exist_ok=True)\n\n    print(\"Loading 8-gen data...\")\n    df = load_data()\n    print(f\"Loaded {len(df)} rows, {df['model_name'].nunique()} generators\")\n\n    all_gen_results = run_prevalence_estimation(df)\n\n    agg, naive_mae, acc_mae = aggregate_results(all_gen_results)\n\n    print(\"\\n\" + \"=\" * 70)\n    print(\"AGGREGATED RESULTS (averaged across 8 held-out generators)\")\n    print(\"=\" * 70)\n    print(f\"{'True %':>8s}  {'Naive':>8s}  {'|Err|':>7s}  {'ACC':>8s}  {'|Err|':>7s}  {'95% CI':>20s}\")\n    for a in agg:\n        # get naive mean from per-gen data\n        tp = a[\"true_prop\"]\n        naive_preds = []\n        for gen, res in all_gen_results.items():\n            for c in res[\"corpora\"]:\n                if c[\"true_prop\"] == tp:\n                    naive_preds.append(c[\"naive_prop\"])\n        naive_mean = float(np.mean(naive_preds))\n        print(f\"{tp*100:7.0f}%  {naive_mean*100:7.1f}%  {a['naive_err_mean']:6.2f}pp  \"\n              f\"{a['acc_pred_mean']*100:7.1f}%  {a['acc_err_mean']:6.2f}pp  \"\n              f\"[{a['acc_ci_lo_mean']*100:.1f}%, {a['acc_ci_hi_mean']*100:.1f}%]\")\n\n    print(f\"\\nNaive MAE  = {naive_mae:.2f}pp\")\n    print(f\"ACC MAE    = {acc_mae:.2f}pp\")\n    viable = acc_mae < 5.0\n    conclusion = \"viable\" if viable else \"not viable\"\n    print(f\"Conclusion: corpus-level depth auditing is {conclusion} (ACC MAE {'<' if viable else '>='} 5pp)\")\n\n    # Save JSON\n    out = {\n        \"corpus_size\": CORPUS_SIZE,\n        \"n_bootstrap\": N_BOOTSTRAP,\n        \"n_generators\": len(all_gen_results),\n        \"per_generator\": all_gen_results,\n        \"aggregated\": agg,\n        \"naive_mae_pp\": naive_mae,\n        \"acc_mae_pp\": acc_mae,\n        \"conclusion\": conclusion,\n    }\n    json_path = os.path.join(RESULTS_DIR, \"corpus_prevalence_demo.json\")\n    with open(json_path, \"w\") as f:\n        json.dump(out, f, indent=2)\n    print(f\"Saved: {json_path}\")\n\n    # Plot\n    pdf_path = os.path.join(RESULTS_DIR, \"corpus_prevalence_calibration.pdf\")\n    plot_calibration(agg, all_gen_results, naive_mae, acc_mae, pdf_path)\n\n\nif __name__ == \"__main__\":\n    main()\nPYEOF\necho \"Updated script written.\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-17T23:31:25.644522+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Updated script written.\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.31}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_corpus-prevalence_20260517T231957",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-17T23:31:25.644669+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-5090",
  "command": "source /root/miniconda3/bin/activate && cd /root/gen-depth-fingerprint && python corpus_prevalence_demo.py 2>&1 | tee logs/corpus_prevalence_demo.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_corpus-prevalence_20260517T231957",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-5090",
    "command": "source /root/miniconda3/bin/activate && cd /root/gen-depth-fingerprint && python corpus_prevalence_demo.py 2>&1 | tee logs/corpus_prevalence_demo.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-17T23:31:25.644875+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/miniconda3/lib/python3.12/site-packages/xgboost/training.py:200: UserWarning: [07:23:57] WARNING: /__w/xgboost/xgboost/src/learner.cc:782: \\nParameters: { \\\"use_label_encoder\\\" } are not used.\\n\\n  bst.update(dtrain, iteration=i, fobj=obj)\\n/root/miniconda3/lib/python3.12/site-packages/xgboost/training.py:200: UserWarning: [07:23:57] WARNING: /__w/xgboost/xgboost/src/learner.cc:782: \\nParameters: { \\\"use_label_encoder\\\" } are not used.\\n\\n  bst.update(dtrain, iteration=i, fobj=obj)\\n/root/miniconda3/lib/python3.12/site-packages/xgboost/training.py:200: UserWarning: [07:23:57] WARNING: /__w/xgboost/xgboost/src/learner.cc:782: \\nParameters: { \\\"use_label_encoder\\\" } are not used.\\n\\n  bst.update(dtrain, iteration=i, fobj=obj)\\n/root/miniconda3/lib/python3.12/site-packages/xgboost/training.py:200: UserWarning: [07:23:57] WARNING: /__w/xgboost/xgboost/src/learner.cc:782: \\nParameters: { \\\"use_label_encoder\\\" } are not used.\\n\\n  bst.update(dtrain, iteration=i, fobj=obj)\\n/root/miniconda3/lib/python3.12/site-packages/xgboost/training.py:200: UserWarning: [07:23:58] WARNING: /__w/xgboost/xgboost/src/learner.cc:782: \\nParameters: { \\\"use_label_encoder\\\" } are not used.\\n\\n  bst.update(dtrain, iteration=i, fobj=obj)\\n/root/miniconda3/lib/python3.12/site-packages/xgboost/training.py:200: UserWarning: [07:23:58] WARNING: /__w/xgboost/xgboost/src/learner.cc:782: \\nParameters: { \\\"use_label_encoder\\\" } are not used.\\n\\n  bst.update(dtrain, iteration=i, fobj=obj)\\n/root/miniconda3/lib/python3.12/site-packages/xgboost/training.py:200: UserWarning: [07:24:00] WARNING: /__w/xgboost/xgboost/src/learner.cc:782: \\nParameters: { \\\"use_label_encoder\\\" } are not used.\\n\\n  bst.update(dtrain, iteration=i, fobj=obj)\\n/root/miniconda3/lib/python3.12/site-packages/xgboost/training.py:200: UserWarning: [07:24:00] WARNING: /__w/xgboost/xgboost/src/learner.cc:782: \\nParameters:
…[truncated 6572 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_corpus-prevalence_20260517T231957",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-17T23:31:25.645116+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat > /root/gen-depth-fingerprint/corpus_prevalence_demo.py << 'PYEOF'\n\"\"\"\ncorpus_prevalence_demo.py — Corpus-level depth prevalence estimation.\n\nBuild 5 synthetic corpora with known depth-2+ proportions (0%, 25%, 50%, 75%, 100%).\nUse LOGO-trained XGBoost with three quantification methods:\n  1. Classify & Count (CC): predicted positive rate\n  2. Adjusted CC (ACC): correct with CV-estimated TPR/FPR\n  3. Probabilistic CC (PCC): mean predicted probability\nReport calibration MAE for each.\n\"\"\"\n\nimport json\nimport os\nimport numpy as np\nimport pandas as pd\nfrom xgboost import XGBClassifier\nfrom sklearn.metrics import confusion_matrix\nimport matplotlib\nmatplotlib.use(\"Agg\")\nimport matplotlib.pyplot as plt\n\nSEED = 42\nFEATURES = [\"entropy_mean\", \"entropy_std\", \"entropy_min\", \"entropy_max\",\n            \"tail_decay\", \"ttr\", \"hapax_ratio\"]\n\nXGB_PARAMS = dict(n_estimators=200, max_depth=6, learning_rate=0.1,\n                  random_state=SEED, eval_metric=\"mlogloss\",\n                  use_label_encoder=False)\n\nCLASS_MAP_3 = {0: 0, 1: 1, 2: 2, 3: 2, 4: 2}\n\nROOT = os.path.dirname(os.path.abspath(__file__))\nDATA_DIR = os.path.join(ROOT, \"data\")\nRESULTS_DIR = os.path.join(ROOT, \"results\")\n\nCORPUS_SIZE = 800\nTRUE_PROPORTIONS = [0.0, 0.25, 0.50, 0.75, 1.00]\nN_BOOTSTRAP = 200\n\n\ndef load_data():\n    df_base = pd.read_csv(os.path.join(DATA_DIR, \"features_all_models.csv\"))\n    new_gens = [\n        (\"llama-3.2-3b\", os.path.join(DATA_DIR, \"llama-3.2-3b\", \"features_pythia410m.jsonl\")),\n        (\"mistral-7b-v0.3\", os.path.join(DATA_DIR, \"mistral-7b-v0.3\", \"features_pythia410m.jsonl\")),\n    ]\n    dfs = [df_base]\n    for gen_name, path in new_gens:\n        records = []\n        with open(path) as f:\n            for line in f:\n                rec = json.loads(line)\n                rec[\"model_name\"] = gen_name\n                records.append(rec)\n        dfs.append(pd.DataFrame(records))\n\n    cols = [\"model_name\", \"seed_id\", \"depth\"] + FEATURES\n    df = pd.concat([d[cols] for d in dfs], ignore_index=True)\n    df[\"label\"] = df[\"depth\"].map(CLASS_MAP_3)\n    return df\n\n\ndef downsample(df, label_col, rng):\n    counts = df[label_col].value_counts()\n    min_n = counts.min()\n    parts = []\n    for lbl in sorted(counts.index):\n        sub = df[df[label_col] == lbl]\n        parts.append(sub.sample(n=min_n, random_state=rng, replace=False))\n    return pd.concat(parts, ignore_index=True)\n\n\ndef estimate_tpr_fpr_cv(train_df, features, n_folds=5, seed=42):\n    rng = np.random.RandomState(seed)\n    indices = np.arange(len(train_df))\n    rng.shuffle(indices)\n    folds = np.array_split(indices, n_folds)\n\n    all_y_true, all_y_pred = [], []\n    for i in range(n_folds):\n        val_idx = folds[i]\n        train_idx = np.concatenate([folds[j] for j in range(n_folds) if j != i])\n        tr = train_df.iloc[train_idx]\n        va = train_df.iloc[val_idx]\n        tr_ds = downsample(tr, \"binary\", rng)\n        clf = XGBClassifier(**XGB_PARAMS)\n        clf.fit(tr_ds[features].values, tr_ds[\"binary\"].values)\n        preds = clf.predict(va[features].values)\n        all_y_true.extend(va[\"binary\"].values)\n        all_y_pred.extend(preds)\n\n    all_y_true = np.array(all_y_true)\n    all_y_pred = np.array(all_y_pred)\n    tn, fp, fn, tp = confusion_matrix(all_y_true, all_y_pred).ravel()\n    tpr = tp / (tp + fn)\n    fpr = fp / (fp + tn)\n    return tpr, fpr\n\n\ndef acc_correct(predicted_prevalence, tpr, fpr):\n    denom = tpr - fpr\n    if abs(denom) < 1e-6:\n        return predicted_prevalence\n    corrected = (predicted_prevalence - fpr) / denom\n    return np.clip(corrected, 0.0, 1.0)\n\n\ndef run_prevalence_estimation(df):\n    generators = sorted(df[\"model_name\"].unique())\n    rng = np.random.RandomState(SEED)\n    all_gen_results = {}\n\n    for gen in generators:\n        print(f\"\\n--- Held-out generator: {gen} ---\")\n        test_df = df[df[\"model_name\"] == gen].copy()\n        train_df = df[df[\"model_name\"] != gen].copy()\n\n        train_bin = train_df[train_df[\"label\"] >= 1].copy()\n        train_bin[\"binary\"] = (train_bin[\"label\"] >= 2).astype(int)\n        test_bin = test_df[test_df[\"label\"] >= 1].copy()\n        test_bin[\"binary\"] = (test_bin[\"label\"] >= 2).astype(int)\n\n        tpr, fpr = estimate_tpr_fpr_cv(train_bin, FEATURES, n_folds=5, seed=SEED)\n        print(f\"  CV TPR={tpr:.4f}, FPR={fpr:.4f}\")\n\n        train_ds = downsample(train_bin, \"binary\", rng)\n        clf = XGBClassifier(**XGB_PARAMS)\n        clf.fit(train_ds[FEATURES].values, train_ds[\"binary\"].values)\n\n        gen1_pool = test_bin[test_bin[\"binary\"] == 0]\n        gen2_pool = test_bin[test_bin[\"binary\"] == 1]\n        n_gen1, n_gen2 = len(gen1_pool), len(gen2_pool)\n        print(f\"  Pool: gen-1={n_gen1}, gen-2+={n_gen2}\")\n\n        corpus_results = []\n        for true_prop in TRUE_PROPORTIONS:\n            n_pos = int(round(CORPUS_SIZE * true_prop))\n            n_neg = CORPUS_SIZE - n_pos\n            if n_neg > n_gen1 or n_pos > n_gen2:\n                continue\n\n            boot_cc, boot_acc, boot_pcc = [], [], []\n            for b in range(N_BOOTSTRAP):\n                brng = np.random.RandomState(SEED + b)\n                s_neg = gen1_pool.sample(n=n_neg, random_state=brng, replace=True)\n                s_pos = gen2_pool.sample(n=n_pos, random_state=brng, replace=True)\n                corpus = pd.concat([s_neg, s_pos], ignore_index=True)\n                X = corpus[FEATURES].values\n\n                preds = clf.predict(X)\n                proba = clf.predict_proba(X)[:, 1]\n\n                cc = float(preds.sum()) / len(preds)\n                acc = float(acc_correct(cc, tpr, fpr))\n                pcc = float(proba.mean())\n\n                boot_cc.append(cc)\n                boot_acc.append(acc)\n                boot_pcc.append(pcc)\n\n            cc_m = float(np.mean(boot_cc))\n            acc_m = float(np.mean(boot_acc))\n            pcc_m = float(np.mean(boot_pcc))\n\n            corpus_results.append({\n                \"true_prop\": true_prop,\n                \"cc_prop\": round(cc_m, 4),\n                \"cc_err\": round(abs(cc_m - true_prop) * 100, 2),\n                \"acc_prop\": round(acc_m, 4),\n                \"acc_err\": round(abs(acc_m - true_prop) * 100, 2),\n                \"pcc_prop\": round(pcc_m, 4),\n                \"pcc_err\": round(abs(pcc_m - true_prop) * 100, 2),\n                \"pcc_ci_lo\": round(float(np.percentile(boot_pcc, 2.5)), 4),\n                \"pcc_ci_hi\": round(float(np.percentile(boot_pcc, 97.5)), 4),\n            })\n            print(f\"  true={true_prop:.0%}  CC={cc_m:.3f}({abs(cc_m-true_prop)*100:.1f}pp)  \"\n                  f\"ACC={acc_m:.3f}({abs(acc_m-true_prop)*100:.1f}pp)  \"\n                  f\"PCC={pcc_m:.3f}({abs(pcc_m-true_prop)*100:.1f}pp)\")\n\n        all_gen_results[gen] = {\n            \"tpr\": round(tpr, 4), \"fpr\": round(fpr, 4),\n            \"corpora\": corpus_results,\n        }\n\n    return all_gen_results\n\n\ndef aggregate_results(all_gen_results):\n    prop_data = {p: {\"cc_err\": [], \"acc_err\": [], \"pcc_err\": [],\n                     \"pcc_pred\": [], \"pcc_ci_lo\": [], \"pcc_ci_hi\": []}\n                 for p in TRUE_PROPORTIONS}\n\n    for gen, res in all_gen_results.items():\n        for c in res[\"corpora\"]:\n            tp = c[\"true_prop\"]\n            prop_data[tp][\"cc_err\"].append(c[\"cc_err\"])\n            prop_data[tp][\"acc_err\"].append(c[\"acc_err\"])\n            prop_data[tp][\"pcc_err\"].append(c[\"pcc_err\"])\n            prop_data[tp][\"pcc_pred\"].append(c[\"pcc_prop\"])\n            prop_data[tp][\"pcc_ci_lo\"].append(c[\"pcc_ci_lo\"])\n            prop_data[tp][\"pcc_ci_hi\"].append(c[\"pcc_ci_hi\"])\n\n    agg = []\n    for tp in TRUE_PROPORTIONS:\n        d = prop_data[tp]\n        if not d[\"pcc_err\"]:\n            continue\n        agg.append({\n            \"true_prop\": tp,\n            \"cc_err_mean\": round(float(np.mean(d[\"cc_err\"])), 2),\n            \"acc_err_mean\": round(float(np.mean(d[\"acc_err\"])), 2),\n            \"pcc_pred_mean\": round(float(np.mean(d[\"pcc_pred\"])), 4),\n            \"pcc_err_mean\": round(float(np.mean(d[\"pcc_err\"])), 2),\n            \"pcc_err_std\": round(float(np.std(d[\"pcc_err\"])), 2),\n            \"pcc_ci_lo_mean\": round(float(np.mean(d[\"pcc_ci_lo\"])), 4),\n            \"pcc_ci_hi_mean\": round(float(np.mean(d[\"pcc_ci_hi\"])), 4),\n        })\n\n    cc_mae = round(float(np.mean([a[\"cc_err_mean\"] for a in agg])), 2)\n    acc_mae = round(float(np.mean([a[\"acc_err_mean\"] for a in agg])), 2)\n    pcc_mae = round(float(np.mean([a[\"pcc_err_mean\"] for a in agg])), 2)\n    return agg, cc_mae, acc_mae, pcc_mae\n\n\ndef plot_calibration(agg, all_gen_results, cc_mae, acc_mae, pcc_mae, out_path):\n    fig, axes = plt.subplots(1, 3, figsize=(14, 4.5))\n\n    methods = [\n        (\"cc\", \"Classify & Count\", cc_mae, \"cc_prop\", \"cc_err\"),\n        (\"acc\", \"Adjusted CC\", acc_mae, \"acc_prop\", \"acc_err\"),\n        (\"pcc\", \"Probabilistic CC\", pcc_mae, \"pcc_prop\", \"pcc_err\"),\n    ]\n\n    for ax, (key, title, mae, prop_key, err_key) in zip(axes, methods):\n        for gen, res in all_gen_results.items():\n            xs = [c[\"true_prop\"] * 100 for c in res[\"corpora\"]]\n            ys = [c[prop_key] * 100 for c in res[\"corpora\"]]\n            ax.scatter(xs, ys, alpha=0.25, s=20, color=\"steelblue\", zorder=2)\n\n        true_pcts = [a[\"true_prop\"] * 100 for a in agg]\n        if key == \"pcc\":\n            pred_pcts = [a[\"pcc_pred_mean\"] * 100 for a in agg]\n            ci_lo = [a[\"pcc_ci_lo_mean\"] * 100 for a in agg]\n            ci_hi = [a[\"pcc_ci_hi_mean\"] * 100 for a in agg]\n            yerr_lo = [p - lo for p, lo in zip(pred_pcts, ci_lo)]\n            yerr_hi = [hi - p for p, hi in zip(pred_pcts, ci_hi)]\n            ax.errorbar(true_pcts, pred_pcts, yerr=[yerr_lo, yerr_hi],\n                        fmt=\"o-\", color=\"darkblue\", capsize=4, capthick=1.5,\n                        markersize=7, zorder=3)\n        else:\n            pred_pcts = []\n            for a in agg:\n                tp = a[\"true_prop\"]\n                vals = []\n                for gen, res in all_gen_results.items():\n                    for c in res[\"corpora\"]:\n                        if c[\"true_prop\"] == tp:\n                            vals.append(c[prop_key] * 100)\n                pred_pcts.append(float(np.mean(vals)))\n            ax.plot(true_pcts, pred_pcts, \"o-\", color=\"darkblue\", markersize=7, zorder=3)\n\n        ax.plot([0, 100], [0, 100], \"k--\", alpha=0.4, linewidth=1)\n        ax.set_xlabel(\"True depth-2+ (%)\", fontsize=10)\n        ax.set_ylabel(\"Predicted depth-2+ (%)\", fontsize=10)\n        ax.set_xlim(-5, 105)\n        ax.set_ylim(-5, 105)\n        ax.set_aspect(\"equal\")\n        ax.set_title(f\"{title}\\nMAE = {mae:.1f}pp\", fontsize=11)\n\n    plt.tight_layout()\n    plt.savefig(out_path, dpi=300, bbox_inches=\"tight\")\n    plt.savefig(out_path.replace(\".pdf\", \".png\"), dpi=150, bbox_inches=\"tight\")\n    print(f\"\\nSaved: {out_path}\")\n\n\ndef main():\n    os.makedirs(RESULTS_DIR, exist_ok=True)\n    print(\"Loading 8-gen data...\")\n    df = load_data()\n    print(f\"Loaded {len(df)} rows, {df['model_name'].nunique()} generators\")\n\n    all_gen_results = run_prevalence_estimation(df)\n    agg, cc_mae, acc_mae, pcc_mae = aggregate_results(all_gen_results)\n\n    best_method = min([(\"CC\", cc_mae), (\"ACC\", acc_mae), (\"PCC\", pcc_mae)], key=lambda x: x[1])\n\n    print(\"\\n\" + \"=\" * 80)\n    print(\"AGGREGATED RESULTS (averaged across 8 held-out generators)\")\n    print(\"=\" * 80)\n    print(f\"{'True %':>8s}  {'CC err':>8s}  {'ACC err':>8s}  {'PCC pred':>9s}  {'PCC err':>8s}  {'PCC 95% CI':>20s}\")\n    for a in agg:\n        print(f\"{a['true_prop']*100:7.0f}%  {a['cc_err_mean']:7.2f}pp  {a['acc_err_mean']:7.2f}pp  \"\n              f\"{a['pcc_pred_mean']*100:8.1f}%  {a['pcc_err_mean']:7.2f}pp  \"\n              f\"[{a['pcc_ci_lo_mean']*100:.1f}%, {a['pcc_ci_hi_mean']*100:.1f}%]\")\n\n    print(f\"\\nCC  MAE = {cc_mae:.2f}pp\")\n    print(f\"ACC MAE = {acc_mae:.2f}pp\")\n    print(f\"PCC MAE = {pcc_mae:.2f}pp\")\n    print(f\"Best: {best_method[0]} ({best_method[1]:.2f}pp)\")\n\n    viable = best_method[1] < 5.0\n    conclusion = \"viable\" if viable else \"not viable\"\n    print(f\"\\nConclusion: corpus-level depth auditing is {conclusion} \"\n          f\"(best MAE = {best_method[1]:.2f}pp {'<' if viable else '>='} 5pp)\")\n\n    out = {\n        \"corpus_size\": CORPUS_SIZE,\n        \"n_bootstrap\": N_BOOTSTRAP,\n        \"n_generators\": len(all_gen_results),\n        \"per_generator\": all_gen_results,\n        \"aggregated\": agg,\n        \"cc_mae_pp\": cc_mae,\n        \"acc_mae_pp\": acc_mae,\n        \"pcc_mae_pp\": pcc_mae,\n        \"best_method\": best_method[0],\n        \"best_mae_pp\": best_method[1],\n        \"conclusion\": conclusion,\n    }\n    json_path = os.path.join(RESULTS_DIR, \"corpus_prevalence_demo.json\")\n    with open(json_path, \"w\") as f:\n        json.dump(out, f, indent=2)\n    print(f\"Saved: {json_path}\")\n\n    pdf_path = os.path.join(RESULTS_DIR, \"corpus_prevalence_calibration.pdf\")\n    plot_calibration(agg, all_gen_results, cc_mae, acc_mae, pcc_mae, pdf_path)\n\n\nif __name__ == \"__main__\":\n    main()\nPYEOF\necho \"Script updated.\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_corpus-prevalence_20260517T231957",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat > /root/gen-depth-fingerprint/corpus_prevalence_demo.py << 'PYEOF'\n\"\"\"\ncorpus_prevalence_demo.py — Corpus-level depth prevalence estimation.\n\nBuild 5 synthetic corpora with known depth-2+ proportions (0%, 25%, 50%, 75%, 100%).\nUse LOGO-trained XGBoost with three quantification methods:\n  1. Classify & Count (CC): predicted positive rate\n  2. Adjusted CC (ACC): correct with CV-estimated TPR/FPR\n  3. Probabilistic CC (PCC): mean predicted probability\nReport calibration MAE for each.\n\"\"\"\n\nimport json\nimport os\nimport numpy as np\nimport pandas as pd\nfrom xgboost import XGBClassifier\nfrom sklearn.metrics import confusion_matrix\nimport matplotlib\nmatplotlib.use(\"Agg\")\nimport matplotlib.pyplot as plt\n\nSEED = 42\nFEATURES = [\"entropy_mean\", \"entropy_std\", \"entropy_min\", \"entropy_max\",\n            \"tail_decay\", \"ttr\", \"hapax_ratio\"]\n\nXGB_PARAMS = dict(n_estimators=200, max_depth=6, learning_rate=0.1,\n                  random_state=SEED, eval_metric=\"mlogloss\",\n                  use_label_encoder=False)\n\nCLASS_MAP_3 = {0: 0, 1: 1, 2: 2, 3: 2, 4: 2}\n\nROOT = os.path.dirname(os.path.abspath(__file__))\nDATA_DIR = os.path.join(ROOT, \"data\")\nRESULTS_DIR = os.path.join(ROOT, \"results\")\n\nCORPUS_SIZE = 800\nTRUE_PROPORTIONS = [0.0, 0.25, 0.50, 0.75, 1.00]\nN_BOOTSTRAP = 200\n\n\ndef load_data():\n    df_base = pd.read_csv(os.path.join(DATA_DIR, \"features_all_models.csv\"))\n    new_gens = [\n        (\"llama-3.2-3b\", os.path.join(DATA_DIR, \"llama-3.2-3b\", \"features_pythia410m.jsonl\")),\n        (\"mistral-7b-v0.3\", os.path.join(DATA_DIR, \"mistral-7b-v0.3\", \"features_pythia410m.jsonl\")),\n    ]\n    dfs = [df_base]\n    for gen_name, path in new_gens:\n        records = []\n        with open(path) as f:\n            for line in f:\n                rec = json.loads(line)\n                rec[\"model_name\"] = gen_name\n                records.append(rec)\n        dfs.append(pd.DataFrame(records))\n\n    cols = [\"model_name\", \"seed_id\", \"depth\"] + FEATURES\n    df = pd.concat([d[cols] for d in dfs], ignore_index=True)\n    df[\"label\"] = df[\"depth\"].map(CLASS_MAP_3)\n    return df\n\n\ndef downsample(df, label_col, rng):\n    counts = df[label_col].value_counts()\n    min_n = counts.min()\n    parts = []\n    for lbl in sorted(counts.index):\n        sub = df[df[label_col] == lbl]\n        parts.append(sub.sample(n=min_n, random_state=rng, replace=False))\n    return pd.concat(parts, ignore_index=True)\n\n\ndef estimate_tpr_fpr_cv(train_df, features, n_folds=5, seed=42):\n    rng = np.random.RandomState(seed)\n    indices = np.arange(len(train_df))\n    rng.shuffle(indices)\n    folds = np.array_split(indices, n_folds)\n\n    all_y_true, all_y_pred = [], []\n    for i in range(n_folds):\n        val_idx = folds[i]\n        train_idx = np.concatenate([folds[j] for j in range(n_folds) if j != i])\n        tr = train_df.iloc[train_idx]\n        va = train_df.iloc[val_idx]\n        tr_ds = downsample(tr, \"binary\", rng)\n        clf = XGBClassifier(**XGB_PARAMS)\n        clf.fit(tr_ds[features].values, tr_ds[\"binary\"].values)\n        preds = clf.predict(va[features].values)\n        all_y_true.extend(va[\"binary\"].values)\n        all_y_pred.extend(preds)\n\n    all_y_true = np.array(all_y_true)\n    all_y_pred = np.array(all_y_pred)\n    tn, fp, fn, tp = confusion_matrix(all_y_true, all_y_pred).ravel()\n    tpr = tp / (tp + fn)\n    fpr = fp / (fp + tn)\n    return tpr, fpr\n\n\ndef acc_correct(predicted_prevalence, tpr, fpr):\n    denom = tpr - fpr\n    if abs(denom) < 1e-6:\n        return predicted_prevalence\n    corrected = (predicted_prevalence - fpr) / denom\n    return np.clip(corrected, 0.0, 1.0)\n\n\ndef run_prevalence_estimation(df):\n    generators = sorted(df[\"model_name\"].unique())\n    rng = np.random.RandomState(SEED)\n    all_gen_results = {}\n\n    for gen in generators:\n        print(f\"\\n--- Held-out generator: {gen} ---\")\n        test_df = df[df[\"model_name\"] == gen].copy()\n        train_df = df[df[\"model_name\"] != gen].copy()\n\n        train_bin = train_df[train_df[\"label\"] >= 1].copy()\n        train_bin[\"binary\"] = (train_bin[\"label\"] >= 2).astype(int)\n        test_bin = test_df[test_df[\"label\"] >= 1].copy()\n        test_bin[\"binary\"] = (test_bin[\"label\"] >= 2).astype(int)\n\n        tpr, fpr = estimate_tpr_fpr_cv(train_bin, FEATURES, n_folds=5, seed=SEED)\n        print(f\"  CV TPR={tpr:.4f}, FPR={fpr:.4f}\")\n\n        train_ds = downsample(train_bin, \"binary\", rng)\n        clf = XGBClassifier(**XGB_PARAMS)\n        clf.fit(train_ds[FEATURES].values, train_ds[\"binary\"].values)\n\n        gen1_pool = test_bin[test_bin[\"binary\"] == 0]\n        gen2_pool = test_bin[test_bin[\"binary\"] == 1]\n        n_gen1, n_gen2 = len(gen1_pool), len(gen2_pool)\n        print(f\"  Pool: gen-1={n_gen1}, gen-2+={n_gen2}\")\n\n        corpus_results = []\n        for true_prop in TRUE_PROPORTIONS:\n            n_pos = int(round(CORPUS_SIZE * true_prop))\n            n_neg = CORPUS_SIZE - n_pos\n            if n_neg > n_gen1 or n_pos > n_gen2:\n                continue\n\n            boot_cc, boot_acc, boot_pcc = [], [], []\n            for b in range(N_BOOTSTRAP):\n                brng = np.random.RandomState(SEED + b)\n                s_neg = gen1_pool.sample(n=n_neg, random_state=brng, replace=True)\n                s_pos = gen2_pool.sample(n=n_pos, random_state=brng, replace=True)\n                corpus = pd.concat([s_neg, s_pos], ignore_index=True)\n                X = corpus[FEATURES].values\n\n                preds = clf.predict(X)\n                proba = clf.predict_proba(X)[:, 1]\n\n                cc = float(preds.sum()) / len(preds)\n                acc = float(acc_correct(cc, tpr, fpr))\n                pcc = float(proba.mean())\n\n                boot_cc.append(cc)\n                boot_acc.append(acc)\n                boot_pcc.append(pcc)\n\n            cc_m = float(np.mean(boot_cc))\n            acc_m = float(np.mean(boot_acc))\n            pcc_m = float(np.mean(boot_pcc))\n\n            corpus_results.append({\n                \"true_prop\": true_prop,\n                \"cc_prop\": round(cc_m, 4),\n                \"cc_err\": round(abs(cc_m - true_prop) * 100, 2),\n                \"acc_prop\": round(acc_m, 4),\n                \"acc_err\": round(abs(acc_m - true_prop) * 100, 2),\n                \"pcc_prop\": round(pcc_m, 4),\n                \"pcc_err\": round(abs(pcc_m - true_prop) * 100, 2),\n                \"pcc_ci_lo\": round(float(np.percentile(boot_pcc, 2.5)), 4),\n                \"pcc_ci_hi\": round(float(np.percentile(boot_pcc, 97.5)), 4),\n            })\n            print(f\"  true={true_prop:.0%}  CC={cc_m:.3f}({abs(cc_m-true_prop)*100:.1f}pp)  \"\n                  f\"ACC={acc_m:.3f}({abs(acc_m-true_prop)*100:.1f}pp)  \"\n                  f\"PCC={pcc_m:.3f}({abs(pcc_m-true_prop)*100:.1f}pp)\")\n\n        all_gen_results[gen] = {\n            \"tpr\": round(tpr, 4), \"fpr\": round(fpr, 4),\n            \"corpora\": corpus_results,\n        }\n\n    return all_gen_results\n\n\ndef aggregate_results(all_gen_results):\n    prop_data = {p: {\"cc_err\": [], \"acc_err\": [], \"pcc_err\": [],\n                     \"pcc_pred\": [], \"pcc_ci_lo\": [], \"pcc_ci_hi\": []}\n                 for p in TRUE_PROPORTIONS}\n\n    for gen, res in all_gen_results.items():\n        for c in res[\"corpora\"]:\n            tp = c[\"true_prop\"]\n            prop_data[tp][\"cc_err\"].append(c[\"cc_err\"])\n            prop_data[tp][\"acc_err\"].append(c[\"acc_err\"])\n            prop_data[tp][\"pcc_err\"].append(c[\"pcc_err\"])\n            prop_data[tp][\"pcc_pred\"].append(c[\"pcc_prop\"])\n            prop_data[tp][\"pcc_ci_lo\"].append(c[\"pcc_ci_lo\"])\n            prop_data[tp][\"pcc_ci_hi\"].append(c[\"pcc_ci_hi\"])\n\n    agg = []\n    for tp in TRUE_PROPORTIONS:\n        d = prop_data[tp]\n        if not d[\"pcc_err\"]:\n            continue\n        agg.append({\n            \"true_prop\": tp,\n            \"cc_err_mean\": round(float(np.mean(d[\"cc_err\"])), 2),\n            \"acc_err_mean\": round(float(np.mean(d[\"acc_err\"])), 2),\n            \"pcc_pred_mean\": round(float(np.mean(d[\"pcc_pred\"])), 4),\n            \"pcc_err_mean\": round(float(np.mean(d[\"pcc_err\"])), 2),\n            \"pcc_err_std\": round(float(np.std(d[\"pcc_err\"])), 2),\n            \"pcc_ci_lo_mean\": round(float(np.mean(d[\"pcc_ci_lo\"])), 4),\n            \"pcc_ci_hi_mean\": round(float(np.mean(d[\"pcc_ci_hi\"])), 4),\n        })\n\n    cc_mae = round(float(np.mean([a[\"cc_err_mean\"] for a in agg])), 2)\n    acc_mae = round(float(np.mean([a[\"acc_err_mean\"] for a in agg])), 2)\n    pcc_mae = round(float(np.mean([a[\"pcc_err_mean\"] for a in agg])), 2)\n    return agg, cc_mae, acc_mae, pcc_mae\n\n\ndef plot_calibration(agg, all_gen_results, cc_mae, acc_mae, pcc_mae, out_path):\n    fig, axes = plt.subplots(1, 3, figsize=(14, 4.5))\n\n    methods = [\n        (\"cc\", \"Classify & Count\", cc_mae, \"cc_prop\", \"cc_err\"),\n        (\"acc\", \"Adjusted CC\", acc_mae, \"acc_prop\", \"acc_err\"),\n        (\"pcc\", \"Probabilistic CC\", pcc_mae, \"pcc_prop\", \"pcc_err\"),\n    ]\n\n    for ax, (key, title, mae, prop_key, err_key) in zip(axes, methods):\n        for gen, res in all_gen_results.items():\n            xs = [c[\"true_prop\"] * 100 for c in res[\"corpora\"]]\n            ys = [c[prop_key] * 100 for c in res[\"corpora\"]]\n            ax.scatter(xs, ys, alpha=0.25, s=20, color=\"steelblue\", zorder=2)\n\n        true_pcts = [a[\"true_prop\"] * 100 for a in agg]\n        if key == \"pcc\":\n            pred_pcts = [a[\"pcc_pred_mean\"] * 100 for a in agg]\n            ci_lo = [a[\"pcc_ci_lo_mean\"] * 100 for a in agg]\n            ci_hi = [a[\"pcc_ci_hi_mean\"] * 100 for a in agg]\n            yerr_lo = [p - lo for p, lo in zip(pred_pcts, ci_lo)]\n            yerr_hi = [hi - p for p, hi in zip(pred_pcts, ci_hi)]\n            ax.errorbar(true_pcts, pred_pcts, yerr=[yerr_lo, yerr_hi],\n                        fmt=\"o-\", color=\"darkblue\", capsize=4, capthick=1.5,\n                        markersize=7, zorder=3)\n        else:\n            pred_pcts = []\n            for a in agg:\n                tp = a[\"true_prop\"]\n                vals = []\n                for gen, res in all_gen_results.items():\n                    for c in res[\"corpora\"]:\n                        if c[\"true_prop\"] == tp:\n                            vals.append(c[prop_key] * 100)\n                pred_pcts.append(float(np.mean(vals)))\n            ax.plot(true_pcts, pred_pcts, \"o-\", color=\"darkblue\", markersize=7, zorder=3)\n\n        ax.plot([0, 100], [0, 100], \"k--\", alpha=0.4, linewidth=1)\n        ax.set_xlabel(\"True depth-2+ (%)\", fontsize=10)\n        ax.set_ylabel(\"Predicted depth-2+ (%)\", fontsize=10)\n        ax.set_xlim(-5, 105)\n        ax.set_ylim(-5, 105)\n        ax.set_aspect(\"equal\")\n        ax.set_title(f\"{title}\\nMAE = {mae:.1f}pp\", fontsize=11)\n\n    plt.tight_layout()\n    plt.savefig(out_path, dpi=300, bbox_inches=\"tight\")\n    plt.savefig(out_path.replace(\".pdf\", \".png\"), dpi=150, bbox_inches=\"tight\")\n    print(f\"\\nSaved: {out_path}\")\n\n\ndef main():\n    os.makedirs(RESULTS_DIR, exist_ok=True)\n    print(\"Loading 8-gen data...\")\n    df = load_data()\n    print(f\"Loaded {len(df)} rows, {df['model_name'].nunique()} generators\")\n\n    all_gen_results = run_prevalence_estimation(df)\n    agg, cc_mae, acc_mae, pcc_mae = aggregate_results(all_gen_results)\n\n    best_method = min([(\"CC\", cc_mae), (\"ACC\", acc_mae), (\"PCC\", pcc_mae)], key=lambda x: x[1])\n\n    print(\"\\n\" + \"=\" * 80)\n    print(\"AGGREGATED RESULTS (averaged across 8 held-out generators)\")\n    print(\"=\" * 80)\n    print(f\"{'True %':>8s}  {'CC err':>8s}  {'ACC err':>8s}  {'PCC pred':>9s}  {'PCC err':>8s}  {'PCC 95% CI':>20s}\")\n    for a in agg:\n        print(f\"{a['true_prop']*100:7.0f}%  {a['cc_err_mean']:7.2f}pp  {a['acc_err_mean']:7.2f}pp  \"\n              f\"{a['pcc_pred_mean']*100:8.1f}%  {a['pcc_err_mean']:7.2f}pp  \"\n              f\"[{a['pcc_ci_lo_mean']*100:.1f}%, {a['pcc_ci_hi_mean']*100:.1f}%]\")\n\n    print(f\"\\nCC  MAE = {cc_mae:.2f}pp\")\n    print(f\"ACC MAE = {acc_mae:.2f}pp\")\n    print(f\"PCC MAE = {pcc_mae:.2f}pp\")\n    print(f\"Best: {best_method[0]} ({best_method[1]:.2f}pp)\")\n\n    viable = best_method[1] < 5.0\n    conclusion = \"viable\" if viable else \"not viable\"\n    print(f\"\\nConclusion: corpus-level depth auditing is {conclusion} \"\n          f\"(best MAE = {best_method[1]:.2f}pp {'<' if viable else '>='} 5pp)\")\n\n    out = {\n        \"corpus_size\": CORPUS_SIZE,\n        \"n_bootstrap\": N_BOOTSTRAP,\n        \"n_generators\": len(all_gen_results),\n        \"per_generator\": all_gen_results,\n        \"aggregated\": agg,\n        \"cc_mae_pp\": cc_mae,\n        \"acc_mae_pp\": acc_mae,\n        \"pcc_mae_pp\": pcc_mae,\n        \"best_method\": best_method[0],\n        \"best_mae_pp\": best_method[1],\n        \"conclusion\": conclusion,\n    }\n    json_path = os.path.join(RESULTS_DIR, \"corpus_prevalence_demo.json\")\n    with open(json_path, \"w\") as f:\n        json.dump(out, f, indent=2)\n    print(f\"Saved: {json_path}\")\n\n    pdf_path = os.path.join(RESULTS_DIR, \"corpus_prevalence_calibration.pdf\")\n    plot_calibration(agg, all_gen_results, cc_mae, acc_mae, pcc_mae, pdf_path)\n\n\nif __name__ == \"__main__\":\n    main()\nPYEOF\necho \"Script updated.\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-17T23:31:25.645385+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Script updated.\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.31}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_corpus-prevalence_20260517T231957",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-17T23:31:25.645511+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-5090",
  "command": "source /root/miniconda3/bin/activate && cd /root/gen-depth-fingerprint && python corpus_prevalence_demo.py 2>&1 | tee logs/corpus_prevalence_demo.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_corpus-prevalence_20260517T231957",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-5090",
    "command": "source /root/miniconda3/bin/activate && cd /root/gen-depth-fingerprint && python corpus_prevalence_demo.py 2>&1 | tee logs/corpus_prevalence_demo.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-17T23:31:25.645739+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/miniconda3/lib/python3.12/site-packages/xgboost/training.py:200: UserWarning: [07:26:03] WARNING: /__w/xgboost/xgboost/src/learner.cc:782: \\nParameters: { \\\"use_label_encoder\\\" } are not used.\\n\\n  bst.update(dtrain, iteration=i, fobj=obj)\\n/root/miniconda3/lib/python3.12/site-packages/xgboost/training.py:200: UserWarning: [07:26:03] WARNING: /__w/xgboost/xgboost/src/learner.cc:782: \\nParameters: { \\\"use_label_encoder\\\" } are not used.\\n\\n  bst.update(dtrain, iteration=i, fobj=obj)\\n/root/miniconda3/lib/python3.12/site-packages/xgboost/training.py:200: UserWarning: [07:26:04] WARNING: /__w/xgboost/xgboost/src/learner.cc:782: \\nParameters: { \\\"use_label_encoder\\\" } are not used.\\n\\n  bst.update(dtrain, iteration=i, fobj=obj)\\n/root/miniconda3/lib/python3.12/site-packages/xgboost/training.py:200: UserWarning: [07:26:04] WARNING: /__w/xgboost/xgboost/src/learner.cc:782: \\nParameters: { \\\"use_label_encoder\\\" } are not used.\\n\\n  bst.update(dtrain, iteration=i, fobj=obj)\\n/root/miniconda3/lib/python3.12/site-packages/xgboost/training.py:200: UserWarning: [07:26:04] WARNING: /__w/xgboost/xgboost/src/learner.cc:782: \\nParameters: { \\\"use_label_encoder\\\" } are not used.\\n\\n  bst.update(dtrain, iteration=i, fobj=obj)\\n/root/miniconda3/lib/python3.12/site-packages/xgboost/training.py:200: UserWarning: [07:26:04] WARNING: /__w/xgboost/xgboost/src/learner.cc:782: \\nParameters: { \\\"use_label_encoder\\\" } are not used.\\n\\n  bst.update(dtrain, iteration=i, fobj=obj)\\n/root/miniconda3/lib/python3.12/site-packages/xgboost/training.py:200: UserWarning: [07:26:07] WARNING: /__w/xgboost/xgboost/src/learner.cc:782: \\nParameters: { \\\"use_label_encoder\\\" } are not used.\\n\\n  bst.update(dtrain, iteration=i, fobj=obj)\\n/root/miniconda3/lib/python3.12/site-packages/xgboost/training.py:200: UserWarning: [07:26:07] WARNING: /__w/xgboost/xgboost/src/learner.cc:782: \\nParameters:
…[truncated 6593 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_corpus-prevalence_20260517T231957",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-17T23:31:25.645970+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat > /root/gen-depth-fingerprint/corpus_prevalence_demo.py << 'PYEOF'\n\"\"\"\ncorpus_prevalence_demo.py — Corpus-level depth prevalence estimation.\n\nBuild 5 synthetic corpora with known depth-2+ proportions (0%, 25%, 50%, 75%, 100%).\nUse LOGO-trained XGBoost with four quantification methods:\n  CC  — Classify & Count (hard predictions)\n  ACC — Adjusted CC (correct with CV-estimated TPR/FPR)  \n  PCC — Probabilistic CC (mean predicted probability)\n  EMQ — EM-based quantification (Saerens et al. 2002)\nReport calibration MAE for each.\n\"\"\"\n\nimport json\nimport os\nimport numpy as np\nimport pandas as pd\nfrom xgboost import XGBClassifier\nfrom sklearn.metrics import confusion_matrix\nimport matplotlib\nmatplotlib.use(\"Agg\")\nimport matplotlib.pyplot as plt\n\nSEED = 42\nFEATURES = [\"entropy_mean\", \"entropy_std\", \"entropy_min\", \"entropy_max\",\n            \"tail_decay\", \"ttr\", \"hapax_ratio\"]\n\nXGB_PARAMS = dict(n_estimators=200, max_depth=6, learning_rate=0.1,\n                  random_state=SEED, eval_metric=\"mlogloss\",\n                  use_label_encoder=False)\n\nCLASS_MAP_3 = {0: 0, 1: 1, 2: 2, 3: 2, 4: 2}\n\nROOT = os.path.dirname(os.path.abspath(__file__))\nDATA_DIR = os.path.join(ROOT, \"data\")\nRESULTS_DIR = os.path.join(ROOT, \"results\")\n\nCORPUS_SIZE = 800\nTRUE_PROPORTIONS = [0.0, 0.25, 0.50, 0.75, 1.00]\nN_BOOTSTRAP = 200\n\n\ndef load_data():\n    df_base = pd.read_csv(os.path.join(DATA_DIR, \"features_all_models.csv\"))\n    new_gens = [\n        (\"llama-3.2-3b\", os.path.join(DATA_DIR, \"llama-3.2-3b\", \"features_pythia410m.jsonl\")),\n        (\"mistral-7b-v0.3\", os.path.join(DATA_DIR, \"mistral-7b-v0.3\", \"features_pythia410m.jsonl\")),\n    ]\n    dfs = [df_base]\n    for gen_name, path in new_gens:\n        records = []\n        with open(path) as f:\n            for line in f:\n                rec = json.loads(line)\n                rec[\"model_name\"] = gen_name\n                records.append(rec)\n        dfs.append(pd.DataFrame(records))\n    cols = [\"model_name\", \"seed_id\", \"depth\"] + FEATURES\n    df = pd.concat([d[cols] for d in dfs], ignore_index=True)\n    df[\"label\"] = df[\"depth\"].map(CLASS_MAP_3)\n    return df\n\n\ndef downsample(df, label_col, rng):\n    counts = df[label_col].value_counts()\n    min_n = counts.min()\n    parts = []\n    for lbl in sorted(counts.index):\n        sub = df[df[label_col] == lbl]\n        parts.append(sub.sample(n=min_n, random_state=rng, replace=False))\n    return pd.concat(parts, ignore_index=True)\n\n\ndef estimate_tpr_fpr_cv(train_df, features, n_folds=5, seed=42):\n    rng = np.random.RandomState(seed)\n    indices = np.arange(len(train_df))\n    rng.shuffle(indices)\n    folds = np.array_split(indices, n_folds)\n    all_y_true, all_y_pred = [], []\n    for i in range(n_folds):\n        val_idx = folds[i]\n        train_idx = np.concatenate([folds[j] for j in range(n_folds) if j != i])\n        tr = train_df.iloc[train_idx]\n        va = train_df.iloc[val_idx]\n        tr_ds = downsample(tr, \"binary\", rng)\n        clf = XGBClassifier(**XGB_PARAMS)\n        clf.fit(tr_ds[features].values, tr_ds[\"binary\"].values)\n        preds = clf.predict(va[features].values)\n        all_y_true.extend(va[\"binary\"].values)\n        all_y_pred.extend(preds)\n    tn, fp, fn, tp = confusion_matrix(np.array(all_y_true), np.array(all_y_pred)).ravel()\n    return tp / (tp + fn), fp / (fp + tn)\n\n\ndef acc_correct(prev, tpr, fpr):\n    d = tpr - fpr\n    if abs(d) < 1e-6:\n        return prev\n    return float(np.clip((prev - fpr) / d, 0, 1))\n\n\ndef emq_prevalence(proba_pos, train_prevalence, max_iter=100, tol=1e-6):\n    \"\"\"EM quantification (Saerens et al. 2002). Returns estimated positive prevalence.\"\"\"\n    n = len(proba_pos)\n    proba_neg = 1.0 - proba_pos\n    pi_train = np.array([1.0 - train_prevalence, train_prevalence])\n    pi = pi_train.copy()\n\n    for _ in range(max_iter):\n        # E-step: adjust posteriors with new priors\n        ratio = pi / pi_train\n        adj_pos = proba_pos * ratio[1]\n        adj_neg = proba_neg * ratio[0]\n        denom = adj_pos + adj_neg\n        denom = np.maximum(denom, 1e-10)\n        post_pos = adj_pos / denom\n\n        # M-step: new prevalence = mean adjusted posterior\n        new_pi1 = float(np.mean(post_pos))\n        new_pi = np.array([1.0 - new_pi1, new_pi1])\n\n        if np.max(np.abs(new_pi - pi)) < tol:\n            pi = new_pi\n            break\n        pi = new_pi\n\n    return float(np.clip(pi[1], 0, 1))\n\n\ndef run_prevalence_estimation(df):\n    generators = sorted(df[\"model_name\"].unique())\n    rng = np.random.RandomState(SEED)\n    all_gen_results = {}\n\n    for gen in generators:\n        print(f\"\\n--- Held-out: {gen} ---\")\n        test_df = df[df[\"model_name\"] == gen].copy()\n        train_df = df[df[\"model_name\"] != gen].copy()\n\n        train_bin = train_df[train_df[\"label\"] >= 1].copy()\n        train_bin[\"binary\"] = (train_bin[\"label\"] >= 2).astype(int)\n        test_bin = test_df[test_df[\"label\"] >= 1].copy()\n        test_bin[\"binary\"] = (test_bin[\"label\"] >= 2).astype(int)\n\n        tpr, fpr = estimate_tpr_fpr_cv(train_bin, FEATURES, n_folds=5, seed=SEED)\n\n        train_ds = downsample(train_bin, \"binary\", rng)\n        train_prev = float(train_ds[\"binary\"].mean())\n        clf = XGBClassifier(**XGB_PARAMS)\n        clf.fit(train_ds[FEATURES].values, train_ds[\"binary\"].values)\n\n        gen1_pool = test_bin[test_bin[\"binary\"] == 0]\n        gen2_pool = test_bin[test_bin[\"binary\"] == 1]\n        n_gen1, n_gen2 = len(gen1_pool), len(gen2_pool)\n\n        corpus_results = []\n        for true_prop in TRUE_PROPORTIONS:\n            n_pos = int(round(CORPUS_SIZE * true_prop))\n            n_neg = CORPUS_SIZE - n_pos\n            if n_neg > n_gen1 or n_pos > n_gen2:\n                continue\n\n            boot_cc, boot_acc, boot_pcc, boot_emq = [], [], [], []\n            for b in range(N_BOOTSTRAP):\n                brng = np.random.RandomState(SEED + b)\n                s_neg = gen1_pool.sample(n=n_neg, random_state=brng, replace=True)\n                s_pos = gen2_pool.sample(n=n_pos, random_state=brng, replace=True)\n                corpus = pd.concat([s_neg, s_pos], ignore_index=True)\n                X = corpus[FEATURES].values\n\n                preds = clf.predict(X)\n                proba = clf.predict_proba(X)[:, 1]\n\n                cc = float(preds.sum()) / len(preds)\n                acc_v = acc_correct(cc, tpr, fpr)\n                pcc = float(proba.mean())\n                emq = emq_prevalence(proba, train_prev)\n\n                boot_cc.append(cc)\n                boot_acc.append(acc_v)\n                boot_pcc.append(pcc)\n                boot_emq.append(emq)\n\n            results = {}\n            for name, arr in [(\"cc\", boot_cc), (\"acc\", boot_acc),\n                              (\"pcc\", boot_pcc), (\"emq\", boot_emq)]:\n                m = float(np.mean(arr))\n                results[f\"{name}_prop\"] = round(m, 4)\n                results[f\"{name}_err\"] = round(abs(m - true_prop) * 100, 2)\n                results[f\"{name}_ci_lo\"] = round(float(np.percentile(arr, 2.5)), 4)\n                results[f\"{name}_ci_hi\"] = round(float(np.percentile(arr, 97.5)), 4)\n            results[\"true_prop\"] = true_prop\n\n            corpus_results.append(results)\n            print(f\"  {true_prop:.0%}  CC={results['cc_err']:.1f}  ACC={results['acc_err']:.1f}  \"\n                  f\"PCC={results['pcc_err']:.1f}  EMQ={results['emq_err']:.1f}pp\")\n\n        all_gen_results[gen] = {\"tpr\": round(tpr, 4), \"fpr\": round(fpr, 4),\n                                \"corpora\": corpus_results}\n\n    return all_gen_results\n\n\ndef aggregate_results(all_gen_results):\n    methods = [\"cc\", \"acc\", \"pcc\", \"emq\"]\n    prop_data = {p: {m: {\"err\": [], \"pred\": [], \"ci_lo\": [], \"ci_hi\": []}\n                     for m in methods} for p in TRUE_PROPORTIONS}\n\n    for gen, res in all_gen_results.items():\n        for c in res[\"corpora\"]:\n            tp = c[\"true_prop\"]\n            for m in methods:\n                prop_data[tp][m][\"err\"].append(c[f\"{m}_err\"])\n                prop_data[tp][m][\"pred\"].append(c[f\"{m}_prop\"])\n                prop_data[tp][m][\"ci_lo\"].append(c[f\"{m}_ci_lo\"])\n                prop_data[tp][m][\"ci_hi\"].append(c[f\"{m}_ci_hi\"])\n\n    agg = []\n    for tp in TRUE_PROPORTIONS:\n        if not prop_data[tp][\"cc\"][\"err\"]:\n            continue\n        entry = {\"true_prop\": tp}\n        for m in methods:\n            d = prop_data[tp][m]\n            entry[f\"{m}_pred_mean\"] = round(float(np.mean(d[\"pred\"])), 4)\n            entry[f\"{m}_err_mean\"] = round(float(np.mean(d[\"err\"])), 2)\n            entry[f\"{m}_ci_lo_mean\"] = round(float(np.mean(d[\"ci_lo\"])), 4)\n            entry[f\"{m}_ci_hi_mean\"] = round(float(np.mean(d[\"ci_hi\"])), 4)\n        agg.append(entry)\n\n    maes = {}\n    for m in methods:\n        maes[m] = round(float(np.mean([a[f\"{m}_err_mean\"] for a in agg])), 2)\n    return agg, maes\n\n\ndef plot_calibration(agg, all_gen_results, maes, out_path):\n    methods = [\n        (\"cc\", \"Classify & Count\"),\n        (\"acc\", \"Adjusted CC\"),\n        (\"emq\", \"EM Quantification\"),\n    ]\n    fig, axes = plt.subplots(1, 3, figsize=(14, 4.5))\n\n    for ax, (key, title) in zip(axes, methods):\n        mae = maes[key]\n        for gen, res in all_gen_results.items():\n            xs = [c[\"true_prop\"] * 100 for c in res[\"corpora\"]]\n            ys = [c[f\"{key}_prop\"] * 100 for c in res[\"corpora\"]]\n            ax.scatter(xs, ys, alpha=0.25, s=20, color=\"steelblue\", zorder=2)\n\n        true_pcts = [a[\"true_prop\"] * 100 for a in agg]\n        pred_pcts = [a[f\"{key}_pred_mean\"] * 100 for a in agg]\n        ci_lo = [a[f\"{key}_ci_lo_mean\"] * 100 for a in agg]\n        ci_hi = [a[f\"{key}_ci_hi_mean\"] * 100 for a in agg]\n        yerr_lo = [p - lo for p, lo in zip(pred_pcts, ci_lo)]\n        yerr_hi = [hi - p for p, hi in zip(pred_pcts, ci_hi)]\n        ax.errorbar(true_pcts, pred_pcts, yerr=[yerr_lo, yerr_hi],\n                    fmt=\"o-\", color=\"darkblue\", capsize=4, capthick=1.5,\n                    markersize=7, zorder=3)\n\n        ax.plot([0, 100], [0, 100], \"k--\", alpha=0.4, linewidth=1)\n        ax.set_xlabel(\"True depth-2+ (%)\", fontsize=10)\n        ax.set_ylabel(\"Predicted depth-2+ (%)\", fontsize=10)\n        ax.set_xlim(-5, 105)\n        ax.set_ylim(-5, 105)\n        ax.set_aspect(\"equal\")\n        ax.set_title(f\"{title}\\nMAE = {mae:.1f}pp\", fontsize=11)\n\n    plt.tight_layout()\n    plt.savefig(out_path, dpi=300, bbox_inches=\"tight\")\n    plt.savefig(out_path.replace(\".pdf\", \".png\"), dpi=150, bbox_inches=\"tight\")\n    print(f\"\\nSaved: {out_path}\")\n\n\ndef main():\n    os.makedirs(RESULTS_DIR, exist_ok=True)\n    print(\"Loading 8-gen data...\")\n    df = load_data()\n    print(f\"Loaded {len(df)} rows, {df['model_name'].nunique()} generators\")\n\n    all_gen_results = run_prevalence_estimation(df)\n    agg, maes = aggregate_results(all_gen_results)\n\n    best_name = min(maes, key=maes.get)\n    best_mae = maes[best_name]\n\n    print(\"\\n\" + \"=\" * 85)\n    print(\"AGGREGATED RESULTS (averaged across 8 held-out generators)\")\n    print(\"=\" * 85)\n    header = f\"{'True':>6s}\"\n    for m in [\"cc\", \"acc\", \"pcc\", \"emq\"]:\n        header += f\"  {m.upper()+' pred':>9s} {m.upper()+' err':>8s}\"\n    print(header)\n    for a in agg:\n        line = f\"{a['true_prop']*100:5.0f}%\"\n        for m in [\"cc\", \"acc\", \"pcc\", \"emq\"]:\n            line += f\"  {a[f'{m}_pred_mean']*100:8.1f}% {a[f'{m}_err_mean']:7.2f}pp\"\n        print(line)\n\n    print()\n    for m in [\"cc\", \"acc\", \"pcc\", \"emq\"]:\n        marker = \" <-- best\" if m == best_name else \"\"\n        print(f\"  {m.upper():4s} MAE = {maes[m]:6.2f}pp{marker}\")\n\n    viable = best_mae < 5.0\n    conclusion = \"viable\" if viable else \"not viable\"\n    print(f\"\\nConclusion: corpus-level depth auditing is {conclusion} \"\n          f\"(best MAE = {best_mae:.2f}pp, method={best_name.upper()}, threshold=5pp)\")\n\n    out = {\n        \"corpus_size\": CORPUS_SIZE,\n        \"n_bootstrap\": N_BOOTSTRAP,\n        \"n_generators\": len(all_gen_results),\n        \"per_generator\": all_gen_results,\n        \"aggregated\": agg,\n        \"maes\": maes,\n        \"best_method\": best_name.upper(),\n        \"best_mae_pp\": best_mae,\n        \"conclusion\": conclusion,\n    }\n    json_path = os.path.join(RESULTS_DIR, \"corpus_prevalence_demo.json\")\n    with open(json_path, \"w\") as f:\n        json.dump(out, f, indent=2)\n    print(f\"Saved: {json_path}\")\n\n    pdf_path = os.path.join(RESULTS_DIR, \"corpus_prevalence_calibration.pdf\")\n    plot_calibration(agg, all_gen_results, maes, pdf_path)\n\n\nif __name__ == \"__main__\":\n    main()\nPYEOF\necho \"Script updated with EMQ.\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_corpus-prevalence_20260517T231957",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat > /root/gen-depth-fingerprint/corpus_prevalence_demo.py << 'PYEOF'\n\"\"\"\ncorpus_prevalence_demo.py — Corpus-level depth prevalence estimation.\n\nBuild 5 synthetic corpora with known depth-2+ proportions (0%, 25%, 50%, 75%, 100%).\nUse LOGO-trained XGBoost with four quantification methods:\n  CC  — Classify & Count (hard predictions)\n  ACC — Adjusted CC (correct with CV-estimated TPR/FPR)  \n  PCC — Probabilistic CC (mean predicted probability)\n  EMQ — EM-based quantification (Saerens et al. 2002)\nReport calibration MAE for each.\n\"\"\"\n\nimport json\nimport os\nimport numpy as np\nimport pandas as pd\nfrom xgboost import XGBClassifier\nfrom sklearn.metrics import confusion_matrix\nimport matplotlib\nmatplotlib.use(\"Agg\")\nimport matplotlib.pyplot as plt\n\nSEED = 42\nFEATURES = [\"entropy_mean\", \"entropy_std\", \"entropy_min\", \"entropy_max\",\n            \"tail_decay\", \"ttr\", \"hapax_ratio\"]\n\nXGB_PARAMS = dict(n_estimators=200, max_depth=6, learning_rate=0.1,\n                  random_state=SEED, eval_metric=\"mlogloss\",\n                  use_label_encoder=False)\n\nCLASS_MAP_3 = {0: 0, 1: 1, 2: 2, 3: 2, 4: 2}\n\nROOT = os.path.dirname(os.path.abspath(__file__))\nDATA_DIR = os.path.join(ROOT, \"data\")\nRESULTS_DIR = os.path.join(ROOT, \"results\")\n\nCORPUS_SIZE = 800\nTRUE_PROPORTIONS = [0.0, 0.25, 0.50, 0.75, 1.00]\nN_BOOTSTRAP = 200\n\n\ndef load_data():\n    df_base = pd.read_csv(os.path.join(DATA_DIR, \"features_all_models.csv\"))\n    new_gens = [\n        (\"llama-3.2-3b\", os.path.join(DATA_DIR, \"llama-3.2-3b\", \"features_pythia410m.jsonl\")),\n        (\"mistral-7b-v0.3\", os.path.join(DATA_DIR, \"mistral-7b-v0.3\", \"features_pythia410m.jsonl\")),\n    ]\n    dfs = [df_base]\n    for gen_name, path in new_gens:\n        records = []\n        with open(path) as f:\n            for line in f:\n                rec = json.loads(line)\n                rec[\"model_name\"] = gen_name\n                records.append(rec)\n        dfs.append(pd.DataFrame(records))\n    cols = [\"model_name\", \"seed_id\", \"depth\"] + FEATURES\n    df = pd.concat([d[cols] for d in dfs], ignore_index=True)\n    df[\"label\"] = df[\"depth\"].map(CLASS_MAP_3)\n    return df\n\n\ndef downsample(df, label_col, rng):\n    counts = df[label_col].value_counts()\n    min_n = counts.min()\n    parts = []\n    for lbl in sorted(counts.index):\n        sub = df[df[label_col] == lbl]\n        parts.append(sub.sample(n=min_n, random_state=rng, replace=False))\n    return pd.concat(parts, ignore_index=True)\n\n\ndef estimate_tpr_fpr_cv(train_df, features, n_folds=5, seed=42):\n    rng = np.random.RandomState(seed)\n    indices = np.arange(len(train_df))\n    rng.shuffle(indices)\n    folds = np.array_split(indices, n_folds)\n    all_y_true, all_y_pred = [], []\n    for i in range(n_folds):\n        val_idx = folds[i]\n        train_idx = np.concatenate([folds[j] for j in range(n_folds) if j != i])\n        tr = train_df.iloc[train_idx]\n        va = train_df.iloc[val_idx]\n        tr_ds = downsample(tr, \"binary\", rng)\n        clf = XGBClassifier(**XGB_PARAMS)\n        clf.fit(tr_ds[features].values, tr_ds[\"binary\"].values)\n        preds = clf.predict(va[features].values)\n        all_y_true.extend(va[\"binary\"].values)\n        all_y_pred.extend(preds)\n    tn, fp, fn, tp = confusion_matrix(np.array(all_y_true), np.array(all_y_pred)).ravel()\n    return tp / (tp + fn), fp / (fp + tn)\n\n\ndef acc_correct(prev, tpr, fpr):\n    d = tpr - fpr\n    if abs(d) < 1e-6:\n        return prev\n    return float(np.clip((prev - fpr) / d, 0, 1))\n\n\ndef emq_prevalence(proba_pos, train_prevalence, max_iter=100, tol=1e-6):\n    \"\"\"EM quantification (Saerens et al. 2002). Returns estimated positive prevalence.\"\"\"\n    n = len(proba_pos)\n    proba_neg = 1.0 - proba_pos\n    pi_train = np.array([1.0 - train_prevalence, train_prevalence])\n    pi = pi_train.copy()\n\n    for _ in range(max_iter):\n        # E-step: adjust posteriors with new priors\n        ratio = pi / pi_train\n        adj_pos = proba_pos * ratio[1]\n        adj_neg = proba_neg * ratio[0]\n        denom = adj_pos + adj_neg\n        denom = np.maximum(denom, 1e-10)\n        post_pos = adj_pos / denom\n\n        # M-step: new prevalence = mean adjusted posterior\n        new_pi1 = float(np.mean(post_pos))\n        new_pi = np.array([1.0 - new_pi1, new_pi1])\n\n        if np.max(np.abs(new_pi - pi)) < tol:\n            pi = new_pi\n            break\n        pi = new_pi\n\n    return float(np.clip(pi[1], 0, 1))\n\n\ndef run_prevalence_estimation(df):\n    generators = sorted(df[\"model_name\"].unique())\n    rng = np.random.RandomState(SEED)\n    all_gen_results = {}\n\n    for gen in generators:\n        print(f\"\\n--- Held-out: {gen} ---\")\n        test_df = df[df[\"model_name\"] == gen].copy()\n        train_df = df[df[\"model_name\"] != gen].copy()\n\n        train_bin = train_df[train_df[\"label\"] >= 1].copy()\n        train_bin[\"binary\"] = (train_bin[\"label\"] >= 2).astype(int)\n        test_bin = test_df[test_df[\"label\"] >= 1].copy()\n        test_bin[\"binary\"] = (test_bin[\"label\"] >= 2).astype(int)\n\n        tpr, fpr = estimate_tpr_fpr_cv(train_bin, FEATURES, n_folds=5, seed=SEED)\n\n        train_ds = downsample(train_bin, \"binary\", rng)\n        train_prev = float(train_ds[\"binary\"].mean())\n        clf = XGBClassifier(**XGB_PARAMS)\n        clf.fit(train_ds[FEATURES].values, train_ds[\"binary\"].values)\n\n        gen1_pool = test_bin[test_bin[\"binary\"] == 0]\n        gen2_pool = test_bin[test_bin[\"binary\"] == 1]\n        n_gen1, n_gen2 = len(gen1_pool), len(gen2_pool)\n\n        corpus_results = []\n        for true_prop in TRUE_PROPORTIONS:\n            n_pos = int(round(CORPUS_SIZE * true_prop))\n            n_neg = CORPUS_SIZE - n_pos\n            if n_neg > n_gen1 or n_pos > n_gen2:\n                continue\n\n            boot_cc, boot_acc, boot_pcc, boot_emq = [], [], [], []\n            for b in range(N_BOOTSTRAP):\n                brng = np.random.RandomState(SEED + b)\n                s_neg = gen1_pool.sample(n=n_neg, random_state=brng, replace=True)\n                s_pos = gen2_pool.sample(n=n_pos, random_state=brng, replace=True)\n                corpus = pd.concat([s_neg, s_pos], ignore_index=True)\n                X = corpus[FEATURES].values\n\n                preds = clf.predict(X)\n                proba = clf.predict_proba(X)[:, 1]\n\n                cc = float(preds.sum()) / len(preds)\n                acc_v = acc_correct(cc, tpr, fpr)\n                pcc = float(proba.mean())\n                emq = emq_prevalence(proba, train_prev)\n\n                boot_cc.append(cc)\n                boot_acc.append(acc_v)\n                boot_pcc.append(pcc)\n                boot_emq.append(emq)\n\n            results = {}\n            for name, arr in [(\"cc\", boot_cc), (\"acc\", boot_acc),\n                              (\"pcc\", boot_pcc), (\"emq\", boot_emq)]:\n                m = float(np.mean(arr))\n                results[f\"{name}_prop\"] = round(m, 4)\n                results[f\"{name}_err\"] = round(abs(m - true_prop) * 100, 2)\n                results[f\"{name}_ci_lo\"] = round(float(np.percentile(arr, 2.5)), 4)\n                results[f\"{name}_ci_hi\"] = round(float(np.percentile(arr, 97.5)), 4)\n            results[\"true_prop\"] = true_prop\n\n            corpus_results.append(results)\n            print(f\"  {true_prop:.0%}  CC={results['cc_err']:.1f}  ACC={results['acc_err']:.1f}  \"\n                  f\"PCC={results['pcc_err']:.1f}  EMQ={results['emq_err']:.1f}pp\")\n\n        all_gen_results[gen] = {\"tpr\": round(tpr, 4), \"fpr\": round(fpr, 4),\n                                \"corpora\": corpus_results}\n\n    return all_gen_results\n\n\ndef aggregate_results(all_gen_results):\n    methods = [\"cc\", \"acc\", \"pcc\", \"emq\"]\n    prop_data = {p: {m: {\"err\": [], \"pred\": [], \"ci_lo\": [], \"ci_hi\": []}\n                     for m in methods} for p in TRUE_PROPORTIONS}\n\n    for gen, res in all_gen_results.items():\n        for c in res[\"corpora\"]:\n            tp = c[\"true_prop\"]\n            for m in methods:\n                prop_data[tp][m][\"err\"].append(c[f\"{m}_err\"])\n                prop_data[tp][m][\"pred\"].append(c[f\"{m}_prop\"])\n                prop_data[tp][m][\"ci_lo\"].append(c[f\"{m}_ci_lo\"])\n                prop_data[tp][m][\"ci_hi\"].append(c[f\"{m}_ci_hi\"])\n\n    agg = []\n    for tp in TRUE_PROPORTIONS:\n        if not prop_data[tp][\"cc\"][\"err\"]:\n            continue\n        entry = {\"true_prop\": tp}\n        for m in methods:\n            d = prop_data[tp][m]\n            entry[f\"{m}_pred_mean\"] = round(float(np.mean(d[\"pred\"])), 4)\n            entry[f\"{m}_err_mean\"] = round(float(np.mean(d[\"err\"])), 2)\n            entry[f\"{m}_ci_lo_mean\"] = round(float(np.mean(d[\"ci_lo\"])), 4)\n            entry[f\"{m}_ci_hi_mean\"] = round(float(np.mean(d[\"ci_hi\"])), 4)\n        agg.append(entry)\n\n    maes = {}\n    for m in methods:\n        maes[m] = round(float(np.mean([a[f\"{m}_err_mean\"] for a in agg])), 2)\n    return agg, maes\n\n\ndef plot_calibration(agg, all_gen_results, maes, out_path):\n    methods = [\n        (\"cc\", \"Classify & Count\"),\n        (\"acc\", \"Adjusted CC\"),\n        (\"emq\", \"EM Quantification\"),\n    ]\n    fig, axes = plt.subplots(1, 3, figsize=(14, 4.5))\n\n    for ax, (key, title) in zip(axes, methods):\n        mae = maes[key]\n        for gen, res in all_gen_results.items():\n            xs = [c[\"true_prop\"] * 100 for c in res[\"corpora\"]]\n            ys = [c[f\"{key}_prop\"] * 100 for c in res[\"corpora\"]]\n            ax.scatter(xs, ys, alpha=0.25, s=20, color=\"steelblue\", zorder=2)\n\n        true_pcts = [a[\"true_prop\"] * 100 for a in agg]\n        pred_pcts = [a[f\"{key}_pred_mean\"] * 100 for a in agg]\n        ci_lo = [a[f\"{key}_ci_lo_mean\"] * 100 for a in agg]\n        ci_hi = [a[f\"{key}_ci_hi_mean\"] * 100 for a in agg]\n        yerr_lo = [p - lo for p, lo in zip(pred_pcts, ci_lo)]\n        yerr_hi = [hi - p for p, hi in zip(pred_pcts, ci_hi)]\n        ax.errorbar(true_pcts, pred_pcts, yerr=[yerr_lo, yerr_hi],\n                    fmt=\"o-\", color=\"darkblue\", capsize=4, capthick=1.5,\n                    markersize=7, zorder=3)\n\n        ax.plot([0, 100], [0, 100], \"k--\", alpha=0.4, linewidth=1)\n        ax.set_xlabel(\"True depth-2+ (%)\", fontsize=10)\n        ax.set_ylabel(\"Predicted depth-2+ (%)\", fontsize=10)\n        ax.set_xlim(-5, 105)\n        ax.set_ylim(-5, 105)\n        ax.set_aspect(\"equal\")\n        ax.set_title(f\"{title}\\nMAE = {mae:.1f}pp\", fontsize=11)\n\n    plt.tight_layout()\n    plt.savefig(out_path, dpi=300, bbox_inches=\"tight\")\n    plt.savefig(out_path.replace(\".pdf\", \".png\"), dpi=150, bbox_inches=\"tight\")\n    print(f\"\\nSaved: {out_path}\")\n\n\ndef main():\n    os.makedirs(RESULTS_DIR, exist_ok=True)\n    print(\"Loading 8-gen data...\")\n    df = load_data()\n    print(f\"Loaded {len(df)} rows, {df['model_name'].nunique()} generators\")\n\n    all_gen_results = run_prevalence_estimation(df)\n    agg, maes = aggregate_results(all_gen_results)\n\n    best_name = min(maes, key=maes.get)\n    best_mae = maes[best_name]\n\n    print(\"\\n\" + \"=\" * 85)\n    print(\"AGGREGATED RESULTS (averaged across 8 held-out generators)\")\n    print(\"=\" * 85)\n    header = f\"{'True':>6s}\"\n    for m in [\"cc\", \"acc\", \"pcc\", \"emq\"]:\n        header += f\"  {m.upper()+' pred':>9s} {m.upper()+' err':>8s}\"\n    print(header)\n    for a in agg:\n        line = f\"{a['true_prop']*100:5.0f}%\"\n        for m in [\"cc\", \"acc\", \"pcc\", \"emq\"]:\n            line += f\"  {a[f'{m}_pred_mean']*100:8.1f}% {a[f'{m}_err_mean']:7.2f}pp\"\n        print(line)\n\n    print()\n    for m in [\"cc\", \"acc\", \"pcc\", \"emq\"]:\n        marker = \" <-- best\" if m == best_name else \"\"\n        print(f\"  {m.upper():4s} MAE = {maes[m]:6.2f}pp{marker}\")\n\n    viable = best_mae < 5.0\n    conclusion = \"viable\" if viable else \"not viable\"\n    print(f\"\\nConclusion: corpus-level depth auditing is {conclusion} \"\n          f\"(best MAE = {best_mae:.2f}pp, method={best_name.upper()}, threshold=5pp)\")\n\n    out = {\n        \"corpus_size\": CORPUS_SIZE,\n        \"n_bootstrap\": N_BOOTSTRAP,\n        \"n_generators\": len(all_gen_results),\n        \"per_generator\": all_gen_results,\n        \"aggregated\": agg,\n        \"maes\": maes,\n        \"best_method\": best_name.upper(),\n        \"best_mae_pp\": best_mae,\n        \"conclusion\": conclusion,\n    }\n    json_path = os.path.join(RESULTS_DIR, \"corpus_prevalence_demo.json\")\n    with open(json_path, \"w\") as f:\n        json.dump(out, f, indent=2)\n    print(f\"Saved: {json_path}\")\n\n    pdf_path = os.path.join(RESULTS_DIR, \"corpus_prevalence_calibration.pdf\")\n    plot_calibration(agg, all_gen_results, maes, pdf_path)\n\n\nif __name__ == \"__main__\":\n    main()\nPYEOF\necho \"Script updated with EMQ.\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-17T23:31:25.646228+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Script updated with EMQ.\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.31}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_corpus-prevalence_20260517T231957",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-17T23:31:25.646357+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-5090",
  "command": "source /root/miniconda3/bin/activate && cd /root/gen-depth-fingerprint && python corpus_prevalence_demo.py 2>&1 | tee logs/corpus_prevalence_demo.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_corpus-prevalence_20260517T231957",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-5090",
    "command": "source /root/miniconda3/bin/activate && cd /root/gen-depth-fingerprint && python corpus_prevalence_demo.py 2>&1 | tee logs/corpus_prevalence_demo.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-17T23:31:25.646486+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Command did not complete within 30 seconds!\\n\\nCommand: 'source /root/miniconda3/bin/activate && cd /root/gen-depth-fingerprint && python corpus_prevalence_demo.py 2>&1 | tee logs/corpus_prevalence_demo.log'\\n\\nStdout:\\n\\n\\n  bst.update(dtrain, iteration=i, fobj=obj)\\n/root/miniconda3/lib/python3.12/site-packages/xgboost/training.py:200: UserWarning: [07:28:35] WARNING: /__w/xgboost/xgboost/src/learner.cc:782: \\nParameters: { \\\"use_label_encoder\\\" } are not used.\\n\\n  bst.update(dtrain, iteration=i, fobj=obj)\\n/root/miniconda3/lib/python3.12/site-packages/xgboost/training.py:200: UserWarning: [07:28:35] WARNING: /__w/xgboost/xgboost/src/learner.cc:782: \\nParameters: { \\\"use_label_encoder\\\" } are not used.\\n\\n  bst.update(dtrain, iteration=i, fobj=obj)\\n\\nStderr:\\n\\n\\n\\n\", \"metadata\": {\"elapsed_seconds\": 30.3}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_corpus-prevalence_20260517T231957",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-17T23:31:25.646645+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-5090",
  "command": "source /root/miniconda3/bin/activate && cd /root/gen-depth-fingerprint && nohup python corpus_prevalence_demo.py > logs/corpus_prevalence_demo.log 2>&1 && tail -40 logs/corpus_prevalence_demo.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_corpus-prevalence_20260517T231957",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-5090",
    "command": "source /root/miniconda3/bin/activate && cd /root/gen-depth-fingerprint && nohup python corpus_prevalence_demo.py > logs/corpus_prevalence_demo.log 2>&1 && tail -40 logs/corpus_prevalence_demo.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-17T23:31:25.646770+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Command did not complete within 30 seconds!\\n\\nCommand: 'source /root/miniconda3/bin/activate && cd /root/gen-depth-fingerprint && nohup python corpus_prevalence_demo.py > logs/corpus_prevalence_demo.log 2>&1 && tail -40 logs/corpus_prevalence_demo.log'\\n\\nStdout:\\n\\n\\n\\nStderr:\\n\\n\\n\\n\", \"metadata\": {\"elapsed_seconds\": 30.8}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_corpus-prevalence_20260517T231957",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-17T23:31:25.646882+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-5090",
  "command": "source /root/miniconda3/bin/activate && cd /root/gen-depth-fingerprint && nohup python corpus_prevalence_demo.py > logs/corpus_prevalence_demo.log 2>&1 &\necho \"PID=$!\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_corpus-prevalence_20260517T231957",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-5090",
    "command": "source /root/miniconda3/bin/activate && cd /root/gen-depth-fingerprint && nohup python corpus_prevalence_demo.py > logs/corpus_prevalence_demo.log 2>&1 &\necho \"PID=$!\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-17T23:31:25.646998+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Command did not complete within 30 seconds!\\n\\nCommand: 'source /root/miniconda3/bin/activate && cd /root/gen-depth-fingerprint && nohup python corpus_prevalence_demo.py > logs/corpus_prevalence_demo.log 2>&1 &\\\\necho \\\"PID=$!\\\"'\\n\\nStdout:\\n\\nPID=34239\\n\\nStderr:\\n\\n\\n\\n\", \"metadata\": {\"elapsed_seconds\": 31.0}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_corpus-prevalence_20260517T231957",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-17T23:31:25.647135+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-5090",
  "command": "sleep 90 && tail -50 /root/gen-depth-fingerprint/logs/corpus_prevalence_demo.log",
  "account": "root",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_corpus-prevalence_20260517T231957",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-5090",
    "command": "sleep 90 && tail -50 /root/gen-depth-fingerprint/logs/corpus_prevalence_demo.log",
    "account": "root",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-17T23:31:25.647274+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Command did not complete within 30 seconds!\\n\\nCommand: 'sleep 90 && tail -50 /root/gen-depth-fingerprint/logs/corpus_prevalence_demo.log'\\n\\nStdout:\\n\\n\\n\\nStderr:\\n\\n\\n\\n\", \"metadata\": {\"elapsed_seconds\": 30.61}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_corpus-prevalence_20260517T231957",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-17T23:31:25.647385+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-5090",
  "command": "tail -50 /root/gen-depth-fingerprint/logs/corpus_prevalence_demo.log",
  "account": "root",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_corpus-prevalence_20260517T231957",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-5090",
    "command": "tail -50 /root/gen-depth-fingerprint/logs/corpus_prevalence_demo.log",
    "account": "root",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-17T23:31:25.647517+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"  75%  CC=8.8  ACC=22.8  PCC=6.2  EMQ=15.5pp\\n  100%  CC=18.0  ACC=0.0  PCC=19.2  EMQ=0.0pp\\n\\n--- Held-out: pythia-2.8b ---\\n  0%  CC=12.9  ACC=0.1  PCC=29.2  EMQ=0.7pp\\n  25%  CC=2.7  ACC=0.2  PCC=14.8  EMQ=1.0pp\\n  50%  CC=7.6  ACC=3.5  PCC=0.4  EMQ=1.0pp\\n  75%  CC=17.8  ACC=6.7  PCC=13.9  EMQ=0.1pp\\n  100%  CC=28.0  ACC=0.0  PCC=28.3  EMQ=2.7pp\\n\\n--- Held-out: qwen3-0.6b ---\\n  0%  CC=23.8  ACC=17.1  PCC=36.2  EMQ=8.7pp\\n  25%  CC=12.9  ACC=18.7  PCC=21.9  EMQ=17.1pp\\n  50%  CC=1.9  ACC=20.1  PCC=7.5  EMQ=17.3pp\\n  75%  CC=9.1  ACC=21.4  PCC=6.9  EMQ=13.4pp\\n  100%  CC=20.1  ACC=0.0  PCC=21.3  EMQ=0.0pp\\n\\n--- Held-out: qwen3-1.7b ---\\n  0%  CC=17.9  ACC=5.2  PCC=32.3  EMQ=4.1pp\\n  25%  CC=7.4  ACC=7.9  PCC=18.4  EMQ=9.5pp\\n  50%  CC=3.3  ACC=10.3  PCC=4.4  EMQ=10.0pp\\n  75%  CC=13.8  ACC=12.9  PCC=9.5  EMQ=8.4pp\\n  100%  CC=24.3  ACC=0.0  PCC=23.4  EMQ=0.0pp\\n\\n--- Held-out: qwen3-8b ---\\n  0%  CC=9.7  ACC=0.0  PCC=27.6  EMQ=0.0pp\\n  25%  CC=3.8  ACC=12.4  PCC=10.9  EMQ=7.4pp\\n  50%  CC=17.1  ACC=15.9  PCC=5.6  EMQ=13.1pp\\n  75%  CC=30.5  ACC=19.5  PCC=22.2  EMQ=18.4pp\\n  100%  CC=43.9  ACC=23.1  PCC=38.8  EMQ=22.8pp\\n\\n=====================================================================================\\nAGGREGATED RESULTS (averaged across 8 held-out generators)\\n=====================================================================================\\n  True    CC pred   CC err   ACC pred  ACC err   PCC pred  PCC err   EMQ pred  EMQ err\\n    0%      14.3%   14.33pp       4.0%    3.97pp      30.5%   30.47pp       2.3%    2.34pp\\n   25%      27.5%    6.48pp      24.4%   10.65pp      40.2%   15.19pp      27.1%    8.87pp\\n   50%      40.7%    9.89pp      49.3%   13.66pp      49.9%    5.03pp      49.7%   11.70pp\\n   75%      53.8%   21.15pp      74.0%   16.95pp      59.6%   15.37pp      71.2%   13.20pp\\n  100%      67.1%   32.93pp      89.3%   10.74pp      69.4%   30.62pp 
…[truncated 496 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_corpus-prevalence_20260517T231957",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-17T23:31:25.647708+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /root/gen-depth-fingerprint/results/corpus_prevalence_demo.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_corpus-prevalence_20260517T231957",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat /root/gen-depth-fingerprint/results/corpus_prevalence_demo.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-17T23:31:25.648023+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"corpus_size\\\": 800,\\n  \\\"n_bootstrap\\\": 200,\\n  \\\"n_generators\\\": 8,\\n  \\\"per_generator\\\": {\\n    \\\"llama-3.2-3b\\\": {\\n      \\\"tpr\\\": 0.6763,\\n      \\\"fpr\\\": 0.1496,\\n      \\\"corpora\\\": [\\n        {\\n          \\\"cc_prop\\\": 0.0838,\\n          \\\"cc_err\\\": 8.38,\\n          \\\"cc_ci_lo\\\": 0.065,\\n          \\\"cc_ci_hi\\\": 0.105,\\n          \\\"acc_prop\\\": 0.0,\\n          \\\"acc_err\\\": 0.0,\\n          \\\"acc_ci_lo\\\": 0.0,\\n          \\\"acc_ci_hi\\\": 0.0,\\n          \\\"pcc_prop\\\": 0.2769,\\n          \\\"pcc_err\\\": 27.69,\\n          \\\"pcc_ci_lo\\\": 0.266,\\n          \\\"pcc_ci_hi\\\": 0.2882,\\n          \\\"emq_prop\\\": 0.0,\\n          \\\"emq_err\\\": 0.0,\\n          \\\"emq_ci_lo\\\": 0.0,\\n          \\\"emq_ci_hi\\\": 0.0,\\n          \\\"true_prop\\\": 0.0\\n        },\\n        {\\n          \\\"cc_prop\\\": 0.2178,\\n          \\\"cc_err\\\": 3.22,\\n          \\\"cc_ci_lo\\\": 0.195,\\n          \\\"cc_ci_hi\\\": 0.2425,\\n          \\\"acc_prop\\\": 0.1295,\\n          \\\"acc_err\\\": 12.05,\\n          \\\"acc_ci_lo\\\": 0.0862,\\n          \\\"acc_ci_hi\\\": 0.1765,\\n          \\\"pcc_prop\\\": 0.3723,\\n          \\\"pcc_err\\\": 12.23,\\n          \\\"pcc_ci_lo\\\": 0.3566,\\n          \\\"pcc_ci_hi\\\": 0.3884,\\n          \\\"emq_prop\\\": 0.1995,\\n          \\\"emq_err\\\": 5.05,\\n          \\\"emq_ci_lo\\\": 0.1622,\\n          \\\"emq_ci_hi\\\": 0.2376,\\n          \\\"true_prop\\\": 0.25\\n        },\\n        {\\n          \\\"cc_prop\\\": 0.352,\\n          \\\"cc_err\\\": 14.8,\\n          \\\"cc_ci_lo\\\": 0.325,\\n          \\\"cc_ci_hi\\\": 0.38,\\n          \\\"acc_prop\\\": 0.3843,\\n          \\\"acc_err\\\": 11.57,\\n          \\\"acc_ci_lo\\\": 0.333,\\n          \\\"acc_ci_hi\\\": 0.4375,\\n          \\\"pcc_prop\\\": 0.4681,\\n          \\\"pcc_err\\\": 3.19,\\n          \\\"pcc_ci_lo\\\":
…[truncated 8424 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_corpus-prevalence_20260517T231957",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-17T23:31:25.648198+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/analysis/ 2>/dev/null || mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/analysis/",
  "description": "Ensure analysis directory exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_corpus-prevalence_20260517T231957",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/analysis/ 2>/dev/null || mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/analysis/",
    "description": "Ensure analysis directory exists"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-17T23:31:25.648319+00:00_

bootstrap_seed_variance.md
feature_importance_stability.md
gen1_subclass_analysis.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_corpus-prevalence_20260517T231957",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-17T23:31:25.648438+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/analysis/corpus_prevalence_demo.md",
  "content": "# Corpus Prevalence Estimation Demo\n\n## Setup\n- 5 synthetic corpora: 0%, 25%, 50%, 75%, 100% depth-2+ proportion\n- Corpus size: 800 documents each\n- 8 held-out generators (LOGO), 200 bootstrap resamples per corpus\n- 4 quantification methods: CC, ACC, PCC, EMQ\n\n## Results\n\n| True depth-2+ % | EMQ Predicted % | |Error| | 95% CI |\n| --- | --- | --- | --- |\n| 0% | 2.3% | 2.34pp | [1.0%, 4.1%] |\n| 25% | 27.1% | 8.87pp | [23.7%, 30.7%] |\n| 50% | 49.7% | 11.70pp | [45.8%, 53.7%] |\n| 75% | 71.2% | 13.20pp | [67.0%, 75.3%] |\n| 100% | 88.8% | 11.16pp | [85.9%, 91.6%] |\n\n## Method Comparison (MAE across 5 corpora, 8 generators)\n\n| Method | MAE |\n| --- | --- |\n| CC (Classify & Count) | 16.96pp |\n| ACC (Adjusted CC) | 11.19pp |\n| PCC (Probabilistic CC) | 19.34pp |\n| EMQ (EM Quantification) | 9.45pp |\n\n## Per-Generator EMQ Performance (MAE across 5 corpora)\n\n| Generator | EMQ MAE | Notes |\n| --- | --- | --- |\n| pythia-2.8b | ~1.1pp | Excellent calibration |\n| olmo-2-1b | ~3.5pp | Good |\n| llama-3.2-3b | ~6.6pp | Moderate |\n| qwen3-1.7b | ~6.4pp | Moderate |\n| pythia-1b | ~7.6pp | Moderate |\n| mistral-7b-v0.3 | ~12.4pp | Poor (high domain shift) |\n| qwen3-0.6b | ~11.3pp | Poor |\n| qwen3-8b | ~12.3pp | Poor |\n\n## Conclusion\n\nMAE = 9.45pp (best, EMQ) >= 5pp threshold.\n\n**Corpus-level depth auditing is NOT viable in the strict LOGO (cross-generator) setting** with the current 7-feature XGBoost classifier.\n\nKey observations:\n1. For in-distribution generators (pythia-2.8b, olmo-2-1b), MAE < 3.5pp, demonstrating the method is sound when domain shift is small.\n2. The bottleneck is generator-specific domain shift in LOGO, not the quantification method itself.\n3. EMQ (Saerens et al. 2002) provides the best correction by adapting posterior probabilities to the test distribution without explicit TPR/FPR estimation.\n4. Naive classify-and-count systematically underestimates high proportions and overestimates low proportions (regression to the mean).\n\n## Outputs\n- Plot: `/root/gen-depth-fingerprint/results/corpus_prevalence_calibration.pdf`\n- Data: `/root/gen-depth-fingerprint/results/corpus_prevalence_demo.json`\n- Script: `/root/gen-depth-fingerprint/corpus_prevalence_demo.py`\n- Log: `/root/gen-depth-fingerprint/logs/corpus_prevalence_demo.log`\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_corpus-prevalence_20260517T231957",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/analysis/corpus_prevalence_demo.md",
    "content": "# Corpus Prevalence Estimation Demo\n\n## Setup\n- 5 synthetic corpora: 0%, 25%, 50%, 75%, 100% depth-2+ proportion\n- Corpus size: 800 documents each\n- 8 held-out generators (LOGO), 200 bootstrap resamples per corpus\n- 4 quantification methods: CC, ACC, PCC, EMQ\n\n## Results\n\n| True depth-2+ % | EMQ Predicted % | |Error| | 95% CI |\n| --- | --- | --- | --- |\n| 0% | 2.3% | 2.34pp | [1.0%, 4.1%] |\n| 25% | 27.1% | 8.87pp | [23.7%, 30.7%] |\n| 50% | 49.7% | 11.70pp | [45.8%, 53.7%] |\n| 75% | 71.2% | 13.20pp | [67.0%, 75.3%] |\n| 100% | 88.8% | 11.16pp | [85.9%, 91.6%] |\n\n## Method Comparison (MAE across 5 corpora, 8 generators)\n\n| Method | MAE |\n| --- | --- |\n| CC (Classify & Count) | 16.96pp |\n| ACC (Adjusted CC) | 11.19pp |\n| PCC (Probabilistic CC) | 19.34pp |\n| EMQ (EM Quantification) | 9.45pp |\n\n## Per-Generator EMQ Performance (MAE across 5 corpora)\n\n| Generator | EMQ MAE | Notes |\n| --- | --- | --- |\n| pythia-2.8b | ~1.1pp | Excellent calibration |\n| olmo-2-1b | ~3.5pp | Good |\n| llama-3.2-3b | ~6.6pp | Moderate |\n| qwen3-1.7b | ~6.4pp | Moderate |\n| pythia-1b | ~7.6pp | Moderate |\n| mistral-7b-v0.3 | ~12.4pp | Poor (high domain shift) |\n| qwen3-0.6b | ~11.3pp | Poor |\n| qwen3-8b | ~12.3pp | Poor |\n\n## Conclusion\n\nMAE = 9.45pp (best, EMQ) >= 5pp threshold.\n\n**Corpus-level depth auditing is NOT viable in the strict LOGO (cross-generator) setting** with the current 7-feature XGBoost classifier.\n\nKey observations:\n1. For in-distribution generators (pythia-2.8b, olmo-2-1b), MAE < 3.5pp, demonstrating the method is sound when domain shift is small.\n2. The bottleneck is generator-specific domain shift in LOGO, not the quantification method itself.\n3. EMQ (Saerens et al. 2002) provides the best correction by adapting posterior probabilities to the test distribution without explicit TPR/FPR estimation.\n4. Naive classify-and-count systematically underestimates high proportions and overestimates low proportions (regression to the mean).\n\n## Outputs\n- Plot: `/root/gen-depth-fingerprint/results/corpus_prevalence_calibration.pdf`\n- Data: `/root/gen-depth-fingerprint/results/corpus_prevalence_demo.json`\n- Script: `/root/gen-depth-fingerprint/corpus_prevalence_demo.py`\n- Log: `/root/gen-depth-fingerprint/logs/corpus_prevalence_demo.log`\n"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-17T23:31:25.648595+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/analysis/corpus_prevalence_demo.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_corpus-prevalence_20260517T231957",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-17T23:31:25.648729+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "register artifact",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_corpus-prevalence_20260517T231957",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "register artifact",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-17T23:31:25.648841+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_corpus-prevalence_20260517T231957",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 55 · 2026-05-17T23:31:25.648988+00:00_

Task complete. Summary:

**Corpus Prevalence Estimation Results:**

| True depth-2+ % | Predicted (EMQ) | |Error| | 95% CI |
| --- | --- | --- | --- |
| 0% | 2.3% | 2.34pp | [1.0%, 4.1%] |
| 25% | 27.1% | 8.87pp | [23.7%, 30.7%] |
| 50% | 49.7% | 11.70pp | [45.8%, 53.7%] |
| 75% | 71.2% | 13.20pp | [67.0%, 75.3%] |
| 100% | 88.8% | 11.16pp | [85.9%, 91.6%] |

**MAE = 9.45pp** (best method: EMQ)

**Conclusion: not viable** for corpus-level auditing in the strict LOGO setting (MAE >= 5pp). The bottleneck is cross-generator domain shift. For in-distribution generators (pythia-2.8b, olmo-2-1b), MAE drops to ~1-3.5pp, confirming the method works when domain shift is small.

Outputs:
- `results/corpus_prevalence_calibration.pdf` (3-panel plot: CC vs ACC vs EMQ)
- `results/corpus_prevalence_demo.json`
- Local artifact: `artifacts/_project/analysis/corpus_prevalence_demo.md`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_corpus-prevalence_20260517T231957"
}
```

</details>

---
