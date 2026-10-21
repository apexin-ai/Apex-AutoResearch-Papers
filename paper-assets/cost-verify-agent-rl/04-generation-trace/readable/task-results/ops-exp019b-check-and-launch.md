# ops exp019b check and launch

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_exp019b-check-and-launch_20260514T183544_result.json`
- **Structured JSON:** [`8e97083ae3616258ff16.json`](../../sessions/8e/8e97083ae3616258ff16.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`run_exp019b.sh` 已存在且配置正确：
- base model: `/root/autodl-tmp/checkpoints/exp008_sft/final` ✓
- train data: `/root/autodl-tmp/expert_sft_v3/expert_sft_train.jsonl` ✓
- val data: `/root/autodl-tmp/expert_sft_v3/expert_sft_val.jsonl` ✓
- output: `/root/autodl-tmp/checkpoints/exp019b_expert_sft_v3/` ✓
- log: `/root/runs/cost-verify-agent-rl/exp019b_expert_sft_v3.log` ✓
- LR=5e-6, epochs=2 ✓

---

**报告：**

| 项目 | 状态 |
|------|------|
| **数据收集** | **进行中** — 2200/3553 (62%)，已运行 1h32m |
| **进度详情** | 速率 ~24 tasks/min，剩余 1353 tasks，预计 **~57 分钟后完成**（约 UTC 19:30） |
| **数据质量** | ok=2180 (99%), valid_sft=2061, move_actions=1747 ✓, put_actions=0 ✓, admissible_move=6145 ✓ |
| **训练脚本** | `run_exp019b.sh` 已就绪，路径全部指向 v3 ✓ |
| **GPU** | GPU 0: 0 MiB / 97887 MiB (0%), GPU 1: 0 MiB / 97887 MiB (0%) — 完全空闲 ✓ |
| **可否启动训练** | **否** — 数据收集仍在运行，v3 目录目前为空（数据在进程结束时写入） |

预计数据收集约 57 分钟后完成，届时可直接执行 `bash scripts/run_exp019b.sh` 启动训练。

---
