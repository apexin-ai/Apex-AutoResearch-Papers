# exp-008v3 Multi-Seed 复现准备报告

## 1. 脚本状态

| 文件 | 服务器路径 | 状态 |
|------|-----------|------|
| `run_exp008v3_binary_probe_grpo.py` | `/root/contrastive_entrain_calib/training/` | **不存在** (仅本地 artifacts 有) |
| `probe_module.py` | `/root/contrastive_entrain_calib/training/` | **不存在** (仅本地 artifacts 有) |
| `dcgrpo_trainer.py` | `/root/mvp_v2_1_expanded/training/` | 存在 |

**需要上传**: `run_exp008v3_binary_probe_grpo.py` + `probe_module.py`

## 2. 数据/模型路径确认

| 资源 | 路径 | 状态 |
|------|------|------|
| Qwen3-8B | `/root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B` | OK (16GB) |
| 训练数据 | `/root/mvp_v2_1_expanded/data/calibration_v2_1_expanded.jsonl` | OK (362条) |
| NLI model | `cross-encoder/nli-deberta-v3-base` (HF cache) | OK |
| Activations | `/root/contrastive_entrain_calib/results/exp001/activations.pt` | OK |
| Directions | `/root/contrastive_entrain_calib/results/exp001/directions.pt` | OK |

## 3. 原始配置提取

```
Framework:     DCGRPOTrainer (继承 trl.GRPOTrainer)
LoRA:          r=64, alpha=64, targets=["q_proj","v_proj","k_proj","o_proj"], bias="none"
lr:            5e-5
warmup:        200 steps
batch_size:    1 (per device)
grad_accum:    16 (effective bs=16)
max_steps:     8000
save_steps:    500
num_gen:       2 (GRPO generations per sample)
max_comp_len:  256 tokens
bf16:          True
grad_ckpt:     True
Reward:        R1=0.25 (binary probe), R2=0.0, R3=0.75 (NLI)
Probe retrain: every 500 steps (on all 362 samples)
Seed:          42 (hardcoded as global constant)
```

**与 exp-008 (SFT) 的关键区别**:
- exp-008v3 用 GRPO + probe 作为 R1 reward signal (0/1 binary)
- exp-008 用 SFT loss + probe penalty (differentiable through hidden states)
- exp-008v3: LoRA alpha=64, 4 modules | exp-008: alpha=128, 7 modules

## 4. 单 GPU 可行性评估

**结论: 完全可行，无需 DeepSpeed**

| 因素 | 原始 (westd-28034) | 当前 (westd-29046) |
|------|-------------------|-------------------|
| GPU | 2x ??? (~80GB total) | 2x RTX PRO 6000 Blackwell (98GB each) |
| 框架 | DeepSpeed ZeRO-2 | 不需要，单卡 98GB 足够 |

显存估算 (单卡 cuda:0):
- Qwen3-8B bf16: ~16GB
- LoRA adapter: ~0.5GB
- GRPO generation buffer (2 seq * 256 tokens): ~2GB
- Gradient + optimizer states (LoRA only): ~2GB
- Gradient checkpointing activation cache: ~5-10GB
- NLI model (DeBERTa-base): ~0.5GB
- **Total peak: ~30-40GB << 98GB available**

DCGRPOTrainer 通过 Accelerate 运行，无 DeepSpeed 硬依赖。只需 `CUDA_VISIBLE_DEVICES=0` 限制到单卡。

## 5. 需要的修改

### 5.1 参数化 Seed + 输出目录
原始脚本 SEED 是全局常量。修改为接受命令行参数：
```python
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--seed", type=int, default=42)
parser.add_argument("--max_steps", type=int, default=2000)
parser.add_argument("--output_dir", type=str, default=None)
args = parser.parse_args()

SEED = args.seed
MAX_STEPS = args.max_steps
OUTPUT_DIR = args.output_dir or f"/root/autodl-tmp/checkpoints/exp008v3_seed{SEED}"
```

### 5.2 max_steps 调整
8000 → 2000 (用户要求)

### 5.3 save_steps 确认
已经是 500，满足 500/1000/1500/2000 四个 checkpoint 的需求。

### 5.4 确保完整模型保存
原始 `trainer.save_model()` 保存 LoRA adapter。eval 时通过 `PeftModel.from_pretrained(base_model, adapter_path)` 加载即可。

## 6. 建议实验命令

### Wrapper 脚本 (`run_multiseed_exp008v3.sh`)
```bash
#!/bin/bash
set -e

export CUDA_VISIBLE_DEVICES=0
export HF_HOME=/root/autodl-tmp/.hf_cache

cd /root/contrastive_entrain_calib/training

for SEED in 43 44 45; do
    echo "===== Starting exp-008v3 seed=$SEED ====="
    python run_exp008v3_binary_probe_grpo.py \
        --seed $SEED \
        --max_steps 2000 \
        --output_dir /root/autodl-tmp/checkpoints/exp008v3_seed${SEED}
    echo "===== Completed seed=$SEED ====="
done
```

### 单独运行 (测试用)
```bash
CUDA_VISIBLE_DEVICES=0 HF_HOME=/root/autodl-tmp/.hf_cache \
python /root/contrastive_entrain_calib/training/run_exp008v3_binary_probe_grpo.py \
    --seed 43 --max_steps 2000 \
    --output_dir /root/autodl-tmp/checkpoints/exp008v3_seed43
```

## 7. 训练时间预估

GRPO 瓶颈在 generation (每 step = 16 samples * 2 completions * 256 tokens):
- RTX PRO 6000 Blackwell generate 速度: ~300-500 tok/s (8B, bf16, no vLLM)
- 每 optimizer step: ~32 completions * 256 tokens / 400 tok/s ≈ 20s generation + ~10s fwd/bwd + ~5s probe/reward
- **估计 ~30-45 秒/step**
- **2000 steps: ~17-25 小时/seed**
- **3 seeds 串行: ~50-75 小时总计**

如果需要加速: 可以用 2 GPU 并行跑不同 seed (CUDA_VISIBLE_DEVICES=0 和 =1 各跑一个)。

## 8. 准备清单

- [ ] 上传 `run_exp008v3_binary_probe_grpo.py` 到 `/root/contrastive_entrain_calib/training/`
- [ ] 上传 `probe_module.py` 到 `/root/contrastive_entrain_calib/training/`
- [ ] 修改脚本添加 argparse (seed, max_steps, output_dir)
- [ ] 创建 wrapper 脚本 `run_multiseed_exp008v3.sh`
- [ ] 先跑 50 步验证单 GPU 可行性 + 估计实际 step 耗时
- [ ] 启动 3-seed 实验
