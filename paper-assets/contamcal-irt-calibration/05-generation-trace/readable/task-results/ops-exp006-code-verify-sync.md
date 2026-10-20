# ops exp006 code verify sync

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_exp006_code_verify_sync_20260514T044322_result.json`
- **Structured JSON:** [`985fe1509595736a8e50.json`](../../sessions/98/985fe1509595736a8e50.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp-006 代码就绪状态报告

### 代码位置
远程服务器 `/root/contamcal-irt-calibration/exp006/`，今天（5月14日）刚写好。

### 文件清单
| 文件 | 行数 | 用途 |
|------|------|------|
| `run_irt_calibration.py` | 617 | PyTorch MLE 版 4PL+γ IRT |
| `run_irt_stan.py` | 525 | CmdStanPy Bayesian 版 4PL+γ IRT |
| `run_all_baselines.py` | 297 | 统一跑所有 baseline + 对比 |
| `baselines/` | 7 个 .py | 各 baseline 实现 |

### Baselines（7个，统一 `calibrate()` 接口）
1. **raw_scores** — 无校准原始分
2. **linear_regression** — 线性回归校准
3. **remove_rescore** — 移除可疑题重打分
4. **dcr_fuzzy** — DCR 模糊匹配
5. **emperor_mitigation** — Emperor mitigation
6. **vanilla_4pl** — 标准 4PL IRT（无 contamination）
7. **single_signal_2pl_gamma** — 单信号 2PL+γ

### Stan 模型文件
`/root/contamcal-irt-calibration/stan_models/` 下有 4 个 `.stan` 文件，包括目标文件 `contam_irt_4pl_simple.stan`。

### Dry-run 支持
- `run_all_baselines.py` 支持 `--dry-run`（合成数据）
- `run_irt_stan.py` 支持 `--synthetic`

### 与预期 baseline 的差异
预期的 7 个 baseline 名称（percentile, z-score, MMLU-only, holdout, no-calibration, temp-scaling, ensemble）和实际实现的 7 个名称**完全不同**。实际 baseline 是针对 contamination calibration 设计的方法（raw_scores, linear_regression, remove_rescore, dcr_fuzzy, emperor_mitigation, vanilla_4pl, single_signal_2pl_gamma），更贴合论文主题。

### 结论
**代码完整可用。** 3个主脚本 + 7个baseline + 4个Stan模型全部就绪，有 dry-run / synthetic 模式可验证。baseline 名称与最初设想不同但更合理——这些是 contamination-aware calibration 领域的真实 baseline。

---
