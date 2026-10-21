# exp_017: LLaMA-3.1-8B CoNLL-2003 LoRA Fine-tune

## 状态: 已完成 (2026-05-14 22:39 ~ 2026-05-15 01:03)

## 1. LLaMA Base Model 路径
```
/root/autodl-tmp/.hf_cache/LLM-Research/Meta-Llama-3___1-8B-Instruct
```

## 2. CoNLL 数据
- 路径: `/root/autodl-tmp/struct_self_consist_ie/data/conll2003/`
- 训练集: `llmfactory_train.json` — **14,041 samples**
- 验证集: `llmfactory_dev.json` — **3,250 samples**
- 格式: ShareGPT (conversations 字段)
- LLaMA Factory dataset_info 注册名: `conll2003_uie_train` / `conll2003_uie_dev`

## 3. 训练命令
```bash
bash -c "cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=1 source /root/miniconda3/bin/activate && llamafactory-cli train train_config_llama_conll2003.yaml"
```

## 4. 关键超参 (从 exp-007 SciERC 复制，微调 eval/save 频率)

| 参数 | exp-007 (SciERC) | exp-017 (CoNLL) |
|------|-------------------|-----------------|
| LoRA rank | 32 | 32 |
| LoRA alpha | 64 | 64 |
| LoRA target | all | all |
| Learning rate | 2e-4 | 2e-4 |
| Epochs | 5 | 5 |
| Batch size (per device) | 2 | 2 |
| Gradient accumulation | 8 | 8 |
| Effective batch size | 16 | 16 |
| LR scheduler | cosine | cosine |
| Warmup ratio | 0.1 | 0.1 |
| bf16 | true | true |
| Gradient checkpointing | true | true |
| Max grad norm | 1.0 | 1.0 |
| cutoff_len | 2048 | 2048 |
| eval_steps | 100 | 200 |
| save_steps | 100 | 200 |
| save_total_limit | 3 | 5 |
| load_best_model_at_end | - | true |
| metric_for_best_model | - | eval_loss |
| Trainable params | ~84M (1.03%) | 83,886,080 (1.03%) |

## 5. 训练结果 (已完成)
- **训练时长**: 2:22:02
- **Train loss**: 0.0392
- **Eval loss**: 0.0226
- **Train samples/sec**: 8.237
- **Total steps**: ~4,390 (14,041 * 5 / 16)

## 6. Checkpoints
- LoRA adapter: `checkpoints/llama3.1-8b-conll2003-lora/`
- Merged model: `checkpoints/llama3.1-8b-conll2003-merged/` (4 shard safetensors, ~15GB)
- Export config: `export_config_llama_conll2003.yaml`

## 7. 配置文件
- 训练配置: `train_config_llama_conll2003.yaml`
- 导出配置: `export_config_llama_conll2003.yaml`
- 参考 (exp-007 SciERC): `train_config_llama.yaml` / `export_config_llama.yaml`

## 8. Dry-run 验证
无需 dry-run — 训练已于 2026-05-15 完成，merged model 完整可用。
训练日志: `checkpoints/exp017_train.log`
