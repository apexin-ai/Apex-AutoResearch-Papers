# analysis exp 32b c4

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_32b_c4_20260519T213424_result.json`
- **Structured JSON:** [`517b6f9289ab160a7319.json`](../../sessions/51/517b6f9289ab160a7319.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验结果摘要：

- **状态**: 成功完成
- **K\* = 2**，与 1.5B/7B/8B/14B 完全一致
- 关键 AUC：0v1 = 0.9575, 1v2 = 0.6183 (>0.60), 2v3 = 0.5454 (<0.60)
- JSD 同样显示 depth 1 之后快速饱和（0v1: 0.1149 → 1v2: 0.0101 → 2v3: 0.0054）
- 无 W&B 记录

**结论**: Scale invariance confirmed up to 32B。模型规模（至少到 32B）不影响 C4 上 K\*=2 的结论，排除了 scale ceiling effect。报告已注册为 artifact `art_20260519_7b278e`。

---
