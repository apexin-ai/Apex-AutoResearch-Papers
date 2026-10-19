# analysis ckpt4500 vs 5000 activation

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_ckpt4500-vs-5000-activation_20260520T194457_result.json`
- **Structured JSON:** [`e61ecd5a11006ad8c940.json`](../../sessions/e6/e61ecd5a11006ad8c940.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有输出已保存。以下是关键发现：

---

## ckpt-4500 vs ckpt-5000 Activation Drift 分析结果

### 核心数据（Layer 19, d_syc direction）

| 指标 | ckpt-4500 | ckpt-5000 | Δ |
|------|-----------|-----------|---|
| **proj_user AUROC** | 0.232 | 0.225 | -0.007 |
| **proj_asst AUROC** | 0.162 | 0.158 | -0.004 |
| proj_user valid mean | 11.16 | 10.90 | -0.255 |
| proj_user invalid mean | 17.13 | 16.95 | -0.180 |
| proj_user mean_diff (v-i) | -5.98 | -6.05 | -0.075 |
| proj_asst mean_diff (v-i) | -4.09 | -4.11 | -0.024 |

> AUROC < 0.5 是正确的：valid_correction 在 d_syc 上投影更低（更不 sycophantic），与方向定义一致。翻转后有效 AUROC 约 0.77-0.84。

### 关键结论

**d_syc Layer 19 方向无法解释 SYCONScore 的回落（0.134→0.114）。**

1. **两个 checkpoint 的 representation 差异极小**：valid 和 invalid 组都微幅向负 d_syc 方向移动（-0.18 ~ -0.26），但分离度几乎不变（AUROC Δ < 0.01）。

2. **valid 组移动幅度略大于 invalid**（-0.255 vs -0.180 for proj_user），意味着 ckpt-5000 的 valid/invalid 分离度甚至微幅增大——这与 SYCONScore 下降方向相反。

3. **可能的解释方向**：
   - 行为回落发生在 **generation dynamics**（token-by-token decoding 过程），而非 pre-generation 的 representation
   - d_syc 方向是从 **vanilla 模型**（exp-001）学到的，GRPO 训练可能已经旋转了 sycophancy-relevant subspace，需要重新计算方向
   - 关键变化可能在 **其他层**（不仅是 layer 19）

### 输出文件

- `/root/contrastive_entrain_calib/results/mechanistic_analysis/activation_drift/projection_stats.json` — 完整统计
- `raw_projections.json` — 每个样本的原始投影值
- `projection_histogram.pdf/png` — 4 panel 分布对比图
- `projection_scatter.png` — per-sample ckpt-4500 vs ckpt-5000 散点图

---
