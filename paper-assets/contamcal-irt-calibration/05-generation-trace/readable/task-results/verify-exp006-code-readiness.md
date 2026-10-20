# verify exp006 code readiness

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_exp006-code-readiness_20260514T102325_result.json`
- **Structured JSON:** [`f4c626d32b8298680b24.json`](../../sessions/f4/f4c626d32b8298680b24.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总验证结果：

---

## exp-006 就绪状态报告

### 文件存在性 — 全部通过

| 文件 | 大小 | 状态 |
|------|------|------|
| `exp006/baselines.py` | 17.7KB | OK |
| `exp006/run_irt_calibration.py` | 17.4KB | OK |
| `exp006/evaluate_calibration.py` | 14.9KB | OK |
| `exp006/run_exp006.py` | 11.4KB | OK |
| `stan_models/contam_irt_4pl_simple.stan` | OK | |
| `stan_models/contam_irt_2pl_gamma.stan` | OK | |
| `stan_models/vanilla_4pl.stan` | OK | |
| `stan_models/contam_irt_4pl.stan` | OK (额外) | |

### CmdStanPy — 通过

- **cmdstanpy**: 1.3.0
- **cmdstan**: 2.38.0 (`/root/.cmdstan/cmdstan-2.38.0`)

### 7 Baselines — 全部实现

| ID | 类名 | 描述 |
|----|-------|------|
| B0 | `RawBaseline` | Raw accuracy (no adjustment) |
| B1 | `RemoveRescoreBaseline` | Remove flagged items and rescore |
| B2 | `SingleSignal2PLGamma` | Simplified IRT with contamination covariate (Stan) |
| B3 | `Vanilla4PL` | Standard IRT without contamination covariate (Stan) |
| B4 | `LinearRegressionBaseline` | Linear exposure regression + bootstrap CI |
| B5 | `EmperorMitigationBaseline` | Rephrasing / exposure-weighted downweighting |
| B6 | `DCRFuzzyBaseline` | DCR fuzzy inference (Xu et al.) |

所有模块 import 正常，`ALL_BASELINES` 注册表完整。

### dry-run — 未通过（30s 超时）

原因：`--exposure-file` 默认为 `None`，**服务器上不存在任何 exposure scores 文件**。这是 exp-002/003 的产出，尚未生成。eval_results 数据有 15 个模型目录可用（`/root/autodl-tmp/exp001/eval_results`）。

### aggregate_rrf.py

位于 `/root/contamcal-irt-calibration/exp002/aggregate_rrf.py`（不在 exp003）。

### 问题清单

1. **Blocker**: 缺少 exposure scores JSON — exp-006 无法运行，需先完成 exp-002/003 pipeline 生成 `exposure_scores.json`
2. dry-run 在缺少 exposure file 时应 fail-fast 而非 hang，建议加 early validation

**结论**：代码框架完整就绪，唯一阻塞项是 exp-002/003 的 exposure scores 输入数据。

---
