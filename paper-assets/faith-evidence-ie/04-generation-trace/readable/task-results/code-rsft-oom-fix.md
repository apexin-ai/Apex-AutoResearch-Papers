# code rsft oom fix

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_rsft-oom-fix_20260515T000325_result.json`
- **Structured JSON:** [`bde44918b2f50c862fa8.json`](../../sessions/bd/bde44918b2f50c862fa8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个修复均已完成并验证通过：

**修复 1** — `rsft_generate.py`: `--batch_size` 默认值从 2 → 1。降低并发序列数（1×8=8），避免 RTX 5090 32GB OOM。

**修复 2** — `rsft_score_filter.py`: 新增三个 CLI 参数 `--format_weight`(0.2) / `--f1_weight`(0.4) / `--ced_weight`(0.4)，`combined_score` 计算已改用参数值替代硬编码。

---
