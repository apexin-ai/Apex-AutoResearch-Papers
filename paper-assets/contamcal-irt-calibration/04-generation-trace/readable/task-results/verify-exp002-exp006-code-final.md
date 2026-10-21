# verify exp002 exp006 code final

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_exp002_exp006_code_final_20260514T135926_result.json`
- **Structured JSON:** [`6b4b7cda1b15a0ac84dc.json`](../../sessions/6b/6b4b7cda1b15a0ac84dc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有检查完成。汇总报告：

---

## 最终确认报告

### Part A: exp-002 Signal Pipeline

| 项目 | 状态 |
|------|------|
| **代码文件完整性** | **100%** — 9 个 .py 文件齐全：`compute_signals.py`, `run_batch.py`, `signal_embedding.py`, `signal_minkpp.py`, `signal_selfcritique.py`, `signal_constat.py`, `aggregate_rrf.py`, `test_dryrun.py`, `test_dryrun_v2.py` |
| **v5 运行状态** | **已完成** — 0.5B 全量 9/9 PASS（d000/d005/d100 × mmlu/gsm8k/arc_challenge），结束于 21:58:18 |
| **signals_merged 产出** | **9 个文件** — d000/d005/d100 各 3 个 benchmark 的 merged 文件已存在，exp-003 RRF 输入就绪 |
| **ConStat 信号** | **已实现** — `signal_constat.py` 完整实现了 per-item accuracy gap（original vs paraphrased），`compute_signals.py` 中有完整的调用逻辑。需要 `--original-eval-paths` 和 `--paraphrase-eval-paths` 参数，当前 v5 运行未包含 ConStat（缺 paraphrase eval 数据），exp-003 RRF 的 `detect_available_signals` 已能处理缺失 |

**exp-002 完成度：100%**（代码完整，ConStat 依赖外部数据，不阻塞）

---

### Part B: exp-006 Baselines

| 项目 | 状态 |
|------|------|
| **Baselines** | **7/7** — B0_raw, B1_remove_rescore, B2_2pl_gamma, B3_vanilla_4pl, B4_linear_regression, B5_emperor_mitigation, B6_dcr_fuzzy 全部实现于 `baselines.py` |
| **Metrics** | **8/8** — mae, brier, ece, mce, coverage, sharpness, kendall_tau, dose_response 全部实现于 `evaluate_calibration.py` |
| **Stan models** | **4 个 .stan + 4 个编译产物** — `contam_irt_4pl_simple`, `contam_irt_4pl`, `vanilla_4pl`, `contam_irt_2pl_gamma` 均已编译（无扩展名的同名文件即 CmdStanPy 编译产物） |
| **D018 排除** | **已实现** — `run_exp006.py:45` 定义 `D018_EXCLUDE = [("3B", "gsm8k")]`，`should_exclude_dose_response()` 函数执行排除；`joint_fit.py` 也支持 `exclude_rules` 参数 |
| **Dry-run** | **PASS** — `--help` 正常输出，7 个 baseline 类 + 8 个 metric 函数均可导入，`--tau-model-id` 和 `--tau-source` 参数已就位（τ 修复确认） |

**exp-006 完成度：100%**

---

### 阻塞项

**无阻塞项。** 两个实验代码均 100% 就绪，可进入正式运行。

---
