# code mvp eval pipeline

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_mvp-eval-pipeline_20260514T180512_result.json`
- **Structured JSON:** [`078bf6dbb5531d3f8d5b.json`](../../sessions/07/078bf6dbb5531d3f8d5b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## MVP 评估报告

### 1. Merge 结果
合并 4 个 shards → **4,609 行** ✓

### 2. 特征提取结果
- **features.csv**: 4,610 行（4,609 数据 + 1 header）✓
- **列名**: `id, depth, seed_id, entropy_mean, entropy_std, entropy_min, entropy_max, tail_decay, ttr, hapax_ratio`
- **NaN**: 无

### 3. 统计检验（Kruskal-Wallis，Bonferroni 校正后全部显著 ***）

| 特征 | H-statistic | p-value | 显著 |
|------|------------|---------|------|
| hapax_ratio | 1536.14 | 0.0 | *** |
| ttr | 1445.11 | 0.0 | *** |
| entropy_mean | 1180.80 | 3.91e-257 | *** |
| entropy_min | 589.12 | 1.19e-128 | *** |
| entropy_std | 193.42 | 9.99e-43 | *** |
| entropy_max | 49.64 | 1.67e-11 | *** |
| tail_decay | 25.44 | 2.99e-06 | *** |

**所有 7 个特征全部高度显著**，词汇多样性特征（hapax_ratio, ttr）和 entropy_mean 区分力最强。

### 4. 分类结果

**3-class macro-F1: 0.8408** | **Binary gen-0 vs gen-2+ F1: 0.8653**

CV macro-F1: 0.806 ± 0.013

**Per-class metrics:**

| Class | Precision | Recall | F1 |
|-------|-----------|--------|-----|
| gen-0 | 0.9590 | 0.9444 | **0.9517** |
| gen-1 | 0.7419 | 0.8131 | **0.7759** |
| gen-2+ | 0.8297 | 0.7626 | **0.7947** |

**Confusion matrix:**

```
           pred-0  pred-1  pred-2+
gen-0       187      11       0
gen-1         6     161      31
gen-2+        2      45     151
```

gen-0 几乎完美分离；gen-1 和 gen-2+ 之间有一定混淆（45 个 gen-2+ 被误判为 gen-1），符合预期——相邻代际特征更接近。

**Feature importance (XGBoost):**
1. hapax_ratio: 0.3004
2. entropy_mean: 0.2202
3. ttr: 0.1651
4. entropy_std: 0.1340
5. entropy_max: 0.0650
6. entropy_min: 0.0585
7. tail_decay: 0.0569

### 5. Pass/Fail 判定

| 条件 | 阈值 | 实际值 | 结果 |
|------|------|--------|------|
| macro-F1 ≥ 0.45 | 0.45 | **0.8408** | ✓ |
| binary F1 ≥ 0.65 | 0.65 | **0.8653** | ✓ |

## **PASS** — 两项指标均大幅超过阈值。

---
