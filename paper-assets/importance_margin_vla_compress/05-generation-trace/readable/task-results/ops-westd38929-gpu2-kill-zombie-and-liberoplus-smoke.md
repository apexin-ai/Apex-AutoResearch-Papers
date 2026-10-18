# ops westd38929 gpu2 kill zombie and liberoplus smoke

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd38929-gpu2-kill-zombie-and-liberoplus-smoke_20260520T234556_result.json`
- **Structured JSON:** [`43843f1ec484a282b47e.json`](../../sessions/43/43843f1ec484a282b47e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## LIBERO-Plus Smoke Test 结果

| 指标 | 值 |
|------|-----|
| **Overall SR** | **3.3% (1/30)** |
| 耗时 | 22.0 min |
| Task 1 (view_0_0_100_2_4) | 0/10 (0%) |
| Task 2 (view_0_0_100_2_8) | 1/10 (10%) |
| Task 3 (view_0_0_100_2_350) | 0/10 (0%) |

**结论：SR = 3.3%，远低于 30% 阈值。**

这与 LIBERO-Plus 排行榜上 OpenVLA Camera SR = 0.8% 一致（我们 3 task 采样方差导致略高）。即使是最轻微的 L1 Camera Viewpoint 扰动，vanilla OpenVLA 也几乎完全失败。

**对 C7 实验线的含义：**
- LIBERO-Plus 作为 robustness benchmark **可用** — 它确实能有效暴露 VLA 对 camera perturbation 的脆弱性
- 但 vanilla OpenVLA baseline SR 太低（~3%），直接用作压缩前后对比的 baseline 意义不大（地板效应）
- 如果 C7 目标是证明 "压缩后鲁棒性不降"，需要先找到一个在 LIBERO-Plus 上有合理 baseline SR 的模型/方法，或者换一个更温和的扰动维度/难度

---
