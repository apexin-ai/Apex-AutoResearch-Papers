# ops d100 rrf prep

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_d100_rrf_prep_20260516T235745_result.json`
- **Structured JSON:** [`2a6863ea813713002f98.json`](../../sessions/2a/2a6863ea813713002f98.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

**d100 RRF 聚合成功**，两个输出模式均完成：

### 包含的 respondents（7 个）
| Respondent | Benchmarks | 备注 |
|---|---|---|
| Llama-3.2-3B_d100_s42 | ARC + GSM8K + MMLU | MMLU 基于 s1+s2 信号（s4 仍在跑），RRF 用 2/3 信号 |
| Qwen2.5-0.5B_d100_s42 | ARC + GSM8K + MMLU | 完整 3 信号 |
| Qwen2.5-0.5B_d100_s123 | ARC + GSM8K + MMLU | 完整 3 信号 |
| Qwen2.5-1.5B_d100_s42 | ARC + GSM8K + MMLU | 完整 3 信号 |
| Qwen2.5-1.5B_d100_s123 | ARC + GSM8K + MMLU | 完整 3 信号 |
| Qwen2.5-3B_d100_a32_s42 | ARC + GSM8K + MMLU | 完整 3 信号 |
| Qwen2.5-3B_d100_a32_s123 | ARC + GSM8K + MMLU | 完整 3 信号 |

### 产出文件
- `/root/autodl-tmp/exp003/rrf_d100/exposure_scores.json` (3.4 MB)
- `/root/autodl-tmp/exp003/rrf_d100/exposure_aggregated.json` (419 KB)
- `/root/autodl-tmp/exp003/rrf_d100/per_model/rrf_scores_all.csv` (19 MB, 115731 rows)
- `/root/autodl-tmp/exp003/rrf_d100/per_model/rrf_summary.json`
- 21 个 per-model per-benchmark JSON 文件

### 注意
Llama d100 MMLU 的 s4_selfcritique 信号仍在运行中，当前 RRF 结果基于 2/3 信号。完成后可重跑获得完整 3 信号版本。

---
