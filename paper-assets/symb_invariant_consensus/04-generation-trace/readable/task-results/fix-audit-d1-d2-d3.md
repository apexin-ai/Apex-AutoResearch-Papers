# fix audit d1 d2 d3

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_audit-d1-d2-d3_20260524T044736_result.json`
- **Structured JSON:** [`787b0f30566d66d2d5c1.json`](../../sessions/78/787b0f30566d66d2d5c1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

编译通过，无错误。ALG@line 警告是既有问题（多个 algorithm 环境共享行号），不影响输出。

## 修改汇总

### D1: BH correction p-value 修正

**根因**：BH 实现缺少单调性强制步骤。`0.011 × 6/1 = 0.066` 是 rank-1 的初始值，但标准 BH 要求 `min(0.066, rank-2 的 0.042) = 0.042`。`statsmodels.multipletests(method='fdr_bh')` 验证两个条件均 adj p = 0.042 < 0.05，显著。

**5 处修改：**

| 文件 | 行 | 旧值 | 新值 |
|---|---|---|---|
| `experiments.tex` | 5 | "No condition shows a significant SICA effect after FDR control...both reach adjusted p = 0.066" | "Two confirmatory conditions show significant degradation after BH FDR control...adj. p = 0.042...No condition shows a significant positive effect" |
| `experiments.tex` | 10 | "No condition shows a significant gain after BH correction" | "Two conditions show significant degradation after BH correction...no condition shows a significant gain" |
| `experiments.tex` | 10 | "{*} uncorrected p < 0.05 (BH adj. p = 0.066)" | "{*} BH adj. p = 0.042" |
| `experiments.tex` | 46 | "BH adj. p = 0.066" | "BH adj. p = 0.042" |
| `appendix.tex` | 596 | "BH adj. p = 0.066" | "BH adj. p = 0.042" |
| `appendix.tex` | 697 | "BH adj. p = 0.066, m=6" | "BH adj. p = 0.042, m=6" |

### D2: Abstract 词数

191 词，已在 200 限制内，无需修改。

### D3: "14× over zero-shot" 修正

| 文件 | 行 | 旧值 | 新值 |
|---|---|---|---|
| `solutions.tex` | 35 | `$14\times$ over zero-shot` | `up to $14\times$ over zero-shot (LLaMA-8B)` |

---
