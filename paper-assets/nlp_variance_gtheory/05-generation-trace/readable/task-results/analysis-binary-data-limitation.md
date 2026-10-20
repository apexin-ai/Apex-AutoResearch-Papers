# analysis binary data limitation

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_binary_data_limitation_20260521T040145_result.json`
- **Structured JSON:** [`fa1c56c5f4fdc5f759cc.json`](../../sessions/fa/fa1c56c5f4fdc5f759cc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Binary data limitation analysis:
- Item difficulty: mean=0.68, std=0.37, range [0.00, 1.00]
- Bernoulli vs observed: Pearson r=1.0000, Spearman ρ=0.9999
- Variance ratio (obs/Bernoulli): mean=1.0008, median=1.0008 — 0/200 items超出±10%，observed variance 完全等于 Bernoulli p(1-p)
- Null simulation: expected item_id=0.08%, observed=61.08%, ratio=737.5x
- text_exact_match 对比: item_id 仅解释 0.66% vs binary 的 61.08%（差 60.42pp）
- Conclusion: item_id dominance **is not** a Bernoulli artifact — null 下 item_id 仅贡献 0.08%，观测值是 737.5 倍。61% 的 item_id 方差反映的是真实的 item difficulty 差异（p_i 从 0.001 到 1.0，std=0.37），而非 Bernoulli 数据的固有膨胀。但 observed var ≈ Bernoulli var（ratio=1.0008）说明 item 内部几乎无 excess variance，即 prompt/seed 等因素对同一 item 的扰动极小。

---
