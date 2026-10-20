# analysis c8 s025 extract

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_c8_s025_extract_20260516T144010_result.json`
- **Structured JSON:** [`0e2c57ec7477f2b50a07.json`](../../sessions/0e/0e2c57ec7477f2b50a07.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

无 warnings。数据完整。以下是完整指标汇总：

---

## c8_llama_importance_s025 (n=250) 关键指标

### 配置
| 参数 | 值 |
|------|-----|
| Model | DeepSeek-R1-Distill-Llama-8B |
| Sparsity | 0.25 |
| Masking | importance (attn_frobenius + cumulative_attn) |
| Segmentation | quantile |
| n_problems | 250 |
| n_bootstrap | 1000 |

### Per-Phase II

| Phase | n | Mean | Median | Median 95% CI |
|-------|---|------|--------|---------------|
| high | 244 | 0.0218 | 0.0171 | [0.0172, 0.0207] |
| mid | 217 | 0.2126 | 0.1916 | [0.1760, 0.2063] |
| low | 250 | 0.4713 | 0.3880 | [0.3953, 0.4484] |

### Phase Gradient (low − high)

| 指标 | 值 |
|------|-----|
| n_paired | 244 |
| mean_diff | 0.4474 |
| **median_diff** | **0.3761** |
| median_diff 95% CI | [0.3147, 0.4039] |
| **Wilcoxon p (one-sided)** | **4.30e-39** |
| **Bonferroni p (k=4)** | **1.72e-38 ✓ significant** |
| **Cohen's d_z** | **1.1174** |
| Rank-biserial r | 0.8689 (228 pos / 16 neg) |

### 与 Baselines 对比

| 指标 | DS-R1-7B s025 (n=50) | LLaMA s025 (n=50, c3) | **LLaMA s025 (n=250, c8)** |
|------|----------------------|------------------------|----------------------------|
| high median | 0.032 | — | 0.0171 |
| mid median | 1.118 | — | 0.1916 |
| low median | 7.196 | — | 0.3880 |
| median_diff | 7.1636 | 0.0947 | **0.3761** |
| Wilcoxon p | — | 0.0209 | **4.30e-39** |
| Bonferroni p | — | 0.0834 (NS) | **1.72e-38** |
| Cohen's d_z | — | 1.1227 | **1.1174** |

### 关键判断

1. **统计显著性**：n=250 下 LLaMA s025 **极其显著** (Bonferroni p = 1.72e-38)，彻底解决了 n=50 时 Bonferroni 不显著的问题。

2. **效应量稳定**：d_z = 1.1174 与 n=50 时的 1.1227 几乎一致，说明 n=50 的效应量估计是可靠的，只是样本不足导致 p 值不够小。

3. **与 DS 的差异**：LLaMA median_diff (0.376) 仅为 DS (7.164) 的 **5.3%**。方向一致（low > high）但幅度差 ~19x。这意味着 phase-gated sparsity 效应在 LLaMA 上存在但远弱于 DS-R1-7B。

4. **n=250 vs n=50 的提升**：median_diff 从 0.0947 增加到 0.3761 (3.97x)——这主要反映了 n=50 时估计不稳定，n=250 的估计更可靠。

---
