# eval d063 8b s42 val sweep cuda0

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_d063-8b-s42-val-sweep-cuda0_20260514T204909_result.json`
- **Structured JSON:** [`8afdf7a4b9287dbfa43b.json`](../../sessions/8a/8afdf7a4b9287dbfa43b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**eval 已成功启动并运行。**

## 提交确认

- **exp_id**: `repo-level-cls-8b-s42-ckpt200-val`
- **tmux session**: `repo-level-cls-8b-s42-ckpt200-val`
- **PID**: 290070
- **GPU 0**: 17684MiB / 32607MiB, 51% utilization
- **日志**: `/tmp/cls8b_s42_ckpt200_val5120.log`
- **参数**: `--split val --max_seq_length 5120 --max_new_tokens 512 --batch_size 1 --device cuda:0`
- **运行中**: 60/9335，running_acc=68.3%

## 注意事项
- 首次提交因 **batch_size 默认 16 导致 OOM**，已修复为 `--batch_size 1`
- 预计运行约 26 分钟（参考同配置 val@8192 sweep 的速度）

## 额外发现
在等待 cuda:0 期间发现已有 val@8192 sweep 完成，结果如下：
| Checkpoint | val@8192 accuracy |
|---|---|
| ckpt-200 | 63.52%（低于 majority baseline 75.88%） |
| ckpt-400 | 80.96% |
| ckpt-600 | ~85.0%（刚完成） |

## 后续
ckpt-200 val@5120 完成后，需接着跑 **ckpt-600 val@5120**。ckpt-400 val@5120 已有结果 (80.47%)。

---
