# analysis mmlu r2 inconsistency check

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_mmlu_r2_inconsistency_check_20260522T193351_result.json`
- **Structured JSON:** [`330defe3856f23ecf769.json`](../../sessions/33/330defe3856f23ecf769.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 排查结论

### 1. 两个数字的来源

- **0.347** = `difficulty_only_R2`（仅 difficulty + difficulty²），scatter plot 标注的值。**来自正确的 difficulty-only 回归。**
- **0.377** = `R2`（full model，含 difficulty + difficulty² + n_choices + question_length + 5个 subject dummy），table 中 R²(full) 列的值。

### 2. 错误在哪

**Table 有误。** `appendix.tex` 第184行的 `R²(diff. only)` 列错误地复制了 R²(full) 的值。这是系统性错误——**所有三个 MC benchmark 都受影响**：

| Benchmark | Table 写的 diff-only | 正确值 |
|-----------|---------------------|--------|
| MMLU | 0.377 | **0.347** |
| ARC | 0.221 | **0.204** |
| HellaSwag | 0.156 | **0.140** |

FF benchmarks (GSM8K, MATH) 的两列数字正确。

### 3. Scatter plot 是对的

Scatter plot 标注的 R²=0.347 是正确的 difficulty-only R²。

### 4. 修正方案

修改 `docs/paper/appendix.tex` 第184-186行：
```latex
MMLU & 0.377 & 0.347 & $<$0.001 \\
ARC & 0.221 & 0.204 & $<$0.001 \\
HellaSwag & 0.156 & 0.140 & $<$0.001 \\
```

排查结果已保存到 `artifacts/exp004/ff_residual_analysis/mmlu_r2_inconsistency_note.json`。

---
