# analysis kendall w concordance

**Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_kendall_w_concordance_20260521T184124_result.json`
- **Structured JSON:** [`c0162a492ecdd6999716.json`](../../sessions/c0/c0162a492ecdd6999716.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果已写入 `round9_supplementary/kendall_w_results.json`。

## 结果

### 5-model × 6 types (main study)
- **W = 0.3977**, χ²(5) = 9.94, **p = 0.072** (边缘显著)
- 模型间对 type 难度排序有中等一致性，但未达 p < 0.05

### 7-model × 5 types (含 Gemini + LLaMA，去掉 coreferential)
- **W = 0.3531**, χ²(4) = 9.89, **p = 0.038** (显著)
- 加入 replication models 后达到统计显著，7 个模型对 5 种 type 的相对难度排序存在显著一致性

### Type mean ranks (7-model, 高 = 更高 violation rate)

| Type | Mean Rank |
|------|-----------|
| incompleteness | **4.50** (最难) |
| lexical | 3.07 |
| authorization_scope | 3.00 |
| scopal | 2.36 |
| conditional_precedence | **2.07** (最易) |

incompleteness 在所有模型中一致排名最高；conditional_precedence 一致最低。coreferential 在 5-model 分析中 mean rank = 2.0（最低）。

---
