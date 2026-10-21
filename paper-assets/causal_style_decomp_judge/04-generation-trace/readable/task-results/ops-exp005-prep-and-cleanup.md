# ops exp005 prep and cleanup

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_exp005_prep_and_cleanup_20260520T224212_result.json`
- **Structured JSON:** [`d47a2b33bc06349a88b4.json`](../../sessions/d4/d47a2b33bc06349a88b4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

### 任务 A: exp-005 RATE control 数据

- `verified_32b.jsonl`: 100 条，全部有 `double_rewrite_text`
- Formality 分布: formal=59, casual=41
- NLI CF >= 0.90 过滤后: **88 条**
- `data/rate_control_input.jsonl` 已生成，88 条记录
  - NLI DR: mean=0.9185, min=0.0030, max=0.9990
  - BERTScore DR: mean=0.8645, min=0.5956, max=1.0000
  - Formality: formal=50, casual=38

注意：NLI DR 有个别极低值（min=0.003），这些 double_rewrite 与 original 语义一致性较差，RATE control 实验中可能需要额外过滤。

### 任务 B: 清理确认

- `scored_verbosity.jsonl`: 原 100 条**全部** null scores（比预期的 7 条多），已清空为 0 行
- `pairwise_verbosity.jsonl`: 文件不存在，无需清理

---
