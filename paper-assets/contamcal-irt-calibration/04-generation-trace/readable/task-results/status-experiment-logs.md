# status experiment logs

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_status_experiment-logs_20260516T145415_result.json`
- **Structured JSON:** [`3437e87b39206f811801.json`](../../sessions/34/3437e87b39206f811801.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/experiment_logs_loop17.txt`。

**汇总**：

| 实验 | 状态 | 关键发现 |
|------|------|---------|
| D108 MMLU domain gamma N=24 v4 | **FAILED** (CmdStan crash) | 7/7 domain 结果已保存。STEM_Math/Science γ>0 显著，Medical/Humanities/Social_Sciences γ<0 显著，CS_Eng/Business_Law 不显著。Humanities rhat=1.014 未收敛 |
| Pooled IRT RRF N=25 v2 | **COMPLETED** | GSM8K (N=16) 校准有效 (delta_mae=+0.118)；MMLU/ARC (N=8) 用 4PL+γ 过参数化，校准恶化 (违反 C008) |
| 1.5B-Instruct eval | **RUNNING** | mmlu paraphrased 66% |
| 0.5B-Instruct eval | **RUNNING** | mmlu 66%，HF 超时已恢复 |

**需关注**：Pooled IRT 的 MMLU/ARC 仅 N=8 用了 4PL+γ，PPP=0.006/0.000 且 cal_mae > raw_mae，应改用 2PL+γ 或等 0.5B 数据凑到 N≥16。

---
