# analysis sparse timeseries 008d

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_sparse_timeseries_008d_20260525T023635_result.json`
- **Structured JSON:** [`264bc79981c52fab7e8f.json`](../../sessions/26/264bc79981c52fab7e8f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。核心结果：

**exp_008d (s1) 只有 `latest.pt` (55K)，无法做计划中的 25K vs 75K 两点对比。**

但现有数据已能得出结论：

| | exp_066 (s0) @ 55K | exp_008d (s1) @ 55K |
|---|---|---|
| dt=2/dt=1 SS reward MAE ratio | 1.37x | **2.70x** |
| VE ratio | 0.62 | **1.67** |

**跨 seed 支持因果方向的证据：**
1. **s0 直接时序证据**（exp_066 完整 12 点时序）：OL fidelity gap 在 25K 达 1.22x 时 VE 仅 0.16，VE 首次 spike 在 40K，滞后 ~15K 步
2. **s1 截面强相关**：更大的 fidelity gap（2.7x vs 1.4x）对应更严重的 VE（1.67 vs 0.62）
3. **两个 seed 的 VE 轨迹一致**：25K 处 VE 低（s0: 0.163, s1: 0.155），之后逐步恶化

**局限**：无法用 s1 独立确认时序因果（无中间 checkpoint），但截面相关性 + s0 时序因果 + VE 轨迹一致性，共同支持 "fidelity gap drives VE" 假说。

报告已注册为 artifact `art_20260525_e45921`，registry notes 已更新。

---
