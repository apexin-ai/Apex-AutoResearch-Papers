# results catalog westd 35807

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_results-catalog_westd-35807_20260529T050549_result.json`
- **Structured JSON:** [`5521b3255ffe8086b907.json`](../../sessions/55/5521b3255ffe8086b907.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计文件已写入 `artifacts/eval_results_audit_20260529.md`。

**汇总**：

- **57 个 eval JSON 文件**：56 个在 `/root/autodl-tmp/eval_results/`，1 个在 `/root/colliforce-vla/eval_results/`
- **覆盖范围**：
  - **Object suite (safelibero_object)**: 53 个文件，4 tasks (orange_juice, chocolate_pudding, milk, bbq_sauce)
  - **Spatial suite (safelibero_spatial)**: 4 个文件，4 tasks (bowl variants)
- **模型类型**：lora_baseline (LoRA), baseline (full-ft/pretrained pi05), a3 (gradient refine), pi05_libero (pretrained)
- **lambda 变体**：l0 (no SDF), l005 (λ=0.005), l01 (λ=0.01), l1 (λ=0.1)
- **训练种子**：seed0, seed1, seed2
- **评估种子**：seed 0/1/2/3/7/42/99/123
- **Collision threshold**: 统一 0.001
- **37 个训练/eval 日志**在 `logs/`
- **16 个 checkpoint 子目录**跨 object_pudding 和 spatial_bowl

所有 per-task TSR/CAR/smoothness/max_displacement/max_ee_displacement 指标已完整记录在审计文件中，可用于论文数字对账。

---
