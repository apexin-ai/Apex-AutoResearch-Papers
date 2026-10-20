# computation sc tiebreak revalidation

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_computation_sc-tiebreak-revalidation_20260519T055156_result.json`
- **Structured JSON:** [`ab7e892c3e4886a91a00.json`](../../sessions/ab/ab7e892c3e4886a91a00.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## SC Tiebreaking 全面重验结果

### 完整对比表

| Exp | Model | Dataset | N | OldSC% | NewSC% | Change | SICA% | OldΔ | NewΔ | #Affected |
|-----|-------|---------|---|--------|--------|--------|-------|------|------|-----------|
| **exp-033** | Mistral-7B | FOLIO-204 | 204 | 54.41 | **55.88** | **+1.47** | 59.31 | +4.90 | +3.43 | 7 |
| exp-052 | Mistral-7B | FOLIO-204 | 204 | 53.92 | **54.41** | **+0.49** | 57.35 | +3.43 | +2.94 | 2 |
| exp-053 | Mistral-7B | FOLIO-204 | 204 | 56.37 | **55.88** | **-0.49** | 55.88 | -0.49 | 0.00 | 1 |
| exp-057 | Mistral-7B | FOLIO-204 | 204 | 57.35 | **58.33** | **+0.98** | 56.86 | -0.49 | -1.47 | 6 |
| exp-058 | Mistral-7B | FOLIO-204 | 204 | 57.84 | **58.33** | **+0.49** | 57.35 | -0.49 | -0.98 | 3 |
| exp-054 | Mistral-7B | FOLIO-204 | 204 | 54.90 | **55.39** | **+0.49** | 55.39 | +0.49 | 0.00 | 6 |
| exp-051-k4 | Mistral-7B | FOLIO-204 | 204 | 54.41 | 54.41 | 0.00 | 52.94 | -1.47 | -1.47 | 18 |
| exp-051-k8 | Mistral-7B | FOLIO-204 | 204 | 57.35 | **58.33** | **+0.98** | 56.37 | -0.98 | -1.96 | 5 |
| exp-051-k16 | Mistral-7B | FOLIO-204 | 204 | 55.88 | 55.88 | 0.00 | 57.35 | +1.47 | +1.47 | 5 |
| exp-051-k20 | Mistral-7B | FOLIO-204 | 204 | 57.35 | 57.35 | 0.00 | 59.31 | +1.96 | +1.96 | 2 |
| exp-026 | Qwen2.5-14B | FOLIO-204 | 204 | 75.00 | **75.49** | **+0.49** | 74.51 | -0.49 | -0.98 | 4 |
| exp-027 | Qwen3-14B | FOLIO-204 | 204 | 83.82 | **84.80** | **+0.98** | 84.31 | +0.49 | -0.49 | 2 |
| exp-046 | Mistral-7B | PW-600 | 600 | 39.33 | 39.33 | 0.00 | 36.50 | -2.83 | -2.83 | 11 |
| exp-034 | Qwen2.5-14B | PW-600 | 600 | 70.33 | **71.33** | **+1.00** | 70.83 | +0.50 | -0.50 | 8 |
| exp-039 | Qwen2.5-14B | PW-600 | 600 | 73.50 | **74.00** | **+0.50** | 71.50 | -2.00 | -2.50 | 12 |
| exp-020 | LLaMA-8B | FOLIO-204 | — | — | — | — | — | — | — | **N/A** |

Δ = SICA% - SC% (正值 = SICA 优于 SC)

### 关键发现

**11/15 个实验 SC 发生变化**，其中 10 个上升、1 个下降（exp-053 -0.49%）。变化范围 -0.49pp 到 +1.47pp。

**对论文核心论点 (SICA > SC) 的影响：**
- **exp-033（主实验）**：delta 从 +4.90pp 降至 +3.43pp，仍显著为正
- exp-057 (T=0.3)：delta 从 -0.49pp 恶化至 -1.47pp（SC 反超 SICA 加剧）
- exp-058 (T=0.5)：delta 从 -0.49pp 恶化至 -0.98pp
- exp-051-k8：delta 从 -0.98pp 恶化至 -1.96pp
- exp-053：delta 从 -0.49pp 变为 0.00pp（改善）
- exp-054：delta 从 +0.49pp 变为 0.00pp

**4 个实验净变化为 0**（exp-051-k4/k16/k20, exp-046）：虽然有 ties 被重新判定，但正确与错误的翻转刚好抵消。

### 受影响题目明细（仅列出影响 SC 正确率的题目）

**exp-033** (+1.47%, 5 gained / 2 lost):
| 题目ID | Old→New | GT | 结果 | 票数分布 |
|--------|---------|-----|------|---------|
| folio_42 | Unknown→True | True | GAINED | {Unknown:5, True:5} |
| folio_65 | True→False | True | LOST | {True:5, False:5, Unknown:2} |
| folio_83 | Unknown→False | False | GAINED | {Unknown:5, False:5, ...} |
| folio_99 | Unknown→True | Unknown | LOST | {Unknown:5, True:5, ...} |
| folio_100 | Unknown→True | True | GAINED | {Unknown:4, True:4, ...} |
| folio_157 | Unknown→False | False | GAINED | {Unknown:5, False:5} |
| folio_163 | Unknown→False | False | GAINED | {Unknown:5, False:5} |

**exp-053** (-0.49%, 0 gained / 1 lost):
| folio_16 | Unknown→False | Unknown | LOST | {Unknown:6, False:6} |

### 注意事项

1. **exp-020（LLaMA-8B FOLIO-204）**：数据在 westd-32608，不可达，无法重验
2. **exp-027 registry 值有误**：task 中列的 80.39% 实际应为 83.82%（文件和 registry 一致）
3. **exp-034**：registry 标注 n=93 crashed，但结果文件含 600 条完整数据
4. **Alphabetical tie-breaking 的系统性偏置**：FOLIO 答案空间 {False, True, Unknown} 中，"False" 字母序最靠前，多数 tie 将 "Unknown" 翻转为具体答案（False/True），整体倾向提升 SC

JSON 结果已分别保存至两台服务器的 `results/sc_tiebreak_revalidation_{25068,16639}.json`。

---
