# CED RSFT Eval Commands (s43 / s45)

准备于训练完成后立即提交。单卡 ~1h，需确认 GPU 显存 < 2GB (C001)。

## eval_ced_rsft_s43

```bash
CUDA_VISIBLE_DEVICES=<GPU> bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_ced_s43/<CHECKPOINT> --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 43 --output_dir /root/autodl-tmp/eval_results/rsft_ced_s43 --no-quantize"
```

## eval_ced_rsft_s45

```bash
CUDA_VISIBLE_DEVICES=<GPU> bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_ced_s45/<CHECKPOINT> --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 45 --output_dir /root/autodl-tmp/eval_results/rsft_ced_s45 --no-quantize"
```

## 提交前检查

1. **确认 checkpoint 路径**：`ls /root/autodl-tmp/rsft_output_ced_s43/` 和 `ls /root/autodl-tmp/rsft_output_ced_s45/`，用最后一个 checkpoint-xxx 目录替换 `<CHECKPOINT>`
2. **确认 GPU 空闲 (C001)**：`nvidia-smi` 确认目标 GPU 显存占用 < 2GB
3. **设置 CUDA_VISIBLE_DEVICES (C002)**：替换 `<GPU>` 为空闲 GPU 编号
4. **--sft_adapter 必须保留**：缺失会导致 rel_f1 ≈ 0

## 参数说明

| 参数 | 值 | 说明 |
|------|-----|------|
| base_model | /root/autodl-tmp/models/Qwen3-4B | 基座模型 |
| sft_adapter | /root/autodl-tmp/sft_output | SFT LoRA adapter（必须） |
| model_path | rsft_output_ced_s43 or s45 的最终 checkpoint | CED RSFT adapter |
| batch_size | 4 | 与 flat_nli eval 一致 |
| max_new_tokens | 1024 | 与 flat_nli eval 一致 |
| --no-quantize | - | 不量化，与训练时一致 |
| 预计耗时 | ~1h/eval | 985 docs, 单卡 |
