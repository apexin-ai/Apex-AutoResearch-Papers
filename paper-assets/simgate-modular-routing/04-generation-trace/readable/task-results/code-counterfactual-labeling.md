# code counterfactual labeling

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_counterfactual-labeling_20260513T171101_result.json`
- **Structured JSON:** [`8defadebe91ce954b0d3.json`](../../sessions/8d/8defadebe91ce954b0d3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run 通过，import 和参数解析均无报错。

**产出：**
- `/root/autodl-tmp/simgate-modular-routing/src/counterfactual_labeling.py` 已写入服务器并验证
- 本地同步副本：`src/counterfactual_labeling.py`

**脚本结构：**
- `fork_and_continue()` — 核心新增：fork 环境 → 执行 first_action → 用 ReAct base policy 续跑 K 步 → 返回 final score → 关闭 JVM
- `get_deterministic_action()` — 复用 phase1 的 candidate 生成 + fork 1-step 评估 + lethal filter 逻辑
- `run_episode()` — 每步获取 internal/det action，diverge 时双 fork + K 步续跑，用 score 差异标 label
- `main()` — CLI 入口，按 episode 写 JSONL，结束打 summary

---
