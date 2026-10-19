# infra bootstrap deep check

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_bootstrap-deep-check_20260523T045822_result.json`
- **Structured JSON:** [`bf6ffee88e466166f8e8.json`](../../sessions/bf/bf6ffee88e466166f8e8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据收集完毕。

---

## 诊断报告

### 进程状态

| 进程 | PID | 状态 | CPU% | 运行时长 | Workers | Worker 状态 |
|------|-----|------|------|---------|---------|------------|
| DE bootstrap v2 | 550508 (python) | alive, sleeping (等 Pool) | 5.5% | 9h09m | ~64 子进程 (550567-550699) | **R (running)**, 活跃计算中 |
| Gemma XNLI bootstrap | 549893→549898 (bash→python) | alive, sleeping (等 Pool) | 0.0% (wrapper) | 14h04m | ~32 子进程 (550127-550161) | **R (running)**, 活跃计算中 |

### Workers 确认活跃

- PID 550567 (DE worker): State=R, nonvoluntary_ctxt_switches=14,083
- PID 550127 (Gemma worker): State=R, nonvoluntary_ctxt_switches=24,612
- 高 nonvoluntary_ctxt_switches 说明 workers 在被调度器频繁抢占——**正在算，但被大量争抢 CPU**

### 系统负载

- **Load average: 504 / 678 / 682**（208 核机器）
- 运行中进程: 1505 / 14613
- 内存: 217GB used / 1TB total（内存充足）

### 日志状态

两个日志都只有 6 行，最后一行是 `[EN->EN] Bootstrap (2000 seeds, N workers)...`，之后再无输出。日志最后修改时间：
- DE log: 12:50:17（启动后立即）
- Gemma log: 12:45:01（启动后立即）

脚本只在**每个 direction 全部 2000 seeds 跑完后**才打印下一行。还没跑完第一个 direction。

### 输出文件

两个目标文件均**不存在**（未完成）：
- `data/llama31/de_bootstrap_n2000_results.json` ❌
- `data/xnli/gemma2/probe_results_bootstrap_n2000.json` ❌

### 判断

**两个进程都在推进，没有卡死，但极度缓慢。** 根本原因是系统 load 达到 500-680（正常应 < 208），CPU 争抢极其严重。96 个 bootstrap workers + 机器上其他大量进程同时在跑，每个 worker 实际分到的 CPU 时间极少。按当前速度，跑完 4 个 direction × 2000 seeds 可能还需要数十小时。

**建议**：如果要加速，需要杀掉机器上其他占 CPU 的进程，或减少 worker 数量避免过度争抢。

---
