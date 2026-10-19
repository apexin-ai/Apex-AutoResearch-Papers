# research scienceworld feasibility

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_scienceworld-feasibility_20260519T031322_result.json`
- **Structured JSON:** [`280a6fe6d164df98268a.json`](../../sessions/28/280a6fe6d164df98268a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/scienceworld_feasibility_report.md`。

**核心结论**：ScienceWorld 接入 RAGEN **高度可行**。

关键发现：
- **API 完全兼容**：text-based reset/step 接口与 ALFWorld 同构，可直接继承 `BaseLanguageBasedEnv`，参照 ALFWorld 实现 wrapper
- **无需从零适配**：RAGEN 已有 12 个环境模板，ALFWorld 实现可直接复用，预估 **12-22 Worker-hours**
- **Expert data 充足**：ScienceWorld 内置 `get_gold_action_sequence()` 可批量生成 gold trajectories，加上 ETO 已发布的 HuggingFace SFT 数据集
- **研究价值高**：EMPO2 (2026.02) 证明 GRPO 在 ScienceWorld 上 baseline 仅 33.2 分（满分 100），有大量改进空间。30 个子任务 + 中间 reward (0-100) 比 ALFWorld 的 binary reward 更适合分析 step-level sign misattribution
- **主要工程风险**：Java/JVM 依赖（py4j）和 JVM 实例内存开销，但与 ALFWorld 的并行化限制类似，可用相同策略处理

---
