# code prepare gemma d025

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prepare-gemma-d025_20260518T222642_result.json`
- **Structured JSON:** [`20ea3ea1f22d3e57f77b.json`](../../sessions/20/20ea3ea1f22d3e57f77b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证完成。

## 验证结果汇总

| 项目 | 状态 |
|------|------|
| **数据文件** `sft_dosage_025.jsonl` | 存在，90MB，54133 行 |
| **Gemma-2-9b 模型** | 完整（8 个 safetensors + tokenizer） |
| **输出目录** `gemma-2-9b_d025_s42` | 不存在，可安全使用 |
| **训练脚本参数** | 解析正常，所有参数匹配 |
| **d000 参考配置** | lora_alpha=32, lora_r=16, lr=5e-5, gradient_checkpointing=false, load_in_4bit=false |
| **Phi-4** | 就绪（6 个 safetensors + tokenizer） |
| **OLMo-2-1124-7B** | 就绪（6 个 safetensors + tokenizer） |

## 就绪命令（d005 完成后提交）

```bash
cd /root/contamcal-irt-calibration && CUDA_VISIBLE_DEVICES=1 PYTHONUNBUFFERED=1 /root/miniconda3/bin/python3.12 exp001/train_sft.py \
  --model-name /root/autodl-tmp/models/gemma-2-9b \
  --data-path /root/autodl-tmp/sft_data/sft_dosage_025.jsonl \
  --output-dir /root/autodl-tmp/exp001/checkpoints/gemma-2-9b_d025_s42 \
  --seed 42 --lr 5e-5 --lora-r 16 --lora-alpha 32 \
  --batch-size 1 --grad-accum 16 --epochs 1 --max-seq-length 2048
```

参数与 d000 完全一致（无 QLoRA、无 gradient checkpointing），仅 data-path 和 output-dir 不同。Phi-4 和 OLMo-2 模型均就绪，后续 dosage chain 可直接使用。

---
