# code llama sft s42 withevi 2048 launch

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_llama-sft-s42-withevi-2048-launch_20260520T211920_result.json`
- **Structured JSON:** [`e37f7a7595b2f30b9fa8.json`](../../sessions/e3/e37f7a7595b2f30b9fa8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已启动。

| 项目 | 值 |
|---|---|
| **PID** | 55468 |
| **GPU** | cuda:3 (18879 MiB / 97887 MiB) |
| **预估时间** | ~3h（985 batches × ~6-12s/it，参考 no-evi@2048 耗时 3.5h@bs4） |
| **输出目录** | `/root/autodl-tmp/eval_results/eval_llama_sft_s42_with_evidence_2048/` |
| **日志** | `/root/runs/faith-evidence-ie/eval_llama_sft_s42_with_evidence_2048.log` |

完整命令：
```bash
CUDA_VISIBLE_DEVICES=3 python -m freige.eval.inference \
    --model_path /root/autodl-tmp/models/meta-llama/Meta-Llama-3.1-8B \
    --sft_adapter /root/autodl-tmp/sft_output_llama_3_1_8b \
    --data_path /root/autodl-tmp/data/docred \
    --output_dir /root/autodl-tmp/eval_results/eval_llama_sft_s42_with_evidence_2048 \
    --batch_size 1 --max_new_tokens 2048 --no-quantize --split dev --seed 42
```

注意：输出目录用了 `/root/autodl-tmp/eval_results/` 而非 `/root/autodl-tmp/freige/eval_outputs/`，与其他所有 eval 结果保持一致。

---
