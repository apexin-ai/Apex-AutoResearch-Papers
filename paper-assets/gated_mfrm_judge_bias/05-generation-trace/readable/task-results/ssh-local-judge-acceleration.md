# ssh local judge acceleration

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_local-judge-acceleration_20260524T084448_result.json`
- **Structured JSON:** [`c1431f91c839aa13aab0.json`](../../sessions/c1/c1431f91c839aa13aab0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

500 items × 18 models × 2 positions = 18000 records/judge。

Phase 6 结果——当前吞吐 **不足以在 May 26 deadline 前完成**：

| Judge | 重启前 records | workers | 当前 records | records/min | 剩余 | 预估完成时间 |
|-------|-------------|---------|------------|-------------|------|-------------|
| LLaMA-3.3-70B | 1046 | 12 | 1084 | ~6.3 | 16916 | ~45h (1.9d) |
| Qwen2.5-72B | 693 | 12 | 713 | ~3.3 | 17287 | ~87h (3.6d) |
| Mistral-Large-2 | 84 | 12 | 97 | ~2.2 | 17903 | ~136h (5.7d) |

**问题根源**：GPU 是瓶颈，不是 workers。但 vLLM 日志显示 KV cache 利用率极低（LLaMA 7%, Qwen 8%, Mistral 27%），说明 **batch size 太小**。Qwen 之前 16 reqs 时 throughput 是 40 tokens/s，降到 12 reqs 后只有 29 tokens/s。

**建议**：进一步提高 workers 到 32（Mistral）或 48（LLaMA/Qwen）以增加 vLLM batch size，充分利用 GPU。要执行吗？

---
