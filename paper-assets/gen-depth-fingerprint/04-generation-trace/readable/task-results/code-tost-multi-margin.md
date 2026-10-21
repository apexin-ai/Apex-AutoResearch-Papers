# code tost multi margin

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_tost-multi-margin_20260517T144211_result.json`
- **Structured JSON:** [`ce2929444000dd1411d9.json`](../../sessions/ce/ce2929444000dd1411d9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果摘要：

**all_vs_size_matched** (diff = -0.032, Cohen's d = -86.0):
| Margin | Equivalent? |
|--------|------------|
| 1% (0.023) | NO (p=1.00) |
| 2% (0.047) | YES (p<0.001) |
| 3% (0.070) | YES (p<0.001) |
| 5% (0.117) | YES (p<0.001) |

**all_vs_depth01** (diff = -0.052, Cohen's d = -119.7):
| Margin | Equivalent? |
|--------|------------|
| 1% (0.023) | NO (p=1.00) |
| 2% (0.047) | NO (p=1.00) |
| 3% (0.070) | YES (p<0.001) |
| 5% (0.117) | YES (p<0.001) |

size_matched 在 2% margin 即达等价；depth01 需要 3% margin。脚本写入 `tost_multi_margin.py`，结果写入 `results/tost_multi_margin.json`。

---
