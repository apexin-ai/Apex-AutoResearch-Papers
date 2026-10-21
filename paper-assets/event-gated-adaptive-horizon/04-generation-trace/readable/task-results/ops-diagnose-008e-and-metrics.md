# ops diagnose 008e and metrics

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_diagnose_008e_and_metrics_20260514T041721_result.json`
- **Structured JSON:** [`0442bef339dbe5fbea0b.json`](../../sessions/04/0442bef339dbe5fbea0b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完毕。

## 008e 诊断

- **PID 121636 状态**：alive（已运行 7h21m）
- **PID 122038 状态**：alive（已运行 6h57m）
- **实际运行命令**：两个完全相同 — `python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008e_subsample_on_fixed_dt1_h15 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 1 --gate_subsample_max_dt 2 --imag_horizon 15`
- **logdir 冲突**：**是** — 两个进程写入同一 logdir，metrics.jsonl 已有重复条目（8 条 step=0 记录），数据已损坏
- **`--gate_dt_embed_dim 0` 是否存在**：**否** — 两个命令都没有
- **代码默认值**：`gate_dt_embed_dim = 32`（configs.yaml:102）
- **GPU 竞争**：两个进程都在 `CUDA_VISIBLE_DEVICES=1`，7 小时才跑到 step=5000，严重竞争
- **建议**：**kill 两个进程，清空 logdir，重新启动**。两个完全相同、写同一 logdir、缺少关键参数、还互相竞争 GPU，全部无效。重启时必须加 `--gate_dt_embed_dim 0`，且只需一个进程。

## 008a 最新指标

- **当前 step**: 68000
- **eval_return 完整轨迹**: 5K→31 | 15K→167 | 25K→231 | 35K→501 | 45K→563 | 55K→488 | **65K→607.98**
- **value_mean @65K**: 226.10
- **actor_loss @65K**: -0.0575
- **value/eval ratio @65K**: 226.10 / 607.98 ≈ **0.372**
- **B/B+ 判断**: eval_return 607.98 **远超 450 阈值 → B+**，且仍在上升

## 008d 最新指标

- **当前 step**: 45000（但最新 eval 只到 35K，45K eval 即将产出）
- **eval_return 轨迹**: 5K→31 | 15K→154 | 25K→167 | **35K→146**
- **value_mean @35K**: 60.20
- **gate_dt_mean @35K**: 2.0（全固定 dt=2，符合预期）
- **value/eval ratio @35K**: 60.20 / 146.34 ≈ **0.411**
- **崩塌确认**: **初步信号有** — eval_return 从 25K 的 167 下降到 35K 的 146（-12.5%），但需等 45K eval 数据确认。如果 45K eval 继续下降（<130），则确认崩塌复现。**待观察**。

---
