# d155 gpu2 deepseek cwm s42 eval

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_d155-gpu2-deepseek-cwm-s42-eval_20260519T123810_result.json`
- **Structured JSON:** [`d358e990f42a2503953e.json`](../../sessions/d3/d358e990f42a2503953e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Eval 正常运行：

- **GPU 2**: PID 833672, 23349 MiB / 32607 MiB, 86% util
- **日志**: 模型已加载，推理已开始（"Model loaded. Starting inference..."）
- **数据**: 9784 test instances，label 分布 {1: 7138, 0: 2646}
- **batch_size**: 从 12 降至 4（6.7B 模型 @seq4096 OOM，4 可正常运行，VRAM 余量 ~9GB）

完整命令：
```
bash -c "cd /home/sonny/exec-sim-repair-verifier && HF_HUB_OFFLINE=1 /root/miniconda3/bin/python eval_repo_cwm.py \
  --checkpoint_dir /root/autodl-tmp/checkpoints_deepseek_cwm_repo/checkpoint-13266 \
  --model_name /root/autodl-tmp/models/deepseek-ai/deepseek-coder-6.7b-instruct \
  --split test --device cuda:0 --max_seq_length 4096 --max_new_tokens 512 \
  --batch_size 4 --output_dir /root/autodl-tmp/eval_results/deepseek_cwm_repo_s42_seq4096/"
```

---
