# check v7 progress

**collapse aware mixing** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_v7_progress_20260513T154422_result.json`
- **Structured JSON:** [`98ec5e8a7b52bff1f7cd.json`](../../sessions/98/98ec5e8a7b52bff1f7cd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## mvp_pilot_v7 进度汇报

### 当前阶段：G1 synth（合成数据生成），67% (204/306)

日志显示 `generate: 67% | 204/306 [2:59:13]`，每 batch 约 65s，正在进行中。

---

### 已完成阶段指标

| 指标 | G0 (final) | G1 (final) | 变化 |
|------|-----------|-----------|------|
| **eff_rank** | 676.96 | 678.30 | +1.3 (稳定) |
| **ppl** | 13.27 | 13.41 | +0.14 (略升) |
| **spectral_entropy** | 6.518 | 6.520 | 稳定 |
| **vocab_coverage** | 0.469 | **0.137** | **-71% 严重下降** |
| **unigram_entropy** | 6.93 | **0.96** | **-86% 崩塌** |
| **unigram_unique** | 23,586 | **6,878** | **-71%** |
| **trigram_entropy** | 11.41 | **1.28** | **-89% 崩塌** |
| **kl_unigram** | — | 1.65 | 高偏移 |
| **logit_kl_mean** | — | 0.0055 | |

### 关键发现

G1 的 spectral 指标（eff_rank, ppl）看起来稳定，但 **生成多样性已严重崩塌**：vocab_coverage 从 47% 跌到 14%，unigram_entropy 从 6.93 跌到 0.96。模型的隐藏表征还行，但输出分布已经高度退化——典型的 model collapse 早期信号，G2 大概率会更差。

### GPU
- 利用率：15%（生成阶段以推理为主，利用率偏低正常）
- 显存：28.9 GB / 97.9 GB

### 剩余时间估算
- G1 synth 剩余：102 batches × ~65s ≈ **1.8h**
- G2 train：~10 min
- G2 eval：~1.8h
- **总计约 3.6h 完成全部流程**

---
