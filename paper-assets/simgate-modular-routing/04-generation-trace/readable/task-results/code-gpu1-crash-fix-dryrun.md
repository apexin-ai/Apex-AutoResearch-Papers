# code gpu1 crash fix dryrun

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_gpu1-crash-fix-dryrun_20260513T080141_result.json`
- **Structured JSON:** [`f5d5d2ebba52c0161ce7.json`](../../sessions/f5/f5d5d2ebba52c0161ce7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

vLLM 正在 GPU1 上加载模型（14.25 GiB），一切正常。

---

## 产出总结

### 1. v2 崩溃根因
**GPU1 被前序实验的 vLLM EngineCore 僵尸进程占用** — PID 163319 占了 28 GiB（31 GiB 中），只剩 3.51 GiB 可用。vLLM 初始化要求 26.65 GiB（gpu_memory_utilization=0.85），直接 `ValueError` 退出。

### 2. 修复内容
- **移除 `run_episode_always_internal` 中的 death filter**（lines 75-83）：删掉 `fork_and_lookahead` + `is_lethal` 重选循环。always-internal 现在是纯 LLM 推理：`select_action_react → step_env`
- `run_episode_always_deterministic` 和 `run_episode_oracle_routing` 的 death filter 保留不动

### 3. Dry-run 结果（通过）
- always-internal: **score=0.0** (37s) — 无 fork_and_lookahead 调用
- always-deterministic: **score=0.0** (47s)
- oracle-routing: **score=0.0** (int=0/det=10) (67s)
- 无 crash / traceback / exception

### 4. 正式提交
- **PID**: 324895
- **tmux session**: `mvp-p1-gpu1-v3`
- **Registry**: RUNNING, spec 已写入
- vLLM 模型加载中（14.25 GiB on GPU1）

---
