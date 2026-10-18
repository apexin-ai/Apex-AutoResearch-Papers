# ops deploy e3 xvla openvla westd27271

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_deploy_e3_xvla_openvla_westd27271_20260523T073129_result.json`
- **Structured JSON:** [`0338375cae745d09bb3a.json`](../../sessions/03/0338375cae745d09bb3a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个模型都成功了。结果汇总：

## E3 Token Cosine Similarity 结果

| Model | CV | #Tok | Mean CosSim | Std | Min | Max |
|-------|------|------|-------------|-------|--------|--------|
| **X-VLA** | 0.151 | 100 | **0.2510** | 0.3377 | -0.1094 | 0.9999 |
| **OpenVLA** | 0.215 | 256 | **0.2981** | 0.1824 | -0.0721 | 0.9776 |

结合已有数据的完整对比：

| Model | CV | Mean CosSim |
|-------|------|-------------|
| π0.5 | 0.055 | 0.9545 |
| X-VLA | 0.151 | 0.2510 |
| OpenVLA | 0.215 | 0.2981 |
| SmolVLA | 0.314 | 0.7224 |

注意：X-VLA 的 Mean CosSim (0.2510) 低于 OpenVLA (0.2981)，这与 CV 的单调递减趋势不一致（X-VLA CV 更低，预期 CosSim 应更高）。SmolVLA 的 CosSim (0.7224) 也不符合趋势。

可能原因：
1. X-VLA 的 `vlm_features` 包含了 vision + text tokens 混合（100 tokens = ~50 vision + 50 text），不纯粹是 vision tokens
2. 不同模型的 connector 架构差异很大（linear proj vs BART encoder vs MLP vs pix-shuffle），直接比较 post-connector tokens 的语义不完全等价

**输出文件：**
- X-VLA stats: `/root/autodl-tmp/importance_margin_vla_compress/artifacts/token_cosine_similarity_xvla_openvla.json`
- OpenVLA stats: `/root/autodl-tmp/importance_margin_vla_compress/artifacts/token_cosine_similarity_openvla.json`
- X-VLA matrices: `artifacts/token_cosine_similarity_matrices_xvla_openvla.npz`
- OpenVLA matrices: `artifacts/token_cosine_similarity_matrices_openvla.npz`

---
