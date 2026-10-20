# ssh prepare phi4 pilot

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_prepare-phi4-pilot_20260518T224632_result.json`
- **Structured JSON:** [`035a84c644de282ec66d.json`](../../sessions/03/035a84c644de282ec66d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修改全部正确。汇总结果：

---

## 产出

### 1. train_sft.py 修改（3 处）

| 位置 | 修改内容 |
|------|----------|
| L125-126 | 新增 `--lora-targets` 参数（逗号分隔的模块名，默认 None 保持向后兼容） |
| L173 | LoRA target_modules 优先使用 `args.lora_targets.split(",")`, 否则用 DEFAULT |
| L258 | train_config.json 中记录实际使用的 `lora_targets` |

不传 `--lora-targets` 时行为与修改前完全一致。

### 2. Phi-4 dry-run：**无法执行**

- Phi-4 模型未下载到服务器（`/root/autodl-tmp/models/` 下无 phi-4）
- GPU 0 被两个进程占满（6106 + 17312 = 23418 / 24564 MiB），无空闲 GPU
- 需要先下载 Phi-4 并等 GPU 释放后再 dry-run

### 3. OLMo-2 架构：**模型也未下载**

### 4. 基于已知架构的推荐命令

**Phi-4**（Phi3ForCausalLM，fused QKV + fused gate_up）：
```bash
CUDA_VISIBLE_DEVICES=N /root/miniconda3/bin/python3.12 exp001/train_sft.py \
  --model-name /root/autodl-tmp/models/phi-4 \
  --data-path /root/autodl-tmp/sft_data/sft_dosage_000.jsonl \
  --output-dir /root/autodl-tmp/outputs/phi-4_d000_s42 \
  --seed 42 --lr 5e-5 --lora-r 16 --lora-alpha 32 \
  --batch-size 1 --grad-accum 16 --epochs 1 --max-seq-length 2048 \
  --gradient-checkpointing \
  --lora-targets qkv_proj,o_proj,gate_up_proj,down_proj
```

**OLMo-2-7B**（OLMo2ForCausalLM，separate QKV + fused gate_up）：
```bash
CUDA_VISIBLE_DEVICES=N /root/miniconda3/bin/python3.12 exp001/train_sft.py \
  --model-name /root/autodl-tmp/models/OLMo-2-1124-7B \
  --data-path /root/autodl-tmp/sft_data/sft_dosage_000.jsonl \
  --output-dir /root/autodl-tmp/outputs/OLMo-2-7B_d000_s42 \
  --seed 42 --lr 5e-5 --lora-r 16 --lora-alpha 32 \
  --batch-size 1 --grad-accum 16 --epochs 1 --max-seq-length 2048 \
  --gradient-checkpointing \
  --lora-targets q_proj,k_proj,v_proj,o_proj,gate_up_proj,down_proj
```

> 模型下载到位后，建议先用 `python -c "from transformers import AutoModelForCausalLM; ..."` 打印 `named_modules()` 确认实际模块名，再执行 dry-run。

---
