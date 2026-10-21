# analysis scale s42 failure

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_scale_s42_failure_20260518T024501_result.json`
- **Structured JSON:** [`bae82ff6d0cb8e7ddaf0.json`](../../sessions/ba/bae82ff6d0cb8e7ddaf0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/scale_s42_failure_analysis.md` 并注册。

核心发现：

**Non-consensus pairs (K<4)**: ent→ppl (K=1), ece→ppl (K=2), ent→d3 (K=3)。两个 ppl pairs 在 Baseline 中也仅 K=3，是 perplexity 爆炸增长导致的结构性问题，非 Scale 特有。ent→d3 的 PG_fwd 以 p=0.053 差 0.003 未过阈值。

**TY=0/8 双重根因**：
1. token_entropy 在 Scale 中被 ADF 判定为 I(1)（Baseline 为 I(0)），d_max 从 0→1，df_resid 从 7→4，摧毁 ent→d* 三个 pair 的 TY 统计力（Wald 从 121-566 降至 0.02-0.29）
2. 即使 df_resid 相同（ece→d* 两模型均为 4），Scale 的 Wald 统计量仍比 Baseline 小 10-100x（ece→d1: 0.16 vs 18.40），说明 Granger 因果信号本身更弱——大模型的 canary 相对方差更低（CV 0.85-0.94x），而下游指标方差更高（CV 1.16-1.52x），信噪比恶化

**论文 framing 建议**：K≥4=5/8 应表述为"多数共识仍成立"，3 个 non-consensus 中 2 个是 ppl pairs（全表均弱），Scale 特有弱点仅 ent→d3 一个 borderline miss。TY=0/8 归因于 T=11 下积分阶数估计不稳定（与 C003 一致）。

---
