# analysis eval xvla random k085 long seed42

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval_xvla_random_k085_long_seed42_20260524T052351_result.json`
- **Structured JSON:** [`87252e2143eb38ad5378.json`](../../sessions/87/87252e2143eb38ad5378.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

## 结果摘要

**X-VLA Random k=0.85 Long: 35.0%** (175/500), CI [30.9%, 39.3%]

**核心发现**：Long 是 k=0.85 disruption peak 最严重的 suite：

| Suite | k=0.85 SR | k=0.5 SR | 非单调 gap |
|-------|-----------|----------|-----------|
| Spatial | 68.2% | 71.4% | -3.2pp |
| Object | 65.0% | 70.6% | -5.6pp |
| Goal | 60.4% | 67.2% | -6.8pp |
| **Long** | **35.0%** | **61.6%** | **-26.6pp** |

- 保留更多 token (k=0.85) 反而比保留更少 (k=0.5) 差 26.6pp，非单调效应在 Long 上最为剧烈
- 任务粒度上极度两极化：T5 (98%)、T3 (88%) 几乎不受影响，T6 (0%)、T4 (2%) 完全崩溃
- X-VLA 用 BART connector（无 RoPE），仍出现 disruption peak → 该效应不限于 RoPE 架构，是更通用的位置/结构敏感性
- 任务复杂度放大 disruption：多步多物体任务受影响最大

Registry 已更新为 DONE/success，报告已注册。

---
