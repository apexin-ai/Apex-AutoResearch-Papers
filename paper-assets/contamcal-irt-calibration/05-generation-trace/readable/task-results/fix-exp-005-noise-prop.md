# fix exp 005 noise prop

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_exp_005_noise_prop_20260515T165937_result.json`
- **Structured JSON:** [`bb59388466d88ef07890.json`](../../sessions/bb/bb59388466d88ef07890.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**exp-005 v4 验证结果：产出完整，实验已完成。**

## 产出完整性

- **25/25 fits 全部完成**，5 σ_e levels × 5 seeds = 25，全部收敛
- 输出文件：`noise_propagation_results.json` (详细) + `noise_propagation_summary.json` (汇总)
- v4 restart log 确认最后 2 个 fits (σ_e=1.0, seeds 45/46) 于 2026-05-14 23:25 完成

## 关键指标摘要

| σ_e | ME CI width | Simple CI width | All Rhat OK | Converged |
|-----|------------|----------------|-------------|-----------|
| 0.1 | 0.0999 ± 0.0010 | 0.1000 ± 0.0011 | Yes | 5/5 |
| 0.3 | 0.0997 ± 0.0011 | 0.1000 ± 0.0012 | Yes | 5/5 |
| 0.5 | 0.0998 ± 0.0011 | 0.0998 ± 0.0013 | Yes | 5/5 |
| 0.7 | 0.0999 ± 0.0012 | 0.0997 ± 0.0013 | Yes | 5/5 |
| 1.0 | 0.1000 ± 0.0012 | 0.0999 ± 0.0013 | Yes | 5/5 |

**单调性检验**：Spearman ρ = 0.4, p = 0.505 → 无显著单调关系

## 结论确认

- **Conclusion: negative** — CI width 对 σ_e 完全不敏感（ME CI 范围仅 0.0997–0.1000，跨 10 倍 noise 水平变化 < 0.03%）
- 符合 Director 决策：降级为 appendix robustness check，"calibrated scores are robust to measurement noise in exposure estimates"
- Checkpoint 状态 DONE/negative 正确

**注意**：Registry 中无 exp-005 条目（仅有 checkpoint 文件）。如需 registry 记录一致性，可补录。

---
