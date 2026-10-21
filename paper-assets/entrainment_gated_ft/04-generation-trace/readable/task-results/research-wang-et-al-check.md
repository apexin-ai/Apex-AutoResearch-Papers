# research wang et al check

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_wang_et_al_check_20260518T205548_result.json`
- **Structured JSON:** [`5e35740fa32be84574a4.json`](../../sessions/5e/5e35740fa32be84574a4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已保存到 `artifacts/wang_et_al_analysis.md`。核心结论：

**Wang et al. 与我们的关系**：他们用同一批 m-a-p 模型做了系统 benchmark，但问的问题完全不同。

- 他们问 "which hybrid is best"，报告聚合分数，推荐 HGRN-2/GDN + 3:1~6:1 ratio
- **不含完整 arch × ratio × benchmark 交叉表**（只有聚合平均值和最优 ratio 下的拆分）
- **不含 MMLU/WinoGrande/BLiMP**
- 发现了 architecture-dependent hybridization effects，但没用 task complexity 维度去解释

**我们的新颖性**：分析角度差异化很大（composition depth 三假设框架），数据层面有中等增量（新 benchmark + 完整交叉数据）。**主要风险**是如果 H_agnostic 胜出（所有 task 同等退化），我们的理论贡献归零，剩余纯 benchmark 数据与 Wang et al. 高度重叠。

---
