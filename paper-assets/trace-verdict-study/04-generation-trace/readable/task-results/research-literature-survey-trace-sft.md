# research literature survey trace sft

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_literature_survey_trace_sft_20260515T120307_result.json`
- **Structured JSON:** [`05dc2cafeb03b31318ba.json`](../../sessions/05/05dc2cafeb03b31318ba.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/_project/intermediate/literature_survey_20260515.md`。

核心发现：

**方向 1（Trace SFT）**：真实且活跃的方向，找到 8 篇直接相关工作（SemCoder/NExT/CodeExecutor/E.T./DCSH/CWM/ICPC'25/ET-CoT）。多数聚焦"模拟执行"而非分类，DCSH 和 ICPC'25 均报告 SFT 收益有限——恰好是我们的研究动机。

**方向 2（Exception/Error 训练）**：DCSH 的 5 种格式确认为 Scratchpad/NExT/SemCoder/CodeExecutor/Concise，**全部是完整语义信息，无 exception-only 变体**。ICST'25 的 stack trace FT（加源代码反而降低准确率）和 SBEST 的"98.3% bug 修复直接对应 exception"是最接近的支撑，但无人在 verdict 任务上做过 exception-only 消融。

**方向 3（信息粒度匹配）**：IB 理论 → MASS → 任务导向压缩构成理论链；Lost in the Middle + Context Length Hurts 提供 LLM 特有的实证机制。没有找到"trace 粒度 vs 代码任务复杂度"的专门研究——新颖性空间。

**方向 4（Verdict 任务）**：test verdict prediction 几乎没有被独立研究。Patch correctness 领域最成熟但主流不用 trace（APPT 79.7%、ComPass 88.35%），仅 Crex (IST 2022) 用 micro-trace 做过分类。**LLM + trace + binary verdict 三者结合是明确的文献空白。**

**综合判断：不存在"虚空画靶"风险。** 建议 framing 从"trace SFT"转向"trace 粒度选择对分类任务的影响"——DCSH 证明 full trace 对 SFT 帮助有限，我们揭示原因（信息粒度不匹配）并给出解法（exception-only）。

---
