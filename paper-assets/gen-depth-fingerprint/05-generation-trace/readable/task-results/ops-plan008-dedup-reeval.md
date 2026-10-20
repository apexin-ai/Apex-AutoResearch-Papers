# ops plan008 dedup reeval

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_plan008-dedup-reeval_20260515T223303_result.json`
- **Structured JSON:** [`63f0e32f944719833bd2.json`](../../sessions/63/63f0e32f944719833bd2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

**Dedup**: news 去除 801 重复（3115→2314），scientific/creative 无重复。

**Dedup 后 vs 前**:
| | news | scientific | creative | wikipedia |
|---|---|---|---|---|
| 3class F1 | 0.574→**0.561** (-1.3pp) | 0.705 (不变) | 0.628 (不变) | 0.793 (不变) |
| binary F1 | 0.627→**0.626** | 0.770 | 0.731 | 0.822 |

- Cross-domain pooled: 0.478→0.478 (基本不变)
- Wiki→news transfer: 0.225→0.231 (+0.6pp)

变化在噪声范围内，结论不变。Registry 已更新，标注 dedup applied。

---
