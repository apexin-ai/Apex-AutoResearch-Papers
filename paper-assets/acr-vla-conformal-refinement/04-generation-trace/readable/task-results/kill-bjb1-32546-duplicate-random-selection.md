# kill bjb1 32546 duplicate random selection

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_kill_bjb1-32546-duplicate-random-selection_20260520T114353_result.json`
- **Structured JSON:** [`55146386d63b1152dac3.json`](../../sessions/55/55146386d63b1152dac3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

PID 360293 和 360306 已 kill 成功。

**bjb1-32546 GPU 最终状态：**

| GPU | 状态 | PID | 实验 |
|-----|------|-----|------|
| cuda:0 | 占用 | 362579 | crm_obs_only / goal / seed52 |
| cuda:1 | **空闲** | — | 已 kill 重复的 random_selection_spatial_seed42 (360293/360306) |
| cuda:2 | **空闲** | — | 无进程 |
| cuda:3 | 占用 | 363783 | crm_obs_only / object / seed49 |
| cuda:4 | 占用 | 364125 | reconvla / object / seed48 |
| cuda:5 | 占用 | 364591 | reconvla / object / seed49 |

cuda:1 和 cuda:2 现在空闲可用。被 kill 的两个重复进程（random_selection_spatial_seed42）已释放 cuda:1 上的 GPU 显存。

---
