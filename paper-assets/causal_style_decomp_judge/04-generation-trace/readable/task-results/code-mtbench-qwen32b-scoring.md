# code mtbench qwen32b scoring

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_mtbench_qwen32b_scoring_20260521T080440_result.json`
- **Structured JSON:** [`d6d62a7b3e9faa7db8d8.json`](../../sessions/d6/d6d62a7b3e9faa7db8d8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

```
## MT-Bench × Qwen3-32B
Pairs: 73 (NLI>=0.9)
Consistency: 49/73 (67.1%)
BT: P(formal)=71.2% [63.0%, 78.8%], p=0.0001
Likert: ATE=0.301, p=0.0068, d=0.149, tie_rate=60.3%
  mean(formal)=8.38, mean(casual)=8.08
Blindspot: Yes
GEE: Style OR=2.96 [0.90, 9.78] p=0.0753, Orig OR=4.51 [1.34, 15.11] p=0.0147
```

产出文件：
- `data/pairwise_results_mtbench_qwen32b.jsonl` (80 records)
- `data/scored_mtbench_qwen32b.jsonl` (80 records)
- `csd_pipeline/mtbench_qwen32b_scoring.py`

要点：BT 显著偏好 formal（71.2%, p=0.0001），Likert ATE 也显著（+0.30, p=0.007），效应量小（d=0.149）。GEE 中 Style OR=2.96 边际显著（p=0.075），Originality OR=4.51 显著（p=0.015）——说明 Qwen3-32B 在 MT-Bench 上存在 formality blindspot，且对 originality 的偏好比 style 更强。

---
