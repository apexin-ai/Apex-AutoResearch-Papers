# research check step data format

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_check-step-data-format_20260513T183545_result.json`
- **Structured JSON:** [`1c07ca322c2cad3c7a3a.json`](../../sessions/1c/1c07ca322c2cad3c7a3a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证结果：

**phase1_signal.py 和 signal_prescreening.py 都已保存 step-level data。** 每步记录包含：
- `observation`（≤500 chars）
- `action`（完整）
- `modality`（"internal" / "deterministic"）
- `score_before`, `score_after`, `score_delta`
- always-internal 额外有 `llm_output`（≤300 chars）
- always-deterministic 额外有 `candidates`（fork 评估结果列表）

**plan-001b 适配性：可直接用，不需改代码。** 现有 episodes.jsonl 已按 episode_idx 配对同 variation 的 internal 和 deterministic trajectories。写一个后处理脚本比较 `always_internal.final_score` vs `always_deterministic.final_score`，即可为所有步骤生成 episode-level counterfactual label，输出 (observation, action, modality_label) triples。

**Prescreening 进度：7/25**（6 完成 + freeze 进行中），每 task ~20min，预计还需 ~6h，约 08:30 CST 完成。

---
