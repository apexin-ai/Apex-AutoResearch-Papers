# code par router train v3

**Meta-Brain: Perturbation-Diagnostic Routing of LoRA Experts for Parameter-E cient VLA Robustness** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_par_router_train_v3_20260516T225031_result.json`
- **Structured JSON:** [`7b5ba3f955ae7c97176c.json`](../../sessions/7b/7b5ba3f955ae7c97176c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果总结

**V3 Router 训练失败：5-Fold CV Macro F1 = 0.5003 ± 0.0043**（远低于 Phase 0 的 0.9963）

### 根因分析

| 维度 | Phase 0 | V3 |
|------|---------|-----|
| Activation norm | ~250 | ~57000 (230x) |
| Hook 路径 | `paligemma.language_model.layers.6` | `paligemma.model.language_model.layers.6` |
| 扰动方式 | LIBERO 仿真（camera/lighting/layout/robot pose） | 合成增强（亮度噪声/色块/state噪声） |
| Within-class std | — | ~19300 |
| Between-class centroid dist | — | 1025-7680 |
| SNR | 高 | <0.4（类严重重叠） |

**核心问题**：v3 的合成扰动太弱，PaliGemma 对这些扰动鲁棒（这实际上说明模型泛化好），layer 6 representation 无法区分三类。

### 产出
- Router checkpoint（最佳可能）：`/root/meta_brain_lora_routing/checkpoints/phase1/par_router_v3/best_router.pt`
- 分析报告：已注册 artifact

### 建议方案（三选一）
1. **用 Phase 0 方法重新采集 activation**（LIBERO 仿真 rollout + 真实环境扰动）
2. **加强扰动强度**（使 activation 产生可区分的模式）
3. **直接使用 Phase 0 router**，确认 hook 路径在推理 pipeline 中可对齐

---
