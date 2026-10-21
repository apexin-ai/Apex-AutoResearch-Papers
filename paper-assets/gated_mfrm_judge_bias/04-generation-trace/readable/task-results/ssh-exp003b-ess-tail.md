# ssh exp003b ess tail

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_exp003b_ess_tail_20260523T134438_result.json`
- **Structured JSON:** [`1e83f868121c405b06ea.json`](../../sessions/1e/1e83f868121c405b06ea.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp-003b ESS_tail 结果

**所有参数 ESS_tail ≥ 100，无警告。**

### Joint GMFRM 模型（主要关注参数）

| 参数 | n | ESS_tail (min/mean/max) | ESS_bulk (min/mean/max) | R-hat |
|------|---|------------------------|------------------------|-------|
| **θ** (judge severity) | 8 | 1884 / 3367 / 4838 | 1536 / 2174 / 3155 | 1.0004–1.0062 |
| **c** (judge contamination) | 8 | 437 / 1392 / 3315 | 217 / 829 / 1463 | 1.0011–1.0266 |
| **d** (threshold) | 9 | 3061 / 4696 / 6858 | 1244 / 3178 / 4311 | 1.0001–1.0027 |
| **σ_c** | scalar | 524 | 227 | 1.0326 |
| **b** (item difficulty) | 176 | 381 / 2044 / 3749 | 317 / 1329 / 2264 | 1.0003–1.0221 |

### 注意点

- **σ_c** 的 ESS_bulk=227 和 R-hat=1.033 是最弱的收敛指标，但仍在可接受范围内（ESS_tail=524 > 400）
- **c[5]** 的 ESS_tail=437 是 c 参数中最低的，ESS_bulk=217
- 所有 R-hat < 1.05，收敛良好

### MFRM-only 模型（对比）

| 参数 | ESS_tail (min/mean/max) |
|------|------------------------|
| θ | 2429 / 2782 / 2999 |
| d | 2331 / 2716 / 2969 |
| b | 1274 / 1751 / 2211 |

JSON 已保存至 `artifacts/exp-003b/ess_tail_report.json`，服务器端 `/root/gated_mfrm_judge_bias/exp003/output_003b/ess_tail_report.json` 含完整逐元素数据。

---
