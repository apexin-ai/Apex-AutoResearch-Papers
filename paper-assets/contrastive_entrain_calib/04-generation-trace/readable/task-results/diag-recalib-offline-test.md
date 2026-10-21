# diag recalib offline test

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_recalib-offline-test_20260518T230408_result.json`
- **Structured JSON:** [`f0e263ab96d33f23587d.json`](../../sessions/f0/f0e263ab96d33f23587d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完整结果如下：

**Per-Layer Analysis:**

| Layer | Cosine | OldNorm | NewNorm |
|-------|--------|---------|---------|
| 19 | 0.9069 | 1.0000 | 3.9438 |
| 20 | 0.8803 | 1.0000 | 5.4734 |
| 24 | 0.8786 | 1.0000 | 17.0951 |
| 27 | 0.8798 | 1.0000 | 36.4849 |
| 32 | 0.8247 | 1.0000 | 66.9615 |
| 33 | 0.8203 | 1.0000 | 70.9664 |
| 35 | 0.7507 | 1.0000 | 84.2601 |

**Summary:**
- **Mean cosine(old, new): 0.8487**
- AUROC (original d_syc): **0.7771**
- AUROC (recalibrated d_syc): **0.7964**
- AUROC delta: **+0.0194**

**解读：**

整体方向稳定（mean cosine 0.85 > 0.8 阈值），recalibration 不紧迫。但有两个值得注意的趋势：

1. **深层 drift 更大**：浅层 (19-27) cosine 0.88-0.91，深层 (32-35) 降到 0.75-0.82。Layer 35 的 0.7507 已接近中度漂移区间。
2. **NewNorm 急剧增长**：从 layer 19 的 3.9 到 layer 35 的 84.3，说明 LoRA 训练后深层的 valid/invalid 激活差异被显著放大。
3. **AUROC 仍可用**：原始 d_syc 的 AUROC 0.777 > 0.7 阈值，判别力尚存。Recalibrated 仅提升 +0.019，增益不大。

**结论**：当前 step-500 的 d_syc 漂移尚在可控范围，R1 震荡的主因可能不是方向漂移。但如果训练继续推进到 step 700+，深层 drift 可能加剧，建议届时再测一次。

---
