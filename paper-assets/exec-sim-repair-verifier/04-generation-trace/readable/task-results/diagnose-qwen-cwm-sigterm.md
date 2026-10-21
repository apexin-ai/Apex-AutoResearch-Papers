# diagnose qwen cwm sigterm

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_qwen-cwm-sigterm_20260520T213033_result.json`
- **Structured JSON:** [`bfa1599b20c6a60d6d89.json`](../../sessions/bf/bfa1599b20c6a60d6d89.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

---

## 诊断报告：Qwen3-8B CWM 训练 SIGTERM 分析

### 根因：tmux 服务器被杀，级联 SIGTERM

**不是** OOM、磁盘满、或容器重启。

证据链：
- 容器 uptime 155 天，无重启
- `dmesg` 无 OOM 记录
- 磁盘正常（根分区 72%，数据盘 48%）
- tmux socket 文件存在（`/tmp/tmux-0/default`，创建于 May 20 09:26），但 tmux server 进程已不存在
- 同时用 `nohup` 启动的 DeepSeek 训练（PID 949112）至今仍在正常运行
- **两个 Qwen 训练运行在 tmux session 内**，tmux server 被杀时级联 SIGTERM 同时终止了两者

tmux 被谁杀的无法确定（bash_history 无相关记录）。最可能是另一个 agent session 在管理实验时误杀了 tmux server。

### 最后成功的 checkpoint

| 实验 | 最后 checkpoint | 进度 | 保存时间 (CST) |
|------|----------------|------|----------------|
| s123 | **checkpoint-3000** | 3000/6633 步 (45.2%), epoch 1.36 | May 21 05:19 |
| s456 | **checkpoint-3000** | 3000/6633 步 (45.2%), epoch 1.36 | May 21 05:03 |

两个 checkpoint 文件完整（adapter_model.safetensors + optimizer.pt + scheduler.pt + rng_state.pth + trainer_state.json 均在）。

### 可以恢复训练

`train_unified.py` 支持 `--resume_from_checkpoint`。GPU 0 和 GPU 3 当前空闲。

**使用 `nohup` 而非 tmux 启动**，避免同类故障：

```bash
# s123 — GPU 0
cd /home/sonny/exec-sim-repair-verifier && \
CUDA_VISIBLE_DEVICES=0 HF_HUB_OFFLINE=1 nohup python train_unified.py \
  --data_dir data/ --task cwm --train_file swebench_full/swebench_train.jsonl \
  --model_name_or_path /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B/ \
  --output_dir /root/autodl-tmp/checkpoints_repo_cwm_8b_s123/ \
  --run_name repo-cwm-qwen3-8b-s123-resume \
  --seed 123 --max_seq_length 2048 --batch_size 1 --grad_accumulation 32 \
  --lr 5e-5 --epochs 3 --warmup_ratio 0.05 --no_wandb \
  --resume_from_checkpoint /root/autodl-tmp/checkpoints_repo_cwm_8b_s123/checkpoint-3000 \
  > ~/runs/exec-sim-repair-verifier/qwen3-8b-cwm-repo-s123-train-v4-resume.log 2>&1 &

# s456 — GPU 3
cd /home/sonny/exec-sim-repair-verifier && \
CUDA_VISIBLE_DEVICES=3 HF_HUB_OFFLINE=1 nohup python train_unified.py \
  --data_dir data/ --task cwm --train_file swebench_full/swebench_train.jsonl \
  --model_name_or_path /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B/ \
  --output_dir /root/autodl-tmp/checkpoints_repo_cwm_8b_s456/ \
  --run_name repo-cwm-qwen3-8b-s456-resume \
  --seed 456 --max_seq_length 2048 --batch_size 1 --grad_accumulation 32 \
  --lr 5e-5 --epochs 3 --warmup_ratio 0.05 --no_wandb \
  --resume_from_checkpoint /root/autodl-tmp/checkpoints_repo_cwm_8b_s456/checkpoint-3000 \
  > ~/runs/exec-sim-repair-verifier/qwen3-8b-cwm-repo-s456-train-v3-resume.log 2>&1 &
```

剩余约 3633 步 (~12s/step)，预计 ~12 小时完成。

---
