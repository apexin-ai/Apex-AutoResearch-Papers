# ops stability measurement step500

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_stability-measurement-step500_20260519T062320_result.json`
- **Structured JSON:** [`4826b38f6c96876b4397.json`](../../sessions/48/4826b38f6c96876b4397.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果如下：

## exp-002v2 checkpoint-500 方向稳定性报告

| Layer | cosine(old,new) | dot AUROC | cos AUROC | \|\|h\|\| mean | \|\|h\|\| std | new \|\|d\|\| |
|-------|----------------|-----------|-----------|------------|-----------|-----------|
| 19 | 0.2782 | 0.7894 | 0.8013 | 104.7 | 2.0 | 5.59 |
| 20 | 0.3067 | 0.7906 | 0.7988 | 115.5 | 2.7 | 8.19 |
| 24 | 0.3533 | 0.7775 | 0.7869 | 260.4 | 7.0 | 26.78 |
| 27 | 0.3809 | 0.8212 | 0.8238 | 407.8 | 9.1 | 55.27 |
| 32 | 0.2395 | 0.8100 | 0.8081 | 839.2 | 17.9 | 105.60 |
| 33 | 0.2208 | 0.8169 | 0.8162 | 988.4 | 20.6 | 111.36 |
| 35 | 0.2005 | 0.8400 | 0.8400 | 1008.5 | 73.0 | 143.04 |

### Summary
- **Mean cosine(old, new): 0.2828**
- **Mean cosine AUROC: 0.8107**
- **Verdict: SIGNIFICANT_DRIFT** (< 0.5)

### 关键发现

1. **方向大幅漂移**：所有层的 cosine similarity 都在 0.20-0.38 范围，远低于 0.8 稳定阈值。深层（32, 33, 35）漂移最严重（cosine ~0.20-0.24）。

2. **但区分能力保持良好**：尽管方向漂移严重，AUROC 全部在 0.78-0.84 范围，说明重新计算的方向仍然能有效区分 valid/invalid。原始方向的区分能力通过 dot product 和 cosine 投影都保持在合理水平。

3. **Activation norms 深层爆炸**：从 layer 19 的 104.7 增长到 layer 35 的 1008.5（近 10x），layer 35 的 std 也高达 73.0，说明深层激活值分布变化剧烈。

4. **建议重新校准 d_syc**：方向在训练 500 步后已经显著旋转，需要用当前 checkpoint 重新提取 directions。AUROC 良好说明重校准后应该能恢复/提升性能。

---
