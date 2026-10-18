# fix experiments tex consistency

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_experiments-tex-consistency_20260519T183051_result.json`
- **Structured JSON:** [`9cca15d8194398e04e3b.json`](../../sessions/9c/9cca15d8194398e04e3b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。修改清单：

**修复 1（§4.2 σ 表述，第 47 行）：**
- `Overall $\sigma$ drops 56\%, but the trajectory is non-monotonic: a rebound at the h3-1 configuration means the highest-attention model does not achieve the lowest cross-architecture variance.`
→ `$\sigma$ reaches a maximum reduction of 56\% at intermediate attention ratios, but rebounds at h3-1, yielding a net endpoint reduction of 39\%: the trajectory is non-monotonic, and the highest-attention model does not achieve the lowest cross-architecture variance.`

**修复 2（p-value 前导零，6 处）：**

| 行 | 原文 | 修改后 |
|---|---|---|
| 9 | `$p = 0.017$` | `$p = .017$` |
| 9 | `$p = 0.100$` | `$p = .100$` |
| 11 | `$p \geq 0.233$` | `$p \geq .233$` |
| 57 | `$p = 0.0005$` | `$p = .0005$` |
| 57 | `$p = 0.020$` | `$p = .020$` |
| 86 | `$p = 0.233$` | `$p = .233$` |

---
