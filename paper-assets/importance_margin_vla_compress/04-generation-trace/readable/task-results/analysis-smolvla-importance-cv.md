# analysis smolvla importance cv

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_smolvla-importance-cv_20260520T085613_result.json`
- **Structured JSON:** [`ea827b6bad43877cfd7e.json`](../../sessions/ea/ea827b6bad43877cfd7e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

**SmolVLA Token Importance CV = 0.314** (±0.015)，Gini = 0.156。

### D103 Connector Spectrum 完整对比

| Model | Connector | CV | Gini | Entropy | Compressible? |
|-------|-----------|------|------|---------|--------------|
| π0 | MLP (frozen) | 0.038 | 0.009 | 0.9999 | No |
| **SmolVLA** | **Pixel-shuffle** | **0.314** | **0.156** | **0.952** | **Yes** |
| OpenVLA | 2L MLP (trained) | 0.215 | N/A | 0.661 | Yes |

### 结论

1. **CV 是区分 connector 可压缩性的有效指标**：compressible connectors (SmolVLA 0.314, OpenVLA 0.215) vs non-compressible (π0 0.038)，阈值约 CV > 0.1 即可分离。

2. **Entropy 单独不行**：SmolVLA entropy = 0.952 接近 π0 的 0.9999，但 SmolVLA 可压缩。Entropy 只在 OpenVLA (0.661) 上明显偏低。

3. **CV 比 entropy 是更好的 compressibility predictor**。复合指标（entropy + CV）不增加区分力，CV 单独即可。SmolVLA 的 CV 甚至高于 OpenVLA，与其 pixel-shuffle connector 产生更大的空间局部性差异一致。

---
