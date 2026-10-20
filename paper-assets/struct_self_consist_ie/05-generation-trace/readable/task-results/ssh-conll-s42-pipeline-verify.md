# ssh conll s42 pipeline verify

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_conll_s42_pipeline_verify_20260521T144628_result.json`
- **Structured JSON:** [`76e5480407752a8e2c2f.json`](../../sessions/76/76e5480407752a8e2c2f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个 seed 的数据完全一致。验证完成。

### CoNLL s42 Pipeline 验证

- **数据源**: 5090-c `output/conll_mf4v2_seed42/samples.jsonl`
- **JSON 结构**: **MF4v2 格式确认**
  - Top-level keys: `['gold', 'greedy', 'id', 'logprobs', 'samples', 'text']`
  - 8 samples/instance，每个 sample 含: `['cumulative_logprob', 'entities', 'events', 'mean_logprob', 'n_tokens', 'relations', 'token_logprobs', 'token_texts']`
- **关键证据**:
  - 有 per-token logprobs (`token_logprobs`, `cumulative_logprob`, `mean_logprob`) ✓
  - N samples = 8 ✓
  - 文件大小 57MB (59,695,496 bytes)，3453 行 ✓
  - report.json 显示 `n_samples=8`, `greedy_f1=0.907`, `verdict=PASS` ✓
- **与 s123/s456 结构一致**: **是**
  - s123: 同结构，3453行，55.8MB
  - s456: 同结构，3453行，55.4MB
  - 三个 seed 的 top-level keys 和 sample keys 完全相同
- **结论**: **数据有效，无需 rerun**。s42 数据确实是 MF4v2 pipeline 输出，结构与 s123/s456 完全一致。

---
