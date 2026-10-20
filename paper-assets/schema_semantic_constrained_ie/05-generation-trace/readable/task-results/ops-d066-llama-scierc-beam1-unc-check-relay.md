# ops d066 llama scierc beam1 unc check relay

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_d066_llama_scierc_beam1_unc_check_relay_20260520T122433_result.json`
- **Structured JSON:** [`17498875b6275cea83c8.json`](../../sessions/17/17498875b6275cea83c8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已开始推理（3 docs written）。

## 报告

| 项目 | 状态 |
|------|------|
| **Llama SciERC beam1 unc** | 完成 ✓ — 275/275 samples, 0 failures, 490KB JSONL |
| **新启动配置** | `llama_docred_200_beam1_unconstrained` — PID 206397, GPU1 |
| **GPU0** | PID 194615 (d065_qwen_greedy_4096_r2), 18910 MiB |
| **GPU1** | PID 206397 (llama_docred_beam1_unc), 18266 MiB |

注意：SciERC 输出 275 行而非预期的 551 行。这可能是 SciERC dev set 在 document-level 有 275 个 doc（每个 doc 多个 sentence 但按 doc 聚合），或 `--max_samples` 等参数导致。需要确认数据集实际大小。

---
