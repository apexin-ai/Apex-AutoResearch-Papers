# code isr monitoring fix

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_isr-monitoring-fix_20260514T013628_result.json`
- **Structured JSON:** [`6618c076543d340c7438.json`](../../sessions/66/6618c076543d340c7438.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

当前 `execution_only` 分支（train_grpo.py:167-172）已经调用 `_full_fn`（即 `sta_reward`/`prolog_sta_reward`），会执行完整 STA ablation 并计算真实 ISR。`result["sta_reward"]` 返回的是 `compute_isr(ablation_results)` 的结果（[0,1] 连续值），不是二值的 execution_reward。

代码流程：
1. `_full_fn({}, cleaned, solver, execution_weight=1.0, sta_weight=0.0, timeout=5)` — 内部先 prove，proved 后跑 `run_sta` + `compute_isr` 得到真实 ISR
2. `reward_val = result["execution_reward"]` — reward 仍然只用 0/1
3. `isr = result.get("sta_reward", 0.0)` — 取到真实 ISR 写入 log

脚本 import 和 `--help` 均通过，无语法错误。

如果之前跑的训练中 isr_mean == prove_rate，那可能是那次训练加载的是更早版本的代码（该文件今天 09:40 才更新）。下一次启动 execution_only 训练时，ISR 监控会反映真实 formalization 质量。

---
