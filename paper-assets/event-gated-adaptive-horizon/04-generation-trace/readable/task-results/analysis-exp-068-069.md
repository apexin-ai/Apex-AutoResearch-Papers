# analysis exp 068 069

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_068_069_20260525T072547_result.json`
- **Structured JSON:** [`876d7b2cec41827d5f57.json`](../../sessions/87/876d7b2cec41827d5f57.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新完毕。汇总报告：

---

```
exp_068_008d_walker_repro_s1 (trained dt_emb, seed=1):
- conclusion: SUCCESS — 复现了 CIVO
- eval_return_final: 39.1 @105K (peak 192.4 @55K → 崩塌至 26.9 @95K)
- ve_ratio trajectory: 0→0.2→0.3→0.6→0.6→1.3→1.6→4.6→4.6→2.7
- nve_peak: 6.57x @85K (ve_ratio=4.6 vs baseline=0.7007)
- nve_final: 4.12x @105K (ve_ratio=2.7 vs baseline=0.656)
- nve_onset: 45K (NVE=1.81x, 首次 > 1.5x)
- civo_alert: YES @85K (detector fired: ve_ratio=4.645, delta_ve=3.090, eval_decline=3/3)
- gate: dt_2_frac=100% (fixed dt=2)
- 与 parent 008d 对比: 完全一致的 CIVO 模式——trained dt_emb 下 ve_ratio 从 55K 起加速上升，
  eval 从 55K 的 192 单调崩塌到 85K 的 33。Walker trained seeds 现有 8/8 onset 记录。

exp_069_008f_walker_repro_s1 (no dt_emb, dt_embed_dim=0, seed=1):
- conclusion: SUCCESS — 确认 no dt_emb 阻止 CIVO
- eval_return_final: 237.8 @105K (peak 390.1 @95K, 全程稳定上升)
- ve_ratio trajectory: 0→0.1→0.2→0.2→0.3→0.3→0.4→0.3→0.3→0.4
- nve_peak: 0.66x @75K
- nve_final: 0.61x @105K (ve_ratio=0.4 vs baseline=0.656)
- civo_alert: NO
- gate: dt_2_frac=100% (fixed dt=2)
- 与 parent 008f 对比: 完全一致——no dt_emb 下 ve_ratio 始终平稳 (≤0.4)，
  eval 持续增长无崩塌。NVE 远低于 1.5x 阈值 (max 0.66x)。

C2 causal control 结论强化:
- 同一 seed=1，同一服务器，唯一差异 = dt_embed_dim (trained vs 0)
- trained dt_emb: NVE 6.57x, eval 崩塌 192→39 ✓
- no dt_emb:     NVE 0.66x, eval 稳定 238 ✓
- dt_emb 是 CIVO 的必要条件得到进一步确认
```

---
