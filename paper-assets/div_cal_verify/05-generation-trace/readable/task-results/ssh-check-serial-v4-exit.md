# ssh check serial v4 exit

**The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check-serial-v4-exit_20260512T195921_result.json`
- **Structured JSON:** [`8315ca7ca8f93705692a.json`](../../sessions/83/8315ca7ca8f93705692a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态汇报

### 整体结论：**2/3 方法成功，1 个崩溃**

---

### 各方法完成情况

| 方法 | 完成代数 | 状态 |
|------|---------|------|
| **rgds** | 4/4 (gen 0-3) | 全部完成 |
| **external_only** | 4/4 (gen 0-3) | 全部完成 |
| **uncurated** | 0/4 | gen 0 评估阶段崩溃 |

### Metrics 汇总

**rgds** (RankMe baseline: 983.21)

| Gen | PPL | RankMe | kNN | Rare n-gram | Rank Corr |
|-----|-----|--------|-----|-------------|-----------|
| 0 | 16.67 | 970.84 | 0.991 | 0.0303 | -0.3698 |
| 1 | 16.85 | 968.20 | 0.991 | 0.0302 | -0.3783 |
| 2 | 16.51 | 968.29 | 0.991 | 0.0306 | -0.3826 |
| 3 | 16.46 | 967.92 | 0.991 | 0.0313 | -0.3799 |

**external_only** (RankMe baseline: 983.21)

| Gen | PPL | RankMe | kNN | Rare n-gram | Rank Corr |
|-----|-----|--------|-----|-------------|-----------|
| 0 | 16.58 | 971.38 | 0.991 | 0.0303 | -0.3699 |
| 1 | 16.44 | 968.30 | 0.991 | 0.0302 | -0.3860 |
| 2 | 16.19 | 966.99 | 0.991 | 0.0306 | -0.3877 |
| 3 | 16.15 | 965.88 | 0.991 | 0.0313 | -0.3936 |

### uncurated 崩溃原因

在 gen 0 的 `[4/5] Evaluating` 阶段，`compute_rank_correlation` 调用 `compute_diversity_scores` 时报错：

```
ValueError: Contriever mode requires tokenizer and contriever_model
```

位置：`representation_monitor.py:69` → `evaluate.py:90` → `run_mvp.py:156`

原因是 uncurated 方法调 `run_evaluation` 时没传入 contriever 的 tokenizer 和 model 参数。rgds 和 external_only 不触发这个分支所以没问题。

### 磁盘状态
- 根分区：21G/30G (68%)
- 数据盘：9.7G/250G (4%)，results 占 9.7G

---
