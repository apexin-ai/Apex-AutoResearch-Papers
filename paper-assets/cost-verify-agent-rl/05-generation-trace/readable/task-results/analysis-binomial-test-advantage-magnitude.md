# analysis binomial test advantage magnitude

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_binomial_test_advantage_magnitude_20260523T094718_result.json`
- **Structured JSON:** [`dcb45cc0984d976af9ff.json`](../../sessions/dc/dcb45cc0984d976af9ff.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/binomial_test_results.md` 并注册。核心结果：

**实验 B — Binomial Test**:
- H₀=0.5（随机）: p = **0.025**, z = 2.26 — 统计上显著，但效应量极小（+2.07pp）
- Wilson 95% CI: **[50.3%, 53.9%]** — 不包含 0.5，也不包含 0.191
- H₀=0.191（binary 理论）: p ≈ 0, z = 45.9 — 完全拒绝

**注意**: 论文当前写 "indistinguishable from 50%" 不准确。52.07% 在 n=3000 下统计上显著高于 50%（p=0.025），建议改为 "marginally above random chance (p = 0.025) but with negligible practical significance"。

**实验 C — Advantage 量级**:
- |mean_fail| / |mean_success| = **7.41**，接近 K−1=7
- 但理论上逐 group 加权平均的 |Â_s|/|Â_f| = **1.32**（m=4 时比值为 1，最常见）
- K−1=7 仅在 m=1（P=2.8%）时成立。7.41 的实际来源是跨 group 聚合效应，不是 m=1 主导
- 分布重叠 88%，point-biserial r=0.068 — 确认 per-window 信号极弱

---
