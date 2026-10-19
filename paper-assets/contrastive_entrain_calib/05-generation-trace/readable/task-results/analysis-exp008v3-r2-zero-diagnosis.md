# analysis exp008v3 r2 zero diagnosis

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp008v3-r2-zero-diagnosis_20260519T141808_result.json`
- **Structured JSON:** [`5e3f2d826b454fc0fbcb.json`](../../sessions/5e/5e3f2d826b454fc0fbcb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**r2_mean=0 是预期行为，不是 bug。**

训练脚本 `run_exp008v3_binary_probe_grpo.py` 中明确设置：

```python
R1_WEIGHT = 0.25  # Binary probe reward
R2_WEIGHT = 0.0   # 显式禁用
R3_WEIGHT = 0.75  # NLI behavioral reward
```

这是 ablation cascade 设计的一部分。exp-008v3 的实验目的是用 Binary Probe 替代 Directional Projection 作为 R1，同时**故意关闭 R2**（方向投影 reward），只保留 R1(probe) + R3(NLI)。

日志确认训练正常运行：
- **R1** 在 {0.0, 0.125, 0.25, 0.375} 间波动（binary probe 的离散输出 × 0.25 weight，符合预期）
- **R2** 恒为 0.0000（weight=0，无影响）
- **R3** 在 0.33~0.99 间正常变化
- **combined** 正常，约 0.25~0.75 范围

无需干预。

---
