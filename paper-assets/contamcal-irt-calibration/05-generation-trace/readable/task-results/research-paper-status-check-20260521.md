# research paper status check 20260521

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_paper_status_check_20260521_20260521T073316_result.json`
- **Structured JSON:** [`6a5d8c26e364f7fcd38b.json`](../../sessions/6a/6a5d8c26e364f7fcd38b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Paper compiles cleanly: 0 errors, 11 warnings (all underfull hbox — cosmetic), no undefined references/citations, 18 pages output.

---

## 状态总结

### 1. Table 3（tab:cross_seed, Bootstrap CI 表）vs 最新 n=3 数据

| 数据点 | 期望值 | 论文当前值 | 匹配 |
|--------|--------|-----------|------|
| Phi-4 MMLU CI | [-0.17, +1.39] | [-0.17, +1.39] | ✅ |
| Phi-4 MMLU mean | +0.72pp | +0.72pp (§5.3 text) | ✅ |
| Phi-4 ARC CI | [+0.51, +0.77] | [+0.51, +0.77] (§5.3 text) | ✅ |
| OLMo-2 MMLU CI | [-0.55, +2.60] | [-0.55, +2.60] | ✅ |
| OLMo-2 ARC CI | [+2.90, +3.78] | [+2.90, +3.78] | ✅ |
| Qwen-7B MMLU CI | [-1.82, -0.34] | [-1.82, -0.34] | ✅ |
| Qwen-7B ARC CI | [-2.90, -2.08] | [-2.90, -2.08] | ✅ |
| Gemma-2 MMLU CI | [+1.49, +3.14] | [+1.49, +3.14] | ✅ |
| Gemma-2 ARC CI | [-1.97, +1.42] | [-1.97, +1.42] | ✅ |
| Qwen-14B MMLU CI | [-24.99, -10.49] | [-24.99, -10.49] | ✅ |
| Qwen-14B ARC CI | [-9.38, -2.76] | [-9.38, -2.76] | ✅ |

**Table 3 完全匹配最新 n=3 BCa CI 数据。** ARC CIs 在 §5.3 正文中而非表格内，mean Δacc 以 1 位小数出现在正文中，均一致。

### 2. Open/In-Progress Review Issues

| ID | Summary | Status | Severity |
|----|---------|--------|----------|
| **R1-C2** | Cross-family MAE CI for pooled analysis not reported | **in_progress** | warning |
| **R6-W2** | S4 (Self-Critique) signal computation details insufficient | **open** | info |
| **R6-W3** | SFT training curves not reported | **open** | info |
| **R6-W4** | Within-family GSM8K PPP not reported | **open** | info |

所有 critical issues 均已 resolved。剩余 1 个 warning + 3 个 info。

### 3. 编译状态

**可编译。** pdflatex 成功输出 18 页 PDF（8 页正文 + references + appendix），0 错误，无 undefined references/citations。

### 4. 推荐下一步修改清单

1. **R1-C2 (warning)**: 补充 cross-family pooled analysis 的 MAE bootstrap CI — 唯一的 in_progress 项
2. **R6-W3 (info)**: 在 Appendix 加 SFT training loss curves 或 convergence statement — 低成本高回报
3. **R6-W4 (info)**: 报告 within-family GSM8K PPP 值 — 跑一次 IRT 即可
4. **R6-W2 (info)**: 在 Appendix 补充 S4 prompt 设计和评分细节 — 纯写作任务
5. **最终编译检查**: 确认 bibtex 完整运行（当前单次 pdflatex 编译，交叉引用可能需要二次编译）

优先级：R1-C2 > R6-W3 > R6-W4 > R6-W2。前三项涉及数据/实验，建议在 deadline 前优先完成。

---
