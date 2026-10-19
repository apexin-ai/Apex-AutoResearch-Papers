# harvest eval json details

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_harvest_eval-json-details_20260528T101925_result.json`
- **Structured JSON:** [`7489b375b6984acda223.json`](../../sessions/74/7489b375b6984acda223.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果汇总（frozen_rate 字段不存在）：

## LoRA Baseline (seed0)

| | eseed0 | eseed99 | **平均** |
|---|---|---|---|
| **avg_CAR** | 0.5300 | 0.5750 | **0.5525** |
| **avg_TSR** | 0.5550 | 0.5200 | **0.5375** |

Per-task (eseed0 / eseed99):
| Task | CAR | TSR | avg_max_ee_disp |
|---|---|---|---|
| orange_juice | 0.46 / 0.58 | 0.32 / 0.26 | 0.4008 / 0.3895 |
| chocolate_pudding | 0.70 / 0.76 | 0.74 / 0.76 | 0.4166 / 0.4141 |
| milk | 0.74 / 0.66 | 0.48 / 0.42 | 0.3538 / 0.3584 |
| bbq_sauce | 0.22 / 0.30 | 0.68 / 0.64 | 0.3892 / 0.3999 |

## SDF λ=0.1 (seed0)

| | eseed0 | eseed99 | **平均** |
|---|---|---|---|
| **avg_CAR** | 0.5250 | 0.5700 | **0.5475** |
| **avg_TSR** | 0.4850 | 0.4650 | **0.4750** |

Per-task (eseed0 / eseed99):
| Task | CAR | TSR | avg_max_ee_disp |
|---|---|---|---|
| orange_juice | 0.50 / 0.58 | 0.26 / 0.26 | 0.3975 / 0.3871 |
| chocolate_pudding | 0.78 / 0.74 | 0.74 / 0.70 | 0.4093 / 0.4093 |
| milk | 0.68 / 0.68 | 0.26 / 0.36 | 0.3557 / 0.3583 |
| bbq_sauce | 0.14 / 0.28 | 0.68 / 0.54 | 0.3853 / 0.3941 |

## 对比（双 seed 平均）

| Model | avg_CAR | avg_TSR |
|---|---|---|
| LoRA Baseline | **0.5525** | **0.5375** |
| SDF λ=0.1 | 0.5475 | 0.4750 |

SDF 在 CAR 上基本持平（-0.005），TSR 下降 6.25pp。frozen_rate 字段不存在于这些 JSON 中。

---
