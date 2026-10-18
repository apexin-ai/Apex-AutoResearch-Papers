# ops harvest attn k07 s42 cqa1

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_harvest-attn-k07-s42-cqa1_20260527T180004_result.json`
- **Structured JSON:** [`7ca3295b99af4724f23e.json`](../../sessions/7c/7ca3295b99af4724f23e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新至 DONE。

## 结果汇总

**Attn k=0.7 Long seed42 (cqa1 副本): Overall SR = 50.8%**

| Task | cqa1 | w41 |
|------|------|-----|
| T0 | 72% | 72% |
| T1 | 70% | 70% |
| T2 | 58% | 70% |
| T3 | 46% | 36% |
| T4 | 36% | 46% |
| T5 | 32% | 26% |
| T6 | 58% | 80% |
| T7 | 48% | 56% |
| T8 | 6% | 8% |
| T9 | 82% | 76% |
| **Overall** | **50.8%** | **53.6%** |

cqa1 版本比 w41 低 2.8pp。Per-task 差异较大（T6 差 22pp，T3/T4 互换趋势），体现了 Long suite 固有的 seed/环境方差。两个副本均值为 **52.2%**。

注意：实际日志文件名为 `eval_pi05_attention_k07_long_seed42.log`（非预期的 `_strict_cqa1` 后缀）。

---
