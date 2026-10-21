# analysis alpha sweep a055 s42 fp32

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_alpha_sweep_a055_s42_fp32_20260520T134300_result.json`
- **Structured JSON:** [`6d7d4b188e1cb5e9858e.json`](../../sessions/6d/6d7d4b188e1cb5e9858e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。

## 结果摘要

**alpha_sweep_a055_s42_fp32: PermG = 0/8, K≥3 = 0/8**

| Alpha | PermG | Zone |
|-------|-------|------|
| 0.45 | 0/8 | Blind zone |
| **0.50** | **6/8** | **Onset** |
| **0.55** | **0/8** | **Sync collapse** |
| 0.60 | 0/8 | Sync collapse |
| 0.75 | 6/8 | Detection regime |

α=0.55 与 α=0.60 一致（PermG=0/8），sync-collapse dip 起始点在 **α∈(0.50, 0.55)** 区间内。0.50→0.55 之间 PermG 从 6/8 骤降至 0/8，过渡非常陡峭（Δα=0.05）。

值得注意的是 PermG 的 p_FDR 全部集中在 0.072——距离 0.05 阈值很近。F-stat 在 forward 方向极大（38–362），reverse 极小（0.03–0.76），方向不对称性非常强，信号存在但在 T=11 下统计功效不足以过 FDR 校正。DiffXcorr 8/8 forward significant 进一步佐证了这点。

Registry 已更新至 DONE(success)，两个 artifacts 已注册。

---
