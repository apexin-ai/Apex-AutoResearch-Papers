# ops mmlu tau from theta

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_mmlu_tau_from_theta_20260517T105737_result.json`
- **Structured JSON:** [`661a6541f7584f0364db.json`](../../sessions/66/661a6541f7584f0364db.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All computations done. Here's the summary:

## MMLU τ 结果

- **加权平均 θ → τ = 0.6377 (p=0.0061)**
- **简单平均 θ → τ = 0.6377 (p=0.0061)**
- **Pooled θ → τ = 0.6377 (p=0.0061)**
- Raw accuracy → τ = 0.6377 (p=0.0061)

三种方法（加权/简单/pooled）以及 raw accuracy 给出完全相同的 τ。原因：ground truth 实际只有 2 个有效水平（1.5B d000 mean = 0.5854, 3B d000 mean = 0.6310），within-scale 几乎没有 GT 变异。任何正确区分 1.5B/3B 的方法都会产生相同排序。

Ground truth 来源：
- 1.5B d000: `Qwen2.5-1.5B_d000_s42_aligned` (0.5853), `Qwen2.5-1.5B_d000_s123_aligned` (0.5855)
- 3B d000 (IRT 集外参考): `Qwen2.5-3B_d000_s42_a32_aligned` (0.6307), `Qwen2.5-3B_d000_v2_s123_aligned` (0.6314)
- 13 模型中 3B 没有 d000，故用上述 2 个 3B d000 的均值作 counterfactual

## ARC V2PL τ 检查

- **原脚本是否包含 0.5B: 是**（`compute_vanilla_2pl_tau.py` 使用 `scales=['0.5B', '1.5B', '3B']`）
- 原始 τ（含 0.5B, N=27, I=1172 全量 items）: **0.5591**
- 排除 0.5B 后（N=16, I=300 subsampled items）: **τ = 0.5966**
- 差异: +0.0375

注意：N=16 版本使用了 300 subsampled items（vs 原始 1172），所以不完全可比。如需严格对比，需要用 N=16 + 全量 1172 items 重跑 Stan。

---
