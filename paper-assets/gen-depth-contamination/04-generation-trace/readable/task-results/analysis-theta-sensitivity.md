# analysis theta sensitivity

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_theta_sensitivity_20260517T195743_result.json`
- **Structured JSON:** [`f8ba2c52a76641575d7a.json`](../../sessions/f8/f8ba2c52a76641575d7a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。21 个实验的 K* 在 6 个 θ 值下的结果：

**核心结论：**
- **C4 域 K\*=2** 在 θ∈[0.575, 0.625] 稳定（10/13 实验），边界 1v2 AUC 在 0.61-0.70 间，margin +0.01 到 +0.10
- **arXiv 域 K\*=3** 在 θ∈[0.55, 0.625] 稳定（4/5 实验），边界 2v3 AUC 在 0.622-0.655 间
- **Retrain-chain K\*=4** 在全范围 [0.55, 0.70] 完全不变（最小 AUC=0.798）
- **θ=0.60 是安全区间 [0.575, 0.625] 的中心**，核心发现在此区间内均保持不变

产出已注册：`art_20260517_d4ffdf`

---
