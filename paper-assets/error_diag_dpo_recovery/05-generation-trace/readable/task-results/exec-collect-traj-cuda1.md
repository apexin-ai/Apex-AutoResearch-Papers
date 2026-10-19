# exec collect traj cuda1

**error diag dpo recovery** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exec_collect-traj-cuda1_20260512T162449_result.json`
- **Structured JSON:** [`77f08ab54dd414b359a0.json`](../../sessions/77/77f08ab54dd414b359a0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务已提交并运行中。汇报如下：

**实验 `datagen_traj_v4_cuda1` 已启动**

| 项目 | 详情 |
|------|------|
| PID | 253522 |
| GPU | cuda:1 (RTX 4090 D, 24GB)，当前占用 ~7.7GB |
| 脚本 | `src/collect_trajectories.py`（含 episode boundary fix，line 340 "Your task is to:" 检测） |
| 模型 | Qwen3-8B (`/root/autodl-tmp/.hf_cache/Qwen3-8B`) |
| 参数 | `--temperature 0.7 --max_steps 40 --num_tasks 250` |
| 输出 | `data/trajectories_v4_cuda1/train.jsonl` |
| 日志 | `/tmp/collect_traj_v4_cuda1.log` |
| 状态 | 模型已加载，环境已初始化，正在收集轨迹 |

按 8B 模型在 ALFWorld 约 30-40% 成功率估算，250 个 task 预期产出 150-175 条 failure 轨迹，满足 125+ 目标。

监控命令：`tail -20 /tmp/collect_traj_v4_cuda1.log`

---
