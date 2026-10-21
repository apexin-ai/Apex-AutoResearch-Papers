# analysis exp 006 007 latest

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_006_007_latest_20260514T004218_result.json`
- **Structured JSON:** [`baffa654333dbba067e6.json`](../../sessions/ba/baffa654333dbba067e6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇总

### 进程状态
- **exp_006 (dt=2)**: ALIVE — GPU PID 85034, 4158 MiB — 当前 step=60000（下次 eval 在 65K）
- **exp_007 (dt=4)**: ALIVE — GPU PID 90359, 4336 MiB — 当前 step=48000（下次 eval 在 55K）

### 完整 Eval Trajectory

| Step | exp_006 (dt=2) | exp_007 (dt=4) | baseline | dt=2 vs base | dt=4 vs base |
|-----:|---------------:|---------------:|---------:|-------------:|-------------:|
| 5K | 31.0 | 31.0 | 31.8 | -2.5% | -2.5% |
| 15K | 256.9 | 129.6 | 153.9 | +66.9% | -15.8% |
| 25K | 321.4 | 176.9 | 254.2 | +26.4% | -30.4% |
| 35K | **485.3** | 126.7 | 290.8 | **+66.9%** | -56.4% |
| 45K | 477.0 | 144.4 | 443.0 | +7.7% | -67.4% |
| 55K | 360.4 | — | 541.2 | **-33.4%** | — |
| 65K | *(待 eval)* | — | 615.9 | — | — |

### 关键发现

**exp_006 (dt=2)**: 35K 峰值 485.3 后持续下行——45K 477.0、55K 360.4。两连跌，幅度 -25.7%，不是波动。55K 时已落后 baseline 33%。65K eval 数据预计 ~2-3 小时后产出，但趋势明确：**dt=2 在 35K 后崩塌**。

**exp_007 (dt=4)**: 严重落后。25K 峰值 176.9 后回落到 126-144 区间，仅 baseline 的 ~30%。**dt=4 基本失败**。

### 结论
两个 fixed-dt 实验均显著劣于 baseline：
- dt=2 早期学得快（35K 超 baseline 67%），但后期崩塌，说明高频决策前期有利但后期过拟合或信用分配问题
- dt=4 全程落后，说明低频决策丧失了必要的控制粒度
- 65K eval 仍值得等（确认 dt=2 是否继续下行），但分叉结论已基本可下：**adaptive horizon 有存在价值**，fixed dt 无法同时兼顾早期效率和后期稳定性

---
