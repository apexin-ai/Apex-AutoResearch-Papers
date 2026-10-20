# ops plan006 harvest results

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_plan006-harvest-results_20260515T232524_result.json`
- **Structured JSON:** [`117f85b9f66fb90610aa.json`](../../sessions/11/117f85b9f66fb90610aa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新完成。

**plan-006-paraphrastic** → `conclusion=success`, `status=DONE`

核心数据：

| 指标 | Paraphrastic | Continuation | Delta |
|------|-------------|-------------|-------|
| 3-class F1 | 0.680 ± 0.009 | 0.788 ± 0.006 | **-0.108** |
| Binary F1 | 0.539 ± 0.017 | 0.749 ± 0.011 | -0.210 |
| Cross-transfer | para→cont: 0.155 | cont→para: 0.431 | — |

Spearman 相关方向全面反转（para 正，cont 负），且 cross-transfer 严重不对称。验证了 attractor convergence hypothesis：paraphrastic 链打断了 continuation 链的收敛轨迹，深度信号显著减弱。

---
