# paper case study appendix

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_case_study_appendix_20260518T194133_result.json`
- **Structured JSON:** [`1424b6d9a090d7135496.json`](../../sessions/14/1424b6d9a090d7135496.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部通过。汇报：

**完成的工作：**

1. **远程数据提取**（cqa1 上 `/root/schema-dag-extraction/artifacts/case_study/case_study_data.json`）：
   - FewRel 80-rel: 从 3 seeds × 25 batches 的 72K 预测中统计 25,075 次 type confusion，272 个 unique pair
   - Few-NERD: 从 66-type 全 schema 提取 3,398 次 confusion，820 个 unique pair
   - 5 个高 SCS 错误实例（SCS > 0.90）

2. **LaTeX appendix**（`main.tex` 新增 Section "Qualitative Error Analysis", label `app:error-analysis`）：
   - Table 1 (RE): FewRel top-10 confused pairs，最高 confusion pair 是 *instance of*/*taxon rank*（N=875, SCS=0.53），最高 SCS pair 是 *followed by*/*follows*（SCS=0.90, N=400）
   - Table 2 (NER): Few-NERD top-10 confused pairs，最高是 *person-other*/*person-politician*（N=121, SCS=0.93）
   - Table 3: 3 个具体错误实例，展示 argument directionality reversal (participant/participant of)、containment inversion (contains/located in)、meronymy-membership conflation (part of/member of)

3. **正文引用**（`results.tex` §4.2 末尾添加一句指向 `Appendix~\ref{app:error-analysis}`）

**选择错误实例的理由**：3 个实例分别代表三种 high-SCS confusion 模式（方向反转、逆关系、上下位混淆），且 SCS 均 > 0.90，与 §4.2 的 pairwise SCS-confusion correlation 论述直接对应。

---
