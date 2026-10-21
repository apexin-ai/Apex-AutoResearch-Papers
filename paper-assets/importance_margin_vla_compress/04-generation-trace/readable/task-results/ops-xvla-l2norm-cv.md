# ops xvla l2norm cv

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_xvla-l2norm-cv_20260520T102821_result.json`
- **Structured JSON:** [`dc18a5e758860143a030.json`](../../sessions/dc/dc18a5e758860143a030.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

**X-VLA L2 Norm CV = 0.1509**

完整对比表（D104 diagnostic composite）：

| Model | Connector | Entropy | L2 Norm CV | Pruning Effect |
|-------|-----------|---------|------------|----------------|
| π0 | Linear projection | 0.9999 | **0.038** | Immune |
| **X-VLA** | **Linear proj + BART encoder** | **0.614** | **0.151** | **Near-immune** |
| OpenVLA | MLP projector | 0.661 | **0.215** | Graded |
| SmolVLA | Pixel-shuffle | 0.952 | **0.314** | Catastrophic |

关键发现：

- X-VLA CV=0.151 介于 π0 (0.038) 和 OpenVLA (0.215) 之间，**不像预期那样接近 π0**
- 原因：虽然 X-VLA 的 connector 是 linear projection，但 `vlm_features` 还经过了 Florence-2 BART encoder（12 层 transformer），这额外引入了非线性，提升了 token 间异质性
- 这与 pruning 实验一致：X-VLA k=0.3 normalized loss=1.0014（仅 0.14% 退化），仍属 near-immune
- Aux visual tokens CV=1.414 是因为 150 个 token 中有大量 zero-padded（min=0.0），不适合直接对比

结论：X-VLA 作为第 4 个数据点支持 CV 作为 compressibility predictor 的趋势，但也揭示了 connector 之后的处理层（如 BART encoder）会提升 CV，需要在论文中注明 "CV reflects the full projection pipeline, not the connector alone"。

---
