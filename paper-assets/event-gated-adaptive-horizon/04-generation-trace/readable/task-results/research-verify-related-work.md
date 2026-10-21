# research verify related work

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_verify-related-work_20260513T111219_result.json`
- **Structured JSON:** [`74b85c7825440cc6e6f3.json`](../../sessions/74/74b85c7825440cc6e6f3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

5 个 `[NEED VERIFY]` 标记已全部清除。核实结果汇总：

| 条目 | 结果 | 说明 |
|------|------|------|
| NE-Dreamer | ✓ 准确 | decoder-free + next-embedding prediction 确认无误 |
| R2-Dreamer | ✓ 准确 | decoder-free + redundancy-reduction objective (Barlow Twins) 确认 |
| HWM | ✓ 准确 | 双尺度预测器 + learned action encoder + 两级分层规划 确认 |
| I-TAP | **已修正** | VQ-VAE → **RQ-VAE** (residual-quantized VAE)，其余准确 |
| FiGAR | ✓ 准确 | 策略同时输出动作和重复次数，"action-repetition head" 描述正确 |
| TempoRL | ✓ 准确 | 学习条件化于状态和动作的 skip-policy，"dedicated skip network" 描述正确 |

---
