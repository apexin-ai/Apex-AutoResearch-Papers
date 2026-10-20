# analysis plan004 classify h7

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_plan004-classify-h7_20260515T073245_result.json`
- **Structured JSON:** [`74545236f9494cc6a102.json`](../../sessions/74/74545236f9494cc6a102.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。

**plan004-o1-ablation-s42 分类结果：**

| 指标 | 计数 | 比率 |
|------|------|------|
| H7 (single premise == conclusion) | 0/63 | 0% |
| H1 (multi-prem, conclusion in premises) | 63/63 | 100% |
| Genuine (无 hacking) | 0/63 | 0% |

所有 63 个 proved 样本均为 H1（结论嵌入前提），零 genuine。这与该实验的 negative 结论一致：O(1) binary ISR 退化后模型完全依赖 conclusion-embedding hacking 策略获取 prove。

---
