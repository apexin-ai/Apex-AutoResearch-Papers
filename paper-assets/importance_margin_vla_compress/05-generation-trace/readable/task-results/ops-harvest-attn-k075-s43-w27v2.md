# ops harvest attn k075 s43 w27v2

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_harvest-attn-k075-s43-w27v2_20260527T212500_result.json`
- **Structured JSON:** [`ed66662fa27d0f03834d.json`](../../sessions/ed/ed66662fa27d0f03834d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。

**结果汇总：Attn k=0.75 Long seed43 (w27) = 49.0%**

| Task | Successes | SR |
|------|-----------|-----|
| T0 | 29/50 | 58% |
| T1 | 34/50 | 68% |
| T2 | 31/50 | 62% |
| T3 | 15/50 | 30% |
| T4 | 16/50 | 32% |
| T5 | 24/50 | 48% |
| T6 | 38/50 | 76% |
| T7 | 13/50 | 26% |
| T8 | 7/50 | 14% |
| T9 | 38/50 | 76% |
| **Overall** | **245/500** | **49.0%** |

**跨硬件一致性分析**：seed42 在 cqa1 上跑出 52.4%，此 seed43 在 w27 上 49.0%。两个 seed 差 3.4pp，与之前观察到的 seed42 跨硬件差异（52.4% vs 50.8% = 1.6pp）量级相当。Attn k=0.75 的 error bar 大致在 49-52% 范围内。

---
