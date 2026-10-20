# check seed0 r2 status

**collapse aware mixing** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_seed0_r2_status_20260514T145259_result.json`
- **Structured JSON:** [`084e242145510dccdb31.json`](../../sessions/08/084e242145510dccdb31.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态：`mvp_seed0_replication_r2`

**进程**: PID 122208 仍在运行，已运行 14h8m

**当前阶段**: G1 generate — 232/306 (76%), 约 ~52s/batch

### 已完成阶段
- **G0**: 训练 ✅ → 评估 ✅ → 生成 ✅
- **G1**: 训练 ✅ → 评估 ✅ → 生成 🔄 76%
- **G2**: 未开始

### 关键指标对比 (final_model)

| 指标 | G0 | G1 | 变化趋势 |
|------|----|----|---------|
| spectral_eff_rank | 676.89 | 678.21 | +1.32 (稳定) |
| perplexity | 13.27 | 13.42 | +0.15 (微升) |
| **unigram_entropy** | **6.93** | **0.92** | **-6.01 (崩塌)** |
| **unique_tokens** | **23,530** | **6,963** | **-70%** |
| **vocab_coverage** | **0.468** | **0.139** | **-70%** |
| bigram_entropy | 10.20 | 1.15 | -9.04 |
| trigram_entropy | 11.42 | 1.22 | -10.19 |
| kl_unigram | — | 1.71 | (vs reference) |
| js_divergence | — | 1.02 | (高) |

### 分析

G1 出现严重的**生成多样性崩塌**：unigram entropy 从 6.93 暴跌到 0.92，vocab coverage 从 47% 降到 14%。但 spectral effective rank 几乎未变（676→678），perplexity 仅微升。这说明模型内部表征维度没塌，但生成的文本多样性已经严重退化——典型的 model collapse 信号。

### 剩余时间估算

- G1 generate 剩余: 74 batches × ~52s ≈ **~1h**
- G2 (train + eval + generate): 参考前两代约 **~5-6h**
- 总计剩余: **~6-7h**

---
