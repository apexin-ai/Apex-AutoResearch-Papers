# ops bjb1 status check urgent

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_bjb1_status_check_urgent_20260522T081328_result.json`
- **Structured JSON:** [`a33d01a470e775d88958.json`](../../sessions/a3/a33d01a470e775d88958.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## ScienceWorld v4b 状态报告

### 状态：**运行中**

| 项目 | 值 |
|------|-----|
| 实验名 | `scienceworld_grpo_cell_c_v4` |
| PID | 386364 (已运行 4h04m) |
| 进度 | **Step 2/15 (13%)** — 刚完成 step 1 的 train，正在做 step 2 的 rollout |
| 预估总时间 | ~22h（step 1 耗时 18m，step 2 含 eval 耗时 ~2h40m） |
| tmux session | `scienceworld_grpo_cell_c_v4` |

### GPU 使用

| GPU | 利用率 | 显存 |
|-----|--------|------|
| cuda:0 | 0% | 47,911 / 97,887 MiB (49%) |
| cuda:1 | 0% | 48,761 / 97,887 MiB (50%) |

GPU 利用率 0% 说明当前处于 **rollout/环境交互阶段**（CPU-bound），不在 forward/backward pass。显存占用 ~49GB/卡符合模型已加载的预期。

### 关键指标（Step 1 Train）

| 指标 | 值 |
|------|-----|
| success | **0.0** |
| score | 13.01 |
| final_score | 16.79 |
| pass@16 | 0.0 |
| action_is_valid | 55.9% |
| action_is_effective | 96.1% |
| episodic_return | 0.0 |
| pg_loss | -0.082 |
| kl_loss | 0.471 |
| grad_norm | 4.065 |
| throughput | 118 tokens/s |
| time_per_step | 1122s (~18.7min) |

### Eval (Step 0, Baseline)

| 指标 | 值 |
|------|-----|
| val success | 0.0 |
| val score | 2.63 |
| val final_score | 4.84 |
| val reward@32 mean | 0.484 |
| val pass@1 | 0.0 |

### 注意事项

- 训练 step 1 的 success=0、pass@16=0，但 score/final_score 非零，说明 agent 有部分进展但未完成任何完整 task。
- Step 2 耗时显著增加（从 18min 跳到 ~2h40m），可能是 rollout 中环境交互变慢（response_length mean=2069 tokens，max=16208）。
- 当前正在做 step 2 的 rollout（GPU 空闲），属正常行为。

---
