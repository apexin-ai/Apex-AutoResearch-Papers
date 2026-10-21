# code llama docred lora training prep

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_llama_docred_lora_training_prep_20260515T181057_result.json`
- **Structured JSON:** [`8937dc26fa2fa45697b0.json`](../../sessions/89/8937dc26fa2fa45697b0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run 成功。训练指标正常：loss=0.1747, token_accuracy=95.3%。

---

**汇报**

**脚本路径**: `/root/schema_semantic_constrained_ie/scripts/train_lora_docred_llama.py`

**训练启动命令**:
```bash
cd /root/schema_semantic_constrained_ie && \
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
CUDA_VISIBLE_DEVICES=1 WANDB_MODE=disabled \
python scripts/train_lora_docred_llama.py
```

**超参数**:
| 参数 | 值 | 来源 |
|---|---|---|
| model | Llama-3.1-8B-Instruct | 同 SciERC |
| LoRA r/alpha/dropout | 16/32/0.05 | 同 SciERC |
| target_modules | q/k/v/o/gate/up/down_proj | 同 SciERC |
| lr | 2e-4, cosine | 同 SciERC |
| epochs | 3 | 同 SciERC |
| batch_size × grad_accum | 2×8=16 | 有效batch同 SciERC (4×4=16)，但单batch更小以适应4096长度 |
| max_length | 4096 | DocRED 文档级，SciERC 是 2048 |

**输出路径**:
- LoRA adapter: `checkpoints/llama_lora_docred/` (根分区)
- Merged model: `/root/autodl-tmp/checkpoints/llama_lora_docred_merged/` (数据盘)

**预估训练时长**: dry-run 每 step ~8.8s，full training 共 `ceil(3053/2)*3/8 ≈ 573 steps`，约 573×8.8s ≈ 84 分钟。SciERC Llama 训练 654s (330 steps)，DocRED 数据量是 1.73 倍且 max_length 翻倍，~80-90 分钟合理。

**注意事项**:
- GPU 0 被其他进程占满（88GB/97GB），**必须用 GPU 1** (`CUDA_VISIBLE_DEVICES=1`)
- Llama DocRED SFT 数据已预生成 Llama chat format，无需 Qwen→Llama 转换
- Dry-run 初始 loss=0.1747 / token_acc=95.3%，与 SciERC 首轮水平一致，数据格式确认正确

---
