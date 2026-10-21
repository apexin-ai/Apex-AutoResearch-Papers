# code llama sft s44 withevi 2048 launch

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_llama-sft-s44-withevi-2048-launch_20260521T004503_result.json`
- **Structured JSON:** [`03c6496953f650a28418.json`](../../sessions/03/03c6496953f650a28418.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已启动。

- **PID**: 64023
- **GPU**: cuda:3, 18879 MiB 占用
- **Adapter**: `/root/autodl-tmp/sft_output_llama_3_1_8b_s44`
- **Output**: `/root/autodl-tmp/eval_results/eval_llama_sft_s44_with_evidence_2048`
- **Log**: `/tmp/eval_llama_sft_s44_with_evidence_2048.log`
- **完整命令**:
```
CUDA_VISIBLE_DEVICES=3 python -m freige.eval.inference \
  --model_path /root/autodl-tmp/models/meta-llama/Meta-Llama-3.1-8B \
  --sft_adapter /root/autodl-tmp/sft_output_llama_3_1_8b_s44 \
  --data_path /root/autodl-tmp/data/docred \
  --output_dir /root/autodl-tmp/eval_results/eval_llama_sft_s44_with_evidence_2048 \
  --batch_size 1 --max_new_tokens 2048 --no-quantize --split dev --seed 42
```
- **Registry**: `eval_llama_sft_s44_with_evidence_2048` → RUNNING, parent=llama_sft_s44_train_eval_r3

---
