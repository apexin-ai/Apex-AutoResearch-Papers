# ops xvla token count check

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_xvla-token-count-check_20260520T045446_result.json`
- **Structured JSON:** [`b5fdf84af21f298f2853.json`](../../sessions/b5/b5fdf84af21f298f2853.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

从 X-VLA 的 `preprocessor_config.json` 和 `modeling_florence2.py` 直接得到结论：

### 1. 输入图像分辨率
**224×224**（X-VLA 自己的 preprocessor 设定，不是 Florence-2-Large 默认的 768×768）

### 2. Vision token 数量计算
DaViT 总空间下采样率 = 4×2×2×2 = **32×**
- 最终 feature map: 224/32 = 7 → **7×7 = 49 spatial tokens**

Feature 聚合方式（`image_feature_source: ["spatial_avg_pool", "temporal_avg_pool"]`）：
- `spatial_avg_pool`: 沿空间维度 pool → T 个 token（单帧 T=1 → **1 token**）
- `temporal_avg_pool`: 沿时间维度 pool → **49 tokens**（空间维度保留）
- 拼接后总计：**50 tokens**（与 `max_pos_embeddings: 50` 完全吻合）

### 3. 结论
**< 100 tokens（仅 ~50 个）**。VTC 在 X-VLA 上基本无意义——50 个 token 的序列压缩空间极其有限，收益可忽略不计。

如果要做 VTC 实验，应选用高 token 数的 VLA（如 OpenVLA 用 SigLIP 输出 256 tokens，或用 768×768 Florence-2 原始配置的 577 tokens）。

---
