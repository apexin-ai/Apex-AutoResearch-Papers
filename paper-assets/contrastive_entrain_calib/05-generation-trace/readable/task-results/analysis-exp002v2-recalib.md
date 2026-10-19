# analysis exp002v2 recalib

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp002v2-recalib_20260519T211555_result.json`
- **Structured JSON:** [`e7633f88039916e5280e.json`](../../sessions/e7/e7633f88039916e5280e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp002v2-recalib 分析报告

### 训练概况
- **总步数**: 501 → 4000（3500 步），step 4000 磁盘写满崩溃
- **Recalibration**: 每 500 步执行，共 7 次，机制本身工作正常

### Recalibration 效果

| Step | cos_sim | AUROC | d_norm |
|------|---------|-------|--------|
| 500 | 0.670 | 0.815 | 79.1 |
| 1000 | 0.860 | 0.855 | 91.1 |
| 2000 | 0.799 | 0.847 | 84.5 |
| 3000 | 0.936 | 0.903 | 120.6 |
| 3500 | 0.858 | 0.909 | 164.1 |

AUROC 从 0.82 提升到 0.91——方向质量确实在改善。但 d_norm 膨胀（79→164），且 R1 始终无法转正。

### 最终指标（step ~4000）
| 指标 | 值 | 判定 |
|------|-----|------|
| R1 mean | -0.12 | 全程负值 |
| R1_strong | -0.15 ~ -0.30 | 系统性深度负值 |
| R3 | 0.87-0.999 | 完全饱和 |
| Entropy | 0.057 | 严重 mode collapse |
| Completion length | 63 tokens (原 240) | 崩塌 |

### Conclusion: **NEGATIVE — mode collapse 确认**

符合 ROADMAP 预期。关键发现：**recalibration 能维持方向质量（AUROC 0.82→0.91），但无法修复 cosine R1 的结构性负值问题。** 信号质量不是瓶颈，cosine 投影公式本身是。

这是 Story A 第 4/4 个 negative result：
1. exp-002 (tanh): 饱和
2. exp-002v2 (cosine): d_syc drift
3. exp-002v3 (scaled×5): 放大负值
4. **exp002v2-recalib (periodic recalib): mode collapse, R1 仍负**

**Story A 证伪完成。** Checkpoint 在 `/root/contrastive_entrain_calib/checkpoints/exp002v2_dcgrpo_cosine/checkpoint-{500..3500}`（4000 可能损坏），可作为 negative evidence。已更新 memory.md。

---
