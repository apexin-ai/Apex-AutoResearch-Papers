# Pi0.5 + A1 SDF 集成可行性报告

## Pi0.5 Training Pipeline 分析

- **Framework**: PyTorch（`/root/autodl-tmp/openpi/scripts/train_pytorch.py`）
- **Training loop**: `train_loop()` 函数，支持 DDP 多 GPU、gradient checkpointing、WandB
- **Loss 扩展性**: **完全可扩展** — 已有 `TrainHooks` 抽象类，支持 `on_model_created`、`extra_params`、`on_step_start`、`on_loss_computed`、`on_save_checkpoint`、`on_cleanup`。A1 的 `SdfAuxHooks` 正是通过此接口集成
- **LoRA 支持**: 有。`colliforce/lora_utils.py` 中 `inject_lora_pi0()` 对 PaliGemma + Action Expert 分别注入 LoRA，目标层为 `q_proj/k_proj/v_proj/o_proj/gate_proj/up_proj/down_proj`
- **中间特征暴露**: 有。`suffix_out` 形状 `[B, action_horizon, 1024]`，通过 `action_out_proj` 的 forward hook 捕获

## Pi0 vs Pi0.5 架构对比

| 特性 | Pi0 | Pi0.5 |
|------|-----|-------|
| 模型类 | `PI0Pytorch` (`pi05=False`) | `PI0Pytorch` (`pi05=True`) |
| PaliGemma | `gemma_2b` (width=2048) | 同 |
| Action Expert | `gemma_300m` (width=1024) | 同 |
| **action_out_proj** | `Linear(1024, action_dim)` | **同** |
| **suffix_out 维度** | `[B, 50, 1024]` | `[B, 10, 1024]`（LIBERO action_horizon=10） |
| Timestep 注入 | 拼接到 action embedding | **AdaRMSNorm** 条件注入 |
| State 输入 | suffix 中的 state_proj | 默认 discrete（LIBERO 用 continuous） |
| max_token_len | 48 | 200 |

**关键结论**: Pi0 和 Pi0.5 共用同一个 `PI0Pytorch` 类，Action Expert 结构完全一致（gemma_300m, width=1024）。`action_out_proj` 作为 SDF hook 的挂载点，在两者中完全相同。

## A1 SDF 集成路径

### 方案 A: 最快路径（推荐）

直接复用现有 `train_a1_sdf_aux.py`，仅修改 config：

```python
# 原 Pi0 config
model_config = Pi0Config(paligemma_variant="gemma_2b", action_expert_variant="gemma_300m")

# 改为 Pi0.5 config
model_config = Pi0Config(pi05=True, action_horizon=10, discrete_state_input=False)
```

加上权重路径改为 `pi05_libero`。**其余所有代码（SdfAuxHooks、SDFDecoder、EEExtractor、LoRA 注入）无需任何修改**。

理由：
- `action_out_proj` hook 挂载点完全相同
- `suffix_out` 最后维度 1024 不变 → SDFDecoder(feature_dim=1024) 直接兼容
- `inject_lora_pi0()` 目标路径 `paligemma_with_expert.paligemma.model.language_model` 和 `paligemma_with_expert.gemma_expert.model` 在 pi0.5 中不变
- AdaRMSNorm 影响的是 layernorm 层，不影响 LoRA 目标层（attention/FFN projections）

### 方案 B: 更干净的路径

新建 `train_a1_pi05_sdf_aux.py`，从 `train_a1_sdf_aux.py` fork，同时：
- 调整 action_horizon=10 对 mean pooling 的影响（50 token pooling vs 10 token pooling）
- 可选：重新调 lambda_sdf/lambda_ee 超参
- 可选：利用 pi0.5 更长的 max_token_len=200 做更丰富的 prompt

## 需要修改的文件

| 文件 | 修改内容 | 复杂度 | 风险 |
|------|---------|--------|------|
| `scripts/train_a1_sdf_aux.py` 中 `build_config()` | `Pi0Config(pi05=True, action_horizon=10, discrete_state_input=False)` | **低** | 无 |
| `scripts/train_a1_sdf_aux.py` 中 `WEIGHTS_BASE` | 权重路径指向 `pi05_libero` | **低** | 无 |
| `scripts/train_a1_sdf_aux.py` 中 `parse_args()` | 可选：调整默认超参（batch_size、lr、warmup_steps） | **低** | 需调参 |
| `colliforce/sdf_decoder.py` | **无需修改** | - | - |
| `colliforce/ee_extractor.py` | **无需修改** | - | - |
| `colliforce/lora_utils.py` | **无需修改** | - | - |
| `openpi/scripts/train_pytorch.py` | **无需修改** | - | - |

## 技术风险

1. **Mean pooling 行为变化（低风险）**: Pi0 的 suffix_out 是 50 个 token pooling 到 1 个 feature vector；Pi0.5 LIBERO 是 10 个 token。更少的 token 意味着 pooled feature 的信息密度不同。可能需要微调 lambda_sdf。

2. **Pi0.5 预训练权重质量（低风险）**: 已有 `pi05_libero` 权重在 westd-45947 上，TSR=98.2% 的 baseline 已验证。

3. **AdaRMSNorm 对 LoRA 的交互（极低风险）**: AdaRMS 修改的是 normalization 层的 scale/shift，不影响 attention/FFN 的 weight 矩阵。LoRA 注入仍然是对 `q_proj/k_proj/v_proj/o_proj/gate_proj/up_proj/down_proj` 做低秩分解，两者正交。

4. **observation.state 格式（低风险）**: Pi0.5 默认 discrete_state_input=True，但 LIBERO config 已显式设为 False。A1 的 `ee_gt = observation.state[:, :3].float()` 读取前 3 维作为 EE position，需确认 pi0.5 LIBERO 数据的 state 格式一致。

5. **显存压力（中风险）**: Pi0.5 的 max_token_len=200（vs Pi0 的 48），prefix 序列更长，显存占用可能增加。可能需要降低 batch_size 或启用 gradient_checkpointing。

## 预估工作量

| 项目 | 工时 |
|------|------|
| 代码修改（config 改动） | 0.5 worker-hours |
| Pi0.5 权重准备（已在 westd-45947，需同步到 westd-35807） | 0.5 worker-hours |
| 首次运行 + debug | 1-2 worker-hours |
| 超参搜索（lambda_sdf、lr、batch_size） | 2-3 worker-hours |
| 评估验证（rollout CAR/TSR） | 2-3 worker-hours |
| **总计** | **6-9 worker-hours** |

## 结论

**Go。** 集成工作量极小。Pi0 和 Pi0.5 共用同一模型类、同一训练框架、同一 hook 接口，Action Expert 维度完全一致。核心修改仅需改 3 行 config 代码。唯一需要实际验证的是超参调整和显存预算。
