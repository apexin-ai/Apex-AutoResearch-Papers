# code exp51 check results

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp51_check_results_20260522T093839_result.json`
- **Structured JSON:** [`7ef784cae0a604af1631.json`](../../sessions/7e/7ef784cae0a604af1631.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp51 oasst2 评估结果

**Phase 1 — Baseline (9-class, no adaptation):**
| 指标 | 值 |
|------|-----|
| oasst2 FPR | **57.5%** (115/200) |
| Mean jailbreak prob | 0.569 |
| Max jailbreak prob | 1.000 |

FPR > 20%，触发 Phase 2。

**Phase 2 — 10-shot Adaptation (加 10 条 oasst2 benign 重训):**
| 指标 | 值 |
|------|-----|
| Adapted oasst2 FPR | **20.5%** (41/200) |
| IID F1 macro | 1.0000 |
| OOD DD F1 | 1.0000 |
| OOD AA F1 | 1.0000 |
| OOD FITD F1 | 1.0000 |

10-shot adaptation 将 FPR 从 57.5% 降到 20.5%，同时 OOD 检测性能无损（所有 OOD attack F1 保持 1.0）。总耗时 1.7 分钟。

---
