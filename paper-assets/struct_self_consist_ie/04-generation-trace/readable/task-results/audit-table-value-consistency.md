# audit table value consistency

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_table-value-consistency_20260519T181739_result.json`
- **Structured JSON:** [`7af3b91ecb43336a8051.json`](../../sessions/7a/7af3b91ecb43336a8051.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Audit complete. Here are the findings:

---

## 审计结果

### 确认的不一致

| 文件 | 表格/位置 | 指标 | 当前值 | 应为值 | 数据源 |
|------|-----------|------|--------|--------|--------|
| appendix.tex:231 | inline (cross\_selection分析段落) | Qwen FewNERD degen | 12.7% | 13.0% | tab:fewnerd, tab:scale\_comparison, 以及所有其他引用均为13.0% |
| appendix.tex:231 | inline (同上) | LLaMA-Qwen degen差值 | +10.7pp | +10.4pp | 23.4% - 13.0% = 10.4% |

### 需要确认的潜在不一致

| 文件 | 表格/位置 | 指标 | 当前值 | 其他表值 | 说明 |
|------|-----------|------|--------|----------|------|
| appendix.tex:1369 | tab:calibration | Few-NERD greedy F1 | .771 | .748 (tab:fewnerd等) | 差2.3pp，无法用seed/rounding解释，caption未说明原因 |
| appendix.tex:1368 | tab:calibration | CoNLL greedy F1 | .909 | .908 (tab:fewnerd等) | 0.1pp差异，可能是rounding或non-gold-filtered |

### 全部通过的核心数值

- **Degen rates**: SciERC 17.8%、CoNLL 61.7%、72B ZS (21.0%/46.2%/67.7%) — 所有表格和正文引用一致
- **Construction deltas**: SciERC +1.02pp、FewNERD +1.40pp、CoNLL -0.39pp、72B ZS +1.53pp — abstract/intro/experiments/discussion/conclusion 全部一致
- **Signal ρ**: tab:quality\_estimation 数值与正文inline引用、appendix表格交叉引用均一致
- **AUROC**: "up to 0.82" = .816 rounded，一致
- **旧错误值(48.4%, 49%)**: 未在任何tex文件中发现
- **CoNLL degen 符号**: -0.39pp 为负，正确

### 修复建议

appendix.tex 第231行，将：
```
Qwen ($12.7$\%)
```
改为：
```
Qwen ($13.0$\%)
```

同行将 `$+10.7$~pp` 改为 `$+10.4$~pp`。

tab:calibration 的 Few-NERD greedy=.771 建议在caption中补充说明其与主表.748差异的原因（不同checkpoint/subsample/protocol）。

需要我直接执行修复吗？

---
