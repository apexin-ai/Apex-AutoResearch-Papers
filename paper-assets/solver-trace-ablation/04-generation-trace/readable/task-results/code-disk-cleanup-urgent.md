# code disk cleanup urgent

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_disk-cleanup-urgent_20260519T170744_result.json`
- **Structured JSON:** [`61c855694ef67ff4244c.json`](../../sessions/61/61c855694ef67ff4244c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

清理完成。

**清理报告：**

| 指标 | 清理前 | 清理后 |
|------|--------|--------|
| 已用 | 30G (100%) | 9.1G (31%) |
| 可用 | 680K | **21G** |

**删除内容：**
- `/tmp/d146_dryrun` — 20G（dry run 模型权重 + checkpoint-1，已完成的测试产物）
- `/root/.cache/huggingface/datasets` — ~1.1G（HF 数据集缓存）
- `/tmp` 旧日志/脚本/临时文件 — ~3M

**未删除：** `/root/solver-trace-ablation/`、`/root/autodl-tmp/` 下所有内容完整保留。D146 训练不受影响。

---
