# experiment lr zscore cross strategy 001

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_lr_zscore_cross_strategy_001_20260515T094139_result.json`
- **Structured JSON:** [`c2fb3360a349ebaa505f.json`](../../sessions/c2/c2fb3360a349ebaa505f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成，registry 和 artifact 已更新。

## 结果摘要

**结论：NEGATIVE — 论文 claim 不成立。**

| 条件 | Model | d1v2 AUC (raw→zscore) | Paper 声称 |
|------|-------|----------------------|-----------|
| temp09 holdout | GPT-2 XL | 0.50 → **0.24** | 0.13 → 0.68 |
| temp09 holdout | OLMo | 0.50 → **0.19** | 0.25 → 0.83 |
| temp09 holdout | Pythia | 0.63 → **0.52** | — |

关键发现：
1. **Raw LR 完全失效**：lbfgs 在未缩放特征上收敛失败（0 iterations），acc = 0.25（随机猜测）
2. **Z-score 大幅提升整体表现**：mean acc 0.25 → 0.61，nucleus/topk50 holdout d1v2 AUC 达 0.61-0.89
3. **但 temp09 holdout d1v2 AUC 反转**：z-score 后 GPT-2 XL 和 OLMo 的 d1v2 AUC 降至 < 0.25（比随机差），说明模型学到了**反向**的 d1/d2 判别边界
4. **temp09 的分布偏移不是 scale 问题**，z-score 无法修复，需要其他方法（如 domain adaptation 或重新设计 feature）

**论文 framing 中 "z-score 恢复 LR cross-strategy d1v2 AUC" 的 claim 需紧急修改或删除。**

---
