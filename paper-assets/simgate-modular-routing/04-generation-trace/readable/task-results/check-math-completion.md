# check math completion

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_math-completion_20260515T075020_result.json`
- **Structured JSON:** [`5457d964b935026b2a50.json`](../../sessions/54/5457d964b935026b2a50.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

## MATH Negative Contrast 实验结果

| 指标 | 值 |
|------|-----|
| **N** | 300 (Level 4: 152, Level 5: 148) |
| **Internal (reasoning)** | **81.7%** [77.3%, 86.0%] |
| **Deterministic (code)** | **76.7%** [72.0%, 81.3%] |
| **差异** | **+5.0%** [+0.7%, +9.3%], **显著** |
| **信号方向** | **反转** — internal > code |

**Contingency**: both correct 215, both wrong 40, only-internal 30, only-code 15
**Labels**: no-preference 266, internal-preferred 25, det-preferred 9
**Filtered** (code path 未实际执行代码): 82/300 (27.3%)

**Level 5 差距更大** (+6.1%) — 越难的题 internal reasoning 优势越明显。

Registry 已更新为 DONE/success，artifact 已注册。vLLM (port 8001, cuda:1) 暂未关闭——有 Llama-3.1-8B 下载正在进行，可能后续还需要。

---
