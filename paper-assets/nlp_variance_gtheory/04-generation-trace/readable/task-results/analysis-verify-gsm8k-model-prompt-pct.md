# analysis verify gsm8k model prompt pct

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_verify_gsm8k_model_prompt_pct_20260522T012212_result.json`
- **Structured JSON:** [`d0f1fde223f08fde49f1.json`](../../sessions/d0/d0f1fde223f08fde49f1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Confirmed. Both JSON files show GSM8K `model:prompt_template` = **8.5311%**. Here's the full analysis:

## 各文件中 GSM8K model:prompt_template 的值

| 来源 | 值 | 一致性 |
|------|------|--------|
| `per_benchmark_gstudy_ff.json` | **8.5311%** (estimate 0.021308241) | 权威数据 |
| `three_in_one_8model.json` | **8.5311%** (same estimate) | 一致 |
| `ff_gstudy_8model_results.md` | **8.53%** [7.56, 9.75] | 一致 |
| `docs/paper/experiments.tex` (Table 1 + 正文) | **12.9%** | **错误** |

## 差异原因

论文 `experiments.tex:73` 的 GSM 列存在数值错误。验证方法——论文表格 GSM 列求和：

```
16.9 + 14.6 + 10.7 + 5.0 + 12.9 + 39.9 = 100.0  (无空间给 "all others")
```

但实际 JSON 中"all others"约 **4.0%**（主要是 prompt_template:item_id = 3.06%、temperature:item_id = 0.60%）。论文错误地将这些成分吸收进了 model:prompt_template，导致从 8.5% 膨胀到 12.9%。同时 prompt 也从 5.4% 被压低到 5.0%。

## 最终权威值

- **model:prompt_template = 8.53%**
- Bootstrap 95% CI: **[7.56%, 9.75%]**（mean 8.65%，1000 resamples）
- Estimate: 0.021308241，total variance 0.2497718596

论文 `experiments.tex` 第 56 行和第 73 行需要修正：12.9% → 8.5%，prompt 5.0% → 5.4%，"all others" <1.0% → ~4.0%。

---
