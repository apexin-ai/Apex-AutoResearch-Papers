# P1 Llama EE FT Prep (westd-16980)

## Llama 模型路径

```
/root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-8B-Instruct
```

其他可用模型（不使用）：
- `Meta-Llama-3.1-70B-Instruct-AWQ-INT4`（太大）
- `Meta-Llama-3___1-8B-Instruct`（重复）

## 环境验证 (westd-16980)

- Python: 3.10.12
- PyTorch: 2.10.0+cu128, CUDA: True
- peft: ok
- trl: ok

## 数据文件确认

| 文件 | westd-16980 状态 |
|------|------------------|
| `data/wikievents/all.jsonl` | 13.8MB |
| `data/wikievents/test.jsonl` | 1.0MB |
| `data/wikievents/dev.jsonl` | 946KB |
| `data/wikievents/ontology_constraints_wikievents.json` | 45KB |
| `data/sft/wikievents_sft_train_llama.jsonl` | 需 Step 0 生成 |
| `data/sft/wikievents_sft_dev_llama.jsonl` | 需 Step 0 生成 |

注意：Qwen 版 SFT 数据（`wikievents_sft_train.jsonl`）不存在于 westd-16980，且格式不兼容 Llama（使用 `<|im_start|>` tokens）。bash 脚本 Step 0 会用 Llama tokenizer 重新生成。

## 创建的文件

### 1. SFT 数据准备脚本

**路径**: `scripts/prepare_sft_data_wikievents_llama.py`

基于 Qwen 版本修改：
- 默认 model_path = Llama-3.1-8B-Instruct
- 使用 `_chat_template_kwargs(tokenizer)` 而非硬编码 `enable_thinking=False`
- 输出到 `*_llama.jsonl`

### 2. 训练脚本

**路径**: `scripts/train_lora_wikievents_llama.py` (167 行)

与 Qwen 版本差异：
- `--model_path` 默认: `/root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-8B-Instruct`
- `--train_data` / `--eval_data`: `wikievents_sft_{train,dev}_llama.jsonl`
- `--output_dir`: `checkpoints/llama_8b_lora_wikievents`
- `--merged_dir`: `checkpoints/llama_8b_lora_wikievents_merged`
- `report_to="none"` 硬编码（无 wandb 相关参数）
- 移除了 `--wandb_project` / `--wandb_run_name` 参数

训练超参不变：LoRA r=16, alpha=32, dropout=0.05, lr=2e-4, 3 epochs, batch=4, grad_accum=4

### 3. Bash 脚本

**路径**: `scripts/run_p1_ee_ft_llama.sh` (70 行, chmod +x)

流程：
- Step 0: 生成 Llama SFT 数据（`prepare_sft_data_wikievents_llama.py`）
- Step 1: LoRA 训练 + merge
- Step 2: Unconstrained inference -> `outputs/ee_llama_ft_wikievents_unconstrained.jsonl`
- Step 3: Constrained inference (full_s1) -> `outputs/ee_llama_ft_wikievents_full_s1.jsonl`
- Step 4: Eval -> `outputs/eval_report_llama_{unconstrained,full_s1}.json`
- Step 5: Violation check -> `outputs/violation_report_llama_ft_{unconstrained,full_s1}.json`

环境变量：`set -eo pipefail`, `TRANSFORMERS_OFFLINE=1`, `HF_HUB_OFFLINE=1`, `WANDB_DISABLED=true`

## 运行命令

```bash
# 在 westd-16980 上
nohup bash /root/schema_semantic_constrained_ie/scripts/run_p1_ee_ft_llama.sh > /root/schema_semantic_constrained_ie/logs/p1_ee_ft_llama.log 2>&1 &
```
