# ssh resume qwen s456 training

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_resume-qwen-s456-training_20260521T182540_result.json`
- **Structured JSON:** [`92d31a6c86d0d2275ace.json`](../../sessions/92/92d31a6c86d0d2275ace.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

恢复成功。

**结果汇总：**

| 项目 | 值 |
|------|-----|
| **完整命令** | `CUDA_VISIBLE_DEVICES=3 /root/miniconda3/bin/python train_repo_cwm.py --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B --output_dir /root/autodl-tmp/checkpoints_repo_cwm_8b_s456/ --seed 456 --run_name repo-cwm-qwen3-8b-lora-s456 --max_seq_length 2048 --batch_size 1 --grad_accumulation 32 --lr 5e-5 --epochs 3 --warmup_ratio 0.1 --lora_rank 16 --lora_alpha 32 --lora_dropout 0.05 --save_steps 100 --eval_steps 100 --save_total_limit 5 --no_wandb --resume_from_checkpoint checkpoint-6100` |
| **tmux session** | `qwen_cwm_s456_resume2` |
| **PID** | 83238 |
| **恢复起始 step** | 6101（从 checkpoint-6100 正确恢复，不是 step 0） |
| **剩余 steps** | ~532 (6101→6633) |
| **GPU 3** | 98% utilization, 27135 MiB |
| **日志** | `~/runs/exec-sim-repair-verifier/qwen_cwm_s456_resume2.log` |

注意：第一次提交因缺少 wandb API key 失败，第二次加了 `--no_wandb` 成功启动。

---
