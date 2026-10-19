# 7B 模型验证 — 调研与准备报告

**日期**: 2026-05-19  
**目标**: 在 Qwen3-8B 上复现 Cell A (step-independent h=2) vs Cell C (episode-level) 对比实验

---

## 1. 显存可行性分析

### 实际 GPU 规格（与预期不同）

| 服务器 | 预期 | 实际 | 显存/卡 |
|--------|------|------|---------|
| westd-47453 | 4x A800 80GB | 4x NVIDIA RTX PRO 6000 Blackwell | **96GB** |
| bjb1-17606 | 2x A6000 48GB | 2x NVIDIA RTX PRO 6000 Blackwell | **96GB** |

两台都是 96GB，远超预期。7B/8B 训练无显存瓶颈。

### Qwen3-8B VRAM 需求估算

模型参数: 8B, bf16 权重: ~16.4GB

**westd (4x 96GB, FSDP 4-way, optimizer_offload=True)**:

| 组件 | 每卡占用 |
|------|----------|
| 参数 (bf16 sharded) | ~4.1GB |
| 梯度 (bf16 sharded) | ~4.1GB |
| 优化器状态 | 0 (CPU offload) |
| 激活值 (micro_bs=1, seq=20480) | ~10-15GB |
| **训练总计** | **~20-25GB** |
| 剩余 | **~70GB** |

vLLM Rollout (交替使用，训练时释放):
- 模型加载: ~16.4GB
- gpu_memory_utilization=0.5 → ~48GB 总预算 → ~30GB KV cache
- **非常充裕**

**bjb1 (2x 96GB, FSDP 2-way, optimizer_offload=True)**:

| 组件 | 每卡占用 |
|------|----------|
| 参数 (bf16 sharded) | ~8.2GB |
| 梯度 (bf16 sharded) | ~8.2GB |
| 优化器状态 | 0 (CPU offload) |
| 激活值 | ~10-15GB |
| **训练总计** | **~28-33GB** |
| 剩余 | **~63GB** |

**结论: 两台服务器均可轻松运行 8B 训练，不需要 gradient checkpointing。westd 作为主训练节点（4卡更快），bjb1 可作为备份或并行跑不同 seed。**

### 磁盘空间

| 服务器 | 总量 | 已用 | 可用 |
|--------|------|------|------|
| westd | 250GB | 124GB | **127GB** |
| bjb1 | 250GB | 144GB | **107GB** |

Qwen3-8B 下载需 ~16.4GB，两台均充足。但 westd 上有大量 ray/wandb 临时文件可清理。

---

## 2. 模型选择建议

### 推荐: `Qwen/Qwen3-8B`

| 选项 | 参数量 | 优劣 |
|------|--------|------|
| **Qwen/Qwen3-8B** | 8B | 同 Qwen3 家族（与 1.7B 一致），已内置指令跟随能力，无需单独 Instruct 版本 |
| Qwen/Qwen2.5-7B-Instruct | 7B | 老一代，与 1.7B 实验不同家族，不利于 model-agnostic claim |
| Qwen/Qwen3-8B-Base | 8B | 纯预训练，无指令跟随，不适合零样本 eval |

**关键信息**:
- Qwen3 系列没有独立的 `-Instruct` 后缀版本（与 Qwen2.5 不同）
- `Qwen/Qwen3-8B` 本身即为指令调优版本，支持 thinking/non-thinking 双模式
- `Qwen/Qwen3-8B-Base` 才是纯预训练版本
- 架构: `Qwen3ForCausalLM`，与 1.7B SFT 模型完全一致
- HuggingFace 模型 ID: `Qwen/Qwen3-8B`
- 大小: ~16.4GB (bf16, safetensors)

### 下载命令（待执行）

```bash
# 在 westd-47453 上
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
huggingface-cli download Qwen/Qwen3-8B --local-dir /root/autodl-tmp/models/Qwen3-8B

# 如果 huggingface-cli 不可用:
python -c "from transformers import AutoModelForCausalLM, AutoTokenizer; \
    AutoTokenizer.from_pretrained('Qwen/Qwen3-8B', cache_dir='/root/autodl-tmp/models/Qwen3-8B'); \
    AutoModelForCausalLM.from_pretrained('Qwen/Qwen3-8B', cache_dir='/root/autodl-tmp/models/Qwen3-8B')"
```

---

## 3. Config 改造要点

### 当前 1.7B Config 核心参数（两个 config 相同部分）

```yaml
model_path: /root/autodl-tmp/checkpoints/qwen3_exp021_ragen_sft_v4  # 1.7B SFT
system.CUDA_VISIBLE_DEVICES: "0,1"
n_gpus_per_node: 2
micro_batch_size_per_gpu: 1
ppo_mini_batch_size: 16
ppo_max_token_len_per_gpu: 65536
gpu_memory_utilization: 0.35
max_model_len: 20480
max_num_batched_tokens: 20480
fsdp_config.optimizer_offload: True
train.env_groups: 16, group_size: 8  # 128 rollout samples
val.env_groups: 32, group_size: 1    # 32 eval episodes
```

### 7B Config 改动（Cell A, westd 4卡）

```yaml
# === 必须改 ===
model_path: /root/autodl-tmp/checkpoints/qwen3_8b_sft_v1  # 8B SFT 后的路径（或 /root/autodl-tmp/models/Qwen3-8B 做零样本）
experiment_name: 7b-cellA-h2
system.CUDA_VISIBLE_DEVICES: "0,1,2,3"
n_gpus_per_node: 4
local_log_dir: "/root/autodl-tmp/checkpoints/7b-cellA-h2/"
default_local_dir: "/root/autodl-tmp/checkpoints/7b-cellA-h2/"

# === 建议改 ===
gpu_memory_utilization: 0.45          # 96GB 卡可提高（1.7B 用 0.35 因为显存紧张）
ppo_mini_batch_size: 32               # 4卡可适当增大（从 16 到 32）
val.env_groups: 32                    # 保持 ≥16 episodes（C003 约束）

# === 保持不变 ===
micro_batch_size_per_gpu: 1           # 安全起步
ppo_max_token_len_per_gpu: 65536      # 充足
max_model_len: 20480                  # 充足
context_window_mode: "step_independent"
step_independent_history_length: 2
optimizer_offload: True               # 保险起见保留
```

### 7B Config 改动（Cell C, westd 4卡）

与 Cell A 完全一致，仅改:
```yaml
experiment_name: 7b-cellC-episode-level
context_window_mode: "full"
local_log_dir: "/root/autodl-tmp/checkpoints/7b-cellC-episode/"
default_local_dir: "/root/autodl-tmp/checkpoints/7b-cellC-episode/"
```

### 关注点
- `attn_implementation: sdpa` — Qwen3-8B 支持，保持不变
- `response_length: 1024` — 单步 response 长度，保持不变
- `max_prompt_length: 16384` — 保持不变
- 不需要 gradient_checkpointing（96GB 充裕）
- 不需要 tensor_model_parallel（8B 单卡可放下）

---

## 4. SFT 需求评估

### 当前 1.7B SFT 情况
- 基座: `Qwen/Qwen3-1.7B`
- SFT 数据: `/root/autodl-tmp/expert_sft/expert_sft_train.jsonl` (2460 examples, **仅在 bjb1 上**)
- SFT 脚本: `/root/autodl-tmp/cost-verify-agent-rl/scripts/sft_train.py` (TRL SFTTrainer)
- SFT 输出: `/root/autodl-tmp/checkpoints/qwen3_exp021_ragen_sft_v4/` (3.3GB)
- 配置: 3 epochs, lr=2e-5, batch=4, grad_accum=4, max_seq=4096

### 8B SFT 建议

**推荐路线: 先零样本 eval → 再 SFT → 再 RL**

1. **零样本 eval**（优先做）:
   - 直接用 `Qwen/Qwen3-8B` 在 ALFWorld 上跑 eval（32 episodes）
   - 目的: 了解 8B 基座在 ALFWorld 上的裸能力
   - 如果零样本成功率 > 30%，可以考虑直接跳过 SFT 做 RL（减少变量）
   - 如果零样本成功率 < 10%，必须 SFT

2. **SFT**（大概率需要）:
   - 复用 1.7B 的 SFT 数据（从 bjb1 同步到 westd）
   - 改 `sft_train.py` 的 `MODEL_PATH` 为 Qwen3-8B
   - 4 卡 FSDP SFT:
     ```bash
     torchrun --nproc_per_node=4 scripts/sft_train.py \
       --data_path /root/autodl-tmp/expert_sft/expert_sft_train.jsonl \
       --output_dir /root/autodl-tmp/checkpoints/qwen3_8b_sft_v1 \
       --num_train_epochs 3 \
       --per_device_train_batch_size 2 \
       --gradient_accumulation_steps 4 \
       --learning_rate 1e-5 \
       --max_seq_length 4096
     ```
   - 注意: 8B SFT 可能需要降低 lr (1e-5 vs 2e-5)，避免 catastrophic forgetting
   - 需要检查 `sft_train.py` 是否支持多卡 DDP/FSDP（当前脚本写的单卡）

3. **为什么不跳过 SFT 直接 RL**:
   - 1.7B 实验从 SFT checkpoint 出发，公平对比要求 8B 也从 SFT 出发
   - 论文需要展示 model-agnostic，控制变量要一致

---

## 5. 下一步行动计划

### Phase 1: 模型下载 + 数据同步 (预计 30 min)

```bash
# [westd] 下载 Qwen3-8B
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
pip install -U huggingface_hub  # 确保 hf CLI 可用
huggingface-cli download Qwen/Qwen3-8B --local-dir /root/autodl-tmp/models/Qwen3-8B

# [bjb1 → westd] 同步 SFT 数据
# 从 bjb1 拉取数据到 westd（需确认两台机器间网络连通方式）
# 方案 A: 如果 bjb1 可从 westd SSH
scp root@bjb1:/root/autodl-tmp/expert_sft/expert_sft_train.jsonl /root/autodl-tmp/expert_sft/
# 方案 B: 通过本地中转
# 方案 C: 重新在 westd 上生成 SFT 数据（如果 expert trajectory 生成脚本可用）
```

### Phase 2: 零样本 Eval (预计 1h)

```bash
# [westd] 用 Qwen3-8B 直接跑 ALFWorld eval
cd /root/autodl-tmp/cost-verify-agent-rl/RAGEN
CUDA_VISIBLE_DEVICES=0,1,2,3 python train.py \
  --config-name _alfworld_7b_zeroshot_eval \
  # 需创建一个 eval-only config:
  # model_path: /root/autodl-tmp/models/Qwen3-8B
  # total_training_steps: 0
  # val_before_train: True
```

### Phase 3: SFT (预计 2-4h)

```bash
# [westd] 修改 sft_train.py 支持 8B + 多卡
# 然后:
CUDA_VISIBLE_DEVICES=0,1,2,3 torchrun --nproc_per_node=4 scripts/sft_train.py \
  --data_path /root/autodl-tmp/expert_sft/expert_sft_train.jsonl \
  --output_dir /root/autodl-tmp/checkpoints/qwen3_8b_sft_v1 \
  --num_train_epochs 3 --learning_rate 1e-5 --max_seq_length 4096
```

### Phase 4: RL 训练 — Cell A vs Cell C (预计各 8-12h)

```bash
# [westd] Cell A: step-independent h=2
CUDA_VISIBLE_DEVICES=0,1,2,3 python train.py --config-name _alfworld_7b_cellA_h2

# [westd 或 bjb1] Cell C: episode-level (可在另一台并行跑)
CUDA_VISIBLE_DEVICES=0,1 python train.py --config-name _alfworld_7b_cellC_episode
```

### 待确认事项
1. bjb1 → westd 文件传输方式（两台是否直连？）
2. `sft_train.py` 是否需要改造支持多卡 FSDP（当前是单卡 TRL）
3. 8B 零样本 eval 是否需要调整 chat template（Qwen3 thinking mode 可能需要 `/no_think` 控制）
4. westd 上 ray 临时文件是否可以清理释放空间

---

## 附录: 现有 Config 文件对比

| 参数 | Cell A (hsweep_h2) | Cell C (exp029) |
|------|-------------------|-----------------|
| context_window_mode | step_independent | full |
| step_independent_history_length | 2 | 2 (unused) |
| experiment_name | hsweep-h2 | exp029-alfworld-episode-level |
| total_training_steps | 15 | 100 |
| **其余参数完全一致** | | |
