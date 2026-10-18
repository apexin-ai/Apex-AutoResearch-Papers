# writing method relatedwork draft

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_writing_method-relatedwork-draft_20260515T035316_result.json`
- **Structured JSON:** [`d5e2000135af34f39220.json`](../../sessions/d5/d5e2000135af34f39220.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个文件已完成并注册：

**`method_framework.md`** — Section 3 完整框架：
- 3.1 Problem Formulation: 定义 SCS、BCS、schema complexity 双因子模型
- 3.2 Controlled Experiment Design: count curve + within-count BCS correlation + multi-channel degradation模型（count→recall, confusability→precision）
- 3.3 SDGD Framework: 5 步算法描述 + `\begin{algorithm}` 格式伪代码 + adaptive threshold（$\tau = \mu + k_\sigma \cdot \sigma$）+ oracle baseline 区分 + 复杂度分析
- 3.4 SDGD-zero vs SDGD-cal: 两个变体的数据需求、信号来源、校准流程、对比表

**`related_work_draft.md`** — Section 2 三维度组织：
- 2.1 Schema Decomposition for IE: UniNER, LLM-PEE, PARSE, KGGen, DEE, SPT, DLISC（7篇），明确 SDGD 与每个方法的区别
- 2.2 Confusability-Aware NLP: IEPile（训练时 vs 推理时）、Familiarity（评估偏差 vs 提取混淆）、CROSSAGENTIE/CMAS（reactive debate vs proactive decomposition）、Lost-in-the-Middle
- 2.3 LLM-Based IE: GoLLIE, Code4UIE, KnowCoder, Self-improving NER, ReasoningNER, ZeroNER, GLiNER/GLiNER2, NuNER, survey

**`maven_description.md`** — 1 段约 150 words：168 types、FrameNet hierarchy、4480 docs、118K mentions、sibling confusion 14.6-19.8%、三个选择理由（cross-task, larger schema, external confusability evidence）

---
