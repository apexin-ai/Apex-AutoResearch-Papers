# analysis n8 seed123 unified rho

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_n8_seed123_unified_rho_20260515T145640_result.json`
- **Structured JSON:** [`fe257731759d20a1f6af.json`](../../sessions/fe/fe257731759d20a1f6af.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果摘要：

**3 个条目已计算，输出在服务器 `review_round2/n8_seed123_unified_rho.json`**

| 条目 | VC | SJ | FK | EM | LP | auroc_VC | auroc_SJ | auroc_FK | auroc_EM | auroc_LP |
|------|-----|-----|-----|-----|-----|---------|---------|---------|---------|---------|
| llama_conll_n8_s123 | .420 | .431 | .426 | .428 | .307 | .703 | .701 | .699 | .701 | .760 |
| llama_scierc_n8_s123 | .419 | .355 | .290 | .284 | .197 | .672 | .640 | .597 | .603 | .572 |
| qwen_scierc_n8_s123 | .413 | .388 | .263 | .314 | .234 | .690 | .681 | .618 | .644 | .590 |

**seed 稳定性**: llama_conll 所有 ρ 的 seed 间差异 <0.01（高度稳定）。llama_scierc 波动稍大（n=529 小样本效应），但信号排序一致。

**缺失**: qwen_conll_n8_seed123 — 服务器上无 Qwen CoNLL seed123 推理数据（N=16 也不存在）。

---
