# ops step50 eval final collect

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_step50-eval-final-collect_20260516T013626_result.json`
- **Structured JSON:** [`94f8baf2ffd00c4edd56.json`](../../sessions/94/94f8baf2ffd00c4edd56.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 完整摘要

| 指标 | 值 |
|------|-----|
| **Accuracy** | 58.91% (777/1319) |
| **Stderr** | ±1.35% |
| **EOS rate** | 98.10% |
| **Avg length** | 222.1 tokens |
| **Runtime** | 3h 21m |

### 关键对比

| Model | GSM8K Accuracy (N=1319) |
|-------|------------------------|
| Post-SFT Standard | 59.29% |
| Post-GRPO step 50 | 58.91% |
| **Δ(GRPO - SFT)** | **-0.38 pp** |

**结论 (negative)**: Standard GRPO v8 在 step 50（reward peak 附近）未能提升 GSM8K 准确率，反而微降 0.38pp（在 stderr 范围内，统计上无显著差异）。GRPO 阶段对 standard pruned model 的 math reasoning recovery 贡献为零。

Cron 已删除，registry 已更新为 DONE/negative。

---
