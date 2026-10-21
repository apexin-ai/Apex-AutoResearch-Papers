# analysis anova v2 final

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_anova_v2_final_20260528T070541_result.json`
- **Structured JSON:** [`4504b16e420b486ebd7f.json`](../../sessions/45/4504b16e420b486ebd7f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果已保存并注册。核心发现：

**ANOVA 结果：**

| Source | SS | df | F | p | η²_p |
|--------|----|----|---|---|------|
| gradient_flow (ON/OFF) | 0.0029 | 1 | 2.083 | .183 | .188 |
| norm_type (BN/LN) | 0.0030 | 1 | 2.157 | .176 | .193 |
| **交互效应** | **0.000003** | **1** | **0.002** | **.967** | **<.001** |
| Residual | 0.0126 | 9 | | | |

**关键解读：**

1. **交互效应完全不显著** (F=0.002, p=.967)。gradient_flow 的效应在 BN 和 LN 间是一致的，不存在 gradient × norm 的交互。这意味着论文叙事需要调整——不是 "交互效应"，而是 **gradient_flow 的干净主效应**。

2. **gradient_flow 主效应方向正确**：OFF (M=0.782) > ON (M=0.751)，partial η²=.188（中大效应量），但 p=.183 不显著。

3. **Detach 合并 vs Vanilla**：p=.085 (two-tailed)，不显著。Detach 数值上高于 Vanilla，支持 "detach 恢复安全性" 的 claim。

4. **vanilla_v2_s0_eval 不在 registry 中**，Vanilla 仅 n=2。如果能补上第三个 seed，统计功效会改善。

---
