# ssh urgent 41312 kill restart

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_urgent_41312_kill_restart_20260517T180943_result.json`
- **Structured JSON:** [`f30ce18795d7bb26c88b.json`](../../sessions/f3/f30ce18795d7bb26c88b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个任务都在正常训练。

**最终状态：**

| GPU | PID | 实验 | 状态 |
|-----|-----|------|------|
| cuda:0 | 125995 | uniform_seed42_v2 (eval 已禁用) | 训练中，ETA ~3.6h，~2.15s/it |
| cuda:1 | 115525 | (已有实验) | 训练中 |
| cuda:2 | 115021 | ess_only_seed123 | 训练中 |
| cuda:3 | 125367 | random_reweight_seed456 | 训练中 |

**修复过程：**
- uniform_seed42: kill 旧进程 → 去掉 `--eval_data_path` 禁用 eval（`--eval_strategy` 不被脚本支持，`--eval_steps 999999` 与 `load_best_model_at_end` 冲突）→ 成功启动
- random_reweight_seed456: 清理了 `grid_b0_3_seed456` 的残留 GPU 注册 → 成功提交到 cuda:3
- cuda:2 上跑的是 ess_only_seed123，不是 random_reweight，未动

---
