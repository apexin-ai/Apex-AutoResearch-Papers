# code llama rsft s42 withevi 2048 launch

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_llama-rsft-s42-withevi-2048-launch_20260521T024516_result.json`
- **Structured JSON:** [`e44deec64e2a3a531978.json`](../../sessions/e4/e44deec64e2a3a531978.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已启动。

| 项目 | 值 |
|------|-----|
| **exp_id** | `eval_llama_rsft_s42_with_evidence_2048` |
| **PID** | 70706 |
| **GPU** | cuda:0, 18879 MiB |
| **Base** | `/root/autodl-tmp/models/meta-llama/Meta-Llama-3.1-8B` |
| **SFT adapter** | `/root/autodl-tmp/sft_output_llama_3_1_8b` |
| **RSFT adapter** | `/root/autodl-tmp/rsft_output_llama_3_1_8b_k1` |
| **Output** | `/root/autodl-tmp/eval_results/eval_llama_rsft_s42_with_evidence_2048` |
| **Log** | `/root/runs/faith-evidence-ie/eval_llama_rsft_s42_with_evidence_2048.log` |

**完整命令：**
```
CUDA_VISIBLE_DEVICES=0 python -m freige.eval.inference \
  --model_path /root/autodl-tmp/rsft_output_llama_3_1_8b_k1 \
  --base_model /root/autodl-tmp/models/meta-llama/Meta-Llama-3.1-8B \
  --sft_adapter /root/autodl-tmp/sft_output_llama_3_1_8b \
  --data_path /root/autodl-tmp/data/docred --split dev \
  --output_dir /root/autodl-tmp/eval_results/eval_llama_rsft_s42_with_evidence_2048 \
  --batch_size 1 --max_new_tokens 2048 --no-quantize --seed 42
```

推理已进行中（~9s/it, 预计 ~2.5h）。Nested LoRA: base → merge SFT → load RSFT。

---
