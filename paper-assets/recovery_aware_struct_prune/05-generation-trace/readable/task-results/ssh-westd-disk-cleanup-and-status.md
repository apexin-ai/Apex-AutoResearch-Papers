# ssh westd disk cleanup and status

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_westd_disk_cleanup_and_status_20260520T215149_result.json`
- **Structured JSON:** [`4f88507b4d45033905c2.json`](../../sessions/4f/4f88507b4d45033905c2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 清理完成，汇总报告

| 指标 | 清理前 | 清理后 |
|------|--------|--------|
| 磁盘已用 | 578G (94%) | 532G (86%) |
| 可用空间 | **42G** | **88G** |

**清理内容**：删除 7 个 optimizer.pt/scheduler.pt 文件，释放 ~46G（主要来自 3 个 16G/15G 的 optimizer.pt）。

**GPU 进程状态**：
- GPU 0: `eval_gsm8k` CKA-only 15% seed123 运行中
- GPU 1: `eval_gsm8k` CKA-only 15% seed456 运行中
- **GPU 2/3: 空闲**，可用于重跑 Standard 15% seed123/456 GRPO 训练

**未删除**：Standard 15 seed123/456 目录只有 README.md 和 completions（无残留 checkpoint），wandb 无 offline runs。

---
