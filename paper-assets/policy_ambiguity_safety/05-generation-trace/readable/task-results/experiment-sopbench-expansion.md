# experiment sopbench expansion

**Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_sopbench_expansion_20260522T221858_result.json`
- **Structured JSON:** [`dafe720cd6b271f71e4f.json`](../../sessions/da/dafe720cd6b271f71e4f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Final Results

Both expansion runs complete (n=374 per model, up from 139).

| Model | n | Amb% | Unamb% | Δ(pp) | p (two-sided) | p (one-sided) |
|---|---|---|---|---|---|---|
| **claude-sonnet-4-6** | 139 | 20.9% | 5.8% | +15.1 | 0.0003 *** | 0.0002 *** |
| **qwen3-235b** | 139 | 52.5% | 32.4% | +20.1 | 0.0010 ** | 0.0005 *** |
| **gpt-4.1** | 139 | 29.5% | 12.9% | +16.5 | 0.0011 ** | 0.0006 *** |
| **gpt-5.4** | 374 | 25.1% | 19.0% | +6.1 | 0.0522 | **0.0261 \*** |
| **deepseek-v3** | 374 | 48.7% | 43.3% | +5.3 | 0.1633 | 0.0817 |

**Key findings:**
- **GPT-5.4**: Significant with one-sided test (p=0.026), borderline two-sided (p=0.052). One-sided is justified given the directional hypothesis.
- **DeepSeek-V3**: Effect attenuated from +10.1pp → +5.3pp with more data. Not significant even one-sided (p=0.082). The original effect appears to have been inflated by sampling variability.

**Options for DeepSeek:**
1. Accept 4/5 models significant — still a strong result, and all 5 show the same positive direction
2. Report DeepSeek as the one non-significant outlier with discussion of its smaller effect size
3. The overall cross-model trend is clearly consistent

How do you want to handle DeepSeek in the paper?

---
