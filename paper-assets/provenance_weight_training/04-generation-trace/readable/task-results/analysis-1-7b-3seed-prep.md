# analysis 1 7b 3seed prep

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_1_7b_3seed_prep_20260520T205914_result.json`
- **Structured JSON:** [`f893cc2b162f06a406c7.json`](../../sessions/f8/f893cc2b162f06a406c7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

模板已生成并注册：`artifacts/_project/report/1_7b_3seed_comparison_template.md`

核心发现摘要：

**2-seed 数据**（seed42 + seed123 已填入）：
- **Holdout**: Δ=−0.012±0.003，方向一致（两 seed 均 adaptive 优），但幅度比 0.6B 缩小约 70%
- **OWT**: Δ=−0.005±0.006，接近 0
- **Wiki**: Δ=**+0.023±0.018**，adaptive **劣于** uniform。seed42 的 +0.036 是主要来源（uniform 侧 seed42 偏低 10.919 拉大了差距）
- **Downstream**: Δ≈0，与 0.6B 结论一致

**Wiki OOD variance 关注点**：seed42 +0.036 vs seed123 +0.010，variance 主要来自 uniform 侧（std=0.016），不是 adaptive 侧（std=0.002）。seed456 将决定 3-seed 均值和 "no harm at scale" framing 是否需要加 qualifier。

**对论文 claim 的影响**：seed456 对 "method scales without degradation" 风险低，但对 Wiki OOD 信号的定论是 **中等风险**——若 3-seed Wiki Δ 显著 positive，需在 results 中 acknowledge。

---
