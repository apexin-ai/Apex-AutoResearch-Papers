# urgent bjb1 45299 check deploy

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_urgent_bjb1-45299-check-deploy_20260523T074412_result.json`
- **Structured JSON:** [`5e07e07c670f5b5db233.json`](../../sessions/5e/5e07e07c670f5b5db233.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇报

### exp_052_stackcube_civo_trigger_s1 — **DONE ✓**
| 指标 | 值 |
|------|-----|
| total_steps | 222,400 |
| eval_final | 29.46 @212.5K |
| eval_peak | **39.87 @162.5K** |
| ve_ratio_peak | **4.67 @52.5K** |
| ve_ratio_final | 0.133 @212.5K |
| checkpoint | checkpoint_202500.pt |

Registry 已更新为 DONE/success。

### exp_053_peginsertion_frozen_s0 — **RUNNING**
| 指标 | 值 |
|------|-----|
| PID | 123495 |
| uptime | 03:23:38 |
| step | **71,600 / 210,000** (34%) |
| train_return | 3.99 |
| GPU | cuda:0+1, ~3.4GB total |

### exp_054_pickcube_frozen_s0 — **已部署 ✓**
| 指标 | 值 |
|------|-----|
| PID | **133956** |
| GPU | cuda:0, 2.8GB |
| server | bjb1-45299 |

两张 RTX PRO 6000 (98GB each)，GPU 利用率很低，无争用风险。

---
