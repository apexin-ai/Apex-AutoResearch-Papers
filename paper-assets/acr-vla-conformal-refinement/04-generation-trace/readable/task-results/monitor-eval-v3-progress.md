# monitor eval v3 progress

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_eval-v3-progress_20260514T122309_result.json`
- **Structured JSON:** [`2e50e881ab269767282b.json`](../../sessions/2e/2e50e881ab269767282b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇总

### bjb1-18228 — 3 个实验

| 实验 | PID | GPU | 状态 | 运行时间 | GPU Util | VRAM |
|------|-----|-----|------|----------|----------|------|
| **eval-acr-spatial-v3** (CORE) | 197057 | cuda:0 | **Running** — 模型/环境已加载，正在执行 rollouts | 6m22s | 24% | 15.2G/24G |
| **eval-scalar-unc-spatial-v2** | 197324 | cuda:1 | **Running** — 模型/环境已加载，正在执行 rollouts | 6m20s | 21% | 1.5G/24G |
| **eval-acr-object-v3** | 197803 | cuda:3 | **Running** — 模型/环境已加载，正在执行 rollouts | 6m15s | 20% | 1.5G/24G |

- **cuda:2**: 空闲 (0% util, 1 MiB)，符合预期
- 三个实验都已完成初始化（SmolVLA + CRM 加载、10 个 task 加载完毕），尚未输出第一个 task 的完整结果。日志停在 `[eval] 10 tasks loaded.`，说明正在跑第一个 task 的 rollouts。
- GPU 0 的 VRAM 明显高于 1、3（15.2G vs 1.5G），可能是 acr_vla + spatial 模式在渲染时占用更多显存。

**无 crash，全部正常运行。**

### bjb2-40593 — eval-vla-mean-spatial

| 实验 | GPU | 状态 | 进度 |
|------|-----|------|------|
| eval-vla-mean-spatial | cuda:0 | **Running** | **5/10 tasks**（第 5 个 task 进行中，rollout 5/10） |

已完成 task 结果：

| Task | Success Rate |
|------|-------------|
| pick_up...between_plate_and_ramekin → plate | 70% (7/10) |
| pick_up...next_to_ramekin → plate | 100% (10/10) |
| pick_up...from_table_center → plate | 0% (0/10) |
| pick_up...on_cookie_box → plate | 30% (3/10) |
| pick_up...in_top_drawer → 进行中 | 0/5 so far |

当前均值 ~50% (20/40)。预估剩余时间：按已运行时间推算，总计 10 tasks，已完成 ~4.5/10，大约还需与已运行时间相当的时间完成。

---
