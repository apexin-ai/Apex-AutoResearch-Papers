# code pi05 a1 dryrun validation

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_pi05_a1_dryrun_validation_20260522T230723_result.json`
- **Structured JSON:** [`9d34f302719cf8de3cc9.json`](../../sessions/9d/9d34f302719cf8de3cc9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

spatial_bowl 已有完整 q01/q99。汇报结果。

---

## Pi0.5 + A1 SDF Dry-run 验证报告

### 1. 验证清单

| 项目 | 状态 | 数据 |
|------|------|------|
| Pi0.5 权重加载 | **通过** | missing=0, unexpected=0 |
| LoRA 注入 | **通过** | Phase 1 LoRA params=0 (冻结) |
| SDF decoder hook | **通过** | sdf_decoder.pt 已保存到 checkpoint |
| EE extractor | **通过** | ee_extractor.pt 已保存，输出 3D (mlp.2: [3, 256]) |
| suffix_out 维度 | **通过** | 输入 feature_dim=1024，SDF decoder feature_proj: [256, 1024] |
| Loss 无 NaN | **通过** | step1=0.1769, step2=0.1207 |
| 2 步训练完成 | **通过** | aux_metadata: phase=1, global_step=2 |

### 2. Trainable params
- **Phase 1**: 658,948（仅 SDF decoder + EE extractor）
- **LoRA params**: 0（Phase 1 冻结，符合预期）

### 3. Loss 值
- Step 1 total loss: **0.1769**
- Step 2 total loss: **0.1207** (best)
- 未单独拆分 action/sdf/ee loss（tqdm 只显示总 loss，logging 被 tqdm 覆盖）

### 4. GPU 显存
- batch_size=4: **~9.4 GB**（模型 ~8 GB + 激活/梯度 ~1.4 GB）
- 估计 batch_size=32: **~19 GB**（线性外推）
- RTX PRO 6000 98 GB: **完全可行**，余量充裕

### 5. 发现的问题及修复

| 问题 | 修复 | 影响范围 |
|------|------|---------|
| Pi0.5 权重为 OCDBT/JAX 格式，缺 `model.safetensors` | 用 `convert_jax_model_to_pytorch.py` 转换（6.8GB） | westd-45947 |
| norm_stats 缺少 q01/q99（Pi0.5 需要 quantile norm） | object_pudding: 用 mean±2.326*std 近似；spatial_bowl: 已由其他进程补充 | westd-45947 |
| LoRA dtype 不匹配（float32 input vs BFloat16 weight） | `lora_utils.py` 修改 `self.base(x)` → `self.base(x.to(self.base.weight.dtype))` | **两台服务器均已修复** |

### 6. norm_stats 兼容性
- Pi0.5 用 `use_quantile_norm=True`（`model_type != PI0`），需要 q01/q99
- Pi0 用 `use_quantile_norm=False`，只需 mean/std
- object_pudding 的 q01/q99 目前是正态近似值，正式训练前建议从数据重新计算

---
