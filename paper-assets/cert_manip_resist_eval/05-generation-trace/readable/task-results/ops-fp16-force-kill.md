# ops fp16 force kill

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fp16-force-kill_20260525T105309_result.json`
- **Structured JSON:** [`94bf0a5b26afce05d2a3.json`](../../sessions/94/94bf0a5b26afce05d2a3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 强杀结果
5 个目标 PID (80811, 80914, 81028, 81180, 9804) 全部已消失，无残留非论文进程。

## 清理结果
7 项全部清理成功。磁盘可用: **80GB** (250GB 用了 69%)

## 论文模型状态

| 模型 | FP16 | AWQ | 下载中? |
|------|------|-----|--------|
| Qwen2.5-14B | 6/8 shards | ✅ 3/3 完整 | PID 75403, 80517 |
| Qwen2.5-32B | 15/17 shards | ✅ 5/5 完整 | PID 10163, 72654, 73012, 80611 |
| Llama-3.1-8B | ✅ 4/4 完整 | 1/2 shards | PID 78663, 78822, 79148, 80704 |

⚠️ 注意：每个下载中的模型都有多个重复下载进程（32B FP16 有 4 个，8B AWQ 有 4 个，14B FP16 有 2 个）。这些重复进程会互相竞争带宽，需要的话可以杀掉多余的只保留各一个。

---
