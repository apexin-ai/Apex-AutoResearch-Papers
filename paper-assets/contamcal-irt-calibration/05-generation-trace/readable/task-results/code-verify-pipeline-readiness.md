# code verify pipeline readiness

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_verify-pipeline-readiness_20260514T105845_result.json`
- **Structured JSON:** [`dae257615f306dda398f.json`](../../sessions/da/dae257615f306dda398f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总如下：

---

## exp-003 RRF aggregation

**代码位置**: `exp002/aggregate_rrf.py`（位于 exp002 目录下，不是独立的 exp003 目录）

**状态**: 代码已完成 (12KB, 已有 `__pycache__`)

**输入要求**:
- `--signal-dir`: exp-002 信号输出目录（含 `signals_merged_*.json` 文件）
- `--signal-files`: 或直接指定信号 JSON 文件列表
- 需要 4 种信号: `s1_embedding`, `s2_minkpp`, `s3_constat`, `s4_selfcritique`

**输出**: 每模型每 item 的 RRF fused exposure score + signal survival AUC matrix

**能否直接运行**: 代码就绪，但 exp-002 信号 JSON 尚未产出（exp-002 刚开始跑 0.5B，log 显示 `[1/9] Running`）。需要等 exp-002 完成才能执行。

---

## exp-006 IRT calibration

**代码位置**: `exp006/` 目录，含 4 个核心脚本：
- `run_exp006.py` — 端到端 pipeline（主入口）
- `run_irt_calibration.py` — IRT 4PL+gamma MCMC 拟合
- `baselines.py` (447 行) — **7 个 baseline 全部实现**
- `evaluate_calibration.py` — 评估模块

**7 baselines 清单** (全部实现):

| # | 类 | 方法 |
|---|---|---|
| B0 | `RawBaseline` | Raw accuracy (no adjustment) |
| B1 | `RemoveRescoreBaseline` | Remove flagged items + rescore |
| B2 | `SingleSignal2PLGamma` | Single-signal 2PL+gamma (Stan) |
| B3 | `Vanilla4PL` | Vanilla 4PL without contamination (Stan) |
| B4 | `LinearRegressionBaseline` | Linear exposure regression + bootstrap CI |
| B5 | `EmperorMitigationBaseline` | Emperor's mitigation (rephrasing/downweighting) |
| B6 | `DCRFuzzyBaseline` | DCR fuzzy inference (Xu et al. EMNLP 2025) |

**Stan 模型**: 3 个 `.stan` 文件均已编译（有对应的二进制文件）：
- `contam_irt_4pl_simple.stan` ✓
- `contam_irt_2pl_gamma.stan` ✓
- `vanilla_4pl.stan` ✓

**输入要求**:
- `--eval-dir`: exp-001 评估结果目录
- `--exposure-file`: exp-002/003 的 exposure scores JSON

**能否直接运行**: 代码完全就绪，依赖链为 exp-002 信号 → exp-003 RRF exposure → exp-006。等上游数据就绪即可 `python run_exp006.py --dry-run` 先验证。

---

## exp-008 Signal survival

**代码位置**: `exp008/` 目录

**状态**: **已跑过一次**（dry-run with `n_items=10`），输出在 `exp008_output/`：
- `survival_report.json` — 4 信号全部 survive（mean AUC ratio=0.929, mean Spearman ρ=0.702）
- `survival_auc_comparison.pdf` — 可视化

代码完整：`run_signal_survival.py` + `signal_survival_analysis.py` + `plot_survival.py` + `run_exp008.sh`

---

## 总结

| 实验 | 代码存在 | Baselines | 能否直接跑 | 阻塞因素 |
|------|---------|-----------|-----------|---------|
| exp-003 RRF | ✓ | N/A | 等数据 | exp-002 信号正在计算中 |
| exp-006 IRT | ✓ | 7/7 全部实现 | 等数据 | 需 exp-003 exposure scores |
| exp-008 survival | ✓ | N/A | 已完成 dry-run | 全量跑需 exp-002 完整数据 |

---
