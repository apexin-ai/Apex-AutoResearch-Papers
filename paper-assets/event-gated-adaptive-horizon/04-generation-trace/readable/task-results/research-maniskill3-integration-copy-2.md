# research maniskill3 integration

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_maniskill3-integration_20260516T025719_result.json`
- **Structured JSON:** [`f22f1deb1715cbf21226.json`](../../sessions/f2/f22f1deb1715cbf21226.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

集成方案已完成并注册 (`art_20260516_252646`)。

**核心发现**：代码集成已基本完成 — `envs/maniskill.py` wrapper、`dreamer.py` make_env 分支、`configs.yaml` maniskill_state preset 都已就位。**唯一的阻塞项是服务器上 mani-skill 包未安装**。

**方案要点**：
1. **选定任务**: PickCube-v1 / StackCube-v1 / PegInsertionSide-v1，均为 8 维连续动作、42-48 维 state obs、dense reward
2. **代码无需大改**: 仅需在 `configs.yaml` 追加 StackCube 和 PegInsertion 配置
3. **实验设计**: 3 tasks × 3 configs (baseline/gated/fixed-dt) × 3 seeds = 27 runs，每 run 预估 1-2 hr
4. **关键风险**: manipulation 的 dense reward 可能导致 gate 退化为 dt=1，需关注 gate_dt_mean 指标

---
