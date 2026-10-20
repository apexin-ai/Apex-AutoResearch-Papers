# ssh check ext seed456 health

**The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_ext_seed456_health_20260513T214440_result.json`
- **Structured JSON:** [`88e57c3948ff3c531c69.json`](../../sessions/88/88e57c3948ff3c531c69.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。诊断报告：

## ext_seed456 诊断结果

### 1. 状态：已完成 ✓

实验于 `Thu May 14 05:43:16 CST 2026` 结束，总耗时约 9161 秒（~2.5h）。

### 2. 完整 gen0-gen7 Metrics

| Gen | PPL | RankMe | kNN | Rare | Corr | Ratio |
|-----|------|--------|------|--------|---------|-------|
| 0 | 36.51 | 273.85 | 0.988 | 0.0284 | -0.0103 | 1.1621 |
| 1 | 44.77 | 291.93 | 0.988 | 0.0203 | -0.0404 | 1.0686 |
| 2 | 50.84 | 298.52 | 0.987 | 0.0152 | -0.0292 | 1.1119 |
| 3 | **54.43** | **298.35** | 0.987 | 0.0130 | -0.0223 | 1.1551 |
| 4 | 49.91 | 295.86 | 0.988 | 0.0118 | -0.0321 | 1.1841 |
| 5 | 50.45 | 297.37 | 0.988 | 0.0111 | -0.0300 | 1.2186 |
| 6 | 47.09 | 294.35 | 0.988 | 0.0100 | -0.0207 | 1.0818 |
| 7 | **43.90** | 292.69 | 0.988 | 0.0106 | -0.0227 | **1.2430** |

PPL 在 gen3 达到峰值 54.43 后回落，gen7 回到 43.90（低于 gen1-6）。Rare ngram 持续下降至 ~0.01 后稳定。Ratio 在 gen7 达到最高 1.243。RankMe baseline=231.08。

### 3. rgds_seed456：已启动 ✓

chain_cuda1 在 ext_seed456 完成后立即启动了 rgds_seed456（`Thu May 14 05:43:16 CST`）。日志显示只有初始化信息，尚在 gen_0 早期阶段。

### 4. GPU 利用情况

| GPU | Utilization | Memory |
|-----|------------|--------|
| cuda:0 | 100% | 77917/97887 MiB |
| cuda:1 | 99% | 12225/97887 MiB |

两块 GPU 都在高负载运行。cuda:1 上 rgds_seed456 正在训练。

---
