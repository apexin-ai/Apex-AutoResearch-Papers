# ssh investigate crm object eval bjb2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_investigate-crm-object-eval-bjb2_20260523T032911_result.json`
- **Structured JSON:** [`02f77fc83a43873b29a8.json`](../../sessions/02/02f77fc83a43873b29a8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调查完成。

**结论：CRM Object eval ×3 全部正常完成，不是崩溃。**

| Seed | Success Rate | 完成时间 (CST) |
|------|-------------|---------------|
| 42 | 50.5% | 10:30 |
| 43 | 53.5% | 10:28 |
| 44 | 51.5% | 10:29 |
| **Mean** | **51.83% ± 1.53%** | |

GPUs 0-2 完成后已被新实验占用：adaptive_conformal_crm (GPU0)、reconvla (GPU1)、goal crm norm=0.05 (GPU2)，均在 11:25 启动。

VLA-only object eval (GPUs 3-5) 进度 ~60%，预计 12:30-13:00 CST 完成，当前趋势看成功率约 80%，远高于 CRM obs-only 的 51.8%。

全部 6 卡在用，无空闲 GPU。报告写入 `artifacts/investigation_crm_object_bjb2.md`。

---
