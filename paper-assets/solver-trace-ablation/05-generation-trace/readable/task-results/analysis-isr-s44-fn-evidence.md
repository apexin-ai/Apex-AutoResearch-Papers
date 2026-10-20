# analysis isr s44 fn evidence

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_isr-s44-fn-evidence_20260515T141051_result.json`
- **Structured JSON:** [`e918881c7ef1ee263b39.json`](../../sessions/e9/e918881c7ef1ee263b39.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文件已保存。结果总结：

**`/root/autodl-tmp/outputs/isr_s44_fn_evidence.json`**

- **数据源**: `/root/runs/solver-trace-ablation/plan002-additive-b01-s44-eval.json`（eval 原始数据仍存在于 runs 目录）
- **89/89 proved 样本全部 n_prem=1**（所有 proved 都是 tautological）
- **77 exact match**（premise == conclusion，原始 H7 检测命中）
- **12 FN**（premise ≠ conclusion，H7 检测遗漏）

12 个 FN 的 mismatch 类型：
| 类型 | 数量 | 说明 |
|------|------|------|
| `vacuous_quantifier_wrapping` | 11 | 模型生成 `∃x(P(x))` 作为 premise，但 conclusion 变成 `∃x(∃y(P(y)))` — 添加冗余量词 + 变量重命名。逻辑等价但文本不同 |
| `structural_simplification` | 1 | folio_304: conclusion 是 premise 的简化子结构 |

这不是简单的 whitespace/case 差异，而是**逻辑等价的结构变体** — 模型在生成 premise 和 conclusion 时使用了略微不同的量词结构，H7 文本匹配器无法识别这种等价性。ISR 也不全是 1.0（多数为 0.8），因为 conclusion 拆分出的 sub-components 中有些因量词差异被标记为 necessary。

---
