# exp r15 mf2 claude tost pool

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_r15-mf2-claude-tost-pool_20260523T065139_result.json`
- **Structured JSON:** [`1ee309a7408399f2b822.json`](../../sessions/1e/1ee309a7408399f2b822.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

JSON 已保存。核心结果：

**LLMBar 池化（formality + verbosity 合并）**
- n=174 pairs, BT%=55.17%, SE=0.0377
- **Power at Δ=10pp = 84%** — 超过 80% 阈值，不需要新 API 调用
- 80% power 只需 n=155，现有 174 已充足

**TOST 等价性检验（LLMBar pooled）**
| Margin | p-value | Significant |
|--------|---------|-------------|
| Δ=5pp  | 0.518   | No          |
| Δ=10pp | 0.100   | No          |
| **Δ=12pp** | **0.035** | **Yes** |
| Δ=15pp | 0.005   | Yes         |
| Δ=20pp | <0.001  | Yes         |

**关键发现**：虽然 power 充足（84%），但 TOST 在 Δ=10pp 仍然 p=0.10 未显著——原因是观测到的 BT%=55.2%（偏离 50% 约 5pp），在 10pp 等价区间边界附近。等价性在 **Δ=12pp 处首次确认**（p=0.035）。

跨 benchmark 池化（含 AlpacaEval/MT-Bench）对 TOST 无意义，因为这些 benchmark 存在真实的风格偏差（formality pooled BT%=66%, verbosity pooled BT%=61%）。

---
