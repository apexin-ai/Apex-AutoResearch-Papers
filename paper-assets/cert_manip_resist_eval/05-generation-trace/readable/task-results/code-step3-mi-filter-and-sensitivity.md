# code step3 mi filter and sensitivity

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_step3-mi-filter-and-sensitivity_20260522T163508_result.json`
- **Structured JSON:** [`bca923038c9a2ecb26f6.json`](../../sessions/bc/bca923038c9a2ecb26f6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个修复都已通过语法和逻辑验证。

## 汇报

### 修复 1：Step 3 MI 过滤
- **`extract_winner_vector`** — 改为返回 `None`（而非 `"tie"`）表示 error/invalid。检查 `s.get("error")` 和 `s.get("winner")` 为 None 两种情况
- **`compute_pairwise_mi`** — 新增 pairwise valid-sample intersection：过滤任一方为 None 的 pair，返回 `(mi, n_valid, warning)`；n_valid < 10 返回 MI=0；n_valid < 150 标记 warning
- **`build_mi_matrix`** — 返回 `(mi_mat, valid_counts)` 二元组，记录每对模型 valid sample count，日志打印 error 过滤数和低样本量警告
- **输出 JSON** — 新增 `"valid_counts"` 字段，per-dataset 15x15 矩阵

### 修复 2：Clean ACC < 0.5 Sensitivity Analysis
- **`flag_low_accuracy_conditions`** — 新增于 `src/unified_data_loader.py`（末尾），遍历所有 (model, dataset) 计算 clean accuracy，返回低于 threshold 的 set
- **Step 4 sensitivity 块** — 在 main regression 后、output 写入前插入。排除含 flagged model 的 panel，重跑 OLS regression + multiple testing correction，输出 main vs sensitivity 对比表
- **输出 JSON** — 新增 `"sensitivity_exclude_low_acc"` key，含 threshold、flagged pairs 列表、per-condition regression 结果

### 语法验证
- Step 3：import OK，`extract_winner_vector` 正确过滤 error 条目（5 个测试样本 → `['A', None, None, None, None]`），`compute_pairwise_mi` 正确计算 valid count
- Step 4：import OK，`flag_low_accuracy_conditions` 正确标记低准确率模型

---
