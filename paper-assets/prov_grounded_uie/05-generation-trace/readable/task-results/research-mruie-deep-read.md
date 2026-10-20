# research mruie deep read

**prov grounded uie** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_mruie-deep-read_20260512T112106_result.json`
- **Structured JSON:** [`74d8ab8ad4bc842223c3.json`](../../sessions/74/74d8ab8ad4bc842223c3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已完成并注册。核心结论：

**Novelty 威胁：🟢 低 → 建议继续**

MR-UIE 的 faithfulness 与 ProvUIE **同词异义**：
- **MR-UIE faithfulness** = 推理过程是否遵循 schema（CoT chain 质量检查），不输出 evidence span，不用 NLI，实现细节甚至未公开
- **ProvUIE faithfulness** = 抽取结果是否被输入文本的具体 span 蕴含（span-level NLI + char-IoU），模型同步输出 evidence span

两者创新方向正交：MR-UIE 做多视角推理策略生成，ProvUIE 做 evidence-aware provenance reward。

**行动建议**：
1. 无需 pivot，按 ROADMAP 继续 MVP
2. 论文中避免用 "faithfulness reward"（撞词），改用 "evidence provenance reward" 或 "grounding reward"
3. Related work 中将 MR-UIE 归入 "reasoning-enhanced UIE"，与 ProvUIE 的 "evidence-grounded extraction" 区分

详细对比表和实验设置见 `artifacts/mruie_analysis_report.md`。

---
