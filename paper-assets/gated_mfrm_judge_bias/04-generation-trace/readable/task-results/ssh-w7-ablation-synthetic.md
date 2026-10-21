# ssh w7 ablation synthetic

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_w7_ablation_synthetic_20260522T182720_result.json`
- **Structured JSON:** [`04e98c5e9b83e603d1d4.json`](../../sessions/04/04e98c5e9b83e603d1d4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

W7 ablation 实验在 autodl-8gpu 的 tmux session `w7_ablation` 中持续运行。当前状态：

**已完成结果：**

| Seed | Variant | θ RMSE | c RMSE | Kendall-τ | R-hat | 耗时 |
|------|---------|--------|--------|-----------|-------|------|
| 0 | full_gmfrm | 0.1241 | 0.3505 | 0.9216 | 1.010 | 237s |
| 0 | binary_gating | 0.1397 | 0.6143 | 0.9020 | 1.010 | 406s |
| 0 | no_judge_severity | 0.1197 | 0.3855 | 0.9167 | 1.010 | 238s |
| 0 | staged_estimation | 0.3005 | 1.2038 | 0.8122 | 1.010 | 251s |
| 1 | full_gmfrm | 0.1507 | 0.7356 | 0.9200 | 1.020 | 197s |

**当前进度：** Seed 1 的 binary_gating 正在运行（~7 min/variant）。

**初步观察（2 seeds）：**
- staged_estimation 明显最差：θ RMSE 比 full_gmfrm 高 2.4x，c RMSE 高 3.4x
- binary_gating 对 c 估计较差（c RMSE 0.6143 vs baseline 0.3505）
- no_judge_severity 的 θ RMSE 与 full_gmfrm 相当，c RMSE 略差
- 单 seed ~19 min，20 seeds 预计 ~6.3 小时，有 checkpoint 每 5 seeds 保存

实验在 tmux 中后台运行，不需要持续轮询。等完成或到 checkpoint 时再查看结果。

---
