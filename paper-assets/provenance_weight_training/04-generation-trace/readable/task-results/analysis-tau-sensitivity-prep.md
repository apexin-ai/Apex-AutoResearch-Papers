# analysis tau sensitivity prep

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_tau_sensitivity_prep_20260515T154552_result.json`
- **Structured JSON:** [`08f4ef8e6e34046685c9.json`](../../sessions/08/08f4ef8e6e34046685c9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本正常工作。τ=0.6 的数据成功读取（PPL=17.681）。τ=0.8 (adaptive_fix_seed42) 训练已完成但还没有 eval_results.json。4 个实验仍在训练。

状态汇总：
- **τ=0.50** — 训练中 (checkpoint-4500/6103)
- **τ=0.60** — eval 已完成，PPL=17.681 ✓
- **τ=0.70** — 训练中 (checkpoint-3000)
- **τ=0.80** — 训练完成，缺 eval（需要跑 eval_perplexity.py）
- **τ=0.90** — 训练中 (checkpoint-2500)
- **τ=0.95** — 训练中 (checkpoint-2000)
- **Uniform baseline** — PPL=17.694（从已有 eval 结果读取）

脚本已就绪，位于 `/root/provenance_weight_training/analysis/tau_sensitivity_analysis.py`。实验完成并跑完 eval 后，直接 `python analysis/tau_sensitivity_analysis.py` 即可生成完整的 sensitivity curve 和统计摘要。

---
