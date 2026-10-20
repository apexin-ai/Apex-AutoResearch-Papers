# exp encoder multiseed e5

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_encoder-multiseed-e5_20260514T215404_result.json`
- **Structured JSON:** [`c5d99fa283b84daf59ce.json`](../../sessions/c5/c5d99fa283b84daf59ce.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。E5-large probe 3-seed 训练结果汇总：

| Metric | Seed 42 | Seed 123 | Seed 456 | **Mean ± Std** |
|--------|---------|----------|----------|----------------|
| macro_f1 | 0.9363 | 0.9403 | 0.9378 | **0.9381 ± 0.0020** |
| f1_stag | 0.9067 | 0.9272 | 0.9179 | **0.9173 ± 0.0103** |
| f1_prog | 0.9660 | 0.9534 | 0.9577 | **0.9590 ± 0.0064** |

方差很小（macro_f1 std=0.002），结果稳定。JSON 已保存到服务器和本地 artifacts，并注册为 `art_20260514_1483bf`。

---
