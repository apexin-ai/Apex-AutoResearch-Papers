# research table t1 full audit

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_table_t1_full_audit_20260524T083928_result.json`
- **Structured JSON:** [`538b6eb30da250d45f8a.json`](../../sessions/53/538b6eb30da250d45f8a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计数据收集完毕。以下是完整的 Table T1 (tab:cross_bench) 和 Table T2 (tab:claude_crossbench) 全行核查结果。

---

## 审计报告：Cross-Benchmark Tables 全行指标来源核查

### Table 23 (`tab:cross_bench`) — 6 行

| # | Bench | Judge | Axis | 论文 d | 论文 p | 实际来源 | 正确 d (pooled) | 正确 p | 问题 |
|---|-------|-------|------|--------|--------|----------|----------------|--------|------|
| 1 | AEval | GPT-4o | Form | .005 | .909 | **非定向** pooled d (orig−cf) | 0.005 | 0.900 | 方向约定与 R2/R3/R6 不同 |
| 2 | AEval | Qwen3 | Form | .081 | .198 | **定向** pooled d (formal−casual) | 0.081 | 0.198 | ✓ 真 d |
| 3 | AEval | Qwen3 | Verb | .375 | .0003 | **定向** pooled d (verbose−concise) | 0.375 | 0.0003 | ✓ 真 d |
| **4** | **AEval** | **Llama-70B** | **Form** | **1.120** | **<.001** | **Cohen's h (arcsine fallback)** | **0.211** | **0.012** | ⚠️ **h 错标为 d，膨胀 5×** |
| 5 | MTB | GPT-4o | Form | .167 | .016 | **定向 Cohen's d_z** (diffs-based SD) | 0.116 (pooled) | 0.016 | 公式与其他行不一致 |
| 6 | MTB | Qwen3 | Form | .149 | .007 | **定向** pooled d (formal−casual) | 0.149 | 0.007 | ✓ 真 d |

### Table 24 (`tab:claude_crossbench`) — 5 行

| # | Bench | Axis | 论文 d | 论文 p | 实际来源 | 脚本输出 d | 问题 |
|---|-------|------|--------|--------|----------|-----------|------|
| 1 | LLMBar | Form | −.021 | .721 | 定向 pooled d | −0.021 | ✓ |
| 2 | LLMBar | Verb | −.039 | .743 | 定向 pooled d | −0.040 | ✓ |
| 3 | AEval | Form | .081 | .090 | 两种算法结果一致 | 0.081 | ✓ |
| **4** | **AEval** | **Verb** | **−.243** | **.005** | **非定向** pooled d (orig−cf) | +0.298 (定向) | ⚠️ 与脚本不一致，符号翻转 |
| **5** | **MTB** | **Form** | **.245** | **<.001** | **非定向** pooled d (orig−cf) | 0.199 (定向) | ⚠️ 与脚本不一致，数值偏大 |

---

### 关键问题

**1. [严重] Row 4 of Table 23: Cohen's h 错标为 Cohen's d**

`cross_benchmark_analysis.py` 中 AlpacaEval × Llama-70B × formality 配置的 `likert_file=None`，走了 `likert_from_pairwise()` fallback：
```python
h = 2 * arcsin(sqrt(win_rate)) - 2 * arcsin(sqrt(0.5))
```
输出的是 **Cohen's h**（arcsine 变换效应量），论文将其标注为 Likert d。

- 论文值: d = 1.120（实为 h ≈ 1.160）
- 现在有 `scored_alpacaeval_llama70b_formality.jsonl` (May 24)，含 `score_formal`/`score_casual` 真 Likert 评分
- **真 Cohen's d = 0.211**（n=86, ATE=0.186, pooled SD=0.882, Wilcoxon p=0.012）
- 分类标注不变（仍为 ‡），但效应量从"大"降为"小"

**2. [中等] 表内 d 公式不一致**

Table 23 中至少使用了 3 种不同的 d 定义：
- Rows 2, 3, 6: 定向 pooled Cohen's d（formal−casual / pooled SD）
- Row 1: 非定向 pooled d（orig−cf / pooled SD）
- Row 5: 定向 Cohen's d_z（mean_diff / SD_diff），而非 pooled d
- Row 4: Cohen's h（与 d 完全不同的度量）

Table 24 中 Rows 1-3 使用定向 d，Rows 4-5 使用非定向 d，且 Row 4 符号翻转。

**3. BT 计算一致性**: 所有行均使用全部 trials（含 inconsistent pairs），**策略统一**，无问题。

### 建议修正

1. **Row 4**: 将 d 从 1.120 修正为 0.211 (p=0.012)，或在表中明确标注该行使用 Cohen's h
2. **统一 d 公式**: 全表使用定向 pooled Cohen's d（formal−casual 或 verbose−concise / pooled SD）
3. **Row 5**: 从 d_z=.167 改为 pooled d=.116，与其他行保持一致
4. **Table 24 Rows 4-5**: 使用脚本输出的定向 d（+0.298 和 0.199），或统一使用非定向并在表注说明

---
