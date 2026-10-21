# analysis exp hopper baseline

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_hopper_baseline_20260527T054925_result.json`
- **Structured JSON:** [`2062dc1d06aeb326fff3.json`](../../sessions/20/2062dc1d06aeb326fff3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry updated to DONE/success.

## 分析结论

**Conclusion: success** — Hopper Hop baseline 确认无 CIVO。

### 关键指标
| 指标 | 值 |
|------|------|
| eval_return final (105K) | **96.43** |
| NVE (ve_ratio) final | **0.559** |
| NVE (ve_ratio) peak | **3.48** @ step 65K (transient) |
| civo/alert | **0.0** (全程未触发) |
| value_mean / target_mean @105K | 53.9 / 54.2 (value 精确追踪 target) |

### 要点
- ve_ratio 在 65K 处出现单次 spike (3.48)，但这是 **transient artifact**：当时 eval_return 从 22.5 骤降至 3.5（临时性能抖动），value 预测 (~12.2) 仍在追踪 target (~12.4)，并非真正的 value overestimation
- 75K 处 ve_ratio 立即恢复至 0.34，此后稳定在 0.5-0.6
- civo/alert 全程 0.0，CIVO 检测系统从未触发
- 最终 value_mean (53.9) ≈ target_mean (54.2)，value function 正常收敛

### 异常
无。训练正常完成 (EXIT_CODE=0)，105K steps，2.88 小时。

---
