# analysis sft tax cross family

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_sft-tax-cross-family_20260522T122621_result.json`
- **Structured JSON:** [`fe44c76d212ac9085aac.json`](../../sessions/fe/fe44c76d212ac9085aac.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成。`artifacts/sft_tax_analysis.md` (art_20260522_942dfa)

核心结果：

| Model | Pre-training | d000 Post-SFT | SFT Tax |
|---|---|---|---|
| Phi-4 14.7B | 84.8% | 76.44% | +8.36 pp |
| Qwen2.5-14B | 79.7% | 69.44% | +10.26 pp |
| Qwen2.5-7B | 74.2% | 66.11% | +8.09 pp |
| Gemma-2 9B | 71.3% | 61.86% | +9.44 pp |
| Falcon3-7B-Base | 67.4% | 58.77% | +8.63 pp |
| LLaMA-3.1 8B | 66.7% | 53.50% | +13.20 pp |
| OLMo-2 7B | 63.7% | 53.79% | +9.91 pp |

**Mean tax = 9.70 pp**。所有家族 SFT 后 MMLU 一致下降。LLaMA-3.1 是离群值 (13.2pp)。SFT tax 大小与 contamination pattern 无相关性。

---
