# research smolvla base compatibility

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_smolvla_base_compatibility_20260516T234059_result.json`
- **Structured JSON:** [`a5c52afd70b228a73978.json`](../../sessions/a5/a5c52afd70b228a73978.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结论

**`lerobot/smolvla_base` 与我们当前代码完全兼容，且已经在使用中。**

### 模型结构（500 keys total）

| 模块 | Key prefix | 维度 |
|------|-----------|------|
| VLM backbone (SmolVLM2-500M, 16 layers) | `model.vlm_with_expert.vlm.model.*` | hidden=960 |
| Action expert (16 layers) | `model.vlm_with_expert.lm_expert.*` | hidden=720 (960×0.75) |
| State projection | `model.state_proj` | (960, 32) |
| Action in/out proj | `model.action_in_proj` / `action_out_proj` | (720, 32) / (32, 720) |
| Time MLPs | `model.action_time_mlp_*` | 720 |

### 兼容性验证

1. **Config 已指向 smolvla_base**: `baseline.yaml` 和所有 `libero_*.yaml` 的 `pretrained` 都是 `/root/autodl-tmp/.hf_cache/lerobot/smolvla_base`
2. **加载路径正确**: `SmolVLAPolicy.from_pretrained()` → `load_vlm_weights=False`(跳过 hub 下载）→ safetensors 加载全部 500 keys（包括 VLM backbone 344 keys）
3. **ACIS 维度匹配**: `visual_dim=960`（= VLM hidden）, `action_dim=720`（= expert hidden）✓
4. **LoRA targets 正确**: regex 匹配 `vlm_with_expert.lm_expert.*.{q,v}_proj` + projection layers ✓
5. **无 key 冲突**: ACIS 在 `IMMSmolVLAWrapper.acis.*` 下，完全在 SmolVLAPolicy 模型树外部
6. **`_adapt_projections` 处理维度适配**: 将 max_state/action_dim=32 适配到目标数据集（如 LIBERO 的 14）

### smolvla_base 相比直接用 SmolVLM2-500M-Video-Instruct 的增量

- **Pretrained action expert**: 在 40+ robotics 数据集上训练过的 expert head
- **Pretrained projection layers**: state/action/time projections
- **VLM backbone 相同**: 冻结状态，与 SmolVLM2-500M-Video-Instruct 一致

### 答案

**不需要任何适配工作。** train.py 的 model loader 已经能直接加载 `smolvla_base`，且目前所有实验配置已经在用它。零代码修改。

---
