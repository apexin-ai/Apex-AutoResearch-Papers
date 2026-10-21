# code method section draft

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_method_section_draft_20260520T202102_result.json`
- **Structured JSON:** [`e85f4e4f042fadd6d361.json`](../../sessions/e8/e85f4e4f042fadd6d361.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Method Section 初稿已写入 `/root/colliforce-vla/docs/method_draft.md`（119 行）。

关键内容对照代码的准确性总结：

| 项目 | 代码实际值 | 文稿中 |
|------|-----------|--------|
| SDF Decoder | 4-layer MLP, hidden=256, Softplus(β=5), skip at layer 2 | ✓ |
| SDF loss | Clamped L1 (δ=0.05) + Eikonal (λ=0.1) | ✓ |
| EE Extractor | Linear(1024,256)→ReLU→Linear(256,3) | ✓ |
| Query points per step | N=64 | ✓ |
| Refiner α/margin/grad_clip | 0.1 / 0.01 / 1.0 | ✓ |
| LoRA ranks | PaliGemma=16, Expert=32 | ✓ |
| Target modules | q/k/v/o_proj + gate/up/down_proj | ✓ |
| Phase 1 warmup | 5000 steps, backbone frozen | ✓ |
| Loss weights | λ_SDF=0.1, λ_EE=0.01, λ_refine=0.1 | ✓ |
| Inference refinement | L2-normalized spatial gradient on action[:3] | ✓ |
| Refinement loss | MSE(v_t, sg(v_t_refined)) on near-collision samples | ✓ |

---
