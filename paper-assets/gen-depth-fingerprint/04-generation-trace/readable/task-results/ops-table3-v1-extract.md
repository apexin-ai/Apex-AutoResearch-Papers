# ops table3 v1 extract

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_table3-v1-extract_20260516T190133_result.json`
- **Structured JSON:** [`a73e6c3401d59ddcce7f.json`](../../sessions/a7/a73e6c3401d59ddcce7f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data collected. Here's the complete report:

---

## === Table 3 (Baselines) — `8gen_table3_unified.json` ===

Binary task (gen1 vs gen2+), pooled LOGO 8-fold:

| Method | Features | Hyperparams | Binary F1 | 95% CI |
|--------|----------|-------------|-----------|--------|
| ld_score | `[ld_score]` | n_est=100, max_depth=3 | **0.4909** | [0.4852, 0.4973] |
| entropy_mean | `[entropy_mean]` | n_est=100, max_depth=3 | **0.6680** | [0.6620, 0.6742] |
| 4det_surface | `[ld_score, entropy_mean, hapax_ratio, ttr]` | n_est=200, max_depth=6 | **0.6857** | [0.6798, 0.6918] |
| 7feature | `[entropy_mean, entropy_std, entropy_max, entropy_min, ttr, hapax_ratio, tail_decay]` | n_est=200, max_depth=6 | **0.6911** | [0.6853, 0.6972] |

Note: The method previously called "3det_surface" is actually **4det_surface** (ld_score + entropy_mean + hapax_ratio + ttr = 4 features, 2 "detector" + 2 surface).

---

## === Table 1 (Per-generator, 7-feature) — `8gen_logo_unfiltered.json` ===

Protocol: 7-feature XGB (n_est=200, max_depth=6), LOGO.

| Generator | 3-class F1 | Binary F1 | Binary 95% CI |
|-----------|-----------|-----------|---------------|
| pythia-1b | 0.8064 | 0.7175 | [0.6998, 0.7350] |
| pythia-2.8b | 0.7983 | 0.7243 | [0.7068, 0.7417] |
| olmo-2-1b | 0.7810 | 0.6954 | [0.6788, 0.7114] |
| qwen3-0.6b | 0.7795 | 0.6911 | [0.6733, 0.7086] |
| qwen3-1.7b | 0.7717 | 0.7093 | [0.6925, 0.7259] |
| qwen3-8b | 0.7143 | 0.6918 | [0.6738, 0.7077] |
| **llama-3.2-3b** | 0.7753 | 0.6968 | [0.6798, 0.7129] |
| **mistral-7b-v0.3** | 0.6815 | 0.6327 | [0.6172, 0.6482] |

Pooled: 3-class F1 = 0.762 [0.7577, 0.7664], Binary F1 = 0.6944 [0.6883, 0.7004]

---

## === LD-Score 状态 ===

**LD-Score (trigram repetition ratio)** 在 v1 unified 评估中有完整结果：
- Binary F1 = **0.4909** (Table 3, hyperparams: n_est=100, max_depth=3)
- 在 `8gen_logo_baselines.json` 中的 LOGO 结果：binary F1 = **0.6574** [0.6718, 0.6837]（注意：这个文件用了不同 seed=789, 而 table3_unified 用 seed=42）

`8gen_baselines.json`（pooled LOGO, 可能是另一脚本）：
- pooled binary F1 = **0.6788** [0.6717, 0.6851]

差异来源：`8gen_table3_unified.json` 的 LD-Score=0.4909 用的是 seed=42 + n_est=100/max_depth=3；`8gen_baselines.json` 和 `8gen_logo_baselines.json` 用的是不同 random seed (789) 和/或不同样本池。

---

## === 8gen_logo_baselines.json 完整对比 (seed=789) ===

| Method | 3-class F1 | Binary F1 | Binary CI |
|--------|-----------|-----------|-----------|
| avg_logprob | 0.6834 | 0.6405 | [0.6716, 0.6829] |
| fastdetectgpt | 0.6552 | 0.5642 | [0.5728, 0.5849] |
| binoculars | 0.3950 | 0.5196 | [0.5317, 0.5432] |
| ld_score | 0.6189 | 0.6574 | [0.6718, 0.6837] |
| 4det_ensemble | 0.7696 | 0.6860 | [0.6934, 0.7048] |
| 4det_surface | 0.7873 | 0.6986 | [0.7036, 0.7146] |
| 7feature_ours | 0.7401 | 0.6614 | [0.6867, 0.6983] |

Config: baselines use n_est=100/max_depth=3, ensembles use n_est=200/max_depth=6, logo_seed=789, bootstrap_n=1000.

---

## === 缺失项 ===

1. **v1 table3_unified 没有 avg_logprob / fastdetectgpt / binoculars 单特征结果**（只有 ld_score 和 entropy_mean 作为单特征）。这些在 `8gen_logo_baselines.json` 里有，但 seed 不同 (789 vs 42)。
2. **v1 table3_unified 没有 4det_ensemble**（只有 4det_surface）。`8gen_logo_baselines.json` 有。
3. **LD-Score 数字不一致**：table3_unified 报 0.4909（seed=42），logo_baselines 报 0.6574（seed=789）。差异巨大，可能是 binary label 定义差异或 LD-Score 计算方式不同（table3 用 trigram ratio 自定义函数，baselines 可能用不同实现）。
4. **`8gen_logo_unfiltered.json` 没有记录用的 seed 和超参**，但从 per-gen CI 宽度推测是同 LOGO protocol。
5. **Per-generator CI 在 `8gen_logo_unfiltered.json` 中是 3-class 和 binary 各自的 per-gen F1 + CI**，格式完整。但 **baselines 的 per-gen 没有 CI**（只有点估计）。

---
