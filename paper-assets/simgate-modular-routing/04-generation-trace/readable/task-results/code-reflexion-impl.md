# code reflexion impl

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_reflexion-impl_20260517T115610_result.json`
- **Structured JSON:** [`fa4c52c67498b9ed4566.json`](../../sessions/fa/fa4c52c67498b9ed4566.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。

`src/reflexion_baseline.py` 已部署到 westb-13313，约 290 行。核心功能：

- **APIAgent**: 通过 vLLM OpenAI-compatible API 调用 Qwen2.5-7B-Instruct，复用 `llm_agent.py` 的 `parse_action` / `_format_valid_actions` / `_format_history`
- **run_episode()**: 复用 `scienceworld_utils` 的 env 管理逻辑，支持 reflection 注入到 system prompt
- **run_trial_loop()**: 外套 trial loop，失败后生成 reflection（reflexion 模式）或直接重试（retry 模式），成功即停
- **输出**: 每 episode 一个 JSON（含 trials 列表、score、death、reflection_text、actions），汇总写到 `results/reflexion_summary.json`
- **11 task 硬编码**，baseline 对照数据（42.9% death rate, DAF 90.4%）写在 summary 中
- `--dry-run` 验证通过

运行前需先启动 vLLM 服务（`--api-base` 默认 `http://localhost:8000/v1`）。

---
