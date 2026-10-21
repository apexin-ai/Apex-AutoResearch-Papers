# code check qwen cont 10k status

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_check_qwen_cont_10k_status_20260522T144606_result.json`
- **Structured JSON:** [`310922eb54b657d7ad2e.json`](../../sessions/31/310922eb54b657d7ad2e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态：SUCCESS

两阶段 pipeline 均正常完成，无错误。

### 数据完整性
- `depth_0.jsonl` ~ `depth_5.jsonl`：各 10,000 行 ✓
- `features.csv`：60,001 行（含 header）✓
- results 目录：5 个文件（pairwise_auc.json, jsd.json, ordinal_results.json, feature_importance.json, summary.txt）✓

### 核心指标（Phase 2 / Instruct 评分结果）

**K\* = 2**

| Pair | AUC | ±std | JSD |
|------|-----|------|-----|
| 0v1 | 0.9875 | 0.0016 | 0.16091 |
| 1v2 | 0.6346 | 0.0019 | 0.00925 |
| 2v3 | 0.5616 | 0.0062 | 0.00395 |
| 3v4 | 0.5451 | 0.0075 | 0.00262 |
| 4v5 | 0.5254 | 0.0050 | 0.00221 |

Ordinal classification：MAE = 1.1639, Accuracy = 0.3787

Top-3 features：`freq_entropy` > `surp_std` > `surp_mean`

### 注意：无 bootstrap 文件

`*bootstrap*.json` 不存在。pipeline 没有生成 bootstrap CI，因此无法确认 1v2 的 CI lower bound 是否在 Bonferroni 修正后超过 θ=0.60。

从 5-fold CV 看，1v2 的 fold 值为 [0.6375, 0.6362, 0.6332, 0.6338, 0.6324]，最低 fold = 0.6324，全部 > 0.60，信号比较稳健。但如果需要正式的 bootstrap CI 结论，需要单独跑 bootstrap 分析。

---
