# Paper Data Tables & Figure Specs — EMNLP 2026 Short Paper

> **Status**: FINAL for plan-012-full (11 tasks / 245 episodes from plan_c).
> Router SFT (plan-002-formal-v4) RUNNING — Table 2 placeholder.
> Generated: 2026-05-14.

---

## Table 1: Death Decomposition Summary (plan-012-full)

### 1A. Aggregate Metrics

| Metric | Value | Source |
|--------|:-----:|--------|
| Δ_full (det − internal) | **+29.60** | plan-012-full |
| Δ_nd (non-death only) | **+2.84** | plan-012-full |
| Death Avoidance Fraction | **90.41%** | plan-012-full |
| Pearson *r* (death rate diff vs Δ_full) | **0.9698** | plan-012-full |
| *p*-value | **8.12×10⁻⁷** | plan-012-full |
| Internal death rate | 42.9% | plan-012-full |
| Deterministic death rate | 16.3% | plan-012-full |
| Tasks | 11 | plan-012-full |
| Episodes | 245 | plan-012-full |

### 1B. Episode-level Label Distribution

| Label | Count | % |
|-------|:-----:|:---:|
| det-preferred | 86 | 35.1% |
| internal-preferred | 9 | 3.7% |
| no-preference | 150 | 61.2% |
| **Total** | **245** | 100% |

### 1C. Per-Task Breakdown

| Task | n | DR_int | DR_det | Δ_full | Δ_nd | Death% | D / I / N |
|------|:-:|:------:|:------:|:------:|:----:|:------:|:---------:|
| find-non-living-thing | 40 | 0.00 | 0.00 | +9.58 | +9.58 | 0.0% | — |
| grow-fruit | 20 | 0.45 | 0.20 | +25.10 | −0.64† | 102.5%† | 6/1/13 |
| inclined-plane-determine-angle | 20 | 0.55 | 0.20 | +36.00 | +1.25† | 96.5%† | 7/0/13 |
| identify-life-stages-2 | 20 | 0.50 | 0.20 | +30.00 | −1.20† | 104.0%† | 6/0/14 |
| measure-melting-point | 20 | 0.55 | 0.25 | +30.05 | +0.05 | 99.8% | — |
| find-animal | 20 | — | — | — | — | — | — |
| identify-life-stages-1 | 20 | — | — | — | — | — | — |
| freeze | 20 | — | — | — | — | — | — |
| chemistry-mix | 20 | — | — | — | — | — | — |
| lifespan-longest-lived | 20+ | — | — | — | — | — | — |
| lifespan-longest-lived-then-shortest | 20 | — | — | — | — | — | — |
| **Aggregate (11 tasks)** | **245** | **0.429** | **0.163** | **+29.60** | **+2.84** | **90.41%** | **86/9/150** |

†Δ_nd computed from alive_mean scores in plan-001b-gpu1 collection data. Death% > 100% when internal is marginally better on non-death episodes (Δ_nd < 0), meaning death avoidance MORE than explains the full gap. These are approximate — final values in `results/plan_012_decomposition/` on server.

**6 tasks with "—"**: Per-task decomposition data exists on server (`results/plan_012_decomposition/`, `results/plan_c/`) but is not in the registry. **ACTION: extract from `results/death_decomposition_report.json` on westb-13313 to fill this table.**

### 1D. Key Observations for Paper

- **find-non-living-thing**: Only zero-death task (n=40). Δ_full=+9.58 is ENTIRELY from non-death performance difference (Δ_nd=+9.58). Critical counter-example: deterministic computation provides genuine task advantage even without death risk.
- **10/11 death-prone tasks**: Death dominates (fraction ≥ 90%). Non-death score deltas are small and sometimes negative (internal marginally better when both survive).
- **Pearson r=0.9698**: Near-perfect linear relationship between per-task death rate difference and Δ_full across 11 task types.

---

## Table 2: Router SFT Results

### 2A. plan-004-ablation-b (Implicit Router — DONE)

Qwen3-1.7B + LoRA r=16, implicit [SIMULATE] token routing. 3 epochs, class_weights auto.

| Metric | Value |
|--------|:-----:|
| Accuracy | 0.6536 |
| Balanced Accuracy | 0.5927 |
| F1 (macro) | 0.5091 |

| Class | Precision | Recall | F1 | Support |
|-------|:---------:|:------:|:--:|:-------:|
| deterministic | 0.9196 | 0.6703 | 0.7754 | 273 |
| internal | 0.1589 | 0.5152 | 0.2429 | 33 |

**Confusion Matrix** (val set, n=306):

|  | Pred: int | Pred: det |
|--|:---------:|:---------:|
| True: int | 17 | 16 |
| True: det | 90 | 183 |

**Source**: plan-004-ablation-b registry metrics.

**Notes**: First non-degenerate model (internal recall=51.5% > 0). But internal precision=15.9% extremely low — 90 false positives vs 17 true positives. Accuracy dropped from 92.3% majority-class baseline to 65.4%. Qwen3 `<think>` tag interference noted.

### 2B. plan-002-formal-v4 (Explicit Router — ⏳ PENDING RESULTS)

> **Status**: RUNNING as of 2026-05-14T06:23. Awaiting completion.

Config: Qwen3-1.7B + LoRA r=16 (0.37% trainable), 3 epochs, batch_size=4 + grad_accum=8, class_weights auto [4.50, 0.5625], lr=2e-5.
Data: 2040 samples (train 1620: det=1440/int=180 | val 420: det=390/int=30).
Fixes from v3: (1) stratified val split, (2) removed upsample_minority, (3) mutual exclusion check.

**Metrics to report when done**:
- accuracy, balanced_accuracy, F1_macro
- Per-class: precision, recall, F1 for deterministic and internal
- Confusion matrix
- Per-task accuracy breakdown (11 tasks)
- Comparison vs plan-004-ablation-b (explicit vs implicit routing)

### 2C. plan-002-dryrun (1-epoch baseline — degenerate)

| Metric | Value | Note |
|--------|:-----:|------|
| Accuracy | 0.923 | = majority-class rate |
| Balanced Accuracy | 0.500 | random for minority |
| F1 (macro) | 0.480 | |
| Internal recall | 0.000 | DEGENERATE: all pred→det |

**Source**: plan-002-dryrun. 1 epoch insufficient for convergence (loss still dropping 0.63→0.48). Included as reference point only.

---

## Table 3: Baseline Comparisons

### 3A. Keyword Routing (plan-011) — All Degenerate

| Version | Keywords | Match Rate | Effective Behavior | Episode Acc. |
|---------|:--------:|:----------:|:------------------:|:------------:|
| v1 (generic, incl. *connect*) | 20 | 85.8% | ≈ always-det | ~97%* |
| v2 (science-only) | 17 | 4.9% | ≈ always-internal | ~1.2% |
| v3 (state-change verbs) | 12 | 2.8% | ≈ always-internal | 1.5% |

*v1 accuracy is inflated: 86% match rate → routes nearly everything to det, which happens to match the dominant label.

**Structural failure**: ScienceWorld uses generic interaction verbs (*connect*, *move*, *pick up*), not science keywords. No static keyword set provides meaningful routing.

**Source**: plan-011-rule-based registry metrics.

### 3B. Fixed-Strategy Baselines

| Strategy | Description | Death Rate | Relative to Oracle |
|----------|-------------|:----------:|:------------------:|
| Always-deterministic | Every step uses simulation | 16.3% | Strong baseline; Δ_full shows +29.6 advantage over internal |
| Always-internal | Every step uses LLM reasoning | 42.9% | Worst; 2.6× death rate vs deterministic |
| Oracle (episode-level) | Best of (det, int) per episode | — | Upper bound; = always-det for 86/245 det-pref episodes |

**Note**: Absolute mean scores (int_mean, det_mean, oracle_mean) for plan_c 11 tasks are on server in `results/plan_012_decomposition/`. The old 30-task preliminary values were: always-internal ≈ −47.5, always-deterministic ≈ −9.2. **ACTION: extract updated 11-task absolute scores from server.**

### 3C. Published External Baselines (from papers, not our experiments)

| Method | ScienceWorld Score | Source |
|--------|:-----------------:|--------|
| CogRouter (CoPO + routing) | 84.6 | Published paper |
| ITP-R (LLM world model routing) | 62.58 | Published paper |

**Note**: Not directly comparable — different agent architectures, different scoring protocols. Cited for context only.

---

## Table 4: Figure Specifications

### Fig 1: Death Rate vs Δ(D−I) Scatter Plot

- **Type**: Scatter plot with linear regression line
- **X-axis**: Per-task death rate difference (DR_int − DR_det)
- **Y-axis**: Δ_full (det_mean − int_mean) per task
- **Points**: 11 task types, each labeled
- **Key annotation**: r=0.9698, p=8.12×10⁻⁷
- **Highlight**: find-non-living-thing at (0, +9.58) — off the trend line, zero death difference but positive Δ
- **Data source**: plan-012-full per-task metrics. Per-task DR and Δ_full from `results/plan_012_decomposition/` on server.
- **Size**: Single column (short paper)
- **Color**: Two tones — death-prone tasks (filled circles) vs zero-death task (open circle/star)

### Fig 2: Label Distribution Bar Chart

- **Type**: Stacked or grouped bar chart, one bar per task
- **Y-axis**: Episode count
- **Colors/segments**: det-preferred (blue), internal-preferred (red), no-preference (gray)
- **Task order**: Sort by Δ_full descending (most det-favored first)
- **Key annotation**: Aggregate: 86D / 9I / 150N out of 245 episodes
- **Data source**: plan-012-full label_dist + per-task labels from `results/plan_c/*/episodes.jsonl`
- **Alternative**: If space is tight, merge into Table 1C and drop this figure. Per-task labels for 5/11 tasks available in registry (see Table 1C); remaining 6 on server.

### Fig 3: Router Confusion Matrix Heatmap

- **Type**: 2×2 heatmap with counts
- **Classes**: deterministic, internal
- **Data source**: plan-002-formal-v4 (pending) confusion matrix. Currently available: plan-004-ablation-b confusion (17/16/90/183).
- **Key annotation**: Overall accuracy, balanced accuracy, class-specific recall
- **Note**: If plan-002-v4 produces a non-degenerate model, use that. Otherwise use plan-004-ablation-b. If both are near-degenerate, the confusion matrix itself IS the finding (router ≈ always-det).

### Figure Priority for 4-page Short Paper

1. **Fig 1 (scatter plot)**: MUST INCLUDE — this is the headline visual for C1 (r=0.9698)
2. **Fig 2 (label dist)**: NICE TO HAVE — can be folded into a table
3. **Fig 3 (confusion matrix)**: CONDITIONAL — include only if router learns non-trivial routing

---

## Section 5: Paper Framing Consistency Check

Cross-checking all quantitative claims in `paper_framing.md` against registry data.

### Consistent Claims

| Claim in paper_framing.md | Registry Value | Source |
|--------------------------|:--------------:|--------|
| Δ_full=+29.60 | 29.6 | plan-012-full |
| Δ_no_death=+2.84 | 2.84 | plan-012-full |
| death fraction=90.41% | 0.9041 | plan-012-full |
| Pearson r=0.9698 | 0.9698 | plan-012-full |
| p=8.12e-07 | 8.12e-07 | plan-012-full |
| 11 task types / 245 episodes | tasks=11, episodes=245 | plan-012-full |
| det-preferred 86 / internal-preferred 9 / no-preference 150 | 86/9/150 | plan-012-full label_dist |
| find-non-living-thing: n=40, zero deaths, Δ=+9.58 | matches | plan-012-decomp key_tasks |
| death_rate_int=0.429, death_rate_det=0.163 | matches | plan-012-full |
| plan-004-ablation-b: accuracy=0.6536, balanced_acc=0.5927, internal recall=0.5152 | matches | plan-004-ablation-b metrics |
| keyword v1 match_rate=85.8%, v2=4.9% | 85.8%, 4.9% | plan-011 |

### Unverified / Needs Source

| Claim | Issue | Action |
|-------|-------|--------|
| **"98.2% tie rate"** (per-step oracle labeling) | No source experiment in registry. Not in plan-012, plan-011, or any registered experiment. Likely from early analysis or manual calculation. | **MUST find source or re-derive from data before citing in paper.** Check `results/` on server for per-step labeling scripts/outputs. |

### Claims from External Papers (not our data)

| Claim | Note |
|-------|------|
| ITP-R 62.58 vs CogRouter 84.6 on ScienceWorld | From published papers. Verify exact numbers against original publications before citing. |

### Stale Numbers (superseded — DO NOT USE)

The following numbers appear in older artifacts (`experiment_tables.md`) and should NOT be used:

| Old Value | Current Value | Note |
|-----------|:------------:|------|
| Δ_full=+38.33 (30 tasks) | +29.60 (11 tasks) | Prescreening data superseded by plan_c |
| DAF=98.8% (30 tasks) | 90.41% (11 tasks) | Lower because plan_c includes find-non-living-thing (40 eps, 0 death) |
| r=0.986 (30 tasks) | 0.9698 (11 tasks) | Still very high but slightly lower |
| Labels: 102/1/146 (249 eps) | 86/9/150 (245 eps) | Plan_c has more internal-preferred episodes |
| death_rate_int=49% | 42.9% | |
| death_rate_det=11.7% | 16.3% | |

---

## Data Gaps & Action Items

| # | Gap | Action | Priority |
|---|-----|--------|----------|
| 1 | Per-task decomposition for 6/11 tasks missing from registry | Extract from `results/plan_012_decomposition/` or `results/plan_c/` on westb-13313 | HIGH |
| 2 | Absolute mean scores (int_mean, det_mean) per task for plan_c 11 tasks | Extract from server; needed for Table 3B and Fig 1 | HIGH |
| 3 | "98.2% tie rate" claim has no registered source | Find source or re-derive | HIGH |
| 4 | plan-002-formal-v4 results pending | Wait for training completion, then fill Table 2B | BLOCKING |
| 5 | Per-task label distribution for 6/11 tasks | Extract from `results/plan_c/*/episodes.jsonl` | MEDIUM (needed for Fig 2) |
| 6 | Oracle baseline score for 11-task data | Compute from plan_c episode data | MEDIUM |
| 7 | Bootstrap CIs for 11-task decomposition | Run bootstrap on plan_c data | LOW (had CIs for 30-task) |

---

## Data Provenance

| Experiment | Status | Episodes | Role in Paper |
|-----------|:------:|:--------:|---------------|
| plan-012-full | DONE | 245 | **Primary**: Table 1 aggregates, C1 claim |
| plan-012-decomposition | DONE | 245+249 | Per-task breakdown, prescreening robustness check |
| plan-001b (all sub-runs) | DONE | 245 | Data collection underlying plan-012 |
| plan-011-rule-based | DONE | 204 | Table 3A keyword baselines |
| plan-004-ablation-b | DONE | — | Table 2A implicit router |
| plan-002-formal-v4 | RUNNING | — | Table 2B explicit router (pending) |
| plan-002-dryrun | DONE | — | Table 2C 1-epoch degenerate reference |
| plan-005 (taxonomy) | DONE | 314 | Supplementary task categorization |
