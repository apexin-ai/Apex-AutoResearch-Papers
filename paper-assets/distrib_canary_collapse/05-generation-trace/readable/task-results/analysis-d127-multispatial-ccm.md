# analysis d127 multispatial ccm

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_d127_multispatial_ccm_20260520T093512_result.json`
- **Structured JSON:** [`7bb02cf7264718abbe84.json`](../../sessions/7b/7bb02cf7264718abbe84.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

D127 Multispatial CCM 完成。核心发现：

**Per-pair CCM（最可靠的结果）**:

| Regime | Forward (canary→ds) | Reverse (ds→canary) | 解读 |
|--------|-------------------|-------------------|------|
| α=0.50 | agg ρ=0.75, 6/8 sig | agg ρ=0.35, 3/8 sig | token_entropy→distinct 单向因果（ρ>0.93, p<0.005），reverse 不显著 |
| α=1.0 | agg ρ=0.62, 6/8 sig | agg ρ=0.96, 8/8 sig | 双向耦合太强，无法区分方向 |
| α=0.0 | agg ρ=0.26, 2/8 sig | agg ρ=-0.11, 1/8 sig | null baseline 基本不显著 ✓ |

**最关键信号在 α=0.50**：token_entropy→distinct_{1,2,3} 三对均显示强单向前向因果（ρ=0.94-0.97, p≤0.005），而反向均不显著。这是 CCM 框架下 canary→downstream 因果关系的清晰证据。

**注意**: Multispatial 聚合（8 replicates 拼接）因复制品非独立（共享时间序列）而膨胀了 reverse ρ，per-pair 分析更可信。

产出文件均在 `westd-17855:/root/autodl-tmp/distrib_canary_collapse/artifacts/d127_ccm/`。

---
