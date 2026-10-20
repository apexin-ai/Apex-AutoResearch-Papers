# Experiment Tables for EMNLP 2026 Short Paper

> **Status**: Preliminary (pre-analysis: prescreening 5 ep/task + MVP 20 ep/task, N=249 episodes).
> Plan-001b full data collection in progress; numbers will be updated upon completion.

---

## Table 1: Death Decomposition Analysis (plan-012)

Core result: deterministic simulation advantage is almost entirely explained by death avoidance.

| Metric | Episode-weighted | Task-weighted† |
|--------|:---------------:|:-------------:|
| Δ_full (det − internal) | **+38.33** | **+41.48** |
| Δ_nd (non-death episodes only) | +0.48 | +0.91 |
| DAF (death avoidance fraction) | 98.8% | 93.9% |
| DAF 95% CI (bootstrap) | [93.9%, 104.5%] | [84.6%, 99.8%] |
| Pearson *r* (Δ_death_rate vs Δ_full) | 0.986 | — |
| *p*-value | <0.0001 | — |
| Δ_penalty_removed | +0.98 | — |
| Internal death rate | 49.0% | — |
| Deterministic death rate | 11.7% | — |
| Tasks / Episodes | 30 / 249 | 30 / 249 |

**Data source**: `results/death_decomposition_report.json` (plan-012, 2026-05-14).
Episode-weighted = aggregate means across all episodes; Task-weighted† = mean of per-task metrics (from registry, pending re-verification).

### Signal Source Decomposition (episode-level)

| Signal Source | Count | % of Episodes |
|--------------|:-----:|:------------:|
| death_asymmetry | 93 | 37.3% |
| tied_alive (no-preference) | 117 | 47.0% |
| both_dead (no-preference) | 29 | 11.6% |
| score_comparison | 10 | 4.0% |

**Interpretation**: 93/102 det-preferred labels (91.2%) come from death asymmetry; only 9 (8.8%) from genuine score differences.

---

## Table 2: Keyword Routing Baseline (plan-011)

All keyword heuristics degenerate — none provides meaningful routing signal.

| Version | Keywords | N | Match Rate | Routing Acc.† | Effective Behavior |
|---------|:--------:|:---:|:----------:|:------------:|-------------------|
| v1 (generic) | 20 (incl. *connect*) | 204 | 86.1% | 97.6% | ≈ always-det |
| v2 (science) | 17 | 203 | 4.9% | 1.2% | ≈ always-internal |
| v3 (state-change) | 12 | ~233 | 2.8% | 1.5% | ≈ always-internal |

**v1 keywords**: heat, cool, boil, melt, freeze, burn, mix, pour, react, dissolve, combine, activate, deactivate, turn on, turn off, **connect**, disconnect, change state, phase change, temperature
**v2 keywords**: heat, cool, boil, melt, freeze, burn, mix, pour, react, dissolve, activate, change state, ignite, combust, evaporate, condense, oxidize
**v3 keywords**: heat, cool, boil, melt, freeze, burn, mix, pour, react, dissolve, activate, change-state

†Routing accuracy = fraction of scorable episodes where keyword routing matches oracle label. v1 gets high accuracy only because match_rate≈86% routes everything to det, which happens to match the dominant label.

**Structural failure**: ScienceWorld actions use generic interaction verbs (*connect*, *move*, *pick up*), not science-specific keywords. Removing *connect* alone drops match rate from 86% to 5%. No static keyword set captures the task-relevant routing signal.

**Data source**: `results/rule_based_accuracy_v1_rerun.json`, `rule_based_accuracy_v2_test.json`, registry plan-011 (v3). Episodes vary slightly due to race condition in concurrent evaluation (see registry notes).

---

## Table 3: Label Distribution (episode-level, N=249)

| Label | Count | Percentage |
|-------|:-----:|:----------:|
| det-preferred | 102 | 41.0% |
| internal-preferred | 1 | 0.4% |
| no-preference | 146 | 58.6% |

**Data source**: `results/death_decomposition_report.json` aggregate.label_distribution.

### Task-level Signal Category (plan-005, N=314 episodes, 30 tasks)

| Category | Tasks | % Tasks | Episodes | % Episodes |
|----------|:-----:|:-------:|:--------:|:----------:|
| Death-dominated (DAF ≥ 95%) | 25 | 83.3% | 250 | 79.6% |
| Genuine-det (DAF < 95%, Δ > 0) | 3 | 10.0% | 19 | 6.1% |
| Internal-preferred (Δ ≤ 0) | 2 | 6.7% | 45 | 14.3% |

**Data source**: `results/plan005/analysis/taxonomy_summary.json` (includes partial plan-001b data).

---

## Table 4: Baseline Comparison (episode-weighted mean scores)

| Method | Mean Score | Notes |
|--------|:---------:|-------|
| always-internal | −47.5 | LLM internal reasoning only; 49% death rate |
| always-deterministic | −9.2 | Deterministic simulation only; 11.7% death rate |
| keyword-v1 (generic) | ≈ always-det | Degenerates: 86% match rate → routes everything to det |
| keyword-v2 (science) | ≈ always-internal | Degenerates: 5% match rate → routes everything to internal |
| keyword-v3 (state-change) | ≈ always-internal | Degenerates: 3% match rate → routes everything to internal |
| oracle (episode-level) | *pending* | Upper bound; requires plan-001b full data |

**Data source**: Episode-weighted means from `results/death_decomposition_report.json`.

---

## Data Provenance Summary

| Source | File / Key | Episodes | Status |
|--------|-----------|:--------:|--------|
| plan-012 decomposition | `death_decomposition_report.json` | 249 | **DONE** (preliminary) |
| plan-011 keyword baseline | `rule_based_accuracy_*.json` | 204 | **DONE** |
| plan-005 taxonomy | `plan005/analysis/taxonomy_summary.json` | 314 | **DONE** (includes partial plan-001b) |
| plan-001b full collection | `plan_c/` (in progress) | — | **RUNNING** |

### Update plan
When plan-001b completes (~40 tasks × 20 ep/task = 800+ episodes):
1. Re-run decomposition analysis → update Table 1
2. Re-compute label distribution → update Table 3
3. Compute oracle baseline score → fill Table 4 oracle row
4. Remove "preliminary" status
