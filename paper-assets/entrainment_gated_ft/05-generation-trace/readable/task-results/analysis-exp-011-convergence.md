# analysis exp 011 convergence

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp-011-convergence_20260519T161625_result.json`
- **Structured JSON:** [`aa6623dc208e318b6613.json`](../../sessions/aa/aa6623dc208e318b6613.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部输出已生成。结果摘要：

**新 benchmark Spearman 结果（exact permutation test）：**

| Benchmark | ρ | exact p | std(pure) | std(h3-1) | conv_ratio |
|-----------|------|---------|-----------|-----------|------------|
| boolq | +0.20 | 0.7833 | 0.0163 | 0.0236 | 0.69 |
| piqa | -0.50 | 0.4500 | 0.0054 | 0.0034 | 1.59 |
| sciq | +0.10 | 0.9500 | 0.0087 | 0.0074 | 1.19 |
| copa (补充) | -0.67 | 0.2667 | 0.0262 | 0.0047 | 5.57 |

**合并 9-benchmark Bonferroni 校正：0 个 benchmark 显著（α=0.05）。** LAMBADA 原来 raw_p=0.0167，校正后 0.1503，也不再显著。BH-FDR 同样无一显著。

**核心结论：未找到第二个 significant anchor。** 即使 LAMBADA 在单独检验中是最强信号（ρ=-1.0, raw_p=0.0167），合并 9 个 benchmark 做 Bonferroni 校正后也不再通过 0.05 阈值。新增的 boolq/piqa/sciq 均无显著趋势，cross-arch std 随 attention ratio 的变化没有一致方向。

COPA 作为补充（n=100），ρ=-0.67 方向与 convergence 假说一致但 p=0.2667 不显著。

输出文件：
- CSV: `/root/entrainment_gated_ft/analysis/exp011_convergence_results.csv`
- JSON: `/root/entrainment_gated_ft/analysis/exp011_convergence_summary.json`
- 脚本: `/root/entrainment_gated_ft/analysis/exp011_convergence_analysis.py`

---
