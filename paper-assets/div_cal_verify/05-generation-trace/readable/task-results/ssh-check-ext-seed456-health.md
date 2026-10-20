# ssh check ext seed456 health

**The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_ext_seed456_health_20260513T214212_result.json`
- **Structured JSON:** [`58edb45ea023446d9cf0.json`](../../sessions/58/58edb45ea023446d9cf0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告

### ext_seed456 — **已完成** ✓

刚于 05:43:16 CST 完成，cuda:1 已释放（0MB）。全部 8 代结果：

| Gen | PPL | RankMe | kNN | Rare n-gram | Rank corr |
|-----|-----|--------|-----|-------------|-----------|
| 0 | 36.51 | 273.85 | 0.9880 | 0.0284 | -0.0103 |
| 1 | 44.77 | 291.93 | 0.9880 | 0.0203 | -0.0404 |
| 2 | 50.84 | 298.52 | 0.9870 | 0.0152 | -0.0292 |
| 3 | 54.43 | 298.35 | 0.9870 | 0.0130 | -0.0223 |
| 4 | 49.91 | 295.86 | 0.9880 | 0.0118 | -0.0321 |
| 5 | 50.45 | 297.37 | 0.9880 | 0.0111 | -0.0300 |
| **6** | **47.09** | **294.35** | **0.9880** | **0.0100** | **-0.0207** |
| **7** | **43.90** | **292.69** | **0.9880** | **0.0106** | **-0.0227** |

Gen-0 RankMe baseline: 231.08。PPL 在 gen 3 达到峰值 54.43 后回落至 gen 7 的 43.90。Rare n-gram 持续下降后在 gen 7 微幅回弹。

### chain_cuda1 — 仍在等待

chain_cuda1.log 只有一行 "Waiting for seed456_methods to finish..."（从 03:32 开始等待）。它等的是 tmux session `seed456_methods`，而不是 ext_seed456 进程本身。ext_seed456 已结束但如果 tmux session 没被清理，chain 可能继续等；如果 session 已随进程退出而消失，chain 会继续执行 `medium_external`。

**rgds_seed456 未被 chain_cuda1 启动**——chain 的后续任务是 medium_external → medium_random50，不包含 rgds_seed456。

### medium_rgds_seed42（cuda:0）— Gen 0/7 训练中

PID 312677，占用 78GB/28GB，刚启动于 05:25。当前在 Gen 0 step [3/5] Training student。刚开始，预计总运行 ~2.5h（每 gen ~20min × 8 gen）。

---
