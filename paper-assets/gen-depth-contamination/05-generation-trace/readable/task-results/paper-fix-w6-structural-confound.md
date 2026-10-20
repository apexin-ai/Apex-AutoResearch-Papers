# paper fix w6 structural confound

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_fix_w6_structural_confound_20260516T032107_result.json`
- **Structured JSON:** [`d419dcfd3110d9c1094e.json`](../../sessions/d4/d419dcfd3110d9c1094e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。Discussion 第 6.4 节现在包含完整的三层论证：

1. **方向相反**（line 41-42）：depth-0 人类文本更短（~191 tokens），generated 更长（195-256），length asymmetry 让 0v1 更保守而非虚高
2. **depth 1-5 稳定**（line 44-46）：各模型内 depth 1-5 token 数变化 ≤4 tokens，无单调递减趋势
3. **OLMo 零截断控制**（line 48-49）：OLMo 全部 256 tokens、<1% EOS 截断，K*=2 仍成立（1v2 AUC=0.615, 2v3=0.550）

配套设施已到位：
- Appendix 表格 `tab:token_length`（appendix.tex line 145-173）含 5 个模型配置 + 4 个解码策略的逐 depth token 统计和 EOS 截断率
- Limitations (12) 已交叉引用 `Section~\ref{sec:length_confound}` 和 `Table~\ref{tab:token_length}`
- appendix_extended.tex Extended Limitations 也有 token length 段落呼应

---
