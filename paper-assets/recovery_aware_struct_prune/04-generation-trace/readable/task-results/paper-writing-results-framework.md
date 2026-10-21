# paper writing results framework

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_writing_results-framework_20260515T070336_result.json`
- **Structured JSON:** [`f29b06783a53a43dd248.json`](../../sessions/f2/f29b06783a53a43dd248.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All three table files exist in `paper/tables/`. All `\ref` and `\cite` keys verified against existing labels and bib entries.

**更新摘要：**

**Results** (§4.4)：
- 添加了 `\input` 引用 Table 1 和 Table 2
- Post-prune 段落：RASP 29% vs Standard 1%，解释 RASP 移除 important-but-redundant groups、保护 functionally unique structures
- Recovery pipeline 段落：SFT 后 Standard 64% vs RASP 57%，解释 SFT trajectory imitation 偏好 importance-based selection 导致反超；GRPO 结果 TBD 占位
- Recovery Δ 和 Statistical significance 段落均用 TBD 占位，等 GRPO 完成后填充

**Ablation** (§4.5)：
- 添加了 `\input` 引用 Table 3
- α ablation 框架：解释 α=0 退化为 Standard，α 增大增加 CKA 权重；α=1.0 已有 29% 数据，其余 TBD
- Per-layer capacity floor ablation：τ ∈ {0%, 20%, 40%, 60%} 预留占位

GRPO 结果到位后需更新 6 处 TBD 标记。

---
