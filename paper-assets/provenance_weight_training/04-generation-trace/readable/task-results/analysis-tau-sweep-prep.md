# analysis tau sweep prep

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_tau_sweep_prep_20260515T170222_result.json`
- **Structured JSON:** [`cd05c6971f18f68423b9.json`](../../sessions/cd/cd05c6971f18f68423b9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本部署完成，dry-run 验证通过。

**产出文件：**
- 脚本：`/root/provenance_weight_training/analysis/tau_sweep_analysis.py`
- 图表：`analysis/figures/tau_ppl_curve.{pdf,png}` + `tau_b_strength.{pdf,png}`
- CSV：`analysis/tau_sweep_summary.csv`
- JSON：`analysis/tau_sweep_full_summary.json`

**当前状态（3/6 有 PPL）：**
- 3 个已完成实验正常出图和统计
- 3 个 RUNNING 实验的 b* 统计已可用（从 step_metrics.jsonl），PPL 待 eval
- Claim 3 判定为 PARTIALLY SUPPORTED，等剩余 3 个实验 eval 后自动完成验证

**注意 τ=0.80 (adaptive_fix_seed42) b* 分布异常：** 49.9% zero、median 仅 0.069，远低于 τ=0.70 和 τ=0.90 的值，可能是该实验的 step_metrics 包含了更多数据（51913 行 vs 其他 ~24k），步数或 batch 记录方式不同。实验全部完成后 rerun 一次即可得到完整结果。

---
