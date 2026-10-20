# analysis nve threshold sensitivity

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_nve-threshold-sensitivity_20260527T104656_result.json`
- **Structured JSON:** [`8ac31672a5f2073c4374.json`](../../sessions/8a/8ac31672a5f2073c4374.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## NVE Threshold Sensitivity Analysis

| Threshold | TP | FP | TN | FN | Accuracy | Precision | Recall | F1 |
|-----------|----|----|----|----|----------|-----------|--------|------|
| 1.0 | 8 | 4 | 22 | 0 | 88.2% | 66.7% | 100% | 0.800 |
| 1.3 | 8 | 4 | 22 | 0 | 88.2% | 66.7% | 100% | 0.800 |
| **1.5** | **8** | **3** | **23** | **0** | **91.2%** | **72.7%** | **100%** | **0.842** |
| 1.7 | 8 | 2 | 24 | 0 | 94.1% | 80.0% | 100% | 0.889 |
| **2.0** | **8** | **0** | **26** | **0** | **100%** | **100%** | **100%** | **1.000** |
| 3.0 | 8 | 0 | 26 | 0 | 100% | 100% | 100% | 1.000 |

数据集：8 CIVO + 26 No-CIVO = 34 experiments（Walker + Cheetah，排除 Hopper、killed/failed、ambiguous）

### 关键发现

**NVE 存在明显的分类间隔**：
- CIVO 实验 NVE peak 范围：3.78 – 138.7（最小 3.78）
- No-CIVO 实验 NVE peak 范围：0.10 – 1.88（最大 1.88）
- **间隔 [1.89, 3.77] 内任何阈值都能实现完美分类**

**当前阈值 1.5 的问题**：3 个假阳性，全来自 frozen/no_dt_emb 实验中的正常 NVE 波动：
- `exp_057_frozen_dt_emb_walker_s2`: NVE=1.88
- `exp_047_frozen_dt_emb_walker_s1`: NVE=1.71
- `exp_082_cheetah_no_dt_emb_s0`: NVE=1.58

**建议**：将阈值从 1.5 上调至 **2.0**。在当前数据上实现完美 F1=1.0，且距离 CIVO 最小 NVE（3.78）还有 1.78x 的安全裕量。1.5 过于激进，会把 frozen dt_emb 的正常波动误报为 CIVO onset。

---
