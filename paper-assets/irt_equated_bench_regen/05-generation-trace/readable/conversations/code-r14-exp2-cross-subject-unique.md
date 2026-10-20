# code r14 exp2 cross subject unique

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 39
- **Recorded user turns:** 0
- **Tool calls:** 19
- **Original source:** `logs/chats/worker_code_r14_exp2_cross_subject_unique_20260522T115630.jsonl`
- **Structured JSON:** [`c9396e159e564e7a3164.json`](../../sessions/c9/c9396e159e564e7a3164.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

39 recorded events

### Tool call

_source line 1 · 2026-05-22T12:01:24.370558+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001/dif_results_temporal.csv",
  "limit": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_r14_exp2_cross_subject_unique_20260522T115630",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001/dif_results_temporal.csv",
    "limit": "5"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-22T12:01:24.370958+00:00_

1	item_id,subject,alpha_mh,delta_mh,se,p_value,ets_class,li_label,li_contamination_type
2	abstract_algebra.1,abstract_algebra,0.8673811041189408,0.3343505559632721,0.2921867891177819,0.27995385252579175,A,False,clean
3	abstract_algebra.10,abstract_algebra,0.5141246508049961,1.5634303993406418,0.36471274316626207,1.8840975857581377e-05,C,False,clean
4	abstract_algebra.100,abstract_algebra,0.45562394251510224,1.8473056183645777,0.4442953571627415,3.3721937472974695e-05,C,,no_annotation
5	abstract_algebra.11,abstract_algebra,0.7175060366563377,0.780138707124792,0.2484055209632857,0.0016556553694112575,A,False,clean

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_r14_exp2_cross_subject_unique_20260522T115630",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-22T12:01:24.371132+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_014/within_subject_dif_detail.csv",
  "limit": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_r14_exp2_cross_subject_unique_20260522T115630",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_014/within_subject_dif_detail.csv",
    "limit": "5"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-22T12:01:24.371275+00:00_

1	subject,item_id,matching_type,delta_mh,p_value,ets_class,n_strata_used
2	business_ethics,business_ethics.1,within,-1.351784714393325,5.9052114434021696e-05,B,5
3	business_ethics,business_ethics.10,within,-0.10054688900418687,0.7688851828549919,A,5
4	business_ethics,business_ethics.100,within,-0.7437526977590142,0.005754220728987236,A,5
5	business_ethics,business_ethics.12,within,0.5563029528034974,0.11223288641506579,A,5

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_r14_exp2_cross_subject_unique_20260522T115630",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-22T12:01:24.371402+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_032_dif_cleaned_mmlu/per_subject_dif_concentration.csv",
  "limit": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_r14_exp2_cross_subject_unique_20260522T115630",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_032_dif_cleaned_mmlu/per_subject_dif_concentration.csv",
    "limit": "5"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-22T12:01:24.371531+00:00_

1	subject,n_items,n_c_items,mean_difficulty,mean_discrimination,pct_c
2	business_ethics,93,45,0.430471169238947,0.06943346351583614,48.38709677419355
3	human_aging,203,85,0.4842011049056262,0.05658960441128911,41.87192118226601
4	formal_logic,109,44,0.3196726498626226,0.049855688224312675,40.36697247706422
5	high_school_microeconomics,220,85,0.4675836976780644,0.10883443415254619,38.63636363636363

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_r14_exp2_cross_subject_unique_20260522T115630",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-22T12:01:24.371654+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r14_mf1_domain_profile/ 2>/dev/null; echo \"---\"; ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/response_matrix*.npz 2>/dev/null",
  "description": "Check output dir and response matrix files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_r14_exp2_cross_subject_unique_20260522T115630",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r14_mf1_domain_profile/ 2>/dev/null; echo \"---\"; ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/response_matrix*.npz 2>/dev/null",
    "description": "Check output dir and response matrix files"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-22T12:01:24.371842+00:00_

---
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/response_matrix.npz
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/response_matrix_index.npz

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_r14_exp2_cross_subject_unique_20260522T115630",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-22T12:01:24.371978+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "head -3 /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_032_dif_cleaned_mmlu/cleaned_mmlu_analysis.csv",
  "description": "Check model metadata columns"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_r14_exp2_cross_subject_unique_20260522T115630",
  "tool": "Bash",
  "tool_args": {
    "command": "head -3 /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_032_dif_cleaned_mmlu/cleaned_mmlu_analysis.csv",
    "description": "Check model metadata columns"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-22T12:01:24.372136+00:00_

model_name,score_full,score_cleaned,rank_full,rank_cleaned,rank_change,abs_rank_change,family,cohort_temporal
0-hero/Matter-0.1-7B,0.5602014710585226,0.579976717112922,3837,3892,55,55,unknown,other
0-hero/Matter-0.1-7B-DPO-preview,0.6613367444835305,0.6863795110593713,2611,2615,4,4,,other

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_r14_exp2_cross_subject_unique_20260522T115630",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-22T12:01:24.372296+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport numpy as np\nidx = np.load('artifacts/response_matrix_index.npz', allow_pickle=True)\nprint('Keys:', list(idx.keys()))\nfor k in idx.keys():\n    arr = idx[k]\n    print(f'{k}: shape={arr.shape}, dtype={arr.dtype}, first 3={arr[:3]}')\n\"",
  "description": "Inspect response matrix index structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_r14_exp2_cross_subject_unique_20260522T115630",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport numpy as np\nidx = np.load('artifacts/response_matrix_index.npz', allow_pickle=True)\nprint('Keys:', list(idx.keys()))\nfor k in idx.keys():\n    arr = idx[k]\n    print(f'{k}: shape={arr.shape}, dtype={arr.dtype}, first 3={arr[:3]}')\n\"",
    "description": "Inspect response matrix index structure"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-22T12:01:24.372424+00:00_

Keys: ['model_names', 'item_ids']
model_names: shape=(5227,), dtype=object, first 3=['0-hero/Matter-0.1-7B' '0-hero/Matter-0.1-7B-DPO-preview'
 '0-hero/Matter-0.1-7B-boost']
item_ids: shape=(12508,), dtype=object, first 3=['abstract_algebra.1' 'abstract_algebra.10' 'abstract_algebra.100']

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_r14_exp2_cross_subject_unique_20260522T115630",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-22T12:01:24.372544+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport numpy as np\nmat = np.load('artifacts/response_matrix.npz')\nprint('Keys:', list(mat.keys()))\nfor k in mat.keys():\n    print(f'{k}: shape={mat[k].shape}, dtype={mat[k].dtype}')\n\"",
  "description": "Inspect response matrix structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_r14_exp2_cross_subject_unique_20260522T115630",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport numpy as np\nmat = np.load('artifacts/response_matrix.npz')\nprint('Keys:', list(mat.keys()))\nfor k in mat.keys():\n    print(f'{k}: shape={mat[k].shape}, dtype={mat[k].dtype}')\n\"",
    "description": "Inspect response matrix structure"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-22T12:01:24.372663+00:00_

Keys: ['indices', 'indptr', 'format', 'shape', 'data']
indices: shape=(38654082,), dtype=int32
indptr: shape=(5228,), dtype=int32
format: shape=(), dtype=|S3
shape: shape=(2,), dtype=int64
data: shape=(38654082,), dtype=int8

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_r14_exp2_cross_subject_unique_20260522T115630",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-22T12:01:24.372854+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport pandas as pd\nmeta = pd.read_csv('artifacts/plan_032_dif_cleaned_mmlu/cleaned_mmlu_analysis.csv')\nprint(meta['cohort_temporal'].value_counts())\nprint()\nprint(meta.columns.tolist())\n\"",
  "description": "Check cohort distribution in model metadata"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_r14_exp2_cross_subject_unique_20260522T115630",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport pandas as pd\nmeta = pd.read_csv('artifacts/plan_032_dif_cleaned_mmlu/cleaned_mmlu_analysis.csv')\nprint(meta['cohort_temporal'].value_counts())\nprint()\nprint(meta.columns.tolist())\n\"",
    "description": "Check cohort distribution in model metadata"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-22T12:01:24.372993+00:00_

cohort_temporal
other    3340
2023     1080
2024      807
Name: count, dtype: int64

['model_name', 'score_full', 'score_cleaned', 'rank_full', 'rank_cleaned', 'rank_change', 'abs_rank_change', 'family', 'cohort_temporal']

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_r14_exp2_cross_subject_unique_20260522T115630",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-22T12:01:24.373124+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r14_mf1_domain_profile",
  "description": "Create output directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_r14_exp2_cross_subject_unique_20260522T115630",
  "tool": "Bash",
  "tool_args": {
    "command": "mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r14_mf1_domain_profile",
    "description": "Create output directory"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-22T12:01:24.373241+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_r14_exp2_cross_subject_unique_20260522T115630",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-22T12:01:24.373424+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r14_mf1_domain_profile/cross_subject_unique_analysis.py",
  "content": "\"\"\"R14 Experiment 2: Cross-Subject-Unique C Item Concentration Analysis.\"\"\"\n\nimport numpy as np\nimport pandas as pd\nfrom scipy import sparse, stats\nfrom sklearn.metrics import cohen_kappa_score\nfrom pathlib import Path\n\nROOT = Path(\"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen\")\nOUT = ROOT / \"artifacts/r14_mf1_domain_profile\"\n\n# ── Load data ──\ncross_dif = pd.read_csv(ROOT / \"artifacts/plan_001/dif_results_temporal.csv\")\nwithin_dif = pd.read_csv(ROOT / \"artifacts/plan_014/within_subject_dif_detail.csv\")\nmeta = pd.read_csv(ROOT / \"artifacts/plan_032_dif_cleaned_mmlu/cleaned_mmlu_analysis.csv\")\n\n# Response matrix for accuracy delta computation\nrm_data = np.load(ROOT / \"artifacts/response_matrix.npz\")\nrm_idx = np.load(ROOT / \"artifacts/response_matrix_index.npz\", allow_pickle=True)\nresponse_matrix = sparse.csr_matrix(\n    (rm_data[\"data\"], rm_data[\"indices\"], rm_data[\"indptr\"]),\n    shape=tuple(rm_data[\"shape\"])\n)\nmodel_names = rm_idx[\"model_names\"]\nitem_ids = rm_idx[\"item_ids\"]\n\n# Build item-to-subject mapping from item_ids\nitem_subjects = pd.Series([iid.rsplit(\".\", 1)[0] for iid in item_ids], index=item_ids, name=\"subject\")\n\n# 5 subjects with within-subject DIF\nwithin_subjects = within_dif[\"subject\"].unique().tolist()\nprint(f\"Within-subject DIF subjects ({len(within_subjects)}): {within_subjects}\")\n\n# ── Part A: Cohen's κ for 5 subjects ──\nprint(\"\\n\" + \"=\"*60)\nprint(\"PART A: Cohen's κ — Cross vs Within DIF Classification\")\nprint(\"=\"*60)\n\nkappa_rows = []\nunique_c_items_all = {}\n\nfor subj in within_subjects:\n    cross_sub = cross_dif[cross_dif[\"subject\"] == subj][[\"item_id\", \"ets_class\"]].copy()\n    cross_sub.columns = [\"item_id\", \"cross_class\"]\n\n    within_sub = within_dif[within_dif[\"subject\"] == subj][[\"item_id\", \"ets_class\"]].copy()\n    within_sub.columns = [\"item_id\", \"within_class\"]\n\n    merged = cross_sub.merge(within_sub, on=\"item_id\", how=\"inner\")\n\n    # Binary: C vs not-C\n    merged[\"cross_C\"] = (merged[\"cross_class\"] == \"C\").astype(int)\n    merged[\"within_C\"] = (merged[\"within_class\"] == \"C\").astype(int)\n\n    # Cohen's kappa\n    kappa = cohen_kappa_score(merged[\"cross_C\"], merged[\"within_C\"])\n\n    # 2x2 contingency table\n    ct = pd.crosstab(merged[\"cross_C\"], merged[\"within_C\"],\n                     rownames=[\"cross_C\"], colnames=[\"within_C\"])\n\n    # Cross-unique C: cross=C AND within≠C\n    cross_unique_c = merged[(merged[\"cross_C\"] == 1) & (merged[\"within_C\"] == 0)]\n    n_cross_unique_c = len(cross_unique_c)\n    unique_c_items_all[subj] = cross_unique_c[\"item_id\"].tolist()\n\n    # Within-unique C: within=C AND cross≠C\n    within_unique_c = merged[(merged[\"within_C\"] == 1) & (merged[\"cross_C\"] == 0)]\n    n_within_unique_c = len(within_unique_c)\n\n    n_total = len(merged)\n    n_cross_c = merged[\"cross_C\"].sum()\n    n_within_c = merged[\"within_C\"].sum()\n\n    kappa_rows.append({\n        \"subject\": subj,\n        \"n_items\": n_total,\n        \"cross_C\": n_cross_c,\n        \"cross_C_pct\": 100 * n_cross_c / n_total,\n        \"within_C\": n_within_c,\n        \"within_C_pct\": 100 * n_within_c / n_total,\n        \"kappa\": kappa,\n        \"cross_unique_C\": n_cross_unique_c,\n        \"within_unique_C\": n_within_unique_c,\n        \"both_C\": merged[(merged[\"cross_C\"] == 1) & (merged[\"within_C\"] == 1)].shape[0],\n        \"neither_C\": merged[(merged[\"cross_C\"] == 0) & (merged[\"within_C\"] == 0)].shape[0],\n    })\n\n    print(f\"\\n{subj} (n={n_total}):\")\n    print(f\"  Cross C: {n_cross_c} ({100*n_cross_c/n_total:.1f}%), Within C: {n_within_c} ({100*n_within_c/n_total:.1f}%)\")\n    print(f\"  κ = {kappa:.3f}\")\n    print(f\"  Cross-unique C: {n_cross_unique_c}, Within-unique C: {n_within_unique_c}\")\n    print(f\"  Contingency table:\\n{ct}\")\n\nkappa_df = pd.DataFrame(kappa_rows)\nkappa_df.to_csv(OUT / \"kappa_results.csv\", index=False)\n\n# Summary statistics\nprint(f\"\\nOverall κ: mean={kappa_df['kappa'].mean():.3f}, range=[{kappa_df['kappa'].min():.3f}, {kappa_df['kappa'].max():.3f}]\")\nprint(f\"Cross C% mean: {kappa_df['cross_C_pct'].mean():.1f}%, Within C% mean: {kappa_df['within_C_pct'].mean():.1f}%\")\n\n# ── Part B: Domain accuracy delta vs cross-unique C concentration ──\nprint(\"\\n\" + \"=\"*60)\nprint(\"PART B: Domain Accuracy Delta vs Cross-Unique C Concentration\")\nprint(\"=\"*60)\n\n# Get 2023 and 2024 model indices\nmodel_cohort = meta.set_index(\"model_name\")[\"cohort_temporal\"]\nmodel_name_to_idx = {name: i for i, name in enumerate(model_names)}\n\nmodels_2023 = [m for m in model_cohort[model_cohort == \"2023\"].index if m in model_name_to_idx]\nmodels_2024 = [m for m in model_cohort[model_cohort == \"2024\"].index if m in model_name_to_idx]\nidx_2023 = [model_name_to_idx[m] for m in models_2023]\nidx_2024 = [model_name_to_idx[m] for m in models_2024]\nprint(f\"Models: 2023={len(idx_2023)}, 2024={len(idx_2024)}\")\n\n# Build item index mapping\nitem_id_to_col = {iid: i for i, iid in enumerate(item_ids)}\n\n# For each of the 5 subjects, compute domain accuracy delta\ndelta_rows = []\nfor subj in within_subjects:\n    subj_items = [iid for iid in item_ids if iid.rsplit(\".\", 1)[0] == subj]\n    col_indices = [item_id_to_col[iid] for iid in subj_items]\n\n    # Extract submatrix for this subject\n    sub_2023 = response_matrix[idx_2023][:, col_indices]\n    sub_2024 = response_matrix[idx_2024][:, col_indices]\n\n    # Mean accuracy per cohort (handle sparse: nonzero entries are correct answers=1)\n    # But we need to distinguish 0 (wrong) from missing. The matrix is sparse with 1=correct.\n    # Actually in a sparse matrix, 0s are implicit. Let's check density.\n    # For MMLU with 4-choice, all models answer all items, so density should be high.\n    # The matrix stores 1 for correct, 0 for incorrect (but 0 is not stored in sparse).\n    # So mean of dense matrix = accuracy.\n\n    acc_2023 = sub_2023.toarray().mean()\n    acc_2024 = sub_2024.toarray().mean()\n    acc_delta = acc_2024 - acc_2023\n\n    n_unique_c = len(unique_c_items_all[subj])\n    n_items = len(subj_items)\n\n    delta_rows.append({\n        \"subject\": subj,\n        \"n_items\": n_items,\n        \"acc_2023\": acc_2023,\n        \"acc_2024\": acc_2024,\n        \"acc_delta\": acc_delta,\n        \"cross_unique_C\": n_unique_c,\n        \"cross_unique_C_pct\": 100 * n_unique_c / n_items if n_items > 0 else 0,\n    })\n\n    print(f\"{subj}: acc_2023={acc_2023:.4f}, acc_2024={acc_2024:.4f}, Δ={acc_delta:+.4f}, unique_C={n_unique_c} ({100*n_unique_c/n_items:.1f}%)\")\n\ndelta_df = pd.DataFrame(delta_rows)\ndelta_df.to_csv(OUT / \"accuracy_delta_vs_unique_c.csv\", index=False)\n\n# Spearman correlation (5 data points — descriptive only)\nif len(delta_df) >= 3:\n    rho, p_val = stats.spearmanr(delta_df[\"acc_delta\"], delta_df[\"cross_unique_C_pct\"])\n    print(f\"\\nSpearman ρ(acc_delta, unique_C%): ρ={rho:.3f}, p={p_val:.3f}\")\n\n    # Also Pearson for reference\n    r, p_r = stats.pearsonr(delta_df[\"acc_delta\"], delta_df[\"cross_unique_C_pct\"])\n    print(f\"Pearson r(acc_delta, unique_C%): r={r:.3f}, p={p_r:.3f}\")\n\n# ── Part C: Direction argument ──\nprint(\"\\n\" + \"=\"*60)\nprint(\"PART C: Direction Argument\")\nprint(\"=\"*60)\n\ncross_c_pcts = kappa_df[\"cross_C_pct\"]\nwithin_c_pcts = kappa_df[\"within_C_pct\"]\n\nprint(f\"Mean cross-subject C%: {cross_c_pcts.mean():.1f}%\")\nprint(f\"Mean within-subject C%: {within_c_pcts.mean():.1f}%\")\nprint(f\"Within > Cross in {(within_c_pcts > cross_c_pcts).sum()}/{len(kappa_df)} subjects\")\n\nfor _, row in kappa_df.iterrows():\n    direction = \"within > cross\" if row[\"within_C_pct\"] > row[\"cross_C_pct\"] else \"cross > within\" if row[\"cross_C_pct\"] > row[\"within_C_pct\"] else \"equal\"\n    print(f\"  {row['subject']}: cross={row['cross_C_pct']:.1f}%, within={row['within_C_pct']:.1f}% ({direction})\")\n\n# ── Generate markdown report ──\nprint(\"\\n\" + \"=\"*60)\nprint(\"Generating report...\")\nprint(\"=\"*60)\n\nreport = []\nreport.append(\"# R14 Experiment 2: Cross-Subject-Unique C Item Concentration Analysis\\n\")\nreport.append(\"## Purpose\\n\")\nreport.append(\"Test whether items classified as C (large DIF) by cross-subject matching but NOT by within-subject matching\")\nreport.append(\"concentrate in subjects with large domain profile shifts. If they do not concentrate,\")\nreport.append(\"multidimensionality confound is unlikely to be the primary driver of cross-subject DIF flags.\\n\")\n\n# Part A\nreport.append(\"## Part A: Cohen's κ — Cross vs Within DIF Classification Agreement\\n\")\nreport.append(f\"Five subjects have both cross-subject and within-subject DIF results ({', '.join(within_subjects)}).\\n\")\nreport.append(\"| Subject | n | Cross C | Cross C% | Within C | Within C% | κ | Cross-unique C | Within-unique C |\")\nreport.append(\"|---------|---|---------|----------|----------|-----------|---|----------------|-----------------|\")\nfor _, row in kappa_df.iterrows():\n    report.append(f\"| {row['subject']} | {row['n_items']} | {row['cross_C']} | {row['cross_C_pct']:.1f}% | {row['within_C']} | {row['within_C_pct']:.1f}% | {row['kappa']:.3f} | {row['cross_unique_C']} | {row['within_unique_C']} |\")\n\nreport.append(f\"\\n**Summary**: Mean κ = {kappa_df['kappa'].mean():.3f} (range: {kappa_df['kappa'].min():.3f}–{kappa_df['kappa'].max():.3f}).\")\nreport.append(f\"Cross-subject matching flags fewer C items on average ({kappa_df['cross_C_pct'].mean():.1f}%) than within-subject matching ({kappa_df['within_C_pct'].mean():.1f}%).\\n\")\n\n# Part B\nreport.append(\"## Part B: Domain Accuracy Delta vs Cross-Unique C Concentration\\n\")\nreport.append(\"Domain accuracy delta = mean accuracy of 2024-cohort models minus 2023-cohort models per subject.\")\nreport.append(f\"Computed from {len(idx_2023)} (2023) and {len(idx_2024)} (2024) models.\\n\")\nreport.append(\"| Subject | n | Acc 2023 | Acc 2024 | Δ Acc | Cross-unique C | Cross-unique C% |\")\nreport.append(\"|---------|---|----------|----------|-------|----------------|-----------------|\")\nfor _, row in delta_df.iterrows():\n    report.append(f\"| {row['subject']} | {row['n_items']} | {row['acc_2023']:.4f} | {row['acc_2024']:.4f} | {row['acc_delta']:+.4f} | {row['cross_unique_C']} | {row['cross_unique_C_pct']:.1f}% |\")\n\nif len(delta_df) >= 3:\n    rho, p_val = stats.spearmanr(delta_df[\"acc_delta\"], delta_df[\"cross_unique_C_pct\"])\n    r, p_r = stats.pearsonr(delta_df[\"acc_delta\"], delta_df[\"cross_unique_C_pct\"])\n    report.append(f\"\\n**Correlation**: Spearman ρ = {rho:.3f} (p = {p_val:.3f}), Pearson r = {r:.3f} (p = {p_r:.3f}).\")\n    report.append(\"With only 5 data points, this is descriptive rather than inferential.\\n\")\n\n# Part C\nreport.append(\"## Part C: Direction Argument\\n\")\nreport.append(\"If multidimensionality confound were the primary driver of cross-subject DIF flags,\")\nreport.append(\"we would expect cross-subject matching to produce *more* C items than within-subject matching\")\nreport.append(\"(because the confound affects only cross-subject matching, inflating DIF estimates).\\n\")\nreport.append(\"**Observed**: The opposite direction holds.\")\nreport.append(f\"Within-subject C% ({kappa_df['within_C_pct'].mean():.1f}%) > Cross-subject C% ({kappa_df['cross_C_pct'].mean():.1f}%).\")\nn_within_higher = (within_c_pcts > cross_c_pcts).sum()\nreport.append(f\"This pattern holds in {n_within_higher}/{len(kappa_df)} subjects:\\n\")\nfor _, row in kappa_df.iterrows():\n    direction = \"✓ within > cross\" if row[\"within_C_pct\"] > row[\"cross_C_pct\"] else \"✗ cross ≥ within\"\n    report.append(f\"- {row['subject']}: cross {row['cross_C_pct']:.1f}% vs within {row['within_C_pct']:.1f}% ({direction})\")\n\nreport.append(\"\\nThis directional evidence indicates that cross-subject matching is *conservative* (flags fewer items as C),\")\nreport.append(\"contradicting the hypothesis that multidimensional confound inflates cross-subject DIF classification.\\n\")\n\n# Conclusion\nreport.append(\"## Conclusion\\n\")\ntotal_cross_unique = kappa_df[\"cross_unique_C\"].sum()\ntotal_items = kappa_df[\"n_items\"].sum()\nreport.append(f\"1. **Moderate agreement**: κ ranges from {kappa_df['kappa'].min():.3f} to {kappa_df['kappa'].max():.3f} (mean {kappa_df['kappa'].mean():.3f}), indicating moderate-to-fair agreement between matching methods on C classification.\")\nreport.append(f\"2. **Cross-unique C items are few**: Only {total_cross_unique} items across 5 subjects ({100*total_cross_unique/total_items:.1f}% of items) are flagged as C by cross-subject but not within-subject matching.\")\nif len(delta_df) >= 3:\n    report.append(f\"3. **No concentration by domain shift**: Spearman ρ = {rho:.3f} between accuracy delta and cross-unique C% — no evidence that cross-unique C items concentrate in high-shift domains.\")\nreport.append(f\"4. **Conservative direction**: Cross-subject matching produces fewer C flags than within-subject matching ({kappa_df['cross_C_pct'].mean():.1f}% vs {kappa_df['within_C_pct'].mean():.1f}%), the opposite of what multidimensionality confound would predict.\")\nreport.append(\"\\nThese findings collectively indicate that multidimensional confound is not the primary driver of DIF flags in cross-subject matching.\")\n\nreport_text = \"\\n\".join(report)\n(OUT / \"cross_subject_unique_analysis.md\").write_text(report_text)\nprint(f\"\\nReport written to {OUT / 'cross_subject_unique_analysis.md'}\")\nprint(\"Done.\")\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_r14_exp2_cross_subject_unique_20260522T115630",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r14_mf1_domain_profile/cross_subject_unique_analysis.py",
    "content": "\"\"\"R14 Experiment 2: Cross-Subject-Unique C Item Concentration Analysis.\"\"\"\n\nimport numpy as np\nimport pandas as pd\nfrom scipy import sparse, stats\nfrom sklearn.metrics import cohen_kappa_score\nfrom pathlib import Path\n\nROOT = Path(\"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen\")\nOUT = ROOT / \"artifacts/r14_mf1_domain_profile\"\n\n# ── Load data ──\ncross_dif = pd.read_csv(ROOT / \"artifacts/plan_001/dif_results_temporal.csv\")\nwithin_dif = pd.read_csv(ROOT / \"artifacts/plan_014/within_subject_dif_detail.csv\")\nmeta = pd.read_csv(ROOT / \"artifacts/plan_032_dif_cleaned_mmlu/cleaned_mmlu_analysis.csv\")\n\n# Response matrix for accuracy delta computation\nrm_data = np.load(ROOT / \"artifacts/response_matrix.npz\")\nrm_idx = np.load(ROOT / \"artifacts/response_matrix_index.npz\", allow_pickle=True)\nresponse_matrix = sparse.csr_matrix(\n    (rm_data[\"data\"], rm_data[\"indices\"], rm_data[\"indptr\"]),\n    shape=tuple(rm_data[\"shape\"])\n)\nmodel_names = rm_idx[\"model_names\"]\nitem_ids = rm_idx[\"item_ids\"]\n\n# Build item-to-subject mapping from item_ids\nitem_subjects = pd.Series([iid.rsplit(\".\", 1)[0] for iid in item_ids], index=item_ids, name=\"subject\")\n\n# 5 subjects with within-subject DIF\nwithin_subjects = within_dif[\"subject\"].unique().tolist()\nprint(f\"Within-subject DIF subjects ({len(within_subjects)}): {within_subjects}\")\n\n# ── Part A: Cohen's κ for 5 subjects ──\nprint(\"\\n\" + \"=\"*60)\nprint(\"PART A: Cohen's κ — Cross vs Within DIF Classification\")\nprint(\"=\"*60)\n\nkappa_rows = []\nunique_c_items_all = {}\n\nfor subj in within_subjects:\n    cross_sub = cross_dif[cross_dif[\"subject\"] == subj][[\"item_id\", \"ets_class\"]].copy()\n    cross_sub.columns = [\"item_id\", \"cross_class\"]\n\n    within_sub = within_dif[within_dif[\"subject\"] == subj][[\"item_id\", \"ets_class\"]].copy()\n    within_sub.columns = [\"item_id\", \"within_class\"]\n\n    merged = cross_sub.merge(within_sub, on=\"item_id\", how=\"inner\")\n\n    # Binary: C vs not-C\n    merged[\"cross_C\"] = (merged[\"cross_class\"] == \"C\").astype(int)\n    merged[\"within_C\"] = (merged[\"within_class\"] == \"C\").astype(int)\n\n    # Cohen's kappa\n    kappa = cohen_kappa_score(merged[\"cross_C\"], merged[\"within_C\"])\n\n    # 2x2 contingency table\n    ct = pd.crosstab(merged[\"cross_C\"], merged[\"within_C\"],\n                     rownames=[\"cross_C\"], colnames=[\"within_C\"])\n\n    # Cross-unique C: cross=C AND within≠C\n    cross_unique_c = merged[(merged[\"cross_C\"] == 1) & (merged[\"within_C\"] == 0)]\n    n_cross_unique_c = len(cross_unique_c)\n    unique_c_items_all[subj] = cross_unique_c[\"item_id\"].tolist()\n\n    # Within-unique C: within=C AND cross≠C\n    within_unique_c = merged[(merged[\"within_C\"] == 1) & (merged[\"cross_C\"] == 0)]\n    n_within_unique_c = len(within_unique_c)\n\n    n_total = len(merged)\n    n_cross_c = merged[\"cross_C\"].sum()\n    n_within_c = merged[\"within_C\"].sum()\n\n    kappa_rows.append({\n        \"subject\": subj,\n        \"n_items\": n_total,\n        \"cross_C\": n_cross_c,\n        \"cross_C_pct\": 100 * n_cross_c / n_total,\n        \"within_C\": n_within_c,\n        \"within_C_pct\": 100 * n_within_c / n_total,\n        \"kappa\": kappa,\n        \"cross_unique_C\": n_cross_unique_c,\n        \"within_unique_C\": n_within_unique_c,\n        \"both_C\": merged[(merged[\"cross_C\"] == 1) & (merged[\"within_C\"] == 1)].shape[0],\n        \"neither_C\": merged[(merged[\"cross_C\"] == 0) & (merged[\"within_C\"] == 0)].shape[0],\n    })\n\n    print(f\"\\n{subj} (n={n_total}):\")\n    print(f\"  Cross C: {n_cross_c} ({100*n_cross_c/n_total:.1f}%), Within C: {n_within_c} ({100*n_within_c/n_total:.1f}%)\")\n    print(f\"  κ = {kappa:.3f}\")\n    print(f\"  Cross-unique C: {n_cross_unique_c}, Within-unique C: {n_within_unique_c}\")\n    print(f\"  Contingency table:\\n{ct}\")\n\nkappa_df = pd.DataFrame(kappa_rows)\nkappa_df.to_csv(OUT / \"kappa_results.csv\", index=False)\n\n# Summary statistics\nprint(f\"\\nOverall κ: mean={kappa_df['kappa'].mean():.3f}, range=[{kappa_df['kappa'].min():.3f}, {kappa_df['kappa'].max():.3f}]\")\nprint(f\"Cross C% mean: {kappa_df['cross_C_pct'].mean():.1f}%, Within C% mean: {kappa_df['within_C_pct'].mean():.1f}%\")\n\n# ── Part B: Domain accuracy delta vs cross-unique C concentration ──\nprint(\"\\n\" + \"=\"*60)\nprint(\"PART B: Domain Accuracy Delta vs Cross-Unique C Concentration\")\nprint(\"=\"*60)\n\n# Get 2023 and 2024 model indices\nmodel_cohort = meta.set_index(\"model_name\")[\"cohort_temporal\"]\nmodel_name_to_idx = {name: i for i, name in enumerate(model_names)}\n\nmodels_2023 = [m for m in model_cohort[model_cohort == \"2023\"].index if m in model_name_to_idx]\nmodels_2024 = [m for m in model_cohort[model_cohort == \"2024\"].index if m in model_name_to_idx]\nidx_2023 = [model_name_to_idx[m] for m in models_2023]\nidx_2024 = [model_name_to_idx[m] for m in models_2024]\nprint(f\"Models: 2023={len(idx_2023)}, 2024={len(idx_2024)}\")\n\n# Build item index mapping\nitem_id_to_col = {iid: i for i, iid in enumerate(item_ids)}\n\n# For each of the 5 subjects, compute domain accuracy delta\ndelta_rows = []\nfor subj in within_subjects:\n    subj_items = [iid for iid in item_ids if iid.rsplit(\".\", 1)[0] == subj]\n    col_indices = [item_id_to_col[iid] for iid in subj_items]\n\n    # Extract submatrix for this subject\n    sub_2023 = response_matrix[idx_2023][:, col_indices]\n    sub_2024 = response_matrix[idx_2024][:, col_indices]\n\n    # Mean accuracy per cohort (handle sparse: nonzero entries are correct answers=1)\n    # But we need to distinguish 0 (wrong) from missing. The matrix is sparse with 1=correct.\n    # Actually in a sparse matrix, 0s are implicit. Let's check density.\n    # For MMLU with 4-choice, all models answer all items, so density should be high.\n    # The matrix stores 1 for correct, 0 for incorrect (but 0 is not stored in sparse).\n    # So mean of dense matrix = accuracy.\n\n    acc_2023 = sub_2023.toarray().mean()\n    acc_2024 = sub_2024.toarray().mean()\n    acc_delta = acc_2024 - acc_2023\n\n    n_unique_c = len(unique_c_items_all[subj])\n    n_items = len(subj_items)\n\n    delta_rows.append({\n        \"subject\": subj,\n        \"n_items\": n_items,\n        \"acc_2023\": acc_2023,\n        \"acc_2024\": acc_2024,\n        \"acc_delta\": acc_delta,\n        \"cross_unique_C\": n_unique_c,\n        \"cross_unique_C_pct\": 100 * n_unique_c / n_items if n_items > 0 else 0,\n    })\n\n    print(f\"{subj}: acc_2023={acc_2023:.4f}, acc_2024={acc_2024:.4f}, Δ={acc_delta:+.4f}, unique_C={n_unique_c} ({100*n_unique_c/n_items:.1f}%)\")\n\ndelta_df = pd.DataFrame(delta_rows)\ndelta_df.to_csv(OUT / \"accuracy_delta_vs_unique_c.csv\", index=False)\n\n# Spearman correlation (5 data points — descriptive only)\nif len(delta_df) >= 3:\n    rho, p_val = stats.spearmanr(delta_df[\"acc_delta\"], delta_df[\"cross_unique_C_pct\"])\n    print(f\"\\nSpearman ρ(acc_delta, unique_C%): ρ={rho:.3f}, p={p_val:.3f}\")\n\n    # Also Pearson for reference\n    r, p_r = stats.pearsonr(delta_df[\"acc_delta\"], delta_df[\"cross_unique_C_pct\"])\n    print(f\"Pearson r(acc_delta, unique_C%): r={r:.3f}, p={p_r:.3f}\")\n\n# ── Part C: Direction argument ──\nprint(\"\\n\" + \"=\"*60)\nprint(\"PART C: Direction Argument\")\nprint(\"=\"*60)\n\ncross_c_pcts = kappa_df[\"cross_C_pct\"]\nwithin_c_pcts = kappa_df[\"within_C_pct\"]\n\nprint(f\"Mean cross-subject C%: {cross_c_pcts.mean():.1f}%\")\nprint(f\"Mean within-subject C%: {within_c_pcts.mean():.1f}%\")\nprint(f\"Within > Cross in {(within_c_pcts > cross_c_pcts).sum()}/{len(kappa_df)} subjects\")\n\nfor _, row in kappa_df.iterrows():\n    direction = \"within > cross\" if row[\"within_C_pct\"] > row[\"cross_C_pct\"] else \"cross > within\" if row[\"cross_C_pct\"] > row[\"within_C_pct\"] else \"equal\"\n    print(f\"  {row['subject']}: cross={row['cross_C_pct']:.1f}%, within={row['within_C_pct']:.1f}% ({direction})\")\n\n# ── Generate markdown report ──\nprint(\"\\n\" + \"=\"*60)\nprint(\"Generating report...\")\nprint(\"=\"*60)\n\nreport = []\nreport.append(\"# R14 Experiment 2: Cross-Subject-Unique C Item Concentration Analysis\\n\")\nreport.append(\"## Purpose\\n\")\nreport.append(\"Test whether items classified as C (large DIF) by cross-subject matching but NOT by within-subject matching\")\nreport.append(\"concentrate in subjects with large domain profile shifts. If they do not concentrate,\")\nreport.append(\"multidimensionality confound is unlikely to be the primary driver of cross-subject DIF flags.\\n\")\n\n# Part A\nreport.append(\"## Part A: Cohen's κ — Cross vs Within DIF Classification Agreement\\n\")\nreport.append(f\"Five subjects have both cross-subject and within-subject DIF results ({', '.join(within_subjects)}).\\n\")\nreport.append(\"| Subject | n | Cross C | Cross C% | Within C | Within C% | κ | Cross-unique C | Within-unique C |\")\nreport.append(\"|---------|---|---------|----------|----------|-----------|---|----------------|-----------------|\")\nfor _, row in kappa_df.iterrows():\n    report.append(f\"| {row['subject']} | {row['n_items']} | {row['cross_C']} | {row['cross_C_pct']:.1f}% | {row['within_C']} | {row['within_C_pct']:.1f}% | {row['kappa']:.3f} | {row['cross_unique_C']} | {row['within_unique_C']} |\")\n\nreport.append(f\"\\n**Summary**: Mean κ = {kappa_df['kappa'].mean():.3f} (range: {kappa_df['kappa'].min():.3f}–{kappa_df['kappa'].max():.3f}).\")\nreport.append(f\"Cross-subject matching flags fewer C items on average ({kappa_df['cross_C_pct'].mean():.1f}%) than within-subject matching ({kappa_df['within_C_pct'].mean():.1f}%).\\n\")\n\n# Part B\nreport.append(\"## Part B: Domain Accuracy Delta vs Cross-Unique C Concentration\\n\")\nreport.append(\"Domain accuracy delta = mean accuracy of 2024-cohort models minus 2023-cohort models per subject.\")\nreport.append(f\"Computed from {len(idx_2023)} (2023) and {len(idx_2024)} (2024) models.\\n\")\nreport.append(\"| Subject | n | Acc 2023 | Acc 2024 | Δ Acc | Cross-unique C | Cross-unique C% |\")\nreport.append(\"|---------|---|----------|----------|-------|----------------|-----------------|\")\nfor _, row in delta_df.iterrows():\n    report.append(f\"| {row['subject']} | {row['n_items']} | {row['acc_2023']:.4f} | {row['acc_2024']:.4f} | {row['acc_delta']:+.4f} | {row['cross_unique_C']} | {row['cross_unique_C_pct']:.1f}% |\")\n\nif len(delta_df) >= 3:\n    rho, p_val = stats.spearmanr(delta_df[\"acc_delta\"], delta_df[\"cross_unique_C_pct\"])\n    r, p_r = stats.pearsonr(delta_df[\"acc_delta\"], delta_df[\"cross_unique_C_pct\"])\n    report.append(f\"\\n**Correlation**: Spearman ρ = {rho:.3f} (p = {p_val:.3f}), Pearson r = {r:.3f} (p = {p_r:.3f}).\")\n    report.append(\"With only 5 data points, this is descriptive rather than inferential.\\n\")\n\n# Part C\nreport.append(\"## Part C: Direction Argument\\n\")\nreport.append(\"If multidimensionality confound were the primary driver of cross-subject DIF flags,\")\nreport.append(\"we would expect cross-subject matching to produce *more* C items than within-subject matching\")\nreport.append(\"(because the confound affects only cross-subject matching, inflating DIF estimates).\\n\")\nreport.append(\"**Observed**: The opposite direction holds.\")\nreport.append(f\"Within-subject C% ({kappa_df['within_C_pct'].mean():.1f}%) > Cross-subject C% ({kappa_df['cross_C_pct'].mean():.1f}%).\")\nn_within_higher = (within_c_pcts > cross_c_pcts).sum()\nreport.append(f\"This pattern holds in {n_within_higher}/{len(kappa_df)} subjects:\\n\")\nfor _, row in kappa_df.iterrows():\n    direction = \"✓ within > cross\" if row[\"within_C_pct\"] > row[\"cross_C_pct\"] else \"✗ cross ≥ within\"\n    report.append(f\"- {row['subject']}: cross {row['cross_C_pct']:.1f}% vs within {row['within_C_pct']:.1f}% ({direction})\")\n\nreport.append(\"\\nThis directional evidence indicates that cross-subject matching is *conservative* (flags fewer items as C),\")\nreport.append(\"contradicting the hypothesis that multidimensional confound inflates cross-subject DIF classification.\\n\")\n\n# Conclusion\nreport.append(\"## Conclusion\\n\")\ntotal_cross_unique = kappa_df[\"cross_unique_C\"].sum()\ntotal_items = kappa_df[\"n_items\"].sum()\nreport.append(f\"1. **Moderate agreement**: κ ranges from {kappa_df['kappa'].min():.3f} to {kappa_df['kappa'].max():.3f} (mean {kappa_df['kappa'].mean():.3f}), indicating moderate-to-fair agreement between matching methods on C classification.\")\nreport.append(f\"2. **Cross-unique C items are few**: Only {total_cross_unique} items across 5 subjects ({100*total_cross_unique/total_items:.1f}% of items) are flagged as C by cross-subject but not within-subject matching.\")\nif len(delta_df) >= 3:\n    report.append(f\"3. **No concentration by domain shift**: Spearman ρ = {rho:.3f} between accuracy delta and cross-unique C% — no evidence that cross-unique C items concentrate in high-shift domains.\")\nreport.append(f\"4. **Conservative direction**: Cross-subject matching produces fewer C flags than within-subject matching ({kappa_df['cross_C_pct'].mean():.1f}% vs {kappa_df['within_C_pct'].mean():.1f}%), the opposite of what multidimensionality confound would predict.\")\nreport.append(\"\\nThese findings collectively indicate that multidimensional confound is not the primary driver of DIF flags in cross-subject matching.\")\n\nreport_text = \"\\n\".join(report)\n(OUT / \"cross_subject_unique_analysis.md\").write_text(report_text)\nprint(f\"\\nReport written to {OUT / 'cross_subject_unique_analysis.md'}\")\nprint(\"Done.\")\n"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-22T12:01:24.373774+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r14_mf1_domain_profile/cross_subject_unique_analysis.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_r14_exp2_cross_subject_unique_20260522T115630",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-22T12:01:24.373923+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 artifacts/r14_mf1_domain_profile/cross_subject_unique_analysis.py",
  "description": "Run the cross-subject unique C analysis",
  "timeout": "120000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_r14_exp2_cross_subject_unique_20260522T115630",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 artifacts/r14_mf1_domain_profile/cross_subject_unique_analysis.py",
    "description": "Run the cross-subject unique C analysis",
    "timeout": "120000"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-22T12:01:24.374090+00:00_

Within-subject DIF subjects (5): ['business_ethics', 'human_aging', 'formal_logic', 'professional_medicine', 'high_school_statistics']

============================================================
PART A: Cohen's κ — Cross vs Within DIF Classification
============================================================

business_ethics (n=186):
  Cross C: 90 (48.4%), Within C: 87 (46.8%)
  κ = 0.925
  Cross-unique C: 5, Within-unique C: 2
  Contingency table:
within_C   0   1
cross_C         
0         94   2
1          5  85

human_aging (n=406):
  Cross C: 170 (41.9%), Within C: 152 (37.4%)
  κ = 0.877
  Cross-unique C: 21, Within-unique C: 3
  Contingency table:
within_C    0    1
cross_C           
0         233    3
1          21  149

formal_logic (n=218):
  Cross C: 88 (40.4%), Within C: 86 (39.4%)
  κ = 0.943
  Cross-unique C: 4, Within-unique C: 2
  Contingency table:
within_C    0   1
cross_C          
0         128   2
1           4  84

professional_medicine (n=496):
  Cross C: 188 (37.9%), Within C: 171 (34.5%)
  κ = 0.874
  Cross-unique C: 23, Within-unique C: 6
  Contingency table:
within_C    0    1
cross_C           
0         302    6
1          23  165

high_school_statistics (n=362):
  Cross C: 128 (35.4%), Within C: 139 (38.4%)
  κ = 0.864
  Cross-unique C: 6, Within-unique C: 17
  Contingency table:
within_C    0    1
cross_C           
0         217   17
1           6  122

Overall κ: mean=0.896, range=[0.864, 0.943]
Cross C% mean: 40.8%, Within C% mean: 39.3%

============================================================
PART B: Domain Accuracy Delta vs Cross-Unique C Concentration
============================================================
Models: 2023=1080, 2024=807
business_ethics: acc_2023=0.5582, acc_2024=0.6125, Δ=+0.0543, unique_C=5 (5.4%)
human_aging: acc_2023=0.6442, acc_2024=0.6597, Δ=+0.0155, unique_C=21 (10.3%)
formal_logic: acc_2023=0.4020, acc_2024=0.4461, Δ=+0.0440, unique_C=4 (3.7%)
professional_medicine: acc_2023=0.5948, acc_2024=0.6
…[truncated 1097 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_r14_exp2_cross_subject_unique_20260522T115630",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-22T12:01:24.374307+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport pandas as pd\ncross = pd.read_csv('artifacts/plan_001/dif_results_temporal.csv')\nwithin = pd.read_csv('artifacts/plan_014/within_subject_dif_detail.csv')\n\n# Check for duplicates\nfor subj in within['subject'].unique():\n    c = cross[cross['subject'] == subj]\n    w = within[within['subject'] == subj]\n    print(f'{subj}: cross={len(c)} (unique item_id={c[\\\"item_id\\\"].nunique()}), within={len(w)} (unique item_id={w[\\\"item_id\\\"].nunique()})')\n    # Check overlap\n    common = set(c['item_id']) & set(w['item_id'])\n    print(f'  overlap: {len(common)} items')\n\"\n",
  "description": "Check for duplicate items in data sources"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_r14_exp2_cross_subject_unique_20260522T115630",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport pandas as pd\ncross = pd.read_csv('artifacts/plan_001/dif_results_temporal.csv')\nwithin = pd.read_csv('artifacts/plan_014/within_subject_dif_detail.csv')\n\n# Check for duplicates\nfor subj in within['subject'].unique():\n    c = cross[cross['subject'] == subj]\n    w = within[within['subject'] == subj]\n    print(f'{subj}: cross={len(c)} (unique item_id={c[\\\"item_id\\\"].nunique()}), within={len(w)} (unique item_id={w[\\\"item_id\\\"].nunique()})')\n    # Check overlap\n    common = set(c['item_id']) & set(w['item_id'])\n    print(f'  overlap: {len(common)} items')\n\"\n",
    "description": "Check for duplicate items in data sources"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-22T12:01:24.374447+00:00_

business_ethics: cross=93 (unique item_id=93), within=186 (unique item_id=93)
  overlap: 93 items
human_aging: cross=203 (unique item_id=203), within=406 (unique item_id=203)
  overlap: 203 items
formal_logic: cross=109 (unique item_id=109), within=218 (unique item_id=109)
  overlap: 109 items
professional_medicine: cross=248 (unique item_id=248), within=496 (unique item_id=248)
  overlap: 248 items
high_school_statistics: cross=181 (unique item_id=181), within=362 (unique item_id=181)
  overlap: 181 items

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_r14_exp2_cross_subject_unique_20260522T115630",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-22T12:01:24.374601+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport pandas as pd\nwithin = pd.read_csv('artifacts/plan_014/within_subject_dif_detail.csv')\n# Show duplicates for one item\ndups = within[within['item_id'] == 'business_ethics.1']\nprint(dups.to_string())\nprint()\n# Check if duplicates are identical\nfor subj in within['subject'].unique():\n    w = within[within['subject'] == subj]\n    deduped = w.drop_duplicates(subset=['item_id'])\n    all_same = True\n    for iid in deduped['item_id']:\n        rows = w[w['item_id'] == iid]\n        if len(rows) > 1 and not rows.drop(columns=['item_id','subject']).iloc[0].equals(rows.drop(columns=['item_id','subject']).iloc[1]):\n            all_same = False\n            print(f'{subj}/{iid}: rows differ')\n            print(rows.to_string())\n            break\n    if all_same:\n        print(f'{subj}: all duplicates are identical')\n\"\n",
  "description": "Check if duplicate rows are identical"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_r14_exp2_cross_subject_unique_20260522T115630",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport pandas as pd\nwithin = pd.read_csv('artifacts/plan_014/within_subject_dif_detail.csv')\n# Show duplicates for one item\ndups = within[within['item_id'] == 'business_ethics.1']\nprint(dups.to_string())\nprint()\n# Check if duplicates are identical\nfor subj in within['subject'].unique():\n    w = within[within['subject'] == subj]\n    deduped = w.drop_duplicates(subset=['item_id'])\n    all_same = True\n    for iid in deduped['item_id']:\n        rows = w[w['item_id'] == iid]\n        if len(rows) > 1 and not rows.drop(columns=['item_id','subject']).iloc[0].equals(rows.drop(columns=['item_id','subject']).iloc[1]):\n            all_same = False\n            print(f'{subj}/{iid}: rows differ')\n            print(rows.to_string())\n            break\n    if all_same:\n        print(f'{subj}: all duplicates are identical')\n\"\n",
    "description": "Check if duplicate rows are identical"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-22T12:01:24.374762+00:00_

            subject            item_id matching_type  delta_mh   p_value ets_class  n_strata_used
0   business_ethics  business_ethics.1        within -1.351785  0.000059         B              5
93  business_ethics  business_ethics.1         cross -1.340018  0.000055         B              4

business_ethics/business_ethics.1: rows differ
            subject            item_id matching_type  delta_mh   p_value ets_class  n_strata_used
0   business_ethics  business_ethics.1        within -1.351785  0.000059         B              5
93  business_ethics  business_ethics.1         cross -1.340018  0.000055         B              4
human_aging/human_aging.1: rows differ
         subject        item_id matching_type  delta_mh   p_value ets_class  n_strata_used
186  human_aging  human_aging.1        within -1.106677  0.012076         B              4
389  human_aging  human_aging.1         cross -1.647141  0.000170         C              3
formal_logic/formal_logic.1: rows differ
          subject         item_id matching_type  delta_mh   p_value ets_class  n_strata_used
592  formal_logic  formal_logic.1        within -1.557046  0.002516         C              4
701  formal_logic  formal_logic.1         cross  0.211954  0.776139         A              4
professional_medicine/professional_medicine.10: rows differ
                    subject                   item_id matching_type  delta_mh   p_value ets_class  n_strata_used
810   professional_medicine  professional_medicine.10        within -0.783287  0.038764         A              5
1058  professional_medicine  professional_medicine.10         cross -1.351377  0.000259         B              5
high_school_statistics/high_school_statistics.10: rows differ
                     subject                    item_id matching_type  delta_mh       p_value ets_class  n_strata_used
1306  high_school_statistics  high_school_statistics.10        within  1.369070  2.958637e-07         B              5
1487  high_school_statistics  hig
…[truncated 85 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_r14_exp2_cross_subject_unique_20260522T115630",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-22T12:01:24.375141+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r14_mf1_domain_profile/cross_subject_unique_analysis.py",
  "old_string": "cross_dif = pd.read_csv(ROOT / \"artifacts/plan_001/dif_results_temporal.csv\")\nwithin_dif = pd.read_csv(ROOT / \"artifacts/plan_014/within_subject_dif_detail.csv\")",
  "new_string": "cross_dif = pd.read_csv(ROOT / \"artifacts/plan_001/dif_results_temporal.csv\")\nwithin_dif_raw = pd.read_csv(ROOT / \"artifacts/plan_014/within_subject_dif_detail.csv\")\nwithin_dif = within_dif_raw[within_dif_raw[\"matching_type\"] == \"within\"].copy()"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_r14_exp2_cross_subject_unique_20260522T115630",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r14_mf1_domain_profile/cross_subject_unique_analysis.py",
    "old_string": "cross_dif = pd.read_csv(ROOT / \"artifacts/plan_001/dif_results_temporal.csv\")\nwithin_dif = pd.read_csv(ROOT / \"artifacts/plan_014/within_subject_dif_detail.csv\")",
    "new_string": "cross_dif = pd.read_csv(ROOT / \"artifacts/plan_001/dif_results_temporal.csv\")\nwithin_dif_raw = pd.read_csv(ROOT / \"artifacts/plan_014/within_subject_dif_detail.csv\")\nwithin_dif = within_dif_raw[within_dif_raw[\"matching_type\"] == \"within\"].copy()"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-22T12:01:24.375350+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r14_mf1_domain_profile/cross_subject_unique_analysis.py has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_r14_exp2_cross_subject_unique_20260522T115630",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-22T12:01:24.375485+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 artifacts/r14_mf1_domain_profile/cross_subject_unique_analysis.py",
  "description": "Re-run with deduplication fix",
  "timeout": "120000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_r14_exp2_cross_subject_unique_20260522T115630",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 artifacts/r14_mf1_domain_profile/cross_subject_unique_analysis.py",
    "description": "Re-run with deduplication fix",
    "timeout": "120000"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-22T12:01:24.375659+00:00_

Within-subject DIF subjects (5): ['business_ethics', 'human_aging', 'formal_logic', 'professional_medicine', 'high_school_statistics']

============================================================
PART A: Cohen's κ — Cross vs Within DIF Classification
============================================================

business_ethics (n=93):
  Cross C: 45 (48.4%), Within C: 42 (45.2%)
  κ = 0.849
  Cross-unique C: 5, Within-unique C: 2
  Contingency table:
within_C   0   1
cross_C         
0         46   2
1          5  40

human_aging (n=203):
  Cross C: 85 (41.9%), Within C: 67 (33.0%)
  κ = 0.750
  Cross-unique C: 21, Within-unique C: 3
  Contingency table:
within_C    0   1
cross_C          
0         115   3
1          21  64

formal_logic (n=109):
  Cross C: 44 (40.4%), Within C: 43 (39.4%)
  κ = 0.904
  Cross-unique C: 3, Within-unique C: 2
  Contingency table:
within_C   0   1
cross_C         
0         63   2
1          3  41

professional_medicine (n=248):
  Cross C: 94 (37.9%), Within C: 77 (31.0%)
  κ = 0.743
  Cross-unique C: 23, Within-unique C: 6
  Contingency table:
within_C    0   1
cross_C          
0         148   6
1          23  71

high_school_statistics (n=181):
  Cross C: 64 (35.4%), Within C: 76 (42.0%)
  κ = 0.745
  Cross-unique C: 5, Within-unique C: 17
  Contingency table:
within_C    0   1
cross_C          
0         100  17
1           5  59

Overall κ: mean=0.798, range=[0.743, 0.904]
Cross C% mean: 40.8%, Within C% mean: 38.1%

============================================================
PART B: Domain Accuracy Delta vs Cross-Unique C Concentration
============================================================
Models: 2023=1080, 2024=807
business_ethics: acc_2023=0.5582, acc_2024=0.6125, Δ=+0.0543, unique_C=5 (5.4%)
human_aging: acc_2023=0.6442, acc_2024=0.6597, Δ=+0.0155, unique_C=21 (10.3%)
formal_logic: acc_2023=0.4020, acc_2024=0.4461, Δ=+0.0440, unique_C=3 (2.8%)
professional_medicine: acc_2023=0.5948, acc_2024=0.6302, Δ=+0.0354, unique_
…[truncated 1074 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_r14_exp2_cross_subject_unique_20260522T115630",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-22T12:01:24.375878+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r14_mf1_domain_profile/cross_subject_unique_analysis.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_r14_exp2_cross_subject_unique_20260522T115630",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r14_mf1_domain_profile/cross_subject_unique_analysis.md"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-22T12:01:24.376041+00:00_

1	# R14 Experiment 2: Cross-Subject-Unique C Item Concentration Analysis
2	
3	## Purpose
4	
5	Test whether items classified as C (large DIF) by cross-subject matching but NOT by within-subject matching
6	concentrate in subjects with large domain profile shifts. If they do not concentrate,
7	multidimensionality confound is unlikely to be the primary driver of cross-subject DIF flags.
8	
9	## Part A: Cohen's κ — Cross vs Within DIF Classification Agreement
10	
11	Five subjects have both cross-subject and within-subject DIF results (business_ethics, human_aging, formal_logic, professional_medicine, high_school_statistics).
12	
13	| Subject | n | Cross C | Cross C% | Within C | Within C% | κ | Cross-unique C | Within-unique C |
14	|---------|---|---------|----------|----------|-----------|---|----------------|-----------------|
15	| business_ethics | 93 | 45 | 48.4% | 42 | 45.2% | 0.849 | 5 | 2 |
16	| human_aging | 203 | 85 | 41.9% | 67 | 33.0% | 0.750 | 21 | 3 |
17	| formal_logic | 109 | 44 | 40.4% | 43 | 39.4% | 0.904 | 3 | 2 |
18	| professional_medicine | 248 | 94 | 37.9% | 77 | 31.0% | 0.743 | 23 | 6 |
19	| high_school_statistics | 181 | 64 | 35.4% | 76 | 42.0% | 0.745 | 5 | 17 |
20	
21	**Summary**: Mean κ = 0.798 (range: 0.743–0.904).
22	Cross-subject matching flags fewer C items on average (40.8%) than within-subject matching (38.1%).
23	
24	## Part B: Domain Accuracy Delta vs Cross-Unique C Concentration
25	
26	Domain accuracy delta = mean accuracy of 2024-cohort models minus 2023-cohort models per subject.
27	Computed from 1080 (2023) and 807 (2024) models.
28	
29	| Subject | n | Acc 2023 | Acc 2024 | Δ Acc | Cross-unique C | Cross-unique C% |
30	|---------|---|----------|----------|-------|----------------|-----------------|
31	| business_ethics | 93 | 0.5582 | 0.6125 | +0.0543 | 5 | 5.4% |
32	| human_aging | 203 | 0.6442 | 0.6597 | +0.0155 | 21 | 10.3% |
33	| formal_logic | 109 | 0.4020 | 0.4461 | +0.0440 | 3 | 2.8% |
34	| professional_medicine | 248 | 0.5948 
…[truncated 2157 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_r14_exp2_cross_subject_unique_20260522T115630",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-22T12:01:24.376275+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport pandas as pd\ncross = pd.read_csv('artifacts/plan_001/dif_results_temporal.csv')\nwithin_subjects = ['business_ethics', 'human_aging', 'formal_logic', 'professional_medicine', 'high_school_statistics']\n\n# Overall cross-subject C%\noverall_c = (cross['ets_class'] == 'C').mean() * 100\nprint(f'Overall cross-subject C%: {overall_c:.1f}% (n={len(cross)})')\n\n# Cross C% for these 5 subjects only\nsub5 = cross[cross['subject'].isin(within_subjects)]\nsub5_c = (sub5['ets_class'] == 'C').mean() * 100\nprint(f'5-subject cross C%: {sub5_c:.1f}% (n={len(sub5)})')\n\n# Per-subject cross C%\nfor s in within_subjects:\n    ss = cross[cross['subject'] == s]\n    print(f'  {s}: {(ss[\\\"ets_class\\\"]==\\\"C\\\").mean()*100:.1f}% (n={len(ss)})')\n\n# Within-subject data\nwithin_raw = pd.read_csv('artifacts/plan_014/within_subject_dif_detail.csv')\nwithin = within_raw[within_raw['matching_type'] == 'within']\nwithin_c_overall = (within['ets_class'] == 'C').mean() * 100\nprint(f'Overall within-subject C%: {within_c_overall:.1f}% (n={len(within)})')\n\"\n",
  "description": "Check overall C% statistics for context"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_r14_exp2_cross_subject_unique_20260522T115630",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport pandas as pd\ncross = pd.read_csv('artifacts/plan_001/dif_results_temporal.csv')\nwithin_subjects = ['business_ethics', 'human_aging', 'formal_logic', 'professional_medicine', 'high_school_statistics']\n\n# Overall cross-subject C%\noverall_c = (cross['ets_class'] == 'C').mean() * 100\nprint(f'Overall cross-subject C%: {overall_c:.1f}% (n={len(cross)})')\n\n# Cross C% for these 5 subjects only\nsub5 = cross[cross['subject'].isin(within_subjects)]\nsub5_c = (sub5['ets_class'] == 'C').mean() * 100\nprint(f'5-subject cross C%: {sub5_c:.1f}% (n={len(sub5)})')\n\n# Per-subject cross C%\nfor s in within_subjects:\n    ss = cross[cross['subject'] == s]\n    print(f'  {s}: {(ss[\\\"ets_class\\\"]==\\\"C\\\").mean()*100:.1f}% (n={len(ss)})')\n\n# Within-subject data\nwithin_raw = pd.read_csv('artifacts/plan_014/within_subject_dif_detail.csv')\nwithin = within_raw[within_raw['matching_type'] == 'within']\nwithin_c_overall = (within['ets_class'] == 'C').mean() * 100\nprint(f'Overall within-subject C%: {within_c_overall:.1f}% (n={len(within)})')\n\"\n",
    "description": "Check overall C% statistics for context"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-22T12:01:24.376430+00:00_

Overall cross-subject C%: 31.3% (n=12508)
5-subject cross C%: 39.8% (n=834)
  business_ethics: 48.4% (n=93)
  human_aging: 41.9% (n=203)
  formal_logic: 40.4% (n=109)
  professional_medicine: 37.9% (n=248)
  high_school_statistics: 35.4% (n=181)
Overall within-subject C%: 36.6% (n=834)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_r14_exp2_cross_subject_unique_20260522T115630",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-22T12:01:24.376614+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r14_mf1_domain_profile/cross_subject_unique_analysis.md",
  "content": "# R14 Experiment 2: Cross-Subject-Unique C Item Concentration Analysis\n\n## Purpose\n\nTest whether items classified as C (large DIF) by cross-subject matching but NOT by within-subject matching\nconcentrate in subjects with large domain profile shifts. If they do not concentrate,\nmultidimensionality confound is unlikely to be the primary driver of cross-subject DIF flags.\n\n## Part A: Cohen's κ — Cross vs Within DIF Classification Agreement\n\nFive subjects have both cross-subject and within-subject DIF results (business_ethics, human_aging, formal_logic, professional_medicine, high_school_statistics).\n\n| Subject | n | Cross C | Cross C% | Within C | Within C% | κ | Cross-unique C | Within-unique C |\n|---------|---|---------|----------|----------|-----------|---|----------------|-----------------|\n| business_ethics | 93 | 45 | 48.4% | 42 | 45.2% | 0.849 | 5 | 2 |\n| human_aging | 203 | 85 | 41.9% | 67 | 33.0% | 0.750 | 21 | 3 |\n| formal_logic | 109 | 44 | 40.4% | 43 | 39.4% | 0.904 | 3 | 2 |\n| professional_medicine | 248 | 94 | 37.9% | 77 | 31.0% | 0.743 | 23 | 6 |\n| high_school_statistics | 181 | 64 | 35.4% | 76 | 42.0% | 0.745 | 5 | 17 |\n\n**Summary**: Mean κ = 0.798 (range: 0.743–0.904), indicating substantial agreement between matching methods.\nCross-subject matching flags slightly more C items on average (40.8%) than within-subject matching (38.1%) for these 5 subjects — the difference is 2.7 pp.\n\n## Part B: Domain Accuracy Delta vs Cross-Unique C Concentration\n\nDomain accuracy delta = mean accuracy of 2024-cohort models minus 2023-cohort models per subject.\nComputed from 1,080 (2023) and 807 (2024) models.\n\n| Subject | n | Acc 2023 | Acc 2024 | Δ Acc | Cross-unique C | Cross-unique C% |\n|---------|---|----------|----------|-------|----------------|-----------------|\n| business_ethics | 93 | 0.5582 | 0.6125 | +0.0543 | 5 | 5.4% |\n| human_aging | 203 | 0.6442 | 0.6597 | +0.0155 | 21 | 10.3% |\n| formal_logic | 109 | 0.4020 | 0.4461 | +0.0440 | 3 | 2.8% |\n| professional_medicine | 248 | 0.5948 | 0.6302 | +0.0354 | 23 | 9.3% |\n| high_school_statistics | 181 | 0.4900 | 0.5320 | +0.0420 | 5 | 2.8% |\n\n**Correlation**: Spearman ρ = −0.700 (p = 0.188), Pearson r = −0.724 (p = 0.167).\nWith only 5 data points, this is descriptive rather than inferential. The direction is *negative*: subjects with larger accuracy deltas tend to have *fewer* cross-unique C items, not more.\n\n## Part C: Direction Argument\n\nIf multidimensionality confound were the primary driver of cross-subject DIF flags,\nwe would expect cross-subject matching to produce substantially more C items than within-subject matching\n(because the confound affects only cross-subject matching, inflating DIF estimates).\n\n**Observed** (same 834 items, 5 subjects):\n- Item-weighted: cross C% = 39.8%, within C% = 36.6% (Δ = 3.2 pp)\n- Per-subject average: cross C% = 40.8%, within C% = 38.1% (Δ = 2.7 pp)\n- Cross > within in 4/5 subjects; high_school_statistics is the exception (cross 35.4% < within 42.0%)\n\nThe cross-subject method does flag slightly more C items, consistent with the direction a confound would predict. However, the magnitude is small (2.7–3.2 pp), and κ ≥ 0.74 across all subjects, indicating the two methods largely agree on which items show large DIF.\n\n**Context**: The overall cross-subject C% across all 57 MMLU subjects is 31.3% (12,508 items). These 5 subjects were selected for within-subject analysis precisely because they had high DIF rates, which explains why their cross C% (39.8%) exceeds the overall average.\n\n## Conclusion\n\n1. **Substantial agreement**: κ ranges from 0.743 to 0.904 (mean 0.798). The two matching methods agree on the DIF classification for the large majority of items.\n2. **Cross-unique C items are few**: Only 57 items across 5 subjects (6.8% of 834 items) are flagged as C by cross-subject but not within-subject matching.\n3. **No concentration by domain shift**: Spearman ρ = −0.700 between accuracy delta and cross-unique C% — the direction is *negative*, meaning cross-unique C items do not cluster in high-shift domains. The two subjects with the most cross-unique C items (human_aging: 21, professional_medicine: 23) have intermediate accuracy deltas (+0.016 and +0.035), not the largest.\n4. **Small directional gap**: Cross-subject matching produces 2.7 pp more C flags than within-subject matching for these 5 subjects. This is consistent with a mild confound effect, but the magnitude is small relative to the overall C rate (~40%) and the high inter-method agreement.\n\nThe combination of high κ, few cross-unique C items, and the absence of concentration in high-shift domains indicates that multidimensional confound contributes at most a minor secondary effect to cross-subject DIF classification, not the primary signal.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_r14_exp2_cross_subject_unique_20260522T115630",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r14_mf1_domain_profile/cross_subject_unique_analysis.md",
    "content": "# R14 Experiment 2: Cross-Subject-Unique C Item Concentration Analysis\n\n## Purpose\n\nTest whether items classified as C (large DIF) by cross-subject matching but NOT by within-subject matching\nconcentrate in subjects with large domain profile shifts. If they do not concentrate,\nmultidimensionality confound is unlikely to be the primary driver of cross-subject DIF flags.\n\n## Part A: Cohen's κ — Cross vs Within DIF Classification Agreement\n\nFive subjects have both cross-subject and within-subject DIF results (business_ethics, human_aging, formal_logic, professional_medicine, high_school_statistics).\n\n| Subject | n | Cross C | Cross C% | Within C | Within C% | κ | Cross-unique C | Within-unique C |\n|---------|---|---------|----------|----------|-----------|---|----------------|-----------------|\n| business_ethics | 93 | 45 | 48.4% | 42 | 45.2% | 0.849 | 5 | 2 |\n| human_aging | 203 | 85 | 41.9% | 67 | 33.0% | 0.750 | 21 | 3 |\n| formal_logic | 109 | 44 | 40.4% | 43 | 39.4% | 0.904 | 3 | 2 |\n| professional_medicine | 248 | 94 | 37.9% | 77 | 31.0% | 0.743 | 23 | 6 |\n| high_school_statistics | 181 | 64 | 35.4% | 76 | 42.0% | 0.745 | 5 | 17 |\n\n**Summary**: Mean κ = 0.798 (range: 0.743–0.904), indicating substantial agreement between matching methods.\nCross-subject matching flags slightly more C items on average (40.8%) than within-subject matching (38.1%) for these 5 subjects — the difference is 2.7 pp.\n\n## Part B: Domain Accuracy Delta vs Cross-Unique C Concentration\n\nDomain accuracy delta = mean accuracy of 2024-cohort models minus 2023-cohort models per subject.\nComputed from 1,080 (2023) and 807 (2024) models.\n\n| Subject | n | Acc 2023 | Acc 2024 | Δ Acc | Cross-unique C | Cross-unique C% |\n|---------|---|----------|----------|-------|----------------|-----------------|\n| business_ethics | 93 | 0.5582 | 0.6125 | +0.0543 | 5 | 5.4% |\n| human_aging | 203 | 0.6442 | 0.6597 | +0.0155 | 21 | 10.3% |\n| formal_logic | 109 | 0.4020 | 0.4461 | +0.0440 | 3 | 2.8% |\n| professional_medicine | 248 | 0.5948 | 0.6302 | +0.0354 | 23 | 9.3% |\n| high_school_statistics | 181 | 0.4900 | 0.5320 | +0.0420 | 5 | 2.8% |\n\n**Correlation**: Spearman ρ = −0.700 (p = 0.188), Pearson r = −0.724 (p = 0.167).\nWith only 5 data points, this is descriptive rather than inferential. The direction is *negative*: subjects with larger accuracy deltas tend to have *fewer* cross-unique C items, not more.\n\n## Part C: Direction Argument\n\nIf multidimensionality confound were the primary driver of cross-subject DIF flags,\nwe would expect cross-subject matching to produce substantially more C items than within-subject matching\n(because the confound affects only cross-subject matching, inflating DIF estimates).\n\n**Observed** (same 834 items, 5 subjects):\n- Item-weighted: cross C% = 39.8%, within C% = 36.6% (Δ = 3.2 pp)\n- Per-subject average: cross C% = 40.8%, within C% = 38.1% (Δ = 2.7 pp)\n- Cross > within in 4/5 subjects; high_school_statistics is the exception (cross 35.4% < within 42.0%)\n\nThe cross-subject method does flag slightly more C items, consistent with the direction a confound would predict. However, the magnitude is small (2.7–3.2 pp), and κ ≥ 0.74 across all subjects, indicating the two methods largely agree on which items show large DIF.\n\n**Context**: The overall cross-subject C% across all 57 MMLU subjects is 31.3% (12,508 items). These 5 subjects were selected for within-subject analysis precisely because they had high DIF rates, which explains why their cross C% (39.8%) exceeds the overall average.\n\n## Conclusion\n\n1. **Substantial agreement**: κ ranges from 0.743 to 0.904 (mean 0.798). The two matching methods agree on the DIF classification for the large majority of items.\n2. **Cross-unique C items are few**: Only 57 items across 5 subjects (6.8% of 834 items) are flagged as C by cross-subject but not within-subject matching.\n3. **No concentration by domain shift**: Spearman ρ = −0.700 between accuracy delta and cross-unique C% — the direction is *negative*, meaning cross-unique C items do not cluster in high-shift domains. The two subjects with the most cross-unique C items (human_aging: 21, professional_medicine: 23) have intermediate accuracy deltas (+0.016 and +0.035), not the largest.\n4. **Small directional gap**: Cross-subject matching produces 2.7 pp more C flags than within-subject matching for these 5 subjects. This is consistent with a mild confound effect, but the magnitude is small relative to the overall C rate (~40%) and the high inter-method agreement.\n\nThe combination of high κ, few cross-unique C items, and the absence of concentration in high-shift domains indicates that multidimensional confound contributes at most a minor secondary effect to cross-subject DIF classification, not the primary signal.\n"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-22T12:01:24.376867+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r14_mf1_domain_profile/cross_subject_unique_analysis.md has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_r14_exp2_cross_subject_unique_20260522T115630",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-22T12:01:24.377017+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r14_mf1_domain_profile/",
  "description": "Verify output files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_r14_exp2_cross_subject_unique_20260522T115630",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r14_mf1_domain_profile/",
    "description": "Verify output files"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-22T12:01:24.377147+00:00_

total 52
drwxr-xr-x  2 ubuntu ubuntu  4096 May 22 12:01 .
drwxr-xr-x 63 ubuntu ubuntu  4096 May 22 11:58 ..
-rw-r--r--  1 ubuntu ubuntu   582 May 22 11:59 accuracy_delta_vs_unique_c.csv
-rw-r--r--  1 ubuntu ubuntu  4802 May 22 12:01 cross_subject_unique_analysis.md
-rw-r--r--  1 ubuntu ubuntu 13224 May 22 11:59 cross_subject_unique_analysis.py
-rw-r--r--  1 ubuntu ubuntu  1973 May 22 11:58 domain_profile_analysis.md
-rw-r--r--  1 ubuntu ubuntu   438 May 22 11:58 domain_profile_results.csv
-rw-r--r--  1 ubuntu ubuntu   580 May 22 11:59 kappa_results.csv
-rw-r--r--  1 ubuntu ubuntu  2977 May 22 11:58 subject_profile_results.csv

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_r14_exp2_cross_subject_unique_20260522T115630",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 39 · 2026-05-22T12:01:24.377319+00:00_

All outputs are in `artifacts/r14_mf1_domain_profile/`:

| File | Content |
|------|---------|
| `cross_subject_unique_analysis.md` | Full report |
| `kappa_results.csv` | Per-subject κ and contingency counts |
| `accuracy_delta_vs_unique_c.csv` | Accuracy delta vs cross-unique C |
| `cross_subject_unique_analysis.py` | Reproducible script |

**Key findings**:

- **κ = 0.798 mean** (0.743–0.904): substantial agreement between cross-subject and within-subject matching on C classification
- **57 cross-unique C items** (6.8% of 834): few items are flagged C only by cross-subject matching
- **ρ = −0.700** (p = 0.188): cross-unique C items do NOT concentrate in high-shift domains — direction is negative (more shift → fewer unique C items)
- **Direction**: cross C% (40.8%) slightly exceeds within C% (38.1%) for these 5 subjects (Δ = 2.7 pp), consistent with a mild confound effect but small relative to ~40% base rate

**Bottom line**: multidimensional confound contributes at most a minor secondary effect. The high inter-method agreement and lack of domain-shift concentration rule it out as the primary driver of cross-subject DIF flags.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_code_r14_exp2_cross_subject_unique_20260522T115630"
}
```

</details>

---
