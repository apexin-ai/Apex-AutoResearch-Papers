# code exp006 irt prep

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp006_irt_prep_20260516T021052_result.json`
- **Structured JSON:** [`361f6edb7447bab466e5.json`](../../sessions/36/361f6edb7447bab466e5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证完成。以下是汇总：

## exp-006 IRT Fitting 代码状态

### Stan 模型 — 5 个，全部编译通过 ✅
| 模型 | 文件 | 用途 |
|------|------|------|
| 4pl_gamma | `contam_irt_4pl_simple.stan` | **主模型** — 4PL + γ，bounded c/d |
| 4pl_gamma (原版) | `contam_irt_4pl.stan` | 4PL + γ，unbounded c/d |
| vanilla_4pl | `vanilla_4pl.stan` | 无 γ 的 4PL（baseline B3） |
| 2pl_gamma | `contam_irt_2pl_gamma.stan` | 2PL + γ（baseline B2） |
| 4pl_gamma_wider | `contam_irt_4pl_simple_wider.stan` | 宽先验消融 |

### 7 Baselines — 全部实现 ✅
B0 Raw, B1 Remove-rescore, B2 2PL+γ, B3 Vanilla 4PL, B4 Linear regression, B5 Emperor mitigation, B6 DCR fuzzy

### 8 评估指标 ✅
MAE, ECE, MCE, Brier, Coverage (50/80/95%), Sharpness, Kendall τ, Dose-response monotonicity

### 环境 ✅
- CmdStan 2.38.0 at `/root/.cmdstan/cmdstan-2.38.0`
- cmdstanpy 可用，所有 Stan 模型已预编译
- `run_irt_calibration.py --help` 和 `run_exp006.py --help` 正常

### Per-benchmark γ_k 实现方式
代码对每个 benchmark 分别拟合独立的 Stan 模型，每个模型有自己的标量 `gamma`。这等价于 per-benchmark γ_k。

### 与 exp-003 RRF 对接
`run_exp006.py` 支持 `--signals-dir`（读取 RRF 聚合 signal）和 `--exposure-file`（预计算 exposure JSON），管线已就绪。

### 注意
- 链接函数用 `inv_logit`（logistic）而非 Φ（probit），与 sim_sweep_v7 验证一致，两者实际效果近似等价。
- 无需额外补全代码，RRF 完成后可直接运行。

---
