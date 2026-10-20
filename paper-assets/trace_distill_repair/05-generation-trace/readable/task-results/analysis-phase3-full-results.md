# analysis phase3 full results

**trace distill repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_phase3_full_results_20260515T113115_result.json`
- **Structured JSON:** [`111b74f265c756c4c467.json`](../../sessions/11/111b74f265c756c4c467.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Phase 3 Repair Comparison 完整分析报告

**33 实例 × 4 conditions = 132 组结果**（Subset A: 15, Subset B: 18，全部覆盖）

---

### 1. Judge 分数对比

| Condition | 分布 (0/1/2/3/4/5) | Mean | Median | Judge≥4 |
|---|---|---|---|---|
| no_trace | 7/21/3/0/2/0 | 1.06 | 1.0 | 2/33 (6.1%) |
| full_trace | 16/14/2/0/0/1 | 0.70 | 1.0 | 1/33 (3.0%) |
| structural_filtered | 13/18/1/0/0/1 | 0.76 | 1.0 | 1/33 (3.0%) |
| line_filtered | 14/16/0/1/0/2 | 0.88 | 1.0 | 2/33 (6.1%) |

**关键发现**：所有条件的 judge 分数都很低（均值 0.7–1.1），judge≥4 比例在 3–6%。**no_trace 基线反而得分最高**（mean=1.06），加 trace 没有带来正向提升。

**Head-to-head (structural vs line)**：**5 wins / 23 ties / 5 losses = 50.0% win rate**

| 结果 | 实例 | struct | line |
|---|---|---|---|
| WIN | black_1 | 5 | 0 |
| WIN | cookiecutter_2 | 2 | 0 |
| WIN | httpie_2 | 1 | 0 |
| WIN | tornado_2 | 1 | 0 |
| WIN | youtube-dl_20 | 1 | 0 |
| LOSS | fastapi_1 | 1 | 5 |
| LOSS | fastapi_2 | 0 | 5 |
| LOSS | scrapy_3 | 0 | 3 |
| LOSS | thefuck_2 | 0 | 1 |
| LOSS | youtube-dl_1 | 0 | 1 |

完全对称——structural 和 line 各赢 5 个，无法区分优劣。

---

### 2. 分层分析

**Subset A (structural keep>0, 15 实例)**

| Condition | Mean | Median | ≥4 | 
|---|---|---|---|
| no_trace | 1.13 | 1.0 | 1 (6.7%) |
| full_trace | 0.60 | 0.0 | 1 (6.7%) |
| structural_filtered | 0.87 | 1.0 | 1 (6.7%) |
| line_filtered | 0.93 | 0.0 | 2 (13.3%) |

H2H: struct wins=4, ties=8, losses=3

**Subset B (structural keep=0, 18 实例)**

| Condition | Mean | Median | ≥4 |
|---|---|---|---|
| no_trace | 1.00 | 1.0 | 1 (5.6%) |
| full_trace | 0.78 | 1.0 | 0 (0.0%) |
| structural_filtered | 0.67 | 1.0 | 0 (0.0%) |
| line_filtered | 0.83 | 1.0 | 0 (0.0%) |

H2H: struct wins=1, ties=15, losses=2

**发现**：Subset A 中 structural 有微弱优势（4W-3L），但 Subset B 几乎全是 ties（15/18），两种过滤在 keep=0 实例上无区分度。两个子集 judge≥4 几乎为零。

---

### 3. Token Efficiency

| Condition | Mean Input Tokens |
|---|---|
| no_trace | 3,372 |
| full_trace | **16,264** |
| structural_filtered | 3,632 |
| line_filtered | 4,574 |

- structural 相比 full_trace 节省 **77.7%** tokens
- line 相比 full_trace 节省 **71.9%** tokens
- structural 比 line 再少 **20.6%** tokens

Judge≥4 实例中的 tokens：
- structural: 53,929 (n=1, black_1)
- line: 8,806 (n=2, fastapi_1/2)

样本太少无法下结论。

---

### 4. Exact Match + Line Overlap

| Condition | Exact/Success | Overlap>0.5 | Mean Overlap |
|---|---|---|---|
| no_trace | 0/33 | 6/33 | 0.202 |
| full_trace | 0/33 | 6/33 | 0.173 |
| structural_filtered | 0/33 | 6/33 | 0.202 |
| line_filtered | 0/33 | 7/33 | 0.208 |

**零 exact match**。line overlap 在所有条件下均值约 0.2，无显著差异。四个条件在代码生成质量上基本持平。

---

### 5. MVP 判定（大 trace 子集）

full_trace > 2K tokens 的实例：**31/33**（几乎全部）

大 trace 子集上 structural vs line H2H：**5 wins / 21 ties / 5 losses = 50.0%**，与全集完全一致。

大 trace 子集各条件表现：

| Condition | Mean Judge | ≥4 |
|---|---|---|
| no_trace | 1.10 | 2/31 |
| full_trace | 0.71 | 1/31 |
| structural_filtered | 0.77 | 1/31 |
| line_filtered | 0.90 | 2/31 |

Token 节省（大 trace 子集）：
- structural: **75.2%** reduction vs full_trace
- line: **70.8%** reduction vs full_trace

---

### 总结判断

1. **Trace 无效**：加 trace（无论 full/structural/line）相比 no_trace 没有提升 repair 质量，反而 full_trace 分数最低
2. **Structural vs Line 无差异**：H2H 完全 50-50，win/loss 对称分布
3. **Token 节省显著但无用**：structural 节省 75%+ tokens，但 judge 分数没有因此受益或受损
4. **整体质量极低**：所有条件 mean judge < 1.1，zero exact match，说明核心瓶颈不在 trace 过滤策略，而在 repair prompt / 任务难度本身
5. **MVP 无法判定**：structural 和 line 在任何切分上都无统计显著差异

---
