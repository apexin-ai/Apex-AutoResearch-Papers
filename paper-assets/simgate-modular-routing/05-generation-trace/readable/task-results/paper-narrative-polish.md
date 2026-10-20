# paper narrative polish

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_narrative-polish_20260517T101309_result.json`
- **Structured JSON:** [`3a452cf7824590f37c14.json`](../../sessions/3a/3a452cf7824590f37c14.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All fixes applied. Here's the full report:

---

## 1. Introduction 故事线连贯性

**结构评估**：
- 开头从具体问题切入 ✓（"must repeatedly decide *how* to compute"，直接用 ScienceWorld 实例）
- 不是泛泛 "LLMs have shown remarkable capabilities..." ✓
- 段落逻辑过渡清晰 ✓

**问题**：

| 位置 | 问题 | 建议 |
|------|------|------|
| introduction.tex:22-23 | 重复段：78.9%、DAF=90.4% 在第12行已给出，第22行原样重复 | 删除此段或合并到第12行段末 |
| introduction.tex:22-28 | 结构偏重：正文 contributions 前有3个密集结果段（lines 22、24、28），读起来像 mini-Results | 建议压缩为1段概述，将具体数字留给 Experiments |
| 结构层面 | 缺少显式的"问题重要性"段。从"现有方法"直接跳到"本文提出" | 在 line 10 后加1-2句说明"理解 routing signal 对部署效率/安全性设计的实际意义" |

**Contribution 支撑**：
- Contribution 1 → §3 (collection-labeling-daf) ✓
- Contribution 2 → §4 (death-decomp, router-diagnostic) ✓
- Contribution 3 → §4.4 (cross-env), discussion, appendix ✓

---

## 2. Related Work Positioning

**结构评估**：
- 按主题分4组 ✓（Tool Use, Adaptive Computation, Counterfactual RL, Safe RL）
- 每组结尾有明确定位（"we ask...", "we reveal...", "our approach differs..."） ✓
- 无 "To our knowledge..." 放错位置 ✓

**问题**：

| 位置 | 问题 | 建议 |
|------|------|------|
| related_work.tex:19 | "Safe RL and LLM Agents" 段混合了 6 个不同主题：safe RL survey、environments (ScienceWorld/ALFWorld/AgentBench)、reasoning methods (ReAct/Reflexion/LATS)、hallucination detection (SelfCheckGPT) | 拆为 "LLM Agent Environments" 和 "Safe RL" 两段，或至少在段内按子类分组 |
| related_work.tex:5 | Tool Use 段有轻微列举感（"Toolformer teaches... ToolkenGPT represents... ART decomposes... Chameleon composes... ReTool applies..."），5个连续主语 | 可接受（有结论句收束），但可考虑分为 "early methods" 和 "recent concurrent work" 两个自然组 |

**引用覆盖**：
- 直接相关方法 ✓（Toolformer, ART, Chameleon, ReTool, concurrent 2026 work）
- Baseline 论文 ✓（ReAct, Reflexion）
- 评测环境 ✓（ScienceWorld, ALFWorld, AgentBench, MATH）
- Routing methods ✓（CogRouter, ARES, RouteLLM, MTRouter）
- 理论基础 ✓（safe RL survey, counterfactual RL）

---

## 3. AI 风格检查

**已直接修复**（4处 -ing 短语结尾）：

| 文件:行 | 原文 | 修复 |
|---------|------|------|
| experiments.tex:39 | "...demonstrating that the decomposition can diagnose..." | → "...mechanism. This confirms that the decomposition can diagnose..." |
| method.tex:50 | "...reflecting the asymmetric cost..." | → "...to reflect the asymmetric cost..." |
| method.tex:101 | "...indicating death avoidance overcompensates..." | → "...DAF exceeds 1; death avoidance then overcompensates..." |
| discussion.tex:11 | "...leading to cascading errors that trigger death." | → "...did not change. These prediction errors compound across steps and ultimately trigger death." |

**剩余 -ing 短语（在数据段落中，未修改）**：

| 文件:行 | 内容 | 说明 |
|---------|------|------|
| main.tex:266 | caption: "reflecting the transition from..." | 表格 caption，数据相关 |
| main.tex:305 | "indicating step-level discrimination is not capacity-sensitive" | Appendix 数据段 |
| experiments.tex:95 | "reinforces that learned routing does not scale predictably" | 实际不是 -ing 结尾（以 "data scales" 结尾），误报 |

**其他检查均通过**：
- 破折号 (—, –)：全文零发现 ✓
- Furthermore/Moreover/Additionally 堆叠：零发现 ✓
- 黑名单词 (delve/leverage/utilize/facilitate/myriad/plethora)：零发现 ✓
- "It is worth noting" / "Notably,"：零发现 ✓

---

## 总结

论文整体写作质量高，AI 痕迹极少。主要改进空间：
1. Introduction 存在数字重复（lines 12 vs 22），压缩后叙事更紧凑
2. Related Work "Safe RL" 段过于密集，建议拆分
3. 4处 -ing 短语结尾已修复

---
