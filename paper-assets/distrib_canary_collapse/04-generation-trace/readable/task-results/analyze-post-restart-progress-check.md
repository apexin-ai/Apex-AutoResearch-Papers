# analyze post restart progress check

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_post-restart-progress-check_20260522T021025_result.json`
- **Structured JSON:** [`9293d5e5fedaf095f53b.json`](../../sessions/92/9293d5e5fedaf095f53b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

### westd-17855 (350G, 67% used, 119G avail)

| 实验 | Gen/预期 | 状态 | 当前进度 |
|------|---------|------|---------|
| **t25_a060_s42_fp32★** | 16/26 | ⚠️ RUNNING (v2+v3 冲突) | GPU 3 双进程竞争 |
| **t25_a050_s42_fp32** | 16/26 | ⚠️ RUNNING (v2+v3 冲突) | GPU 0 双进程竞争 |
| t20_a060_s43_fp32 | 18/21 | RUNNING (v2) | Gen 17/20 生成合成数据，~1-1.5h 完成 |
| t25_a045_s43_fp32 | 6/26 | RUNNING | Gen 5/25, GPU 5 |
| t15_a075_s43_fp32 | 4/16 | RUNNING | Gen 3/15, GPU 1 |
| t10_a075_s43_fp32 | 3/11 | RUNNING | Gen 2/10, GPU 2 |

### westd-19828 (250G, 42% used, 147G avail)

| 实验 | Gen/预期 | 状态 | 当前进度 |
|------|---------|------|---------|
| t25_a075_s43_fp32 | 6/26 | RUNNING | GPU 0 |
| t10_a050_s43_fp32 | 3/11 | RUNNING | GPU 1 |

### 无已完成实验，d102 暂无法执行

---

### ⚠️ 严重问题：t25_a060★ 和 t25_a050 有双进程冲突

GPU 实占确认：

- **GPU 0**: PID 552687 (t25_a050 v2) + PID 582623 (t25_a050 v3 --start_gen 13) → 28622 MiB / 24G
- **GPU 3**: PID 552609 (t25_a060 v2) + PID 582545 (t25_a060 v3 --start_gen 14) → 28622 MiB / 24G

v2 进程（03:32 启动，无 --start_gen）和 v3 进程（09:01 启动，带 --start_gen）同时写同一输出目录，同一 GPU。结果可能被覆盖/污染，GPU 内存双倍占用导致训练减速。

**建议**：kill v2 进程（PID 552609 + 552687 及其父进程），保留 v3（正确的 resume 版本）。是否执行？

### 另注
- t20_a060_s43 v1 曾因磁盘满失败（已恢复，v2 在跑，当前磁盘充足）
- t20_a060_s43 最接近完成（18/21），预计 ~1-1.5h 后可跑 d102

---
