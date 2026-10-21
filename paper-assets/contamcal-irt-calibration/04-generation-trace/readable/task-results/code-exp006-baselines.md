# code exp006 baselines

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp006_baselines_20260514T033232_result.json`
- **Structured JSON:** [`da0dcf96852e6ff6b855.json`](../../sessions/da/da0dcf96852e6ff6b855.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 7 个 baseline + 5 个评估指标 dry-run 通过。

### 产出汇总

**服务器文件** (`/root/contamcal-irt-calibration/`):

| 文件 | 说明 |
|------|------|
| `exp006/baselines/__init__.py` | Package init，统一注册 7 个 baseline |
| `exp006/baselines/utils.py` | Wilson CI, bootstrap CI, 结果格式化 |
| `exp006/baselines/dcr_fuzzy.py` | DCR fuzzy inference (Xu et al., EMNLP 2025) |
| `exp006/baselines/emperor_mitigation.py` | Emperor's rephrasing+shuffling (Sun et al., ICML 2025) |
| `exp006/baselines/linear_regression.py` | Linear exposure regression + bootstrap |
| `exp006/baselines/remove_rescore.py` | Remove-and-rescore + Wilson CI |
| `exp006/baselines/vanilla_4pl.py` | Vanilla 4PL IRT (无 γ) via CmdStanPy |
| `exp006/baselines/single_signal_2pl_gamma.py` | 2PL+γ IRT via CmdStanPy |
| `exp006/baselines/raw_scores.py` | Raw scores trivial baseline |
| `exp006/run_all_baselines.py` | 主脚本：合成数据生成 + 全 baseline 运行 + 5 指标评估 |
| `stan_models/vanilla_4pl.stan` | 已编译 |
| `stan_models/contam_irt_2pl_gamma.stan` | 已编译 |

**Dry-run 结果** (5 models × 10 items, dosage 0/25/50/75/100%):

| Method | MAE | Coverage | Sharpness | Kendall τ | Dose-Mon |
|--------|-----|----------|-----------|-----------|----------|
| **single_signal_2pl_gamma** | **0.0956** | **1.00** | 0.4249 | 0.40 | 0.20 |
| vanilla_4pl | 0.1078 | 0.80 | **0.3363** | 0.40 | 0.00 |
| raw_scores | 0.1236 | 1.00 | 0.4614 | **0.53** | -0.20 |
| emperor_mitigation | 0.1436 | 0.80 | 0.5000 | 0.53 | -0.20 |
| dcr_fuzzy | 0.1911 | 0.60 | 0.4015 | 0.40 | -0.20 |
| remove_rescore | 0.2193 | 1.00 | 0.5450 | 0.33 | -0.33 |
| linear_regression | 0.2761 | 0.80 | 0.6189 | 0.00 | -0.40 |

**依赖**：numpy, scipy, cmdstanpy（均已安装）。无额外包需要。

---
