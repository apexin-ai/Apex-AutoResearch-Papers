# analysis prepare result aggregation

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_prepare_result_aggregation_20260515T124004_result.json`
- **Structured JSON:** [`62ad15c11e0a4ef05b89.json`](../../sessions/62/62ad15c11e0a4ef05b89.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本运行正常。结果汇总：

**33 个实验**，25 个有 standalone eval，3 个 fallback（adaptive_fix），5 个无 eval（1 个未启动 + 4 个运行中）。

关键发现：
- **Uniform baseline**: 17.6938 ± 0.0077
- **Grid-best (b=0.5)**: 17.6448 ± 0.0065，三个 seed 一致选中 b=0.5
- **Adaptive**: 17.6389 ± 0.0071，adaptive ratio = 1.119（超过 grid-best）
- **Adaptive_fix**: 缺少 standalone eval（trainer_state fallback ppl≈21.9，不可比）
- **运行中**: ess_only(5500/6103), golden_ratio(5000/6103), nmin1(3500/6103), tau_0.6(4000/6103)

CSV 输出到 `/root/provenance_weight_training/results/summary_table.csv`。adaptive_fix 的 3 个实验需要补跑 standalone eval 才能纳入正式对比。

---
