# analysis threshold sensitivity

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_threshold-sensitivity_20260517T091255_result.json`
- **Structured JSON:** [`34d42a912a071318a2fb.json`](../../sessions/34/34d42a912a071318a2fb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。结果：

**τ_mag 敏感度呈阶梯形，非平滑曲线：**

| τ 范围 | TPR | FPR | J |
|--------|-----|-----|-------|
| 0.30–0.45 | 1.000 | 0.286 | 0.714 |
| 0.50–0.70 | 0.667 | 0.286 | 0.381 |

关键发现：
- **FPR 在整个 [0.30, 0.70] 范围内恒定为 0.286**（两个 FP 的 ve_ratio 分别为 0.7281 和 0.7499，均 > 0.70）
- **唯一断点在 τ≈0.497**：exp_008d_s3 的触发 ve_ratio=0.4969，τ≥0.50 即丢失该 TP
- **τ=0.49 是最优**：恰好卡在 0.4969 下方，是能达到 J=0.714 的最紧阈值
- 降低 τ 无收益（不会增加 TP 或减少 FP），magnitude threshold 无法单独消除 FP（需改进其他条件如时间持续性或加速度阈值）

---
