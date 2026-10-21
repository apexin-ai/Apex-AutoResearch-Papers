# ops fp16 download check

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fp16-download-check_20260525T160251_result.json`
- **Structured JSON:** [`aaa7d1593dedb0dc348f.json`](../../sessions/aa/aaa7d1593dedb0dc348f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 下载状态报告

| 模型 | 状态 | Shards | 大小 | 备注 |
|------|------|--------|------|------|
| **Qwen2.5-14B-Instruct FP16** | ✅ Complete | 8/8 | 28GB | 日志报错 3 shards 失败（temp 路径问题），但后续自动重试成功——失败 shards 的时间戳(23:13/23:17)晚于错误时间(19:10) |
| **Qwen2.5-32B-Instruct FP16** | ✅ Complete | 17/17 | 60GB | 日志截断在 51-64% 进度处，但进程已结束，所有 shards 均已落盘 |
| **Llama-3.1-8B-Instruct FP16** | ✅ Complete | 4/4 | 30GB | 无日志文件（可能命名不同），文件完整 |
| **Qwen2.5-14B-Instruct-AWQ** | ✅ Complete | 3/3 | 9.4GB | — |
| **Qwen2.5-32B-Instruct-AWQ** | ✅ Complete | 5/5 | 19GB | — |
| **Llama-3.1-8B-Instruct-AWQ-INT4** | ✅ Complete | 2/2 | 5.4GB | — |

**存储路径**: `/root/autodl-tmp/modelscope_cache/` (非 `/root/autodl-tmp/models/`)

**磁盘**: 250GB 总量，154GB 已用，**97GB 可用 (38%)**

**下载进程**: 全部已结束，无残留 Python 进程。

所有 6 个模型（3 FP16 + 3 AWQ）已就绪，可以开始 FP16 vs AWQ 精度对比实验。

---
