# ssh cls14b restart and f1fix

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_cls14b-restart-and-f1fix_20260522T203135_result.json`
- **Structured JSON:** [`c123049ea907dff581d0.json`](../../sessions/c1/c123049ea907dff581d0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部确认完毕。

**任务 1 - CLS 14B 训练**：已启动并正在训练
- GPU 0：14196MiB, 86% 利用率, PID 212100
- 训练参数：trainable 20.9M / 14.8B (0.14%), 6384 steps, `--no_wandb`

**任务 2 - F1 macro bug**：
- 脚本 bug 已修复（第 257 行 `f1_macro+100` → `f1_macro*100`）
- 结果文件中的值本身正确（0shot: 64.0, 3shot: 72.79），无需重跑
- Registry `14b-baseline-0shot-3shot-v2` 已补充 `f1_macro` 字段

**GPU 状态**：
- GPU 0：CLS 14B 训练中 (501W, 86%)
- GPU 2：CWM 14B 训练中 (374W, 64%)
- GPU 1/3：空闲

---
