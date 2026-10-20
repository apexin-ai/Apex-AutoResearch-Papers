# code plan017 14b rsft s43 ced scoring

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan017_14b_rsft_s43_ced_scoring_20260523T114634_result.json`
- **Structured JSON:** [`2ffa32575183302dc3de.json`](../../sessions/2f/2ffa32575183302dc3de.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成：

- **PID 250046** 在 cuda:1 上运行 CED scoring
- **输入**: `/root/autodl-tmp/rsft_generations_14b_s43/generations.jsonl` (24216 candidates)
- **输出**: `/root/autodl-tmp/rsft_scored_14b_s43/`
- **参数**: 与 s42 一致 — NLI model `cross-encoder/nli-deberta-v3-base`, top_k=1, scoring_mode=ced
- **Registry**: `plan017_14b_rsft_s43_ced_scoring` → RUNNING
- **监控 cron** 已注册，每 3 分钟轮询进度

---
