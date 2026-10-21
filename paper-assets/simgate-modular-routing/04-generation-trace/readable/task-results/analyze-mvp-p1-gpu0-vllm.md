# analyze mvp p1 gpu0 vllm

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_mvp-p1-gpu0-vllm_20260513T151639_result.json`
- **Structured JSON:** [`05f91487d01ffc5cad8e.json`](../../sessions/05/05f91487d01ffc5cad8e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## mvp-p1-gpu0-vllm 分析完成

| Task | internal | det | oracle | det−internal | 90% CI |
|------|----------|-----|--------|-------------|--------|
| melt | −54.70 | −14.55 | +2.15 | **+40.15** | [25.0, 60.2] |
| change-state | −54.70 | −14.50 | +0.45 | **+40.20** | [25.0, 60.2] |
| pooled | — | — | — | **+40.17** | [27.6, 52.8] |

**结论: SUCCESS** — 2/2 task types 的 det 显著优于 internal，90% CI 下界均 > 0。

核心发现：det 的优势主要来自避免 −100 惩罚（internal 约 55% episode 超时失败，det 仅 15%），而非绝对得分高。Oracle 分数也很低（0.5~2.2），说明这些 task 本身难度大，收益机制是"少犯错"而非"做得好"。

Registry 已更新为 DONE，report 已写入 memory.md。

---
