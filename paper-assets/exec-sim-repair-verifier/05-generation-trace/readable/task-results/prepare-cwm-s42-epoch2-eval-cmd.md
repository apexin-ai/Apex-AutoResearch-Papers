# prepare cwm s42 epoch2 eval cmd

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prepare_cwm-s42-epoch2-eval-cmd_20260517T194907_result.json`
- **Structured JSON:** [`ad9ea922ca8d2e3b924f.json`](../../sessions/ad/ad9ea922ca8d2e3b924f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

checkpoint-8844 存在。当前 GPU 1 上的完整命令已获取。

```
CWM s42 epoch 3 eval 命令（当前 GPU 1）：
CUDA_VISIBLE_DEVICES=1 python3 /home/sonny/exec-sim-repair-verifier/eval_repo_cwm.py --checkpoint_dir /root/autodl-tmp/checkpoints_deepseek_cwm_repo/best/ --model_name /root/autodl-tmp/models/deepseek-ai/deepseek-coder-6.7b-instruct --data_dir /home/sonny/exec-sim-repair-verifier/data/swebench_full --device cuda:0 --batch_size 1 --max_seq_length 4096 --max_new_tokens 512 --output eval_deepseek_cwm_repo_s42.json --pred_output eval_deepseek_cwm_repo_s42_predictions.jsonl --output_dir /root/autodl-tmp/eval_results/deepseek_cwm_repo_s42_test --split test

CWM s42 epoch 2 eval 命令（GPU 2 释放后启动）：
CUDA_VISIBLE_DEVICES=2 python3 /home/sonny/exec-sim-repair-verifier/eval_repo_cwm.py --checkpoint_dir /root/autodl-tmp/checkpoints_deepseek_cwm_repo/checkpoint-8844/ --model_name /root/autodl-tmp/models/deepseek-ai/deepseek-coder-6.7b-instruct --data_dir /home/sonny/exec-sim-repair-verifier/data/swebench_full --device cuda:0 --batch_size 1 --max_seq_length 4096 --max_new_tokens 512 --output eval_deepseek_cwm_repo_s42_ep2.json --pred_output eval_deepseek_cwm_repo_s42_ep2_predictions.jsonl --output_dir /root/autodl-tmp/eval_results/deepseek_cwm_repo_s42_ep2_test --split test
```

注意：脚本内部用 `--device cuda:0`，实际 GPU 由 `CUDA_VISIBLE_DEVICES` 控制映射。

---
