# ops d013 kill cleanup

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_d013-kill-cleanup_20260514T233425_result.json`
- **Structured JSON:** [`bccebad9513d18de8828.json`](../../sessions/bc/bccebad9513d18de8828.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。汇总：

| 项目 | 状态 |
|------|------|
| GRPO (PID 244606 + 子进程 244611) | 已 kill |
| Baseline eval (PID 239932) | 已 kill |
| GPU0 | 空闲 (0 MiB) |
| GPU1 | 空闲 (0 MiB) |
| 磁盘清理 | recovered_* 已删，数据盘 61G/250G 使用 (25%) |
| Baseline eval 结果 | **不存在**（eval 被 kill 时尚未完成写出） |

数据盘剩余内容：
- `/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B` — 原始模型
- `pruned_rasp_20`, `pruned_rasp_25`, `pruned_standard_20`, `pruned_standard_25` — 剪枝 checkpoint

两块 GPU 已就绪，可以启动 SFT。

---
