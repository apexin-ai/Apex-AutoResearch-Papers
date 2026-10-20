# analysis phase2 tf ar switching

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_phase2_tf_ar_switching_20260525T220409_result.json`
- **Structured JSON:** [`36d9479f0beee83ebfbf.json`](../../sessions/36/36d9479f0beee83ebfbf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。总结：

**结论：INCONCLUSIVE (negative)**

实验执行正常（39 conversations，7 conditions，1059s），但**指标选择有问题**：

1. **指标不匹配**：`eval_switching.py` 测的是 raw mid-point GAR（单 token 对 goal positions 的原始注意力权重，范围 0.01-0.12），而非论文中的 normalized GAR（nGAR，TF≈0.50 / AR≈0.064）。两者差 1-2 个数量级。

2. **TF-AR 基线差异极小**：在 raw mid-point GAR 下，pure_tf 和 pure_ar 的差异 <1 SE（多数 turn t-stat<1），pure_ar 甚至略高于 pure_tf（方向与 nGAR 相反），完全没有可检测的 "drop"。

3. **方差压倒信号**：per-conversation CV 高达 89-100%，cross-condition 差异 ~0.01 被 within-condition std ~0.05-0.09 完全淹没。

4. **唯一正面发现**：pre-switch turns 完美匹配 pure_tf（偏差 <0.0001），验证了实验设计本身是正确的。

**对 paper 的建议**：不要用此实验支撑 C3。C3 的主要证据来自 SS 实验（gap 31×→1.3×, p<0.001）。如需 switching 证据，应改用 nGAR 或 PPL 作为指标重跑。

报告已写入 `artifacts/switching_analysis.md`，registry 已更新为 DONE/negative。

---
