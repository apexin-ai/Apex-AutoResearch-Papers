# ops kill llama expanded

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_kill-llama-expanded_20260515T120900_result.json`
- **Structured JSON:** [`389c1279c1552d60f6d0.json`](../../sessions/38/389c1279c1552d60f6d0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**报告：**
- PID 440297 (run_llama_expanded.sh wrapper) — 已 kill（需 kill -9）
- PID 440724 (vLLM EngineCore) — 已 kill
- 额外发现并 kill 了同一实验的子进程树：440302 (run_llama_expanded.sh) → 470474 (episode_level_collection.py) → 470889 (vLLM EngineCore)
- tmux session `llama-cross-model-expanded` 已不存在
- **GPU 0 已完全释放**：0MiB / 32607MiB，0% 利用率，无进程占用

---
