# code paper sensitivity fix

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_paper-sensitivity-fix_20260519T221357_result.json`
- **Structured JSON:** [`0278d50525e98e269af4.json`](../../sessions/02/0278d50525e98e269af4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部修改完成。汇总：

**Sensitivity 更新（6 处）：**
1. `method.tex:59` — "5/5 families" → "all five families...180/180 model--seed--threshold pairs"
2. `results.tex:11` — "150/150 model-combination pairs" → "180/180 model--seed--combination pairs"
3. `results.tex:27` — 添加 "(six model--seed configurations;"
4. `appendix.tex:158` — "All five families" → "All six model--seed configurations"
5. `appendix.tex:170` — Table 7 添加 Qwen-7B (s123) 行，s42 行加标注
6. `appendix.tex:175` — "all five families" → "all six model--seed configurations"

**V-recovery 修复（3 处）：**
1. `limitations.tex:9` — "Single seed." → "Seed coverage."
2. `abstract.tex:1` — "partial rebound" → "partial-to-full rebound"
3. `limitations.tex:10` — "Triple-seed validation...is in progress" 保持不变（s0 未完成，描述仍准确）

---
