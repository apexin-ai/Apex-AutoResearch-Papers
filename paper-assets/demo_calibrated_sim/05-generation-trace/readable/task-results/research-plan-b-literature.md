# research plan b literature

**Why Calibration Fails: A Taxonomy of Failure Modes in Dialect-Aware LLM User Simulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_plan-b-literature_20260513T062721_result.json`
- **Structured JSON:** [`3694c37fce2a2870f1e9.json`](../../sessions/36/3694c37fce2a2870f1e9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`register_artifact` isn't available as a tool in this session. The evidence table is written to `artifacts/plan_b_evidence_table.md` directly on disk — it's accessible but won't be in the MCP registry. Moving on to the summary.

---

## 完成情况

### 1. 证据表
写入 `artifacts/plan_b_evidence_table.md`，按 4 个失败机制分类：

| 失败机制 | 核心数据 |
|---|---|
| **FM1: 全局行为抑制** | BCP 使 completion 下降 46-73%（mvp-004），Llama-3-8B 直接降至 5% floor |
| **FM2: 跨维度干扰** | 单维度 BCP 导致非目标维度偏移 25-66%（mvp-004） |
| **FM3: 过校正反弹** | overcorrected variant politeness 反升 +8.2%（base）/+14.3%（DPO） |
| **FM4: DPO+BCP 交互反转** | DPO 模型 BCP politeness gap 反向 -10.3%，10/12 checks 恶化 |

### 2. 文献更新
`literature_map.yaml` 新增 4 篇 Plan B 相关论文（总计 28 篇）：

| 论文 | 关联失败机制 |
|---|---|
| **Basil et al. 2025** — Playing Pretend (arXiv 2512.05858) | FM1: persona prompting 降低 factual accuracy |
| **Anonymous 2026** — Expert Personas + PRISM (arXiv 2603.18507) | FM1: persona-accuracy trade-off，性能下降达 30pp |
| **Gupta et al. 2026** — Intra-Fairness Dynamics (arXiv 2602.16438) | FM2+FM4: bias spillover effect，跨维度干扰 |
| **Lee et al. 2024** — DPO Toxicity Mechanics (ICML 2024) | FM4: DPO bypass 而非 remove，解释 calibration reversal |

### 3. 文献空白（Novelty Gap）

**没有人做过 BCP/prompt-based behavioral calibration 的系统性失败分析。** 具体地：

- **FM1（completion collapse）**：persona prompting 文献只研究 classification/QA accuracy，没人在 multi-turn agent dialogue 中量化 completion 崩溃
- **FM2（cross-dimension interference）**：Gupta 2026 发现了 DPO 的 bias spillover，但没人在 prompt-level calibration 中发现同类现象
- **FM3（overcorrection rebound）**：文献中无先例——BCP 要求降低 politeness 反而升高是新发现
- **FM4（DPO+BCP reversal）**：Lee 2024 解释了 DPO 的 bypass 机制，但 DPO 训练反转 prompt calibration 效果是全新的 interaction failure

**Plan B 的 novelty 定位**：首篇系统性记录 prompt-based behavioral calibration 在 LLM user simulator 中的失败模式分类学（taxonomy of failure modes），有跨模型、跨维度、跨方法（BCP alone / DPO+BCP）的实证数据支撑。

---
