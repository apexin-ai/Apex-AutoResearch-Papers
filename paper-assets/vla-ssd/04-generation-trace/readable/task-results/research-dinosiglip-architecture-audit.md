# research dinosiglip architecture audit

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_dinosiglip-architecture-audit_20260516T023757_result.json`
- **Structured JSON:** [`4ad28bfdc7ef03fa931c.json`](../../sessions/4a/4ad28bfdc7ef03fa931c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。报告已保存到 `/root/autodl-tmp/vla-ssd/results/architecture_audit/dinosiglip_audit.md`。

核心发现：

**`extract_siglip_features.py` 提取的是 DINOv2+SigLIP fused backbone + projector 的输出，不是纯 SigLIP。**

证据链：
1. `config.json`: `use_fused_vision_backbone: true`, `timm_model_ids` 包含 DINOv2 ViT-L 和 SigLIP ViT-SO400M
2. `PrismaticVisionBackbone.forward()`: 将 6-channel 输入拆分，分别过 DINOv2 和 SigLIP，然后 **`torch.cat` 沿 embed_dim 拼接** → (B, 256, 2176)
3. `PrismaticProjector`: 接收 2176 维 fused input → 3层 MLP → 4096 维输出，DINOv2 和 SigLIP 信息完全混合
4. `extract_siglip_features.py`: 直接调用 `model.vision_backbone(pixel_values)` + `model.projector()`，整个流程没有任何步骤分离纯 SigLIP

**影响**: RSA=0.615 ("SigLIP+Projector") vs RSA=0.388 (standalone DINOv2) 的对比存在两个混淆：(1) "SigLIP"侧包含 DINOv2 信息；(2) "SigLIP"侧有 trained projector 而 DINOv2 侧没有。

---
