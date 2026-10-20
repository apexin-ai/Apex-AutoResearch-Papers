# ssh westd phi4 olmo2 prep

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_westd-phi4-olmo2-prep_20260518T230749_result.json`
- **Structured JSON:** [`34de033fbe1cb472775e.json`](../../sessions/34/34de033fbe1cb472775e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GPU 0/2 已完全释放。

---

## 产出总结

### 模型模块名
| 模型 | model_type | LoRA targets |
|------|-----------|-------------|
| **Phi-4** (14B) | `phi3` | `qkv_proj, o_proj, gate_up_proj, down_proj` |
| **OLMo-2-1124-7B** | `olmo2` | `q_proj, k_proj, v_proj, o_proj, gate_proj, up_proj, down_proj` |

### Dry-run 结果
| 模型 | 加载 | LoRA 应用 | Tokenize | 训练 | GPU 显存 |
|------|------|----------|----------|------|---------|
| **Phi-4** | OK | OK (targets 确认) | OK (50k, 37s) | OK (step 4+, ~2.7s/step) | ~29GB on cuda:2 |
| **OLMo-2** | OK | OK (targets 确认) | OK (50k, 35s) | OK (step 56+, ~1.8s/step) | ~69GB on cuda:0 |

Loss 值因 HF Trainer 进度条 `\r` 覆盖未能捕获，但训练步骤稳定推进证明梯度计算正常。

### train_sft.py 修改
已在 westd-29999 上添加 `--lora-targets` 参数：
- 接受逗号分隔的模块名字符串
- 不指定时 fallback 到 `MODEL_TARGET_MODULES` 字典或 `DEFAULT_LORA_CONFIG`
- Phi-4 (`model_type=phi3`) 已有内置映射，不传也行

### 推荐训练命令

**Phi-4 (cuda:2)**:
```bash
CUDA_VISIBLE_DEVICES=2 /root/miniconda3/bin/python3.12 exp001/train_sft.py \
  --model-name /root/autodl-tmp/models/phi-4 \
  --data-path /root/autodl-tmp/sft_data/sft_dosage_XXX.jsonl \
  --output-dir /root/autodl-tmp/exp001/checkpoints/phi-4_dXXX_s42 \
  --seed 42 --lr 5e-5 --lora-r 16 --lora-alpha 32 \
  --batch-size 1 --grad-accum 16 --epochs 1 --max-seq-length 2048 \
  --lora-targets qkv_proj,o_proj,gate_up_proj,down_proj
```

**OLMo-2 (cuda:0)**:
```bash
CUDA_VISIBLE_DEVICES=0 /root/miniconda3/bin/python3.12 exp001/train_sft.py \
  --model-name /root/autodl-tmp/models/OLMo-2-1124-7B \
  --data-path /root/autodl-tmp/sft_data/sft_dosage_XXX.jsonl \
  --output-dir /root/autodl-tmp/exp001/checkpoints/OLMo-2-7B_dXXX_s42 \
  --seed 42 --lr 5e-5 --lora-r 16 --lora-alpha 32 \
  --batch-size 2 --grad-accum 8 --epochs 1 --max-seq-length 2048 \
  --lora-targets q_proj,k_proj,v_proj,o_proj,gate_proj,up_proj,down_proj
```

OLMo-2 不传 `--lora-targets` 也行（DEFAULT_LORA_CONFIG 已覆盖）。Phi-4 同理（`MODEL_TARGET_MODULES["phi3"]` 已内置）。

---
