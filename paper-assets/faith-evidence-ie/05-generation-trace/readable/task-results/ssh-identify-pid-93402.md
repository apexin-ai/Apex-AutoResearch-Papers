# ssh identify pid 93402

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_identify-pid-93402_20260521T090552_result.json`
- **Structured JSON:** [`3de05e9e2b372670ba19.json`](../../sessions/3d/3de05e9e2b372670ba19.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

PID 93402 是本项目的 eval 推理进程，运行了约 2 分 8 秒：

```
python -m freige.eval.inference \
  --model_path /root/autodl-tmp/models/Qwen3-4B \
  --sft_adapter /root/autodl-tmp/sft_output \
  --output_dir /root/autodl-tmp/eval_results/d140_4b_sft_s42_with_evi_2048 \
  --split dev --batch_size 4 --max_new_tokens 2048 --no-quantize --seed 42
```

实验标识：**d140_4b_sft_s42_with_evi_2048**（Qwen3-4B SFT eval，带 evidence，max_new_tokens=2048）。

当前全部 GPU 占用：

| GPU | PID | 显存 |
|-----|-----|------|
| cuda:0 | 87387 | 6,150 MiB |
| cuda:1 | 88992 | 11,454 MiB |
| cuda:2 | 87307 | 19,590 MiB |
| cuda:3 | 93402 | 11,140 MiB |

---
