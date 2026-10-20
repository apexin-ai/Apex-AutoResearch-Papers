# knowledge plan registry refresh

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_knowledge_plan_registry_refresh_20260515T193300_result.json`
- **Structured JSON:** [`c3c3f0034e6279a1462b.json`](../../sessions/c3/c3c3f0034e6279a1462b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

映射表已写入 `artifacts/plan_registry_mapping.md` 并注册。

核心发现：

| plan_id | 需更新的 registry_id | 状态 |
|---------|---------------------|------|
| exp-001 | `exp_001_sft_injection` (替换 exp_001_sft_d100_15B_v2) | DONE/success |
| **exp-002** | `exp_002_signals_05B` (新增) | DONE/success |
| **exp-003** | `exp_003_rrf_05B` (新增) | DONE/success |
| exp-004 | `exp_004_sim_sweep_v7` (替换 failed 的 v1) | RUNNING |
| exp-005 | `exp_005_noise_prop_v4` (替换 failed 的 v2) | DONE/negative |
| **exp-006** | `exp_006_irt_05B_gsm8k` (新增) | DONE/success |
| **exp-008** | `exp_008_signal_survival_v4` (新增) | DONE/success |

4 个 plan entry 完全缺失 registry_id（exp-002/003/006/008），2 个指向了 failed 的旧版本（exp-004/005）。更新后 Claim 2 应从 0% 跳到接近完成，Claim 1/3 也会大幅提升。

---
