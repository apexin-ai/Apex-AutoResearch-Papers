# analyze w41 attn k085 s43

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_w41_attn_k085_s43_20260527T205521_result.json`
- **Structured JSON:** [`a6772eebcb0e731c256a.json`](../../sessions/a6/a6772eebcb0e731c256a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成。

## 结果汇报

**总体成功率: 52.4%** (262/500)，EXIT_CODE=0，无错误。

**Per-task breakdown:**

| Task | 描述 | SR |
|------|------|----|
| T0 | alphabet soup + tomato | 26% |
| T1 | cream cheese + butter | 56% |
| T2 | stove + moka pot | 38% |
| T3 | black bowl → drawer | 68% |
| T4 | white mug + left plate | 46% |
| T5 | book → back shelf | 70% |
| T6 | white mug → plate | 72% |
| T7 | alphabet soup + cream | 54% |
| T8 | both moka pots → stove | 4% |
| T9 | yellow white mug → microwave | 90% |

**对比:**
- vs seed42 (50.0%): seed43 高 2.4pp，种子间波动合理
- vs D282 记录 (52.4%): **完全一致**，w41 重跑复现了之前 w27_v2 的结果
- 两个 seed 均值: (50.0 + 52.4) / 2 = **51.2%**

---
