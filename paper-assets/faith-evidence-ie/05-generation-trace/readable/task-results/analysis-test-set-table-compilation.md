# analysis test set table compilation

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_test_set_table_compilation_20260521T184910_result.json`
- **Structured JSON:** [`ed20bd273a171841c286.json`](../../sessions/ed/ed20bd273a171841c286.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成。Test Set Scaling Table 已写入 memory.md。

### 综合表格

| Scale | SFT test | RSFT test ign_f1 | Dev→Test Gap |
|-------|----------|------------------|-------------|
| 1.7B | ❌ 未开始 | **0.2933** | -21.9pp |
| 4B | 🔄 运行中 | ❌ FAILED | — |
| 8B | 🔄 运行中 | **0.3353** | -20.8pp |
| 14B | 🔄 运行中 | **0.3849** | -20.4pp |
| LLaMA-8B | ❌ 未开始 | **0.3599** | -20.6pp |

### 待提交

| 优先级 | 实验 | 阻塞原因 |
|--------|------|---------|
| P0 | 4B RSFT 重训 + test eval | checkpoint 丢失，retrain 被 killed |
| P1 | 1.7B SFT test | 未开始 |
| P1 | LLaMA SFT test | 未开始 |

关键发现：Dev→Test gap 在所有 scale 上惊人一致（~20-22pp），scaling 排序与 dev 完全一致。4B RSFT 是唯一缺口。

---
