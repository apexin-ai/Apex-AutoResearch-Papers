# train llama32 3B d000 sft cuda4

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_llama32_3B_d000_sft_cuda4_20260516T102653_result.json`
- **Structured JSON:** [`5cdda0288210bf105050.json`](../../sessions/5c/5cdda0288210bf105050.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练成功启动并在运行。

**汇报：**

| 项目 | 值 |
|---|---|
| 模型路径 | `/root/autodl-tmp/models/LLM-Research/Llama-3___2-3B` |
| 架构 | LlamaForCausalLM (3B, 28 layers, hidden=3072) |
| 训练数据 | `/root/autodl-tmp/exp001/sft_data/sft_dosage_000.jsonl` (50000 samples) |
| Output dir | `/root/autodl-tmp/exp001/checkpoints/Llama-3.2-3B_d000_s42/` |
| GPU | cuda:4 (CUDA_VISIBLE_DEVICES=4) |
| PID | 752961 |
| VRAM | 23493 MiB / 24GB, 100% utilization |
| tmux session | `llama3b_d000_s42` |
| 日志 | `/tmp/llama3b_d000_s42.log` |
| 超参 | lora_r=16, lora_alpha=32, lr=5e-5, batch=2, grad_accum=8, epochs=1, gradient_checkpointing=true, --merge |

训练命令：
```
CUDA_VISIBLE_DEVICES=4 python /root/contamcal-irt-calibration/exp001/train_sft.py \
  --model-name /root/autodl-tmp/models/LLM-Research/Llama-3___2-3B \
  --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_000.jsonl \
  --output-dir /root/autodl-tmp/exp001/checkpoints/Llama-3.2-3B_d000_s42 \
  --seed 42 --lora-r 16 --lora-alpha 32 --lr 5e-5 \
  --batch-size 2 --grad-accum 8 --epochs 1 \
  --gradient-checkpointing --merge
```

注意：模型来源为 ModelScope 上 `LLM-Research/Llama-3.2-3B`（HF 格式，已验证 config.json 为 LlamaForCausalLM）。HuggingFace 直接下载因 gated repo 失败，服务器无 HF token。

---
