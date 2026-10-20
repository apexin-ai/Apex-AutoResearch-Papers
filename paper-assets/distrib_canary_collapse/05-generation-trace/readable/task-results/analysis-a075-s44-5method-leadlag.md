# analysis a075 s44 5method leadlag

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_a075_s44_5method_leadlag_20260516T141651_result.json`
- **Structured JSON:** [`f478181339117025c9c2.json`](../../sessions/f4/f478181339117025c9c2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。结果摘要：

## α=0.75 seed=44 — 5-Method Lead-Lag Results

| Method | Forward sig | Reverse sig |
|--------|-------------|-------------|
| Naive XCorr | 4/8 | — |
| Diff XCorr (FDR) | 8/8 | 8/8 |
| Threshold Onset | 4/8 | 0/8 |
| **Perm Granger (FDR)** | **6/8** | **0/8** |
| TY Granger | 1/8 | 0/8 |

**Consensus robust pairs (≥3/5): 5/8**

关键发现：
- Perm Granger 方向不对称性极强：6/8 forward vs 0/8 reverse
- 比 s42 参考结果（3/8 FDR fwd）更强，cross-seed drift 偏高但方向一致
- TY 仅 ece→distinct_2 显著（d_max=1, df_resid=5, F=23.56）���token_entropy pairs 因 d_max=2 导致 df_resid=1 无检验力
- 最强 pair: ece→distinct_2（4/5 methods 一致）

Artifacts 已注册。完整 JSON 在 `westd-19828:/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a075_s44/analysis/5method_leadlag.json`。

---
