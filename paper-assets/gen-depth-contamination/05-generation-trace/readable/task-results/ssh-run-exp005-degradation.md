# ssh run exp005 degradation

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_run_exp005_degradation_20260513T023913_result.json`
- **Structured JSON:** [`59675f631694ba75fe79.json`](../../sessions/59/59675f631694ba75fe79.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

exp-005 完成，registry 已更新为 DONE (success)。

## 结果摘要

### Cross-model Kendall τ (by avg AUC)

| 模型对 | τ | p |
|--------|---|---|
| Pythia vs OLMo | **0.848** | 0.000 |
| Pythia vs Qwen | 0.524 | 0.006 |
| OLMo vs Qwen | 0.486 | 0.011 |
| **Mean** | **0.619** | — |

### Degradation ordering (top-3 最先饱和的特征)

| Pythia-1.4B | OLMo-1B | Qwen-1.5B |
|-------------|---------|-----------|
| surp_d1_std | surp_std | **freq_entropy** |
| surp_d2_std | surp_d1_std | surp_std |
| surp_std | surp_d2_std | surp_d1_std |

### 判断：**success，需要 caveat**

- Pythia/OLMo 一致性强（τ=0.85, ρ=0.95），共享 surp_*_std 作为最早饱和的特征组
- Qwen 偏离：freq_entropy 排 #1（AUC=0.97），TailFreq 组在 Qwen 上的判别力远强于另外两个模型
- 深层 depth pair（3v4, 4v5）跨模型一致性迅速衰减到接近随机（τ→0），说明 ordering consistency 主要体现在早期 depth
- **C2 claim**：部分支持——同族模型一致性好，跨架构族需要加 caveat 说明 Qwen 的 TailFreq 特异性

---
