# ops extract p0 paper data

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_extract-p0-paper-data_20260516T131044_result.json`
- **Structured JSON:** [`bf214422cae206c0f36c.json`](../../sessions/bf/bf214422cae206c0f36c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## P0 数据提取报告

---

### 1. Sample Count N

**8-gen LOGO (unfiltered) — `8gen_logo_unfiltered.json`:**
| Task | N |
|------|---|
| 3-class (gen-0/gen-1/gen-2+) | 37,058 |
| binary (gen-0 vs gen-1+) | 29,095 |

8 generators: llama-3.2-3b, mistral-7b-v0.3, olmo-2-1b, pythia-1b, pythia-2.8b, qwen3-0.6b, qwen3-1.7b, qwen3-8b

**6-gen dataset_stats.json per-generator totals (depth 0–4):**
| Generator | N |
|-----------|---|
| pythia-1b | 4,555 |
| pythia-2.8b | 4,609 |
| olmo-2-1b | 4,713 |
| qwen3-0.6b | 4,538 |
| qwen3-1.7b | 4,617 |
| qwen3-8b | 4,497 |
| **6-gen total** | **27,529** |

**New generators (features_pythia410m.jsonl):**
- llama-3.2-3b: 4,680 lines
- mistral-7b-v0.3: 4,849 lines

**(a)** 存在且可直接用。**(b)** 8-gen scope (LOGO 结果)；6-gen scope (dataset_stats)。

---

### 2. LOFO — Leave-One-Family-Out

**Family-level holdout (`family_holdout_3class.json`) — 6-gen scope:**

| Held-out Family | Macro F1 | Per-generator |
|-----------------|----------|---------------|
| Pythia | 0.7717 | pythia-1b: 0.7932, pythia-2.8b: 0.7506 |
| OLMo | 0.7616 | olmo-2-1b: 0.7616 |
| Qwen | 0.7544 | qwen3-0.6b: 0.8033, qwen3-1.7b: 0.7885, qwen3-8b: 0.6730 |

**Feature-level LOFO (`lofo_ablation_results.json`) — 6-gen scope:**
- Full baseline F1: 0.7904
- Most impactful feature dropped: `entropy_max` (Δ = −0.015)
- Least impactful: `entropy_min` (Δ ≈ 0)

**(a)** 存在且可用。**(b)** 仅 6-gen scope（不含 llama-3.2-3b、mistral-7b-v0.3）。**(c)** 数值如上。没有 8-gen family holdout（新增的 llama 和 mistral 各自独立成 family，需要重跑才能得到 5-family LOFO）。

---

### 3. Baselines

**`review_p1d_6gen_baselines.json` — 6-gen scope, 3-class LOGO:**

| Method | F1 | 95% CI |
|--------|-----|--------|
| Avg-LogProb | 0.7368 | [0.7318, 0.7419] |
| FastDetectGPT | 0.6883 | [0.6833, 0.6931] |
| LD-Score | 0.6546 | [0.6489, 0.6602] |
| Binoculars | 0.4164 | [0.4106, 0.4217] |

**Ensemble (`review_baseline_ensemble_results.json`) — 6-gen scope:**

| Feature Set | F1 | 95% CI |
|-------------|-----|--------|
| 4-baseline ensemble | 0.7964 | [0.7921, 0.8007] |
| 4-baseline + surface (ttr, hapax) | 0.8049 | [0.8003, 0.8092] |
| 7-feature (ours, no baselines) | 0.7887 | [0.7839, 0.793] |

**(a)** 存在且可用。**(b)** 仅 6-gen scope。**(c)** 数值如上。8-gen LOGO 主结果（F1=0.762）用的是 our features，但 baselines 没有 8-gen 版本。

---

### 4. Feature Ablation (surface-only / reference-only)

**`ablation_results.json` — 6-gen scope, 10-fold CV, N=2,967:**

| Feature Group | Macro F1 | Std |
|---------------|----------|-----|
| Full (all 7 features) | 0.8202 | 0.0102 |
| Surface-only (ttr, hapax) | 0.7611 | 0.0184 |
| Reference-only (entropy×4, tail_decay) | 0.7162 | 0.0174 |

**Bootstrap pairwise comparisons (all Bonferroni-significant, p=0.0):**
- Full vs reference-only: Δ = +0.104 [0.091, 0.118]
- Full vs surface-only: Δ = +0.059 [0.053, 0.065]
- Surface vs reference: Δ = +0.045 [0.027, 0.063]

**(a)** 存在且可用。**(b)** 6-gen scope only。**(c)** 数值如上。

---

### 总结：需 Director 决策

| 数据项 | 8-gen 版本? | 备注 |
|--------|-------------|------|
| LOGO 主结果 | ✅ 有 | F1=0.762 (3-class), 0.694 (binary) |
| Family holdout | ❌ 仅 6-gen | 新增 llama/mistral 需重跑 |
| Baselines | ❌ 仅 6-gen | 需在 8-gen 数据上重跑 4 个 baseline |
| Feature ablation | ❌ 仅 6-gen | 需在 8-gen 数据上重跑 |
| Feature LOFO | ❌ 仅 6-gen | 同上 |

---
