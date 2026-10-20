# infra investigate gpu2 orphan

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_investigate_gpu2_orphan_20260516T002653_result.json`
- **Structured JSON:** [`e9e59370ede9b86877c6.json`](../../sessions/e9/e9e59370ede9b86877c6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

清理完成。汇总：

**PID 276148 身份**：`rsft-ced-s45-r2` 训练进程（PPID 276147），是被 kill 的 `rsft_ced_s45_train_r2` 的子进程残留。没有对应的 tmux session 存活，属于 orphan。

**清理结果**：已成功 kill。

**GPU 当前状态**：
| GPU | 显存占用 | 状态 |
|-----|---------|------|
| 0 | 10,855 / 32,607 MiB | eval_flat_nli_s44 (PID 270467) |
| 1 | 28,341 / 32,607 MiB | rsft_ced_s43_train_r3 (PID 277315) |
| **2** | **0 / 32,607 MiB** | **空闲，可用** |
| 3 | 10,859 / 32,607 MiB | eval_flat_nli_seed45 (PID 272169) |

GPU 2 已完全释放，可以重新提交 CED s45 训练。

---
