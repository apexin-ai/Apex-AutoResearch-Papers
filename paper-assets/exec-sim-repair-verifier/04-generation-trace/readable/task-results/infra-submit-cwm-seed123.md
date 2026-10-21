# infra submit cwm seed123

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_submit-cwm-seed123_20260512T112516_result.json`
- **Structured JSON:** [`599acf1addf123010e99.json`](../../sessions/59/599acf1addf123010e99.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

cwm-seed123 已启动并在加载 tokenizer。汇总结果：

---

### cwm-seed123 (新提交)
- **PID**: 34509
- **tmux session**: `cwm-seed123`
- **服务器**: seetacloud-westd-4x5090, cuda:0
- **完整命令**: `bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /home/sonny/exec-sim-repair-verifier && python3 train_cwm_baseline.py --data_dir data/ --model_name Qwen/Qwen3-4B --output_dir checkpoints_cwm_seed123/ --batch_size 2 --grad_accumulation 16 --no_wandb --seed 123 && python3 eval_cwm_baseline.py --data_dir data/ --checkpoint_dir checkpoints_cwm_seed123/best/ --model_name Qwen/Qwen3-4B --output eval_cwm_seed123.json"`
- **状态**: 正在加载 tokenizer，即将开始训练

### cls-seed0 (seetacloud cuda:1, PID 31570)
- **已运行**: 22h35m
- **进度**: step 393/1434 (27%), ~3.34s/it
- **预计剩余**: ~58min (epoch 1 of 3)

### cls-seed789 (home cuda:0, PID 2748645)
- **状态**: 已完成 (PASS)
- 进程已退出，日志末尾显示 `Per-class F1 >65%: PASS, Accuracy gap >=10pp: PASS (+37.2pp), EXIT_CODE=0`

---
