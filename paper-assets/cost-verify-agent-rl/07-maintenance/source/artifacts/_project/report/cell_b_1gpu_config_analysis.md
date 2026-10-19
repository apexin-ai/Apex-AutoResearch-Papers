# Cell B 1-GPU 等效配置分析

## 1. 原始配置关键参数

| 参数 | 值 | 来源 |
|------|-----|------|
| `system.CUDA_VISIBLE_DEVICES` | `"0,1"` | cell B config |
| `trainer.n_gpus_per_node` | `2` | cell B config |
| `micro_batch_size_per_gpu` | `1` | cell B config |
| `ppo_mini_batch_size` | `16` | cell B config |
| `es_manager.train.env_groups` | `16` | cell B config |
| `es_manager.train.group_size` | `8` (GRPO K) | cell B config |
| `total_training_steps` | `15` | cell B config |
| `test_freq` | `5` | cell B config |
| `save_freq` | `5` | cell B config |
| `lr` | `1e-6` | cell B config |
| `kl_loss_coef` | `0.01` | cell B config |
| `kl_loss_type` | `low_var_kl` | cell B config |
| `entropy_coeff` | `0.001` | cell B config |
| `clip_ratio_low / high` | `0.2 / 0.28` | cell B config |
| `advantage_mode` | `"episode_level"` | cell B config |
| `adv_estimator` | `grpo` | cell B config |
| `context_window_mode` | `"step_independent"` | cell B config |
| `step_independent_history_length` | `2` | cell B config |
| `optimizer_offload` | `True` | cell B config |
| `use_dynamic_bsz` | `False` (default) | actor config default |
| `ppo_max_token_len_per_gpu` | `65536` | cell B config (unused when dynamic_bsz=False) |
| `model` | Qwen3-4B (bf16, ~8GB) | checkpoint config.json |
| `val.env_groups` | `134` (OOD) | cell B config |

## 2. Effective Batch Size 计算

RAGEN 的 batch 由环境采样决定，不受 GPU 数量影响：

```
训练样本数/step = env_groups × group_size = 16 × 8 = 128 episodes
```

PPO 更新流程（dp_actor.py）：
- `mini_batches = data.split(ppo_mini_batch_size=16)` → 128/16 = **8 mini-batches**
- 每个 mini-batch 内: `gradient_accumulation = ppo_mini_batch_size / ppo_micro_batch_size_per_gpu = 16 / 1 = 16`
- FSDP 在多 GPU 间分片 mini-batch 并 all-reduce 梯度 → **有效梯度与 GPU 数无关**

**结论：2 GPU → 1 GPU 不改变 effective batch size。** FSDP 仅影响并行速度，不影响梯度等效性。

已有先例验证：`_alfworld_hsweep_h10_1gpu.yaml` 从 2 GPU 切 1 GPU，只改了 `CUDA_VISIBLE_DEVICES` 和 `n_gpus_per_node`，其余参数（`ppo_mini_batch_size`、`env_groups`、`group_size`）完全不变。

## 3. GRPO K=8 是否受 GPU 数影响

**不受影响。** `group_size: 8` 在 `es_manager` 层面控制每个 prompt 生成 8 个 rollout response。这发生在 vLLM 推理引擎中（`tensor_model_parallel_size: 1`），与训练 GPU 数解耦。

## 4. 1-GPU 等效配置（需修改的参数）

| 参数 | 原值 (2 GPU) | 新值 (1 GPU) | 理由 |
|------|-------------|-------------|------|
| `system.CUDA_VISIBLE_DEVICES` | `"0,1"` | `"0"` | 仅用 cuda:0 |
| `trainer.n_gpus_per_node` | `2` | `1` | 单 GPU |
| `trainer.test_freq` | `5` | `999` | 关闭中间 validation |
| `trainer.experiment_name` | `factorial-h2-episode-adv` | `cell-b-1gpu-seed{N}` | 区分实验 |

**所有其他参数保持不变**，包括 `ppo_mini_batch_size`、`env_groups`、`group_size`、`lr`、`kl_loss_coef` 等。

## 5. 是否需要创建新 config 文件

**推荐创建新文件**，原因：
- Hydra 支持命令行 override，但修改项较少且需要长期复用
- 新文件更清晰，便于 wandb 追溯

也可通过 Hydra 命令行 override 实现（不创建文件）：
```bash
python train.py --config-name _alfworld_factorial_h2_episode_adv \
  system.CUDA_VISIBLE_DEVICES='"0"' \
  trainer.n_gpus_per_node=1 \
  trainer.test_freq=999 \
  trainer.experiment_name=cell-b-1gpu-seed1
```

## 6. 启动命令模板

```bash
#!/bin/bash
rm -rf /tmp/fast_downward_* /tmp/ray/* /tmp/tmp* 2>/dev/null
source /root/miniconda3/etc/profile.d/conda.sh
conda activate base
cd /root/cost-verify-agent-rl/RAGEN
export WANDB_PROJECT=cost-verify-agent-rl
export CUDA_VISIBLE_DEVICES=0

python train.py --config-name _alfworld_cell_b_1gpu \
  trainer.experiment_name=cell-b-1gpu-seed1 \
  seed.train=10000
```

注意：RAGEN 使用 `python train.py`（不是 torchrun），内部通过 Ray 管理 GPU worker。`n_gpus_per_node` 在 config 中指定，不需要 `torchrun --nproc_per_node`。

## 7. 关闭中间 Validation 的方法

训练循环逻辑（`agent_trainer.py`）：
```python
if self.config.trainer.test_freq > 0 and (is_last_step or self.global_steps % self.config.trainer.test_freq == 0):
    val_metrics = self._validate()
```

- 设 `test_freq: 999`（大于 `total_training_steps=15`）→ 中间步不触发 validation
- `is_last_step` 条件保证最后一步仍做 validation
- `val_before_train: True` 保留 → 训练前做一次 baseline validation
- **最终效果：仅 step 0（before train）和 step 15（last step）做 validation**

每次 validation = 134 OOD episodes × 1 rollout，省略中间 2 次可节省约 20-40 分钟。

## 8. 训练时长预估

- **GPU**: NVIDIA RTX PRO 6000 Blackwell (98GB VRAM)，单卡足以容纳 Qwen3-4B 全量训练
- **模型**: ~8GB (bf16) + optimizer states (offloaded to CPU)
- **vLLM**: `gpu_memory_utilization: 0.35` → ~34GB for rollout KV cache

时间估算（基于类似配置的 h-sweep 实验）：
- 每步 rollout（128 episodes × 50 max turns）: ~15-25 min（瓶颈在 ALFWorld 环境交互 + vLLM 推理）
- 每步训练（PPO update on 1 GPU）: ~2-5 min
- Validation（134 episodes）: ~10-20 min
- **15 steps 无中间 val**: ~(15 × 25) + 2 × 15 = **~6-7 小时**
- **含中间 val（test_freq=5）**: 额外 +2 次 val ≈ +30 min

**1 GPU vs 2 GPU 时间差**：训练阶段 ~2x 慢，但 rollout 阶段（主要瓶颈）不受影响（vLLM 始终单卡 `tensor_model_parallel_size=1`）。总体慢 ~10-20%。

## 9. 内存可行性

| 组件 | 估算 VRAM |
|------|----------|
| 模型权重 (bf16) | ~8 GB |
| 梯度 (bf16) | ~8 GB |
| Optimizer states | CPU offloaded |
| vLLM KV cache (0.35) | ~34 GB |
| 激活值 + 临时 | ~10-15 GB |
| **总计** | **~60-65 GB / 98 GB** |

内存充裕，无 OOM 风险。
