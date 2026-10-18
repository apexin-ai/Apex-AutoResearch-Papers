# code openvla reencoding adapt

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_openvla_reencoding_adapt_20260519T162506_result.json`
- **Structured JSON:** [`4eb13791fe7bca468600.json`](../../sessions/4e/4eb13791fe7bca468600.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。产出文件：

| 文件 | 用途 |
|------|------|
| `artifacts/openvla_vtc_adapter.py` | VTC 适配模块：`VisionTokenCompressor` (4096 dim, 16 heads)、`OpenVLAActionTokenizer` (256-bin 离散化)、`OpenVLASmartCompressWrapper` |
| `artifacts/train_openvla_smart_compress.py` | 训练脚本：加载 OpenVLA 7B + VTC，冻结 backbone，LIBERO 数据 + cross-entropy loss |
| `artifacts/eval_openvla_smart_compress.py` | 评估脚本：LIBERO 仿真 rollout，per-task 成功率 + Wilson CI |
| `artifacts/configs/openvla_smart_compress_m32.yaml` | M=32 配置 (87.5% 压缩: 256→32) |

**关键适配设计：**

1. **维度变化**：hidden_dim 960→4096, num_heads 12→16, vision tokens 128→256/camera
2. **动作范式**：SmolVLA 的 flow matching (MSE) → OpenVLA 的 autoregressive (cross-entropy on discretized action tokens)
3. **无 action expert**：OpenVLA 用标准 LM head 生成动作 token，所以只训练 VTC（SmolVLA 额外训练 expert+projections）
4. **输入构建**：`_build_compressed_inputs` 在 input_ids 中找到 image placeholder tokens，替换为 M 个 compressed embeddings，同步调整 attention_mask 和 labels
5. **多相机支持**：每个相机单独过 vision backbone → 拼接 → 压缩（如 2 cameras: 512→M）
6. **Action tokenizer**：支持 per-dim min/max normalization，自动检测 OpenVLA vocabulary 中的 action token 起始 ID

---
