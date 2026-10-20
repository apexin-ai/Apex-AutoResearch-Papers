# ops check exp020 exp022c final

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-exp020-exp022c-final_20260524T105336_result.json`
- **Structured JSON:** [`1614eb0a7e1c258ca1e1.json`](../../sessions/16/1614eb0a7e1c258ca1e1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

日志 80 秒前还在更新，实验正在活跃运行。根据时间线估算进度：

- exp_022c 于 15:40 启动，现在 ~18:54，已运行约 3h14m
- Gen 1 已完成（训练+评估），正在 Gen 2 的数据生成阶段（generating 35000 synthetic samples）
- 日志中大量 right-padding warning 说明正在生成数据

exp_020 从日志看，Gen 0 完成时间 ~May 24 早上，到 Gen 10 完成 ~18:50，每代约 1-1.5h。exp_022c 3代总计预计 ~5-6h，还需约 2-3h。

---

## 结果汇总

### exp_020 (GPT-2-medium, r=0, 10-gen) — **已完成** ✓

正常跑完所有 10 代，日志最后输出 `FINAL RESULTS SUMMARY`。Gen 10 metrics：

| Metric | Gen 0 | Gen 5 | Gen 10 |
|--------|-------|-------|--------|
| **Eff. Rank** | 23.09 | 151.94 | **97.02** |
| **PPL** | 15.45 | 49.35 | **545.97** |
| **Distinct-4** | 0.913 | 0.658 | **0.379** |
| **σ₁** | 6598.1 | 1317.5 | **1497.7** |
| **log_det** | 689.4 | 732.1 | **320.6** |
| **train_loss** | — | 1.913 | **1.690** |

趋势清晰：纯合成训练下 PPL 指数级恶化（15→546），D4 持续下降（0.91→0.38），eff_rank 先升后降（Gen 2 峰值 185→Gen 10 降至 97）。

### exp_022c (GPT-2-medium, r=0.3, 3-gen) — **进行中**

- 当前状态：**Gen 2 数据生成中**（generating 35000 synthetic samples）
- Gen 1 已完成：eff_rank=136.08, ppl=12.02, D4=0.905
- 进程 PID 868285，tmux session `exp_022c`
- 启动于 15:40，已运行 ~3h15m，预计还需 **2-3h** 完成剩余 Gen 2 训练+评估 + Gen 3 全流程

### GPU 使用

| GPU | 型号 | 使用率 | 显存 | 用途 |
|-----|------|--------|------|------|
| 0 | RTX PRO 6000 (96GB) | **0%** | 0/97887 MiB | 空闲 |
| 1 | RTX PRO 6000 (96GB) | **100%** | 26431/97887 MiB | exp_022c |

---
