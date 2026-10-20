# check data scaling v2

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_data-scaling-v2_20260514T145800_result.json`
- **Structured JSON:** [`1c439c9b4a862cf9dbf0.json`](../../sessions/1c/1c439c9b4a862cf9dbf0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

data-scaling-v2 实验成功完成，已注册到 registry (DONE/success)。

**数据缩放结果摘要（Test set, macro_f1）：**

| Ratio | Instances | Windows | Test macro_F1 | Test Acc |
|-------|-----------|---------|---------------|----------|
| 10%   | 138       | 1,107   | 0.8054        | 0.8514   |
| 25%   | 346       | 2,749   | 0.8203        | 0.8640   |
| 50%   | 693       | 5,715   | 0.8715        | 0.9030   |
| 100%  | 1,386     | 10,634  | **0.9055**    | **0.9282** |

缩放趋势清晰：数据量从 10%→100%，macro_F1 从 0.805→0.906，stagnation 类的 F1 提升最大（0.711→0.859），progress 类始终较高（0.90→0.95）。50%→100% 仍有显著提升，未出现饱和。

---
