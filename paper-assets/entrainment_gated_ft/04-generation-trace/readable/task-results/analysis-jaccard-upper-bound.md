# analysis jaccard upper bound

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_jaccard-upper-bound_20260520T045417_result.json`
- **Structured JSON:** [`7f59db71f60f9770c5c8.json`](../../sessions/7f/7f59db71f60f9770c5c8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。核心结果：

| 指标 | Helped | Hurt |
|------|--------|------|
| **J_obs 范围** | 0.086–0.108 | 0.070–0.116 |
| **J_max 范围** | 0.777–0.988 | 0.642–0.930 |
| **J_null 范围** | 0.042–0.050 | 0.043–0.056 |
| **Normalized ES 范围** | [0.047, 0.081] | [0.031, 0.077] |
| **Mean J_obs/J_max** | — | 11.1% |

**Saturation trend**（mean norm_ES by ratio）:
- Helped: 0.0518 → 0.0573 → 0.0596 → 0.0658（单调递增，CV=0.086）
- Hurt: 0.0512 → 0.0406 → 0.0680 → 0.0617（非单调，CV=0.188）

**J_null 验证**：analytical 与 10k permutation 差异 < 0.0001，验证通过。

**关键论点**：J_obs ~0.09 看似低，但 J_max 受集合大小不对称约束（平均仅 ~0.85），J_null ~0.05。Normalized ES 在所有 ratio 上一致高于 chance，helped set 的 norm_ES 随 attention ratio 单调上升——floor effect 是几何天花板的产物，非信号缺失。

---
