# code direction aware vs strict gate

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_direction_aware_vs_strict_gate_20260521T095946_result.json`
- **Structured JSON:** [`09a949a3f565e57b496d.json`](../../sessions/09/09a949a3f565e57b496d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Results:

### FORMALITY
| Gate | n pairs | BT P(formal) | 95% CI | p |
|------|---------|---------------|--------|---|
| Strict bidir | 88 | 0.6647 | [0.5852, 0.7386] | < 0.0001 |
| Direction-aware (max) | 97 | 0.6340 | [0.5567, 0.7061] | 0.0001 |
| Extra only (9) | 9 | 0.3337 | [0.1120, 0.6109] | — |

**Difference**: Δ = −0.0307, CI [−0.0651, −0.0018] → CI 不含 0，**有差异**。9 个 extra pairs 倾向 casual (P(formal)=0.33)，拉低了 DA 估计。但注意：formality 当前 pipeline 实际用的是 min(fwd,bwd)（即 strict），max(fwd,bwd) 只是假设性对比。

### VERBOSITY
| Gate | n pairs | BT P(verbose) | 95% CI | p |
|------|---------|---------------|--------|---|
| Strict bidir | 65 | 0.7845 | [0.7076, 0.8537] | < 0.0001 |
| Direction-aware | 86 | 0.7732 | [0.7034, 0.8429] | < 0.0001 |
| Extra only (21) | 21 | 0.7379 | [0.5714, 0.8806] | — |

**Difference**: Δ = −0.0113, CI [−0.0564, +0.0296] → CI 含 0，**无显著差异**。21 个 extra pairs 的 BT (0.7379) 与整体方向一致。

### 核心结论
- **Verbosity**（R3-W2 关注的核心）：direction-aware gate 额外纳入的 21 pairs (21%) **不引入系统偏差**，BT 估计无显著变化
- **Formality**：pipeline 已用 strict bidir (min)，无额外 pairs 问题。假设性 max(fwd,bwd) 对比表明 formality 确实需要 strict gate
- 脚本: `csd_pipeline/gate_comparison_bt.py`（已部署到服务器）

---
