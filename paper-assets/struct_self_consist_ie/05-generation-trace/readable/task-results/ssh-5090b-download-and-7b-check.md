# ssh 5090b download and 7b check

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_5090b-download-and-7b-check_20260520T014245_result.json`
- **Structured JSON:** [`b9465c108dec48a61d0d.json`](../../sessions/b9/b9465c108dec48a61d0d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态总结

**5090-b：Qwen2.5-7B 下载**
- 状态：**仍在下载中**（PID 160848 存活）
- 已下载：8.0G
- 进度：tokenizer 文件（vocab.json, tokenizer_config.json）已完成，模型权重应仍在下载中

**5090-c：7B 训练**
- 状态：**仍在训练中**（PID 71837 存活）
- 进度：**97%**（20017/20590 steps），刚保存了 checkpoint-20000 并删除了旧的 checkpoint-14000
- 速度：~2.7s/it
- 预计剩余：~573 steps × ~2.7s ≈ **~26 分钟**完成训练

训练尚未结束，pipeline 还未进入下一阶段（export/inference）。

---
