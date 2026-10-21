# code maniskill3 eval scripts

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_maniskill3-eval-scripts_20260516T032426_result.json`
- **Structured JSON:** [`a4f370db0c4e01a0e2cf.json`](../../sessions/a4/a4f370db0c4e01a0e2cf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个 evaluation 脚本已写入服务器 `/root/autodl-tmp/event-gated-adaptive-horizon/scripts/` 并通过 DMC logdir dry-run 验证：

| 脚本 | 功能 | 验证结果 |
|---|---|---|
| `eval_nve_maniskill.py` | NVE = value_mean / eval_return，标注 >1.5x pathological | baseline walker 33 步中 1 步 pathological (step 78K, NVE=2.73)，008d 3 步中 1 步 |
| `eval_dt_distribution.py` | dt 分布统计 + degeneration 检测 (dt=1 >95%) | baseline 正确跳过（无 gate），008d 显示 fixed dt=2 100% |
| `eval_summary_maniskill.py` | 综合汇总表 (exp_id/task/config/return/NVE/success_rate/dt_dist) | 3 个实验汇总表正确输出，task/config 自动推断 |

所有脚本支持：
- `--logdirs` 多实验对比
- `--output` / `--output-json` / `--output-csv` 持久化
- ManiSkill `success_rate` 字段（多候选名自动匹配）
- tensorboard events fallback（无 metrics.jsonl 时）

---
