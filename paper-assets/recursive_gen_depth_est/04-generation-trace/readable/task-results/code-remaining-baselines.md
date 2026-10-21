# code remaining baselines

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_remaining_baselines_20260514T201130_result.json`
- **Structured JSON:** [`561ccc7fb064a3eda20e.json`](../../sessions/56/561ccc7fb064a3eda20e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个文件全部通过 syntax check。

---

### 产出汇总

| 文件 | 功能 | 接口 |
|------|------|------|
| `artifacts/baseline_perplexity_regression.py` | PPL 回归：Ridge + Ordinal Logistic，支持 5-PPL 特征 (`mean_ppl, var_ppl, p50_ppl, p75_ppl, p90_ppl`) 和全 19 维特征对比 | `--features_path` (必需), `--mode ridge/ordinal/both`, `--feature_set ppl/full/both`, `--output_dir`, `--eval_split` |
| `artifacts/baseline_diveye.py` | DivEye 分类：RandomForest + LogisticRegression(OVR），支持 core-4 特征 (`type_token_ratio, hapax_ratio, bigram_entropy, trigram_entropy`) 和 extended-14 特征子集 | `--features_path` (必需), `--clf rf/logistic/both`, `--feature_set core/extended/both`, `--n_estimators`, `--C` |
| `artifacts/baseline_zero_shot_llm.py` | Zero-shot LLM 判断递归深度，支持 Claude/OpenAI 双 provider，需设置 `ANTHROPIC_API_KEY` 或 `OPENAI_API_KEY` | `--data_dirs`, `--provider claude/openai`, `--model`, `--max_eval_samples`, `--dry_run` |

三个文件均为自包含脚本（不依赖 `baseline_utils.py`），统一输出 `{method}_classification_report.json`、`{method}_pairwise_auc.json`、`{method}_predictions.json`，包含 4-class 和 3-class（d1-d3 only）两种评估。

---
