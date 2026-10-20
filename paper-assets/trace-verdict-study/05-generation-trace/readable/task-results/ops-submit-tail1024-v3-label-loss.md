# ops submit tail1024 v3 label loss

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_submit_tail1024_v3_label_loss_20260518T063926_result.json`
- **Structured JSON:** [`ae5f4b2cd5c550d64c0a.json`](../../sessions/ae/ae5f4b2cd5c550d64c0a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

**1. 参数名确认：`--label_only_loss`**（描述：Only compute loss on completion tokens）

**2. 完整训练命令：**
```bash
cd /root/trace-verdict-study && /root/miniconda3/bin/python train/train_sft.py --condition full_trace_tail_1024 --model_path /root/autodl-tmp/models/CodeLlama-13b-Instruct-hf --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_full_trace_tail1024_seed42_v3 --seed 42 --wandb_project trace-verdict-study --wandb_run_name codellama13b_full_trace_tail1024_seed42_v3 --gradient_checkpointing --label_only_loss
```

**3. tail-2048 进度：327/444 steps (73%), 已运行 2h46m，预计还需 ~54min**

---
