# check exp029 progress

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_exp029_progress_20260517T025523_result.json`
- **Structured JSON:** [`a502c62b8e748971bb3f.json`](../../sessions/a5/a502c62b8e748971bb3f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp029_episode_level 训练状态

**状态：存活，正常运行中**

| 项目 | 值 |
|------|------|
| tmux session | ALIVE |
| 运行进程 | PID 905580 (Ray TaskRunner)，已运行 6h43m |
| 原始 PID 896477 | 已死（被 Ray 子进程接管） |
| 日志最后更新 | 2026-05-17 10:54:08（~9分钟前） |

### 进度

- **当前步数**: 14/100 (14%)
- **已用时间**: 6h36m
- **预计剩余**: ~37h56m（约 26.5 min/step）
- **预计完成时间**: 约 5月19日凌晨

### 最新 Metrics（step 12）

| 指标 | 值 |
|------|------|
| success | 23.4% |
| pass@8 | 62.5% |
| action_is_valid | 55.9% |
| action_is_effective | 85.4% |
| entropy | 0.0419 |
| ppo_kl | 0.00886 |
| grad_norm | 3.01 |
| response_length (mean) | 11,787 tokens |
| throughput | 553.5 tokens/s |

### GPU

- GPU 0: 97233/97887 MiB，0% utilization
- GPU 1: 97233/97887 MiB，0% utilization

GPU 利用率显示 0% 是因为查询瞬间正处于 ALFWorld 环境交互阶段（CPU-bound），模型权重已加载在显存中，训练正常推进。

---
