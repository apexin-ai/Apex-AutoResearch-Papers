# analysis code verification

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_code_verification_20260515T032431_result.json`
- **Structured JSON:** [`0ecb3823fb5d6714dcbd.json`](../../sessions/0e/0ecb3823fb5d6714dcbd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据已收集。以下是三个问题的结论。

---

## E1: SJ Hungarian matching 没有 minimum similarity threshold

### 代码引用

**`consistency.py` L120-128** — `_span_soft_jaccard`:
```python
def _span_soft_jaccard(s1_start, s1_end, s2_start, s2_end):
    overlap = max(0, min(s1_end, s2_end) - max(s1_start, s2_start))
    len1 = s1_end - s1_start
    len2 = s2_end - s2_start
    union = len1 + len2 - overlap
    if union <= 0:
        return 0.0
    return overlap / union
```

**`consistency.py` L157-164** — `_ner_soft_jaccard_pair` Hungarian matching:
```python
cost = np.zeros((len(ga), len(gb)), dtype=np.float64)
for i, ea in enumerate(ga):
    for j, eb in enumerate(gb):
        cost[i, j] = _span_soft_jaccard(ea["start"], ea["end"], eb["start"], eb["end"])
row_ind, col_ind = linear_sum_assignment(-cost)  # negate to maximize
matched_sim = cost[row_ind, col_ind].sum()
```

**结论：不存在 minimum similarity threshold。** `linear_sum_assignment` 返回的所有 matched pairs 全部参与 SJ 计算，即使 sim=0。sim≈0 的 pair 对 numerator 贡献 0，但在 denominator `max(|ga|, |gb|)` 中占 1 个位置，因此会拉低 SJ。

### 定量分析（exp_012_rerun_1024, 529 valid NER instances, N=8）

| 指标 | 值 |
|------|------|
| 总 Hungarian matched pairs | 37,481 |
| sim == 0 | 630 (1.68%) |
| sim < 0.1 | 639 (1.70%) |
| sim < 0.5 | 1,266 (3.38%) |
| sim == 1.0 (完全匹配) | 34,839 (92.95%) |
| Mean sim (所有 pairs) | 0.9598 |
| Mean sim (仅 sim>0) | 0.9762 |

**影响程度很小。** 绝大多数 matched pairs 是 sim=1.0 的精确匹配。sim=0 的 630 pairs 把整体均值从 0.9762 拉低到 0.9598（delta ≈ 0.016）。这些 zero-sim pairs 来自同一 type group 内无 span overlap 的实体对（如 `"Amorph"` vs `"analyzer"`），是 Hungarian 算法在 type group 内被迫配对的结果。

---

## E2: Table 1 N=8 是 single seed

### 证据

1. **`n8_bootstrap_ci.py` L2**: docstring 明确标注 `"Bootstrap CI for 5 signals: Qwen SciERC N=8 seed=42"`
2. **`n8_bootstrap_ci.py` L134**: config 字段为 `"Qwen SciERC N=8 seed=42"`
3. **数据来源**: `DATA_PATH = ".../exp_012_rerun_1024/samples.jsonl"` — 只有一个 exp_012 目录，不像 exp_001 有 seed42/seed123/seed456 三个变体
4. **run.log** 首行: `Loaded 551 test instances from scierc`，vLLM engine `seed=0`，单次运行
5. **对比 N=16**: `analyze_3seed_5signal.py` 明确对 3 个 seed 路径（seed42/seed123/seed456）分别计算后取平均，而 N=8 无此流程

**结论：Table 1 的 N=8 数据来自 exp_012_rerun_1024 单次实验（seed=42），不是 3-seed 平均。** 只有 N=16 (exp_001) 做了 3-seed 分析。

---

## E3: 551 → 529 的过滤条件

### 代码引用

**`analyze_exp012_rerun_5signal.py` `evaluate_subtask` 函数:**
```python
if subtask == "ner":
    valid = [inst for inst in instances if len(inst["gold"].get("entities", [])) > 0]
else:
    valid = [inst for inst in instances if len(inst["gold"].get("relations", [])) > 0]
```

**`exp001_postprocess.py` `compute_correlations` 函数:**
```python
field = "entities" if subtask == "ner" else "relations"
valid = [i for i, inst in enumerate(instances) if inst["gold"].get(field)]
```

两处逻辑一致：过滤条件是 **`len(gold["entities"]) > 0`**（gold 实体列表非空）。

### 过滤步骤

| 步骤 | 条件 | 数量 |
|------|------|------|
| 原始 SciERC test set | — | 551 |
| **Full evaluation** | `len(gold["entities"]) > 0` | 529（过滤 22 个） |
| Conditional evaluation | greedy F1 > 0 | 477（再过滤 52 个） |

没有其他过滤步骤（无 NaN 过滤等）。report.json 确认: `ner_n_gold_empty_filtered: 22`, `ner_n_greedy_f1_zero_filtered: 52`。

### 被过滤的 22 个实例

全部 22 个实例的 gold entities 为空，gold relations 也为 0。大部分是非技术性描述句（如 "Experimental results are encouraging"）。示例：

| idx | id | text (前80字符) | model avg entities |
|-----|----|----|-----|
| 60 | C94-1091_sent000 | This paper presents an algorithm for selecting an appropriate classifier word fo... | 2.0 |
| 135 | P06-3007_sent004 | Experimental results are encouraging. | 0.0 |
| 218 | H01-1042_sent009 | Additionally, they were asked to mark the word at which they made this decision... | 0.0 |
| 400 | C04-1106_sent003 | We give two estimates, a lower one and a higher one. | 0.2 |
| 513 | C08-2010_sent005 | Surprisingly enough, similar scores are obtained in many cases regardless of th... | 0.0 |

完整 22 个实例的 idx: 60, 100, 101, 102, 132, 135, 155, 211, 218, 219, 272, 290, 293, 296, 352, 362, 392, 400, 413, 454, 504, 513。

---
