# ops adapt scripts llama

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_adapt-scripts-llama_20260516T044945_result.json`
- **Structured JSON:** [`1e21edc3ddd8678ac385.json`](../../sessions/1e/1e21edc3ddd8678ac385.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

信息收集完毕。以下是完整报告。

---

## LLaMA-3.1-8B-Instruct 兼容性报告

### 1. swift sft 兼容性：✅ 完全自动

- **ms-swift 4.2.0** 原生支持 LLaMA 3.1（从 config.json `model_type: "llama"` 自动识别）
- **LoRA targets**: 自动检测（q_proj, k_proj, v_proj, o_proj, gate_proj, up_proj, down_proj）
- **Chat template**: 从 tokenizer_config.json 自动加载
- **无需额外参数**，只需换 `--model` 路径

### 2. Eval 脚本兼容性：✅ 无需改代码

两个 eval 脚本 (`recovery.py`, `injected_eval.py`) 使用：
- `AutoModelForCausalLM` + `AutoTokenizer` + `PeftModel` — 模型无关
- `tokenizer.apply_chat_template()` — LLaMA 3.1 Instruct 有完整 chat template

唯一 Qwen 相关：`--base_model` 默认值为 `/root/autodl-tmp/models/Qwen/Qwen3-8B`。运行时传参覆盖即可，无需改源码。

### 3. 数据格式：✅ 通用

数据为标准 `{"messages": [{"role": "user", "content": ...}, {"role": "assistant", "content": ...}]}` 格式，内容无模型特定 token，swift 自动根据模型应用对应 template。

### 4. 阻塞项：模型下载未完成

权重文件在 `._____temp/` 中（1.3G / 预期 ~16G），下载中断或未完成。需重新下载后才能跑实验。

---

### 5. 完整训练命令（三个条件）

```bash
# === Vanilla ===
swift sft \
  --model /root/autodl-tmp/models/Meta-Llama-3.1-8B-Instruct \
  --dataset /root/autodl-tmp/tax_error_inject_agent/data/mini_pipeline_v4/sft_vanilla_v4.jsonl \
  --output_dir /root/autodl-tmp/tax_error_inject_agent/output/llama31-vanilla-s42 \
  --lora_rank 16 \
  --num_train_epochs 3 \
  --per_device_train_batch_size 4 \
  --gradient_accumulation_steps 2 \
  --learning_rate 1e-4 \
  --max_length 4096 \
  --seed 42 \
  --data_seed 42 \
  --logging_steps 10 \
  --gradient_checkpointing true \
  --bf16 true \
  --save_strategy epoch

# === TaxEI ===
swift sft \
  --model /root/autodl-tmp/models/Meta-Llama-3.1-8B-Instruct \
  --dataset /root/autodl-tmp/tax_error_inject_agent/data/mini_pipeline_v4/sft_taxei_v4.jsonl \
  --output_dir /root/autodl-tmp/tax_error_inject_agent/output/llama31-taxei-s42 \
  --lora_rank 16 \
  --num_train_epochs 3 \
  --per_device_train_batch_size 4 \
  --gradient_accumulation_steps 2 \
  --learning_rate 1e-4 \
  --max_length 4096 \
  --seed 42 \
  --data_seed 42 \
  --logging_steps 10 \
  --gradient_checkpointing true \
  --bf16 true \
  --save_strategy epoch

# === Random ===
swift sft \
  --model /root/autodl-tmp/models/Meta-Llama-3.1-8B-Instruct \
  --dataset /root/autodl-tmp/tax_error_inject_agent/data/mini_pipeline_v4/sft_random_v4.jsonl \
  --output_dir /root/autodl-tmp/tax_error_inject_agent/output/llama31-random-s42 \
  --lora_rank 16 \
  --num_train_epochs 3 \
  --per_device_train_batch_size 4 \
  --gradient_accumulation_steps 2 \
  --learning_rate 1e-4 \
  --max_length 4096 \
  --seed 42 \
  --data_seed 42 \
  --logging_steps 10 \
  --gradient_checkpointing true \
  --bf16 true \
  --save_strategy epoch

# === TaxEI-RP (Recovery Paired) ===
swift sft \
  --model /root/autodl-tmp/models/Meta-Llama-3.1-8B-Instruct \
  --dataset /root/autodl-tmp/tax_error_inject_agent/data/recovery_paired/sft_taxei_rp.jsonl \
  --output_dir /root/autodl-tmp/tax_error_inject_agent/output/llama31-taxei-rp-s42 \
  --lora_rank 16 \
  --num_train_epochs 3 \
  --per_device_train_batch_size 4 \
  --gradient_accumulation_steps 2 \
  --learning_rate 1e-4 \
  --max_length 4096 \
  --seed 42 \
  --data_seed 42 \
  --logging_steps 10 \
  --gradient_checkpointing true \
  --bf16 true \
  --save_strategy epoch
```

### 6. Eval 命令

```bash
# Baseline (no injection)
CUDA_VISIBLE_DEVICES=3 python eval/recovery.py \
  --base_model /root/autodl-tmp/models/Meta-Llama-3.1-8B-Instruct \
  --model_path /root/autodl-tmp/tax_error_inject_agent/output/llama31-vanilla-s42/checkpoint-xxx \
  --model_variant vanilla \
  --num_episodes 47 \
  --output eval_results/llama31_vanilla_baseline.json

# Injected eval (context injection)
CUDA_VISIBLE_DEVICES=3 python eval/injected_eval.py \
  --base_model /root/autodl-tmp/models/Meta-Llama-3.1-8B-Instruct \
  --model_path /root/autodl-tmp/tax_error_inject_agent/output/llama31-taxei-s42/checkpoint-xxx \
  --model_variant taxei \
  --num_episodes 47 \
  --output eval_results/llama31_injected_taxei.json

# Action injection eval
CUDA_VISIBLE_DEVICES=3 python eval/recovery.py \
  --base_model /root/autodl-tmp/models/Meta-Llama-3.1-8B-Instruct \
  --model_path /root/autodl-tmp/tax_error_inject_agent/output/llama31-taxei-rp-s42/checkpoint-xxx \
  --model_variant taxei \
  --inject --inject_mode action \
  --num_episodes 47 \
  --output eval_results/llama31_action_inject_taxei.json
```

### 7. 需修改的文件：无

所有脚本通过命令行参数 `--model` / `--base_model` 指定模型路径，无需改源码。

### 8. 待办

| 项目 | 状态 |
|------|------|
| 完成 LLaMA-3.1-8B-Instruct 模型下载 | ❌ 需重新下载（当前 1.3G/~16G） |
| 等 Qwen3-8B 当前训练结束释放 GPU | ⏳ |
| 跑 LLaMA 3.1 三条件训练 | 待上述两项完成 |

---
