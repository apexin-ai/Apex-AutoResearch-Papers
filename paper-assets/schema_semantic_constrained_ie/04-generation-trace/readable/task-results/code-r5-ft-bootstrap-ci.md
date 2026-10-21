# code r5 ft bootstrap ci

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_r5_ft_bootstrap_ci_20260517T135402_result.json`
- **Structured JSON:** [`a1ee22bfd5dd11043402.json`](../../sessions/a1/a1ee22bfd5dd11043402.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果摘要：

**R-F1 Bootstrap 结果 (constrained − unconstrained)：**

| Setting | ΔR-F1 | 95% CI | p-value | 显著性 |
|---------|-------|--------|---------|--------|
| Qwen-LoRA-SciERC | −0.10pp | [−0.30, +0.00] | 0.726 | n.s. |
| Qwen-LoRA-DocRED | −0.37pp | [−0.76, −0.05] | 0.014 | * |
| Llama-LoRA-SciERC | +0.02pp | [+0.00, +0.07] | 0.736 | n.s. |
| Llama-LoRA-DocRED | +0.02pp | [−0.15, +0.22] | 0.851 | n.s. |

**核心结论：** 3/4 settings 无显著差异（p>0.7），Qwen-DocRED 有微弱负效应（−0.37pp, p=0.014）。Fine-tuning 后模型已内化 schema 遵从，constrained decoding 基本无额外收益。

论文建议表述：
> In the fine-tuning regime, the effect of constrained decoding is negligible: across four LoRA settings, three show no significant R-F1 difference ($p{>}0.70$), while one (Qwen-DocRED) exhibits a small negative effect ($-0.37$\,pp, $p{=}0.014$, 95\% CI [$-0.76$, $-0.05$]).

产出已注册至 `artifacts/_project/report/r5_ft_bootstrap_results.md`。

---
