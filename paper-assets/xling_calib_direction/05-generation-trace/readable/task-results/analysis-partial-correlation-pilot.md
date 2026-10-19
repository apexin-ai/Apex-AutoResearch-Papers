# analysis partial correlation pilot

**Shifting the Cross-Lingual Calibration Pareto Frontier: Probe-Based Calibration Transfer via CaCLR** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_partial_correlation_pilot_20260521T041917_result.json`
- **Structured JSON:** [`7266b390ece40bf9aa65.json`](../../sessions/72/7266b390ece40bf9aa65.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果摘要

发现了 **Simpson's Paradox**——比预期的"depth confound"故事更强。

### 核心数值

|  | Raw rho | Partial rho (ctrl depth) | Per-layer median rho |
|--|---------|--------------------------|---------------------|
| **Qwen2.5-7B** | −0.16 (ns) | +0.18 (ns, underpowered) | **+0.80** |
| **Llama-3.1-8B** | −0.16 (ns) | **+0.41 (p=0.006)** | **+0.60** |

### 机制

- CKA 随 depth 下降（rho≈−0.5），AUROC 随 depth 上升（rho≈+0.65）
- 直接 pool 所有 layer：两个趋势相消，raw correlation 接近零/弱负
- **控制 depth 后符号反转为正**：在同一层内，CKA 越高（表示越相似）→ transfer AUROC 越高
- 14/17 个 layer-level correlation 为正

### 判断

**YES — CKA 有独立解释力。** Reviewer 说的 depth confound 确实存在，但控制后关系更强而非消失。这是 Simpson's paradox，反而加强了论文 novelty：

1. 直接回应 Reviewer 的 confound 质疑
2. 符号反转本身就是 publishable finding
3. 机制清晰：同一 depth 下，跨语言表示越相似 → 校准方向迁移越好

**局限**：Qwen partial correlation 不显著（n=40 underpowered）；per-layer n=5 只能看方向。

产出已写入 `artifacts/partial_correlation_pilot.md`。

---
