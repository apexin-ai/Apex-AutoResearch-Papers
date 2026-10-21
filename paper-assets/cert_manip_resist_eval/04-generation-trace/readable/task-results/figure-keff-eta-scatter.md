# figure keff eta scatter

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_figure_keff-eta-scatter_20260523T134400_result.json`
- **Structured JSON:** [`3496c33ddbbaab43af1c.json`](../../sessions/34/3496c33ddbbaab43af1c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

图已生成，清楚展示了 diversity-capability confound。

结果：
- **服务器路径**: `/root/cert_manip_resist_eval/artifacts/figures/fig_keff_eta_scatter.{pdf,png}`
- **r_full = 0.81** (全部 3003 panels，K_eff 与 η_max 高度正相关)
- **r_poolA = 0.50** (Pool A 的 126 panels，confound 显著降低)
- K_eff 范围: [2.16, 4.30], η_max 范围: [0.11, 0.46]

注意 r_full=0.81 比预期的 0.70 更高，r_poolA=0.50 与预期一致。散点图的 banding pattern 是正常的——因为 η_max 由离散的 individual ASR 值决定，包含相同"最弱模型"的 panels 会有相似的 η_max。

---
