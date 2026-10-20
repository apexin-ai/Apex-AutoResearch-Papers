# analysis paper figure data

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_paper-figure-data_20260514T185842_result.json`
- **Structured JSON:** [`821811b9536b9499c37e.json`](../../sessions/82/821811b9536b9499c37e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

提取完成。汇总：

| 实验 | Checkpoints | 最终 step | eval_return | ve_ratio | 状态 |
|------|------------|-----------|-------------|----------|------|
| **exp_001_baseline** | 51 | 505K | 970.41 | 0.69 | Healthy |
| **exp_008d** (trained dt_emb, s0) | 6 | 55K | 82.75 | **1.67** | Collapsed |
| **exp_009b** (trained dt_emb, s2) | 11 | 105K | 267.93 | 0.25 | Partial collapse |
| **exp_008f** (no dt_emb, s0) | 11 | 105K | 503.21 | 0.20 | Healthy |
| **exp_009c** (no dt_emb, s2) | 11 | 105K | 148.34 | 0.75 | Healthy |
| **exp_008e_v3** (untrained dt_emb) | 11 | 105K | 869.88 | 0.53 | Healthy (mitigation) |
| **exp_008a** (B+ control) | 11 | 105K | 777.66 | 0.39 | Healthy |
| **exp_006** (fixed dt=2) | 7 | 65K | 132.86 | **2.72** | Collapsed |

数据已保存到服务器 `/root/autodl-tmp/event-gated-adaptive-horizon/logdir/paper_figure_data.json`，产出已注册 (`art_20260514_a00b68`)。

关键发现与论文因果链吻合：collapsed 实验 (exp_008d, exp_006) 的 ve_ratio 远 >1（delusional critic），而 healthy 实验的 ve_ratio 稳定在 0.2-0.75。

---
