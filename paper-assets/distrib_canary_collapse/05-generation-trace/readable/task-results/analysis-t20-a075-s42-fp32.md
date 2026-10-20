# analysis t20 a075 s42 fp32

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_t20_a075_s42_fp32_20260520T182930_result.json`
- **Structured JSON:** [`aefc4d79acd30f645516.json`](../../sessions/ae/aefc4d79acd30f645516.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## T=20 α=0.75 s42 fp32 分析结果

### 核心指标

| 指标 | 值 |
|------|-----|
| **PermG Forward** | **6/8** |
| PermG Reverse | 0/8 |
| Diff XCorr FDR fwd | 7/8 |
| Threshold Onset fwd | 6/8 |
| Naive XCorr fwd | 4/8 |
| TY Granger fwd | 5/8 |
| **K≥3 Robust Pairs** | **6/8** (全部 4/5 票) |

### 预测验证

| | Predicted | Observed |
|---|-----------|----------|
| PermG count | 7 | 6 |
| 95% CI | [6, 8] | 6 ∈ [6,8] |
| **Verdict** | | **PASS** (lower boundary) |
| **Scenario** | | **A (T-invariance)** |

### 与 T=10 对比

T=10 baseline PermG = 6/8, T=20 = 6/8, delta = 0. 完全一致。

### Cross-alpha T=20 全景

| α | T=20 PermG | Scenario |
|---|-----------|----------|
| 0.50 | 6/8 | A (T-invariant) |
| 0.60 | 0/8 | Sync dip |
| **0.75** | **6/8** | **A (T-invariant)** |
| 1.00 | 6/8 | A (T-invariant) |

### 关键发现

1. **T-invariance 确认**：T=20 相比 T=10 零增益，6/8 是结构性上限
2. **Mauve 非检测是结构性的**：两个 mauve pair PermG p > 0.4，不是 borderline，不是 power 问题
3. **方向性不对称强**：PermG 6/8 fwd vs 0/8 rev，因果方向明确
4. **3/4 alpha 值 T-invariant at 6/8**：α=0.60 sync dip 仍是唯一异常点

产出已注册：`art_20260520_9b6aa5` (verify JSON), `art_20260520_248a09` (analysis report)

---
