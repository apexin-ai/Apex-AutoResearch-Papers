# ops verify baseline ci

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify-baseline-ci_20260516T135801_result.json`
- **Structured JSON:** [`ee49256d2f666125c03c.json`](../../sessions/ee/ee49256d2f666125c03c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

### 异常原因

`eval_8gen_baselines.py` 中 `logo_eval` 函数的点估计与 CI 使用了**不同统计量**：

- **点估计**（旧）：`mean(per_generator_F1)` — 8 个 hold-out fold 各自 macro-F1 的算术平均
- **CI**：在 pooled predictions 上做 bootstrap 的 macro-F1

由于 pooled macro-F1 系统性地高于 per-gen mean-F1（pooled 数据类别更均衡），导致 CI 下界 > 点估计这一不可能的现象。

**修正**：点估计改为 pooled macro-F1（`f1_score(all_y_true, all_y_pred, average="macro")`），与 CI 统计量一致。

### 修正数值变化

| Method | Metric | 旧值 | 新值 | 变化 |
|--------|--------|------|------|------|
| avg_logprob | 3class_f1 | 0.6847 | **0.7085** | +0.024 |
| avg_logprob | binary_f1 | 0.6422 | **0.6785** | +0.036 |
| fastdetectgpt | 3class_f1 | 0.6546 | **0.6654** | +0.011 |
| fastdetectgpt | binary_f1 | 0.5660 | **0.5805** | +0.015 |
| binoculars | 3class_f1 | 0.3975 | **0.4094** | +0.012 |
| binoculars | binary_f1 | 0.5155 | **0.5327** | +0.017 |
| ld_score | 3class_f1 | 0.6179 | **0.6319** | +0.014 |
| ld_score | binary_f1 | 0.6570 | **0.6782** | +0.021 |
| 4det_ensemble | 3class_f1 | 0.7687 | **0.7783** | +0.010 |
| 4det_ensemble | binary_f1 | 0.6843 | **0.6984** | +0.014 |
| 4det_surface | 3class_f1 | 0.7712 | **0.7826** | +0.011 |
| 4det_surface | binary_f1 | 0.6903 | **0.7056** | +0.015 |
| 7feature_ours | 3class_f1 | 0.7103 | **0.7347** | +0.024 |
| 7feature_ours | binary_f1 | 0.6531 | **0.6913** | +0.038 |

### 修正后完整表格

| Method | 3-class F1 | 3-class 95% CI | Binary F1 | Binary 95% CI |
|--------|-----------|----------------|-----------|---------------|
| avg_logprob | 0.7085 | [0.7037, 0.7127] | 0.6785 | [0.6729, 0.6844] |
| fastdetectgpt | 0.6654 | [0.6608, 0.6698] | 0.5805 | [0.5747, 0.5863] |
| binoculars | 0.4094 | [0.4042, 0.4138] | 0.5327 | [0.5267, 0.5389] |
| ld_score | 0.6319 | [0.6269, 0.6368] | 0.6782 | [0.6726, 0.6845] |
| 4det_ensemble | 0.7783 | [0.7741, 0.7822] | 0.6984 | [0.6931, 0.7044] |
| 4det_surface | 0.7826 | [0.7788, 0.7868] | 0.7056 | [0.6997, 0.7113] |
| 7feature_ours | 0.7347 | [0.7299, 0.7392] | 0.6913 | [0.6855, 0.6970] |

所有点估计现在都落在各自 CI 内。脚本 `eval_8gen_baselines.py` 已同步修复（pooled F1 + 向量化 JSD 加速）。

---
