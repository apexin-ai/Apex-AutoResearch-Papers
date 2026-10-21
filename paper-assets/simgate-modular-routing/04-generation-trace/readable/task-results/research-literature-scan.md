# research literature scan

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_literature-scan_20260514T003850_result.json`
- **Structured JSON:** [`d8013f4be2ec52ba0b8d.json`](../../sessions/d8/d8013f4be2ec52ba0b8d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

literature_map.yaml 已创建。以下是扫描报告：

---

## 文献增量扫描报告 (2026-05-14)

### 扫描范围
18 组关键词，覆盖 2025-2026 年 arXiv、顶会 (EMNLP/ICLR/NeurIPS/ACL) 论文。

### 新发现论文：12 篇

| 论文 | 会议/来源 | 关系 | 关键发现 |
|------|-----------|------|----------|
| **CogRouter** (Yang+ 2026) | arXiv:2602.12662 | complementary | ScienceWorld SOTA 82.3%，路由认知深度而非模态 |
| **ITP** (Liu+ 2026) | arXiv:2601.08955 | complementary | 世界模型 lookahead 在 ScienceWorld 上规划 |
| **MTRouter** (Zhang+ 2026) | ACL 2026 | complementary | ScienceWorld 多轮 LLM 路由，成本优化 |
| **ReTool** (Feng+ 2025) | ICLR 2026 | complementary | RL 学习何时用代码解释器（数学域） |
| **ARES** (Yang+ 2026) | arXiv:2603.07915 | complementary | 轻量 router 做推理深度选择，-52.7% tokens |
| **Dyna-Think** (2025) | arXiv:2506.00320 | complementary | 世界模型 + 推理融合框架 |
| **TSR** (IBM, 2026) | ICLR 2026 | complementary | 轨迹搜索 rollout 训练方法 |
| **ToolSafety** (2025) | EMNLP 2025 | complementary | 工具调用安全数据集 |
| **OpenAgentSafety** (2026) | ICLR 2026 | background | Agent 安全评测基准 |
| **LLM Agentic Failures** (2025) | arXiv:2512.07497 | complementary | 4 类 agent 失败模式分类 |
| **EnvSimBench** (2025) | 2025 | complementary | "state-change cliff"：多变量状态更新时 LLM 灾难性失败 |
| **MoR** (Bae+ 2025) | NeurIPS 2025 | background | 架构级自适应深度 |

### Novelty 威胁评估：**无威胁**

**未发现 direct competitor。** 没有论文声称 death/safety avoidance 是 routing signal 的主要来源。现有工作分为三类：
1. **路由不同目标**：CogRouter 路由认知深度，MTRouter 路由不同 LLM，ARES 路由推理强度——都不是内部推理 vs 确定性计算的模态路由
2. **不分析信号组成**：ReTool/ITP 优化何时用工具/世界模型，但不分解 routing signal 的来源
3. **定性而非定量**：LLM Agentic Failures 定性分类失败模式，不量化 death avoidance 贡献

### 建议引用的关键论文（按优先级）

**必须引用（Related Work 定位）：**
- **CogRouter** — ScienceWorld SOTA 基线 + adaptive computation 对比
- **ReTool** — tool-use routing 最新代表（ICLR 2026）
- **MTRouter** — ScienceWorld 上的多轮路由工作（ACL 2026）
- **ITP** — 世界模型路由（ScienceWorld 评测）
- **EnvSimBench** — "state-change cliff" 发现解释了我们 death avoidance 发现的底层机制

**建议引用（强化论证）：**
- **ARES** — 轻量 router 架构的平行工作
- **ToolSafety** (EMNLP 2025) — 区分我们的 "safety" 定义（灾难性任务失败 vs 工具滥用安全）
- **Dyna-Think** — 推理与模拟融合（我们分析它们的信号组成）

---
