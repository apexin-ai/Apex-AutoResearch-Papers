# ssh cwm repo best ckpt reeval

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_cwm-repo-best-ckpt-reeval_20260523T111605_result.json`
- **Structured JSON:** [`d5ab4256a42c52f7ba00.json`](../../sessions/d5/d5ab4256a42c52f7ba00.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 eval 都已成功启动并正在推理。

## 汇报

| 项目 | s123 | s456 |
|------|------|------|
| **Checkpoint** | checkpoint-300 (val-best, eval_loss=0.2875) | checkpoint-300 (val-best, eval_loss=0.2769) |
| **路径** | `/root/autodl-tmp/checkpoints_repo_cwm_8b_s123/checkpoint-300` | `/root/autodl-tmp/checkpoints_repo_cwm_8b_s456/checkpoint-300` |
| **GPU** | GPU 0 (RTX 5090, 16.9GB/32.6GB) | GPU 1 (RTX 5090, 16.9GB/32.6GB) |
| **PID** | 278342 | 278740 |

**Eval 配置（与 s42 对齐）：**
- `max_seq_length=2048`, `max_new_tokens=1024`, `batch_size=1`
- Base model: `/root/autodl-tmp/models/Qwen/Qwen3-8B`
- Test data: 9784 instances (`swebench_test.jsonl`)

**GPU 利用率：** GPU 0 48%, GPU 1 49%, 各占 ~17GB 显存，正常。

**预计完成时间：** 每条样本约 30-35 秒（从 log 看），9784 条 ≈ 80-95 小时/GPU。这比预期的 4-6h 慢很多——s42 eval 是多 shard 并行跑的（cwm_8b_ckpt400_test_shard2/3/4 目录可见）。如果需要加速，可以把 GPU 2 也利用上做 shard 分片。

---
