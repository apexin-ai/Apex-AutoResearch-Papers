# analysis error categorization discordant

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_error-categorization-discordant_20260520T002049_result.json`
- **Structured JSON:** [`7b7bc74ec7b382b8ce27.json`](../../sessions/7b/7b7bc74ec7b382b8ce27.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。核心发现：

### 1. Debate Discordant (60题 SC→Wrong)

- **答案类型偏斜严重**：False 类被翻转 82.8%（29个SC对的里24个被Debate翻错），True 类 63.9%，Unknown 仅 25.5%。Debate 对有确定答案（True/False）的题破坏力远大于 Unknown 题。
- **Fallback 为 0**：这 60 题全部没有触发 fallback 机制——Debate 过程"成功"完成但得出了错误结论，说明问题不在 debate 失败，而在 debate 产出的 constraints 本身质量有问题。
- **Mean valid debates 反而更高** (2.93 vs baseline 2.52)：更多的有效 debate 反而导致更多错误，符合"debate 引入 confident but wrong constraints"的假说。

### 2. Contrastive Discordant (34题)

- **Degenerate 率为 0%**（baseline 20.1%）：全部 34 题都是非退化的——Contrastive 产出了 constraints 但方向错误，非 constraint 缺失问题。
- **Pro/con 数量更高** (8.32 pro + 7.32 con vs baseline 4.97 + 4.28)，imbalance 也更大 (1.0 vs 0.68)：这些题 constraint 数量充足但 pro 偏多，pro-biased scoring 可能导致了错误。
- **Unknown 过度翻转**：Unknown 类占 41%（14/34），而 baseline 仅 34%，Unknown 题更容易被 Contrastive 翻错。
- **语言复杂度更高**：negation 97.1% (vs 76.5%), conditional 82.4% (vs 61.8%), quantifier 79.4% (vs 70.6%)。

### 3. 跨方法重叠

- **重叠仅 15 题**，Jaccard=0.19，两种方法的失败模式高度不同。
- **Debate 独有 45 题**偏向 True/False（17+19=36, 80%），且语言复杂度接近 baseline。
- **Contrastive 独有 19 题**偏向 Unknown（10/19=53%），且语言复杂度极高（negation 94.7%, conditional 84.2%）。
- **两者都翻转的 15 题** 100% 含否定词，答案类型均匀分布——这些是对两种 constraint 提取方法都具有挑战性的"universally hard"题目。

---
