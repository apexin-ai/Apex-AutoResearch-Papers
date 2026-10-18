# code e3 token cosine similarity

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_e3_token_cosine_similarity_20260523T054900_result.json`
- **Structured JSON:** [`ceff6fb1aee148e9a415.json`](../../sessions/ce/ceff6fb1aee148e9a415.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本已写入 westd-41074 服务器（568 行）。

## 设计思路与 Hook 位置总结

**每个模型的 post-connector token 提取方式：**

| 模型 | Hook 位置 | 提取方法 | 实际 token 数 |
|------|-----------|----------|--------------|
| **π0** | `paligemma.model.multi_modal_projector` | 直接调用 vision_tower → projector → ×√d | 256 (1 cam) |
| **π0.5** | `paligemma.model.multi_modal_projector` | 同上，2 个 camera 分别处理后 concat | 512 (2×256) |
| **X-VLA** | `model.forward_vlm()["vlm_features"]` | 调 `_build_model_inputs` + `forward_vlm`，取返回的 vlm_features | ~50 |
| **OpenVLA** | `vla.projector` output | 直接调 `vla.vision_backbone(pixels)` → `vla.projector(patches)` | 256 |
| **OFT** | `vla.projector` output | 两张图分别过 vision_backbone，concat 后过 projector | 512 (2×256) |
| **SmolVLA** | `connector` module (forward hook) | Hook connector + 调 `prepare_images` 触发 forward pass | 128 (2×64) |

**注意事项：**
- π0.5 理论 768 tokens (3 image slots)，但 LIBERO 只有 2 cameras，实际提取 512
- π0、X-VLA、OFT 模型不在 westd-41074 上，脚本会自动 skip（需在对应服务器运行）
- 支持 `--models pi05,openvla,smolvla` 参数选择性运行
- 输出：heatmap PDF/PNG + stats JSON + 原始矩阵 NPZ，均保存在 `artifacts/`

---
