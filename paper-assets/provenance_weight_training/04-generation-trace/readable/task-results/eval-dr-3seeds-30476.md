# eval dr 3seeds 30476

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_dr_3seeds_30476_20260518T132136_result.json`
- **Structured JSON:** [`13c33ba7e23fa5ae96e6.json`](../../sessions/13/13c33ba7e23fa5ae96e6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 个 eval 全部成功完成。

## 结果汇总

### PPL 结果

| 模型 | Loss | Perplexity | Tokens |
|------|------|------------|--------|
| detect_remove_q05_seed123 | 2.8491 | **17.27** | 4,077,068 |
| detect_remove_q05_seed456 | 2.8493 | **17.28** | 4,077,068 |
| detect_remove_q09_seed42 | 2.8577 | **17.42** | 4,077,068 |

q05 两个 seed 的 PPL 非常接近（17.27 vs 17.28），复现性良好。q09 的 PPL 略高（17.42），说明更激进的过滤阈值（移除更多数据）导致了轻微的性能下降。

### D&R q05 filtered 数据统计

- 样本数：153,725
- 估算 token 总量：约 **1.03 亿 tokens**（基于 words × 1.3 近似）

---
