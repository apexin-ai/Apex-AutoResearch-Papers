# paper final response template

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_final_response_template_20260522T110854_result.json`
- **Structured JSON:** [`7b6b5d15f613d8bddb01.json`](../../sessions/7b/7b6b5d15f613d8bddb01.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

更新完成。总结：

1. **R² 数字** — 模板中无 "0.218" / "22%" 残留，全部已是 semipartial R²=0.273。

2. **新增 3 个 Q&A blocks**：
   - **Q6 (Gemini leverage)**: count_16 r=−0.80 确实由单个 leverage point 驱动（Cook's D=0.490），但 count_8 (n=50) trimmed r 从 −0.887 增强至 −0.913，论文已在 §4.3/Appendix U 中披露。
   - **Q7 (Ecological fallacy)**: BCS 是 Level-2 contextual variable，within-batch variance=0，ecological fallacy 结构上不适用；effect direction 在所有层级一致为负。
   - **Q8 (FewRel contamination)**: 三条证据线——per-type accuracy 高方差(σ=0.147)、跨模型 degradation slope 一致、IntraSub causal mechanism (ρ=0.954)——排除 memorization artifact。

3. **Appendix/Table 编号** — 全部 8 个 Q&A 中的引用与 main.aux 一致：E.1=Partial Correlation, E.2=NER Power, U=Gemini Cross-Model, Y=Relaxed Matching, C=Factorial, Table 2/5/6/10/25 均正确。

---
