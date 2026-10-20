# DocRED LoRA Merge + Eval 命令清单

> 生成时间: 2026-05-15
> 训练状态: step 382/573 (epoch 2/3), 两个模型均在训练中

## 训练进程信息

| 模型 | PID | GPU | 当前进度 | 预计剩余 |
|------|-----|-----|---------|---------|
| Llama-3.1-8B DocRED LoRA | 298323 | cuda:0 | 382/573 (epoch 2/3) | ~191 steps |
| Qwen3-8B DocRED LoRA | 298245 | cuda:1 | 382/573 (epoch 2/3) | ~191 steps |

## 重要说明

1. **训练脚本自带 merge**: 两个训练脚本 (`train_lora_docred.py`, `train_lora_docred_llama.py`) 在训练完成后会自动执行 `merge_and_save()`，将 LoRA adapter 合并到 base model 并保存到 merged_dir。**如果训练正常结束，不需要手动 merge。**
2. **下面的手动 merge 命令**是备用方案，仅在训练脚本的 merge 步骤失败或训练用了 `--no_merge` 时才需要。
3. **磁盘空间**: `/root/autodl-tmp` 有 162GB 可用，每个 merged 模型约 16GB (bf16)，足够。
4. **现有 eval 脚本**: `scripts/run_docred_lora_eval.sh` 已包含所有 4 条 eval 命令，可直接使用。

---

## 路径总览

| 资源 | 路径 |
|------|------|
| Qwen base model | `/root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B` |
| Llama base model | `/root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-8B-Instruct` |
| Qwen LoRA adapter | `/root/schema_semantic_constrained_ie/checkpoints/qwen_lora_docred/` |
| Llama LoRA adapter | `/root/schema_semantic_constrained_ie/checkpoints/llama_lora_docred/` |
| Qwen merged (输出) | `/root/autodl-tmp/checkpoints/qwen_lora_docred_merged/` |
| Llama merged (输出) | `/root/autodl-tmp/checkpoints/llama_lora_docred_merged/` |
| DocRED dev data | `data/docred/dev.json` |
| DocRED constraints | `data/docred/ontology_constraints_docred.json` |

---

## 1. Qwen3-8B DocRED — Merge (备用)

仅在自动 merge 失败时使用。在 CPU 上执行，不占 GPU 显存。

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/schema_semantic_constrained_ie

python -c "
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import PeftModel

base_path = '/root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B'
adapter_path = 'checkpoints/qwen_lora_docred'
merged_dir = '/root/autodl-tmp/checkpoints/qwen_lora_docred_merged'

print('[merge] loading base...', flush=True)
base = AutoModelForCausalLM.from_pretrained(base_path, torch_dtype=torch.bfloat16, device_map='cpu', trust_remote_code=True)
print('[merge] loading adapter...', flush=True)
model = PeftModel.from_pretrained(base, adapter_path)
print('[merge] merging...', flush=True)
model = model.merge_and_unload()
import os; os.makedirs(merged_dir, exist_ok=True)
model.save_pretrained(merged_dir, safe_serialization=True)
tok = AutoTokenizer.from_pretrained(base_path, trust_remote_code=True)
tok.save_pretrained(merged_dir)
print(f'[merge] done -> {merged_dir}', flush=True)
"
```

预期输出: `/root/autodl-tmp/checkpoints/qwen_lora_docred_merged/` (含 model*.safetensors + tokenizer 文件)

---

## 2. Qwen3-8B DocRED — Unconstrained Eval

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/schema_semantic_constrained_ie

CUDA_VISIBLE_DEVICES=1 python run_constrained_extraction.py \
    --mode unconstrained \
    --dataset docred \
    --model_path /root/autodl-tmp/checkpoints/qwen_lora_docred_merged \
    --data_path data/docred/dev.json \
    --constraints_path data/docred/ontology_constraints_docred.json \
    --output_path outputs/w5_qwen_docred_lora_unconstrained_eval.jsonl \
    --device cuda:0 \
    --max_new_tokens 4096 \
    --batch_size 1
```

预期输出: `outputs/w5_qwen_docred_lora_unconstrained_eval.jsonl`

---

## 3. Qwen3-8B DocRED — Constrained Eval (full_s1)

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/schema_semantic_constrained_ie

CUDA_VISIBLE_DEVICES=1 python run_constrained_extraction.py \
    --mode full_s1 \
    --dataset docred \
    --model_path /root/autodl-tmp/checkpoints/qwen_lora_docred_merged \
    --data_path data/docred/dev.json \
    --constraints_path data/docred/ontology_constraints_docred.json \
    --output_path outputs/w5_qwen_docred_lora_constrained_eval.jsonl \
    --device cuda:0 \
    --max_new_tokens 4096 \
    --batch_size 1
```

预期输出: `outputs/w5_qwen_docred_lora_constrained_eval.jsonl`

---

## 4. Llama-3.1-8B DocRED — Merge (备用)

仅在自动 merge 失败时使用。

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/schema_semantic_constrained_ie

python -c "
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import PeftModel

base_path = '/root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-8B-Instruct'
adapter_path = 'checkpoints/llama_lora_docred'
merged_dir = '/root/autodl-tmp/checkpoints/llama_lora_docred_merged'

print('[merge] loading base...', flush=True)
base = AutoModelForCausalLM.from_pretrained(base_path, torch_dtype=torch.bfloat16, device_map='cpu', trust_remote_code=True)
print('[merge] loading adapter...', flush=True)
model = PeftModel.from_pretrained(base, adapter_path)
print('[merge] merging...', flush=True)
model = model.merge_and_unload()
import os; os.makedirs(merged_dir, exist_ok=True)
model.save_pretrained(merged_dir, safe_serialization=True)
tok = AutoTokenizer.from_pretrained(base_path, trust_remote_code=True)
tok.save_pretrained(merged_dir)
print(f'[merge] done -> {merged_dir}', flush=True)
"
```

预期输出: `/root/autodl-tmp/checkpoints/llama_lora_docred_merged/` (含 model*.safetensors + tokenizer 文件)

---

## 5. Llama-3.1-8B DocRED — Unconstrained Eval

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/schema_semantic_constrained_ie

CUDA_VISIBLE_DEVICES=0 python run_constrained_extraction.py \
    --mode unconstrained \
    --dataset docred \
    --model_path /root/autodl-tmp/checkpoints/llama_lora_docred_merged \
    --data_path data/docred/dev.json \
    --constraints_path data/docred/ontology_constraints_docred.json \
    --output_path outputs/w5_llama_docred_lora_unconstrained_eval.jsonl \
    --device cuda:0 \
    --max_new_tokens 4096 \
    --batch_size 1
```

预期输出: `outputs/w5_llama_docred_lora_unconstrained_eval.jsonl`

---

## 6. Llama-3.1-8B DocRED — Constrained Eval (full_s1)

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/schema_semantic_constrained_ie

CUDA_VISIBLE_DEVICES=0 python run_constrained_extraction.py \
    --mode full_s1 \
    --dataset docred \
    --model_path /root/autodl-tmp/checkpoints/llama_lora_docred_merged \
    --data_path data/docred/dev.json \
    --constraints_path data/docred/ontology_constraints_docred.json \
    --output_path outputs/w5_llama_docred_lora_constrained_eval.jsonl \
    --device cuda:0 \
    --max_new_tokens 4096 \
    --batch_size 1
```

预期输出: `outputs/w5_llama_docred_lora_constrained_eval.jsonl`

---

## 快捷方式：使用现有 eval 脚本

```bash
# 运行全部 4 条 eval（前提：merged 模型已存在）
bash scripts/run_docred_lora_eval.sh all

# 或单独运行
bash scripts/run_docred_lora_eval.sh qwen_unconstrained
bash scripts/run_docred_lora_eval.sh qwen_constrained
bash scripts/run_docred_lora_eval.sh llama_unconstrained
bash scripts/run_docred_lora_eval.sh llama_constrained
```

---

## 建议执行顺序

1. 等训练完成（两个进程各自完成 epoch 3 + 自动 merge）
2. 验证 merged 模型存在:
   ```bash
   ls /root/autodl-tmp/checkpoints/qwen_lora_docred_merged/model*.safetensors
   ls /root/autodl-tmp/checkpoints/llama_lora_docred_merged/model*.safetensors
   ```
3. 若 merged 缺失 → 执行对应的手动 merge 命令（命令 1 或 4）
4. 并行跑 eval（Qwen 用 cuda:1, Llama 用 cuda:0）:
   ```bash
   # Terminal 1
   bash scripts/run_docred_lora_eval.sh qwen_unconstrained
   bash scripts/run_docred_lora_eval.sh qwen_constrained

   # Terminal 2
   bash scripts/run_docred_lora_eval.sh llama_unconstrained
   bash scripts/run_docred_lora_eval.sh llama_constrained
   ```

## DocRED 特有注意事项

- **max_new_tokens=4096**: DocRED 是文档级 RE，96 种 relation type，输出可能很长。eval 脚本已设 4096。若发现输出被截断，可考虑增大到 6144（参考 SciERC 用 2048 够了，但之前 zero-shot DocRED Llama eval 曾用过 6144）。
- **96 relation types**: 相比 SciERC 的 7 种，DocRED constraints 文件 (`ontology_constraints_docred.json`, 63KB) 要大得多，constrained decoding 的 mask 计算开销更大。
- **batch_size=1**: DocRED 长文本 + constrained decoding 显存开销大，保持 batch_size=1。
