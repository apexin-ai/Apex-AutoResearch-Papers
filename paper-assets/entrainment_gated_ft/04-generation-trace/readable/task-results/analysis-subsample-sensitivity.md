# analysis subsample sensitivity

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_subsample-sensitivity_20260521T132528_result.json`
- **Structured JSON:** [`d0d246292a20ea6753bd.json`](../../sessions/d0/d0d246292a20ea6753bd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Artifact 已注册。结果摘要：

**CI width at n=100**（对应 COPA 的 N=100）：
| Benchmark | CI width |
|-----------|----------|
| PIQA | 0.130 |
| HellaSwag | 0.140 |
| ARC-Easy | 0.160 |
| LAMBADA | 0.180 |

所有 benchmark 在 n=100 时 CI width 都在 0.13–0.18，远超 0.03 稳定阈值，**COPA (N=100) 排除完全合理**。

**CI width 收敛曲线**（符合 ~1/√n 衰减）：
- n=500 时 CI width ≈ 0.06–0.08
- n=1000 时 CI width ≈ 0.04–0.06
- 仅 HellaSwag (N=10042, width=0.013) 和 LAMBADA (N=5153, width=0.025) 在 full N 时达到 < 0.03
- PIQA (N=1838, width=0.034) 和 ARC-Easy (N=2376, width=0.032) 在 full N 时刚好在阈值边缘

**α 越大需要更多样本**：LAMBADA (α≈0.31) 的 CI width 在每个 n 值下都最宽，因为 variance = α(1-α)/n 在 α 接近 0.5 时更大。

---
