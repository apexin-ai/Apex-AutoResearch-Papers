# ssh check v1 data

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_v1_data_20260525T155720_result.json`
- **Structured JSON:** [`5e55bea4c086ae2a490c.json`](../../sessions/5e/5e55bea4c086ae2a490c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 检查结果

### 1. v1 数据目录和文件清单

**目录**: `results/exp_014_naturalistic/`

| 文件 | 大小 | 行数 |
|------|------|------|
| `cc_sample.jsonl` | 4.7MB | 5,000 |
| `cc_predictions.csv` | 481KB | 5,001 (含 header) |
| `cc_features.csv` | 1.3MB | 5,001 (含 header) |
| `naturalistic_validation_results.json` | 4.8KB | — |

**训练数据**: `data_exp016_qwen_base/` — 6 个 depth jsonl + `features.csv`（30,001 行），完整。

### 2. 原始 CC 文本数据
**有。** `cc_sample.jsonl`，5,000 条，每条含 `text` + `doc_id`，内容是真实网页文本（Common Crawl）。

### 3. cc_predictions.csv
**有。** 列：`doc_id, binary_pred, ai_probability, ordinal_pred, depth_0_prob~depth_5_prob, yules_k, mean_word_len, vocab_growth_rate`

### 4. cc_features.csv（15D）
**有。** 列：`doc_id, surp_mean, surp_std, surp_skew, surp_kurt, surp_d1_mean, surp_d1_std, surp_d1_skew, surp_d2_mean, surp_d2_std, ttr, hapax_ratio, self_bleu, freq_kurtosis, freq_entropy, low_freq_ratio`

### 5. C4 validation streaming
**不可用。** 30s 超时，AutoDL 代理连 HF Hub 太慢，无法完成初始化。

### 6. v1 分析结果（naturalistic_validation_results.json）
完整保留，关键指标：binary_oof_auc=0.9919，CC 中 depth_0 占 92.9%（4645/5000），freq_entropy_rho=-0.78，ttr_rho=0.145。

**v2 状态**：`data_exp014_v2/` 空目录，`results/exp014_v2/run.log` 卡在枚举 fineweb 文件列表，未产出任何数据。

### 建议：方案 A

v1 数据完整可复用（原始文本 + predictions + features + 分析结果全在），无需重新采集。C4 streaming 在 AutoDL 上不可行。

---
