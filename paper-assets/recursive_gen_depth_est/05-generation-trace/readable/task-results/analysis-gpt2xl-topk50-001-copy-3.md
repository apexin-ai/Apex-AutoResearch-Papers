# analysis gpt2xl topk50 001

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_gpt2xl_topk50_001_20260515T024241_result.json`
- **Structured JSON:** [`1af0997e46ac2be2d1cd.json`](../../sessions/1a/1af0997e46ac2be2d1cd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE。分析总结：

**GPT-2 XL top-k k=50**: 4-class RF **74.45%** (CI 73.0-75.8%), d1v2 AUC **0.813**, 3-class RF **69.47%**。

与同模型对比：相比 nucleus baseline (83.3%) 下降 **-8.85pp**，相比 temp09 (85.4%) 下降 **-10.95pp**。d1v2 AUC 从 0.913/0.937 降至 0.813，中间深度区分力显著削弱。

跨模型 top-k 影响：GPT-2 XL 降幅 (-8.85pp) 与 Pythia (-8.6pp) 几乎一致，OLMo 仅降 3.1pp。Top-k 截断对 GPT-2 XL 和 Pythia 的深度信号破坏程度相当，OLMo 更鲁棒。

值得注意：尽管 top-k 是三种策略中最差的，74.45% 仍是随机基线 (25%) 的 ~3 倍，深度信号在 top-k 下依然存在且可检测。three_class_filtered 结果缺失，contamination filtering 未跑完。

---
