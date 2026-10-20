# analysis exp013 constraint ablation

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp013-constraint-ablation_20260521T225710_result.json`
- **Structured JSON:** [`9b1a39b4049d0828d485.json`](../../sessions/9b/9b1a39b4049d0828d485.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。结果非常清晰：

## 结果

### Qwen2.5-14B (exp036 + exp032)

| Method | FOLIO-204 Acc | PW-600 Acc | Overall Acc |
|--------|--------------|-----------|------------|
| MaxSAT (SICA) | 0.7549 (154/204) | 0.7150 (429/600) | 0.7251 (583/804) |
| Count-only | **0.7598** (155/204) | **0.7400** (444/600) | **0.7450** (599/804) |

MaxSAT vs Count-only agreement: FOLIO 98.04%, PW 93.83%

### DeepSeek-R1-Distill-8B (FOLIO, with raw constraints)

| Method | FOLIO Acc |
|--------|----------|
| MaxSAT (SICA) | 0.7451 |
| Count-only (trace vote) | 0.7451 |
| Constraint-count | 0.7451 |
| Random-weight | 0.6814 |

MaxSAT vs Count-only agreement: **100%**
MaxSAT vs Random-weight agreement: 83.33%

## 结论

1. **MaxSAT 没有贡献**：Count-only 在 14B 上反而高 2pp（0.7450 vs 0.7251）。在 8B 上两者 100% 一致。MaxSAT solver 的加权聚合相对于简单计票没有正向收益。

2. **Random-weight 显著更差**（-6.4pp），说明 constraint 的数量结构有意义（不能随机乱赋权），但 MaxSAT 特定的满足性求解并不比"数票"更好。

3. **Disagreement 案例**显示 MaxSAT 有时会用少数 trace 的高权重 override 多数投票（如 PW 中 3 票 vs 9 票），这种 override 有正有负，净效果为负。

---
