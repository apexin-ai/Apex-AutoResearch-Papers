# research gradient analysis prep

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_gradient-analysis-prep_20260527T040535_result.json`
- **Structured JSON:** [`eef94f91ba34baa1f43a.json`](../../sessions/ee/eef94f91ba34baa1f43a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告：v2 梯度分析脚本状态

### 现有脚本（可用）

| 脚本 | 路径 | 用途 | 5条件支持 |
|------|------|------|-----------|
| **v2_gradient_analysis.py** | `openvla-oft/scripts/` | patch_features 级别，合成数据 | ✅ 全5条件 |
| **run_gradient_analysis_v2.py** | `scripts/` | per-layer backbone，**真实训练数据** | ✅ 自动检测 |
| **plot_gradient_analysis_v2.py** | `scripts/` | 4-panel 可视化 (PDF) | ✅ 全条件 |
| **compare_gradient_conditions.py** | `scripts/` | 条件间对比表 | ⚠️ **只有3条件** (缺BN) |

### 分析指标

两个脚本输出的指标覆盖 ROADMAP 需要的全部证据：
- **cosine similarity** cos(g_action, g_occ) → 证明梯度正交性 (cosine≈0)
- **gradient magnitude ratio** ||g_occ||/||g_action||
- **spatial gradient variance** → Cell 1 方差 vs Cell 3 方差不对称
- **per-layer action/occ grad norms** + **conflict rate**
- **quadrant-level gradient asymmetry**

### Checkpoint 可用性

**10894 上已完成 50000_chkpt：**
| 条件 | 实验ID | occ_head |
|------|--------|----------|
| Full OCC BN (Cell 1) | `mvp_occ_s3_v2` | ✅ |
| Full OCC LN (Cell 2) | `full_occ_ln_s3_v2` | ✅ |
| Detach BN (Cell 3) | `ablation_occ_detach_s3_v2` | ✅ |

**34685 上已完成 50000_chkpt：**
| 条件 | 实验ID | occ_head |
|------|--------|----------|
| Full OCC BN (Cell 1) | `full_occ_bn_v2_s1` | 待确认 |
| Detach BN (Cell 3) | `detach_bn_v2_s0/s1/s2` | 待确认 |
| Detach LN (Cell 4) | `detach_ln_s3` | ✅ |
| Vanilla | `vanilla_v2_s1`, `vanilla_v2_s2` | N/A |

**关键问题：Checkpoint 分布在两台服务器。**
- 10894 独有：Full OCC LN
- 34685 独有：Vanilla, Detach LN
- 无法在单台服务器跑全部 5 条件

### 需要补的

1. **`compare_gradient_conditions.py` 需扩展到 5 条件**（当前只有 Vanilla / Full OCC LN / Detach LN，缺 Full OCC BN 和 Detach BN）
2. **跨服务器执行策略**：
   - 10894 跑 3 条件：Full OCC BN, Full OCC LN, Detach BN（并行3 GPU）
   - 34685 跑 2 条件：Vanilla, Detach LN（并行2 GPU）
   - 合并 JSON 结果到同一目录，用 `plot_gradient_analysis_v2.py` 出图

### 执行时间估算

`run_gradient_analysis_v2.py` 用真实数据，每条件 800 samples / batch_size 4 = 200 batches，约 7-10 分钟/条件。两台服务器并行，总计 ~15 分钟可完成全部 5 条件分析。

---
