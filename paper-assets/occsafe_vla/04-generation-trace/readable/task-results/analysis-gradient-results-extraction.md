# analysis gradient results extraction

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_gradient_results_extraction_20260524T120927_result.json`
- **Structured JSON:** [`efed086e55a703140f45.json`](../../sessions/ef/efed086e55a703140f45.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。汇总如下：

## gradient_analysis_mixed_seed 结果

| Condition | Mean Grad Norm | vs Vanilla | Cosine Sim | Conflict Rate | Detach |
|-----------|---------------|-----------|-----------|--------------|--------|
| **Vanilla_s0** | 0.1262 | 1.00x | — | — | No |
| **Full_OCC_s0** | 0.1272 | **1.01x** | 0.004 | 0.44 | No |
| **Detach_BN_s2** | 0.0049 | **0.04x** | — | — | Yes |
| **Random_s2** | 0.1365 | **1.08x** | 0.005 | 0.44 | No |

### Per-backbone

| Condition | DINO mean | DINO vs V | SigLIP mean | SigLIP vs V |
|-----------|----------|----------|------------|------------|
| Vanilla_s0 | 0.1838 | 1.00x | 0.0753 | 1.00x |
| Full_OCC_s0 | 0.1753 | 0.95x | 0.0846 | 1.12x |
| Detach_BN_s2 | 0.0062 | **0.03x** | 0.0038 | **0.05x** |
| Random_s2 | 0.2052 | 1.12x | 0.0757 | 1.01x |

### 关键发现
- **Full OCC (1.01x) 和 Random OCC (1.08x)** 梯度范数与 Vanilla 几乎一致，确认 OCC auxiliary head 不干扰 action head 梯度
- **Detach_BN 灾难性梯度崩塌**：仅为 Vanilla 的 4%（DINO 3%, SigLIP 5%），与 D026 结论一致
- **Cosine similarity ≈ 0**，conflict rate ≈ 44%，action 和 aux 梯度正交/独立
- **Detach_LN_s0 缺失**——目录中没有该条件的输出文件，需要检查是否运行失败或被跳过

---
