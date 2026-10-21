# code mistral filter and extract

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_mistral-filter-and-extract_20260516T113839_result.json`
- **Structured JSON:** [`14bf85a3c43826cfef0c.json`](../../sessions/14/14bf85a3c43826cfef0c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务已启动并设置监控。汇总：

**Phase 1 过滤统计（Mistral-7B rp=1.0）**：

| Depth | 原始 | 保留 | 过滤 | 过滤率 |
|-------|------|------|------|--------|
| 0 | 996 | 996 | 0 | 0.0% |
| 1 | 994 | 924 | 70 | 7.0% |
| 2 | 970 | 734 | 236 | 24.3% |
| 3 | 952 | 559 | 393 | 41.3% |
| 4 | 937 | 452 | 485 | 51.8% |
| **Total** | **4849** | **3665** | **1184** | **24.4%** |

**Phase 2 进度**：
- Pythia-410M ✅ 完成（20s）
- OLMo-2-1B 🔄 加载中
- Qwen3-0.6B ⏳ 待执行

**PID**: 303414 | **日志**: `/tmp/mistral_filter_extract.log`

Mistral 退化模式明显——depth 4 过半被过滤，比 Llama 退化更严重。Cron 每 3 分钟检查完成状态。

---
