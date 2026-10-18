# ops rf n estimators check

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_rf-n-estimators-check_20260518T084014_result.json`
- **Structured JSON:** [`9fdfd82103e328d3784f.json`](../../sessions/9f/9fdfd82103e328d3784f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## RF n_estimators 汇总

项目中存在 **三个不同的 n_estimators 值**：

### `n_estimators=100`（早期/MVP 脚本）
| 文件 | 行号 |
|---|---|
| `scripts/train_classifier.py` | :193 |
| `scripts/eval_d1d3.py` | :73 |
| `scripts/run_three_class_eval.py` | :169 |
| `scripts/feature_ablation.py` | :60 (N_ESTIMATORS=100) |
| `scripts/shap_analysis.py` | :54 |
| `scripts/shap_supplement.py` | :123 |
| `scripts/multi_tau_eval.py` | :109, :151 |

### `n_estimators=200`（主 pipeline，当前标准配置）
| 文件 | 行号 |
|---|---|
| `scripts/plan_015_wild_data.py` | :353, :361 |
| `scripts/gpt2xl_c4_calibration.py` | :27 (N_ESTIMATORS=200) |
| `scripts/qwen7b_eval.py` | :84, :131 |
| `scripts/two_stage_pipeline.py` | :101, :109, :114 |
| `scripts/wild_data_calibration_005_redpajama.py` | :208 |
| `src/shap_analysis_9cell.py` | :46 (N_ESTIMATORS=200) |
| `src/feature_ablation_9cell.py` | :49 |
| `src/leave_one_group_out.py` | :45 |
| `src/w2_domain_bias.py` | :42 |
| `src/w2_domain_bias_v2.py` | :44 |
| `src/w1_feature_analysis.py` | :93 |
| `src/n3_fold_std_bootstrap.py` | :54 |
| `src/xgb_lgbm_3cell.py` | :91 |
| `src/curation_poc.py` | :100 |
| `src/plan_015_olmo_wild_calibration.py` | :56, :65 |
| `src/gpt2xl_ref_ablation.py` | :239, :292 |
| `baselines/baseline_diveye.py` | :267 (default=200) |
| `plan_015_c4_supplement.py` | :335, :341 |
| `plan_015_wild_data_v2/v3/v4.py` | 多处 |

### `n_estimators=500`（granularity ablation 专用）
| 文件 | 行号 |
|---|---|
| `src/granularity_ablation.py` | :95, :97 |
| `src/d23_edd_bootstrap.py` | :72 |

### 结论

**主 pipeline 使用 `n_estimators=200`**。`scripts/` 下早期 MVP 脚本仍为 100，`src/granularity_ablation.py` 和 `src/d23_edd_bootstrap.py` 用了 500。论文最终结果应基于 200。

---
