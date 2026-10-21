# code d146 status check

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d146-status-check_20260519T150903_result.json`
- **Structured JSON:** [`7befc8e5face255abcba.json`](../../sessions/7b/7befc8e5face255abcba.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## D146 Pipeline 状态报告

| 项目 | 状态 |
|------|------|
| **tmux session** | `d146-pipeline` 存活（PID 441009 活跃） |
| **GPU 0** | 84.5 / 97.9 GB 显存，87% utilization |
| **当前实验** | `d146_pf_exec_s42`（第 1/6 个） |
| **当前进度** | **step 23 / 500**（4.6%） |
| **最新 step 时间** | 2026-05-19 15:09:31 UTC |

### 各实验状态

| 实验 | 状态 |
|------|------|
| d146_pf_exec_s42 | **训练中** step 23/500 |
| d146_pf_exec_s43 | 未开始 |
| d146_pf_exec_s44 | 未开始 |
| d146_pf_isr_s42 | 未开始 |
| d146_pf_isr_s43 | 未开始 |
| d146_pf_isr_s44 | 未开始 |

### 当前实验指标（exec_s42 前 23 步）

reward 大部分为 0，偶有 spike（step 11: 0.375, step 19: 0.375, step 10: 0.125）。prove_rate 同步，parse_rate 稳定 1.0。尚处于训练极早期，模型还未起飞。

### 预估剩余时间

- 平均 step time ≈ 15 s/step
- exec_s42 剩余：(500−23) × 15s ≈ **1h 59min**
- 6 个实验总计：每个约 2h 5min，还剩 5.95 个实验 ≈ **~12.4 h**
- 预计全部完成：约 **明天凌晨 3:30 UTC**（北京时间 5/20 11:30）

---
