# analysis fixed vs random

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_fixed_vs_random_20260521T040030_result.json`
- **Structured JSON:** [`c921d68be8c646657a66.json`](../../sessions/c9/c921d68be8c646657a66.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果已保存。汇报如下：

---

**Fixed vs Random sensitivity (binary_correct):**

| Scenario | G | Delta% | ΔG vs baseline |
|---|---|---|---|
| all_random (baseline) | 0.6108 | 38.92% | — |
| temperature_fixed | 0.6233 | 36.92% | +0.0125 |
| ordering_fixed | 0.6145 | 38.32% | +0.0037 |
| precision_fixed | 0.6458 | 33.49% | +0.0350 |
| temp_prec_fixed | 0.6595 | 31.54% | +0.0487 |
| three_fixed (temp+ord+prec) | 0.6638 | 30.94% | +0.0530 |

**text_exact_match sensitivity:**

| Scenario | G | Delta% |
|---|---|---|
| all_random | 0.0066 | 99.34% |
| temperature_fixed | 0.0454 | 13.94% |
| temp_prec_fixed | 0.0598 | 10.43% |
| three_fixed | 0.0610 | 10.21% |

---

**Key finding: binary_correct 的 G 系数对 fixed/random 选择不敏感。** 即使最保守场景（temperature + ordering + precision 全部 fixed），G 仅从 0.611 升到 0.664（+0.053），结论不变——item 方差占主导（61.1%），评估可靠性中等偏上。

**text_exact_match 则对 temperature 的 fixed/random 选择极其敏感：** temperature 主效应占 79.7% 总方差。当 temperature 设为 random 时，这巨大方差计入 error term，G 降至 0.007（几乎为零）；设为 fixed 后 G 升至 0.045。但无论哪种假设，text_exact_match 的 G 系数都很低（<0.07），说明该指标本身可靠性差。

这为回应 reviewer 提供了有力论据：**方差分解的实质结论（item 是最大方差源、binary_correct 可靠性远高于 text_exact_match）不随 fixed/random 假设改变。**

---
