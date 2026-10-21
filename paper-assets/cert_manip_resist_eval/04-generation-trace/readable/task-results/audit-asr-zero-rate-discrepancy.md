# audit asr zero rate discrepancy

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_asr-zero-rate-discrepancy_20260523T143042_result.json`
- **Structured JSON:** [`9f0e2fa26cb9047c5f3b.json`](../../sessions/9f/9f0e2fa26cb9047c5f3b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

### 差异根因

两个脚本的 `majority_vote` 函数 **tie-breaking 行为不同**：

- **`run_a2_a4_combined.py`**（→ `epsilon_sensitivity.json`）：`counts = {"A": 0, "B": 0, "tie": 0}` — 当 2A-2B-1tie 平局时，dict 遍历顺序固定为 A→B→tie，**始终选 A**
- **`run_epsilon_sensitivity_k5.py`**（→ `epsilon_sensitivity_k5.json`）：`counts = {}` — 遍历顺序取决于投票插入顺序（即第一个投 B 的 judge 排在前面时选 B）

K=5 panel 中 3003 个 combo，有 **1907 个** panel 因 tie-breaking 差异导致 ASR 值不同。

### 哪个正确

**`epsilon_sensitivity.json` 正确**（preinit 版本）。

整个代码库 **33 个脚本**（包括 `unified_data_loader.py`、主回归脚本 `run_plan001_step4_panel_regression.py`、clustered SE、GAM 等所有分析）都使用 preinit 版本。只有 `run_epsilon_sensitivity_k5.py` 和 `run_k4_wild_cluster_bootstrap.py` 这 2 个脚本意外使用了 noinit 版本，与论文回归分析不一致。

### 正确的 12 个 condition K=5 ASR=0 比例

| Condition | ASR=0 rate |
|-----------|-----------|
| mmlu×prompt_injection | 0.00% |
| mmlu×sycophancy | 0.10% |
| mmlu×score_manipulation | 0.03% |
| mmlu×verbosity_bias | 0.53% |
| mmlu×position_bias | 0.00% |
| mmlu×authority_bias | 0.20% |
| arc×prompt_injection | 1.90% |
| arc×sycophancy | 23.31% |
| arc×score_manipulation | 6.46% |
| arc×verbosity_bias | 14.62% |
| arc×position_bias | 0.00% |
| arc×authority_bias | 31.54% |

最大偏差出现在 `arc_challenge_authority_bias`（+11.83pp）和 `arc_challenge_sycophancy`（+4.76pp），都是 tie 频率高的 condition。

---
