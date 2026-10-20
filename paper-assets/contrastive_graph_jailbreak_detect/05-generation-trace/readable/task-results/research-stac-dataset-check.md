# research stac dataset check

**contrastive graph jailbreak detect** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_stac-dataset-check_20260517T052916_result.json`
- **Structured JSON:** [`bec95b88f0dc1b9c773b.json`](../../sessions/be/bec95b88f0dc1b9c773b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调研完成。核心发现:

1. **Repo public，数据可直接获取** — `data/STAC_benchmark_data.json` (4.73MB, 483 traces)
2. **数据格式清晰** — JSON array，每个 trace 包含 `generation_config`(含 failure_mode 标注)、`attack_plan`(含 verified_tool_chain)、`interaction_history`(OpenAI chat format with tool calls)、`planner_history`
3. **关键限制: 无 benign traces** — 这是纯攻击 benchmark。要做 contrastive 检测，需要另外构造/获取正常 agent 交互数据（可从 SHADE-Arena 或 Agent-SafetyBench 原始 repo 获取）
4. **无 train/test split** — 需自行划分
5. **License CC BY-NC 4.0** — 学术研究可用，不可商用

---
