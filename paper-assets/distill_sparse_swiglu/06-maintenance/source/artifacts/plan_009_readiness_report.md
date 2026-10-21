# Plan 009: Mistral-7B 泛化验证 — 预备检查报告

**日期**: 2026-05-15

## 1. 模型可用性

**状态: 就绪**

- 路径: `/root/autodl-tmp/models/mistral-7b/`
- 大小: 14GB (3 shard safetensors)
- 版本: Mistral-7B-v0.3 (`MistralForCausalLM`, vocab_size=32768)
- 文件完整: config.json, tokenizer, 3x safetensors shards 均在

## 2. 架构对比

| 属性 | LLaMA-3.1-8B | Mistral-7B-v0.3 |
|------|-------------|-----------------|
| hidden_size | 4096 | 4096 |
| intermediate_size | 14336 | 14336 |
| num_hidden_layers | 32 | 32 |
| num_attention_heads | 32 | 32 |
| num_key_value_heads | 8 (GQA) | 8 (GQA) |
| hidden_act | silu (SwiGLU) | silu (SwiGLU) |
| vocab_size | 128256 | 32768 |
| sliding_window | N/A | null (disabled) |

MLP 维度完全一致。SwiGLU 结构相同 (gate_proj + up_proj + down_proj)。

## 3. 代码兼容性

**结论: 无需修改代码，只需传 `--model_name_or_path` 参数。**

逐文件分析:

| 文件 | 兼容性 | 说明 |
|------|--------|------|
| `src/predictor.py` | ✅ 完全兼容 | PredictorWrapper 通过 `model.model.layers[i].mlp` 访问 MLP，Mistral 结构一致。`config.hidden_size/intermediate_size/num_hidden_layers` 均存在 |
| `src/train.py` | ✅ 完全兼容 | 用 `AutoModelForCausalLM` 自动加载。默认路径 hardcode 为 llama，通过 `--model_name_or_path /root/autodl-tmp/models/mistral-7b` 覆盖 |
| `src/evaluate.py` | ✅ 完全兼容 | 同 train.py，传参即可 |
| `src/baselines.py` | ✅ 完全兼容 | 通过 `model.model.layers` 遍历，访问 `mlp.gate_proj/up_proj/down_proj`，Mistral 接口一致 |
| `src/data_utils.py` | ✅ 完全兼容 | 纯数据加载，无模型依赖 |
| `src/losses.py` | ✅ 完全兼容 | 纯损失函数，无模型依赖 |

原因: HuggingFace 的 `MistralForCausalLM` 内部结构从 `LlamaForCausalLM` 派生，MLP 层接口完全相同。

## 4. 磁盘空间

| 分区 | 总量 | 已用 | 可用 |
|------|------|------|------|
| / (根) | 30G | 16G | 15G |
| /root/autodl-tmp (数据盘) | 250G | 39G | 212G |

Mistral-7B 已占用 14GB（在数据盘），无需额外空间。训练 checkpoint 约 100MB，空间充足。

## 5. 启动 Plan 009 所需步骤

1. **训练命令** (无需代码改动):
   ```bash
   python src/train.py \
     --model_name_or_path /root/autodl-tmp/models/mistral-7b \
     --loss_type kl \
     --num_steps 1000 \
     --gpu 0 \
     --output_dir /root/distill_sparse_swiglu/checkpoints/mistral_kl_s42 \
     --wandb_run_name mistral_kl_s42
   ```

2. **评估命令**:
   ```bash
   python src/evaluate.py \
     --model_name_or_path /root/autodl-tmp/models/mistral-7b \
     --checkpoint checkpoints/mistral_kl_s42/predictor_kl.pt \
     --gpu 1 \
     --baseline_mode teal_vanilla,wina,rsparse
   ```

3. **注意事项**:
   - GPU 约束: 仅使用 cuda:0 和 cuda:1 (C001)
   - Mistral tokenizer vocab 不同 (32768 vs 128256)，但 data_utils 用 tokenizer 动态编码，无影响
   - wandb project 可沿用 `distill_sparse_swiglu`，run name 加 `mistral_` 前缀区分
