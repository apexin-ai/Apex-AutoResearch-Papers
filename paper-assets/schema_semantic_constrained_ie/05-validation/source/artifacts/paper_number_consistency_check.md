# 论文数字一致性检查报告

**日期**: 2026-05-15
**论文目录**: `artifacts/_project/paper/`
**检查范围**: Llama SciERC 2×2 composability matrix 数据入表验证

---

## 表格编号映射（从 main.aux 确认）

| 编号 | Label | 内容 | 位置 |
|------|-------|------|------|
| Table 1 | tab:prompt_comparison | Violation landscape | section3_violation_landscape.tex |
| Table 2 | tab:scierc-ablation | SciERC 5-way ablation (Qwen) | section5_scierc_draft.tex |
| Table 3 | tab:composability | Composability matrix | section5_scierc_draft.tex:142-169 |
| Table 4 | tab:docred-ablation | DocRED ablation (Qwen) | section5_docred_draft.tex |
| Table 5 | tab:cross-model | Cross-model validation | section5_crossmodel_draft.tex |
| Table 6 | tab:runtime | Runtime overhead | section5_runtime.tex |
| Table 10 | tab:lora-per-relation | LoRA per-relation DR (Qwen) | appendix_discussion.tex |
| Table 11 | tab:llama-per-relation-dr | Llama DocRED per-relation | appendix_llama_per_relation.tex |

---

## 1. Llama SciERC Zero-shot 数据

### Table 5 (cross-model, section5_crossmodel_draft.tex)

| 指标 | 期望值 | 论文值 | 状态 |
|------|--------|--------|------|
| Llama (U) DR | 13.34% | 13.34 | ✅ |
| Llama (U) R-F1 | 2.68% | 2.68 | ✅ |
| Llama (U) E-F1 | 23.56% | 23.56 | ✅ |
| Llama (S1) DR | 0.08% | 0.08 | ✅ |
| Llama (S1) R-F1 | 2.54% | 2.54 | ✅ |
| Llama (S1) E-F1 | 23.49% | 23.49 | ✅ |

### §5.4 正文（section5_crossmodel_draft.tex）

| 引用 | 期望值 | 论文文本 | 状态 |
|------|--------|----------|------|
| ΔDR | -99.4% | "99.4% for Llama (13.34→0.08%)" (line 53) | ✅ |
| ΔR-F1 SciERC | -0.14pp | "Llama: $-$0.14/$+$0.29pp" (line 55) | ✅ |

---

## 2. Llama SciERC Fine-tuned LoRA 数据

### Table 3 (composability matrix, section5_scierc_draft.tex:142-169)

**当前状态**: 表格标题明确写 "Qwen3-8B, 551 documents"，仅包含 Qwen 的 4 行数据。

| 指标 | 期望值 | 论文值 | 状态 |
|------|--------|--------|------|
| Llama LoRA Unconstrained DR | 1.11% | — | ❌ 缺失 |
| Llama LoRA Unconstrained R-F1 | 45.45% | — | ❌ 缺失 |
| Llama LoRA Unconstrained E-F1 | 67.76% | — | ❌ 缺失 |
| Llama LoRA Constrained DR | 0.09% | — | ❌ 缺失 |
| Llama LoRA Constrained R-F1 | 45.47% | — | ❌ 缺失 |
| Llama LoRA Constrained E-F1 | 67.76% | — | ❌ 缺失 |
| Llama LoRA ΔDR | -91.9% | — | ❌ 缺失 |
| Llama LoRA ΔR-F1 | +0.02pp | — | ❌ 缺失 |

**全文搜索确认**: grep `45.45|45.47|67.76|1.11|91.9` 在 paper/ 目录下零命中（排除 .log/.bib 无关匹配）。Llama LoRA 数据**完全不在论文任何位置**。

### §5.2 Composability 段落（section5_scierc_draft.tex:125-140）

当前段落仅讨论 Qwen LoRA 数据：
- "Fine-tuning alone raises R-F1 from 8.23 to 43.86" → Qwen
- "DR entirely (1.95→0%)" → Qwen
- "R-F1 changes by −0.09pp (43.86→43.77)" → Qwen

❌ 无任何 Llama LoRA 讨论。

### Appendix B（appendix_discussion.tex）

- CF-DR Trade-off 段落引用 "Table composability" 但仅讨论 Qwen CF=1.18%
- Per-Relation DR Elimination (Table 10) 仅 Qwen LoRA
- ❌ 无 Llama LoRA 数据

---

## 3. Qwen SciERC 数据（交叉验证）

### Table 3 Qwen 行

| 指标 | 期望值 | 论文值 | 状态 |
|------|--------|--------|------|
| Zero-shot Unconstrained DR | 15.37% | 15.37 | ✅ |
| Zero-shot Unconstrained R-F1 | 8.23% | 8.23 | ✅ |
| Zero-shot Constrained DR | 0.93% | 0.93 | ✅ |
| Zero-shot Constrained R-F1 | 8.36% | 8.36 | ✅ |
| LoRA Unconstrained DR | 1.95% | 1.95 | ✅ |
| LoRA Unconstrained R-F1 | 43.86% | 43.86 | ✅ |
| LoRA Constrained DR | 0.0% | 0 | ✅ |
| LoRA Constrained R-F1 | 43.77% | 43.77 | ✅ |

### Table 5 Qwen 行

| 指标 | 期望值 | 论文值 | 状态 |
|------|--------|--------|------|
| Qwen SciERC (U) DR | 15.37% | 15.37 | ✅ |
| Qwen SciERC (U) R-F1 | 8.23% | 8.23 | ✅ |
| Qwen SciERC (S1) DR | 0.93% | 0.93 | ✅ |
| Qwen SciERC (S1) R-F1 | 8.36% | 8.36 | ✅ |

---

## 4. 需要注意的下游影响

如果将 Llama LoRA 数据加入论文，以下位置的措辞需要更新：

### 4a. Limitations（main.tex:70）
当前: "Composability with fine-tuned models is validated on SciERC LoRA (DR=0%, R-F1 loss <0.1pp)"
- Llama LoRA DR=0.09%（非 0%），需改为 "DR≤0.09%" 或分模型说明
- R-F1 loss = +0.02pp（<0.1pp）仍成立 ✅

### 4b. Abstract（abstract.tex:14）
当前: "Composed with LoRA fine-tuning on SciERC, OntoCoDec achieves DR=0% at R-F1 43.77 (loss <0.1pp)"
- 这是 Qwen 数据，若加入 Llama 需要泛化措辞（如 "DR≤0.09%"）

### 4c. Introduction（section1_introduction_draft.tex:27）
当前: "composability with fine-tuning (DR→0% at <0.1pp F1 cost)"
- 同上，Llama DR=0.09% 使 "DR→0%" 不再精确

### 4d. §7 Conclusion（section7_conclusion_compressed.tex:13）
当前: "Fine-tuning reduces CF by 88% (+9.82pp→+1.18pp)"
- 这是 Qwen 数据，Llama LoRA 的 CF 数据未知，可能需要补充

### 4e. Table 3 标题
当前: "Composability matrix on SciERC (Qwen3-8B, 551 documents)"
- 需扩展为 2 models × 2 settings × 2 modes = 8 行

---

## 5. 总结

### ✅ 已正确出现（6/6 Llama zero-shot 数字 + 全部 Qwen 数字）
- Table 5: Llama SciERC zero-shot 全部 6 个数字完全匹配
- §5.4 正文: ΔDR=-99.4%, ΔR-F1=-0.14pp 正确引用
- Table 3/5: 全部 Qwen 数字精度一致

### ❌ 完全缺失（8/8 Llama LoRA 数字）
- **Table 3**: 无 Llama LoRA 行（DR=1.11%/0.09%, R-F1=45.45%/45.47%, E-F1=67.76%/67.76%）
- **§5.2 正文**: 无 Llama LoRA 讨论
- **Appendix B**: 无 Llama LoRA 数据
- **全文**: grep 确认零命中

### 建议修改列表

1. **Table 3 扩展**: 添加 Llama LoRA 2 行（Unconstrained + Full S1），改标题为双模型
2. **§5.2 composability 段落**: 添加 Llama LoRA 结果讨论（DR: 1.11%→0.09%, ΔDR=-91.9%; R-F1: 45.45→45.47, +0.02pp）
3. **Abstract**: "DR=0%" → "DR≤0.09%" 或 "near-zero DR"
4. **Introduction**: "DR→0%" → "DR→near-zero" 或 "DR≤0.09%"
5. **Limitations**: "DR=0%" → "DR≤0.09%" 并注明 Llama DR 不为零
6. **Appendix B**: 考虑添加 Llama LoRA per-relation 分析（类似 Table 10 的 Llama 版本）
7. **注意**: Llama LoRA ΔDR=-91.9%（vs Qwen -100%），composability 的 claim 从 "DR elimination" 变为 "91.9-100% DR reduction"，需调整措辞强度
