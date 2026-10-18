# infra check all models

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_check-all-models_20260521T202507_result.json`
- **Structured JSON:** [`60bdb9765c05722971dc.json`](../../sessions/60/60bdb9765c05722971dc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**无下载进程在运行。** 3 个模型有未完成的分片（在 `._____temp/` 目录中，说明下载中断了）。

## 汇总

| 模型 | 状态 | 分片 | 已完成大小 | 问题 |
|------|------|------|-----------|------|
| Qwen2.5-72B-Instruct-AWQ | **不完整** | 7/11 | ~24.5G | 分片 1,3,7,8 在 `._____temp/`（~9.8G 未移入） |
| Qwen2.5-32B-Instruct-AWQ | **完整** ✓ | 5/5 | ~21.2G | — |
| Qwen2.5-14B-Instruct-AWQ | **完整** ✓ | 3/3 | ~9.4G | — |
| Llama-3.1-70B-Instruct-AWQ | **不完整** | 8/9 | ~33.0G | 分片 5 在 `._____temp/`（1.3G 未移入） |
| Llama-3.1-8B-Instruct-AWQ | **完整** ✓ | 2/2 | ~5.4G | — |
| Mistral-Large-Instruct-2407-AWQ | **不完整** | 13/14 | ~57.4G | 分片 8 在 `._____temp/`（1.6G 未移入） |

**磁盘**: 250G 已用 161G，剩余 90G。

**结论**：3 个小模型（Qwen 14B/32B、Llama 8B）完整。3 个大模型（Qwen 72B、Llama 70B、Mistral Large）下载中断，无进程在跑，需要恢复下载。`._____temp/` 中的文件是 ModelScope 下载的临时文件，说明这些分片下载未完成就断了。

---
