# analysis all gpu progress check

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_all-gpu-progress-check_20260522T113244_result.json`
- **Structured JSON:** [`10ea6e17e71fb38b105d.json`](../../sessions/10/10ea6e17e71fb38b105d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Now I have all the data. Here's the progress report:

## GPU 实验进度报告 (westd-16639, 2026-05-22 19:34 CST)

**所有 4 个 PID 存活，4 GPU 满载 (96-100% util, ~90GB/98GB VRAM)**

### cuda:0 — Qwen2.5 PW 3-seed (PID 552333, 运行 4h)
| Seed | 进度 | 状态 |
|------|------|------|
| 456 | 600/600 | **DONE** (之前完成) |
| 789 | 600/600 | **DONE** (之前完成) |
| 123 | ~217/600 (36%) | **运行中** |

当前 seed=123 从 15:33 开始，~66s/problem，剩余 383 题 → **ETA ~7h (约明早 02:30)**

### cuda:1 — LLaMA-8B FOLIO 3-seed (PID 596151, 运行 26min)
| Seed | 进度 | 状态 |
|------|------|------|
| 123 | 45/204 (22%) | **运行中**，36s/prob |

日志 ETA 96 min 完成 seed123。之后还有 seed456、seed789 各 ~2h → **全部完成 ETA ~6h (约明早 01:30)**

### cuda:2 — Mistral PW 4-seed (PID 510987, 运行 8h)
| Seed | 进度 | 状态 |
|------|------|------|
| 42 | 600/600 | **DONE** (11:31→16:28, 5h) |
| 123 | 378/600 (63%) | **运行中**，~29s/prob |
| 456 | 未开始 | — |
| 789 | 未开始 | — |

seed123 剩 222 题 ~1.8h，之后 seed456+789 各 ~4.8h → **全部完成 ETA ~11h (约明早 07:00)**

### cuda:3 — Mistral FOLIO seed=789 (PID 576938, 运行 44min)
| Seed | 进度 | 状态 |
|------|------|------|
| 789 | 113/204 (55%) | **运行中**，24s/prob |

日志 ETA 36.6 min → **完成 ETA ~20:10 今晚**（最先完成）

---

**最先空出的 GPU**: cuda:3，约 37 分钟后完成。

---
