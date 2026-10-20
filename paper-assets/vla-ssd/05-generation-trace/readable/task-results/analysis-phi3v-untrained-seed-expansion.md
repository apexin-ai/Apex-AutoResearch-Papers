# analysis phi3v untrained seed expansion

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_phi3v_untrained_seed_expansion_20260520T114811_result.json`
- **Structured JSON:** [`da9d4a33c93a2c05e961.json`](../../sessions/da/da9d4a33c93a2c05e961.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。实验状态已更新为 DONE/success。

## 结果摘要

**15-seed 合并后的 Phi3V untrained R² profile**:

| 指标 | 15-seed | 5-seed |
|------|---------|--------|
| peak_r2 | **0.578 ± 0.018 (L6)** | 0.583 ± 0.016 (L4) |
| mean_r2 (L1-L32) | 0.487 | ~0.490 |
| profile_shape | early_peak_monotonic_decline | same |
| late_layer_mean (L25-L32) | 0.392 | 0.452 |

**关键发现**: CI 没有收紧，反而增大了（avg std 0.035→0.068），主要因为新 seeds 暴露了 **late-layer 不稳定性**——L27-L32 有多个 seed 出现 R²≈-0.33（probe 完全失败）。5-seed 样本恰好避开了这些极端值，低估了真实方差。

**vs trained Phi3V**: untrained peak 0.578 (L6) → trained peak 0.634 (L11)，训练使 peak 右移 5 层、R² 提升 0.056，且稳定了 late-layer 表征。

**Verdict**: SUCCESS——2×2 矩阵最后一块拼图完成（15 seeds 对齐），profile shape 确认为 early_peak_monotonic_decline，late-layer instability 是有科学意义的新发现。

---
