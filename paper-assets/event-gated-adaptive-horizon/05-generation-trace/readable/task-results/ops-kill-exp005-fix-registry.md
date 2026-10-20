# ops kill exp005 fix registry

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_kill_exp005_fix_registry_20260513T215230_result.json`
- **Structured JSON:** [`027fdcb308c39fa0e66e.json`](../../sessions/02/027fdcb308c39fa0e66e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GPU 1 已释放（3 MiB）。全部完成：

**1. Kill exp_005** — 已杀（PID 51726），cuda:1 已释放

**2. Metrics 核实结果**：

| Step | eval_return (实际) | registry 旧值 |
|------|-------------------|--------------|
| 85K | **212.34** | 319.3 (误录) |
| 105K | **276.08** | 337.8 (误录) |

旧的 319.3/337.8 不是 eval_return，可能是某个时刻的 train_return 采样值。eval 轨迹：峰值 541.18@55K → 持续下降 → 最终 98.84@145K。

**3. Registry 更新**：
- `exp_001_baseline`: DONE/success, metrics 已更新
- `exp_005_event_gated_v4`: DONE/negative, metrics 已用实际值修正, failure_reason 已记录

**4. Cron 删除** — `exp_005_event_gated_v4` cron 已删除

---
