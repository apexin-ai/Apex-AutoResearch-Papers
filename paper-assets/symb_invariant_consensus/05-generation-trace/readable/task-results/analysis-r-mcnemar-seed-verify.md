# analysis r mcnemar seed verify

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_r-mcnemar-seed-verify_20260520T105518_result.json`
- **Structured JSON:** [`503a2a4d69a8c16700db.json`](../../sessions/50/503a2a4d69a8c16700db.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部分析完成。以下是完整报告。

---

## Direction R: McNemar Exact Test 报告

### 1. Seed 一致性

**确认：SC traces 一致。** R脚本直接从 `results/exp033_mistral_7b_folio204/sc_answer_matrix.json` 加载已有的12条SC traces，不重新生成。combo策略是将NLI预测作为第13票加入。

- R结果中SC baseline = 111/204 = 54.41%，与exp033完全吻合
- **修正**：exp033未使用显式seed（`run_full_mvp.py --seed`默认`None`，日志无seed记录）。用户所述"seed=42"未在代码/日志中找到证据。但这不影响一致性——R直接复用exp033的traces文件。

### 2. 模型注意

结果JSON记录的实际模型是 **`/root/models/deberta-large-mnli`**（`microsoft/deberta-large-mnli`），非任务描述中的 `cross-encoder/nli-deberta-v3-base`。请确认论文中引用正确的模型名。

### 3. 核心数字

| 指标 | 值 |
|------|-----|
| SC baseline | 111/204 = **54.41%** |
| NLI-SICA-combo | 118/204 = **57.84%** |
| Delta | **+3.43pp** (+7 problems) |

### 4. McNemar 2x2 Contingency Table

|  | Combo Correct | Combo Wrong |
|--|:---:|:---:|
| **SC Correct** | 110 | 1 |
| **SC Wrong** | 8 | 85 |

- b (SC correct, combo wrong) = **1**
- c (SC wrong, combo correct) = **8**
- Discordant pairs = **9**

### 5. McNemar Exact p-value

**p = 0.0391** (two-sided binomial test, min(1,8) out of 9 trials)

- **Significant at α=0.05**: Yes
- **Significant at α=0.01**: No

### 6. Per-label McNemar

| Label | n | b | c | discordant | p |
|-------|---|---|---|------------|---|
| True | 72 | 1 | 3 | 4 | 0.625 |
| False | 63 | 0 | 4 | 4 | 0.125 |
| Unknown | 69 | 0 | 1 | 1 | 1.000 |

per-label均不显著（样本太小，discordant pairs仅1-4对）。

### 7. 95% CI for Accuracy Difference

| 方法 | 95% CI |
|------|--------|
| Normal approximation | [0.59pp, 6.28pp] |
| Bootstrap (10000 resamples) | [0.98pp, 6.37pp] |

两种方法CI均不包含0，与p<0.05一致。

### 结论

NLI-SICA-combo相比SC baseline的+3.43pp提升**统计显著**（McNemar exact p=0.039, α=0.05），但效应量较小——9对discordant pairs中combo赢8对、输1对。CI上界约6pp，说明真实效应可能在0.6-6.4pp之间。如果论文需要report，建议同时给出p值和discordant pair counts，因为n=9的discordant pairs使得结果对单题翻转非常敏感。

---
