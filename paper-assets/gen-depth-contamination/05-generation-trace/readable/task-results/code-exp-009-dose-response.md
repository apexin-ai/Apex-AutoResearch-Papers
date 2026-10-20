# code exp 009 dose response

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_009_dose_response_20260516T221726_result.json`
- **Structured JSON:** [`d5708d260272ef77f731.json`](../../sessions/d5/d5708d260272ef77f731.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 个任务全部正常运行：

| Job | GPU | Ratio | Status |
|-----|-----|-------|--------|
| `exp_009_dose_10pct` | cuda:1 | 10% | 训练中 (seed 0, no_filter, ~1.94 it/s, 348 steps) |
| `exp_009_dose_30pct` | cuda:2 | 30% | 训练中 |
| `exp_009_dose_50pct` | cuda:3 | 50% | 训练中 |

每个 ratio 需要跑 15 个 run（5 seeds × 3 strategies），每个 run 包含 continued pretraining + lm-eval (MMLU/HellaSwag)。预计 wall clock ~5-8h 完成全部。

产出结构：
- 数据: `data/exp_009_dose_response/ratio_{10,30,50}/`
- 结果: `results/exp_009_dose_response/ratio_{10,30,50}/`（含 `statistical_analysis.json`）
- 日志: `logs/exp_009_dose_response_{10,30,50}.log`

---
