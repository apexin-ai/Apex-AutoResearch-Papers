# exp-008 SFT Probe Penalty 调查报告

## 1. SFT 脚本路径与完整配置

**路径**: `/root/contrastive_entrain_calib/training/run_exp008_binary_probe_penalty.py`

### 核心确认：这是真正的 SFT 脚本

- **Loss**: `L = L_sft + λ_reward × λ_probe × S(t) - λ_reward × R3`
  - L_sft = cross-entropy on last-assistant-turn tokens (标准 SFT loss)
  - S(t) = frozen logistic probe score，通过 hidden states 可微分
  - R3 = NLI reward (precomputed，常数，仅 monitoring)
- **训练框架**: 自定义 training loop (非 GRPO/trl)
- **无 generation**: 不生成 completions，直接在 gold responses 上计算 SFT loss

### 当前配置

| 参数 | 值 |
|------|-----|
| Model | Qwen3-8B (`/root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B`) |
| Data | `calibration_v2_1_expanded.jsonl` (362 samples) |
| LoRA rank | 64 |
| LoRA alpha | **128** |
| LoRA targets | **7 modules**: q/k/v/o/gate/up/down_proj |
| LoRA dropout | 0.05 |
| lr | 5e-5 |
| warmup | 200 steps |
| max_steps | **8000** |
| batch_size | 1 |
| grad_accum | 16 (effective bs=16) |
| max_seq_len | 1024 |
| save_steps | 500 |
| gradient_checkpointing | True |
| bf16 | True |
| seed | 42 (argparse 已支持 `--seed`) |
| λ_reward | 0.1 |
| λ_probe | 1.0 |
| reward_layers | [19, 20, 24, 27, 32, 33, 35] |
| probe retrain | 每 500 steps |
| max_grad_norm | 1.0 |

### Probe 机制

- Probe 是 frozen logistic regression (权重不更新)
- 但 hidden states → probe → S(t) 路径是可微的 → 梯度流回模型
- 每 500 steps retrain probe (在全部 362 samples 上重新拟合)
- 这意味着模型有动机"欺骗" probe (probe reward trap 的核心机制)

### Stop-gradient 分析

- Probe 权重 frozen: `probe.eval()`, `requires_grad=False` on probe params
- 但模型 hidden states **不** 被 detach → 梯度通过 probe 流回模型
- 这正是 probe reward trap 的条件：模型学习操纵自身 representations 来降低 S(t)

---

## 2. 与 GRPO exp-008v3 配置差异对照表

| 配置项 | exp-008 (SFT) | exp-008v3 (GRPO) |
|--------|---------------|------------------|
| 训练方式 | SFT loss + probe penalty | GRPO generation + reward |
| Loss | L_sft + λ×S(t) | GRPO policy gradient |
| Probe 使用方式 | **可微 penalty** (梯度流回模型) | **binary reward** (0/1, 不可微) |
| LoRA alpha | **128** | **64** |
| LoRA modules | **7** (q/k/v/o/gate/up/down) | **4** (q/k/v/o) |
| Generation | 无 | 2 completions/sample, 256 tokens |
| Framework | 自定义 loop | DCGRPOTrainer (trl) |
| Reward weights | λ_reward=0.1, λ_probe=1.0 | R1=0.25(probe), R3=0.75(NLI) |
| max_steps | 8000 | 8000 |
| save_steps | 500 | 500 |
| Seed 参数化 | ✓ (argparse --seed) | ✗ (全局常量 SEED=42) |

**关键差异**: SFT 版本的 probe 是可微的（梯度直接优化模型降低 S(t)），GRPO 版本的 probe 只作为 binary reward signal。SFT 版本更容易触发 probe reward trap，因为优化信号更直接。

---

## 3. 需要的修改

### 3.1 已满足
- [x] Seed 参数化：argparse 已支持 `--seed`

### 3.2 需通过命令行参数覆盖
- [ ] `--max_steps 2000` (默认 8000)

### 3.3 需修改脚本代码
- [ ] LoRA alpha: 128 → **64** (匹配 GRPO 配置以公平对比)
- [ ] LoRA targets: 7 modules → **4 modules** (`["q_proj", "v_proj", "k_proj", "o_proj"]`)

修改位置 (`run_exp008_binary_probe_penalty.py`, TrainConfig class):
```python
# 修改前
lora_alpha: int = 128
lora_targets: list[str] = field(
    default_factory=lambda: ["q_proj", "v_proj", "k_proj", "o_proj", "gate_proj", "up_proj", "down_proj"]
)

# 修改后
lora_alpha: int = 64
lora_targets: list[str] = field(
    default_factory=lambda: ["q_proj", "v_proj", "k_proj", "o_proj"]
)
```

也需要在 argparse 中添加 `--lora_alpha` 和 `--lora_targets` 参数，或直接改默认值。

---

## 4. 建议的训练命令

### 单次运行
```bash
CUDA_VISIBLE_DEVICES=0 HF_HOME=/root/autodl-tmp/.hf_cache \
python /root/contrastive_entrain_calib/training/run_exp008_binary_probe_penalty.py \
    --seed 42 --max_steps 2000
```

### Multi-seed wrapper
```bash
#!/bin/bash
set -e
export CUDA_VISIBLE_DEVICES=0
export HF_HOME=/root/autodl-tmp/.hf_cache
cd /root/contrastive_entrain_calib/training

for SEED in 42 43 44; do
    echo "===== exp-008 SFT seed=$SEED ====="
    python run_exp008_binary_probe_penalty.py \
        --seed $SEED \
        --max_steps 2000 \
        --output_dir /root/contrastive_entrain_calib/checkpoints/exp008_sft_seed${SEED}
    echo "===== Completed seed=$SEED ====="
done
```

### 时间预估
- SFT 无 generation，显著快于 GRPO
- 每 step: ~5-8s (forward + backward + probe eval)
- 2000 steps: **~3-4.5 小时/seed**
- 3 seeds 串行: **~9-14 小时**

---

## 5. GPU 进程状态

| PID | 脚本 | 状态 |
|-----|------|------|
| 553700 | `run_exp003_len512_r3only.py` | **运行中** (自 May 23，已跑 ~21h) |

**无 exp008 相关进程在运行。** GPU 上跑的是 exp003 (R3-only baseline)，不是 exp008v3 GRPO。

---

## 6. 附加发现

- `run_exp008_gs8_ablation.py` 也在服务器上，是 exp-008 的 group_size=8 变体 (batch=8, grad_accum=2)
- exp008 checkpoint 目录不存在 → 从未执行过
- exp008v3 GRPO 脚本 **不在服务器上**（仅本地 artifacts 有）

## 7. 下一步行动建议

1. 修改 `run_exp008_binary_probe_penalty.py`: alpha=64, 4 modules
2. 等 exp003 完成（或用 GPU:1 并行）后启动 exp008 multi-seed
3. 无需 kill 任何进程
