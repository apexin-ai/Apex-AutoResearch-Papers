# analysis cheetah rssm v3 verify

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_cheetah-rssm-v3-verify_20260526T081417_result.json`
- **Structured JSON:** [`0fa6181e19a70a388836.json`](../../sessions/0f/0fa6181e19a70a388836.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

V3 standardized 分析成功完成。汇报如下：

---

## 结果汇报

### 1. PID 234523 状态
**已终止**（进程不存在）。同时清理了另外两个残留进程：PID 839413（超时 GPU 运行）和 PID 538202（运行 2.5h 的 CPU 运行）。

### 2. 上次 GPU 运行使用了错误脚本
- **脚本**: `analyze_rssm_exp101.py` (version: `exp101_v1.0`)
- **不是** `analyze_rssm_standardized.py` (version: `v3_standardized`)
- 关键差异：exp101 按 episode 计数（请求 1000 只加载 112），standardized 按 transition 采样（真正 1000 个采样点）

### 3. V3 Standardized 重跑结果（已完成）

| 指标 | dt=1 | dt=2 | ratio (dt2/dt1) |
|------|------|------|-----------------|
| **obs_MSE** | 5.2554 | 4.8952 | **0.93x** |
| **reward_MAE** | 0.1410 | 0.1405 | **1.00x** |

Per-key obs_MSE:
- position: dt1=0.00428, dt2=0.00824, ratio=1.93x
- velocity: dt1=10.506, dt2=9.782, ratio=0.93x

### 4. 与 exp101 结果对比

| 指标 | exp101 | v3_standardized | 差异 |
|------|--------|-----------------|------|
| dt1 obs_MSE | 5.131 | 5.255 | +2.4% |
| dt2 obs_MSE | 4.851 | 4.895 | +0.9% |
| obs ratio | 0.945 | 0.931 | 趋势一致 |
| dt1 reward_MAE | 0.1406 | 0.1410 | +0.3% |
| dt2 reward_MAE | 0.1408 | 0.1405 | -0.2% |
| reward ratio | 1.002 | 0.997 | 趋势一致 |

**结论**：两个脚本结果高度一致（差异 <3%），核心发现不变——dt=2 的 obs_MSE 反而比 dt=1 低（ratio<1），reward 几乎无差异。方法论现在使用了正确的 v3_standardized 脚本，metadata 中 `script_version="v3_standardized"`, `method="sequential_rollout"`, `n_samples=1000`。

修复：给 `analyze_rssm_standardized.py` 的 `load_world_model` 加了 `wm.to(config.device)` 以支持 GPU 运行。

---
