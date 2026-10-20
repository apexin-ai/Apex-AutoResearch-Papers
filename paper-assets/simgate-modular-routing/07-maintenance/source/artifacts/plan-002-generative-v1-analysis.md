# plan-002-generative-v1 训练结果分析

## 1. 训练概况

| 项目 | 值 |
|------|-----|
| 模型 | Qwen3-1.7B + LoRA (r=16, alpha=32, dropout=0.05) |
| 可训练参数 | 6,422,528 / 1,726,997,504 (0.37%) |
| 数据 | data/plan-004-implicit, 2040 samples base |
| 训练集 | 3120 samples (upsample internal 180→1560, 1:1 平衡) |
| 验证集 | 300 samples (internal=30, deterministic=270) |
| Epochs | 3, 总 steps=294 (98/epoch) |
| Effective batch | 32 (bs=4 × grad_accum=8) |
| lr | 2e-5, warmup=10%, cosine decay |
| 训练时长 | 286.25s (~4.77 min) |
| 吞吐 | 32.7 samples/s, 1.03 steps/s |
| 最终 train_loss (avg) | 0.8853 |

## 2. Loss 趋势

### Train Loss (每 10 steps 记录)

| Epoch | Loss | 趋势 |
|-------|------|------|
| 0.10 | 5.437 | 初始高 loss |
| 0.21 | 5.080 | |
| 0.31 | 4.253 | 快速下降 |
| 0.41 | 2.411 | |
| 0.51 | 1.200 | |
| 0.62 | 0.794 | |
| 0.72 | 0.600 | |
| 0.82 | 0.503 | |
| 0.92 | 0.412 | epoch 1 结束趋于平稳 |
| 1.02 | 0.312 | |
| 1.33 | 0.339 | epoch 2 在 0.27-0.34 波动 |
| 1.64 | 0.275 | |
| 1.94 | 0.227 | |
| 2.04 | 0.248 | epoch 3 在 0.20-0.25 波动 |
| 2.55 | 0.213 | |
| 2.86 | 0.199 | |
| 2.96 | 0.199 | 最终 loss |

**趋势判断**: Loss 单调下降，无发散或震荡。Epoch 1 快速收敛（5.4→0.3），Epoch 2-3 缓慢改善（0.3→0.2）。

### Eval Loss

| Epoch | eval_loss | 变化 |
|-------|-----------|------|
| 1.0 | 0.3915 | — |
| 2.0 | 0.2827 | -27.8% |
| 3.0 | 0.2599 | -8.1% |

**过拟合检查**: eval_loss 持续下降，无过拟合迹象。Train loss (最后10步均值 ~0.21) vs eval_loss (0.26) 差距合理。

## 3. Eval 指标

**⚠️ 关键问题：routing_acc / internal_recall / det_recall 未在训练中输出。**

原因：`generative_router_sft.py` 定义了 `make_eval_fn(tokenizer)` 函数（line 237），会计算 routing_acc、internal_recall、det_recall。但在 Trainer 初始化时（line ~420），**`compute_metrics` 参数未传入**，导致 HuggingFace Trainer 只输出默认的 eval_loss。

需要单独运行 eval 子命令获取路由指标（见第 7 节）。

## 4. Checkpoint 状态

| 路径 | 说明 |
|------|------|
| `checkpoints/plan-002-generative-v1/checkpoint-196/` | Epoch 2 checkpoint |
| `checkpoints/plan-002-generative-v1/checkpoint-294/` | Epoch 3 checkpoint |
| `checkpoints/plan-002-generative-v1/final_adapter/` | 最终 LoRA adapter |
| `checkpoints/plan-002-generative-v1/train_config.json` | 训练配置 |
| `checkpoints/plan-002-generative-v1/TRAINING_COMPLETE` | 完成标志 |

final_adapter 内容:
- `adapter_model.safetensors`: 25.7 MB
- `adapter_config.json`: 1 KB
- tokenizer 文件齐全

**状态**: 正常保存，load_best_model_at_end=True 生效（best model by eval_loss）。

## 5. 结论判断

**PENDING — 需要跑 eval 才能判断**

训练本身健康：
- Loss 收敛良好，无发散
- eval_loss 持续下降，无过拟合
- Checkpoint 完整保存
- internal_recall 未知（compute_metrics 未接入 Trainer）

**无法判定 success/negative**，因为核心指标 internal_recall 缺失。

## 6. 与 ablation-b 对比

| 指标 | ablation-b | plan-002-generative-v1 |
|------|-----------|----------------------|
| 方法 | implicit generative SFT | generative SFT (同方法改进版) |
| internal_recall | 51.5% | 未测 |
| 数据 | plan-004-implicit | plan-004-implicit (同) |
| upsample | yes | yes (ratio=1.0) |
| grad_accum | 未知 | 8 (effective bs=32) |
| epochs | 未知 | 3 |

对比需在 eval 后完成。

## 7. 需要额外跑的 eval

### 方法 1: 脚本内置 eval 子命令

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
cd /root/autodl-tmp/simgate-modular-routing && \
CUDA_VISIBLE_DEVICES=0 HF_HUB_OFFLINE=1 python src/training/generative_router_sft.py eval \
  --adapter_path checkpoints/plan-002-generative-v1/final_adapter \
  --model_name /root/autodl-tmp/models/Qwen/Qwen3-1.7B \
  --task_types "boil,melt,change-the-state-of-matter-of" \
  --max_variations 5 \
  --max_steps 30 \
  --gpu_id 0 \
  --output_dir results/plan-002-generative-v1/
```

注意：eval 子命令依赖 `ablation_eval_common.py`，需确认该文件存在且 ScienceWorld 环境可用。

### 方法 2: 修复 compute_metrics 后重新短训

在 Trainer 初始化中加入 `compute_metrics=make_eval_fn(tokenizer)`，可以快速验证 val set 上的 routing 指标（但这只是 val set 上的 token-level prediction，不等于实际游戏环境中的 routing 效果）。

### 建议

优先跑方法 1（实际环境 eval），这是与 ablation-b 对比的标准方式。

## 8. Bug 记录

**`compute_metrics` 未接入 Trainer**: `make_eval_fn()` 在 line 237 定义但未在 SamplerTrainer 初始化时传入。建议修复后续实验的训练脚本，在 Trainer kwargs 中加入 `compute_metrics=make_eval_fn(tokenizer)`。
