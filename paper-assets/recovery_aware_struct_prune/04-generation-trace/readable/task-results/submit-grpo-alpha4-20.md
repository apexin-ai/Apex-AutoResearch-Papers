# submit grpo alpha4 20

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_submit_grpo_alpha4_20_20260521T185824_result.json`
- **Structured JSON:** [`c80c3b4c76693cdbca01.json`](../../sessions/c8/c80c3b4c76693cdbca01.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

进程已启动确认。

**GRPO 训练已提交:**

| 项目 | 值 |
|------|-----|
| exp_id | `grpo_alpha4_20` |
| PID | 406593 |
| 服务器 | westd-29022, cuda:2 |
| model_path | `/root/autodl-tmp/recovery_aware_struct_prune/sft_alpha4_20/` |
| output_dir | `/root/autodl-tmp/recovery_aware_struct_prune/grpo_alpha4_20/` |
| 超参 | 100 steps, lr=1e-6, bs=2×8, DAPO loss, β=0.01, temp=0.4, num_gen=4, adamw_8bit |
| 日志 | `/root/autodl-tmp/recovery_aware_struct_prune/logs/grpo_alpha4_20.log` |
| 预计完成 | ~2-3 小时（约 21:00-22:00 UTC） |

注：`train_grpo_v5.py` 不支持 `--save_only_model` 参数，未添加。

---
