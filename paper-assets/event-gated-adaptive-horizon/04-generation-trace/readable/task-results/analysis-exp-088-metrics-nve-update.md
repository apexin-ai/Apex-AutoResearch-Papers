# analysis exp 088 metrics nve update

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_088_metrics_nve_update_20260525T210814_result.json`
- **Structured JSON:** [`08c86fb006e98775ea47.json`](../../sessions/08/08c86fb006e98775ea47.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。汇总：

**任务 1 — exp_088 指标提取 & registry 更新**:
- eval_return: best=final=309.3@105K (vs baseline 446.1)
- ve_ratio_peak=0.31@45K, civo_alert=0 全程
- NVE_peak=1.82@35K（早期瞬态，baseline ve_ratio 分母极低导致），NVE_final=0.09
- gate_dt=2.0 constant（gate 未激活）
- checkpoint_path / log_path 已设置

**任务 2 — NVE 分析更新**:
- N=62→63, Healthy=37→38
- exp_088 是 θ=1.5× 的新 FP（NVE_peak=1.82 来自 step 35K 的低绝对值噪声比）
- Method A θ=1.5×: AUROC 0.989→0.986, F1 0.926→0.909, FP 4→5
- Method A θ=2.0× 不受影响（NVE=1.82 < 2.0）
- Method B 不受影响（ve_ratio_peak=0.31 远低于所有阈值）
- 新增第 7 节讨论早期瞬态 NVE spike 的局限性及缓解策略

---
