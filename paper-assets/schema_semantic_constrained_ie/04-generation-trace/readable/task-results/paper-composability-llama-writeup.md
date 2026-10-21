# paper composability llama writeup

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_composability_llama_writeup_20260515T175614_result.json`
- **Structured JSON:** [`436de33be17cf9a2f5a0.json`](../../sessions/43/436de33be17cf9a2f5a0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

PDF 重编译成功。现在汇总评估结果。

---

## 论文状态评估报告

### 整体状态：**论文基本完整，数据齐全**

论文已编译为 17 页 PDF（305KB），所有 section 齐备。

### 第二步：Llama 跨模型数据 — **已全部写入论文**

**Llama LoRA SciERC constrained eval (pid 290317) 已完成：**
| 指标 | 值 |
|------|-----|
| DR | 0.09% (1/1081 triples, Evaluate-for) |
| RV | 0% |
| ET | 0% |
| CF | 0.46% (8/1757 entities) |
| R-F1 | 45.47% |
| E-F1 | 67.76% |
| Parse failures | 0 |

**数据在论文中的位置：**
- **Table 3 (cross-model)**: Qwen + Llama × SciERC + DocRED 零-shot 4 格全填 ✅
- **Table 5 (composability)**: 2 model × 2 train × 2 decode = 8 行全填 ✅，Llama LoRA S1 行数据与服务器 report 完全一致
- **§5.4 Cross-Model Validation 正文**: tightness × RV interaction, CF trade-off, F1 分析 ✅
- **§5.5 Composability 正文**: 引用了 Llama LoRA constrained 数据（DR 1.11%→0.09%, R-F1 +0.02pp, CF 0.46%）✅

### 第四步：W1 CF Fallback Analysis — **已写入 Appendix B**

`appendix_discussion.tex` 包含完整的：
- CF-DR re-routing 实验数据（CF 9.90%→0.04%, DR 0.93%→14.78%）
- Violation budget 净增 +3.99pp 分析
- 63.3% CF 来自 schema 歧义的分析
- Near-Pareto-optimal 结论

从 §7 Discussion (CF Severity 段) 和 Limitations section 均有引用。

### 修复的问题

**LaTeX bug**: Limitations section 有两处 `\\ref{...}`（双反斜杠=换行+literal text），已修复为 `\ref{...}`，PDF 重编译成功。

### 还差什么

| 项目 | 状态 | 说明 |
|------|------|------|
| Qwen DocRED LoRA | failed | registry 显示 `w5_qwen_docred_lora_training` RUNNING/failed。Limitations 已声明 "DocRED fine-tuning is not reported" |
| Registry 更新 | 待做 | `w5_llama_lora_scierc_constrained_eval` 仍为 ANALYZING，应更新为 DONE + 填入 metrics |
| 全文校对 | 待做 | 数字一致性、cross-reference 完整性需要通检 |

### 下一步建议

1. 更新 registry 中 Llama LoRA constrained eval 状态
2. 重新尝试 Qwen DocRED LoRA training（如果时间允许，DDL May 25）
3. 全文数字一致性审查 + 编译检查（无 warning/undefined reference）
4. May 19 内部稿 → submit_paper_to_review

---
