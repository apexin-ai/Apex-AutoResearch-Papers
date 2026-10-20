# ops local exp check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_local-exp-check_20260514T121929_result.json`
- **Structured JSON:** [`333d77ed6cd49fd598bc.json`](../../sessions/33/333d77ed6cd49fd598bc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇总

### exp_004_sim_sweep_v2
- **状态**: Running (5h8m)
- **进度**: 3/12 conditions，当前第 3 个 (`auc0.8_n100_prior1.0_binary`) 的 seed 1/10 完成，seed 2 正在跑
- 前 2 个 condition（n=20, n=50）每个约 1.5-2h，当前 n=100 condition 每个 seed ~80min，10 seeds 预计 ~13h
- **ETA**: 日志显示 ETA 15.3h（从 10:15 起算），即大约明天凌晨 ~01:30 完成当前 condition。剩余 9 个 conditions 后面还需很长时间
- **总 ETA**: 粗估剩余 9 个 conditions × ~4-13h/condition，总计还需 **2-4 天**

### exp_005_noise_prop_v3
- **状态**: Running (3h53m)
- **进度**: **11/25 fits** 完成（上次 9/25），当前正在跑第 12 个 fit（σ_e=0.5, seed=43 的 simple model）
- 每个 fit ~35min（与预期一致），每对 (simple + ME) ~35min 共 ~70min/pair
- **ETA**: 剩余 14 fits × ~35min ≈ **8.2h**，预计今天 ~20:30 完成

---
