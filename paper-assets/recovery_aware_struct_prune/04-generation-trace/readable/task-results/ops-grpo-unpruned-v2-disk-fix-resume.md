# ops grpo unpruned v2 disk fix resume

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_grpo-unpruned-v2-disk-fix-resume_20260516T021246_result.json`
- **Structured JSON:** [`a8ef9cd19fd05c5d43d6.json`](../../sessions/a8/a8ef9cd19fd05c5d43d6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

checkpoint-20 完整（model.safetensors + optimizer.pt + scheduler.pt + rng_state.pth + trainer_state.json）。

日志确认 **从 step 21 开始训练**（进度条 `21/100`），resume 成功。

## 汇报

| 项目 | 结果 |
|------|------|
| 清理空间 | 删除 checkpoint-5/10/15/25，释放 ~108G |
| 磁盘状态 | 142G/250G（57%），109G 可用 |
| 脚本修改 | train_grpo_v5.py 添加 `--resume_from_checkpoint` 参数 |
| 恢复训练 | PID 77652，cuda:1（44238 MiB），从 step 20 恢复，当前 step 21/100 |
| save_total_limit | 已改为 3（防止再次磁盘满） |
| eval_sft_unpruned_baseline | 仍在 cuda:0 运行（PID 74134），sft_unpruned_baseline 未删 |

---
