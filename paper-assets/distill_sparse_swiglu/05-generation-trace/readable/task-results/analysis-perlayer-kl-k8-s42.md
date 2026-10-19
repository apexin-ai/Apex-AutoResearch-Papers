# analysis perlayer kl k8 s42

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_perlayer_kl_k8_s42_20260523T031356_result.json`
- **Structured JSON:** [`8239941d46774ce7c6ba.json`](../../sessions/82/8239941d46774ce7c6ba.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

| 指标 | 值 |
|------|-----|
| 训练状态 | 正常完成（1000/1000 steps） |
| Final avg KL | 0.0983 |
| Final avg sparsity | 0.281 |
| Wall time | ~1894s |
| **WikiText-2 PPL** | **8.97** |

### 对比

| 配置 | PPL (uniform 30%) |
|------|-------------------|
| K=1 (E2E) | 9.05 |
| K=4 | 9.22 |
| **K=8** | **8.97** |

**Conclusion: success.** K=8 的 PPL 8.97 优于 K=4 (9.22) 和 K=1 (9.05)，验证了 doubling masking breadth 改善 train-inference alignment 的假设。Registry 已更新为 DONE/success。

---
