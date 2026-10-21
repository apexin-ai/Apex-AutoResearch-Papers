# ops emergency gpu saturation check

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_emergency-gpu-saturation-check_20260516T075333_result.json`
- **Structured JSON:** [`7fcd0f93741ef27c6954.json`](../../sessions/7f/7fcd0f93741ef27c6954.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 17 张 GPU 都在跑实验，没有空闲卡。以下是完整盘点：

## GPU 状态汇总

### bjb1-18228 (4× GPU) — 全部在用
| GPU | PID | 实验 | 运行时间 |
|-----|-----|------|----------|
| 0 | 390936 | eval-acr-object-v4-default-r2 | >1天 |
| 1 | 452987 | perdof seed44 norm=0.1 | 2h57m |
| 2 | 428411 | obs_only seed44 norm=0.2 | 6h22m |
| 3 | 428122 | reconvla seed44 | 6h22m |

### bjb1-32546 (6× GPU) — 全部在用
| GPU | PID | 实验 | 运行时间 |
|-----|-----|------|----------|
| 0 | 226878 | scalar seed44 r2 | 42m |
| 1 | 212665 | vla_mean seed44 | 2h56m |
| 2 | 220786 | obs_only seed44 norm=0.3 | 1h48m |
| 3 | 233553 | **obs_only seed45 norm=0.2** ✅ | 10m |
| 4 | 227086 | obs_only seed44 norm=0.1 | 42m |
| 5 | 229751 | obs_only seed44 default | 41m |

### bjb2-28827 (6× GPU) — 全部在用
| GPU | PID | 实验 | 运行时间 |
|-----|-----|------|----------|
| 0 | 105947 | mag-perdof-norm003-object | >1天 |
| 1 | 109655 | mag-perdof-norm005-object | >1天 |
| 2 | 140759 | mag-perdof-norm03-r3 | >1天 |
| 3 | 144513 | mag-perdof-norm02-seed43-r3 | >1天 |
| 4 | 101616 | mag-obsonly-norm005-object | >1天 |
| 5 | 215941 | **argmin seed45** ✅ | 9m |

### bjb2-40593 (1× GPU) — 在用
| GPU | PID | 实验 | 运行时间 |
|-----|-----|------|----------|
| 0 | 316387 | perdof seed44 default | 36m |

## 结论

**17/17 GPU 全部在用，0 张空闲。** Director 报告的 11/17 可能是短暂状态，现在已经全部填满。

优先级任务状态：
1. ✅ seed45 argmin — 已在 bjb2-28827 GPU 5 上跑（~10分钟前启动）
2. ✅ seed45 obs_only ε=0.2 — 已在 bjb1-32546 GPU 3 上跑（~10分钟前启动）
3. ❌ seed45 VLA-only baseline — 无空闲卡
4. ❌ seed45 perdof ε=0.2 — 无空闲卡
5. ❌ seed45 scalar — 无空闲卡

剩余 3 个 seed45 实验需要等现有实验完成后才能部署。bjb2-28827 上 5 个 magnitude sweep 实验已跑超过 1 天，可能最先完成释放 GPU。

---
