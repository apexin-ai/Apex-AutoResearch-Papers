# check verify correction approach

**error diag dpo recovery** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_verify-correction-approach_20260512T135516_result.json`
- **Structured JSON:** [`2388989347953fb6f1ba.json`](../../sessions/23/2388989347953fb6f1ba.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 检查结果

### 1. 当前运行的是**从头重做版本**（错误）

`test_correction_feasibility.py` 的 docstring 明确写着 "fresh-start attempts"。主循环逻辑：
- 对每个 task 创建新环境，调用 `collect_single_trajectory` 跑完整 episode
- 没有 `failure_step` 参数、没有 replay 逻辑
- 每个 attempt 都是独立的从头开始的完整 episode

### 2. Replay 版本**存在且可用**

`test_correction_feasibility_replay.py` 实现了正确的 replay-then-correct 逻辑：
- `detect_failure_step()` — 检测原始轨迹中的首个失败信号（"Nothing happens"、重复动作等）
- `extract_original_steps()` — 从原始对话中提取 action 序列
- `replay_and_correct()` — replay 原始 actions 到 `failure_step - 1`，然后用模型生成纠正续写
- 日志输出区分 `replay_steps` 和 `correction_steps`

### 3. 日志确认是 fresh-start 行为

```
[1/100] attempt=0 task=25 type=look_at_obj reward=False steps=40 time=88.5s sr=0/1
[2/100] attempt=0 task=79 type=pick_and_place reward=False steps=40 time=69.0s sr=0/2
[3/100] attempt=0 task=114 type=look_at_obj reward=False steps=40 time=60.5s sr=0/3
```
- 全部跑满 40 步后失败，没有 replay/correction 步数区分
- 总计 100 episodes（10 tasks × 10 attempts），目前完成 3/100
- 进度约 3%，已耗时 ~4 分钟

### 4. 建议

**需要切换到 replay 版本。** 当前运行的 fresh-start 版本不符合 Director 要求（从失败步骤开始纠正）。应该：
1. Kill 当前进程
2. 用 `test_correction_feasibility_replay.py` 重跑

---
