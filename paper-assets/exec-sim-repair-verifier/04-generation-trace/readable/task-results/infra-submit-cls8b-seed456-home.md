# infra submit cls8b seed456 home

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_submit-cls8b-seed456-home_20260512T135526_result.json`
- **Structured JSON:** [`125575dbf66227e68b86.json`](../../sessions/12/125575dbf66227e68b86.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练正常启动。

**cls8b-seed456 已提交并确认运行：**

| 项目 | 值 |
|------|-----|
| PID | 2810143 |
| Server | home-1x5090, GPU 0 |
| GPU 占用 | 17617 MiB / 32607 MiB, 94% 利用率 |
| tmux session | cls8b-seed456 |
| 模型 | `/home/sonny/projects/verifier-tts-struct-ie/models/Qwen3-8B` (15.3M/8.2B trainable, 0.19%) |
| 超参 | batch_size=2, grad_accum=16, lr=2e-4, epochs=3, seed=456 |
| 训练速度 | ~3.6s/step, 1434 steps total, 预计 ~1.4h |
| 完整命令 | `bash -c "export PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True && cd /home/sonny/exec-sim-repair-verifier && python3 train_verifier.py --data_dir data/ --model_name /home/sonny/projects/verifier-tts-struct-ie/models/Qwen3-8B --output_dir checkpoints_cls8b_seed456/ --batch_size 2 --grad_accumulation 16 --lr 2e-4 --epochs 3 --seed 456 --no_wandb && python3 eval_verifier.py --data_dir data/ --checkpoint_dir checkpoints_cls8b_seed456/best --model_name /home/sonny/projects/verifier-tts-struct-ie/models/Qwen3-8B --output eval_cls8b_seed456.json"` |

注：首次提交因 `--device cuda:0` 参数不被脚本支持而失败（EXIT_CODE=2），已移除并重新提交。GPU 选择由 `CUDA_VISIBLE_DEVICES=0` 自动处理。

---
