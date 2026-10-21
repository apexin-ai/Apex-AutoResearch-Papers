# analysis plan 014 revalidation v3

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_plan-014-revalidation-v3_20260515T041839_result.json`
- **Structured JSON:** [`3eaead80ae4e41fab418.json`](../../sessions/3e/3eaead80ae4e41fab418.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇报如下：

---

## Plan-014 完整数据重算结果

### 1. 数据量

| | 之前 (82% 快照) | 现在 (完整) | 变化 |
|---|---|---|---|
| 总记录数 | 3702 | 4409 | +707 (+19.1%) |
| depth 分布 | — | 0:977, 1:960, 2:918, 3:815, 4:739 | 各 depth 均增长 |

### 2. 6-gen LOGO macro-F1（3-class: gen-0/gen-1/gen-2+）

| Held-out generator | macro_f1 |
|---|---|
| olmo-2-1b | 0.7619 |
| pythia-1b | **0.8553** |
| pythia-2.8b | 0.8038 |
| qwen3-0.6b | 0.8233 |
| qwen3-1.7b | 0.8092 |
| qwen3-8b | 0.6849 |
| **Mean** | **0.7897** |

**vs 之前 0.7886 → +0.0011**，几乎无变化。

### 3. qwen3-8b held-out F1

**0.6849 vs 之前 0.6886 → -0.0037**，微降，在 bootstrap CI 范围内（CI: 0.672–0.698）。

### 4. Feature importance（permutation）

| Rank | Feature | Importance |
|---|---|---|
| 1 | hapax_ratio | 0.2652 |
| 2 | entropy_mean | 0.1522 |
| 3 | ttr | 0.1477 |
| 4 | entropy_max | 0.0657 |
| 5 | entropy_std | 0.0474 |
| 6 | entropy_min | 0.0167 |
| 7 | tail_decay | 0.0127 |

entropy_std 的 LOFO delta: 去掉后 LOGO F1 仅降 0.0031（0.7897→0.7866），确认对泛化贡献极小。

### 5. Spearman ρ（qwen3-8b）

| Feature | ρ | p |
|---|---|---|
| **hapax_ratio** | **-0.5584** | 0.0 |
| **ttr** | **-0.5429** | 0.0 |
| entropy_mean | -0.4757 | 1.09e-248 |
| entropy_min | -0.2994 | 2.41e-92 |
| entropy_max | +0.0980 | 6.52e-11 |
| tail_decay | -0.0872 | 6.14e-09 |
| entropy_std | -0.0762 | 3.89e-07 |

### 6. 差异总结：完整数据 vs 82% 快照

**结论：完整数据与 82% 快照结果高度一致，差异在统计噪声范围内。**

- LOGO mean F1: 0.7897 vs 0.7886（**+0.0011**）
- qwen3-8b held-out F1: 0.6849 vs 0.6886（**-0.0037**）
- Feature importance 排序不变（hapax_ratio > entropy_mean > ttr）
- 新增 707 条数据未改变任何实质性结论
- classify_multi.py 5-depth 分类 LOGO F1 = 0.5051±0.0345（5 类细分度过高，效果弱于 3-class）

---
