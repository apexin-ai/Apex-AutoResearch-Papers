# monitor rsft gen progress

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_rsft_gen_progress_20260516T174200_result.json`
- **Structured JSON:** [`bb891084ef03ac205508.json`](../../sessions/bb/bb891084ef03ac205508.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 个 PID 全部存活。计算进度：

## 进度报告

| 任务 | 行数 | 已完成 docs | 总 docs | 进度 | 运行时间 |
|------|------|------------|---------|------|---------|
| **1.7B** (PID 349794, cuda:0) | 8680 | 1085 | 3027 | 35.8% | 3h51m |
| **8B** (PID 349382, cuda:3) | 7000 | 875 | 3027 | 28.9% | 3h51m |
| **LLaMA 8B** (PID 360970, cuda:2) | 4496 | 562 | 2963 | 19.0% | 1h52m |

## 速率与 ETA

| 任务 | 速率 | 剩余 docs | 预计剩余时间 | ETA (UTC) |
|------|------|-----------|-------------|-----------|
| **1.7B** | ~282 docs/h | 1942 | ~6.9h | ~May 16 23:30 |
| **8B** | ~227 docs/h | 2152 | ~9.5h | ~May 17 02:00 |
| **LLaMA 8B** | ~300 docs/h | 2401 | ~8.0h | ~May 17 00:30 |

注：上次记录 (~6h 前) 1.7B=531 docs, 8B=428 docs。按差值计算增量速率：
- 1.7B: (1085-531)/3.85h ≈ 144 docs/h — 比全程均值低，说明前期有加载/warmup 时间拉高了均值，实际稳态速率可能更接近这个数
- 8B: (875-428)/3.85h ≈ 116 docs/h

用增量速率修正：

| 任务 | 增量速率 | 剩余 | 修正 ETA (UTC) |
|------|---------|------|---------------|
| **1.7B** | ~144 docs/h | 1942 | ~13.5h → May 17 06:00 |
| **8B** | ~116 docs/h | 2152 | ~18.5h → May 17 11:00 |
| **LLaMA 8B** | ~300 docs/h (仅1.9h数据) | 2401 | ~8h → May 17 00:30 |

## GPU 状态

| GPU | 利用率 | 显存 |
|-----|--------|------|
| cuda:0 (1.7B) | 40% | 13.5/32.6 GB |
| cuda:1 (空闲) | 56% | 10.3/32.6 GB |
| cuda:2 (LLaMA) | 88% | 24.0/32.6 GB |
| cuda:3 (8B) | 76% | 28.1/32.6 GB |

GPU 1 有 10GB 占用和 56% 利用率但不属于这 3 个任务，可能有其他进程。三个目标任务均正常运行。

**总结**：LLaMA 最快预计明天凌晨完成，1.7B 明天早上，8B 明天中午。如果增量速率稳定的话，三个任务都还需要 8-18 小时。

---
