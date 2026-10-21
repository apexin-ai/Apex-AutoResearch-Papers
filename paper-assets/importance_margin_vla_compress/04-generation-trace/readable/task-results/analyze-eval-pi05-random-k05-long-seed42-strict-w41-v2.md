# analyze eval pi05 random k05 long seed42 strict w41 v2

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval_pi05_random_k05_long_seed42_strict_w41_v2_20260527T120416_result.json`
- **Structured JSON:** [`fc6120e06dcde9f56fd4.json`](../../sessions/fc/fc6120e06dcde9f56fd4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。

## 结果总结

**π0.5 Random k=0.5 Long (strict) Overall SR = 49.8%**

Per-task: 70, 40, 68, 74, 50, 30, 40, 62, 8, 56

### 极端压缩点 k=0.5 三方法 strict 对比（Long suite）

| 方法 | Overall SR |
|------|-----------|
| L2norm | 50.0% |
| **Random** | **49.8%** |
| Attn | 49.8% |

三种方法在 k=0.5 处几乎完全一致（50.0% vs 49.8% vs 49.8%），差异在噪声范围内。这符合极端压缩下方法差异消失的预期——丢弃一半 token 后，无论用什么策略选择保留哪些，性能都坍缩到同一水平。

---
