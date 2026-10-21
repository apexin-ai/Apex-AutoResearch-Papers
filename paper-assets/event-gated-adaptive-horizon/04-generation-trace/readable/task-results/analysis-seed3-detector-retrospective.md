# analysis seed3 detector retrospective

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_seed3-detector-retrospective_20260517T032411_result.json`
- **Structured JSON:** [`96ee943cbf720a067fb5.json`](../../sessions/96/96ee943cbf720a067fb5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果已写入 `artifacts/analysis/seed3_detector_retrospective.json`。

## 关键发现

**CIVO detector 未触发。** 4 个条件从未同时满足。核心原因：

1. **时序错位** — 45K 步满足 3/4 条件（delta_ve 加速 + 3点下降 + delta_ve>0.1），但 ve_ratio=0.497，差 0.003 未过 0.5 阈值。这与预估一致：NVE=1.50× 对应 ve_ratio≈0.497。

2. **终端下降不是渐进的** — 452→268 是 95K→105K 的单步崩溃，不满足"连续3点下降"（条件4）。在 85K 时 eval 已经有一次下跌（356→314），但 95K 又反弹到 452，所以 105K 时不构成 3 点连续下降。

3. **条件最接近同时触发的位置**：
   - **45K**: 3/4 条件满足，仅 ve_ratio 差 0.003 未达标
   - **85K**: ve_ratio=0.97 + delta_ve=0.21（2/4），但无加速且无 3 点下降

## 对 detector 设计的启示

- 0.5 阈值对该 seed 来说过于严格（45K 时 0.497 恰好错过）
- 3 点连续下降条件对"突发崩溃"模式无效
- 如果将 ve_ratio 阈值降至 0.49 或取消条件 4 的严格性，45K 即可触发，lead time 约 60K 步

---
