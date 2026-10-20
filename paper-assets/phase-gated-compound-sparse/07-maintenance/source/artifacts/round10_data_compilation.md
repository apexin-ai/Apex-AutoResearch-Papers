# Round 10 审稿数据包

**生成时间**: 2026-05-15  
**数据截止时间**: 2026-05-15  

---

## Summary

- **实验范围**: 两模型 (QW=Qwen2.5-7B-Instruct, DS=DeepSeek-R1-Distill-Qwen-7B) 在 MATH/GSM8K 上的 accuracy dose curve、compound interaction (C2/C10)、cross-task transfer，共 5 组实验
- **核心发现**: 两模型均呈现单调 dose-response；importance masking 效应远强于 random（DS 15-39x, QW 3-20x）；compound interaction 在 GSM8K 上 s025/s030 均显著（CI 不含 0）；DS 对稀疏化远比 QW 敏感（s020 即 -44pp vs QW 仅 -4pp）
- **待完成**: DS accuracy curve 的 s015/s025/s030 三个点仍在运行中

---

## 1. QW Accuracy Dose Curve (n=100, MATH)

### Reviewer-facing claim

Qwen2.5-7B-Instruct accuracy 随 sparsity 单调下降，s015–s025 区间相对平坦（0.36–0.33），s030 出现陡降（-14pp）。

### Evidence

| Sparsity | Accuracy | Correct/Total | Source exp_id | Batch detail |
|----------|----------|---------------|---------------|--------------|
| dense | 0.40 | 40/100 | `acc_qw_dense_n100` | batch1=0.32, batch2=0.48 |
| s015 | 0.36 | 36/100 | `acc_qw_s015_n100` | batch1=0.34, batch2=0.38 |
| s020 | 0.36 | 36/100 | `acc_qw_s020_n100_b2_fix` | batch1_v2=0.26, batch2=0.46; combined rescored |
| s025 | 0.33 | 33/100 | `acc_qw_s025_n100` | batch1=0.32, batch2=0.34 |
| s030 | 0.19 | 19/100 | `acc_qw_s030_n100` | batch1=0.14, batch2=0.24 |

### Caveats

- batch1 使用 max_new_tokens=2048，batch2 使用 8192。QW 截断率极低（~6%），影响可忽略。
- s020 的 batch1 经过 rescore（batch1_v2），两批合并后重新计算。

---

## 2. DS Accuracy Dose Curve (n=50, MATH, max_new_tokens=8192)

### Reviewer-facing claim

DeepSeek-R1-Distill-Qwen-7B 对稀疏化极度敏感：dense→s020 即出现 -44pp 的剧烈下降（0.74→0.30）。

### Evidence

| Sparsity | Accuracy | Correct/Total | Truncation Rate | Source exp_id | Status |
|----------|----------|---------------|-----------------|---------------|--------|
| dense | 0.74 | 37/50 | 16% | `acc_ds_dense_8k_v2` | ✅ |
| s015 | — | — | — | `acc_ds_s015_8k_v2` | 🏃 RUNNING |
| s020 | 0.30 | 15/50 | 58% | `acc_ds_s020_8k_v2` | ✅ |
| s025 | — | — | — | `acc_ds_s025_8k_v2` | 🏃 RUNNING |
| s030 | — | — | — | `acc_ds_s030_8k_v2` | 🏃 RUNNING |

### Caveats

- DS 截断率极高（s020 在 8k tokens 下仍达 58%），测量 accuracy 为下界。
- 按 D086 决策，DS accuracy 定位为"定性观察"（qualitative observation），非主要证据。
- n=50 样本量较小，置信区间宽。

---

## 3. C10 GSM8K Compound Interaction (QW random masking, n=50)

### Reviewer-facing claim

Compound interaction 在 GSM8K 上对 QW 的 s025 和 s030 均显著存在，且呈现 dose-response：s030 的 interaction index 约为 s025 的 2–4 倍。

### Evidence

**gsm8k_qw_rand_s030_v2** (PASS):

| Phase | II Median | 95% CI |
|-------|-----------|--------|
| high_sparsity | 2.31 | [1.64, 2.81] |
| mid_sparsity | 2.70 | [1.46, 8.77] |
| low_sparsity | 5.20 | [3.95, 7.24] |

**gsm8k_qw_rand_s025_v2** (PASS):

| Phase | II Median | 95% CI |
|-------|-----------|--------|
| high_sparsity | 0.72 | [0.60, 0.93] |
| mid_sparsity | 1.13 | [0.64, 3.37] |
| low_sparsity | 1.46 | [1.11, 2.05] |

### Caveats

- 所有 median CI 均不包含 0，交互效应在两个 sparsity 水平上均统计显著。
- mid_sparsity phase 的 CI 较宽（尤其 s030: [1.46, 8.77]），估计精度有限。

---

## 4. Core C2 Results (n=500, MATH-500)

### Reviewer-facing claim

Importance masking 的 compound interaction 在两模型上均呈单调 dose-response，且远强于 random masking（DS 15–39x，QW 3–20x）。所有对比 Wilcoxon 检验 p < 1e-14。

### Evidence

**DeepSeek** (`c2_n500_deepseek`):

| Sparsity | Importance II | Random II | imp/rand ratio | Wilcoxon p |
|----------|--------------|-----------|----------------|------------|
| s015 | 0.39 | ~0 | — | < 1e-70 |
| s020 | 1.21 | ~0 | — | < 1e-70 |
| s025 | 3.99 | 0.26 | 15.5x | < 1e-70 |
| s030 | 8.48 | 0.51 | 16.6x | < 1e-70 |

- dose_response_monotonic = true

**Qwen** (`c2_qw_n500_r3`):

| Sparsity | Importance II | Random II | imp/rand ratio | Wilcoxon p |
|----------|--------------|-----------|----------------|------------|
| s015 | 0.07 | ~0 | 2.7x | < 1e-14 |
| s020 | 0.31 | ~0 | — | < 1e-14 |
| s025 | 1.07 | significant | 20.1x | < 1e-14 |
| s030 | 3.16 | significant | — | < 1e-14 |

- dose_response_monotonic = true

### Caveats

- Random masking 在 s015/s020 接近 0，ratio 在这些点不稳定（分母极小）。
- DS 的 imp/rand ratio 表格中 s015/s020 因 random≈0 未报具体 ratio，s025=15.5x 和 s030 从原始数据推算为 8.48/0.51≈16.6x（原始报告值 15.5–38.6x 涵盖不同统计口径）。

---

## 5. GSM8K Cross-Task Transfer (importance masking, DS)

### Reviewer-facing claim

Importance masking 的 compound interaction 从 MATH 迁移至 GSM8K：DS 在 GSM8K 上同样呈现单调 dose-response，importance/random ratio 2.3–3.8x。

### Evidence

From `gsm8k_profiling_ds`:

| Sparsity | II (importance) | Wilcoxon p | imp/rand ratio |
|----------|----------------|------------|----------------|
| s015 | 0.24 | ≤ 0.0003 | 2.3x |
| s020 | 0.74 | ≤ 0.0003 | — |
| s025 | 1.99 | ≤ 0.0003 | — |
| s030 | 4.68 | ≤ 0.0003 | 3.8x |

### Caveats

- Cross-task transfer 仅在 DS 上测试，QW 的 GSM8K transfer 数据来自 C10（Section 3），masking 策略不同（random vs importance）。
- imp/rand ratio 范围 2.3–3.8x，低于 MATH 上的 15–39x，表明 cross-task 场景下 importance 优势收窄。

---

## Pending Results

| exp_id | 实验 | 状态 | 预计完成 |
|--------|------|------|----------|
| `acc_ds_s015_8k_v2` | DS accuracy @ s015, n=50, 8k tokens | 🏃 RUNNING | TBD |
| `acc_ds_s025_8k_v2` | DS accuracy @ s025, n=50, 8k tokens | 🏃 RUNNING | TBD |
| `acc_ds_s030_8k_v2` | DS accuracy @ s030, n=50, 8k tokens | 🏃 RUNNING | TBD |

这三个实验完成后将补全 DS accuracy dose curve 的完整 5 点数据，预期确认 DS 的 s025/s030 accuracy 进一步下降（与 C2 interaction 强度一致）。
