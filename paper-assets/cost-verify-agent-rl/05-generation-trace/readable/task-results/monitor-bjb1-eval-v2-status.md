# monitor bjb1 eval v2 status

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_bjb1_eval_v2_status_20260520T000328_result.json`
- **Structured JSON:** [`9441982b22966adec657.json`](../../sessions/94/9441982b22966adec657.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Eval v2 状态汇总

**进程**: PID 195853 运行中，启动于 07:42（约21分钟前），**不是**之前报告的18h——这是一次全新重启。

**GPU 状态**:
| GPU | 显存 | 利用率 | 温度 | 功耗 |
|-----|------|--------|------|------|
| cuda:0 | 84,161 / 97,887 MiB (86%) | 41% | 41°C | 145W |
| cuda:1 | 84,161 / 97,887 MiB (86%) | 95% | 41°C | 176W |

**进度**:
- 已完成: **464 / 1796** episodes (25.8%)
- 成功: **167 / 464** (36.0% success rate)
- Resume 后新增: 25 episodes (从 440 → 464)

**速度与 ETA**:
- 当前速度: ~1.2 episodes/min (平均 ~50s/episode)
- 剩余: 1332 episodes
- 预计剩余: **~18.5 小时** (约明天凌晨 02:30 完成)

**输出文件**: `/root/autodl-tmp/checkpoints/scienceworld_sft/eval_results_dev_v2.jsonl` (68KB, 464行)

**日志文件**: `/tmp/eval_scienceworld_v2_resumed.log`

**注意**: 当前在跑 `inclined-plane-friction-named-surfaces` 系列，很多 episode 跑满100步超时 (FAIL)，拉低速度。后续 task 类型可能更快或更慢。

---
