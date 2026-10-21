# eval cls8b s42 ckpt1000 test mutation

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_cls8b-s42-ckpt1000-test-mutation_20260516T005219_result.json`
- **Structured JSON:** [`4dee0e66608f24300300.json`](../../sessions/4d/4dee0e66608f24300300.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已提交并运行。

**汇报：**

| 项目 | 值 |
|------|-----|
| **exp_id** | `cls8b-s42-ckpt1000-test-mutation` |
| **PID** | 444497 |
| **GPU** | cuda:0 (RTX 5090, 空闲) |
| **Checkpoint** | `/root/autodl-tmp/checkpoints_repo_cls_8b_s42_resume/checkpoint-1000/` |
| **输出目录** | `/root/autodl-tmp/eval_results/cls8b_s42_ckpt1000_test_mutation/` |
| **日志** | `/root/autodl-tmp/eval_results/cls8b_s42_ckpt1000_test_mutation/run.log` |
| **状态** | RUNNING，模型已加载，推理进行中 |

**注意：** 指定的 checkpoint 路径 `checkpoints_repo_cls_8b_conda/checkpoint-1000` 不存在（该目录只到 step 600）。实际使用的是 `checkpoints_repo_cls_8b_s42_resume/checkpoint-1000`——s42 原始训练中断后 resume 继续的 step 1000。

流程：eval_repo_cls.py 完成后自动执行 mutation_breakdown 脚本，结果写入 `mutation_breakdown.json`。

---
