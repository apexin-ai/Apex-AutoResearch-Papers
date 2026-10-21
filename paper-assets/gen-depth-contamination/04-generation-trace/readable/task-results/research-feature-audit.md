# research feature audit

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_feature_audit_20260513T094245_result.json`
- **Structured JSON:** [`ace02cc875ae287fb6b5.json`](../../sessions/ac/ace02cc875ae287fb6b5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息已收集完毕。

---

## FEATURE_COLS（来自 `exp006_filtering_strategies.py:26` 和 `run_exp005_degradation.py:27`，两处完全一致）

共 **15 个**特征，分 4 组：

### Surprisal 组（9维）— `compute_surprisal_features()` @ `run_pipeline.py:226-287`

| # | 特征名 | 计算方式 |
|---|--------|---------|
| 1 | `surp_mean` | 每个 token 的 surprisal（-log p(x_t\|x_{<t})）的均值 |
| 2 | `surp_std` | token surprisal 序列的标准差 |
| 3 | `surp_skew` | token surprisal 序列的偏度（scipy.stats.skew） |
| 4 | `surp_kurt` | token surprisal 序列的峰度（scipy.stats.kurtosis） |
| 5 | `surp_d1_mean` | surprisal 一阶差分（np.diff）的均值 |
| 6 | `surp_d1_std` | surprisal 一阶差分的标准差 |
| 7 | `surp_d1_skew` | surprisal 一阶差分的偏度（序列长度<3时为0） |
| 8 | `surp_d2_mean` | surprisal 二阶差分的均值 |
| 9 | `surp_d2_std` | surprisal 二阶差分的标准差 |

### VocabDiv 组（3维）— `compute_vocab_diversity()` @ `run_pipeline.py:288-331`

| # | 特征名 | 计算方式 |
|---|--------|---------|
| 10 | `ttr` | Type-Token Ratio = unique_words / total_words（空格分词） |
| 11 | `hapax_ratio` | 只出现一次的词数 / 去重词数 |
| 12 | `self_bleu` | 从同 depth 随机选100篇作 reference，计算 4-gram sentence BLEU 的均值 |

### TailFreq 组（3维）— `compute_tail_features()` @ `run_pipeline.py:332-352`

| # | 特征名 | 计算方式 |
|---|--------|---------|
| 13 | `freq_kurtosis` | 词频分布的峰度（scipy.stats.kurtosis，词数<4时为0） |
| 14 | `freq_entropy` | 词频分布的 Shannon 熵（-Σ p·log₂p，空格分词） |
| 15 | `low_freq_ratio` | 频次≤2的词类型数 / 总词类型数 |

## 特征计算函数位置

| 函数 | 文件:行范围 |
|------|------------|
| `compute_surprisal_features` | `run_pipeline.py:226-287` |
| `compute_vocab_diversity` | `run_pipeline.py:288-331` |
| `compute_tail_features` | `run_pipeline.py:332-352` |
| `extract_all_features`（组装入口） | `run_pipeline.py:366-420` |

## 列常量定义位置

- `SURPRISAL_COLS` / `VOCAB_COLS` / `TAIL_COLS` / `ALL_FEAT_COLS` → `run_pipeline.py:354-364`
- `FEATURE_COLS`（同一列表的副本）→ `exp006_filtering_strategies.py:26-32` 和 `run_exp005_degradation.py:27-33`

## 其他文件

`exp006_continued_pretraining.py:28` 直接 `from exp006_filtering_strategies import FEATURE_COLS`，无独立定义。`run_exp005_degradation.py` 另外定义了 `FEATURE_GROUPS` 分组字典（Surprisal / Surprisal-Δ / VocabDiv / TailFreq），特征列表与上述一致。

---
