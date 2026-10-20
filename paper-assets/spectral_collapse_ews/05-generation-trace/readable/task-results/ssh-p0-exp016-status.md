# ssh p0 exp016 status

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_p0-exp016-status_20260521T232427_result.json`
- **Structured JSON:** [`081d3ff9f286a6ad95c1.json`](../../sessions/08/081d3ff9f286a6ad95c1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告

### exp_016 (fixed_mix r=0.30, seed=44, GPU 0) — **存活，正常运行**

- **PID 614614**: 存活，运行 8m47s
- **GPU 0**: 49% 利用率, 19045 MiB / 97887 MiB — Director 之前看到 0% 是瞬时快照，现在正常
- **进度**: Gen 0 评估已完成 (eff_rank=417.55, ppl=9.55, d4=0.7305)，Gen 1 正在生成样本 **1920/35000** (5.5%)
- **检查点**: `fixed_mix_r03_seed44/gen_0` (May 22 07:19)

**预估完成时间**: 参考 exp_015 每代 ~2h 的节奏，exp_016 有 10 代（gen 1-10），剩余约 **19h**。预计 **May 23 ~02:00 服务器时间**。

---

### exp_015 (fixed_mix r=0.25, seed=44, GPU 1) — **存活，正常运行**

- **GPU 1**: 49% 利用率, 25017 MiB / 97887 MiB
- **进度**: Gen 0-6 已完成，**Gen 7/10 正在生成样本 28800/37500** (76.8%)
- 已完成代数指标:

| Gen | eff_rank | ppl | distinct-4 | train_loss |
|-----|----------|------|------------|------------|
| 0 | 417.55 | 9.55 | 0.7305 | — |
| 1 | 475.92 | 10.22 | 0.6379 | 1.8002 |
| 2 | 484.39 | 10.64 | 0.5156 | 1.6887 |
| 3 | 488.62 | 11.00 | 0.4518 | 1.4731 |
| 4 | 493.01 | 11.33 | 0.4156 | 1.3883 |
| 5 | 494.32 | 11.64 | 0.4008 | 1.3187 |
| 6 | 498.74 | 11.97 | 0.3994 | 1.2940 |

- **每代耗时**: ~2h（从 checkpoint 时间戳推算）
- **剩余**: gen 7 剩约 35min + gen 8-10 共 3 代 × 2h = 6h → 共 **~6.5h**
- **预估完成时间**: **May 22 ~14:30 服务器时间**

---
