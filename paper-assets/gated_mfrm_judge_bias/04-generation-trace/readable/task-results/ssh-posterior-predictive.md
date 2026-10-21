# ssh posterior predictive

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_posterior_predictive_20260522T222746_result.json`
- **Structured JSON:** [`287b9e49097ac3f05cf9.json`](../../sessions/28/287b9e49097ac3f05cf9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇报：

- **Predictive samples**: 1000 draws（从 16000 posterior samples 中随机抽取），每 draw 5661 observations → PPC shape `(1000, 5661)`
- **PPC mean win rate**: 0.5934，观测值 0.5987 — 模型拟合良好
- **新 InferenceData 文件**: `/root/gated_mfrm_judge_bias/exp003/output_003b/joint_gmfrm_idata_with_ppc.nc`，35.7 MB，包含 `posterior`, `sample_stats`, `observed_data`, `posterior_predictive` 四个 group
- **PPC 图**: 已保存至 `/root/gated_mfrm_judge_bias/artifacts/exp003b_diagnostics/ppc.pdf`（左：整体 win rate 分布 vs 观测值；右：per-model win rate 95% CI vs 观测值）
- 执行耗时约 5 秒，无错误

---
