# ops fix and resubmit tail1024

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fix_and_resubmit_tail1024_20260518T030337_result.json`
- **Structured JSON:** [`dcc368c293bf2757bb2b.json`](../../sessions/dc/dcc368c293bf2757bb2b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

- **训练脚本完整路径**: `/root/trace-verdict-study/train/train_sft.py`（不是 `train.py`）
- **工作目录**: `/root/trace-verdict-study`
- **启动命令格式**（从 head2048 进程提取）:
  ```
  /root/miniconda3/bin/python train/train_sft.py --condition full_trace_head --model_path /root/autodl-tmp/models/CodeLlama-13b-Instruct-hf --gradient_checkpointing --gpu 0 --seed 42 --output_dir ... --wandb_project trace-verdict-study --wandb_run_name ...
  ```

`codellama13b_full_trace_tail1024_seed42` 启动失败的原因是脚本名错误（用了 `train.py` 而非 `train/train_sft.py`）。

---
