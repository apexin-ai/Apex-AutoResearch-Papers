# exec v3 collect trajectories

**error diag dpo recovery** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exec_v3-collect-trajectories_20260512T153610_result.json`
- **Structured JSON:** [`979996863f7a86e67a7b.json`](../../sessions/97/979996863f7a86e67a7b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务已完成。汇总：

**修改内容** (`src/collect_trajectories.py`):
1. 移植 `translate_action()` — 从 `test_icl_14b.py` 复制，含 put→move、clean→wash、heat→cook、fuzzy match 等映射
2. env generator 现在 yield `admissible_commands`
3. `collect_single_trajectory()` 在 `env.step()` 前翻译 action，每步更新 admissible

**验证结果**: 2/5 = 40% 成功率（之前 0/89 = 0%），translate_action 生效（task 2 触发 18 次翻译, task 3 触发 4 次）

**后台任务**:
- screen session: `traj_v3` (PID 230943)
- 目标: 250 条轨迹
- 输出: `data/trajectories_v3/train.jsonl`
- 日志: `data/trajectories_v3/collect.log`
- 预计耗时: ~250 × 70s ≈ 5 小时
- 监控: `screen -ls` / `grep "INFO" data/trajectories_v3/collect.log` / `wc -l data/trajectories_v3/train.jsonl`

---
