# analysis floor ablation 0p6 v2

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_floor_ablation_0p6_v2_20260523T163319_result.json`
- **Structured JSON:** [`db8dd08039be9b2f0c42.json`](../../sessions/db/db8dd08039be9b2f0c42.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE。结果汇总：

## GSM8K Accuracy

**floor=0.6: 62.02%** (818/1319, ±1.34%)

## Floor Ablation 完整趋势

| Floor | GSM8K Acc | 趋势 |
|-------|-----------|------|
| 0.3   | 65.05%    | 最高 |
| 0.4   | 64.37%    | baseline |
| 0.5   | 61.71%    | ↓ |
| **0.6** | **62.02%** | ≈ 0.5 |

趋势：floor 从 0.3→0.4 轻微下降，0.5 和 0.6 显著下降但彼此持平（差异在 CI 内）。floor 越高（保留越多原始权重），恢复效果反而越差，说明更激进的重初始化（低 floor）有利于 GRPO 阶段的恢复训练。

## 异常检查

无异常。GRPO 100 步正常完成（train_loss=0.0065），EOS rate 98%，checkpoint 完整保存（~12GB model.safetensors）。

---
