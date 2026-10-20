# research literature scan retry

**Why Calibration Fails: A Taxonomy of Failure Modes in Dialect-Aware LLM User Simulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_literature-scan-retry_20260513T054551_result.json`
- **Structured JSON:** [`455a38946ab01ca5189a.json`](../../sessions/45/455a38946ab01ca5189a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

更新完成。总结：

## 文献扫描结果（2026-05-13）

**新增 4 篇论文，无 direct competitor。DemoCalib 新颖性不变。**

### 重点关注

**sim2real2026gap** (arXiv 2603.11245) — "Mind the Sim2Real Gap in User Simulation for Agentic Tasks"
- 首次在 τ-bench 上跑 451 名真人用户，量化 sim2real 行为差距
- 结论：LLM 模拟器"过度合作、风格单一、缺乏真实挫败感"，虚增 agent 成功率
- **与我们最接近**：同一问题空间（τ-bench 模拟器保真度），但只诊断不开药。DemoCalib 的 DPO 校准是对他们发现的直接解决方案。论文中应作为核心 motivation 引用。

### 其他新增

| ID | 论文 | 类别 | 与我们的关系 |
|---|---|---|---|
| khan2026decoding | Decoding-Time Debiasing via PRM (2605.02348, May 4) | method-component | 互补：推理时去偏 vs 我们训练时 DPO |
| gupta2025endive | EnDive: Cross-Dialect Benchmark (EMNLP 2025 Findings) | evaluation | 覆盖 AAVE + Indian English，可引用为评估参照 |
| nakash2026divert | DIVERT: Diversity-Guided User Simulation (2604.21480) | background | 评估效率优化，间接相关 |

### 未收录但值得留意

- ϕ-DPO (2602.22601)：Fairness DPO 变体，但针对多模态持续学习
- Intra-Fairness Dynamics (2602.16438)：DPO 做公平性对齐时的 spillover 效应，写 limitation 时可引用
- Linguistic Stereotypes (2603.18729)：SAE vs AAE 在多 agent 架构中的刻板印象分析

---
