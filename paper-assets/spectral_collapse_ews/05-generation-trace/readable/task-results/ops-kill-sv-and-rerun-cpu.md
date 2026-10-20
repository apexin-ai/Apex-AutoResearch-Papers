# ops kill sv and rerun cpu

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_kill-sv-and-rerun-cpu_20260525T225201_result.json`
- **Structured JSON:** [`16972d73afcc24a6f0f4.json`](../../sessions/16/16972d73afcc24a6f0f4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个任务全部完成。

## 任务 1: Kill GPU 进程
- PID 3307 已 kill，cuda:0 显存已释放（0 MiB）

## 任务 2: SV 分布提取结果

**产出文件**：
- JSON: `/root/spectral_collapse_ews/results/sv_distributions_gen0_gen2.json` (51KB)
- PDF: `/root/spectral_collapse_ews/results/sv_distribution_comparison.pdf` (21KB)

**分布形态变化分析**：

| 指标 | Gen 0 (base) | Gen 2 (collapsed) | 变化 |
|------|-------------|-------------------|------|
| σ₁ | 6598.11 | 1886.86 | **-71.4%** |
| r_eff | 23.09 | 113.30 | **+390.8%** |
| σ_min | 0.018391 | 0.027984 | +52.2% |
| Tail/Head ratio | 0.000006 | 0.000024 | ×4 |
| Gini coefficient | 0.8575 | 0.7580 | -11.6% |

**文字描述**：
- **σ₁ 大幅压缩（-71.4%）**：主成分能量从 6598 降至 1887，说明递归训练破坏了表示空间中的主导方向
- **尾部相对膨胀**：Tail/Head ratio 从 0.000006 到 0.000024（×4），尾部奇异值相对增大
- **整体均匀化**：Gini 从 0.86 降至 0.76，r_eff 从 23 跃升至 113（+391%）。谱分布趋向均匀，这是 spectral collapse 的典型特征——信息维度表面上"扩展"了，实际上是因为主成分崩塌而非尾部真正携带了更多信息

---
