# research tau bench survey

**Why Calibration Fails: A Taxonomy of Failure Modes in Dialect-Aware LLM User Simulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_tau-bench-survey_20260512T095914_result.json`
- **Structured JSON:** [`d2a1a3f5baaa5a3f77c1.json`](../../sessions/d2/d2a1a3f5baaa5a3f77c1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调研完成。分析文档已写入 `artifacts/tau_bench_analysis.md`。

核心发现：
- **115 个 test 任务**（人工标注）+ 500 个 train 任务（synthetic），涵盖退货/换货/取消/修改/查询等操作
- **User simulator** 用 LLM 模拟，system prompt 中注入 task instruction（含角色、目标、性格），有 4 种策略（llm/react/verify/reflection）
- **评估是确定性的**：通过数据库状态哈希比对 + 文本子串匹配，binary reward (0/1)，不依赖 LLM judge
- **对 DemoCalib 最关键的 hook 点**：`LLMUserSimulationEnv.build_system_prompt()` 注入行为校准、`ToolCallingAgent.solve()` 循环拦截 agent 行为、`Env.calculate_reward()` 扩展为细粒度 reward

---
