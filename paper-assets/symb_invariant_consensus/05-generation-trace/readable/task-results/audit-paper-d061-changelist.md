# audit paper d061 changelist

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_paper-d061-changelist_20260522T210842_result.json`
- **Structured JSON:** [`10c459149738866234a5.json`](../../sessions/10/10c459149738866234a5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已生成 changelist，写入 `artifacts/d061_changelist.json`。

核心发现：

**已完成（无需修改）：** A（75.49→75.98 SC列）、B（Oracle Δ +14.22→+13.73）、C（sign test）、F（LLaMA bridge case）均已修正。

**需修改（21处确认）：**
- **D: 39.17→39.33**（9处）— appendix.tex 7处 + solutions.tex 2处。Mistral PW-D5 SC 在主表已改为 39.33，但 appendix 的 trace independence 表、DRC 表、Multi-NLI caption、BH combo 表、fine-tuned NLI 表以及 solutions.tex 叙事/表格中仍为 39.17
- **E: DeBERTa Δ 更新**（6处）— Multi-NLI 表 +1.17→+0.83, +7.00→+6.67, +11.17→+11.00；BH combo 表同步更新（含 combo 绝对值）
- **+7.00→+6.67 叙事**（4处）— abstract.tex、introduction.tex、solutions.tex 正文中引用 +7.00pp 的位置
- **G: scatter plot**（2处）— gap 15.83→15.67, gain 7.00→6.67

**潜在级联变更（17处，目标值待确认）：** RoBERTa/BART Δ 值（6处表格+1处叙事）、DRC combo 精确值（2处）、fine-tuned NLI Δ（4处含叙事）、BH p-values（3处）、scatter plot 其余数据点（3处）。这些需要 D061 重算输出确定具体目标值。

---
