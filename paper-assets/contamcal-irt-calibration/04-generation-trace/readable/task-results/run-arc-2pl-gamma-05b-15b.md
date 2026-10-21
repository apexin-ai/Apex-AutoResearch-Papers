# run arc 2pl gamma 05b 15b

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_run_arc_2pl_gamma_05b_15b_20260516T091149_result.json`
- **Structured JSON:** [`2e1ad012874ee56d7a02.json`](../../sessions/2e/2e1ad012874ee56d7a02.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry updated. Here's the summary:

## ARC 2PL+γ 结果

| Benchmark | N_mod | N_item | γ̂ | 95% CI | R̂ | ESS | PPP | raw_MAE | cal_MAE | ΔMAE |
|-----------|-------|--------|------|--------|------|-----|-----|---------|---------|------|
| arc_challenge | 8 | 1172 | 2.734 | [1.31, 4.14] | 1.009 | 1315 | 0.000 | — | — | — |

**关键发现：**
- 收敛良好：Rhat=1.009, ESS=1315, 0 divergences
- γ̂=2.73 显著排除零（CI 不含 0）
- **PPP=0.000 仍然失败** — 与 4PL+γ 一样

**结论（negative）：** 2PL+γ 并没有解决 ARC 的 PPP 问题。原因不是过参数化（4PL 参数太多），而是 N=8 模型 vs 1172 items 的根本性数据稀疏 + ARC 可能违反 IRT 单维假设（item clustering/multidimensionality）。γ 估计因 PPP 失败不可靠。

**Models included:** 8 个 1.5B aligned（d000/d005/d025/d100 × s42/s123），比预期 N=5 多（因为 s123 系列已完成 eval）。

---
