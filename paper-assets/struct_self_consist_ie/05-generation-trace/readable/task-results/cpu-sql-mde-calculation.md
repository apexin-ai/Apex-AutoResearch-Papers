# cpu sql mde calculation

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_cpu_sql_mde_calculation_20260521T120032_result.json`
- **Structured JSON:** [`2fa309fe0d1f293564f7.json`](../../sessions/2f/2fa309fe0d1f293564f7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### MDE 计算

**n=196, α=0.05, power=0.80:**

| 框架 | σ_diff 假设 | MDE |
|------|-----------|-----|
| Paired t-test | σ=0.10 | **2.00pp** |
| Paired t-test | σ=0.15 | **3.00pp** |
| McNemar (binary) | p_disc=12.76% | **7.15pp** |

### 与观察效应对比

- Spider 观察到的 MV gain = **+0.51pp**，远低于 MDE (2-7pp)
- 检测 0.51pp 效应的统计功效仅 **4-11%**（需要 80%）
- 87% degeneracy 使有效样本仅 ~25 个，进一步恶化

### 所需样本量（σ=0.125）

| 目标效应 | 所需 n |
|---------|--------|
| 0.5pp | 4,906 |
| 1.0pp | 1,227 |
| 2.0pp | 307 |

### 结论

n=196 **严重 underpowered**。但对论文论证不致命——SQL 实验的价值在于证明框架跨任务适用性，方向性正结果 (+0.51pp) 与 NER 一致，即使单独不显著。Rebuttal 可承认 limitation 并指出需更大规模验证。

报告已注册：`art_20260521_8caaeb`

---
