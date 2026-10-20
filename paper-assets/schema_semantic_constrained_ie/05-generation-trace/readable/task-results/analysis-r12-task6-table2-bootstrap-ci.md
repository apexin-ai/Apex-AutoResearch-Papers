# analysis r12 task6 table2 bootstrap ci

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_r12_task6_table2_bootstrap_ci_20260520T180503_result.json`
- **Structured JSON:** [`39106b7ebc4bb92d3ea3.json`](../../sessions/39/39106b7ebc4bb92d3ea3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。以下是结果总结和论文 caption 文本。

## 结果

**R-F1 差异（constrained − unconstrained）：所有 n.s.**

| Setting | ΔR-F1 (pp) | 95% CI | p |
|---------|-----------|--------|---|
| Qwen SciERC (n=551) | −0.10 | [−0.30, 0.00] | 0.726 |
| Llama SciERC (n=551) | +0.02 | [0.00, +0.07] | 0.736 |
| Qwen DocRED (n=998) | −0.31 | [−0.69, +0.01] | 0.056 |
| Llama DocRED (n=998) | +0.06 | [−0.11, +0.25] | 0.535 |

**DR% 差异：全部 p < 0.001**

| Setting | ΔDR% (pp) | 95% CI | p |
|---------|-----------|--------|---|
| Qwen SciERC | −1.95 | [−2.87, −1.11] | <0.001 |
| Llama SciERC | −1.02 | [−1.98, −0.29] | <0.001 |
| Qwen DocRED | −0.75 | [−1.07, −0.48] | <0.001 |
| Llama DocRED | −0.29 | [−0.53, −0.10] | <0.001 |

**数据验证**：聚合 TP/FP/FN 与 d066_unified eval 完全一致（e.g. Qwen SciERC unc: tp=461, fp=667, fn=513 → R-F1=43.86%）。

## 论文 Caption/Footnote 文本

用于 Table 2 caption（SciERC composability table）：

> Paired bootstrap test (10{,}000 iterations, document-level resampling): $\Delta$R-F1 between constrained and unconstrained decoding is not statistically significant for either model ($p{>}0.5$, two-sided), while DR reduction is significant for both ($p{<}0.001$, one-sided).

如果需要更详细的 footnote（含 DocRED 的扩展版）：

> Bootstrap significance (10{,}000 iterations, document-level resampling, seed=42): No R-F1 difference reaches significance at $\alpha{=}0.05$ (Qwen $\Delta{=}{-}0.10$\,pp, $p{=}0.73$; Llama $\Delta{=}{+}0.02$\,pp, $p{=}0.74$). DR\% reduction is significant in all settings ($p{<}0.001$). On DocRED (998 docs), results are consistent: R-F1 $\Delta$ ranges from $-0.31$ to $+0.06$\,pp (all $p{>}0.05$) while DR\% reduction remains significant.

**文件位置**：
- JSON: `westd-16980:/root/autodl-tmp/schema_outputs/r12_table2_bootstrap_ci.json`
- 脚本: `westd-16980:/root/schema_semantic_constrained_ie/scripts/r12_bootstrap_ci_table2.py`

---
