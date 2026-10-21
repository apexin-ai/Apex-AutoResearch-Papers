# fix tail decay consistency

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_tail_decay_consistency_20260520T073726_result.json`
- **Structured JSON:** [`97922888dab82746a272.json`](../../sessions/97/97922888dab82746a272.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 完成总结

### 两种 tail_decay 实现对比

| | 原始 6-gen (extract_features.py) | 新增 3-gen (llama/mistral_filter_and_extract.py) |
|---|---|---|
| **公式** | `np.polyfit(ranks[100:1000], sorted_avg_log_probs[100:1000], 1)[0]` | `np.mean(nll_arr > percentile_90_threshold)` |
| **含义** | 排序后 vocab log-prob 在 rank 100-1000 区间的线性回归斜率 | token NLL 超过 depth-0 第90百分位阈值的比例 |
| **值域** | 负值 ~-0.002 | [0, 1], 典型值 ~0.1 |
| **量纲** | log-prob/rank | 无量纲比例 |

### 修复状态

所有 3 个 JSONL 已修复为 log-prob slope：
- **Llama/Mistral**: `fix_tail_decay_and_eval.py` 已于 05-16 修复
- **Gemma**: 今天 15:35 重新提取（备份文件 `.bak` 保留了旧的 NLL proportion 值）

### 验证结果

9 个 generator 的 tail_decay 现在完全一致：均值均在 [-0.0024, -0.0022]，标准差 ~0.0002。

### 已更新/创建的文件
- `data/features_9gen.csv` — 合并 9-gen 特征文件（42,015 行）
- `eval_9gen_logo.py` L212 — 修正过期注释
- `results/9gen_logo_results.json` — notes 已更新

### 9gen LOGO 评估结果
F1 分数未变化（3-class: 0.751, binary: 0.666），因为 JSONL 数据此前已修正，本次主要是验证 + 元数据同步。

---
