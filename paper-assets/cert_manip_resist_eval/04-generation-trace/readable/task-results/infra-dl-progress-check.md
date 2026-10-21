# infra dl progress check

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_dl-progress-check_20260521T204816_result.json`
- **Structured JSON:** [`7fa13fda3e3275b62e7e.json`](../../sessions/7f/7fa13fda3e3275b62e7e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总：

| 模型 | safetensors | 目标 | 状态 | 详情 |
|------|------------|------|------|------|
| **Qwen-72B** | 11/11 | 11 | **完成** | 日志显示 `DOWNLOAD COMPLETE`，总大小 39G |
| **Llama-70B** | 8/9 | 9 | **下载中** | 缺 shard 5，`.incomplete` 文件 2.7G/~4.6G（约 59%），PID 19524 存活 |
| **Mistral-Large** | 13/14 | 14 | **下载中** | 缺 shard 8，`.incomplete` 文件 4.1G/~4.6G（约 89%），PID 19219 存活 |

**进程状态**：
- PID 19519 (Llama bash wrapper) — 存活
- PID 19524 (Llama python 实际下载) — 存活，已运行 ~18 分钟
- PID 19214 (Mistral bash wrapper) — 存活
- PID 19219 (Mistral python 实际下载) — 存活，已运行 ~18 分钟，CPU 7.4%

**预估完成**：
- Mistral shard 8：剩余 ~0.5G，按当前速度约 1-2 分钟内完成
- Llama shard 5：剩余 ~1.9G，约 3-5 分钟完成

**磁盘**：/root/autodl-tmp 250G 已用 174G，剩余 77G，空间充足。

---
