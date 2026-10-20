# analysis lomo 8x5 full

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_lomo_8x5_full_20260522T133021_result.json`
- **Structured JSON:** [`b82cf42fd61f560a1d6e.json`](../../sessions/b8/b82cf42fd61f560a1d6e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

JSON saved successfully (32882 bytes, 5 benchmarks × 8 models = 40 LOMO sub-analyses).

---

## LOMO 8×5 Results Summary

| Benchmark | G_full | Range | SD | CV | max\|ΔG\| | Most Impactful Removal |
|-----------|--------|-------|-----|------|-----------|----------------------|
| MMLU | 0.8962 | 0.0119 | 0.0043 | 0.49% | 0.0193 | InternLM2.5-7B |
| ARC | 0.8917 | 0.0278 | 0.0083 | 0.94% | 0.0256 | Llama-3.1-8B |
| HellaSwag | 0.8716 | 0.0308 | 0.0093 | 1.09% | 0.0280 | Llama-3.1-8B |
| GSM8K | 0.8629 | 0.0341 | 0.0106 | 1.25% | 0.0300 | Gemma-2-9B |
| MATH | 0.8880 | 0.0296 | 0.0105 | 1.20% | 0.0287 | InternLM2.5-7B |

**Global max |ΔG| = 0.0300** (GSM8K, removing Gemma-2-9B)

**Key findings:**
- G_item 在所有 40 个 LOMO 子集中保持 >0.83，最低为 GSM8K 去掉 Gemma-2-9B 时的 0.833
- CV 均 <1.3%，表明 G_item 对模型样本选择高度稳健
- 最大绝对变化 0.030 发生在 GSM8K（数学推理任务模型间差异最大）
- MMLU 最稳定（CV=0.49%），符合 knowledge-testing 类 benchmark 模型间一致性高的预期
- Llama-3.1-8B 和 InternLM2.5-7B 对结果影响最大（各出现 2 次 max），可能因其在某些 benchmark 上的表现极端

结果已保存到 `artifacts/exp004/data/lomo_8x5_full.json`。

---
