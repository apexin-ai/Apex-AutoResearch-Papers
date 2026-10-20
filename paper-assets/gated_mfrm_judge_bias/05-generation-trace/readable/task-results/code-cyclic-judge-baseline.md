# code cyclic judge baseline

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_cyclic_judge_baseline_20260521T230859_result.json`
- **Structured JSON:** [`903ab7f7486bfed7650d.json`](../../sessions/90/903ab7f7486bfed7650d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证通过。

**结果**:
- 文件: `/root/gated_mfrm_judge_bias/baselines/cyclic_judge.py`，58 行
- `fit_cyclic_judge`: shape (20,), mean=0.000000, std=0.1774
- `fit_cyclic_judge_balanced(k=2)`: shape (20,), mean=0.000000
- RMSE vs raw_avg: cyclic=0.0473, balanced=0.0253（接近但不同，balanced 更接近 raw_avg 符合预期——用了更多 judge 信息）

---
