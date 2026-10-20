# analysis discriminative rate full

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_discriminative-rate-full_20260518T035020_result.json`
- **Structured JSON:** [`cc29fea2d7e925a3ab14.json`](../../sessions/cc/cc29fea2d7e925a3ab14.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。核心结果：

**Full dataset: 804 problems (307 multi-candidate)**

| Metric | Overall | ProofWriter | FOLIO |
|--------|---------|-------------|-------|
| Source-trace disc (domain, weight) | 38.6% [38.0, 39.1] | 35.8% | 53.1% |
| Z3 semantic disc | 8.2% [7.6, 8.8] | 8.3% | 7.8% |
| Problems with disc weight | 284/307 (92.5%) | 217/235 | 67/72 |

**Pilot validation**
- Pilot k=20 exact weight rate: 37.2% (matches original report)
- Pilot subset k=12 algebraic: 37.0%
- Full 804 algebraic: 38.6%

Pilot 37.2% → full 38.6%，高度一致。

**关键数字解读**
- **Source-trace disc (38.6%)**: ~61% 的 constraint 权重是跨答案共享的 domain facts，只有 38.6% 绑定到单一答案
- **Z3 semantic disc (8.2%)**: 只有 answer assertion constraints（642/7844）含 answer-dependent 变量；92% 的约束对任何候选答案语义等价 → 直接回应 W1 confound
- FOLIO disc rate 显著高于 ProofWriter (53.1% vs 35.8%)

**方法说明**
- Full dataset 的 per-trace constraint 文本未持久化（`raw_constraints` 为空），weight-based rate 通过 `D_w = 2*TW - Σ(sica_scores)` 从 scorer 输出代数推导
- Pilot 43 题作为 ground truth 验证代数方法（差距仅 0.2pp）

结果 JSON 已保存到 `/root/symb_invariant_consensus/results/discriminative_rate_analysis.json`，脚本在 `/root/symb_invariant_consensus/scripts/analyze_discriminative_rate.py`。

---
