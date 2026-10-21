# analysis exp 017 strategyqa v2

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp-017-strategyqa-v2_20260517T040206_result.json`
- **Structured JSON:** [`44f392e9dc7126192201.json`](../../sessions/44/44f392e9dc7126192201.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果摘要

```
## exp-017-strategyqa-v2 Results
- SICA accuracy: 18.33% (11/60)
- SC accuracy:   16.67% (10/60)
- Gap: +1.67pp (SICA > SC)
- N problems: 60, K=12, T=0.7
- C0 (multi-candidate rate): 6.7% (4/60)
- Constraint extraction rate: 28.3% (17/60)
- Contradiction rate: 6.7% (4/60)
- SICA-SC agreement: 98.3% (59/60)
- Wall time: 7.3 min
- Completion flag: EXP017_DONE, EXIT_CODE=0
```

## 严重问题：答案提取失败

**73.3% 的问题 (44/60) 答案为空**，SC 和 SICA 均未能提取到有效答案。日志中大量 `extraction_method=none, answer=NONE` 警告证实了这一点。

这意味着实际有效的评估仅覆盖 16/60 个问题，实验数据 **不可靠**。

根因推测：answer extraction regex/parser 针对 Yes/No 格式的适配有问题。模型生成了推理 trace 但 extractor 无法从中解析出 "Yes"/"No" 答案。

## 结论

**INVALID** — 答案提取管道在 StrategyQA (Yes/No) 格式上严重失效（73% 空答案），accuracy 数字 (18%/17%) 远低于随机基线 (50%)，不能得出任何关于 SICA vs SC 的有效结论。需要修复 answer extraction 后重跑。

---
