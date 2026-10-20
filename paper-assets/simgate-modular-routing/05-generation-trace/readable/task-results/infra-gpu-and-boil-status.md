# infra gpu and boil status

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_gpu-and-boil-status_20260513T191501_result.json`
- **Structured JSON:** [`a65624ebfadc513a18ae.json`](../../sessions/a6/a65624ebfadc513a18ae.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总报告

### GPU 状态
| GPU | 型号 | 利用率 | 显存 |
|-----|------|--------|------|
| GPU0 | RTX 5090 | 0% (idle between inferences) | 28013 / 32607 MiB |
| GPU1 | RTX 5090 | 0% | **0 / 32607 MiB** |

### Prescreening (GPU0, PID 649681) — RUNNING
已完成 **9/25 tasks**（+ 2 skipped MVP-tested: boil, change-the-state-of-matter-of）

当前 identify-life-stages-1 只跑了 2 episodes（正常 5），可能正在进行中。

Signal type 分布（已完成的 9 个）：
- death-dominated: 4 (chemistry-mix-paint-tertiary-color, find-plant, grow-fruit, identify-life-stages-1)
- genuine-det: 3 (find-animal, find-living-thing, freeze)
- internal-preferred: 1 (find-non-living-thing)
- mixed: 1 (chemistry-mix)

### Boil v3 (GPU1, PID 650421) — DONE
20 episodes 完成：

| 策略 | Mean | Std |
|------|------|-----|
| always-internal | -44.7 | 50.0 |
| always-deterministic | -9.3 | 30.3 |
| oracle-routing | **3.8** | 15.2 |
| oracle − internal | **+48.5** | — |
| oracle − det | **+13.1** | — |

Oracle routing 大幅优于两个 baseline，但绝对分数仍低（3.8）——大部分 episode 得分 0，只有 1 个 episode 拿到 70 分拉高了均值。

### GPU1 空闲，可派新任务。

---
