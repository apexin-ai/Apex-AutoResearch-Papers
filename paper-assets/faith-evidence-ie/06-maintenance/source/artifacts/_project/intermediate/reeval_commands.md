# D076 Reeval 提交命令

生成时间: 2026-05-16
状态: Ready-to-submit（路径已验证，参数格式已从运行中进程确认）

## 参数来源

命令格式从当前运行的 `eval_rsft_ced_s45` 和 `reeval_flat_nli_s43_r2` 进程提取，符合 D076 协议。

eval 脚本: `python -m freige.eval.inference`
base_model: `/root/autodl-tmp/models/Qwen3-4B`
sft_adapter: `/root/autodl-tmp/sft_output`
data_path: `/root/autodl-tmp/data/docred`

---

## 1. reeval_ced_s44

- **exp_id**: `reeval_ced_s44`
- **方法**: CED RSFT, seed=44
- **Checkpoint**: `rsft_output_s44/checkpoint-510` ✅ 已验证 (adapter_model.safetensors 528MB)
- **目标 GPU**: `{GPU}` (待分配，提交前 nvidia-smi 确认显存 < 2GB)
- **output_dir**: `eval_results/rsft_ced_s44_reeval`

```bash
cd /root/autodl-tmp && CUDA_VISIBLE_DEVICES={GPU} HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 /root/miniconda3/bin/python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_s44/checkpoint-510 --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 44 --output_dir /root/autodl-tmp/eval_results/rsft_ced_s44_reeval --no-quantize
```

---

## 2. reeval_ced_s42

- **exp_id**: `reeval_ced_s42`
- **方法**: CED RSFT, seed=42
- **Checkpoint**: `rsft_output/checkpoint-510` ✅ 已验证 (adapter_model.safetensors 528MB)
- **目标 GPU**: `{GPU}` (待分配，提交前 nvidia-smi 确认显存 < 2GB)
- **output_dir**: `eval_results/rsft_ced_s42_reeval`

```bash
cd /root/autodl-tmp && CUDA_VISIBLE_DEVICES={GPU} HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 /root/miniconda3/bin/python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output/checkpoint-510 --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 42 --output_dir /root/autodl-tmp/eval_results/rsft_ced_s42_reeval --no-quantize
```

---

## 3. reeval_flat_nli_s42

- **exp_id**: `reeval_flat_nli_s42`
- **方法**: flat-NLI RSFT, seed=42
- **Checkpoint**: `rsft_output_flat_nli/checkpoint-507` ✅ 已验证 (adapter_model.safetensors 528MB)
- **目标 GPU**: `{GPU}` (待分配，提交前 nvidia-smi 确认显存 < 2GB)
- **output_dir**: `eval_results/rsft_flat_nli_s42_reeval`

```bash
cd /root/autodl-tmp && CUDA_VISIBLE_DEVICES={GPU} HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 /root/miniconda3/bin/python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_flat_nli/checkpoint-507 --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 42 --output_dir /root/autodl-tmp/eval_results/rsft_flat_nli_s42_reeval --no-quantize
```

---

## 提交前检查清单 (C001/C002)

1. `nvidia-smi` 确认目标 GPU 显存占用 < 2GB
2. `CUDA_VISIBLE_DEVICES` 已显式设置（禁止依赖 device_map="auto"）
3. 替换 `{GPU}` 为实际物理 GPU 编号
