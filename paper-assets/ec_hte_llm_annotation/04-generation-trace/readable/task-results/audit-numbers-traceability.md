# audit numbers traceability

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_numbers-traceability_20260524T042839_result.json`
- **Structured JSON:** [`160161b6eb8575fb7a46.json`](../../sessions/16/160161b6eb8575fb7a46.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

核查完成。报告已写入 `artifacts/_project/report/number_audit_report.md`。

**摘要：~80 个关键数字中发现 3 CRITICAL + 5 WARNING。**

### 必须修复（CRITICAL，全在 method.tex:61 同一句话）

1. **DGP 标签错误**：写了 "outcome-side error alone (DGP C)"，但 DGP C 是 "both errors"，应改为 DGP B
2. **PPCI |bias| 值无出处**：声称 0.003–0.004，但 PPCI table 中 DGP B 的 PPCI bias 是 0.015/0.020，不匹配
3. **27% RMSE advantage 无法复现**：从 PPCI table DGP A 计算 EC-HTE vs PPCI 的 RMSE 优势约 38%，非 27%

### 建议修复（WARNING）

- **W2**: method.tex:12 "≤4%" 与 method.tex:21 "<5%" 内部不一致（K4 实际 4-5%），统一为 "<5%"
- **W1**: AUC=0.86 在 registry 中对应的实际值是 0.833（可能是不同评分规则），需确认
- W3/W4: 两处 ≤0.001 的四舍五入差异（影响极小）
- W5: Figure 1 "7.5% subgroup estimates" 未在 registry 中独立验证

### 通过

其余全部数字（R²≥0.97, 14.9%, 7.4×, 260/520, 2.86×/2.41×, 93.8%, 89%, 5.9×, 4.7×, 4.9×, γ_T=0.10→75%, 11 CMs, Table 1 全部 18 个单元格等）均与 registry 精确匹配或在合理四舍五入范围内。跨文件一致性良好。

---
