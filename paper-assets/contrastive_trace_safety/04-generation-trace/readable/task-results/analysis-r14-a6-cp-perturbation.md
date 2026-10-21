# analysis r14 a6 cp perturbation

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_r14_a6_cp_perturbation_20260518T182931_result.json`
- **Structured JSON:** [`93d60b8a25d2e250690e.json`](../../sessions/93/93d60b8a25d2e250690e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

A6 完成。

## 结果

| Model | Shift | Prec | BA | FPR | ΔPrec | ΔBA | ΔFPR |
|-------|-------|------|----|-----|-------|-----|------|
| R1-8B | -3 | .652 | .773 | .177 | +.056 | -.011 | +.012 |
| R1-8B | -2 | .635 | .780 | .176 | +.038 | -.004 | +.011 |
| R1-8B | -1 | .618 | .784 | .171 | +.021 | +.001 | +.006 |
| R1-8B | **0** | **.596** | **.784** | **.165** | — | — | — |
| R1-8B | +1 | .573 | .781 | .159 | -.023 | -.003 | -.007 |
| R1-8B | +2 | .550 | .775 | .150 | -.046 | -.009 | -.015 |
| R1-8B | +3 | .530 | .771 | .143 | -.066 | -.013 | -.022 |
| OT-7B | -3 | .404 | .714 | .298 | +.053 | +.006 | +.012 |
| OT-7B | **0** | **.351** | **.707** | **.286** | — | — | — |
| OT-7B | +3 | .300 | .702 | .276 | -.052 | -.005 | -.010 |
| R1-32B | -3 | .625 | .698 | .360 | +.055 | -.024 | +.078 |
| R1-32B | **0** | **.570** | **.722** | **.281** | — | — | — |
| R1-32B | +3 | .503 | .750 | .236 | -.068 | +.029 | -.045 |
| QwQ-32B | -3 | .661 | .728 | .158 | +.052 | +.038 | +.029 |
| QwQ-32B | **0** | **.609** | **.690** | **.129** | — | — | — |
| QwQ-32B | +3 | .550 | .676 | .114 | -.059 | -.014 | -.015 |

### ±2 steps 内最大变化量

| Model | |ΔPrec|\_max | |ΔBA|\_max | |ΔFPR|\_max |
|-------|-----------|---------|----------|
| R1-8B | 0.046 | 0.009 | 0.015 |
| OT-7B | 0.040 | 0.006 | 0.011 |
| R1-32B | 0.033 | 0.025 | 0.052 |
| QwQ-32B | 0.053 | 0.019 | 0.017 |

**BA 高度稳定**：4 个模型在 ±2 steps 内 |ΔBA| 均 < 0.025，R1-8B/OT-7B 尤其鲁棒（< 0.01）。R1-32B 的 FPR 最敏感（0.052），可能因数据量小（100 traces）且 W=1 无时序平滑。所有模型在 ±3 steps 均无灾难性退化。

---
