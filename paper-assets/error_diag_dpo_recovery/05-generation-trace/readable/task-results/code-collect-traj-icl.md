# code collect traj icl

**error diag dpo recovery** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_collect_traj_icl_20260512T173518_result.json`
- **Structured JSON:** [`b86215d4d281b48540e6.json`](../../sessions/b8/b86215d4d281b48540e6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部通过。结果汇总：

### 产出

1. **`src/collect_trajectories_icl.py`** 已写入远程服务器

2. **Dry-run 验证结果**（全部通过）：
   - Expert 数据加载：6 种 task type 共 3119 条（pick_and_place=759, pick_clean_then_place=576, look_at_obj=279, pick_heat_then_place=371, pick_two_obj=662, pick_cool_then_place=472）
   - ICL 示例按 task type 正确抽取（每个任务 2 条同类型示例）
   - Prompt 构造格式正确（instruction → OK → ICL example turns → current task obs）
   - 输出 JSONL 格式验证通过：5 条记录，所有必需字段存在且类型正确

3. **ICL prompt 示例**（task 0, pick_and_place 类型）：
   - turn 0 `[user]`: 系统指令（available actions 等）
   - turn 1 `[assistant]`: "OK"
   - turn 2-59: 2 条 pick_and_place expert 轨迹（共 58 turns），包含完整的 task obs → Thought+Action → Observation 序列直到任务完成
   - turn 60 `[user]`: 当前任务观察

### 与 v5 的关键差异
| | collect_trajectories.py | collect_trajectories_icl.py |
|---|---|---|
| ICL 策略 | 3 个固定类型各取最短 1 条 | 按当前任务类型随机抽 2 条同类型 |
| 模型 | Qwen3-8B + BnB 4bit | Qwen3-14B-AWQ |
| temperature | 0.7 | 0.5 |
| seed | 无 | 有（可复现） |
| dry_run | 无 | 有 |

---
