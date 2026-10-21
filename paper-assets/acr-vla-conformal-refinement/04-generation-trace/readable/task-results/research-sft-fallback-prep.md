# research sft fallback prep

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_sft-fallback-prep_20260513T152057_result.json`
- **Structured JSON:** [`f0e9a243cb27a1a94a7e.json`](../../sessions/f0/f0e9a243cb27a1a94a7e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

当前服务器只有 1 GPU。数据集信息已确认。现在编写最终产出。

---

## 调研结果

### 1. 数据集可用性 ✅

`lerobot/libero` 数据集可直接加载：
- 1693 episodes, 273,465 frames, 10 fps
- `observation.images.image` / `image2`：256×256 视频 (av1)
- `observation.state`：8 维
- `action`：7 维
- 需要 `rename_map` 将 `image`→`camera1`, `image2`→`camera2` 映射到 SmolVLA 的期望键名

### 2. LoRA 原生支持 ✅

LeRobot 0.5.1 已内置 PEFT/LoRA 支持，**无需任何代码修改**：
- `TrainPipelineConfig.peft: PeftConfig` 字段
- SmolVLA 默认 LoRA targets：expert 层的 q/v projections + state/action projections
  ```
  (model\.vlm_with_expert\.lm_expert\..*\.(q|v)_proj|model\.(state_proj|action_in_proj|action_out_proj|action_time_mlp_in|action_time_mlp_out))
  ```
- 配置接口：`--peft.method_type=LORA --peft.r=16`

### 3. 已知 Bug

`lerobot-train` 启动时 Groot policy 的 dataclass 在 Python 3.12 上崩溃。**已在 bjb2-40593 上修复**（lazy import patch）。4-GPU 服务器也需要同样的 patch：

```python
# 写入 /root/miniconda3/lib/python3.12/site-packages/lerobot/policies/groot/__init__.py
from .configuration_groot import GrootConfig
from .processor_groot import make_groot_pre_post_processors

def __getattr__(name):
    if name == "GrootPolicy":
        from .modeling_groot import GrootPolicy
        return GrootPolicy
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

__all__ = ["GrootConfig", "GrootPolicy", "make_groot_pre_post_processors"]
```

### 4. VRAM 与训练时间估算

模型大小：864.7 MB (fp16), ~432M params

| 配置 | 可训练参数 | 单卡 VRAM (bs=8) | 4 卡 VRAM (bs=8/卡) |
|------|-----------|-----------------|-------------------|
| LoRA r=16 | ~0.5-1M (~0.2%) | ~6-10 GB | ~6-10 GB/卡 |
| LoRA r=32 | ~1-2M (~0.4%) | ~7-11 GB | ~7-11 GB/卡 |
| 全参数微调 | 432M (100%) | ~10-14 GB | ~10-14 GB/卡 |

4090 24GB 完全够用。LoRA 可以尝试 batch_size=16/卡。

训练时间（25K steps）：
- 单卡：~3-5 小时
- 4 卡 DDP：~1.5-3 小时

### 5. 社区模型参考配置

`lerobot/smolvla_libero` 的原始训练：
- base: `lerobot/smolvla_base`, dataset: `lerobot/libero`
- **全参数微调**（freeze_vision_encoder=false, train_expert_only=false, peft=None）
- batch_size=32, steps=25000, lr=1e-4
- CosineDecay warmup=1000, decay=25000

### 6. LoRA SFT 训练命令

**单卡（当前 bjb2-40593 服务器）：**

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
source /etc/network_turbo
export HF_HOME=/root/autodl-tmp/.hf_cache
export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt
export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt

lerobot-train \
  --policy.type=smolvla \
  --policy.pretrained_path=lerobot/smolvla_base \
  --dataset.repo_id=lerobot/libero \
  --rename_map='{"observation.images.image":"observation.images.camera1","observation.images.image2":"observation.images.camera2"}' \
  --batch_size=16 \
  --steps=25000 \
  --save_freq=5000 \
  --eval_freq=0 \
  --log_freq=100 \
  --num_workers=4 \
  --seed=1000 \
  --policy.scheduler_decay_steps=25000 \
  --policy.push_to_hub=false \
  --peft.method_type=LORA \
  --peft.r=16 \
  --wandb.enable=true \
  --wandb.project=acr-vla-conformal \
  --wandb.entity=null \
  --job_name=smolvla_libero_lora_r16 \
  --output_dir=/root/autodl-tmp/outputs/smolvla_libero_lora_r16
```

**4 卡 DDP（autodl-4090x4 服务器）：**

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
source /etc/network_turbo
export HF_HOME=/root/autodl-tmp/.hf_cache
export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt
export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt

accelerate launch --num_processes=4 \
  -m lerobot.scripts.lerobot_train \
  --policy.type=smolvla \
  --policy.pretrained_path=lerobot/smolvla_base \
  --dataset.repo_id=lerobot/libero \
  --rename_map='{"observation.images.image":"observation.images.camera1","observation.images.image2":"observation.images.camera2"}' \
  --batch_size=32 \
  --steps=25000 \
  --save_freq=5000 \
  --eval_freq=0 \
  --log_freq=100 \
  --num_workers=4 \
  --seed=1000 \
  --policy.scheduler_decay_steps=25000 \
  --policy.push_to_hub=false \
  --peft.method_type=LORA \
  --peft.r=16 \
  --wandb.enable=true \
  --wandb.project=acr-vla-conformal \
  --wandb.entity=null \
  --job_name=smolvla_libero_lora_r16 \
  --output_dir=/root/autodl-tmp/outputs/smolvla_libero_lora_r16
```

> 注意：`batch_size` 是总 batch size（accelerate 自动分配到各 GPU）。4 卡时 batch_size=32 → 8/卡。

**如果想用更高 rank 或全参数微调做对比：**

```bash
# LoRA r=32
--peft.r=32

# 全参数微调（去掉 --peft.* 参数，加上）
--policy.freeze_vision_encoder=false \
--policy.train_expert_only=false
```

### 7. 注意事项

- `--rename_map` 的 dict 格式需要用单引号包裹，避免 shell 转义
- 首次运行会自动下载 `lerobot/libero` 数据集和 `lerobot/smolvla_base` 权重，确保 `network_turbo` 已启用
- 当前 bjb2-40593 只有 1× 4090，4 卡训练需要在 bjb1 服务器上执行
- 两台服务器都需要 Groot lazy import patch

---
