# code r14 exp1 domain profile

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 15
- **Recorded user turns:** 0
- **Tool calls:** 7
- **Original source:** `logs/chats/worker_code_r14_exp1_domain_profile_20260522T115610.jsonl`
- **Structured JSON:** [`4518cf8f785d2b4dc13b.json`](../../sessions/45/4518cf8f785d2b4dc13b.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

15 recorded events

### Tool call

_source line 1 · 2026-05-22T11:58:26.593504+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport numpy as np\n# Load response matrix\nrm = np.load('artifacts/response_matrix.npz')\nprint('Response matrix keys:', list(rm.keys()))\nprint('X shape:', rm['X'].shape)\n\nidx = np.load('artifacts/response_matrix_index.npz', allow_pickle=True)\nprint('Index keys:', list(idx.keys()))\nprint('model_names[:5]:', idx['model_names'][:5])\nprint('item_ids[:5]:', idx['item_ids'][:5])\nprint('n_models:', len(idx['model_names']), 'n_items:', len(idx['item_ids']))\n\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_r14_exp1_domain_profile_20260522T115610",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport numpy as np\n# Load response matrix\nrm = np.load('artifacts/response_matrix.npz')\nprint('Response matrix keys:', list(rm.keys()))\nprint('X shape:', rm['X'].shape)\n\nidx = np.load('artifacts/response_matrix_index.npz', allow_pickle=True)\nprint('Index keys:', list(idx.keys()))\nprint('model_names[:5]:', idx['model_names'][:5])\nprint('item_ids[:5]:', idx['item_ids'][:5])\nprint('n_models:', len(idx['model_names']), 'n_items:', len(idx['item_ids']))\n\"\n"
  }
}
```

</details>

---

### Tool call

_source line 2 · 2026-05-22T11:58:26.594032+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport pandas as pd\nmeta = pd.read_csv('artifacts/plan_032_dif_cleaned_mmlu/cleaned_mmlu_analysis.csv')\nprint('Meta columns:', list(meta.columns))\nprint('Meta shape:', meta.shape)\nprint('cohort_temporal value_counts:')\nprint(meta['cohort_temporal'].value_counts())\nprint()\nprint('Sample model_name:', meta['model_name'].iloc[:3].tolist())\n\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_r14_exp1_domain_profile_20260522T115610",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport pandas as pd\nmeta = pd.read_csv('artifacts/plan_032_dif_cleaned_mmlu/cleaned_mmlu_analysis.csv')\nprint('Meta columns:', list(meta.columns))\nprint('Meta shape:', meta.shape)\nprint('cohort_temporal value_counts:')\nprint(meta['cohort_temporal'].value_counts())\nprint()\nprint('Sample model_name:', meta['model_name'].iloc[:3].tolist())\n\"\n"
  }
}
```

</details>

---

### Tool result

_source line 3 · 2026-05-22T11:58:26.594309+00:00_

Exit code 1
Traceback (most recent call last):
  File "&lt;string>", line 6, in &lt;module>
    print('X shape:', rm['X'].shape)
                      ~~^^^^^
  File "/usr/lib/python3/dist-packages/numpy/lib/_npyio_impl.py", line 243, in __getitem__
    raise KeyError(f"{key} is not a file in the archive") from None
KeyError: 'X is not a file in the archive'
Response matrix keys: ['indices', 'indptr', 'format', 'shape', 'data']

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_r14_exp1_domain_profile_20260522T115610",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-22T11:58:26.595093+00:00_

&lt;tool_use_error>Cancelled: parallel tool call Bash(python3 -c "
import numpy as np
# Load r…) errored&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_r14_exp1_domain_profile_20260522T115610",
  "tool": "Bash",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-22T11:58:26.595365+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport numpy as np\nfrom scipy import sparse\n\nrm = np.load('artifacts/response_matrix.npz')\nprint('Keys:', list(rm.keys()))\nprint('Shape:', rm['shape'])\nprint('Format:', rm['format'])\n\n# Load as sparse\nX = sparse.load_npz('artifacts/response_matrix.npz')\nprint('Sparse type:', type(X))\nprint('X shape:', X.shape)\nprint('X dtype:', X.dtype)\nprint('nnz:', X.nnz)\n# Check value range\nprint('min:', X.data.min(), 'max:', X.data.max())\nprint('unique values sample:', np.unique(X.data)[:10])\n\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_r14_exp1_domain_profile_20260522T115610",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport numpy as np\nfrom scipy import sparse\n\nrm = np.load('artifacts/response_matrix.npz')\nprint('Keys:', list(rm.keys()))\nprint('Shape:', rm['shape'])\nprint('Format:', rm['format'])\n\n# Load as sparse\nX = sparse.load_npz('artifacts/response_matrix.npz')\nprint('Sparse type:', type(X))\nprint('X shape:', X.shape)\nprint('X dtype:', X.dtype)\nprint('nnz:', X.nnz)\n# Check value range\nprint('min:', X.data.min(), 'max:', X.data.max())\nprint('unique values sample:', np.unique(X.data)[:10])\n\"\n"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-22T11:58:26.595581+00:00_

Keys: ['indices', 'indptr', 'format', 'shape', 'data']
Shape: [ 5227 12508]
Format: np.bytes_(b'csr')
Sparse type: &lt;class 'scipy.sparse._csr.csr_matrix'>
X shape: (5227, 12508)
X dtype: int8
nnz: 38654082
min: 1 max: 1
unique values sample: [1]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_r14_exp1_domain_profile_20260522T115610",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-22T11:58:26.595815+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport pandas as pd\nimport numpy as np\n\nmeta = pd.read_csv('artifacts/plan_032_dif_cleaned_mmlu/cleaned_mmlu_analysis.csv')\nprint('Meta columns:', list(meta.columns))\nprint('Meta shape:', meta.shape)\nprint('cohort_temporal value_counts:')\nprint(meta['cohort_temporal'].value_counts())\nprint()\nprint('Sample model_name:', meta['model_name'].iloc[:3].tolist())\n\nidx = np.load('artifacts/response_matrix_index.npz', allow_pickle=True)\nprint()\nprint('Index keys:', list(idx.keys()))\nmn = idx['model_names']\nii = idx['item_ids']\nprint('model_names[:3]:', mn[:3])\nprint('item_ids[:5]:', ii[:5])\nprint('n_models:', len(mn), 'n_items:', len(ii))\n# Parse subjects from item_ids\nsubjects = set()\nfor item in ii[:20]:\n    parts = str(item).rsplit('.', 1)\n    subjects.add(parts[0])\nprint('Sample subjects:', list(subjects)[:5])\n\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_r14_exp1_domain_profile_20260522T115610",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport pandas as pd\nimport numpy as np\n\nmeta = pd.read_csv('artifacts/plan_032_dif_cleaned_mmlu/cleaned_mmlu_analysis.csv')\nprint('Meta columns:', list(meta.columns))\nprint('Meta shape:', meta.shape)\nprint('cohort_temporal value_counts:')\nprint(meta['cohort_temporal'].value_counts())\nprint()\nprint('Sample model_name:', meta['model_name'].iloc[:3].tolist())\n\nidx = np.load('artifacts/response_matrix_index.npz', allow_pickle=True)\nprint()\nprint('Index keys:', list(idx.keys()))\nmn = idx['model_names']\nii = idx['item_ids']\nprint('model_names[:3]:', mn[:3])\nprint('item_ids[:5]:', ii[:5])\nprint('n_models:', len(mn), 'n_items:', len(ii))\n# Parse subjects from item_ids\nsubjects = set()\nfor item in ii[:20]:\n    parts = str(item).rsplit('.', 1)\n    subjects.add(parts[0])\nprint('Sample subjects:', list(subjects)[:5])\n\"\n"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-22T11:58:26.596041+00:00_

Meta columns: ['model_name', 'score_full', 'score_cleaned', 'rank_full', 'rank_cleaned', 'rank_change', 'abs_rank_change', 'family', 'cohort_temporal']
Meta shape: (5227, 9)
cohort_temporal value_counts:
cohort_temporal
other    3340
2023     1080
2024      807
Name: count, dtype: int64

Sample model_name: ['0-hero/Matter-0.1-7B', '0-hero/Matter-0.1-7B-DPO-preview', '0-hero/Matter-0.1-7B-boost']

Index keys: ['model_names', 'item_ids']
model_names[:3]: ['0-hero/Matter-0.1-7B' '0-hero/Matter-0.1-7B-DPO-preview'
 '0-hero/Matter-0.1-7B-boost']
item_ids[:5]: ['abstract_algebra.1' 'abstract_algebra.10' 'abstract_algebra.100'
 'abstract_algebra.11' 'abstract_algebra.12']
n_models: 5227 n_items: 12508
Sample subjects: ['abstract_algebra']

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_r14_exp1_domain_profile_20260522T115610",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-22T11:58:26.596380+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "mkdir -p artifacts/r14_mf1_domain_profile"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_r14_exp1_domain_profile_20260522T115610",
  "tool": "Bash",
  "tool_args": {
    "command": "mkdir -p artifacts/r14_mf1_domain_profile"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-22T11:58:26.596576+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_r14_exp1_domain_profile_20260522T115610",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-22T11:58:26.596845+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/scripts/r14_domain_profile.py",
  "content": "\"\"\"R14 MF1: Domain-Level Ability Profile Analysis.\n\nCompares 2023 vs 2024 cohort accuracy across MMLU domains.\nIf all domain-level Cohen's d < 0.3 → profile shift is flat,\nruling out multidimensional spurious DIF as a confound.\n\"\"\"\n\nimport numpy as np\nimport pandas as pd\nfrom scipy import sparse, stats\nfrom pathlib import Path\n\nROOT = Path(__file__).resolve().parent.parent\nOUT = ROOT / \"artifacts\" / \"r14_mf1_domain_profile\"\nOUT.mkdir(parents=True, exist_ok=True)\n\n# --- MMLU Subject → Domain mapping ---\nDOMAIN_MAP = {}\nfor s in [\n    \"abstract_algebra\", \"anatomy\", \"astronomy\", \"college_biology\",\n    \"college_chemistry\", \"college_computer_science\", \"college_mathematics\",\n    \"college_physics\", \"computer_security\", \"conceptual_physics\",\n    \"electrical_engineering\", \"elementary_mathematics\", \"high_school_biology\",\n    \"high_school_chemistry\", \"high_school_computer_science\",\n    \"high_school_mathematics\", \"high_school_physics\", \"high_school_statistics\",\n    \"machine_learning\", \"medical_genetics\", \"virology\",\n]:\n    DOMAIN_MAP[s] = \"STEM\"\n\nfor s in [\n    \"formal_logic\", \"high_school_european_history\", \"high_school_us_history\",\n    \"high_school_world_history\", \"international_law\", \"jurisprudence\",\n    \"logical_fallacies\", \"moral_disputes\", \"moral_scenarios\", \"philosophy\",\n    \"prehistory\", \"world_religions\",\n]:\n    DOMAIN_MAP[s] = \"Humanities\"\n\nfor s in [\n    \"econometrics\", \"high_school_geography\",\n    \"high_school_government_and_politics\", \"high_school_macroeconomics\",\n    \"high_school_microeconomics\", \"high_school_psychology\",\n    \"human_sexuality\", \"professional_psychology\", \"public_relations\",\n    \"security_studies\", \"sociology\", \"us_foreign_policy\",\n]:\n    DOMAIN_MAP[s] = \"Social Science\"\n\nfor s in [\n    \"business_ethics\", \"clinical_knowledge\", \"college_medicine\",\n    \"global_facts\", \"human_aging\", \"management\", \"marketing\",\n    \"miscellaneous\", \"nutrition\", \"professional_accounting\",\n    \"professional_law\", \"professional_medicine\",\n]:\n    DOMAIN_MAP[s] = \"Other\"\n\n# --- Load data ---\nprint(\"Loading response matrix...\")\nX = sparse.load_npz(ROOT / \"artifacts\" / \"response_matrix.npz\")\nidx = np.load(ROOT / \"artifacts\" / \"response_matrix_index.npz\", allow_pickle=True)\nmodel_names = idx[\"model_names\"]\nitem_ids = idx[\"item_ids\"]\n\nmeta = pd.read_csv(ROOT / \"artifacts\" / \"plan_032_dif_cleaned_mmlu\" / \"cleaned_mmlu_analysis.csv\")\n\n# --- Build cohort masks ---\nmodel_to_idx = {name: i for i, name in enumerate(model_names)}\nmeta_2023 = meta[meta[\"cohort_temporal\"] == \"2023\"]\nmeta_2024 = meta[meta[\"cohort_temporal\"] == \"2024\"]\n\nidx_2023 = np.array([model_to_idx[m] for m in meta_2023[\"model_name\"] if m in model_to_idx])\nidx_2024 = np.array([model_to_idx[m] for m in meta_2024[\"model_name\"] if m in model_to_idx])\nprint(f\"Cohort sizes: 2023={len(idx_2023)}, 2024={len(idx_2024)}\")\n\n# --- Parse item subjects and map to domains ---\nitem_subjects = np.array([str(iid).rsplit(\".\", 1)[0] for iid in item_ids])\nunique_subjects = sorted(set(item_subjects))\nprint(f\"Found {len(unique_subjects)} unique subjects\")\n\nunmapped = [s for s in unique_subjects if s not in DOMAIN_MAP]\nif unmapped:\n    print(f\"WARNING: unmapped subjects (assigned to Other): {unmapped}\")\n    for s in unmapped:\n        DOMAIN_MAP[s] = \"Other\"\n\nitem_domains = np.array([DOMAIN_MAP[s] for s in item_subjects])\n\n# --- Convert to dense for cohort subsets (memory ~OK for 1887 × 12508 int8) ---\nprint(\"Extracting cohort submatrices...\")\nX_2023 = X[idx_2023].toarray().astype(np.float32)  # (1080, 12508)\nX_2024 = X[idx_2024].toarray().astype(np.float32)  # (807, 12508)\n\n# --- Per-domain analysis ---\ndomains = [\"STEM\", \"Humanities\", \"Social Science\", \"Other\"]\nresults = []\n\nfor domain in domains:\n    col_mask = item_domains == domain\n    n_items = col_mask.sum()\n    n_subjects = len(set(item_subjects[col_mask]))\n\n    acc_2023 = X_2023[:, col_mask].mean(axis=1)  # per-model accuracy\n    acc_2024 = X_2024[:, col_mask].mean(axis=1)\n\n    mean_2023 = acc_2023.mean()\n    mean_2024 = acc_2024.mean()\n    sd_2023 = acc_2023.std(ddof=1)\n    sd_2024 = acc_2024.std(ddof=1)\n\n    # Pooled SD for Cohen's d\n    n1, n2 = len(acc_2023), len(acc_2024)\n    pooled_sd = np.sqrt(((n1 - 1) * sd_2023**2 + (n2 - 1) * sd_2024**2) / (n1 + n2 - 2))\n    d = (mean_2024 - mean_2023) / pooled_sd if pooled_sd > 0 else 0.0\n\n    # 95% CI for d using standard formula\n    se_d = np.sqrt((n1 + n2) / (n1 * n2) + d**2 / (2 * (n1 + n2)))\n    d_ci_lower = d - 1.96 * se_d\n    d_ci_upper = d + 1.96 * se_d\n\n    results.append({\n        \"domain\": domain,\n        \"n_items\": int(n_items),\n        \"n_subjects\": int(n_subjects),\n        \"mean_acc_2023\": round(float(mean_2023), 4),\n        \"sd_acc_2023\": round(float(sd_2023), 4),\n        \"mean_acc_2024\": round(float(mean_2024), 4),\n        \"sd_acc_2024\": round(float(sd_2024), 4),\n        \"cohens_d\": round(float(d), 4),\n        \"d_ci_lower\": round(float(d_ci_lower), 4),\n        \"d_ci_upper\": round(float(d_ci_upper), 4),\n    })\n    print(f\"  {domain:16s}: d={d:+.4f} [{d_ci_lower:.4f}, {d_ci_upper:.4f}]  \"\n          f\"acc_2023={mean_2023:.4f}  acc_2024={mean_2024:.4f}  n_items={n_items}\")\n\n# --- Overall ---\nacc_2023_all = X_2023.mean(axis=1)\nacc_2024_all = X_2024.mean(axis=1)\nmean_all_2023 = acc_2023_all.mean()\nmean_all_2024 = acc_2024_all.mean()\nsd_all_2023 = acc_2023_all.std(ddof=1)\nsd_all_2024 = acc_2024_all.std(ddof=1)\nn1, n2 = len(acc_2023_all), len(acc_2024_all)\npooled_sd_all = np.sqrt(((n1 - 1) * sd_all_2023**2 + (n2 - 1) * sd_all_2024**2) / (n1 + n2 - 2))\nd_all = (mean_all_2024 - mean_all_2023) / pooled_sd_all\nse_d_all = np.sqrt((n1 + n2) / (n1 * n2) + d_all**2 / (2 * (n1 + n2)))\n\nresults.append({\n    \"domain\": \"Overall\",\n    \"n_items\": int(len(item_ids)),\n    \"n_subjects\": int(len(unique_subjects)),\n    \"mean_acc_2023\": round(float(mean_all_2023), 4),\n    \"sd_acc_2023\": round(float(sd_all_2023), 4),\n    \"mean_acc_2024\": round(float(mean_all_2024), 4),\n    \"sd_acc_2024\": round(float(sd_all_2024), 4),\n    \"cohens_d\": round(float(d_all), 4),\n    \"d_ci_lower\": round(float(d_all - 1.96 * se_d_all), 4),\n    \"d_ci_upper\": round(float(d_all + 1.96 * se_d_all), 4),\n})\nprint(f\"\\n  {'Overall':16s}: d={d_all:+.4f} [{d_all - 1.96*se_d_all:.4f}, {d_all + 1.96*se_d_all:.4f}]  \"\n      f\"acc_2023={mean_all_2023:.4f}  acc_2024={mean_all_2024:.4f}\")\n\n# --- Save CSV ---\ndf = pd.DataFrame(results)\ndf.to_csv(OUT / \"domain_profile_results.csv\", index=False)\nprint(f\"\\nSaved: {OUT / 'domain_profile_results.csv'}\")\n\n# --- Profile flatness ---\ndomain_ds = [r[\"cohens_d\"] for r in results if r[\"domain\"] != \"Overall\"]\nd_range = max(domain_ds) - min(domain_ds)\nd_max = max(abs(d) for d in domain_ds)\n\n# --- Per-subject Cohen's d for supplementary detail ---\nsubject_results = []\nfor subj in sorted(unique_subjects):\n    col_mask = item_subjects == subj\n    n_items = col_mask.sum()\n    if n_items < 5:\n        continue\n    acc_2023 = X_2023[:, col_mask].mean(axis=1)\n    acc_2024 = X_2024[:, col_mask].mean(axis=1)\n    m1, m2 = acc_2023.mean(), acc_2024.mean()\n    s1, s2 = acc_2023.std(ddof=1), acc_2024.std(ddof=1)\n    n1, n2 = len(acc_2023), len(acc_2024)\n    ps = np.sqrt(((n1-1)*s1**2 + (n2-1)*s2**2) / (n1+n2-2))\n    d = (m2 - m1) / ps if ps > 0 else 0.0\n    subject_results.append({\n        \"subject\": subj,\n        \"domain\": DOMAIN_MAP[subj],\n        \"n_items\": int(n_items),\n        \"mean_acc_2023\": round(float(m1), 4),\n        \"mean_acc_2024\": round(float(m2), 4),\n        \"cohens_d\": round(float(d), 4),\n    })\n\ndf_subj = pd.DataFrame(subject_results)\ndf_subj.to_csv(OUT / \"subject_profile_results.csv\", index=False)\nprint(f\"Saved: {OUT / 'subject_profile_results.csv'}\")\n\n# --- Generate report ---\nreport_lines = []\nreport_lines.append(\"# R14 MF1: Domain-Level Ability Profile Analysis\\n\")\nreport_lines.append(\"## Purpose\\n\")\nreport_lines.append(\n    \"Quantify whether 2023→2024 cohort ability differences are uniform across MMLU domains \"\n    \"(STEM, Humanities, Social Science, Other). If all domain-level Cohen's d < 0.3 and the \"\n    \"profile is flat, multidimensional ability shifts cannot produce spurious DIF.\\n\"\n)\n\nreport_lines.append(\"## Cohort Sizes\\n\")\nreport_lines.append(f\"- 2023 (Reference): {len(idx_2023)} models\")\nreport_lines.append(f\"- 2024 (Focal): {len(idx_2024)} models\\n\")\n\nreport_lines.append(\"## Domain-Level Results\\n\")\nreport_lines.append(\"| Domain | Items | Subjects | Acc (2023) | Acc (2024) | Cohen's d | 95% CI |\")\nreport_lines.append(\"|--------|------:|:--------:|:----------:|:----------:|:---------:|:------:|\")\nfor r in results:\n    ci = f\"[{r['d_ci_lower']:.3f}, {r['d_ci_upper']:.3f}]\"\n    report_lines.append(\n        f\"| {r['domain']} | {r['n_items']} | {r['n_subjects']} | \"\n        f\"{r['mean_acc_2023']:.3f} | {r['mean_acc_2024']:.3f} | \"\n        f\"{r['cohens_d']:+.3f} | {ci} |\"\n    )\nreport_lines.append(\"\")\n\nreport_lines.append(\"## Profile Flatness\\n\")\nreport_lines.append(f\"- Max |d| across domains: {d_max:.4f}\")\nreport_lines.append(f\"- Range of d across domains: {d_range:.4f}\")\nreport_lines.append(f\"- Overall d: {d_all:.4f}\\n\")\n\nall_below_03 = all(abs(d) < 0.3 for d in domain_ds)\nreport_lines.append(\"## Interpretation\\n\")\nif all_below_03:\n    report_lines.append(\n        f\"All domain-level Cohen's d values fall below the 0.3 threshold \"\n        f\"(max |d| = {d_max:.3f}). The inter-domain range is only {d_range:.3f}, \"\n        f\"indicating a nearly flat ability profile shift. This rules out \"\n        f\"multidimensional ability confounds as a source of spurious DIF: \"\n        f\"the 2024 cohort is uniformly slightly {'stronger' if d_all > 0 else 'weaker'} \"\n        f\"across all domains, rather than differentially strong in specific areas.\"\n    )\nelse:\n    report_lines.append(\n        f\"Some domain-level Cohen's d values exceed 0.3 (max |d| = {d_max:.3f}). \"\n        f\"This suggests non-uniform ability shifts across domains, which could \"\n        f\"contribute to differential item functioning through multidimensional confounds.\"\n    )\n\nreport_lines.append(\"\")\nreport_lines.append(\"## Per-Subject Detail (top 10 largest |d|)\\n\")\ndf_subj_sorted = df_subj.reindex(df_subj[\"cohens_d\"].abs().sort_values(ascending=False).index)\nreport_lines.append(\"| Subject | Domain | Items | d |\")\nreport_lines.append(\"|---------|--------|------:|:---:|\")\nfor _, row in df_subj_sorted.head(10).iterrows():\n    report_lines.append(f\"| {row['subject']} | {row['domain']} | {row['n_items']} | {row['cohens_d']:+.3f} |\")\nreport_lines.append(\"\")\n\nreport = \"\\n\".join(report_lines)\n(OUT / \"domain_profile_analysis.md\").write_text(report)\nprint(f\"Saved: {OUT / 'domain_profile_analysis.md'}\")\nprint(\"\\n--- REPORT ---\")\nprint(report)\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_r14_exp1_domain_profile_20260522T115610",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/scripts/r14_domain_profile.py",
    "content": "\"\"\"R14 MF1: Domain-Level Ability Profile Analysis.\n\nCompares 2023 vs 2024 cohort accuracy across MMLU domains.\nIf all domain-level Cohen's d < 0.3 → profile shift is flat,\nruling out multidimensional spurious DIF as a confound.\n\"\"\"\n\nimport numpy as np\nimport pandas as pd\nfrom scipy import sparse, stats\nfrom pathlib import Path\n\nROOT = Path(__file__).resolve().parent.parent\nOUT = ROOT / \"artifacts\" / \"r14_mf1_domain_profile\"\nOUT.mkdir(parents=True, exist_ok=True)\n\n# --- MMLU Subject → Domain mapping ---\nDOMAIN_MAP = {}\nfor s in [\n    \"abstract_algebra\", \"anatomy\", \"astronomy\", \"college_biology\",\n    \"college_chemistry\", \"college_computer_science\", \"college_mathematics\",\n    \"college_physics\", \"computer_security\", \"conceptual_physics\",\n    \"electrical_engineering\", \"elementary_mathematics\", \"high_school_biology\",\n    \"high_school_chemistry\", \"high_school_computer_science\",\n    \"high_school_mathematics\", \"high_school_physics\", \"high_school_statistics\",\n    \"machine_learning\", \"medical_genetics\", \"virology\",\n]:\n    DOMAIN_MAP[s] = \"STEM\"\n\nfor s in [\n    \"formal_logic\", \"high_school_european_history\", \"high_school_us_history\",\n    \"high_school_world_history\", \"international_law\", \"jurisprudence\",\n    \"logical_fallacies\", \"moral_disputes\", \"moral_scenarios\", \"philosophy\",\n    \"prehistory\", \"world_religions\",\n]:\n    DOMAIN_MAP[s] = \"Humanities\"\n\nfor s in [\n    \"econometrics\", \"high_school_geography\",\n    \"high_school_government_and_politics\", \"high_school_macroeconomics\",\n    \"high_school_microeconomics\", \"high_school_psychology\",\n    \"human_sexuality\", \"professional_psychology\", \"public_relations\",\n    \"security_studies\", \"sociology\", \"us_foreign_policy\",\n]:\n    DOMAIN_MAP[s] = \"Social Science\"\n\nfor s in [\n    \"business_ethics\", \"clinical_knowledge\", \"college_medicine\",\n    \"global_facts\", \"human_aging\", \"management\", \"marketing\",\n    \"miscellaneous\", \"nutrition\", \"professional_accounting\",\n    \"professional_law\", \"professional_medicine\",\n]:\n    DOMAIN_MAP[s] = \"Other\"\n\n# --- Load data ---\nprint(\"Loading response matrix...\")\nX = sparse.load_npz(ROOT / \"artifacts\" / \"response_matrix.npz\")\nidx = np.load(ROOT / \"artifacts\" / \"response_matrix_index.npz\", allow_pickle=True)\nmodel_names = idx[\"model_names\"]\nitem_ids = idx[\"item_ids\"]\n\nmeta = pd.read_csv(ROOT / \"artifacts\" / \"plan_032_dif_cleaned_mmlu\" / \"cleaned_mmlu_analysis.csv\")\n\n# --- Build cohort masks ---\nmodel_to_idx = {name: i for i, name in enumerate(model_names)}\nmeta_2023 = meta[meta[\"cohort_temporal\"] == \"2023\"]\nmeta_2024 = meta[meta[\"cohort_temporal\"] == \"2024\"]\n\nidx_2023 = np.array([model_to_idx[m] for m in meta_2023[\"model_name\"] if m in model_to_idx])\nidx_2024 = np.array([model_to_idx[m] for m in meta_2024[\"model_name\"] if m in model_to_idx])\nprint(f\"Cohort sizes: 2023={len(idx_2023)}, 2024={len(idx_2024)}\")\n\n# --- Parse item subjects and map to domains ---\nitem_subjects = np.array([str(iid).rsplit(\".\", 1)[0] for iid in item_ids])\nunique_subjects = sorted(set(item_subjects))\nprint(f\"Found {len(unique_subjects)} unique subjects\")\n\nunmapped = [s for s in unique_subjects if s not in DOMAIN_MAP]\nif unmapped:\n    print(f\"WARNING: unmapped subjects (assigned to Other): {unmapped}\")\n    for s in unmapped:\n        DOMAIN_MAP[s] = \"Other\"\n\nitem_domains = np.array([DOMAIN_MAP[s] for s in item_subjects])\n\n# --- Convert to dense for cohort subsets (memory ~OK for 1887 × 12508 int8) ---\nprint(\"Extracting cohort submatrices...\")\nX_2023 = X[idx_2023].toarray().astype(np.float32)  # (1080, 12508)\nX_2024 = X[idx_2024].toarray().astype(np.float32)  # (807, 12508)\n\n# --- Per-domain analysis ---\ndomains = [\"STEM\", \"Humanities\", \"Social Science\", \"Other\"]\nresults = []\n\nfor domain in domains:\n    col_mask = item_domains == domain\n    n_items = col_mask.sum()\n    n_subjects = len(set(item_subjects[col_mask]))\n\n    acc_2023 = X_2023[:, col_mask].mean(axis=1)  # per-model accuracy\n    acc_2024 = X_2024[:, col_mask].mean(axis=1)\n\n    mean_2023 = acc_2023.mean()\n    mean_2024 = acc_2024.mean()\n    sd_2023 = acc_2023.std(ddof=1)\n    sd_2024 = acc_2024.std(ddof=1)\n\n    # Pooled SD for Cohen's d\n    n1, n2 = len(acc_2023), len(acc_2024)\n    pooled_sd = np.sqrt(((n1 - 1) * sd_2023**2 + (n2 - 1) * sd_2024**2) / (n1 + n2 - 2))\n    d = (mean_2024 - mean_2023) / pooled_sd if pooled_sd > 0 else 0.0\n\n    # 95% CI for d using standard formula\n    se_d = np.sqrt((n1 + n2) / (n1 * n2) + d**2 / (2 * (n1 + n2)))\n    d_ci_lower = d - 1.96 * se_d\n    d_ci_upper = d + 1.96 * se_d\n\n    results.append({\n        \"domain\": domain,\n        \"n_items\": int(n_items),\n        \"n_subjects\": int(n_subjects),\n        \"mean_acc_2023\": round(float(mean_2023), 4),\n        \"sd_acc_2023\": round(float(sd_2023), 4),\n        \"mean_acc_2024\": round(float(mean_2024), 4),\n        \"sd_acc_2024\": round(float(sd_2024), 4),\n        \"cohens_d\": round(float(d), 4),\n        \"d_ci_lower\": round(float(d_ci_lower), 4),\n        \"d_ci_upper\": round(float(d_ci_upper), 4),\n    })\n    print(f\"  {domain:16s}: d={d:+.4f} [{d_ci_lower:.4f}, {d_ci_upper:.4f}]  \"\n          f\"acc_2023={mean_2023:.4f}  acc_2024={mean_2024:.4f}  n_items={n_items}\")\n\n# --- Overall ---\nacc_2023_all = X_2023.mean(axis=1)\nacc_2024_all = X_2024.mean(axis=1)\nmean_all_2023 = acc_2023_all.mean()\nmean_all_2024 = acc_2024_all.mean()\nsd_all_2023 = acc_2023_all.std(ddof=1)\nsd_all_2024 = acc_2024_all.std(ddof=1)\nn1, n2 = len(acc_2023_all), len(acc_2024_all)\npooled_sd_all = np.sqrt(((n1 - 1) * sd_all_2023**2 + (n2 - 1) * sd_all_2024**2) / (n1 + n2 - 2))\nd_all = (mean_all_2024 - mean_all_2023) / pooled_sd_all\nse_d_all = np.sqrt((n1 + n2) / (n1 * n2) + d_all**2 / (2 * (n1 + n2)))\n\nresults.append({\n    \"domain\": \"Overall\",\n    \"n_items\": int(len(item_ids)),\n    \"n_subjects\": int(len(unique_subjects)),\n    \"mean_acc_2023\": round(float(mean_all_2023), 4),\n    \"sd_acc_2023\": round(float(sd_all_2023), 4),\n    \"mean_acc_2024\": round(float(mean_all_2024), 4),\n    \"sd_acc_2024\": round(float(sd_all_2024), 4),\n    \"cohens_d\": round(float(d_all), 4),\n    \"d_ci_lower\": round(float(d_all - 1.96 * se_d_all), 4),\n    \"d_ci_upper\": round(float(d_all + 1.96 * se_d_all), 4),\n})\nprint(f\"\\n  {'Overall':16s}: d={d_all:+.4f} [{d_all - 1.96*se_d_all:.4f}, {d_all + 1.96*se_d_all:.4f}]  \"\n      f\"acc_2023={mean_all_2023:.4f}  acc_2024={mean_all_2024:.4f}\")\n\n# --- Save CSV ---\ndf = pd.DataFrame(results)\ndf.to_csv(OUT / \"domain_profile_results.csv\", index=False)\nprint(f\"\\nSaved: {OUT / 'domain_profile_results.csv'}\")\n\n# --- Profile flatness ---\ndomain_ds = [r[\"cohens_d\"] for r in results if r[\"domain\"] != \"Overall\"]\nd_range = max(domain_ds) - min(domain_ds)\nd_max = max(abs(d) for d in domain_ds)\n\n# --- Per-subject Cohen's d for supplementary detail ---\nsubject_results = []\nfor subj in sorted(unique_subjects):\n    col_mask = item_subjects == subj\n    n_items = col_mask.sum()\n    if n_items < 5:\n        continue\n    acc_2023 = X_2023[:, col_mask].mean(axis=1)\n    acc_2024 = X_2024[:, col_mask].mean(axis=1)\n    m1, m2 = acc_2023.mean(), acc_2024.mean()\n    s1, s2 = acc_2023.std(ddof=1), acc_2024.std(ddof=1)\n    n1, n2 = len(acc_2023), len(acc_2024)\n    ps = np.sqrt(((n1-1)*s1**2 + (n2-1)*s2**2) / (n1+n2-2))\n    d = (m2 - m1) / ps if ps > 0 else 0.0\n    subject_results.append({\n        \"subject\": subj,\n        \"domain\": DOMAIN_MAP[subj],\n        \"n_items\": int(n_items),\n        \"mean_acc_2023\": round(float(m1), 4),\n        \"mean_acc_2024\": round(float(m2), 4),\n        \"cohens_d\": round(float(d), 4),\n    })\n\ndf_subj = pd.DataFrame(subject_results)\ndf_subj.to_csv(OUT / \"subject_profile_results.csv\", index=False)\nprint(f\"Saved: {OUT / 'subject_profile_results.csv'}\")\n\n# --- Generate report ---\nreport_lines = []\nreport_lines.append(\"# R14 MF1: Domain-Level Ability Profile Analysis\\n\")\nreport_lines.append(\"## Purpose\\n\")\nreport_lines.append(\n    \"Quantify whether 2023→2024 cohort ability differences are uniform across MMLU domains \"\n    \"(STEM, Humanities, Social Science, Other). If all domain-level Cohen's d < 0.3 and the \"\n    \"profile is flat, multidimensional ability shifts cannot produce spurious DIF.\\n\"\n)\n\nreport_lines.append(\"## Cohort Sizes\\n\")\nreport_lines.append(f\"- 2023 (Reference): {len(idx_2023)} models\")\nreport_lines.append(f\"- 2024 (Focal): {len(idx_2024)} models\\n\")\n\nreport_lines.append(\"## Domain-Level Results\\n\")\nreport_lines.append(\"| Domain | Items | Subjects | Acc (2023) | Acc (2024) | Cohen's d | 95% CI |\")\nreport_lines.append(\"|--------|------:|:--------:|:----------:|:----------:|:---------:|:------:|\")\nfor r in results:\n    ci = f\"[{r['d_ci_lower']:.3f}, {r['d_ci_upper']:.3f}]\"\n    report_lines.append(\n        f\"| {r['domain']} | {r['n_items']} | {r['n_subjects']} | \"\n        f\"{r['mean_acc_2023']:.3f} | {r['mean_acc_2024']:.3f} | \"\n        f\"{r['cohens_d']:+.3f} | {ci} |\"\n    )\nreport_lines.append(\"\")\n\nreport_lines.append(\"## Profile Flatness\\n\")\nreport_lines.append(f\"- Max |d| across domains: {d_max:.4f}\")\nreport_lines.append(f\"- Range of d across domains: {d_range:.4f}\")\nreport_lines.append(f\"- Overall d: {d_all:.4f}\\n\")\n\nall_below_03 = all(abs(d) < 0.3 for d in domain_ds)\nreport_lines.append(\"## Interpretation\\n\")\nif all_below_03:\n    report_lines.append(\n        f\"All domain-level Cohen's d values fall below the 0.3 threshold \"\n        f\"(max |d| = {d_max:.3f}). The inter-domain range is only {d_range:.3f}, \"\n        f\"indicating a nearly flat ability profile shift. This rules out \"\n        f\"multidimensional ability confounds as a source of spurious DIF: \"\n        f\"the 2024 cohort is uniformly slightly {'stronger' if d_all > 0 else 'weaker'} \"\n        f\"across all domains, rather than differentially strong in specific areas.\"\n    )\nelse:\n    report_lines.append(\n        f\"Some domain-level Cohen's d values exceed 0.3 (max |d| = {d_max:.3f}). \"\n        f\"This suggests non-uniform ability shifts across domains, which could \"\n        f\"contribute to differential item functioning through multidimensional confounds.\"\n    )\n\nreport_lines.append(\"\")\nreport_lines.append(\"## Per-Subject Detail (top 10 largest |d|)\\n\")\ndf_subj_sorted = df_subj.reindex(df_subj[\"cohens_d\"].abs().sort_values(ascending=False).index)\nreport_lines.append(\"| Subject | Domain | Items | d |\")\nreport_lines.append(\"|---------|--------|------:|:---:|\")\nfor _, row in df_subj_sorted.head(10).iterrows():\n    report_lines.append(f\"| {row['subject']} | {row['domain']} | {row['n_items']} | {row['cohens_d']:+.3f} |\")\nreport_lines.append(\"\")\n\nreport = \"\\n\".join(report_lines)\n(OUT / \"domain_profile_analysis.md\").write_text(report)\nprint(f\"Saved: {OUT / 'domain_profile_analysis.md'}\")\nprint(\"\\n--- REPORT ---\")\nprint(report)\n"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-22T11:58:26.597291+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/scripts/r14_domain_profile.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_r14_exp1_domain_profile_20260522T115610",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-22T11:58:26.597495+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 scripts/r14_domain_profile.py",
  "timeout": "120000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_r14_exp1_domain_profile_20260522T115610",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 scripts/r14_domain_profile.py",
    "timeout": "120000"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-22T11:58:26.598839+00:00_

Loading response matrix...
Cohort sizes: 2023=1080, 2024=807
Found 57 unique subjects
Extracting cohort submatrices...
  STEM            : d=+0.2613 [0.1697, 0.3529]  acc_2023=0.5049  acc_2024=0.5374  n_items=2914
  Humanities      : d=+0.1588 [0.0674, 0.2501]  acc_2023=0.5903  acc_2024=0.6150  n_items=2786
  Social Science  : d=+0.1474 [0.0561, 0.2387]  acc_2023=0.6588  acc_2024=0.6847  n_items=2862
  Other           : d=+0.1465 [0.0551, 0.2378]  acc_2023=0.5754  acc_2024=0.5959  n_items=3946

  Overall         : d=+0.1729 [0.0816, 0.2643]  acc_2023=0.5814  acc_2024=0.6068

Saved: /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r14_mf1_domain_profile/domain_profile_results.csv
Saved: /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r14_mf1_domain_profile/subject_profile_results.csv
Saved: /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r14_mf1_domain_profile/domain_profile_analysis.md

--- REPORT ---
# R14 MF1: Domain-Level Ability Profile Analysis

## Purpose

Quantify whether 2023→2024 cohort ability differences are uniform across MMLU domains (STEM, Humanities, Social Science, Other). If all domain-level Cohen's d < 0.3 and the profile is flat, multidimensional ability shifts cannot produce spurious DIF.

## Cohort Sizes

- 2023 (Reference): 1080 models
- 2024 (Focal): 807 models

## Domain-Level Results

| Domain | Items | Subjects | Acc (2023) | Acc (2024) | Cohen's d | 95% CI |
|--------|------:|:--------:|:----------:|:----------:|:---------:|:------:|
| STEM | 2914 | 21 | 0.505 | 0.537 | +0.261 | [0.170, 0.353] |
| Humanities | 2786 | 12 | 0.590 | 0.615 | +0.159 | [0.067, 0.250] |
| Social Science | 2862 | 12 | 0.659 | 0.685 | +0.147 | [0.056, 0.239] |
| Other | 3946 | 12 | 0.575 | 0.596 | +0.146 | [0.055, 0.238] |
| Overall | 12508 | 57 | 0.581 | 0.607 | +0.173 | [0.082, 0.264] |

## Profile Flatness

- Max |d| across domains: 0.2
…[truncated 1013 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_r14_exp1_domain_profile_20260522T115610",
  "tool": "Bash",
  "elapsed_ms": 1
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-22T11:58:26.599132+00:00_

分析完成。三个文件已写入 `artifacts/r14_mf1_domain_profile/`：

**核心结论**：所有 4 个 domain 的 Cohen's d 均 < 0.3（STEM 最高 d=+0.261，其余三个 ≈ 0.15），domain 间 range 仅 0.115。Overall d=0.173 与预期一致。Profile shift 近乎 flat，排除了多维度能力差异产生 spurious DIF 的可能。

STEM 的 d 略高（0.26 vs ~0.15），主要由 physics/math 类 subject 驱动（college_physics d=0.43, high_school_mathematics d=0.42），但即使 STEM 也未超过 0.3 阈值。

产出文件：
- `domain_profile_results.csv` — 逐 domain 统计表
- `subject_profile_results.csv` — 逐 subject 的 Cohen's d
- `domain_profile_analysis.md` — 完整报告

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_code_r14_exp1_domain_profile_20260522T115610"
}
```

</details>

---
