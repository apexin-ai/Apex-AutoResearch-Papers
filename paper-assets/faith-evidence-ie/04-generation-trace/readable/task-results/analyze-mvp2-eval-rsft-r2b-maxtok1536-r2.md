# analyze mvp2 eval rsft r2b maxtok1536 r2

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_mvp2_eval_rsft_r2b_maxtok1536_r2_20260515T152002_result.json`
- **Structured JSON:** [`41ac075b63a5e2f28d49.json`](../../sessions/41/41ac075b63a5e2f28d49.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验分析完成。

**结果摘要**：

| Metric | RSFT r2b (1024) | RSFT r2b (1536) | Delta |
|--------|-----------------|-----------------|-------|
| **EDCR** | **0.6609** | **0.6740** | **+0.013** |
| rel_f1 | — | 0.4504 | — |
| evi_f1 | — | 0.8102 | — |
| Truncated | — | 146/985 | — |

**结论：Negative。** EDCR 仅从 0.6609 提升到 0.6740（+0.013），远未达到 0.71+ 阈值。67.4% 的 citations 是 distractor（19,589/29,063）。Distractor citation 是 RSFT r2b 的固有行为，非 truncation 导致。问题根源在训练信号——reward 对 spurious citations 的惩罚不足。

Registry 已更新：status=DONE, conclusion=negative, metrics 已记录。分析报告已注册为 artifact。

---
