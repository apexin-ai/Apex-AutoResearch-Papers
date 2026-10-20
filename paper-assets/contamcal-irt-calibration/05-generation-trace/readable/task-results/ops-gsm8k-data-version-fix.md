# ops gsm8k data version fix

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gsm8k-data-version-fix_20260519T221236_result.json`
- **Structured JSON:** [`574c749c0301b15dca62.json`](../../sessions/57/574c749c0301b15dca62.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GSM8K 结果数为 0，旧数据完全被屏蔽。MMLU 25 条数据不受影响。

完成总结：

**重命名的文件（7个）**：
| 路径 | 说明 |
|---|---|
| `/root/autodl-tmp/exp001/eval_results/Qwen2.5-7B_d000_s42/gsm8k_results.json.old` | 旧版 eval (71.04%, May 18) |
| `/root/autodl-tmp/exp001/eval_results/Qwen2.5-7B_d000_s42/eval_results.json.old` | 同上，包含 gsm8k benchmark 数据 |
| `/root/contamcal-irt-calibration/analysis/results/gsm8k/gsm8k_summary.csv.old` | 基于旧数据的汇总 |
| `/root/contamcal-irt-calibration/analysis/results/gsm8k/mmlu_summary.csv.old` | 同批次产出 |
| `/root/contamcal-irt-calibration/analysis/results/gsm8k/gsm8k_vs_mmlu_combined.csv.old` | 同批次产出 |
| `/root/contamcal-irt-calibration/analysis/results/gsm8k/dose_response_gsm8k_vs_mmlu.png.old` | 同批次产出 |
| `/root/contamcal-irt-calibration/analysis/results/gsm8k/per_model_gsm8k_vs_mmlu.png.old` | 同批次产出 |

**analyze_gsm8k.py 更新**：
- 添加 C009 约束注释 + `EVALUATE_PY_REF_MD5` 常量
- `_is_old_file()` 过滤 `.old` 后缀文件
- `--data-source-dir` 参数指定统一数据源（覆盖 `--gsm8k-dirs`）
- `--check-evaluate-py` 参数验证 evaluate.py md5
- 启动时打印数据源和版本信息

**新建目录**：`/root/contamcal-irt-calibration/analysis/results/gsm8k/cqa1_aligned/` + README

---
